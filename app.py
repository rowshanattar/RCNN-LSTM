import streamlit as st
import cv2
import os
import tempfile
import numpy as np
from rolo.yolo_wrapper import YOLODetector
from rolo.rolo_sim import RoloTracker

st.title("🎯 ROLO-style Object Tracker")

# Upload video
uploaded_video = st.file_uploader("📤 Upload a video file", type=["mp4", "avi"])

# Save to Temporary File

if uploaded_video is not None:
    st.success("Video uploaded successfully!")

    # Save video to a temporary file
    temp_input = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    temp_input.write(uploaded_video.read())
    temp_input.close()

    # Temporary output file for playback and download
    temp_output = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    output_path = temp_output.name
    temp_output.close()

    # Preview original video
    st.video(temp_input.name)

    if st.button("▶️ Run Object Tracking"):
        st.text("Running YOLO + Simulated ROLO...")

        yolo = YOLODetector("yolo/yolov3.cfg", "yolo/yolov3.weights", "yolo/coco.names")
        tracker = RoloTracker()

        cap = cv2.VideoCapture(temp_input.name)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = None

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            detections = yolo.detect(frame)
            if detections:
                x, y, w, h, conf, label = detections[0]
                tracked_box = tracker.track((x, y, w, h))
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {conf:.2f}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            if out is None:
                height, width = frame.shape[:2]
                out = cv2.VideoWriter(output_path, fourcc, 20.0, (width, height))

            out.write(frame)

        cap.release()
        if out is not None:
            out.release()

        # Show result video directly
        st.success("✅ Tracking complete!")
        st.video(output_path)

        # Download button
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Tracked Video", f, file_name="tracked_output.mp4")

## Run the Demo

To run the ROLO demo, use the following command:

```bash
python -m rolo.demo
```

## Model Files
You can download the model files from [Google Drive](https://drive.google.com/drive/folders/1iwfb6mcimNVMdBjLduMPnS4NfrB-tU6O?usp=drive_link).

Note: After download the models file from yolo, put them in yolo folder

## 📁 Project Structure

<img src="project_structure.webp" alt="Project Structure" width="500"/>

.
├── Data/
│   └── video.mp4              # Input video file
│
├── rolo/
│   ├── demo.py                # Runs the ROLO object tracking demo
│   ├── rolo_sim.py            # Simulation or testing for ROLO
│   └── yolo_wrapper.py        # Wrapper to integrate YOLO with ROLO
│
├── yolo/
│   ├── file.cfg               # YOLO configuration file
│   ├── file.weights           # Pre-trained YOLO weights
│   └── coco.names             # Class labels (COCO dataset)
│
├── app.py                     # Main Streamlit app for the project
├── requirements.txt           # Required Python packages
└── README.md                  # Project documentation

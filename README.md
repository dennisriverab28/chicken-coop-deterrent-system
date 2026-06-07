# Chicken Coop Automated Deterrent System

**Course:** TTU Microcontrollers Project Lab  
**Platform:** Raspberry Pi (Python)  
**Collaborator:** Saheel Faisal

---

## Overview

An automated Raspberry Pi system that protects a chicken coop from predators. The system opens and closes the coop door automatically based on sunrise/sunset times, counts chickens using sensor combos, detects predator motion and triggers audio/physical deterrents, and logs all events to a SQLite database with a Streamlit web dashboard for monitoring.

---

## Features

| Feature | Description |
|---------|-------------|
| **Auto Door Control** | Opens/closes coop door via linear actuator + stepper motor at dawn/dusk |
| **Sunrise/Sunset Scheduling** | Fetches live sunrise/sunset times via weather API |
| **Chicken Counter** | Dual-sensor combo (IR + limit switch) counts chickens entering/leaving |
| **Motion Detection** | PIR-based predator detection triggers deterrents |
| **Audio Deterrents** | Plays random predator sounds (dog bark, wolf howl, hawk, eagle, etc.) |
| **Sprayer Deterrent** | Activates water sprayer relay on motion detection |
| **Light Deterrent** | Controls GPIO-driven light on motion trigger |
| **Event Logging** | SQLite database logs all coop events with timestamps |
| **Web Dashboard** | Streamlit dashboard showing detection logs and hourly trends |
| **Manual Override** | Manual door open/close via terminal interface |

---

## Hardware

| Component | Purpose |
|-----------|---------|
| Raspberry Pi | Main controller |
| PIR Sensor | Motion/predator detection |
| IR Sensor | Chicken entry/exit counting |
| Limit Switch | Chicken entry/exit counting (combo with IR) |
| Linear Actuator | Coop door opening/closing |
| Stepper Motor + Relay | Door mechanism |
| Water Sprayer + Relay | Deterrent sprayer |
| GPIO-driven Light | Deterrent light |
| Speaker | Audio playback for deterrent sounds |

---

## Project Structure

```
Chicken_Coop_Deterrent_System/
├── main_system.py              # Entry point — runs all modules in threads
├── top_module.py               # High-level system coordinator
├── manual_override.py          # Manual door control via terminal
│
├── sunset_sunrise_control.py   # Sunrise/sunset API integration
├── motion_sound_system.py      # PIR motion detection + audio deterrent
├── motion_light_controller.py  # PIR motion detection + light deterrent
├── sound_deterrent.py          # Sound playback controller
├── sprayer.py                  # Water sprayer relay control
│
├── relay_polarity_control.py   # Linear actuator polarity relay
├── relay_stepper_control.py    # Stepper motor via relay
├── servo_control.py            # Servo motor control
│
├── event_logger.py             # SQLite event logging
├── ir_counter_day.py           # IR sensor chicken counter (daytime)
├── limit_switch_day.py         # Limit switch chicken counter
├── STEP_TEST.py                # Stepper motor test script
├── switch_testing.py           # Switch hardware test
│
├── sounds/                     # Audio deterrent files (.mp3)
│   ├── dog_barking.mp3
│   ├── wolf-howl-6310.mp3
│   ├── hawk-78766.mp3
│   ├── an-eagle-squawking-overhead-226774.mp3
│   └── ... (11 total)
│
├── web/
│   └── dashboard.py            # Streamlit predator detection dashboard
│
├── test_*.py                   # Hardware test scripts for each subsystem
├── requirements.txt
└── README.md
```

---

## Setup & Run

### Requirements
- Raspberry Pi (any model with GPIO)
- Python 3.x
- Install dependencies:
```bash
pip install -r requirements.txt
```

### Run the Full System
```bash
python main_system.py
```
This starts three concurrent threads:
1. Auto day/night door cycle
2. Motion detection + deterrents
3. Chicken combo counter

### Manual Door Override
```bash
python manual_override.py
```

### Web Dashboard
```bash
# From the web/ directory
streamlit run web/dashboard.py
```
Displays detection logs and hourly predator trend charts from the SQLite database.

---

## How It Works

1. **Door Scheduling** — At startup, the system fetches today's sunrise/sunset times. A background thread checks every 30 seconds and opens/closes the door accordingly using a linear actuator + stepper motor.

2. **Chicken Counting** — During daytime, the system watches for a combo trigger: both an IR sensor and a limit switch must fire within 2 seconds to count as one valid chicken passing. False triggers (only one sensor) are logged as invalid.

3. **Predator Deterrence** — A PIR sensor continuously monitors for motion. On detection, the system plays a random deterrent sound (wolf, hawk, dog, etc.), activates the sprayer, and turns on the deterrent light. All events are logged with timestamps.

4. **Dashboard** — The Streamlit app reads from the SQLite database (`predator_data.db`) and renders detection logs filtered by date, plus a bar chart of detections per hour.

---

## Notes

- SQLite database files (`*.db`) are generated at runtime and are not included in the repo.
- Sound files in `sounds/` must be present on the Pi for audio deterrents to work.
- Ensure GPIO pins match your wiring before running (pins defined at the top of each module).

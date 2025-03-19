# Random Speedometer App

This project is a Python application designed to run on a Raspberry Pi Zero W 2. It generates random zeros and ones and displays the results in a 240x240 speedometer graphic window. The application can be controlled using a gamepad, allowing users to select operation durations of 1 minute, 5 minutes, or 10 minutes, as well as an exit option.

## Project Structure

```
random-speedometer-app
├── src
│   ├── main.py               # Entry point of the application
│   ├── graphics
│   │   └── speedometer.py     # Handles the speedometer graphic
│   ├── controllers
│   │   └── gamepad.py         # Manages gamepad input
│   ├── utils
│   │   └── random_generator.py  # Generates random zeros and ones
├── requirements.txt           # Lists project dependencies
├── README.md                  # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd random-speedometer-app
   ```

2. **Install dependencies:**
   Make sure you have Python installed on your Raspberry Pi. Then, install the required libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Connect the gamepad:**
   Ensure your gamepad is connected to the Raspberry Pi.

## Usage

To run the application, execute the following command in the terminal:
```bash
python src/main.py
```

Follow the on-screen instructions to select the duration of operation and start generating random bits.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
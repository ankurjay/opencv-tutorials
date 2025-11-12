# OpenCV Tutorials

This repository contains Python scripts that carry out tutorials for various modules in OpenCV. It makes use of both free `(opencv)` and non-free `(opencv_contrib)` packages, and therefore, requires compilation of OpenCV from source. A setup script is provided that handles this compilation and cleanup.

## First-Time Installation Guide


> ### Compatibility Warning
> 
> This repository has been tested and is known to work on > **Ubuntu 24.04 LTS (Noble Numbat)**. Since OpenCV is  compiled from source, the resulting compiled libraries are specific to this Linux distribution. They may **not** work on Windows, Mac OS or different Linux distributions.

1. Clone the git repository onto your machine.

```
git clone https://github.com/ankurjay/opencv-tutorials.git
```

2. Run the setup script

```
cd <your-target-directory>/opencv-tutorials

chmod +x setup.sh

./setup.sh
```

3. Wait for the script to finish. This step may take 5-30 minutes depending on your system speed. After compilation is complete, close the terminal.


4. You now have an Isolated Environment that is setup to use OpenCV!

## Using the Isolated Environment

After the initial installation is complete, you need to **activate** the environment.

Open up a new terminal and type:

```
cd <your-target-directory>/opencv-tutorials

source opencv_env/bin/activate.sh
```

You will see `(opencv_env)` appear at the start of your terminal prompt, indicating that your environment is now successfully activated.


## Running a Tutorial

Each tutorial consists of a folder with a `main.py` script, and optionally some image/video files that are used in the tutorial. Once you have an activated environment, you can run the script normally like this:

```python3 your_script_name.py```


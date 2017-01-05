# Help
Test code and notes for EV3

## Getting Started and Help

### Connect to EV3 from computer
1. Open Terminal
2. Type:

  ```bash
  ssh robot@ev3dev.local
  ```
3. Default password is `maker`

### Interactive Python
Once logged in to the EV3 you can run Python as:
```bash
python3
```

### Running Python files
If you have files on the EV3 you can run them as:
```bash
python3 file.py
```

### Running programs from Brickman

If you have a Python file on the EV3 you can run it from the Brickman menu, however the file must first be set to be executable with the `chmod` command:

```bash
chmod u+x file.py
```

### Cloning this repository onto EV3

For example, if you want to run the `speak.py` demo:

1. Connect to EV3 from computer with SSH (see above)
2. Run:

  ```bash
  git clone https://github.com/apirakw/ev3.git
  ```
3. Change into the `ev3/demo` directory:

  ```bash
  cd ev3/demo
  ```
4. Run the program:

  ```bash
  python3 speak.py
  ```

### Links and Resources
* [Python for ev3dev](https://github.com/rhempel/ev3dev-lang-python)
* [EV3python tutorial](https://sites.google.com/site/ev3python/)
* Python [API](https://python-ev3dev.readthedocs.io/en/latest/spec.html) including [Motors](https://python-ev3dev.readthedocs.io/en/latest/motors.html), [Sensors](https://python-ev3dev.readthedocs.io/en/latest/sensors.html) and [Buttons, LEDs, and Sound](https://python-ev3dev.readthedocs.io/en/latest/other.html)
* Writing using [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Examples

* demo: Simple demonstrations taken [Python ev3dev](https://github.com/rhempel/ev3dev-lang-python) and [EV3python](https://sites.google.com/site/ev3python/)

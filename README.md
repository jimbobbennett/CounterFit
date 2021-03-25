# CounterFit

[![GitHub license](https://img.shields.io/github/license/JimBobBennett/CounterFit.svg)](https://github.com/JimBobBennett/CounterFit/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/JimBobBennett/CounterFit.svg)](https://GitHub.com/JimBobBennett/CounterFit/graphs/contributors/)
[![GitHub issues](https://img.shields.io/github/issues/JimBobBennett/CounterFit.svg)](https://GitHub.com/JimBobBennett/CounterFit/issues/)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/JimBobBennett/CounterFit.svg)](https://GitHub.com/JimBobBennett/CounterFit/pull/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/JimBobBennett/CounterFit.svg?style=social&label=Watch&maxAge=2592000)](https://GitHub.com/JimBobBennett/CounterFit/watchers/)
[![GitHub forks](https://img.shields.io/github/forks/JimBobBennett/CounterFit.svg?style=social&label=Fork&maxAge=2592000)](https://GitHub.com/JimBobBennett/CounterFit/network/)
[![GitHub stars](https://img.shields.io/github/stars/JimBobBennett/CounterFit.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/JimBobBennett/CounterFit/stargazers/)

![The CounterFit logo](./images/CounterFitLogo.png)

IoT is great fun, but has a downside - hardware. You need access to a range of devices such as sensors and actuators to build your IoT projects. Sometimes you might have these devices, other times you may not - maybe you are waiting for a delivery, or parts are out of stock, or they are too expensive.

That's where this tool comes in.

## What is CounterFit

CounterFit is a tool that is designed to fake various IoT hardware components, such as LEDs, buttons, temperature sensors and the like, that you can then access from IoT device code running on your computer rather than on an IoT device. It is made of two parts:

* The CounterFit app - this is a web app run locally where you can connect fake sensors and actuators to your virtual hardware
* Shims - these are libraries that fake popular hardware APIs so you can take code that runs against well known hardware and run it against the CounterFit app.

**This project is under construction**

This project is seriously under construction! Please let me know if you want to help.

![Under development animated GIF](https://media.giphy.com/media/3o7qE1YN7aBOFPRw8E/giphy.gif)

## Installing and running the app

* Install the CounterFit app:

    ```sh
    pip install CounterFit
    ```

* Run the app:

    ```sh
    CounterFit
    ```

* The app will launch, listening for web requests on port 5000, and open a web browser for you to start adding virtual sensors and actuators to your project

### Running on a different port

To use a different port than the default 5000, set the `--port` option when you run the app:

```sh
CounterFit --port 5050
```

## Shims

The shims are designed to mimic the APIs for popular hardware components. The idea being you should be able to take code built against the shim and eventually run it on real hardware by changing the name of the package that is imported.

### Available shims

* ![Grove Shim](https://img.shields.io/badge/Platform-Python-green) [![Grove Shim](https://img.shields.io/badge/Shim-Grove-yellow)](./shims/grove/README.md) [![PyPI](https://img.shields.io/pypi/v/counterfit-shims-grove)](https://pypi.org/project/counterfit-shims-grove) [Grove Py](https://github.com/Seeed-Studio/grove.py) shims that work with the [Seeed Grove ecosystem](https://www.seeedstudio.com/category/Grove-c-1003.html).

## Samples

Check out the [samples](./samples) directory for a range of samples.

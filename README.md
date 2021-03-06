# PySpleeterGUI

![PreviewImage](docs/img/preview.png)

An interface of Spleeter project by Deezer to ease musician removing instruments from a music.
This is a simple interface for [Spleeter](https://github.com/deezer/spleeter), the [Deezer](https://www.deezer.com) source separation library with pretrained models written in Python and uses Tensorflow, as the original repository said. This is my first actual Python project, so please bear with this project's unhandled measures and not-the-best practices.

Developed using [PyQt5](https://pypi.org/project/PyQt5/), for Python 3.x on Windows.

MIT License.

# How to use
1. `git clone https://github.com/rareguy/PySpleeterGUI`
2. Move to PySpleeterGUI folder
3. `python main.py`

# Current features
##### v0.1
- It's working... partially.
- Only 1 preset available to use, `spleeter:2stems`. More in the future!
- Tested on Python 3.x on Windows. And was intended for Windows.
- Bugs and several unused feature may present, feel free to suggest some ideas.
- Requirements:
    - Read [this](https://github.com/deezer/spleeter/wiki/1.-Installation) Spleeter wiki. Make sure Spleeter is working (test it via [Quick Start](https://github.com/deezer/spleeter#quick-start) guide of Spleeter).
    - [PyQt5](https://pypi.org/project/PyQt5/). You can install it using `pip install PyQt5` command.
- Known bugs:
    - Window size is not consistent. If the filename length was more than the window, the window will stretch.
    - Console log and progress bar is not functional. I haven't figured out how to mount `stderr` of Spleeter to the built-in console log.
    - After rendering it just dies. Either it's the Spleeter is not successful on my computer or I set up the wrong implementation. It's always saying that `folder already exists` while the one that writes the output is the spleeter itself.

##### v0.1.1
- Console log is now working properly. Now to fill it in?
- Window size is consistent, but the layout isn't.
- The previous bug of `folder already exists` is fixed, somehow, by Spleeter devs?
- Known bugs:
    - If you try to render twice in one run, it might cause the program to close unexpectedly. Might, still working on what might be the cause.
    - It become not responding if the Spleeter took long enough to render the audio. I should find the responsive function of Spleeter when it's rendering. Threading, maybe?

# Future plans
- Fixing bugs from previous versions
- Adding custom training
- Custom output folder
- All-in-one dependency installer (so the program will work swiftly even though you haven't installed anything particular)
- Progress bar is not functional (how to receive progress signal from spleeter?)
- Etc. Will add more things from suggestions.

Cheers!

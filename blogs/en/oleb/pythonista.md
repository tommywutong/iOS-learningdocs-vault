---
title: Pythonista
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/07/pythonista/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d0fcad5a6e60099f'
translated: false
---

> 原文：[Pythonista](https://oleb.net/blog/2012/07/pythonista/)　·　Ole Begemann

# Pythonista

Today, my friend [Ole Zorn](https://twitter.com/olemoritz) released [Pythonista](http://omz-software.com/pythonista/) on the App Store. Pythonista can perhaps best be described as a full-fledged Python IDE for the iPad.

[![Pythonista Source Code Editor](https://oleb.net/media/pythonista-screenshot-code-editor.png)](https://oleb.net/media/pythonista-screenshot-code-editor.png)

It comes with a great source editor, complete with syntax highlighting, an extended keyboard (best feature: swipe left/right to navigate in the current line) and basic code completion for Python. The app’s built-in Python interpreter comes with the (almost) complete set of Python’s standard modules so a lot of existing Python code should work out of the box. You can either write a complete “mini-app” in the code editor and run it or explore the Python APIs from the interactive console.

Ole even wrote five new modules especially for Pythonista. These allow you to play sound, control iOS’s pasteboard, customize the interactive console and, coolest of all, write graphical mini-apps in Python, complete with touch handling and Core Animation-style layers and animations.

Pythonista includes complete documentation for the Python language, standard library and the custom extensions. The documentation browser is accessible from the code editor with a single tap. It also comes with ten examples that demonstrate the features and are a great way to learn some Python basics:

- A [Memory](https://en.wikipedia.org/wiki/Concentration_(game))-style game ([screenshot](https://oleb.net/media/pythonista-screenshot-memory.png))
- A [SameGame](https://en.wikipedia.org/wiki/Same_Game) variant ([screenshot](https://oleb.net/media/pythonista-screenshot-samegame.png))
- An analog clock ([screenshot](https://oleb.net/media/pythonista-screenshot-analog-clock.png))
- A particle generator that you can control with your fingers ([screenshot](https://oleb.net/media/pythonista-screenshot-particles.png))
- A simple multi-touch piano ([screenshot](https://oleb.net/media/pythonista-screenshot-piano.png))
- A graph plotter for mathematical functions ([screenshot](https://oleb.net/media/pythonista-screenshot-plotter.png))
- A lottery number generator ([screenshot](https://oleb.net/media/pythonista-screenshot-lottery.png))
- A variant of the [Snake](https://en.wikipedia.org/wiki/Snake_(video_game)) game ([screenshot](https://oleb.net/media/pythonista-screenshot-snake.png))
- A simple stop watch ([screenshot](https://oleb.net/media/pythonista-screenshot-stopwatch.png))
- A demo of the customization features of the interactive console ([screenshot](https://oleb.net/media/pythonista-screenshot-zen.png))

To test Pythonista out, I wrote a very simple Twitter search client today. It takes a keyword, performs a Twitter search on it and displays the most recent results. Despite the fact that I only have a very basic knowledge of Python and I have to look up pretty much every single API I use, it only took me about an hour to get [a decent result](https://oleb.net/media/pythonista-screenshot-twittersearch.png). [Download the code](https://oleb.net/media/pythonista-twitter-search.py) if you’re interested.

The app does have some limitations, of course, most of them due to the restrictions of the iOS platform. Needless to say that you can’t turn the Python apps you wrote into full-fledged iOS apps. Everything stays within Pythonista and Ole decided to forgo integrating any file-sharing functionality via Dropbox or iTunes so far [for fear of an Apple rejection](https://twitter.com/olemoritz/status/223108041078349824). So you’re currently limited to copy and paste to get code in and out of the app (unless you write a Python script that uploads itself, that is). Another thing that is currently not possible is drawing images loaded from the web but I hope that will be added in an update.

My favorite feature for the next version would be support for URL schemes that would let you run a script from via a URL (if Apple allows it). That way, apps like [Launch Center Pro](http://appcubby.com/launch-center/) could theoretically act as a hub for scripting other apps. It’s like the iOS version of Unix pipes, if you will.

Overall, I think Pythonista is a really great app. It’s truly useful if you’re at all into Python and “dynamic languages”, it’s pretty unique on iOS and it’s really well executed, too. Not to mention that playing around with it is a lot of fun. [$5/€4 on the App Store](http://itunes.apple.com/us/app/pythonista/id528579881?ls=1&mt=8).

---
title: CodeRunner
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/10/coderunner/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:36c6f7eb8901f2f9'
translated: false
---

> 原文：[CodeRunner](https://oleb.net/blog/2011/10/coderunner/)　·　Ole Begemann

# CodeRunner

One of the great things about “scripting” languages like Ruby is that almost every one of them comes with an interactive environment (for example, [IRB](https://en.wikipedia.org/wiki/Interactive_Ruby_Shell) for Ruby). Launched from the command line, these shells drop you right into a working environment of the language and there is usually no faster way to quickly test out little code snippets.

# No interactive environment for Objective-C/Cocoa

I always wanted to have something similar for Objective-C and Cocoa but the fact that Obj-C is a compiled language makes the whole thing a lot more involved: launch an editor, create a `main()` function, type the code you want to test, compile, launch the executable. And if it doesn’t work the first time, rinse and repeat. Creating a new Xcode project just to test a little code snippet always seemed like overkill, too.

I used to launch the interactive [MacRuby](http://www.macruby.org/) shell if I wanted to quickly test a snippet of Cocoa code. That worked fine but the fact that the syntax was different than Objective-C meant that I couldn’t copy and paste the code into an Obj-C project once I got it working.

# CodeRunner to the rescue

[CodeRunner](http://krillapps.com/coderunner/) is a great tool by Nikolai Krill that has solved all these issues for me. You launch it and it opens up with a pre-written `main()` function, ready for you to paste your code snippet in. Press `Cmd + R` and CodeRunner immediately compiles and runs the code (no need to save it first), showing you the log output right under the code editor in the same window. Once you are sure your code is working, simply copy and paste it back to Xcode.

![CodeRunner screenshot](https://oleb.net/media/coderunner-screenshot.png)

I use CodeRunner several times a week. Some examples where I find it especially useful:

- to work.
- Writing regular expressions and testing them against different strings.
- Parsing JSON data that I received from a web service and checking how the resulting Cocoa objects look like.

Generally speaking, it’s a great tool to play around with all aspects of [the Foundation framework](http://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/ObjC_classic/Intro/IntroFoundation.html). The only little gripe I have is that the Objective-C template still uses the GCC compiler by default. I think it’s time to switch over to LLVM/Clang. The compile script is easy to change, though.

Although I have been using it exclusively for Objective-C so far, CodeRunner works with a multitude of languages out of the box. The new version 1.1 can be configured to run any language that can be invoked from the command line.

CodeRunner costs [$4.99 on the Mac App Store](http://itunes.apple.com/us/app/coderunner/id433335799?mt=12). I highly recommend it.

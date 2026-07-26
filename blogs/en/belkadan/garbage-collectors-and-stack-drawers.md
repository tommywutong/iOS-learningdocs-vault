---
title: Garbage Collectors and Stack Drawers
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:f07b5260f507027d'
translated: false
---

> 原文：[Garbage Collectors and Stack Drawers](https://belkadan.com/blog/2009/06/Garbage-Collectors-and-Stack-Drawers/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Z shell](https://belkadan.com/blog/2009/06/Z-shell/)

[What Happened to Dockyard?](https://belkadan.com/blog/2009/07/What-Happened-to-Dockyard/) »

« [C++ Templates are Turing-Complete](https://belkadan.com/blog/2009/05/C-plus-plus-Templates-are-Turing-Complete/?tag=programming-languages)

[Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/?tag=programming-languages) »

[User-Side Troubleshooting](https://belkadan.com/blog/2011/05/User-Side-Troubleshooting/?tag=mac-os-x) »

## [Garbage Collectors and Stack Drawers](#)

This week’s post contains two short unrelated topics, one interesting and one practical.

For a while now, I’ve been casually following the birth of the [Parrot Virtual Machine](http://www.parrot.org/). Parrot’s goal is to be a general-use virtual machine for dynamic languages, most notably Perl 6 and followed by Python. (Sort of like Microsoft’s [Common Language Infrastructure](http://en.wikipedia.org/wiki/Common_Language_Infrastructure), but more dynamic and open source.) As someone interested in high-level language design, there’s a lot of cool things here…if only I knew enough Perl to write my own front-end. (You can do it in other languages too, including good old lex-yacc / flex-bison, but you lose out on some of the work they’ve done for you.)

Anyway, today on the Parrot blog there was a post about (mostly) lockless [concurrent garbage collection](http://wknight8111.blogspot.com/2009/06/concurrent-garbage-collection.html). The idea is not only pretty amazing to me, it’s also more and more applicable as parallelism becomes more and more relevant. The original technique was also published in 1998. (For context, the garbage collectors in Java and Cocoa today are already running on separate threads, and two of the “features” of the upcoming Mac OS X Snow Leopard are [Grand Central Dispatch](http://www.apple.com/macosx/technology/#grandcentral) and [OpenCL](http://www.apple.com/macosx/technology/#opencl). Parallelism is the way to go.) I haven’t yet read the technical papers linked from that post, but there’s a very clear summary there that is astounding in its simplicity. (As in, I could probably go implement the simplest one myself without reading the paper.)

Things like this are cool for two reasons: one, that such a neat hack can be done, and two, that Parrot would take care of it for me if I target that as a backend.

That wraps it up for Parrot, for now. Someday I’ll get a chance to play with it for real.

On to the next tip! If you use Leopard’s “Stacks” feature, you might get frustrated with the untidy look of your stacks in your Dock…especially if you have stacks of all folders! Fortunately, a solution’s been around for a couple of years now: wonderful [drawer icons](http://www.geocities.jp/chy065/) by Yasushi Chida. These icons are actually attached to old resource fork text clippings (what you get if you drag text to the Finder). These are cleverly (?) named with a “.app” extension to keep QuickLook away.

Installing these wonderful drawers is easy: just drag the icon you like to your stack. They’re already named with a leading space, so they’ll pop to the front of your stack if it’s sorted by Name, and they’re timestamped in the future to handle Date Created or Date Modified. (Date Added is a little trickier; I’ll summarize my solution at the end of next week’s post. I’m not just being lazy; it’s on another computer.) The problem comes when you accidentally (?) click on the drawer icon: you get the message “The application “ System ” cannot be launched.”

To fix this, I cannibalized an AppleScript application, a legitimate Mac OS X bundle application, and dropped in a simple script that pops open the enclosing folder (essentially mirroring the “Open in Finder” option at the _end_ of the list). For the icon, I used [Iconverter](http://www.versiontracker.com/dyn/moreinfo/macosx/16468) (VersionTracker link, developer’s site seems to have disappeared) to extract the icon to a Mac OS X .icns file, which I then place in the dummy application’s resources directory. (Preview can pull icons from the clipboard, but it can’t save .icns. The developer app Icon Composer can’t pull icons from the clipboard — I’m going to file a bug on this.) Here’s the source of the executable script at the core of the “application”; you can also download [the whole setup](http://belkadan.com/blog/upload/Drawer.zip) and modify it yourself.

```
#!/bin/bash

container=`dirname "$0"`
open "$container/../../.."
```

Now things work beautifully; there are no resources or outdated formats involved, and the drawer icon does something reasonable if you click on it. I don’t use stacks for much, and when I do they’re almost always in Grid view. But this makes them a lot easier to distinguish—and a lot more aesthetically pleasing as well. Now, if only you could get rid of the icon in the Grid view…

This entry was posted on [June](https://belkadan.com/blog/2009/06) 26, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Programming languages](https://belkadan.com/blog/tags/programming-languages), [Mac OS X](https://belkadan.com/blog/tags/mac-os-x)

---
title: Swift on Mac OS 9
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/'
original_language: en
published: 2020-04-01
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:bf67af605884dd51'
translated: false
---

> 原文：[Swift on Mac OS 9](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Flexible Identities in git](https://belkadan.com/blog/2020/02/Flexible-Identities-in-git/)

[Shallow Git Repositories](https://belkadan.com/blog/2020/04/Shallow-Git-Repositories/) »

« [Leaving Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=swift)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=swift) »

« [Color Palette #8](https://belkadan.com/blog/2018/01/Color-Palette-8/?tag=mac-os-classic)

[ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=mac-os-classic) »

« [So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=compilers)

[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=compilers) »

[SICPelago](https://belkadan.com/blog/2025/04/SICPelago/?tag=april-fools) »

## [Swift on Mac OS 9](#)

It’s April 1, and that means it’s both [April Fools’ Day](https://en.wikipedia.org/wiki/April_Fools'_Day) and [the anniversary of the founding of Apple Inc.](https://en.wikipedia.org/wiki/History_of_Apple_Inc.) While this year is a sober one due to [current events](https://staythefuckhome.com), I think a lot of people still appreciate what people are creating and sharing to keep spirits up, whether that be music or art or…impractical programming projects. And while _pranks_ on April Fools’ seem less and less fun[1](#fn:harder), obvious jokes and whimsy, not at anyone’s expense, are still something I believe in…and even better if they actually work.

Last year I implemented [the world’s best code visualizer](https://forums.swift.org/t/new-code-visualizer-for-swift-source-is-view/22454). This year I decided to seriously attempt something that I’d thought about in the past: getting a [Swift](https://swift.org) program to run on Mac OS 9.more

### What’s a Mac OS 9?

![](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/macos9.png)

Twenty (!) years ago, before the macOS[2](#fn:names-osx) we know today, there was another operating system known as “Mac OS”.[3](#fn:names-classic) It was one of the first OSs to use a GUI at all, something that we pretty much take for granted these days. It also dates from the days when only one program could run at a time; because of that, even the latest version uses _cooperative multitasking_ to run multiple programs—that is, a program has to yield its time to let others run.[4](#fn:MultiFinder) If a program crashed or overwrote memory it wasn’t supposed to, there was a good chance you’d have to restart the whole system.

Mac OS 9 ran on [PowerPC](https://en.wikipedia.org/wiki/PowerPC) processors, which were also used in the GameCube, PS3, _and_ Xbox 360; earlier versions of the OS had started on Motorola’s [68k](https://en.wikipedia.org/wiki/Motorola_68000_series) CPU series. Its successor Mac OS X[5](#fn:ten) also ran on PowerPC when it first launched; it wasn’t until 10.4 that Apple began to switch to Intel processors instead, and 10.6 when PowerPC was finally dropped.

Mac OS X was a huge step forward from Mac OS 9 in a number of ways, including _preemptive multitasking_ so that you could _actually_ run multiple things at once. But Apple didn’t want to just leave OS 9 programs behind, so they did two things:

- The _[Classic environment](https://en.wikipedia.org/wiki/List_of_macOS_components#Classic)_ set up a sandbox that looked enough like Mac OS 9 to run Classic Mac OS programs directly in Mac OS X. Because the Classic environment was itself an app, all the programs that ran inside it were protected from interfering with other Mac OS X programs and vice versa. It really was quite effective, and actually survived longer than booting into Mac OS 9 (which never received support for newer PowerPC processors). But its life ended with the switch to Intel-powered Macs—Classic was built on running the instructions in the original apps directly, only having to provide compatibility shims for libraries. Think of it like [Wine](https://www.winehq.org) / [CrossOver](https://www.codeweavers.com) rather than [VirtualBox](https://www.virtualbox.org) / [Parallels](https://www.parallels.com/products/desktop/).[6](#fn:Rosetta)
- _[Carbon](https://en.wikipedia.org/wiki/Carbon_(API))_ was a packaged-up version of the old Mac OS _Toolbox_ APIs so that you could write Mac OS X apps the same way you always had. You basically just recompiled your app and added an extra annotation saying you were “Carbonized”. ([Sound familiar?](https://developer.apple.com/mac-catalyst/) [7](#fn:catalyst)) Fun aside: This is the reason (one of the reasons?) [Core Foundation](https://developer.apple.com/documentation/corefoundation) exists—to [provide a common interface between Carbon and Cocoa](https://youtu.be/NTGJm2BdqSU). (h/t [Marshall Elfstrand](https://twitter.com/llahsram/status/1246118151118450690) for the video link.)

Classic ended with the switch to Intel processors back in the 2000s, but Carbon worked all the way up to last year, macOS Mojave. Apple never released a 64-bit version of Carbon, presumably to encourage developers to move to Cocoa, and with last year’s macOS Catalina, support for 32-bit apps was dropped ~~entirely~~ with very few exceptions.[8](#fn:32-bit)

### What’s the goal?

Since I learned to program on Classic Mac OS, and years later spent a good chunk of my career working on [Swift](https://swift.org), I’ve had the tantalizing thought that I’d like to **write a program in Swift and run it on Mac OS 9.** That is,

- I write Swift source code that calls Carbon / Toolbox APIs.
- I compile it for PowerPC with (a version of) the Swift compiler.
- I package it up as necessary for Mac OS 9.
- Profit!

Is this useful? No! Absolutely not! But neither was [ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/), and yet I still learned a lot doing it.

As you probably guessed, I managed to accomplish this, or I wouldn’t be writing this blog post. So, without further ado, here’s a picture of a Swift Toolbox app running on Mac OS 9.2, on my friend Nadine’s Power Mac G4. (Check out that blazing fast 400MHz processor!)

[![You can see BitPaint running in the middle, and the Classic version of Apple System Profiler showing that yes, this is Mac OS 9.2.](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/running.jpg)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/running.jpg)

I assume a good number of people reading this would like to know how to do it too!

- **If you want to build your own PPC-capable Swift compiler**, check out the following repositories:

  ```
  git clone https://belkadan.com/source/ppc-swift-project
  cd ppc-swift-project
  git clone -b ppc-swift https://belkadan.com/source/swift
  git clone -b ppc-swift https://belkadan.com/source/llvm-project
  git clone https://github.com/apple/swift-cmark cmark
  make  # quick start to build swiftc and the stripped-down stdlib
  ```

  Note the directory and branch names of the sub-repos, and note that they should be nested inside the ppc-swift-project repo. **You will also need the [`mpw`](https://github.com/ksherlock/mpw) emulator and a copy of the [Macintosh Programmer’s Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) tools[9](#fn:mpw-img)** to build an actual app using modern macOS.
- **If you want a prebuilt PPC-capable Swift toolchain**, here’s one: [ppc-swift-toolchain](https://www.dropbox.com/s/g3c6tnsg08z6zgv/ppc-swift-toolchain.zip?dl=1). Note that while I’ve put a built Swift.o in this toolchain, you’ll probably only have success with optimized code that doesn’t actually have any remaining links to the stdlib (i.e. everything is inlined away). **You will also need the [`mpw`](https://github.com/ksherlock/mpw) emulator and a copy of the [Macintosh Programmer’s Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) tools.[9](#fn:mpw-img)**

  You may still want to check out the example in the [ppc-swift-project](https://belkadan.com/source/ppc-swift-project) repo. The required flags for `swiftc`, `PPCLink`, and `Rez` can be a little finicky. (And note that the `SIZE` and `carb` resources are required for any Carbon app, so you can’t just skip the Rez part if you actually want to run your app.)

  _**UPDATE:** The [latest version](https://www.dropbox.com/s/89zw69j5rw0wli7/ppc-swift-toolchain-2023.zip?dl=1) of this toolchain (from Feb 23) *does* support linking to the stdlib and using non-optimized code. You should definitely still copy your setup from the (now multiple) examples in the project repo, though._
- **If you just want to try a built version of BitPaint**, here’s one: [BitPaint-swift.hqx](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/BitPaint-swift.hqx).

  [![(".hqx. Now that's an extension I haven't heard in a long time.")](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/obi-wan.jpg)](https://en.wikipedia.org/wiki/BinHex)

I’d like to hear about anything you make with these tools! Meanwhile, if you’d like to hear how I made this work, read on.

### Gathering materials

The last time I was building Classic Mac OS apps, I was using [CodeWarrior](https://www.macintoshrepository.org/577-codewarrior-pro-6). Actually, calling that “building Classic Mac OS apps” was a stretch; I was learning C and using CodeWarrior’s terminal I/O library to get a stdin/stdout interface that Classic Mac OS didn’t have natively. (Remember, no command line!) I could try to get some version of CodeWarrior running again, but that didn’t seem like the most convenient thing. I didn’t think I’d be able to get the Swift _compiler_ running on Classic, so I’d be shuttling object files back and forth between OSs to get anything done.

Fortunately for me, I’m not the only one interested in building Classic apps on modern macOS. At some point I found about the [`mpw`](https://github.com/ksherlock/mpw) project: an emulator specifically for running Apple’s [Macintosh Programmer’s Workshop](https://en.wikipedia.org/wiki/Macintosh_Programmer%27s_Workshop) tools. And I knew it was going to work, too, because Steve Troughton-Smith, (in)famous in the Apple community for finding undocumented and prerelease features in Apple’s OSs, had [written up his experiences](https://www.highcaffeinecontent.com/blog/20150124-MPW,-Carbon-and-building-Classic-Mac-OS-apps-in-OS-X) building an app with `mpw` that ran on System 1 all the way up to modern Mac OS X, just by building with the appropriate compiler and against the appropriate libraries.

If you’re interested in all this, I highly recommend checking out his [blog post](https://www.highcaffeinecontent.com/blog/20150124-MPW,-Carbon-and-building-Classic-Mac-OS-apps-in-OS-X). Not only was this the reference I used to get started, but the app you see running in the above picture, BitPaint, is Troughton-Smith’s test app, ported to Swift. (I did ask him ahead of time if it was okay to use his app for a hobbyist project.) Longtime Mac developer Gwynne Raskind also gave a two-part high-level tour of the Toolbox APIs on Mike Ash’s blog several years ago ([part 1](https://mikeash.com/pyblog/friday-qa-2012-01-13-the-mac-toolbox.html) | [part 2](https://mikeash.com/pyblog/the-mac-toolbox-followup.html)); fortunately, Carbon takes care of a fair amount for us even on Mac OS 9.

So okay. What does MPW give us?

- A PowerPC compiler
- A PowerPC assembler
- A PowerPC linker
- The Classic Mac OS header files
- The Classic Mac OS library stubs, for linking against
- debug mystery misbehavior

That’s pretty good; as Troughton-Smith’s blog post shows, it’s enough to build an entire app that’ll run on Classic. My idea was to take object files produced by a modern compiler and feed them to the PowerPC linker, which means I’ll additionally need:

- A modified version of the Swift compiler that supports emitting MPW-compatible object files
- Some stripped-down form of the Swift standard library and runtime (enough to read in and interact with Carbon headers, at least)
- one, but not the charger for it, and so I did most of my testing using

  SheepShaver

  . My friend Nadine provided some testing on actual machines once things were working.

And, well, that should be it! So, off we go.

### Modern compiler, classic linker

To make things more manageable, I set an intermediate goal: build an app using _Clang,_ the modern C compiler that ships with Xcode. Clang uses the same [LLVM](http://llvm.org) infrastructure as the Swift compiler, so I figured I could deal with all the object format and workflow issues in Clang, and then move on to the Swift-specific parts.

The first thing I did was try to figure out what the file format was for PowerPC object files. It turns out it’s a format called XCOFF; searching for modern documentation on this turned up an [IBM reference doc](https://www.ibm.com/support/knowledgecenter/ssw_aix_71/filesreference/XCOFF.html). Pretty much no one else uses this format, which was not encouraging. The first time I started looking into this project, I was worried I’d have to have my compiler write out assembly code and then send _that_ through the MPW PowerPC assembler…after fixing it up to account for the differences in how LLVM and MPW print PowerPC assembly.

However, when I checked to see if LLVM supported XCOFF, I was in for a stroke of luck. It turns out IBM has started adding support for XCOFF to LLVM just last year, as part of [adding support for their AIX OS](https://lists.llvm.org/pipermail/llvm-dev/2019-February/130175.html)…_which runs on PowerPC._ So I could ask Clang to generate XCOFF files for AIX, which means it should only be a short step to making it generate XCOFF files for Classic Mac OS.

At this point I remembered a bit of trivia. [Apple and IBM used to have a close partnership, along with Motorola.](https://en.wikipedia.org/wiki/AIM_alliance) They’d even made some common standards that were used across platforms and CPUs, though perhaps with less impact than they’d hoped. Was it possible that AIX and Classic Mac OS used the same calling conventions for their procedures, and they could just interoperate without any extra work?

I got lucky: the answer is (nearly) yes. The [AIX register conventions](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/assembler/idalangref_reg_use_conv.html) and [stack conventions](https://www.ibm.com/support/knowledgecenter/en/ssw_aix_72/assembler/idalangref_runtime_process.html) match up with the ones in the [Mac OS Runtime Architectures](https://developer.apple.com/library/archive/documentation/mac/pdf/MacOS_RT_Architectures.pdf) guide. That meant I could feed object files produced by Clang directly into MPW’s `PPCLink` and get a working Classic Mac OS binary out.

I’m pretty sure my mouth fell open when I first saw this work.

```
% clang -c test.c \
    -target powerpc-ibm-aix-xcoff \
    -isystem ${MPW}/Interfaces/CIncludes \
    -integrated-as \
    -fpascal-strings
% mpw PPCLink test.o ${PPC_LIBRARIES} -o Test
```

That should work with just top-of-master-branch LLVM/Clang (and a very simple test.c). I did end up needing to change LLVM in a few ways in the end, but it’s really fairly minimal, so much thanks to the IBM folks for doing the hard part of the work for me!

### Now do Swift

Being able to compile a simple test program was a great milestone, but I had to do a fair bit of work before I could get swiftc to compile a whole BitPaint. Here are some of the highlights:

- **Teach Swift about the PPC/AIX target.** This mostly involved adding `ppc` and `AIX` cases to switch statements across the Swift compiler, but also involved making a simple description of the Swift calling conventions for Clang (which I cribbed from the 32-bit ARM implementation) and then assuring the PPC/AIX backend that this was an okay calling convention to be using. I got lucky in the amount of work I had to do here because Swift already supports 32-bit ARM, little-endian 64-bit PowerPC (when running Linux), and big-endian 64-bit s390x (another IBM architecture); all the pieces were already in place.
- **Add support for Pascal strings.** The Mac’s first high-level programming language was Pascal, not C! As such, the default format for strings throughout the Toolbox APIs was _Pascal strings_ (a length byte followed by string data) rather than _C strings_ (string data followed by a null byte). With the `-fpascal-strings` command-line flag, Clang supports static Pascal strings with the syntax `"\pHello World"`. The `\p` would be replaced by the length of the string (which must be no more than 255 bytes) so that you didn’t have to count it yourself. [I hacked this into Swift as well](https://belkadan.com/source/swift/commitdiff/293d4b39ab9bbfd3f0762b6883da860e3601d373), and while my implementation probably has problems[10](#fn:utf-8), it was enough to get simple things working.
- **Turn off reflection support and nearly all runtime metadata.** The Swift runtime is very powerful, but I didn’t want to write much of a runtime for this project, which was primarily about calling a bunch of C functions. Beyond that, though, the default format for Swift metadata makes heavy use of _relative addressing_ (mainly to reduce startup time, but [learn more here](https://youtu.be/G3bpj-4tWVU)) as well as symbols pointing inside of a global, and the LLVM XCOFF implementation doesn’t (yet?) support either. So to get to a working proof-of-concept, I aggressively commented out parts of IRGen that made use of either feature. I’d like to get some of the static metadata back at some point, but reflection’s not something I’m ever interested in. Probably.
- **Make a smol stdlib.** The full Swift standard library has a _lot_ of things in it I don’t need, and some that I wouldn’t even know _how_ to implement. (What’s a String in a world that can’t assume Unicode?) But all the logic to integrate with C code is based on having some basic types in the standard library (like Int16 and UnsafeMutablePointer). What I ended up doing was taking a subset of the standard library sources, and then adding additional files and commenting things out until it worked.

  …haha, nope, even that wasn’t good enough. My early attempts at this compiled okay, but they managed to crash PPCLink when I tried to write a test program, presumably because there’s just _too many symbols_ in the standard library. So I cut things down to an even _smaller_ subset, and that (eventually) worked. Of course, I was working on this at the same time as I was modifying the compiler to get to a working proof-of-concept, so I think I ultimately went further than I needed to. (A bunch of symbols are only used for runtime metadata purposes.) As mentioned above, non-optimized builds of non-trivial programs don’t work yet, so I don’t know if I’m in the danger zone or not, but I might try to add a few more things back in.

  Rather than modify the actual Swift repo for this, I decided to keep my stripped-down standard library separate, so you can find it in the [ppc-swift-project](https://belkadan.com/source/ppc-swift-project) repo. **This might be a good reference for someone looking for a C-compatible, runtime-less subset of Swift**, perhaps for an embedded or other resource-constrained environment.
- **Disable jump tables.** LLVM optimizes switch statements into _[jump tables](https://en.wikipedia.org/wiki/Branch_table)_ when it looks like it’ll help performance and/or code size, but its default implementations of jump tables also weren’t supported in the LLVM XCOFF implementation. I imagine the AIX folks will get around to implementing this sooner or later, but for now I just disabled jump tables entirely, forcing the compiler to emit switches as a series of `if`s instead.

You can check out all the changes in the [swift](https://belkadan.com/source/swift/shortlog/refs/heads/ppc-swift) and [llvm-project](https://belkadan.com/source/llvm-project/shortlog/refs/heads/ppc-swift) repos, if you’re curious. Very few are appropriate for upstreaming to their respective projects, but I’ll try to get the ones that _are_ relevant upstreamed at some point.

### A week of mysterious failures

Having made all the changes above, I had an app that worked! In Swift!

…except, it only worked some of the time. I’d change something arbitrary and suddenly events wouldn’t register any more. It got so bad that I added a counter: after _any_ ten events, exit the app. Without that, I’d get trapped, unable to even quit without restarting the (virtual) machine. Even in a seemingly working version, my friend Nadine reported that trying to use the Reset command caused the app to crash. What was going on?

I decided I had to get to the bottom of something strange I’d seen earlier: even the _Clang_ version of the program didn’t work correctly when I turned on optimizations. It’s possible that that was a bug in IBM’s newly-added AIX support, or 32-bit PowerPC support since it’s not such a common platform, or even LLVM’s optimizations. It could be that AIX and Classic Mac OS really weren’t as similar as I thought they were, and so my code wasn’t agreeing with the system code on how things were supposed to work. And it could be that the optimized code was using an instruction that SheepShaver didn’t support, though that didn’t really seem to match the symptoms.

And the symptoms were weird. Some local variables were getting corrupted, but others weren’t. So I started testing everything I could think of:

- was the stack aligned properly?
- was the stack pointer somehow not getting restored properly?
- (see the

  Mac OS Runtime Architectures

  guide)
- was there something causing the Code Fragment Manager (dynamic linker) to put the wrong address in for cross-library calls?

Without being able to rely on logging, I made the simplest textual debug output facility I could: modifying the title of a menu. (It later turned out that writing to stdout in Mac OS 9 automatically results in a file being created, so I could have used that instead.) I wrote C functions that tracked the current stack pointer to make sure it was getting restored properly; I made good use of the `DumpXCOFF` and `DumpPEF` tools that came with MPW; I learned how PEF “pidata” (“pattern-initialized data”) worked and tried to step through CFM relocations by hand (again, see the [Mac OS Runtime Architectures](https://developer.apple.com/library/archive/documentation/mac/pdf/MacOS_RT_Architectures.pdf) guide). I even started trying to decompile some of the actual system libraries to see if they were doing anything suspicious, even though a bug in the actual Mac OS 9 seemed incredibly unlikely. This led all the way to learning about the “toolbox ROM”, which isn’t actually ROM at all: it’s a boot script and a compressed set of system libraries. (It’s called that because it’s content that _used_ to be in ROM.) Fortunately [SheepShaver already knows how to load it](https://github.com/cebix/macemu/blob/2e302d60a337daa252c6992335e6365a9beac83f/SheepShaver/src/rom_patches.cpp#L148), which meant that I could do the same decompression and then manually split out the individual libraries.

Yeah, I got way off in the weeds. I learned a lot, though!

Finally, I looked at the decompiled optimized code—the C version, not the Swift version. I observed that the variable getting corrupted was in general-purpose register 13. That’s supposed to be an okay place to put data in Classic Mac OS (and in 32-bit AIX, and in 32-bit Mac OS X), but I decided I didn’t trust that, particularly because that register had been used to track thread-local storage in 64-bit AIX. So I marked r13 as reserved…

…and the problems went away. Optimized, non-optimized, even with [`-fstack-protector-all`](https://clang.llvm.org/docs/ClangCommandLineReference.html#cmdoption-clang-fstack-protector) on. And Swift.

(Debugging this took about a week, unfortunately, which led to this project being a little less ambitious than I originally wanted.)

### “Future directions”

What didn’t I get to? An awful lot, actually.

- There’s no runtime at all, which means no dynamic allocation (among other things).
- There’s no type metadata, which means no generics (that aren’t optimized away).
- There’s no field metadata, which means no key paths (that aren’t optimized away).
- MacRoman

  as the native encoding, but it wouldn’t necessarily look much like today’s Swift.String.
- was choking on large object files. If I do get more standard library stuff working, I’ll probably split it out of the ‘Swift’ module somehow.
- linkage

  in a number of ways to make the LLVM XCOFF backend happy, so I’m not sure multi-file builds would work. I didn’t even test it.
- to work on older versions of Mac OS X as well, but my friend Nadine tried and it didn’t, and it wasn’t a priority to figure out.
- I wanted to try making nice abstractions on top of the some of the Toolbox APIs.
- I wanted to make more complicated example apps!

Maybe I’ll follow up on some of these, but I’ve been putting a lot of effort into making sure I could finish this by April 1, so I should probably get to some of the things I’ve been neglecting in favor of this project instead.

### Summary

This project took a lot of time, even though I (1) know a lot about compilers and (2) hacked my way to success instead of being careful and maintaining proper software development practices. But I learned a lot, and I accomplished a goal I’ve had in the back of my mind for a long time.

If you made it all the way to the end of the article, here’s a reward: BitPaint running under Classic on Mac OS X 10.2 (also courtesy of Nadine).

[![You can see BitPaint running in the middle, and the Classic version of Apple System Profiler...but also the Mac OS X "About This Computer" box showing 10.2.8.](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/classic.jpg)](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/classic.jpg)

Stay safe, everyone, and help the people around you when you can. And if anybody makes something with this project, I want to hear about it!

1. [“Being mean is easy, young man. Humor is harder.” – Annalee Flower Horne](https://twitter.com/LeeFlower/status/1109450357778853890) [↩︎](#fnref:harder)
2. Née OS X, née _Mac_ OS X. [↩︎](#fnref:names-osx)
3. Née “System”, as in “System 7”. The OS only got branded in Mac OS 7.6. [↩︎](#fnref:names-classic)
4. If you’re interested in hearing more about this, check out the [MultiFinder](https://en.wikipedia.org/wiki/MultiFinder) article on Wikipedia. [↩︎](#fnref:MultiFinder)
5. [Always “ten”, never “ex”.](https://twitter.com/UINT_MIN/status/790977467842301952) [↩︎](#fnref:ten)
6. Apple _did_ also make an emulator for PowerPC apps when they switched to Intel chips, called [Rosetta](https://en.wikipedia.org/wiki/Rosetta_(software)). In a way this was an even more technically impressive feat than Classic, but why couldn’t they run Classic through Rosetta? The Wikipedia article suggests that it’s because Classic required lower-level system hooks that they didn’t want to provide in Rosetta; I could also imagine it being too many layers to get good performance through, or even just Apple trying to shed the maintenance burden of a piece of software that, in general, was getting less and less use each year. [↩︎](#fnref:Rosetta)
7. While I couldn’t resist the opportunity to make a _technical_ comparison to Catalyst, I don’t think the situations are really that similar. For a Mac programmer, Carbon/Toolbox would have been the familiar API then, but for a Mac programmer, AppKit is the familiar API now, and UIKit is the newly-introduced thing. [↩︎](#fnref:catalyst)
8. “[This has made a lot of people very angry and been widely regarded as a bad move.](https://www.goodreads.com/quotes/1-the-story-so-far-in-the-beginning-the-universe-was)” The problem here isn’t just with developers needing to port their existing apps to 64-bit (or to Cocoa, if they were still on Carbon even after it stopped receiving updates); it’s a concern with older apps whose developers have no plans to update them. People are especially concerned about games, which can’t be “replaced” by a similar app that handles the same data. On the other hand, there’s a _lot_ of older code in the OS that Apple no longer has to support, which means fewer security vulnerabilities, fewer bugs, and faster development. In theory, anyway. Meanwhile, people are resorting to bizarre things like [running macOS Mojave in a virtual machine](https://appletoolbox.com/need-to-run-32-bit-apps-on-macos-catalina-use-a-mojave-virtual-machine/), which I regret to inform you totally works, mostly. [↩︎](#fnref:32-bit)
9. Actually getting MPW these days is increasingly tricky. I’m not comfortable hosting it myself, and the still-available hosting linked at the bottom of the Wikipedia page contains the tools in the form of an [HFS](https://en.wikipedia.org/wiki/Hierarchical_File_System) disk image—the disk format Apple used _before_ [HFS+](https://en.wikipedia.org/wiki/HFS_Plus), which has itself been superseded by [APFS](https://en.wikipedia.org/wiki/Apple_File_System). HFS disk images are no longer supported on macOS 10.15 Catalina, so to extract the disk image I ended up using my Mac OS 9 install and a hastily-obtained install of [Disk Copy](https://support.apple.com/kb/DL1262), which for some reason Apple still hosts. If you have a pre-Catalina machine around, that’s probably easier. [↩︎](#fnref:mpw-img) [↩︎2](#fnref:mpw-img:1)
10. Swift strings are supposed to be valid UTF-8, and I’m not sure if some part of the compiler will choke if they’re not. But if I ever have a string literal that’s longer than 127 bytes, a length byte is going to show up as part of a multibyte UTF-8 sequence rather than a single Unicode scalar. Fortunately all my test strings have been short so far.

  (Strings on Classic Mac OS were encoded as [MacRoman](https://en.wikipedia.org/wiki/Mac_OS_Roman) by default anyway, so I’d also run into this problem if I tried to, say, put a MacRoman ellipsis character in a static string.) [↩︎](#fnref:utf-8)
11. As an aside, the code for cross-library calls (“named indirect calls”) seems like it ought to be sharing logic for calls through a function pointer. That would decrease code size at the cost of one extra jump, but maybe that one extra jump has a significant impact on performance.[12](#fn:footnote) [↩︎](#fnref:indirect)
12. This post sets a record for “number of footnotes on any post I’ve written” (even without this one). It was suggested I commemmorate that with a footnote. [↩︎](#fnref:footnote)

This entry was posted on [April](https://belkadan.com/blog/2020/04) 01, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Compilers](https://belkadan.com/blog/tags/compilers), [April Fools](https://belkadan.com/blog/tags/april-fools)

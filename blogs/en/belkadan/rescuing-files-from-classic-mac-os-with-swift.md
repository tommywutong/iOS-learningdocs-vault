---
title: 'Rescuing Files From Classic Mac OS...with Swift!'
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/'
original_language: en
published: 2023-01-22
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:3b92539984918c05'
translated: false
---

> 原文：[Rescuing Files From Classic Mac OS...with Swift!](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/)

[Setting up GoToSocial](https://belkadan.com/blog/2023/02/Setting-up-GoToSocial/) »

« [ROSE-8 on Mac OS 9](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/?tag=mac-os-classic)

« [The Two Faces of Codable/Serde](https://belkadan.com/blog/2022/11/Codable-Serde/?tag=swift)

[There's No Such Thing As "Implicitly Atomic"](https://belkadan.com/blog/2023/10/Implicity-Atomic/?tag=swift) »

« [Suffusion: Playing with Filesystems](https://belkadan.com/blog/2020/07/Suffusion/?tag=filesystems)

[GitMounter](https://belkadan.com/blog/2023/11/GitMounter/?tag=filesystems) »

## [Rescuing Files From Classic Mac OS...with Swift!](#)

My winter break project was getting the files off an old PowerBook from the 90s (my dad’s old work computer) that I’ve had lying around for a while. (There’s _probably_ not anything of interest there to anyone but our family, but who knows?) I’ve looked at this before, but it’s hard to get a [25-year-old computer](https://en.wikipedia.org/wiki/PowerBook_3400c) to talk to a modern OS. I can’t compress or image the whole disk because it’s already mostly full. “Standard” file sharing protocols fall short because Classic Mac OS files are a little more complicated than just a stream of data. And I don’t want to mess with the system too much, because it’s old and I don’t want the hard disk to suddenly fail or whatever.

So I decided to just write a dead-simple one-off file transfer program that throws data over a TCP connection. I haven’t even written the decoder yet for this ad-hoc archive format; I’ve just [netcat](https://en.wikipedia.org/wiki/Netcat)-ed the whole stream into files to look at later. But the most fun part is that some of my [past](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/) [work](https://belkadan.com/blog/2020/05/ROSE-8-on-Mac-OS-9/) is paying off: I’m writing this in Swift, a modern language running on a decades-old OS.

I’ve named the project “Krypton” because it is about [getting something off a doomed substrate](https://en.wikipedia.org/wiki/Krypton_(comics)#Overview), and I guess that makes the archive format a “krypt”.

### What’s special about files on Mac OS?

These days, we’re used to files being pretty simple: they’ve got a name (usually with an extension), and they’ve got contents. If you think a little further, you might identify that files _on disk_ have some additional metadata, like permissions, or a timestamp for when the file was last modified. Classic Mac OS had this too, of course, but it also had two (well, three) additional kinds of information that were an essential part of the file: its _type_ and _creator,_ and its _resource fork._

The type and creator are both “[four-character codes](https://en.wikipedia.org/wiki/FourCC)”, four-byte values conventionally written using characters rather than numerically. This extended to compilers: Mac C compilers allowed (and still allow) multi-character literals with the syntax `'APPL'`, producing a single 32-bit integer. Of course, this depends on the character set in use; typically, this would be [MacRoman](https://en.wikipedia.org/wiki/Mac_OS_Roman). A file’s type was critical information because file names on Mac OS conventionally did not include extensions; the type code was the only indicator of what was in the file (much like how MIME types are used by web browsers). `APPL` was the type code for applications (we didn’t call them apps yet); `TEXT` was the code for plain text; `MooV` was the code for QuickTime movies, which eventually became the basis for MPEG-4.

The creator wasn’t as critical as the file type; it told the system which application to open a file with if you just double-clicked it (rather than opening it from within a running app), which also affected its icon. You’re still able to set which application to use on a per-file basis on today’s macOS; that’s a feature that goes all the way back to creator codes.

Finally, and most importantly, files had a _resource fork,_ entirely parallel to their regular contents that contained structured data in a table keyed by (again) four-character codes. For an application this included UI specification, user-visible strings (convenient for localization), and even code, at least on older systems. Documents were free to include resource info as apps saw fit; many files _only_ had resource forks, leaving the unstructured “data fork” empty.

So it’s clear that you can’t just treat a Classic Mac OS file as a single stream of bytes like you can a POSIX-style file. A variety of container formats were invented to deal with this mismatch between Macs and other computers…but I’m not using any of them, because I’m doing the _bare minimum_ to rescue the contents of the old hard drive. Instead, I implemented what a friend described as “basically [cpio](https://en.wikipedia.org/wiki/Cpio)”, throwing the file’s name, “catalog info” (basic metadata, including the type and creator codes), data fork, and resource fork across a TCP connection, to be compressed and stored on a modern OS with a much much bigger hard drive until I can get around to writing an unarchiver.

(For the record, modern macOS and APFS _still_ support resource forks and type and creator codes, if only grudgingly, using [extended attributes](https://eclecticlight.co/2017/08/14/show-me-your-metadata-extended-attributes-in-macos-sierra/). And to flip it around, a fully-preserving archive format has to support extended attributes too, at least optionally. So Classic isn’t being _that_ outlandish.)

### Swift’s Benefits

The biggest benefits of doing this project in Swift are very similar to what the benefits would have been for using C++, back in the 90s, but with even more safety. Take directory walking. In C, this looks something like the following:

```
FSIterator *iter;
OSStatus err = FSOpenIterator(&directory, kFSIterateFlat, &iter);
if (err != noErr) { return err; }
// use iter
FSCloseIterator(iter); // hopefully no early exits!
```

But in Swift, without wrapping this API at all…

```
var iter: FSIterator? = nil
try FSOpenIterator(&directory, .init(kFSIterateFlat), &iter).check()
defer { FSCloseIterator(iter) }
```

Is it shorter? Not much. Is it _nicer?_ Absolutely! First off, we have `defer` to ensure no resources are leaked even if there’s an early-exit later in the function. But it’s that throwing `check()` method that really changes the game.

```
extension OSStatus { // available on all Int32, not ideal, but worth it
  func check(file: StaticString = #file, line: Int = #line) throws {
    if self != noErr {
      throw MacError(self, file: file, line: line)
    }
  }
}
```

C-style error codes, transformed into Swift’s [propagating errors](https://belkadan.com/blog/2021/12/Swift-Delight-Try/), and capturing the file and line of the operation to boot. Easier to use _and_ more information preserved! You’d have to write a macro to do this in C, and rewrite all your functions to handle error results as well as their normal return values.

We haven’t done a chapter on Errors in the [Swift Runtime](https://belkadan.com/blog/tags/swift-runtime/) series^[1](#fn:series), but I’ll quickly lay it out here: Swift errors are implemented as heap allocations containing the original type metadata, the conformance to Error, and the value, inline. This is very much like the usual representation of `any Foo` save for the part where it’s _always_ on the heap. The reason for that is twofold: first, so that the representation can be compatible with the Objective-C class NSError on Apple platforms, and second, so that the type `Error?` fits in a register, and the code can check whether an error was thrown by comparing against `nil`. Only some platforms actually _do_ this; the rest “just” have an out-parameter that would essentially be `Error **` in C.^[2](#fn:alloc) So the `check()` method here _is_ less efficient than just returning error codes…but only really in the failure case, and even then not that much.

### Tribulations

It wouldn’t be a “Swift on Classic” post without some weird bugs. I tried to avoid the worst of them by testing in [SheepShaver](https://sheepshaver.cebix.net) first, as I had done with previous projects. But when I went to run my program on the actual laptop, it froze the whole machine.

Now, this is unfortunately a reasonably common failure mode on Classic. Applications were cooperatively scheduled, so if one hangs, everything stops, and if one _really_ messes up, it’ll take down the OS with it. Somehow I was “really messing up”. But I couldn’t see why.

Well, when you’re up a creek with only print-debugging for a paddle, sometimes you have to take things slow. And heavy-handedly. I commented out more and more of my code until I found the problem, which was…a very simple library call? That I was definitely using correctly? And that wouldn’t be using any fancy Swift features?

Okay. What are the differences between my SheepShaver environment and the real one? SheepShaver is running Mac OS 9. The laptop is running…Mac OS 8.6. Aha! Maybe the API I’m using isn’t available on 8.6? But I’m not loading it from the OS, I’m loading it from CarbonLib, which is supposed to support this kind of backwards-deployment.

(I gave [an explanation of Carbon](https://belkadan.com/blog/2020/04/Swift-on-Mac-OS-9/#whats-a-mac-osnbsp9) in the first post in the series, so I’m not going to repeat it here.)

Well…it _could_ be a bug in CarbonLib. In fact, CarbonLib had multiple versions. Did the PowerBook have the latest one? It turns out it didn’t! So after getting the latest from [Macintosh Garden](https://macintoshgarden.org), I tried again. This time, the call didn’t freeze the computer. But it did still fail, with a very generic error. Was I going to have to rewrite my whole program to use older APIs? The documentation says this should be working…

Finally I got lucky, noticing a snippet of an article from around that time that said the “new APIs” should work on Mac OS 8 on any HFS+ drive. Surely, surely this laptop was using HFS+, a hard drive format released with Mac OS 8.1 (over a year before 8.6). Modern macOS can’t even _read_ the original HFS anymore.

But that was it. The drive was HFS, or “Mac OS Standard”. It didn’t support Unicode, it didn’t support more than 65536 different files per disk^[3](#fn:size), and it didn’t support filenames longer than 31 characters. And it didn’t support the new file system APIs. So I did, in the end, have to rewrite my code, though I kept the other version around too. (In case I have to do this again on a slightly newer computer? I dunno.)

I’m still tickled that I solved my problem with, essentially, a software update.

### Roads not taken

When I mentioned this project to my (non-programmer) cousin, she said, “And you can’t just copy it onto a USB drive or whatever?” And, well…this laptop predates USB, but the basic idea is sound. I already had to get a new power adapter, so I totally could have gotten an external hard drive with a [SCSI](https://en.wikipedia.org/wiki/SCSI) port^[4](#fn:scsi) and a SCSI-to-USB adapter. Or possibly even just gotten the adapter, and started up the laptop in “target disk mode” where it just acts like one big external hard drive itself. But I’m a software person, so I got hung up on software solutions.

The other possibility is that I could have better trusted the software of the time. Remember I said there were various container formats to deal with Mac files being Different? Many Mac file transfer programs understood that, and automatically encoded files into one of those containers when transferring to another machine (either to preserve the information on a non-Mac, or so the Mac on the other side could immediately decode it). I probably could have gotten one of those programs working too.

But whatever, it was a fun project. Even if I have so many other projects I could be doing…

### Wrapping up

Like I said, I may have gotten data off the old PowerBook, but I haven’t actually decoded it yet. (I _hope_ I didn’t miss anything…) Still, it felt great to use my just-for-kicks between-jobs vanity project from 2020 to actually do some useful work…and I really do think doing it in Swift was easier than doing it in C would have been.

You can find the code for this project in the examples section of my [ppc-swift-project repo](https://belkadan.com/source/ppc-swift-project/).

EDIT: And here’s the [latest built ppc-swift toolchain](https://www.dropbox.com/s/89zw69j5rw0wli7/ppc-swift-toolchain-2023.zip?dl=1), so you don’t have to build it yourself. It’s still a Swift 5.3-dev, though, so no fancy Swift features from the last few years.

![](https://belkadan.com/blog/2023/01/Rescuing-Files-with-Swift//laptop)

1. What happened to this much-beloved series? [RSI](https://belkadan.com/blog/2021/07/Keyboard-Pants/). These days, most of my blog posts are first written on my phone, where thumb-typing uses a different set of muscles from the keyboarding I do all week for work. But the Swift Runtime series requires constantly referencing the source code while I’m writing, as well as lots of diagrams and reformatting and such that aren’t just linear text. As such, I haven’t been able to work on them on my phone, and so the project remains on indefinite hold. I do still hope to pick it up again some day, but clearly I am not in a place to make promises. [↩︎](#fnref:series)
2. This _does_ mean that throwing an error in Swift requires memory allocation. An alternate strategy would be to pass down the address of a fixed-size buffer used for the error if it’s small enough, basically `inout any Foo?`. But this would be slightly slower to test the results after a call, at least on the platforms with a dedicated error register, and that’s something Swift wanted to make fast. It also makes conversion between Error and NSError simpler on platforms where that matters, and then it’s easier if the implementations aren’t drastically different across platforms. [↩︎](#fnref:alloc)
3. Which has another interesting consequence: as disks got larger, the _smallest possible non-empty file_ also gets larger. On the PowerBook I was rescuing files from, the smallest possible file was 46KB, meaning the disk must have been about 3GB. For comparison, most modern filesystems support file allocations as small as 4KB (including HFS+), and some even have a special case for _very_ small files to store the contents alongside the metadata. [↩︎](#fnref:size)
4. Pronounced “scuzzy”, though supposedly one of the original designers wanted it to be pronounced “sexy” and nobody took them up on it. [↩︎](#fnref:scsi)

This entry was posted on [January](https://belkadan.com/blog/2023/01) 22, [2023](https://belkadan.com/blog/2023) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Mac OS Classic](https://belkadan.com/blog/tags/mac-os-classic), [Swift](https://belkadan.com/blog/tags/swift), [Filesystems](https://belkadan.com/blog/tags/filesystems)

---
title: ROSE-8
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2020/01/ROSE-8/'
original_language: en
published: 2020-01-13
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4516739b8fc96db1'
translated: false
---

> 原文：[ROSE-8](https://belkadan.com/blog/2020/01/ROSE-8/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/)

[Setting up gitweb on Shared Hosting](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting/) »

« [So You Want to Be a (Compiler) Wizard](https://belkadan.com/blog/2016/05/So-You-Want-To-Be-A-Compiler-Wizard/?tag=assembly)

[ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=assembly) »

« [quasiquarantine](https://belkadan.com/blog/2019/12/Quasiquarantine/?tag=source-code)

[ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=source-code) »

[ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=rose-8) »

## [ROSE-8](#)

_or, “How I put too much time into making an 8-bit ISA and accompanying virtual machine”_

It all started with my colleague Cassie [having fun designing a toy 8-bit ISA](https://twitter.com/porglezomp/status/1215183514427174912) (“instruction set architecture”). I love encoding tables (I helped out a little with the one for [Swift’s `String` struct representation](https://github.com/apple/swift/blob/master/stdlib/public/core/StringObject.swift)), and I did [assignments in college](http://inst.eecs.berkeley.edu/~cs61cl/fa08/project/asm/asmproject.html) involving simplified CPUs. So I started thinking about what it would be like to write a program in Cassie’s ISA…and decided its four registers were too limited for me. How could I get up to 8 registers while still keeping most of the instructions in a single byte?

That was the start of the project I named ROSE-8: a toy instruction set for a non-existent CPU with 8-bit registers and 32[KiB](https://en.wikipedia.org/wiki/Kibibyte) of memory. Over the last several days I’ve been coming up with the pieces you need for such a little computer, deciding on the best way to encode them as “ROSE-8 machine code”, and then actually implementing it as a toy VM. You can feed code into the ROSE-8 and it will do things!

```
let printFromLastSegment: [Instruction] = [
  .geti(-1), // GET the Immediate value -1 (255)
  .set1,     // SET the data1 segment to 'it'
  .zero,     // get the value 0 (special encoding)
  .setr(.r0) // SET Register r0 to 'it'
  // LoaD the byte at data1[r0], then Update r0 by incrementing
  .ld1u(.r0, update: true),
  .bezi(5),  // Branch if 'it' (the byte) is Equal to Zero,
             // to the Immediate offset 5 bytes forward
             // (This will be the STOP)
  .prnt,     // PRiNT 'it' (otherwise)
  .jofi(-4), // Jump to the OFfset (Immediate) 4 bytes backward
             // (This will be the LD1U)
  .stop      // self-explanatory :-)
]

var machine = Machine()
machine.load(printFromLastSegment)
machine.load("Hello World!\n".utf8, atSegment: 255)
machine.run()
```

_Sorry for not making this blog post accessible to a general programming audience. If anyone has a good recommendation for an intro to CPU architecture, I’ll link it here!_

If you want to play around with what I have, you can [download](https://belkadan.com/blog/2020/01/ROSE-8/ROSE-8.tar.bz2) it as a Swift package. There’s a bit more documentation in there, as well as a version of the discussion below. I also previously uploaded [a near-final version of the “spec”](https://pastebin.com/5Ngnsr9c) if you just want to see the instructions and their encodings.

**EDIT:** I forgot to explicitly thank Cassie for their input, suggestions, and conversation, not to mention the idea in the first place. Thank you, Cassie!

**EDIT 2:** I continued the development of ROSE-8 and projects built on top of it. The most up-to-date source is [now available on this site](https://belkadan.com/source/ROSE-8/), and there’s [a tag for all related blog posts](https://belkadan.com/blog/tags/rose-8/).

### A Detour: On GitHub

Normally with a project like this, I’d be posting it on GitHub, both to make it easy for people to browse around the source and to make it easy to track changes (and possibly even take pull requests). But unfortunately, GitHub’s taken a contract from ICE, which is a pretty heinous thing to do these days. They’re hardly the only tech company involved with ICE (as if that makes it better, “there is no ethical consumption under capitalism” and all that), but back in December I signed an [open letter](https://github.com/drop-ice/dear-github-2.0) to GitHub asking them to “commit to a higher ethical standard” in this and in the future. Until they cancel their ICE contract, [I’m not putting any new projects on GitHub](https://twitter.com/UINT_MIN/status/1203485775318241281).

(Why not GitLab or Bitbucket? Well, [GitLab’s not _immediately_ a problem, but I don’t have much faith](https://www.theregister.co.uk/2019/10/17/gitlab_reverse_ferret/). Bitbucket is owned by Atlassian, an Australian company, so I probably wouldn’t have _this_ problem with them, but…at this point I’m feeling burned, and not inclined to make my project’s canonical home be somewhere else at all. It’s certainly a testament to GitHub’s success though that its competitors don’t seem nearly as compelling.)

Anyway, you get archive drops from me instead, at least for now. I did still leave the git repository inside the archive, but I didn’t start tracking revisions till partway into the project (bad me), so the history isn’t as interesting as it might be.

**EDIT:** [I set up my own hosting instead.](https://belkadan.com/blog/2020/01/Gitweb-on-Shared-Hosting)

### Further Background

So, how _do_ you get up to 8 registers while still keeping most of the instructions in a single (8-bit) byte? The answer I chose has actually been around for a long time: make a special register called an _accumulator._ In some architectures, that means giving one regular register special privileges, including the [Intel 8080](https://en.wikipedia.org/wiki/Intel_8080) that’s an ancestor of most modern desktops. But I chose to make the accumulator be its own thing, colloquially called “it”. This name comes from programming environments that use this to reference the last thing you accessed; the oldest one I’ve used is [HyperTalk](https://twitter.com/UINT_MIN/status/774071210590113792) and I’ve seen from [LOLCODE](https://github.com/justinmeza/lolcode-spec/blob/master/v1.2/lolcode-spec-v1.2.md#if-then) that it’s reasonable to have this be part of how you program.

With the accumulator as the implicit target of most operations, it was “easy” to have eight registers available and still have room for a large number of operations. I took some other hints from Cassie’s ISA, like the compact encoding for bitstring immediate operations based on the intuition that adding or subtracting large numbers known at compile-time isn’t very common.

The next big challenge was memory. ([Cassie realized this too.](https://twitter.com/porglezomp/status/1215184390344626177)) With 8-bit registers, you’d only be able to address 256 bytes of memory, which…isn’t a ton. I took another hint from old Intel machines by using [segment registers](https://en.wikipedia.org/wiki/X86_memory_segmentation): accessing address 0x55 means something different based on which segment you’re accessing it in. Around this point I also realized this felt pretty familiar…

…and realized that the last 8-bit machine I heard about was the Game Boy, via Eevee’s series about [writing a Game Boy Color game](https://eev.ee/blog/2018/06/19/cheezball-rising-a-new-game-boy-color-game/), which I very much enjoyed / am enjoying. With that consciously realized, I got to check what I was doing against [the list of Game Boy opcodes](http://gameboy.mongenel.com/dmg/opcodes.html) (provided by Randy Mongenel) to make sure I wasn’t ~~making any stupid mistakes~~ making any mistakes that Nintendo hadn’t, at least not accidentally.

The last “clever bit” of this architecture is how to do function calls. If you want more than 256 bytes of _code,_ some of it is going to be too far away to refer to with an 8-bit register. It’s the segment problem again! So there’s a “code” segment for “normal” function calls…but since that means a fair amount of overhead getting too and from a far-away function, there’s _also_ support for “offset” function calls. Encoding jumps by offset (from the current instruction) is pretty standard practice for jumping around _in_ a function, but unusual for calls, because the thing you’re calling has to know how to get back. I’m still not sure if I think this is worth it, but I haven’t really written enough big or even medium-sized programs to know yet.

### Future Projects?

- An assembler/interpreter, i.e. running from a text file (and outputting to a binary file, I guess). Writing arrays of instructions by hand (as shown above) isn’t so bad _except_ for manually computing addresses and offsets, so I still want to get to this at some point.
- Memory-mapped I/O, so that it’s possible to implement something Game-Boy-like with buttons and maybe a “screen”.
- I’m not building a compiler that targets ROSE-8 but someone could, in theory.

This entry was posted on [January](https://belkadan.com/blog/2020/01) 13, [2020](https://belkadan.com/blog/2020) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Source code](https://belkadan.com/blog/tags/source-code), [ROSE-8](https://belkadan.com/blog/tags/rose-8)

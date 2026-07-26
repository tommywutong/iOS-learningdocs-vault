---
title: Relative References in ARM64 Disassembly
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/05/ARM64-Relative-References/'
original_language: en
published: 2022-05-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a18fc978ffae5c96'
translated: false
---

> 原文：[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/)

[Swift was always going to be part of the OS](https://belkadan.com/blog/2022/10/Swift-in-the-OS/) »

« [ROSE-8: Console Mode](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=assembly)

« [gdba](https://belkadan.com/blog/2011/06/Gdba/?tag=debugging)

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

## [Relative References in ARM64 Disassembly](#)

POV: You are a compiler targeting arm64^[1](#fn:arm64), and you want some code to reference this global variable from the same library. The classic way to do this is to emit an instruction that loads “the address of X”, which will be [determined at run time by the dynamic loader](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/). But that’s not super efficient! For one thing, addresses are 64 bits long, and instructions are only 32 bits, so you can either break it up into multiple instructions, or load the address from some _other_ location. But more importantly, the global variable is _in the same library._ The dynamic loader isn’t going to break it up from this code^[2](#fn:ios), and if we knew _how far away it was_ we could reference it that way.

That’s what the `adrp` instruction’s for. In real life, the code was a call to `objc_msgSend`, and the global was the selector^[3](#fn:selector). And rather than reference this variable by symbol, the compiler had emitted a [relative reference](https://duriansoftware.com/joe/optimizing-global-constant-data-structures-using-relative-references) using `adrp`.

Which made it hard to figure out what the selector _was_ when all I had was the disassembly.

```
; code is made up but resembles the real thing
; don't worry about the bold/colors just yet
[0xcd23c] mov x1, x3            ; load the target parameter from x3
[0xcd240] adrp x8, 2347         ; ???
[0xcd244] ldr x2, [x8, #0x208]  ; load the selector from ???
[0xcd248] bl 0x3f04             ; symbol stub for: objc_msgSend
```

So how does this work? [ARM’s site documents `adrp`](https://developer.arm.com/documentation/dui0802/b/A64-General-Instructions/ADRP) as follows:

> Address of 4KB page at a PC-relative offset.
> 
> ```
> ADRP  Xd, label
> ```
> 
> `label`: Is the program label whose 4KB page address is to be calculated. An offset from the page address of this instruction, in the range ±4GB.

(underlining added)

I didn’t understand what this meant at first, and had to search around a bit more to figure out what it meant…especially because I didn’t have a label anymore! This was disassembly! But eventually I understood that the argument represents an offset _in pages_ (4[KiB](https://en.wikipedia.org/wiki/Kibibyte) units) from the start of _this_ page (the page that the `adrp` instruction is on). To do this computation by hand, we take the address of the `adrp` instruction and _drop the last three hex digits,_ because 4Ki is 0x1000. Then we add the offset given as the argument to `adrp`, in units of 4Ki/0x1000. Finally, we add the offset in `ldr` to get the address of the global.

```
0xcd000 + 2347 * 0x1000 + 0x208 = 0x9f8208
```

I don’t know why LLDB’s disassembler uses hex for `ldr` offsets but decimal for `adrp` offsets, but it doesn’t really matter.

At this point we have an address; if we load it we get a [`SEL`](https://developer.apple.com/documentation/objectivec/sel). In practice a `SEL` is a C string containing the selector name, but that’s not guaranteed, and also when I did this at work I didn’t even think of that. Instead, I asked LLDB to tell me what symbol corresponded to this address (after ensuring that debug symbols were loaded).

```
(lldb) image lookup --address '0xcd000 + 2347 * 0x1000 + 0x208'
      Address: FooKit[0x00000000009f8208] (FooKit.__DATA.__objc_selrefs + 8)
      Summary: "description"
```

And there you go. It does work the other way, as well:

```
(lldb) x '*(char **)(0xcd000 + 2347 * 0x1000 + 0x208)'
0x00007e88: 64 65 73 63 72 69 70 74 69 6f 6e 00 72 65 73 70  description.resp
0x00007e98: 6f 6e 64 73 54 6f 53 65 6c 65 63 74 6f 72 3a 00  ondsToSelector:.
```

You can see that the data for the next selector, `respondsToSelector:`, is packed in right after.

(And then I decided to write this up, because it took some trial and error to understand and then actually put into practice.)

1. Specifically, you are an Apple Swift compiler, so you call it “arm64” instead of “aarch64” like ARM wishes you would. [↩︎](#fnref:arm64)
2. Some systems do not make this guarantee, the most interesting modern one being [WebAssembly](https://forums.swift.org/t/wasm-support/16087/39). But iOS-on-arm64 does. [↩︎](#fnref:ios)
3. Specifically, an implicit `SEL` variable generated by the compiler, necessary because [the ObjC support in dyld deduplicates selectors across the process when a library is loaded](https://github.com/apple-opensource/dyld/blob/master/dyld3/shared-cache/OptimizerObjC.cpp#L1152). [↩︎](#fnref:selector)

This entry was posted on [May](https://belkadan.com/blog/2022/05) 14, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Assembly](https://belkadan.com/blog/tags/assembly), [Debugging](https://belkadan.com/blog/tags/debugging), [Objective-C](https://belkadan.com/blog/tags/objective-c)

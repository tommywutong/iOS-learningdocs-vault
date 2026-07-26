---
title: ARM64 反汇编中的相对引用
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/05/ARM64-Relative-References/'
original_language: en
published: 2022-05-14
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:a18fc978ffae5c96'
translated: true
---

> 原文：[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [默认参数与基于标签的重载](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/)

[Swift 从来就注定会成为操作系统的一部分](https://belkadan.com/blog/2022/10/Swift-in-the-OS/) »

« [ROSE-8：控制台模式](https://belkadan.com/blog/2020/01/ROSE-8-Console/?tag=assembly)

« [gdba](https://belkadan.com/blog/2011/06/Gdba/?tag=debugging)

« [Objective-Rust](https://belkadan.com/blog/2020/08/Objective-Rust/?tag=objective-c)

## [ARM64 反汇编中的相对引用](#)

设想一下：你是一个面向 arm64^[1](#fn:arm64) 的编译器，想让某段代码引用同一个库里的这个全局变量。经典做法是发出一条加载"X 的地址"的指令，这个地址会[在运行时由动态加载器决定](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)。但这样做效率并不高！一方面，地址长度是 64 位，而指令只有 32 位，所以你要么把它拆成多条指令，要么从别的位置加载这个地址。但更重要的是，这个全局变量_就在同一个库里_。动态加载器不会把它从这段代码里拆开^[2](#fn:ios)，如果我们知道_它相距多远_，就能用这种方式来引用它。

这正是 `adrp` 指令的用途。在实际场景里，这段代码是对 `objc_msgSend` 的调用，那个全局变量就是选择器（selector）^[3](#fn:selector)。编译器没有按符号来引用这个变量，而是用 `adrp` 发出了一个[相对引用](https://duriansoftware.com/joe/optimizing-global-constant-data-structures-using-relative-references)。

这就让我很难只凭反汇编搞清楚这个选择器到底_是_什么。

```
; code is made up but resembles the real thing
; don't worry about the bold/colors just yet
[0xcd23c] mov x1, x3            ; load the target parameter from x3
[0xcd240] adrp x8, 2347         ; ???
[0xcd244] ldr x2, [x8, #0x208]  ; load the selector from ???
[0xcd248] bl 0x3f04             ; symbol stub for: objc_msgSend
```

那这到底是怎么回事呢？[ARM 的官网是这样描述 `adrp` 的](https://developer.arm.com/documentation/dui0802/b/A64-General-Instructions/ADRP)：

> 相对 PC 偏移处的 4KB 页地址。
> 
> ```
> ADRP  Xd, label
> ```
> 
> `label`：要计算其 4KB 页地址的那个程序标签。相对本指令所在页地址的偏移量，取值范围 ±4GB。

(下划线是我加的)

我一开始没看懂这段话是什么意思，不得不多查了一些资料才弄明白……尤其是因为我手头根本没有 label 了！这可是反汇编啊！但最终我搞懂了：这个参数表示的是一个以_页（page）_为单位（4[KiB](https://en.wikipedia.org/wiki/Kibibyte)）、从_当前_页（也就是 `adrp` 指令所在的那一页）起始的偏移量。要手算这个地址，我们取 `adrp` 指令的地址，然后_去掉最后三位十六进制数字，_因为 4Ki 正好是 0x1000。接着把 `adrp` 参数里给出的偏移量（单位是 4Ki/0x1000）加上去。最后，再加上 `ldr` 里的偏移量，就得到了这个全局变量的地址。

```
0xcd000 + 2347 * 0x1000 + 0x208 = 0x9f8208
```

我不知道为什么 LLDB 的反汇编器给 `ldr` 的偏移量用十六进制，给 `adrp` 的偏移量却用十进制，不过这其实无关紧要。

到这一步我们已经有了一个地址；如果加载它，得到的是一个 [`SEL`](https://developer.apple.com/documentation/objectivec/sel)。实际上 `SEL` 是一个包含选择器名称的 C 字符串，但这一点并没有保证，而且我当时在工作中做这件事时压根没想到这一点。于是，我改为让 LLDB 告诉我这个地址对应的是哪个符号（在确保调试符号已经加载之后）。

```
(lldb) image lookup --address '0xcd000 + 2347 * 0x1000 + 0x208'
      Address: FooKit[0x00000000009f8208] (FooKit.__DATA.__objc_selrefs + 8)
      Summary: "description"
```

就是这样。反过来也同样管用：

```
(lldb) x '*(char **)(0xcd000 + 2347 * 0x1000 + 0x208)'
0x00007e88: 64 65 73 63 72 69 70 74 69 6f 6e 00 72 65 73 70  description.resp
0x00007e98: 6f 6e 64 73 54 6f 53 65 6c 65 63 74 6f 72 3a 00  ondsToSelector:.
```

可以看到，紧挨着后面打包的正是下一个选择器 `respondsToSelector:` 的数据。

（后来我决定把这些写下来，因为从弄懂到真正上手实践，期间经历了不少试错。）

1. 准确地说，你是一个 Apple 的 Swift 编译器，所以你把它叫做"arm64"，而不是像 ARM 希望的那样叫"aarch64"。 [↩︎](#fnref:arm64)
2. 有些系统并不提供这种保证，现代系统里最有意思的例子是 [WebAssembly](https://forums.swift.org/t/wasm-support/16087/39)。但运行在 arm64 上的 iOS 是提供这种保证的。 [↩︎](#fnref:ios)
3. 准确地说，是编译器生成的一个隐式 `SEL` 变量，之所以需要它，是因为[加载库时，dyld 里对 ObjC 的支持会在整个进程范围内对选择器去重](https://github.com/apple-opensource/dyld/blob/master/dyld3/shared-cache/OptimizerObjC.cpp#L1152)。 [↩︎](#fnref:selector)

本文发表于 [五月](https://belkadan.com/blog/2022/05) 14 日, [2022](https://belkadan.com/blog/2022)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[汇编](https://belkadan.com/blog/tags/assembly)、[调试](https://belkadan.com/blog/tags/debugging)、[Objective-C](https://belkadan.com/blog/tags/objective-c)

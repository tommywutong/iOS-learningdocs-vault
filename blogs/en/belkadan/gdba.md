---
title: gdba
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2011/06/Gdba/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2ede441ac36f5949'
translated: false
---

> 原文：[gdba](https://belkadan.com/blog/2011/06/Gdba/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Chrome vs. Safari](https://belkadan.com/blog/2011/06/Chrome-vs-Safari/)

[Dealing with "Sandwich Code"](https://belkadan.com/blog/2011/06/Sandwich-Code/) »

[Relative References in ARM64 Disassembly](https://belkadan.com/blog/2022/05/ARM64-Relative-References/?tag=debugging) »

## [gdba](#)

Just wanted to share a quick hint for GDB users. When you want to debug a program that takes command-line arguments, the “traditional” way looks something like this:

```
% gdb a.out
GNU gdb 6.3.50-20050815...

(gdb) set args x y z
(gdb) run
```

But you can do even better. GDB itself has the command-line flag `--args`, which means that the rest of the arguments go to the program you’re debugging!

```
% gdb --args a.out x y z
```

I found this so useful that I made `gdba` an alias for `gdb --args`.

```
% alias gdba='gdb --args'
```

Bonus tip: if your project uses `make`, you can remake your executable from inside GDB and re-run, without even using the `shell` command.

```
(gdb) make
(gdb) run
```

Haven’t tried [LLDB](http://lldb.llvm.org/) yet, but hoping it gets there. GDB still locks up whenever I accidentally use tab-completion on a big project. I should just disable that.

This entry was posted on [June](https://belkadan.com/blog/2011/06) 05, [2011](https://belkadan.com/blog/2011) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Debugging](https://belkadan.com/blog/tags/debugging), [GDB](https://belkadan.com/blog/tags/gdb)

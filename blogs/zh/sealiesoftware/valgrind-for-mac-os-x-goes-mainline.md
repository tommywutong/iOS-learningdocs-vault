---
title: Mac OS X 版 Valgrind 并入主线
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html'
original_language: en
published: 2009-06-03
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8a81c94fd367074f'
translated: true
---

> 原文：[Mac OS X 版 Valgrind 并入主线](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **博客**  
 [最近](http://sealiesoftware.com/blog/index.html)  
 [归档](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **项目**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium 归档

\<\< [[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 篇](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：单态派发](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html)

**Mac OS X 版 Valgrind 并入主线** ([2009-06-03 7:20 PM](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html))

多亏了 Nicholas Nethercote 和 Julian Seward 的英勇工作，Valgrind 的 Mac OS X 移植版[现已并入 Valgrind 的主干](http://blog.mozilla.com/nnethercote/2009/05/28/mac-os-x-now-supported-on-the-valgrind-trunk/)。这是朝着支持 Mac OS X 的官方 [Valgrind](http://valgrind.org) 发行版迈出的重要一步。

对于手上有 [Snow Leopard](http://www.apple.com/macosx/snowleopard/) 种子版的各位，Valgrind 目前还不能用。Valgrind 运作在内核 / Libc 接口那些底层且不被官方支持的内部机制之上。一旦内核和 Libc 发生变化，Valgrind 就得跟着适配，否则就没法用了。Snow Leopard 版 Valgrind 支持最早也要等到 Snow Leopard 内核和 Libc 开源之后才可能出现，而这本身又不会早于 Snow Leopard 自己发布。

[Sealie Software](http://sealiesoftware.com/index.html)

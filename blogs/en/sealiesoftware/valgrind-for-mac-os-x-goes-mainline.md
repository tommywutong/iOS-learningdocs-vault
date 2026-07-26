---
title: Valgrind for Mac OS X goes mainline
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html'
original_language: en
published: 2009-06-03
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:8a81c94fd367074f'
translated: false
---

> 原文：[Valgrind for Mac OS X goes mainline](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html)　·　Hamster Emporium (Greg Parker)

[![](http://sealiesoftware.com/hamster.jpg)](http://sealiesoftware.com/blog/index.html)  
  
 **blog**  
 [recent](http://sealiesoftware.com/blog/index.html)  
 [archive](http://sealiesoftware.com/blog/archive/index.html)  
 [twitter](http://twitter.com/gparker)  
   
 **projects**  
 [Mac OS X](http://www.apple.com/macosx/)  
 [Keyboard](http://sealiesoftware.com/keyboard/index.html)  
 [backlight](http://sealiesoftware.com/keyboard/index.html)  
 [CSC Menu](http://sealiesoftware.com/cscmenu/index.html)  
 [Valgrind](http://sealiesoftware.com/valgrind/index.html)  
 [Fringe Player](http://sealiesoftware.com/fringe/index.html)  
 [pssh](http://sealiesoftware.com/pssh/index.html)  
 [Peal](http://sealiesoftware.com/peal/index.html)  
 [Frankenmouse](http://sealiesoftware.com/frankenmouse/index.html)

## Hamster Emporium archive

\<\< [[objc explain]: So you crashed in objc_msgSend(): iPhone Edition](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: Monomorphic dispatch](http://sealiesoftware.com/blog/archive/2009/05/14/objc_explain_Monomorphic_dispatch.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html)

**Valgrind for Mac OS X goes mainline** ([2009-06-03 7:20 PM](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html))

Thanks to the heroic work of Nicholas Nethercote and Julian Seward, the Mac OS X port of Valgrind is [now available on Valgrind's trunk](http://blog.mozilla.com/nnethercote/2009/05/28/mac-os-x-now-supported-on-the-valgrind-trunk/). This is a big step forward towards an official [Valgrind](http://valgrind.org) release with Mac OS X support.

For those of you with [Snow Leopard](http://www.apple.com/macosx/snowleopard/) seeds, Valgrind won't work. Valgrind operates at the low-level unsupported guts of the kernel/Libc interface. When the kernel and Libc change, Valgrind needs to adapt or die. Valgrind support for Snow Leopard will not be available until the open-source release of Snow Leopard's kernel and Libc at the earliest, which in turn is not before Snow Leopard itself ships.

Sealie Software

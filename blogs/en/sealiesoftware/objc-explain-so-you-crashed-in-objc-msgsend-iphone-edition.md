---
title: '[objc explain]: So you crashed in objc_msgSend(): iPhone Edition'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html'
original_language: en
published: 2009-06-08
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:18454c25c39b384e'
translated: false
---

> 原文：[[objc explain]: So you crashed in objc_msgSend(): iPhone Edition](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: Thread-local garbage collection](http://sealiesoftware.com/blog/archive/2009/08/28/objc_explain_Thread-local_garbage_collection.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Valgrind for Mac OS X goes mainline](http://sealiesoftware.com/blog/archive/2009/06/03/Valgrind_for_Mac_OS_X_goes_mainline.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html)

**[objc explain]: So you crashed in objc_msgSend(): iPhone Edition** ([2009-06-08 11:40 PM](http://sealiesoftware.com/blog/archive/2009/06/08/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_Edition.html))

[So you crashed in objc_msgSend()](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html) has been updated with register usage for iPhone's ARM processor. The table now looks like this:

|  | `receiver` | `SEL` | `receiver` | `SEL` |
|---|---|---|---|---|
| i386 | eax* | ecx | eax* | ecx |
| x86_64 | rdi | rsi | rsi | rdx |
| ppc | r3 | r4 | r4 | r5 |
| ppc64 | r3 | r4 | r4 | r5 |
| arm | r0 | r1 | r1 | r2 |

Sealie Software

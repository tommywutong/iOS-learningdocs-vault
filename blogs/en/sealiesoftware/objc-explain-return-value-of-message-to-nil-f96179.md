---
title: '[objc explain]: return value of message to nil'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html'
original_language: en
published: 2007-04-21
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:1a4d023372966de4'
translated: false
---

> 原文：[[objc explain]: return value of message to nil](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: Exceptions and autorelease pools](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Reboot](http://sealiesoftware.com/blog/archive/2007/4/21/Reboot.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html)

**[objc explain]: return value of message to nil** ([2007-4-21 3:01 AM](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html))

**Updated: [return value of message to nil](http://sealiesoftware.com/blog/325904.html)**

Ints up to 64 bits: 0  
 Pointers: nil  
 Structs: undefined  
 Float, double, long double: 0.0 on i386; 0.0 on ppc 10.5 and later; undefined on ppc 10.4 and earlier

**Updated: [return value of message to nil](http://sealiesoftware.com/blog/325904.html)**

Sealie Software

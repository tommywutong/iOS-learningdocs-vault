---
title: '[objc explain]: return value of message to nil'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html'
original_language: en
published: 2012-02-29
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:60827a21090d8f06'
translated: false
---

> 原文：[[objc explain]: return value of message to nil](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: So you crashed in objc_msgSend(): iPhone 5s Edition](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]: objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html)

**[objc explain]: return value of message to nil** ([2012-2-29 2:40 PM](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html))

#### LLVM Compiler 3.0 (Xcode 4.2) or later

Integers up to 64 bits: 0  
 Floating-point up to `long double`: 0.0  
 Pointers: `nil`  
 Structs: `{0}`  
 Any `_Complex` type: `{0, 0}`

#### Notes

C++ objects returned by value are initialized to `{0}`, even if the type has a default constructor that does something else. This may be fixed in the future.  
 Struct return is undefined if you call `objc_msgSend_stret()` directly.  
 Struct return is undefined if you use an older compiler.  
 Floating-point return is undefined on Mac OS X 10.4 and earlier on Power PC.  
 `_Complex long double` return is undefined if you use an older compiler.

[Sealie Software](http://sealiesoftware.com/index.html)

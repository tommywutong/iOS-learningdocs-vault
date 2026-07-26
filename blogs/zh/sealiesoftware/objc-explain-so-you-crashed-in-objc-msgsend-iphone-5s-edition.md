---
title: '[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 5s 篇'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html'
original_language: en
published: 2013-09-12
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:8a21cdfe2a386566'
translated: true
---

> 原文：[[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 5s 篇](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：非指针 isa](http://sealiesoftware.com/blog/archive/2013/09/24/objc_explain_Non-pointer_isa.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：发给 nil 的消息的返回值](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html)

**[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 5s 篇** ([2013-09-12 12:45 PM](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html))

[你在 objc_msgSend() 里崩溃了](http://sealiesoftware.com/blog/archive/2008/09/22/objc_explain_So_you_crashed_in_objc_msgSend.html) 一文已经更新，加入了 iPhone 5s 的 ARM64 处理器的寄存器使用情况。现在那张表看起来是这样的：

|  | `receiver` | `SEL` | `receiver` | `SEL` |
|---|---|---|---|---|
| i386 | eax* | ecx | eax* | ecx |
| x86_64 | rdi | rsi | rsi | rdx |
| ppc | r3 | r4 | r4 | r5 |
| ppc64 | r3 | r4 | r4 | r5 |
| arm | r0 | r1 | r1 | r2 |
| arm64 | x0 | x1 | — | — |

[Sealie Software](http://sealiesoftware.com/index.html)

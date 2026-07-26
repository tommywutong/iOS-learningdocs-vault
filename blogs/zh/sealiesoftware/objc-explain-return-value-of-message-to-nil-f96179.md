---
title: '[objc explain]：发给 nil 的消息的返回值'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html'
original_language: en
published: 2007-04-21
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:1a4d023372966de4'
translated: true
---

> 原文：[[objc explain]：发给 nil 的消息的返回值](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：异常与自动释放池](http://sealiesoftware.com/blog/archive/2008/09/16/objc_explain_Exceptions_and_autorelease_pools.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [重启](http://sealiesoftware.com/blog/archive/2007/4/21/Reboot.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html)

**[objc explain]：发给 nil 的消息的返回值** ([2007-4-21 3:01 AM](http://sealiesoftware.com/blog/archive/2007/4/21/objc_explain_return_value_of_message_to_nil.html))

**更新：[发给 nil 的消息的返回值](http://sealiesoftware.com/blog/325904.html)**

不超过 64 位的整数：0  
 指针：nil  
 struct：未定义  
 float、double、long double：在 i386 上是 0.0；在 10.5 及更新的 ppc 上是 0.0；在 10.4 及更早的 ppc 上未定义

**更新：[发给 nil 的消息的返回值](http://sealiesoftware.com/blog/325904.html)**

[Sealie Software](http://sealiesoftware.com/index.html)

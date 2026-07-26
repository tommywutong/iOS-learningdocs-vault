---
title: '[objc explain]：发给 nil 的消息的返回值'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html'
original_language: en
published: 2012-02-29
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:60827a21090d8f06'
translated: true
---

> 原文：[[objc explain]：发给 nil 的消息的返回值](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：你在 objc_msgSend() 里崩溃了：iPhone 5s 篇](http://sealiesoftware.com/blog/archive/2013/09/12/objc_explain_So_you_crashed_in_objc_msgSend_iPhone_5s_Edition.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [[objc explain]：objc_msgSend_vtable](http://sealiesoftware.com/blog/archive/2011/06/17/objc_explain_objc_msgSend_vtable.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html)

**[objc explain]：发给 nil 的消息的返回值** ([2012-2-29 2:40 PM](http://sealiesoftware.com/blog/archive/2012/2/29/objc_explain_return_value_of_message_to_nil.html))

#### LLVM Compiler 3.0（Xcode 4.2）或更新版本

不超过 64 位的整数：0  
 不超过 `long double` 的浮点数：0.0  
 指针：`nil`  
 struct：`{0}`  
 任意 `_Complex` 类型：`{0, 0}`

#### 说明

按值返回的 C++ 对象会被初始化为 `{0}`，哪怕该类型有一个行为不同的默认构造函数也是如此。这一点未来可能会被修正。  
 如果你直接调用 `objc_msgSend_stret()`，struct 的返回值是未定义的。  
 如果你使用更老的编译器，struct 的返回值是未定义的。  
 在 Mac OS X 10.4 及更早版本的 Power PC 上，浮点数的返回值是未定义的。  
 如果你使用更老的编译器，`_Complex long double` 的返回值是未定义的。

[Sealie Software](http://sealiesoftware.com/index.html)

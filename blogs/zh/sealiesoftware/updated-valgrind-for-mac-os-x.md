---
title: '更新：Mac OS X 版 Valgrind'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html'
original_language: en
published: 2008-10-27
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:86a01df61304700d'
translated: true
---

> 原文：[更新：Mac OS X 版 Valgrind](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]：objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [空间就是时间：你的计算机理论课骗了你](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html)

**更新：Mac OS X 版 Valgrind** ([2008-10-27 5:47 PM](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html))

修复了读取调试信息时启动阶段的一处挂起问题。

valgrind-opensource-3 与 valgrind-opensource-4 之间的全部差异就是：

```
    -#if !defined(VGO_DARWIN)
    +#if !defined(VGO_darwin)
```

哎呀！

[Sealie Software](http://sealiesoftware.com/index.html)

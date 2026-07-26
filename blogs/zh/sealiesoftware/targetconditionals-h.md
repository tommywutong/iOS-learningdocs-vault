---
title: TargetConditionals.h 速查表
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html'
original_language: en
published: 2010-08-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:16cc7cd18fe74d4d'
translated: true
---

> 原文：[TargetConditionals.h 速查表](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [诊断工程系的 Gregory Parker 博士](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html) | [归档](http://sealiesoftware.com/blog/archive/index.html) | [自己动手实现 Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html) \>\>

[![(链接)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html)

**TargetConditionals.h** ([2010-8-16 2:30 PM](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html))

更新于 2017-2-27

| TARGET_OS_OSX | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|
| TARGET_OS_IOS | 0 | 1 | 1 | 0 | 0 | 0 | 0 |
| TARGET_OS_TV | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
| TARGET_OS_WATCH | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| TARGET_OS_SIMULATOR | 0 | 0 | 1 | 0 | 1 | 0 | 1 |
|  |  |  |  |  |  |  |  |
| TARGET_OS_MAC | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| TARGET_OS_IPHONE | 0 | 1 | 1 | 1 | 1 | 1 | 1 |
| TARGET_OS_EMBEDDED | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| TARGET_IPHONE_SIMULATOR | 与 TARGET_OS_SIMULATOR 相同 |  |  |  |  |  |  |

[Sealie Software](http://sealiesoftware.com/index.html)

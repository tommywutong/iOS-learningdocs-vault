---
title: TargetConditionals.h
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html'
original_language: en
published: 2010-08-16
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:16cc7cd18fe74d4d'
translated: false
---

> 原文：[TargetConditionals.h](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [Dr. Gregory Parker, Department of Diagnostic Engineering](http://sealiesoftware.com/blog/archive/2010/09/01/Dr_Gregory_Parker_Department_of_Diagnostic_Engineering.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Do-it-yourself Objective-C weak import](http://sealiesoftware.com/blog/archive/2010/4/8/Do-it-yourself_Objective-C_weak_import.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html)

**TargetConditionals.h** ([2010-8-16 2:30 PM](http://sealiesoftware.com/blog/archive/2010/8/16/TargetConditionalsh.html))

Updated 2017-2-27

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
| TARGET_IPHONE_SIMULATOR | same as TARGET_OS_SIMULATOR |  |  |  |  |  |  |

Sealie Software

---
title: 'updated: Valgrind for Mac OS X'
source: Hamster Emporium (Greg Parker)
source_key: sealiesoftware
source_url: 'http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html'
original_language: en
published: 2008-10-27
status: frozen
license: 未声明 → 保守视为保留所有权利，仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:86a01df61304700d'
translated: false
---

> 原文：[updated: Valgrind for Mac OS X](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html)　·　Hamster Emporium (Greg Parker)

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

\<\< [[objc explain]: objc_msgSend_stret](http://sealiesoftware.com/blog/archive/2008/10/30/objc_explain_objc_msgSend_stret.html) | [archive](http://sealiesoftware.com/blog/archive/index.html) | [Space is time: how your CS theory class lied to you](http://sealiesoftware.com/blog/archive/2008/10/14/Space_is_time_how_your_CS_theory_class_lied_to_you.html) \>\>

[![(link)](http://sealiesoftware.com/link.gif)](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html)

**updated: Valgrind for Mac OS X** ([2008-10-27 5:47 PM](http://sealiesoftware.com/blog/archive/2008/10/27/updated_Valgrind_for_Mac_OS_X.html))

Update for [Valgrind for Mac OS X](http://sealiesoftware.com/valgrind/index.html): fixes a hang at launch when reading debug info.

The entire difference between valgrind-opensource-3 and valgrind-opensource-4 is:

```
    -#if !defined(VGO_DARWIN)
    +#if !defined(VGO_darwin)
```

D'oh!

[Sealie Software](http://sealiesoftware.com/index.html)

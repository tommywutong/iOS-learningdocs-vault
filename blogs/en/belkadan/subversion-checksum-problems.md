---
title: Subversion Checksum Problems
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2009/03/Subversion-Checksum-Problems/'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:130cce6a944ccd29'
translated: false
---

> 原文：[Subversion Checksum Problems](https://belkadan.com/blog/2009/03/Subversion-Checksum-Problems/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [JavaScript Tetris](https://belkadan.com/blog/2009/03/JavaScript-Tetris/)

[Categories and +load](https://belkadan.com/blog/2009/03/Categories-and-load/) »

## [Subversion Checksum Problems](#)

OK, so I didn’t quite make this up in one week, but I’ll keep trying. Here’s a tip for SVN users who get the dreaded “checksum mismatch” (usually by entirely replacing a file instead of editing it or something, actually I’m not quite sure what the exact cause is). There are already a couple workarounds on the Internet, but this one’s pretty clean.

1. `cp `_`theFile`_` `_`theFile.bak`_  
   Save your changes.
2. `svn info `_`theFile`_` | grep "Last Changed Rev"`  
   This is the last time the file changed in the repository; say it’s something like 6207.
3. `svn update -r`_`620`**`6`**_` `_`theFile`_  
   Rollback the file to the previous version, in this case 6206.
4. `svn update `_`theFile`_  
   Restore the most recent version of the file. (I’m not sure if this step is purely necessary, but it doesn’t hurt.) This should fix the checksum.
5. `mv `_`theFile.bak`_` `_`theFile`_  
   Move the changed file back, and…
6. `svn commit`

If you don’t use SVN, sorry, this post is not for you. Something more interesting next week, perhaps?

This entry was posted on [March](https://belkadan.com/blog/2009/03) 15, [2009](https://belkadan.com/blog/2009) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Subversion](https://belkadan.com/blog/tags/subversion)

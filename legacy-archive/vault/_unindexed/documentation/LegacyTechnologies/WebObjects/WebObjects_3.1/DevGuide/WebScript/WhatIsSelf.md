---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/WhatIsSelf.html
archived_at: '2026-07-15T07:48:08.421973Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](WritingOwnMethods.md)

# What is self?

In WebScript, __self__ is available in every method. It refers to the object ( the WOApplication object, the WOSession object, or the WOComponent object) associated with a script. When you send a message to __self__, you're telling the object associated with the script to perform a method that's implemented in the script. For example, suppose you have a script that implements the method __giveMeARaise__. From another method in the same script you could invoke __giveMeARaise__ as follows:

```
[self giveMeARaise];
```

This tells the WOApplication, WOSession, or WOComponent object associated with the script to perform its __giveMeARaise__ method.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](Categories.md)

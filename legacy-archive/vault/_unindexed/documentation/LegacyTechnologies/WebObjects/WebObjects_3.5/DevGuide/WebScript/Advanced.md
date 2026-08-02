---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/WebScript/Advanced.html
archived_at: '2026-07-15T07:52:28.600658Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.md) [!Previous Section](ModernSyntax.md)

# Advanced WebScript

In WebScript, you create subclasses of WOComponent, WOSession, and WOApplication and you use declared variables of classes defined in the Foundation Framework, Enterprise Objects Framework, or the WebObjects Framework. For most WebScript applications, this is sufficient.
Sometimes, however, you might want to subclass some other class or at least extend the behavior of that class without having to resort to compiled code. For these cases, WebScript allows you to do two things: create a _scripted class_, which is a scripted subclass of anything other than WOApplication, WOSession, or WOComponent; or create a _category_, which is a way to extend the behavior of a class without subclassing it.

[!Table of Contents](WebScript.md) [!Next Section](ScriptedClasses.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

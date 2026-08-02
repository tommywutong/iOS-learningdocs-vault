---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/WebScript15.html
archived_at: '2026-07-15T08:06:29.174321Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](The%20WebScript%20Language.md) [!Previous Section](WebScript14.md)

# Advanced WebScript

In WebScript, you create subclasses of WOComponent, WOSession, WOApplication, and WODirectAction and you use declared variables of classes defined in the Foundation Framework, Enterprise Objects Framework, or the WebObjects Framework. For most WebScript applications, this is sufficient.
Sometimes, however, you might want to subclass some other class or at least extend the behavior of that class without having to resort to compiled code. For these cases, WebScript allows you to do two things: create a _scripted class_, which is a scripted subclass of anything other than WOApplication, WOSession, WOComponent, or WODirectAction; or create a _category_, which is a way to extend the behavior of a class without subclassing it.

[!Table of Contents](The%20WebScript%20Language.md) [!Next Section](WebScript16.md)

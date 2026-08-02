---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Deciding.html
archived_at: '2026-07-15T07:48:15.506314Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](compiled.book.md)

# Deciding to use compiled code

Most WebObjects applications are written entirely in WebScript. However, you might decide that it's better to use compiled code instead. The primary reasons you use compiled code are:

- To boost performance
- To provide your own custom subclasses

You also might want to provide a compiled subclass of one or more of the classes in the WebObjects Framework. You can subclass the WebObjects classes WOApplication (WebApplication in Java), WOSession (WebSession in Java), and WOComponent (Component in Java) simply by creating a script file. For example, writing methods in __Application.wos__ is the same as subclassing WOApplication. Creating a component is the same as subclassing WOComponent. Usually, the only reason you would create a compiled subclass as opposed to a scripted subclass is to improve performance.
If you write compiled code in Java, the entire application must be written in Java, including the component logic. If you use Objective-C, you can mix Objective-C and WebScript. That is, you can provide part of the application's logic as compiled Objective-C objects, and the rest of the application can be left in WebScript. You can also mix C and C++ code with Objective-C. See the section "[Notes for Objective-C Developers](ObjCNotes.md#apple-heztk)" later in this chapter.

__Note:__  Java support is only available on the Windows NT platform.

[!Table of Contents](compiled.book.md) [!Next Section](SetUp.md)

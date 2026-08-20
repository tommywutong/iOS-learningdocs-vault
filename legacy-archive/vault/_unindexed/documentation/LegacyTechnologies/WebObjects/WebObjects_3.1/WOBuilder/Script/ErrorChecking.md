---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/WOBuilder/Script/ErrorChecking.html
archived_at: '2026-07-15T07:50:58.556853Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Script.book.md)
[!Previous Section](DeleteMethods.md)

Error Checking

# Error Checking

If you make a syntax error when writing a method, WebObjects Builder displays a message box describing the error when you try to close the script window or to save the component.

!

As further error checking, you can use the Check Consistency command to verify that the component's elements are bound to variables and methods that actually exist in the script file.

Select the component you want to check.

Choose Tools->Check Consistency.

!

The Check Consistency command also tells you if it detects a method that is declared but is not bound to anything. This is not necessarily an error---for example, you would never bind __awake__ or __sleep__ to any element in a component, but these two methods are used. They are invoked at the beginning and end of each request-response loop.

[!Table of Contents](Script.book.md)
[!Next Section](SetStylePreference.md)

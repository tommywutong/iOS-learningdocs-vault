---
title: Scripting Bridge Programming Guide
apple_id: TP40006104
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptingBridgeConcepts/Introduction/Introduction.html
archived_at: '2026-07-15T07:18:54.585175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](About%20Scripting%20Bridge.md)

# Introduction to Scripting Bridge Programming Guide for Cocoa

Introduced in OS X v10.5, Scripting Bridge is a framework and a technology that makes it much easier for Cocoa developers to control and communicate with scriptable applications. Instead of incorporating AppleScript scripts in your application or dealing with the complexities of sending and handling Apple events, you can simply send Objective-C messages to an object that represents an application with a scripting interface. Your Cocoa application can do anything an AppleScript script can, but it does so in Objective-C code that is integrated with the rest of your project’s code.

The current version of Scripting Bridge has some limitations that are described in [About Scripting Bridge](About%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqmznknlts).

This guide has the following chapters:

- [About Scripting Bridge](About%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqmznknlts) describes what Scripting Bridge does and how it does it, and highlights the advantages it brings to Cocoa application development. It also gives an overview of Scripting Bridge classes and methods.
- [Using Scripting Bridge](Using%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltc) explains how to prepare your project for Scripting Bridge, how to obtain instances of scriptable applications, how to get and set object properties, how to add objects to a scriptable application, and how best to manipulate element arrays.
- [Improving the Performance of Scripting Bridge Code](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnrnknltc) discusses ways in which you can make your Scripting Bridge code more efficient.

The following documents cover concepts and technologies related to Scripting Bridge:

- _[AppleScript Overview](../../Apple%20Script/AppleScript%20Overview/Introduction%20to%20AppleScript%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tm2i)_
- _[Cocoa Scripting Guide](../Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_
- _[Ruby and Python Programming Topics for Mac](../Ruby%20and%20Python%20Programming%20Topics%20for%20Mac/Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dsmzw)_
[Next](About%20Scripting%20Bridge.md)


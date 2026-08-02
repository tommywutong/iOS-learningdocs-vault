---
title: Pasteboard Programming Topics for Cocoa
apple_id: 10000068i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2009-01-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CopyandPaste/CopyandPaste.html
archived_at: '2026-07-15T07:13:55.444179Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Pasteboard%20Fundamentals.md)

# Introduction to Pasteboards Programming Topics

You typically use pasteboards in copy and paste operations, although pasteboards also provide the basis of system services (see [System Services](../Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)). `NSPasteboard` objects transfer data to and from the pasteboard server. The server is shared by all running applications. It contains data that the user has cut or copied, as well as other data that one application wants to transfer to another. `NSPasteboard` objects are an application’s sole interface to the server and to all pasteboard operations.

You should read this document to learn how to implement copy and paste in your application, and to learn about the different types of pasteboard

This document contains the following articles:

- [Pasteboard Fundamentals](Pasteboard%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjufvjvomi) explains how pasteboards work.
- [Implementing Copy and Paste](Implementing%20Copy%20and%20Paste.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjvfvjvomi) explains the basics of implementing copy and paste in your application.
- [Named Pasteboards](Named%20Pasteboards.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqzdqlkciffessscivda) discusses the ability to name pasteboards to reflect their function and the data they contain.
- [Data Types](Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqzdslkcineuuskkifdq) discusses the variety of data that can be placed on pasteboards.
- [Reading and Writing Font Data](Reading%20and%20Writing%20Font%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denjwfvjvomi) describes how to work with fonts.
- [Reading and Writing RTFD Data](Reading%20and%20Writing%20RTFD%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqgqztelkcineuirkkjfaq) describes how to work with RTFD data.
- [Filter Services](Filter%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dmlkcijbuorkdiraq) discusses the ability of pasteboards to convert data from one type to another using filter services.
- [Providing a Filter Service](Providing%20a%20Filter%20Service.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dolkcijbuorkdiraq) describes how to create a filter service.

[Next](Pasteboard%20Fundamentals.md)


---
title: AppSandboxLoginItemXPCDemo
apple_id: DTS40012292
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: null
published: '2012-06-09'
source_url: https://developer.apple.com/library/archive/samplecode/AppSandboxLoginItemXPCDemo/Introduction/Intro.html
archived_at: '2026-07-18T03:01:07.584216Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AppSandboxLoginItemXPCDemo

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2012-06-09 Updated to reflect current best practices. Specifically, replaced NSOperationQueue with dispatch_async() and srandomdev() with arc4random(). |
| __Build Requirements:__ | OS X 10.8 or later, Xcode 4.4 or later |
| __Runtime Requirements:__ | OS X 10.8 or later |

This sample project shows how to use NSXPCConnection to communicate between an AppSandboxed app and its associated login item. After launching, the user will get a window with a text input field in which they can enter questions for which a yes/no response is warranted. The application then passes these questions to a login item that responds with an entertaining answer to the question. This sample is intended to demonstrate the mechanics of interprocess communication between AppSandboxed processes.

[Next](ReadMe.txt.md)


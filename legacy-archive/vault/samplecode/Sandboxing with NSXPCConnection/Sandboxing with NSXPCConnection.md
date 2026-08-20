---
title: Sandboxing with NSXPCConnection
apple_id: DTS40012665
resource_type: Sample Code
platform: macOS
topic: Security
technology: Foundation
published: '2012-08-21'
source_url: https://developer.apple.com/library/archive/samplecode/SandboxingAndNSXPCConnection/Introduction/Intro.html
archived_at: '2026-07-18T03:23:08.073283Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Sandboxing with NSXPCConnection

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2012-08-21 Illustrates Sandboxing and Interprocess Communication using NSXPCConnection. |
| __Build Requirements:__ | Xcode 4.4 or later, OS X v10.8 or later. |
| __Runtime Requirements:__ | OS X v10.8 or later. |

"SandboxingAndNSXPCConnection" shows how the security concept of least privilege separation can be implemented using App Sandboxing and XPC interprocess communication (IPC). The goal of least privilege separation is to reduce the amount of code that runs with special privileges. This is achieved in this sample code by splitting the application into separate processes, each with the least amount of privilege necessary to complete its job. This sample uses NSXPCConnection, which allows you to use your own objects and interfaces when communicating between processes in your application.

[Next](ReadMe.txt.md)


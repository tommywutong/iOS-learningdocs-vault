---
title: AppleScriptRunner
apple_id: DTS10003441
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-31'
source_url: https://developer.apple.com/library/archive/samplecode/AppleScriptRunner/Introduction/Intro.html
archived_at: '2026-07-18T03:01:10.010170Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.c.md)

# AppleScriptRunner

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2006-07-31 Updated to produce a universal binary. No code changes were required. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnbugewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X 10.3 |

Embedding and executing AppleScripts within your application bundle allows you to quickly add functionality to your application without changing any code which otherwise becomes very complicated.
AppleScriptRunner contains a folder within its application bundle, "AppleScripts" which contains a number of customizable AppleScripts. The selected AppleScript is executed while passing it a Text parameter. How do you send email from your application? AppleScriptRunner allows you to send email by running the enclosed "Mail" AppleScript. How do you add Text-To-Speech? Just call the enclosed "Speak" AppleScript.
By packaging up functionality into AppleScripts called by an application it could allow users to create their own customizable alerts/events, extend the behavior of the main application, package functionality into components, and more.

[Next](main.c.md)


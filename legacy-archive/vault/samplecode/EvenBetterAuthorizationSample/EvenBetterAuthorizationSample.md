---
title: EvenBetterAuthorizationSample
apple_id: DTS40013768
resource_type: Sample Code
platform: macOS
topic: Security
technology: Security
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/EvenBetterAuthorizationSample/Introduction/Intro.html
archived_at: '2026-07-18T03:07:51.509596Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](App-Sandboxed-AppDelegate.h.md)

# EvenBetterAuthorizationSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2013-09-17 Shows how to factor an application's privileged operations into a privileged helper tool run by launchd. |
| __Build Requirements:__ | Xcode 4.6.3 |
| __Runtime Requirements:__ | OS X 10.8 |

EvenBetterAuthorizationSample shows how to factor privileged operations out of your application and into a privileged helper tool that is run by launchd. It uses modern technology—namely SMJobBless, introduced in 10.6, and NSXPCConnection, introduced in 10.8—to radically reduce the code needed to support privileged helper tools as compared to older samples. You should study this sample if your application needs ongoing access to privileged operations. For example, if you're writing a packet capture tool (where the underlying technology, BPF, is only available to a privileged process) and you want to make it available to users in a controlled and configurable fashion (determined by an authorization right), EvenBetterAuthorizationSample is for you.

[Next](App-Sandboxed-AppDelegate.h.md)


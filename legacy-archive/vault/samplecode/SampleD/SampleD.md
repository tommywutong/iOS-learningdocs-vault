---
title: SampleD
apple_id: DTS10003653
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2005-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/SampleD/Introduction/Intro.html
archived_at: '2026-07-18T03:22:58.820066Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](client.pl.md)

# SampleD

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-10-27 Updated to produce a universal binary. No code changes were required. Separately, updated comments and code flow to improve readability and consistency. |
| __Build Requirements:__ | Mac OS X 10.4, Xcode 2.1, gcc 4.0 |
| __Runtime Requirements:__ | Mac OS X 10.4 or greater |

SampleD consists of two programs designed to demonstrate the use of the Apple System Logger (ASL) API as well as the basic construction and behavior of a launchd daemon.
"SampleD" is a basic launchd daemon that, when instantiated by launchd, will listen on a socket indefinitely. Launchd takes care of registering the socket before the daemon is even launched, so all this code needs to do is accept any incoming connections and then write a message to them. This code also demonstrates how to use Apple System Logger APIs to construct and issue well formatted logging information to the syslogd server.
"Report" is a program that demonstrates the use of ASL to query the syslogd server for log messages created by the SampleD daemon.

[Next](client.pl.md)


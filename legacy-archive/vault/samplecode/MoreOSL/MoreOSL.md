---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Introduction/Intro.html
archived_at: '2026-07-18T03:15:50.384061Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MIBCarbon.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreOSL

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 C library for implementing AppleScript support within your application. |
| __Build Requirements:__ | n/a |
| __Runtime Requirements:__ | Carbon |

MoreOSL, or MOSL for short, is a source code library for implementing AppleScript support within your application. It has the following key features. o C implementation -- Many AppleScript support frameworks (for example, PowerPlant, MacApp) are available to C++ applications only. MOSL is entirely written in C. o object focused -- Historically, DTS AppleScript support samples have concentrated on supporting text scripting. MOSL ignores text scripting and concentrates on the scripting of discrete objects, such as windows and items within windows. o modern -- MOSL incorporates modern AppleScript techniques, such as 'deep' object resolution. It is also fully Carbon compatible. o well tested -- MOSL includes a test application, TestMoreOSL, that demonstrates its capabilities. It also includes a large suite of AppleScript-based tests. o comprehensive -- MOSL allows you to easily implement the bulk of the core event suite. MOSL supports all key forms except formRelativePosition. MOSL also supports data comparison for most revelant data types. The MoreOSL library is targetted to run on a PowerPC with Mac OS 8.5 and above. It compiles and works best under Carbon, but it will compile and work with InterfaceLib. Requires: Mac OS 8.5 Keywords: AppleScript, OSL, ObjectSupportLib, scripting implementation

[Next](MIBCarbon.h.md)


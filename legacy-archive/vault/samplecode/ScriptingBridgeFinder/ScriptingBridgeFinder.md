---
title: ScriptingBridgeFinder
apple_id: DTS10004283
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ScriptingBridge
published: '2011-08-05'
source_url: https://developer.apple.com/library/archive/samplecode/ScriptingBridgeFinder/Introduction/Intro.html
archived_at: '2026-07-18T03:23:33.365896Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# ScriptingBridgeFinder

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-08-05 Updated new project setup instructions in the ReadMe. Project updated for Xcode 4. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimrygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.2, Mac OS X 10.6 Snow Leopard or later. |
| __Runtime Requirements:__ | Mac OS X 10.6 Snow Leopard or later. |

This sample details the steps involved in putting together a project that uses Scripting Bridge to send Apple events to the Finder application. The sample is a small application launcher that scans the contents of the Applications folder (two levels deep) using Scripting Bridge for items the Finder considers applications. The user interface presents a list of the items that are found and allows the user to launch them. The program processes requests to launch applications from the user interface by using Scripting Bridge to ask the Finder to launch them.

[Next](ReadMe.txt.md)


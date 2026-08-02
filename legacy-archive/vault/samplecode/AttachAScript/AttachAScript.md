---
title: AttachAScript
apple_id: DTS10003911
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Foundation
published: '2011-07-14'
source_url: https://developer.apple.com/library/archive/samplecode/AttachAScript/Introduction/Intro.html
archived_at: '2026-07-18T03:01:13.375914Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# AttachAScript

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2011-07-14 Updated all classes to use properties and improved error handling. Project updated for Xcode 4. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojrgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 3.2, Mac OS X 10.6 Snow Leopard or later |
| __Runtime Requirements:__ | This app uses Apple events to communicate over TCP/IP so you must have "Remote Apple Events" turned on in the "Sharing" pane of the "System Preferences" before you can run the application. Mac OS X 10.6 Snow Leopard or later. |

If your application needs to communicate with other applications or processes, it can use AppleScript as a communication layer. Using the techniques described here, the included scripts handle all of the communication details while your application just makes calls to the scripting machinery. This design allows you to modularize the part of your application concerned with interprocess communication. The scripts are stored in the application's Resources folder and can be tuned in the field for particular needs and requirements, potentially by end users, without needing to recompile the application.

This sample targets the iTunes application, using remote Apple events over a network. The scripts handle all of the details involved in communicating with iTunes, while the program provides the user interface.

[Next](ReadMe.txt.md)


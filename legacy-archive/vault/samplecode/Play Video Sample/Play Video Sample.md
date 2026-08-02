---
title: Play Video Sample
apple_id: DTS10000437
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Play_Video_Sample/Introduction/Intro.html
archived_at: '2026-07-18T03:19:13.581753Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](PlayVideo.c.md)

# Play Video Sample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 The sample makes use of the RequestVideo sample code API. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon Display Manager 1.0, which is built into the Systems included with the first PowerMacs up through System 7.5. Display Manager 2.0 was first introduced in System 7.5.2 and is built into the system for all Macintoshes with the release of System 7.5.3. |

PlayVideo is a sample which makes use of the RequestVideo sample code API. PlayVideo & RequestVideo together demonstrate the usage of the Display Manager introduced with the PowerMacs and integrated into the system under System 7.5. With the RequestVideo sample code library, developers will be able to explore the Display Manager API by changing bit depth and screen resolution on multisync displays on built-in, NuBus, and PCI based video. Display Manager 1.0 is built into the Systems included with the first Power Macs up through System 7.5. Display Manager 2.0 was first introduced in System 7.5.2 and is built into the system for all Macintoshes with the release of System 7.5.3. It is a good idea to reset the screen(s) to the original setting before exit since the call to RVSetVideoAsScreenPrefs() may not do the right thing under Display Manager 1.0 with certain video drivers. Included with this project are: New Displays.h and Video.h header files. You will need to install the new universal Displays.h and Video.h header files to compile this sample code. These new universal headers are included with the Display Manager Development Kit. You will need to install these new universal Displays.h and Video.h header files only if they are newer than the ones inside your development environment. A link library called "DisplayLib" for the Display Manager 2.0 features (InterfaceLib contains the Display Manager 1.0 entry points). The link library is simply a namespace binding library with no code implementation behind it. The Display Manager glue library is needed to provide runtime code to access the Display Manager 2.0 features. A runtime library called "Display Library" which contains the PowerPC glue code to use the Display Manager 2.0 API (the InterfaceLib contains the Display Manager 1.0 glue code). The Display Library is built into system 7.5.3 and later systems. To make use if the Display Manger 2.0 features from PowerPC code while running System 7.1.2 through 7.5.2 you must have the "Display Library" file within the Code Fragment Manager search path - in the same directory as the application or in the extensions folder. Application Sample Code. This sample code will build a FAT application - an application that contains 68K code in code resources in the resource fork and PowerPC code in a PEF container in the data fork. You must build the 68K side of the app first since it is included in the PowerPC project for building the PowerPC side of the app. Requirements: Display Manager 1.0, which is built into the Systems included with the first PowerMacs up through System 7.5. Display Manager 2.0 was first introduced in System 7.5.2 and is built into the system for all Macintoshes with the release of System 7.5.3. Keywords: Display Manager, Play Video

[Next](PlayVideo.c.md)


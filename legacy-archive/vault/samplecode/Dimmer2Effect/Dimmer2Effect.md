---
title: Dimmer2Effect
apple_id: DTS10000825
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-02-25'
source_url: https://developer.apple.com/library/archive/samplecode/Dimmer2Effect/Introduction/Intro.html
archived_at: '2026-07-18T03:06:56.107434Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ComponentIncludes-ComponentDispatchHelper.c.md)

# Dimmer2Effect

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-02-25 Shows how to build a custom 2 source effect component for QuickTime. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon QuickTime 5+, Metrowerks CodeWarrior 7+, ProjectBuilder 1.1.1+, Microsoft Visual C++ 6 or later, Mac OS 9, Mac OS X 10.1+, Win98+ |

This sample shows how to build a custom effect component for QuickTime. The structure of this sample is that of a "Framework" which can be used to build new effects very quicly. Replace a few lines of code, write some new blit code and you're done...easy as cake. The sample effect this framework builds is called "Dimmer2". Dimmer2 uses two sources as input and renders the first source with a dim value that starts at full on, and ramps to full off. It then does the opposite for the second source starting at full off and ramping up to full on using a QT Tween to produce the dim values used to modify the pixels. CodeWarrior and Project Builder projects are included: - The CodeWarrior targets build a traditional PPC code resource, Carbon CFM component and a Carbon Mach-O component. The last two for Mac OS X only. - The Project Builder target will build a Mach-O dylib for Mac OS X. - Microsoft Visual C++ project included, see ReadMe for more details. Requirements: QuickTime 5+, Metrowerks CodeWarrior 7+, ProjectBuilder 1.1.1+, Microsoft Visual C++ 6 or later, Mac OS 9, Mac OS X 10.1+, Win98+ Keywords: QuickTime Effects Components

[Next](ComponentIncludes-ComponentDispatchHelper.c.md)


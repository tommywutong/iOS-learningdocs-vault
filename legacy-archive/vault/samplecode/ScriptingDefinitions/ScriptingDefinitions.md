---
title: ScriptingDefinitions
apple_id: DTS10003718
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-05-30'
source_url: https://developer.apple.com/library/archive/samplecode/ScriptingDefinitions/Introduction/Intro.html
archived_at: '2026-07-18T03:23:34.066856Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# ScriptingDefinitions

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.3, 2008-05-30 Changed code used for "rich text" from 'ctxt' to 'ricT' in the Standard Text Suite in the file ScriptingDefinitions.sdef. Added a ReadMe file that talks about the new, recommened XInclude method for including the Standard Suite in an .sdef file. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnzrhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.4.1 |
| __Runtime Requirements:__ | Mac OS X 10.4 |

This sample contains two scripting definition (sdef) files:
- Sketch.sdef: the scripting interface for Sketch (available separately in /Developer/Examples/AppKit). In Tiger, this file may be added to the Sketch application to drive its scriptability, in place of its existing scriptSuite and scriptTerminology files.
- Skeleton.sdef: a starting point for the scripting interface of an application. It contains definitions for the Standard Suite and the Standard Text Suite that you can include in your application's .sdef file (see enclosed ReadMe.txt for special Mac OS X 10.5 recommendations). Functionality for these suites is supplied by Cocoa Scripting.

[Next](ReadMe.txt.md)


---
title: LaunchWithDoc
apple_id: DTS10000311
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/LaunchWithDoc/Introduction/Intro.html
archived_at: '2026-07-18T03:13:27.945126Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](LaunchWithDoc.c.md)

# LaunchWithDoc

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-22 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

The smallest LaunchAplication example I could come up with. this launches an application with a 'odoc' AppleEvent this little bit of code here uses two Standard File calls to get the application to launch and the file to launch with, you will of course want to replace these with whatever you want to do NOTE: This also works for launching non-System 7 applications. If the Finder sees an 'odoc' or 'pdoc' Apple event in the launch block and the application being launched is NOT system 7 aware, the Finder coerces the Apple event into puppetstrings. So you don't need to special case for non-7.0 applications. Pretty neat, huh? Requires: System 7.0 Keywords: Process Manager, 'odoc' AppleEvent

[Next](LaunchWithDoc.c.md)


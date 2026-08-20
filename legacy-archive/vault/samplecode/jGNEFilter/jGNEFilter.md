---
title: jGNEFilter
apple_id: DTS10000189
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/jGNEFilter/Introduction/Intro.html
archived_at: '2026-07-18T03:29:47.574993Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](init.a.md)

# jGNEFilter

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

JGNESample This snippet is a sample GetNextEvent filter which uses the JGNEFilter mechanism described in Tech Note #85 "GetNextEvent: Blinking Apple Menu". The init, written in MPW assembler, installs a filter which SysBeeps whenever a key is pressed with the shift key held down. The jGNE mechanism is the only valid place where the event record can be examined after a GetNextEvent call, since tail patching GetNextEvent breaks several aspects of the system.

[Next](init.a.md)


---
title: DSp Context SwitchOld
apple_id: DTS10000052
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/DSp_Context_SwitchOld/Introduction/Intro.html
archived_at: '2026-07-18T03:05:50.853422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](DSp%20Context%20Switch%20Main.c.md)

# DSp Context SwitchOld

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-10-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon DrawSprocket, Context Switch |

Demonstration of DSp 1.7 or 1.1.4 context switching. This eaxmple shows DSP context switching with both DSp 1.7 and later built in functions and the equivalent in DrawSprcoket 1.1.4 and earlier. Due to a bug in earlier version of DSp 1.7, it is recommended that the DSpContext_Reserve and DSpContext_Queue functions only beused in DSp 1.7.3 and later, prior to this it is recommended that one use the earlier version of the the switching code. The controls for the sample application are: - right arrow for a larger context - left arrow for smaller - Cmd-Q to exit. PowerPC, System 8.1+, DrawSprocket, and either Universal Interfaces 3.3 or DrawSprocket SDK Requirements: DrawSprocket, Context Switch Keywords:

[Next](DSp%20Context%20Switch%20Main.c.md)


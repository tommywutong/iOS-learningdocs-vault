---
title: DiagnosticAUs
apple_id: DTS40008639
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/DiagnosticAUs/Introduction/Intro.html
archived_at: '2026-07-18T03:06:49.003445Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# DiagnosticAUs

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-04-15 Set of sample AudioUnits to perform various diagnostic functions on the system |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

The DiagnosticAUs project contains targets for three diagnostic audio units: AUValidSamples, AUPulseDetector, and DebugDispatcher. The DebugDispatcher unit just passes audio through, the AUPulseDetectorr is also a pass through unit but uses a pulse output to detect latency, and the AUValidSamples unit is a pass through that validates the incoming samples as the arrive.

[Next](ReadMe.txt.md)


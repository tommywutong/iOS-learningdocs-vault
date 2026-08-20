---
title: DiagnosticAUs
apple_id: DTS40008639
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/DiagnosticAUs/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:06:50.193152Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DiagnosticAUs](DiagnosticAUs.md)


[Next](AUPulseDetector.cpp.md)[Previous](DiagnosticAUs.md)

# ReadMe.txt

```
### DiagnosticAUs ###

===========================================================================
DESCRIPTION:

The DiagnosticAUs project contains targets for twhree diagnostic audio units: AUValidSamples, AUPulseDetector, and DebugDispatcher. The DebugDispatcher unit just passes audio through, the AUPulseDetectorr is also a pass through unit but uses a pulse output to detect latency, and the AUValidSamples unit is a pass through that validates the incoming samples as the arrive.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.6 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.6 or later

===========================================================================
PACKAGING LIST:

AUPulseDetector.cpp
- Implemention for the AUPulseDetector unit

AUPulseDetectorView.cpp
- Cocoa view for the AUPulseDetector unit

AUValidSamples.cpp
- Implemention for the DebugDispath unit

AUValidSamplesView.cpp
- Cocoa view for the AUValidSamples unit

DebugAU.cpp
- Implemention for the DebugDispath unit

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2009 Apple Inc. All rights reserved.
```

[Next](AUPulseDetector.cpp.md)[Previous](DiagnosticAUs.md)


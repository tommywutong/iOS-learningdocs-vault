---
title: MatrixMixerTest
apple_id: DTS40008645
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2016-02-11'
source_url: https://developer.apple.com/library/archive/samplecode/MatrixMixerTest/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:14:33.275863Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MatrixMixerTest](MatrixMixerTest.md)


[Next](MeteringView.h.md)[Previous](MixerController.h.md)

# ReadMe.md

```
### MatrixMixerTest ###

===========================================================================
DESCRIPTION:

MatrixMixerTest is a Cocoa-based application that provides an example of obtaining an instance of the matrix mixer audio unit and using it for audio mixing. The application also provides an example of creating metering views for viewing audio signal levels.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.11 or later. Xcode 7.2 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.8 or later

===========================================================================
PACKAGING LIST:

main.mm
- The main file of the project

MeteringView.h
MeteringView.mm
- MeteringView class for displaying the input signal levels

MixerController.h
MixerController.mm
- Controller class for managing and manipulating the matrix mixer

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0 - First version.
Version 1.1 - Project Updated for Xcode 4.6.3 and 10.8 SDK. Fixed MeterView
              crashing bugs in 64-bit, some re-factoring, added Core Audio Utility
              files, added more logging. App is sandboxed.
Version 2.0 - Project updated for Xcode 7.2 and 10.11 SDK. Removed deprecated
              API warnings. Added MatrixMixerVolumes utility file.

===========================================================================
Copyright (C) 2002-2016 Apple Inc. All rights reserved.
```

[Next](MeteringView.h.md)[Previous](MixerController.h.md)


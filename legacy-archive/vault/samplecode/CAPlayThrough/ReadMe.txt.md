---
title: CAPlayThrough
apple_id: DTS10004443
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-09-23'
source_url: https://developer.apple.com/library/archive/samplecode/CAPlayThrough/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:02:24.048286Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CAPlayThrough](CAPlayThrough.md)


[Next](main.m.md)[Previous](CAPlayThrough.md)

# ReadMe.txt

```
### CAPlayThrough ###

===========================================================================
DESCRIPTION:

The CAPlayThrough example project provides a Cocoa based sample application for obtaining all possible input and output devices on the system, setting the default device for input and/or output, and playing through audio from the input device to the output. The application uses two instances of the AUHAL audio unit (one for input, one for output) and a varispeed unit. the varispeed does two things: 
(1) if there is a difference between the sample rates of the input and output device, the varispeed AU does a resample (this is a setting that is made and is constant through the lifetime of the I/O operation, presuming the devices involved don't change) 
(2) As the devices involved may NOT be synchronized, a further adjustment is made over time, by varying the rate of playback between the two devices. This rate adjustment is made by looking at the rate scalar in the time stamps of the two devices. The rate scalar describes the measured difference between the idealized sample rate of a given device (say 44.1KHz) and the measured sample rate of the device as it is running - which will also vary. This adjustment is made by tweaking the rate parameter of the varispeed.

The app also uses a ring buffer to store the captured audio data from input and access it as needed by the output unit.

===========================================================================
BUILD REQUIREMENTS:

OS X v10.7 or later
Xcode 4.3 or later

===========================================================================
RUNTIME REQUIREMENTS:

OS X v10.7 or later

===========================================================================
PACKAGING LIST:

CAPlayThroughController.h
CAPlayThroughController.mm
- Controller class for managing PlayThrough objects. Handles building the available devices menu, resetting the PlayThrough objects, and starting and stopping the audio feed.

CAPlayThrough.h
CAPlayThough.cpp
- The CAPlayThrough class. Handles capturing data from input, storing to the ring buffer, and retrieving it for use by the output unit. Also performs the setup for the ring buffer, two AUHAL units and varispeed unit.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.2.2
- First version.
- Updated for Mac OS X 10.7 Lion & Xcode 4.3, now using newer AudioObjectXXX APIs.
- Updated for Xcode 4.6.3. Added v1.0.4 version of required Core Audio Utility Classes.

===========================================================================
Copyright (C) 2012-2013 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](CAPlayThrough.md)


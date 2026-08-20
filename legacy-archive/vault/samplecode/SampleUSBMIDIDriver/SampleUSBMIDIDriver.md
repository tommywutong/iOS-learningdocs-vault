---
title: SampleUSBMIDIDriver
apple_id: DTS40008412
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreMIDI
published: '2009-03-18'
source_url: https://developer.apple.com/library/archive/samplecode/SampleUSBMIDIDriver/Introduction/Intro.html
archived_at: '2026-07-18T03:23:05.719137Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](SampleUSBMIDI.cpp.md)

# SampleUSBMIDIDriver

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2009-03-18 Project for building a sample USB MIDI device driver |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Mac OS X v10.6 or later |

SampleUSBDriver is an example of a Mac OS X MIDI driver. MIDI drivers are CFPlugIns (described in the CoreFoundation documentation).
The sample driver is structured as a collection of reusable C++ classes, with the code specific to a single vendor's devices isolated to a small portion of the source code. If you find yourself needing to modify the classes other than SampleUSBDriver, please consider trying to implement the changes in a subclass instead, or telling Apple about the changes you need to make (use http://www.apple.com/developer/bugreporter). This allows the possibility of Apple providing improvements and fixes in the base classes in the future without your having to modify your driver other than to recompile it.
Use SampleUSBDriver as a starting place for a USB MIDI interface driver. Derive your USB driver from USBMIDIDriverBase. Derive non-USB drivers from MIDIDriver.
The MIDI driver programming interface is documented in <CoreMIDI/MIDIDriver.h>,
which your source should include. Your driver may also use the application
programming interface in <CoreMIDI/CoreMIDI.h>.

[Next](SampleUSBMIDI.cpp.md)


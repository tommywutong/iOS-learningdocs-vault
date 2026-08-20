---
title: SampleDriverPlugIn
apple_id: DTS40008642
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDriverPlugIn/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:00.623598Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDriverPlugIn](SampleDriverPlugIn.md)


[Next](Source-SDPPlugIn.cpp.md)[Previous](SampleDriverPlugIn.md)

# ReadMe.txt

```
This project illustrates implementing a plug-in to the Core Audio HAL that conforms to the API in <CoreAudio/AudioDriverPlugIn.h>.

The purpose of this kind of plug-in is to give IOAudio-based drivers a way to provide custom properties for their devices through the HAL's API. This API allows for the plug-in to override standard properties that do not affect I/O.

The plug-in the project implements the following:
- all the bundle entry points via the base class HP_DriverPlugIn.h
- a single device wide property called Foo whose value is a UInt32
- opening a connection to the IOAudioEngine in the driver and setting up a mach port to receive notifications from the engine
```

[Next](Source-SDPPlugIn.cpp.md)[Previous](SampleDriverPlugIn.md)


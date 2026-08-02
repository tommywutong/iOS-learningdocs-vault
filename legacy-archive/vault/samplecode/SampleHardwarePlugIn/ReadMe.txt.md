---
title: SampleHardwarePlugIn
apple_id: DTS40008643
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/SampleHardwarePlugIn/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:01.369349Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleHardwarePlugIn](SampleHardwarePlugIn.md)


[Next](Source-SHPControl.cpp.md)[Previous](SampleHardwarePlugIn.md)

# ReadMe.txt

```
### SampleHardwarePlugIn ###

===========================================================================
DESCRIPTION:

This is the CFPlugIn interface presented by a HAL plug-in. The HAL will create only one instance of each interface. This instance is responsible for providing all required services on behalf of as many devices of the kind it implements.

The Initialize method is called to allow the plug-in to set itself up. At this time any devices of it's kind and their streams can be presented to the system using AudioHardwareDevicesCreated() and AudioHardwareStreamsCreated(). The plug-in is also responsible for managing it's own notifications, and may install any CFRunLoopSources it needs using AudioHardwareAddRunLoopSource() at this time as well.

Teardown() is called when the HAL is unloading itself and the plug-in should dispose of any devices and streams it has created using AudioHardwareDevicesDied() and AudioHardareStreamsDied().

The rest of the methods in this interface correspond to the semantics of their similarly named counterparts in <CoreAudio/AudioHardware.h>. The HAL basically passes these calls directly to the plug-in in this fashion.

Plug-ins do not have to manage device or stream property listener procs. Instead, a plug-in can call AudioHardwareDevicePropertyChanged() or AudioHardwareStreamPropertyChanged() and the HAL will take care of calling all the appropriate listeners.

Note that only version 4 or later plug-ins will be loaded into 64 bit processes.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.5 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.5 or later

===========================================================================
PACKAGING LIST:

<< Describe important files here >>

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0
- First version.

===========================================================================
Copyright (C) 2009 Apple Inc. All rights reserved.
```

[Next](Source-SHPControl.cpp.md)[Previous](SampleHardwarePlugIn.md)


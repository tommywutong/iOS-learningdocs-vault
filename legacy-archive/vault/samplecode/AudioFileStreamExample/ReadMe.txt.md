---
title: AudioFileStreamExample
apple_id: DTS40008648
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioToolbox
published: '2013-06-29'
source_url: https://developer.apple.com/library/archive/samplecode/AudioFileStreamExample/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:01:24.912935Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AudioFileStreamExample](AudioFileStreamExample.md)


[Next](afsclient.cpp.md)[Previous](AudioFileStreamExample.md)

# ReadMe.txt

```
### AudioFileStreamExample ###

===========================================================================
DESCRIPTION:

The AudioFileStreamExample project provides two targets, a client that receives the streamed data and parses it for the appropriate audio file properties and data, and a server that opens an AudioFile for read and sends the raw bytes over a specified port. The example shows how to utilize the AudioFileStream callback mechanisms to received and process the data provided by the server, and plays the audio data using the AudioQueue API.

===========================================================================
BUILD REQUIREMENTS:

Mac OS X v10.8 or later

===========================================================================
RUNTIME REQUIREMENTS:

Mac OS X v10.8 or later

===========================================================================
PACKAGING LIST:

afsclient.cpp
- The client side code

afsserver.cpp
- The server side code

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

Version 1.0.1
- First version.
- Updated Xcode Project.

===========================================================================
Copyright (C) 2009-2013 Apple Inc. All rights reserved.
```

[Next](afsclient.cpp.md)[Previous](AudioFileStreamExample.md)


---
title: Audio Codec Examples
apple_id: DTS40012991
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2013-01-02'
source_url: https://developer.apple.com/library/archive/samplecode/AudioCodecExamples/Listings/SampleFiles_SampleAudioFilesReadMe_txt.html
archived_at: '2026-07-18T03:01:20.448217Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Audio Codec Examples](Audio%20Codec%20Examples.md)


[Next](Document%20Revision%20History.md)[Previous](PublicUtility-CAXException.h.md)

# SampleFiles/SampleAudioFilesReadMe.txt

```
There are two sample audio files included with this project:

SampleIMACodecTest.caf
SampleIMACodecTest.mov

Both will playback correctly thereby testing the decoder when the AudioCodecExample.component is built and placed in one of these locations:

/Library/Audio/Plug-Ins/Components
~/Library/Audio/Plug-Ins/Components


SampleIMACodecTest.caf - is an Acme/DEMO IMA encoded 2 channels 44.1kHz Core Audio Format file, created from an uncompressed Garage Band .aif file using afconvert.

The command used to create the above test file is as follows and can be used to test the encoder using your own source file.

     afconvert -f caff -d DEMO sourceFile.aif


SampleIMACodecTest.mov - is an Acme/DEMO IMA encoded 2 channels 16kHz audio only QuickTime Movie file, created from an uncompressed Garage Band .aif file using QuickTime 7 Export to Movie File.
```

[Next](Document%20Revision%20History.md)[Previous](PublicUtility-CAXException.h.md)


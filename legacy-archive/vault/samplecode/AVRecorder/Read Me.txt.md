---
title: AVRecorder
apple_id: DTS40011004
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2012-11-29'
source_url: https://developer.apple.com/library/archive/samplecode/AVRecorder/Listings/Read_Me_txt.html
archived_at: '2026-07-18T03:00:28.123339Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVRecorder](AVRecorder.md)


[Next](Document%20Revision%20History.md)[Previous](AVRecorder-main.m.md)

# Read Me.txt

```
About AVRecorder
================

AVRecorder demonstrates usage of AV Foundation capture API for recording movies and using transport controls.

The main components are:

• AVRecorderDocument.[h,m] -- The core AVRecorder code
• AVCaptureDeviceFormat_AVRecorderAdditions.[h,m] -- Prints a pretty device format NSString
• AVFrameRateRange_AVRecorderAdditions.[h,m] -- Prints a pretty frame rate NSString

Using the Sample
----------------
Begin and complete video recording with the Record button. If the selected video device supports transport controls, use the Rewind, Play, Stop, and FF buttons to control the tape.

How It Works
------------

AVRecorder makes use of the following AV Foundation AVCapture classes to provide movie recording:

AVCaptureDevice
AVCaptureFileOutput
AVCaptureInput
AVCaptureMovieFileOutput
AVCaptureOutput
AVCaptureSession
AVCaptureVideoPreviewLayer

See the AV Foundation documentation for more information.
```

[Next](Document%20Revision%20History.md)[Previous](AVRecorder-main.m.md)


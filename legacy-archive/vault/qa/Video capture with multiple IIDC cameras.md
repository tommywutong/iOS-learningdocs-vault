---
title: Video capture with multiple IIDC cameras
apple_id: DTS10003381
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1365/_index.html
archived_at: '2026-07-18T02:30:26.384539Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1365

# Video capture with multiple IIDC cameras

## Q:  My QTKit Capture application uses multiple IIDC cameras to capture video with a frame size of 640x480 @ 30 fps, but I've found I can only capture with three cameras. Is this a known limitation?

A: My QTKit Capture application uses multiple IIDC cameras to capture video with a frame size of 640x480 @ 30 fps, but I've found I can only capture with three cameras. Is this a known limitation?

The limitation you're encountering comes from the bandwidth each camera is using on the FireWire bus.

In general, the FireWire bus that IIDC cameras connect to can run at a maximum speed of 400Mb/sec.

The FireWire spec allows up to 80% of the total bandwidth to be used for isochronous traffic, like video. IIDC cameras can operate at different frame rates, different frame sizes and can also produce different flavors of YUV data -- YUV 4:1:1 and YUV 4:2:2. Depending on these factors the amount of bandwidth consumed will vary.

Multiple IIDC streams can be active simultaneously. The number of active streams is only limited by the number of cameras present and the amount of FireWire bus bandwidth available. If there is insufficient bandwidth for a given setting (pixel format / frame size / frame rate), QuickTime will attempt to use a smaller frame size. If that fails, it will try a slower frame rate.

The solution is to work with smaller frame sizes, lower frame rates or to add an additional FireWire bus using a 3rd party PCI card giving you more bandwidth to play with.

See [QA1586 QTKit Capture - Specifying Media Compression Settings](https://developer.apple.com/qa/qa2008/qa1586.html) to learn how to configure media compression settings (format, frame size, and so on) for the QTKit Capture `QTCaptureMovieFileOutput` object.

QTKit Capture will send you the `QTCaptureSessionRuntimeErrorNotification` when you are trying to record to multiple cameras simultaneously and you've exceeded the bandwidth limitations. This will allow you to detect this condition (in the absence of any error code being returned). The notification user info dictionary `QTCaptureSessionErrorKey` entry contains an `NSError` object that describes the error that prevented the session from running properly.

Here's how to setup to receive this notification:

__Listing 1__  How to receive the `QTCaptureSessionRuntimeErrorNotification` notification.

```
// handle the QTCaptureSessionRuntimeErrorNotification  -(void)handleNotification:(NSNotification *)theNotification {     // your code to handle notification here }  ...  // setup to receive the QTCaptureSessionRuntimeErrorNotification  NSNotificationCenter *nc; nc = [NSNotificationCenter defaultCenter]; [nc addObserver:self         selector:@selector(handleNotification:)         name:QTCaptureSessionRuntimeErrorNotification         object:nil];
```


The limitations described above also apply for Sequence Grabber, i.e. the number of active streams is limited by the number of cameras present and the amount of FireWire bus bandwidth available. The solution is to work with smaller frame sizes, lower frame rates or to add an additional FireWire bus using a 3rd party PCI card giving you more bandwidth to play with.

To configure the sequence grabber settings, use `SGSettingsDialog`, `SGSetSettings` and `SGSetChannelSettings`. See the [Movie Creation Guide](https://developer.apple.com/documentation/QuickTime/RM/CreatingMovies/MTCreateMovies/A-Intro/chapter_1000_section_1.html#//apple_ref/doc/uid/TP40000906-IntroductiontoQuickTimeMovieCreationGuide-DontLinkElementID_142) for additional information.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | Updated for QTKit Capture. |
| 2004-08-25 | New document that discusses factors which influence the number of IIDC cameras that can simultaniously be used for capture. |


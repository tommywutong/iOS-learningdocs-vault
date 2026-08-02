---
title: QTKit Capture - Setting DecompressedVideoOutput CVPixelBuffer Attributes
apple_id: DTS10004603
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-03-06'
source_url: https://developer.apple.com/library/archive/qa/qa1582/_index.html
archived_at: '2026-07-18T02:32:19.949812Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1582

# QTKit Capture - Setting DecompressedVideoOutput CVPixelBuffer Attributes

## Q:  How can I resize the `CVImageBuffer`'s I'm getting passed when using the QTCaptureDecompressedVideoOutput delegate method `captureOutput:didOutputVideoFrame:withSampleBuffer:fromConnection:`?

A: How can I resize the `CVImageBuffer`'s I'm getting passed when using the QTCaptureDecompressedVideoOutput delegate method `captureOutput:didOutputVideoFrame:withSampleBuffer:fromConnection:`?

You can ask QTCaptureDecompressedVideoOutput to provide you with a `CVImageBuffer` of a specific size and pixel format using the `setPixelBufferAttributes:` method passing in an `NSDictionary` with the appropriate `kCVPixelBuffer` attributes defined.

If your application required 320x240 ARGB pixel buffers out of QTCaptureDecompressedVideoOutput you could set the attributes as shown in the following example.

__Listing 1__  Setting QTCaptureDecompressedVideoOutput pixel buffer attributes.

```
static void SetOutputPixelBufferAttributes(QTCaptureDecompressedVideoOutput *inDecompressedVideoOutput) {     NSDictionary *attributes = [NSDictionary dictionaryWithObjectsAndKeys:                                 [NSNumber numberWithDouble:320.0], (id)kCVPixelBufferWidthKey,                                 [NSNumber numberWithDouble:240.0], (id)kCVPixelBufferHeightKey,                                 // k32ARGBPixelFormat may be used on Mac OS X 10.4.x                                 [NSNumber numberWitUnsignedInt:kCVPixelFormatType_32ARGB],                                                                 (id)kCVPixelBufferPixelFormatTypeKey,                                 nil];      [inDecompressedVideoOutput setPixelBufferAttributes:attributes]; }
```

Specifying pixel buffer attributes may cause the connected capture device to automatically be reconfigured to best match the requested output format. Conversions may also be necessary. For example, a pixel format conversion would be required if the capture device does not have an RGB mode yet RGB data has been requested. QTCapture will do all conversions for you and will choose the most optimal video pipeline for the requested output format.

For optimal performance move any time intensive tasks to another thread if necessary reserving the delegate method thread for queuing up frames for processing and dropping them as required.

- [QTCaptureDecompressedVideoOutput](https://developer.apple.com/documentation/QuickTime/Reference/QTCaptureDecompressedVideoOutput_Ref/Introduction/Introduction.html)
- [QTCaptureVideoPreviewOutput](https://developer.apple.com/documentation/QuickTime/Reference/QTCaptureVideoPreviewOutput_Class/Reference/Reference.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-06 | Editorial |
| 2008-01-22 | New document that describes how to configure a DecompressedVideoOutput objects CVPixelBuffer attributes. |


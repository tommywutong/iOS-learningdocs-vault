---
title: QTKit Capture - Extracting SMPTE Timecode information from a QTSampleBuffer
apple_id: DTS40007468
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-03-17'
source_url: https://developer.apple.com/library/archive/qa/qa1600/_index.html
archived_at: '2026-07-18T02:32:24.224692Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1600

# QTKit Capture - Extracting SMPTE Timecode information from a QTSampleBuffer

## Q:  How can I extract SMPTE timecode information during device playback using the `QTCaptureFileOutput` object?

A: How can I extract SMPTE timecode information during device playback using the `QTCaptureFileOutput` object?

If the device you are capturing from is providing SMPTE timecode, the sample buffer (`QTSampleBuffer`) objects presented at the output will be tagged with timecode meta-data that may be accessed using the `QTSampleBufferSMPTETimeAttribute` key.

For example, both the `QTCaptureFileOutput` and `QTCaptureDecompressedVideoOutput` objects have a delegate method called `captureOutput:didOutputSampleBuffer:fromConnection:` which is invoked every time the output receives a new sample buffer. By using the `QTSampleBuffer` `attributeForKey:` method, the SMPTE timecode can be pulled out for each sample buffer recieved as shown in Listing 1.

__Listing 1__

```objc
- (void)captureOutput:(QTCaptureFileOutput *)captureOutput                       didOutputSampleBuffer:(QTSampleBuffer *)sampleBuffer                              fromConnection:(QTCaptureConnection *)connection {     NSValue *SMPTETime = [sampleBuffer attributeForKey:QTSampleBufferSMPTETimeAttribute];     if (SMPTETime) {         NSLog(@"SMPTE Time: %@", QTStringFromSMPTETime([SMPTETime SMPTETimeValue]));     } }
```

A `QTSampleBuffer` may have other attributes as well. The following attributes are declared in `QTSampleBuffer.h`.

Returns the date on which the media in the buffer was originally recorded.

The value is an `NSDate`.

The `@"dateRecorded"` string value can be used in key paths for key-value coding, key-value observing, and bindings.

If the buffer is from a real time source, this attribute returns the buffer's host time.

The value returned by this attribute can be compared with the return value of `CVGetCurrentHostTime` or `AudioGetCurrentHostTime` to determine whether or not it is too late for the buffer to be processed in real time.

The value is an `NSNumber` interpreted as a `UInt64`.

The `@"hostTime"` string value can be used in key paths for key-value coding, key-value observing, and bindings.

Returns the SMPTE timecode for the sample buffer, if it has one.

The value is an `NSValue` interpreted as a `SMPTETime` (defined in CoreAudio/CoreAudioTypes.h).

The `@"SMPTETime"` string value can be used in key paths for key-value coding, key-value observing, and bindings.

If the buffer marks a scene change in the input content, returns a Scene Change constant. The returned constant specifies the type of scene change.

The `@"sceneChangeType"` string value can be used in key paths for key-value coding, key-value observing, and bindings.

Indicates that a scene change was explicitly marked in the sample buffers metadata.

This constant is returned by `QTSampleBufferSceneChangeTypeAttribute` specifying what kind of scene change, if any, is marked by a sample buffer.

Indicates that the scene changed due to a discontinuity in time stamps between the current sample buffer and the previous sample buffer.

This constant is returned by `QTSampleBufferSceneChangeTypeAttribute` specifying what kind of scene chnage, if any, is marked by a sample buffer.

- Introduction to QTKit Capture Programming Guide

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-17 | New document that describes how to use the QTSampleBufferSMPTETimeAttribute with a sample buffer. |


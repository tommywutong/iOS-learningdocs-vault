---
title: QTKit Capture - Disabling Audio Or Video When Capturing From a Muxed Device
apple_id: DTS40007674
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: QTKit
published: '2008-05-19'
source_url: https://developer.apple.com/library/archive/qa/qa1607/_index.html
archived_at: '2026-07-18T02:32:42.039330Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1607

# QTKit Capture - Disabling Audio Or Video When Capturing From a Muxed Device

## Q:  How can I disable the audio or video stream when capturing from a muxed device?

A: How can I disable the audio or video stream when capturing from a muxed device?

Muxed devices such as DV and HDV Cameras are represented in QTKit Capture by the media type `QTMediaTypeMuxed`.

To only capture a single stream from the device (for example video only), disable the audio connections on the device input for the capture device by using the `QTCaptureConnection` method `setEnabled:` and passing in `NO`.

__Listing 1__  Disable Audio Connections From A Muxed Device Input.

```
QTCaptureDevice *theDefaultMuxedDevice; QTCaptureDeviceInput *theDeviceInput; BOOL success; NSError *error;  ...  // get the default muxed device theDefaultMuxedDevice = [QTCaptureDevice defaultInputDeviceWithMediaType:QTMediaTypeMuxed];  // open the device success = [theDefaultMuxedDevice open:&error]; if (YES == success) {     // get the associated device input     theDeviceInput = [QTCaptureDeviceInput deviceInputWithDevice:theDefaultMuxedDevice];      // get the list of owned connections      NSArray *ownedConnections = [theDeviceInput connections];      // disable all the audio connections     for (QTCaptureConnection *connection in ownedConnections) {         if ( [[connection mediaType] isEqualToString:QTMediaTypeSound] ) {             [connection setEnabled:NO];         }     } } else {     // do something with the error code }  ...
```

If you only want to capture audio, disable the `QTMediaTypeVideo` connections.

Introduction to QTKit Capture Programming Guide

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-05-19 | New document that describes the use of the setEnabled: method to disable audio or video capture from muxed devices. |


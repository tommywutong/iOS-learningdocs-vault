---
title: Setting the orientation of video with AV Foundation
apple_id: DTS40011134
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-06-24'
source_url: https://developer.apple.com/library/archive/qa/qa1744/_index.html
archived_at: '2026-07-18T02:34:32.597625Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1744

# Setting the orientation of video with AV Foundation

## Q:  How do I set the orientation of video with AV Foundation?

A: AV Foundation Capture

You can set an orientation on a `AVCaptureConnection` to specify how you want the images oriented in the `AVCaptureOutput` output destination (`AVCaptureMovieFileOutput`, `AVCaptureStillImageOutput` or `AVCaptureVideoDataOutput`) or `AVCaptureVideoPreviewLayer` for the connection.

Use the `AVCaptureConnection` `supportsVideoOrientation` property (`getter= isVideoOrientationSupported`) to determine whether the object supports changing the orientation of the video, and the `videoOrientation` property to specify how you want the images oriented in the the output destination or preview layer. For example, here's a code snippet showing how to set the `videoOrientation` for a `AVCaptureStillImageOutput`'s `AVCaptureConnection` to `AVCaptureVideoOrientationLandscapeLeft`:

__Listing 1__  Setting the `videoOrientation` for a `AVCaptureStillImageOutput`'s `AVCaptureConnection`.

```objc
#import <AVFoundation/AVFoundation.h>

AVCaptureStillImageOutput *stillImageOutput = <#A still image output#>;
AVCaptureConnection *connection =
    [stillImageOutput connectionWithMediaType:AVMediaTypeVideo];
if ([connection isVideoOrientationSupported])
{
    [connection setVideoOrientation: AVCaptureVideoOrientationLandscapeLeft];
}
```

Applications that do not take into consideration the video track transform and still image exif metadata may not display these media items in the proper orientation.

`AVCaptureVideoDataOutput` clients may receive __physically__ rotated `CVPixelBuffers` in their `-captureOutput:didOutputSampleBuffer:fromConnection:` delegate callback. All 4 `AVCaptureVideoOrientation` modes are supported, and rotation is hardware accelerated. To request buffer rotation, a client calls `-setVideoOrientation:` on the `AVCaptureVideoDataOutput`'s video `AVCaptureConnection`.

If you are using an `AVAssetWriter` object to write a movie file, you can use the `transform` property of the associated `AVAssetWriterInput` to specify the output file orientation. This will write a display transform property into the output file as the preferred transformation of the visual media data for display purposes. See the `AVAssetWriterInput.h` interface file for the details.

If you are using an `AVMutableComposition` to edit your visual assets, you can set the `preferredTransform` property on any of the video tracks (`AVMutableCompositionTrack`).

If you are using an `AVMutableVideoComposition` to edit the video tracks in a video composition, use an `AVMutableVideoCompositionLayerInstruction` object to modify the transform to apply to a given track in the video composition. Use the `setTransform:atTime:` method to set a value of the transform at a time within the time range of the instruction, or use the `setTransformRampFromStartTransform:toEndTransform:timeRange:` method to set a transform ramp to apply during a given time range.

Otherwise, if you specify the `AVAssetExportPresetPassthrough` export option to let all tracks pass through but you still want to set a transform on the composition, set the `preferredTransform` property on the composition tracks as described above.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-06-24 | Updated to include information about using an AVCaptureVideoPreviewLayer's AVCaptureConnection videoOrientation property to set the orientation instead of the deprecated AVCaptureVideoPreviewLayer orientation property. Modified code snippet to show how to get the AVCaptureConnection for the AVCaptureOutput. Other miscellaneous changes. |
| 2013-04-29 | Updated to include information about AVMutableComposition, AVMutableVideoComposition and AVAssetExportSession. |
| 2013-01-24 | Added information about physically rotating CVPixelBuffers in the AVCaptureVideoDataOutput -captureOutput:didOutputSampleBuffer:fromConnection: delegate callback. |
| 2011-06-29 | New document that describes how to set the orientation of video with AV Foundation. |


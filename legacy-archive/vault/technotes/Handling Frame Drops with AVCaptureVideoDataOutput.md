---
title: Handling Frame Drops with AVCaptureVideoDataOutput
apple_id: DTS40017661
resource_type: Technical Note
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-07-12'
source_url: https://developer.apple.com/library/archive/technotes/tn2445/_index.html
archived_at: '2026-07-26T19:54:15.327782Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2445

# Handling Frame Drops with AVCaptureVideoDataOutput

You may find you are dropping frames while using `AVCaptureVideoDataOutput` to process frames from video being captured. How do you determine whose fault it is? And once it occurs, what can you do about it? How can you recover? This technote discusses techniques for handling these frame drops.

[Your capture(_:didOutputSampleBuffer:from:) method must be efficient to avoid frame drops](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvmu6vksl5bucucukvjekx27l5cesrcpkvkfavkuknau2ucmivbfkrsgivjf6rssj5gv6x27jvcviscpirpu2vktkrpuerk7ivdemskdjfcu4vc7krhv6qkwj5euix2gkjau2rk7irje6uct)[Set alwaysDiscardsLateVideoFrames to YES](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvjukvc7ifgfoqkzkncesu2difjeiu2mifkekvsjircu6rssifguku27krhv6wkfkm)[AVCaptureVideoDataOutput can report frame drops](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvke4vcbi4zq)[Frame drops can be mitigated by lowering the frame rate](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvdfeqknivpuiuspkbjv6q2bjzpuerk7jveviskhifkekrc7ijmv6tcpk5cveskoi5pviscfl5dfeqknivpveqkuiu)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvjekrsfkjcu4q2fkm)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Your capture(_:didOutputSampleBuffer:from:) method must be efficient to avoid frame drops

Delegates of an `AVCaptureVideoDataOutput` object can use the video frame provided in the `capture(_:didOutputSampleBuffer:from:)` method in conjunction with other APIs for additional processing. This method is called periodically, so it must be able to process a sample buffer within the amount of time allotted to a frame. If it takes too long and you hold onto the video frames, AV Foundation may stop delivering frames not only to your delegate but also to other outputs such as a preview layer.

If your application is causing samples to be dropped by retaining the provided `CMSampleBuffer` objects for too long, but it needs access to the sample data for a long period of time, consider copying the data into a new buffer and then calling `CFRelease` on the sample buffer if it was previously retained so the memory it references can be reused.

[Back to Top](#)

## Set alwaysDiscardsLateVideoFrames to YES

Always set the `alwaysDiscardsLateVideoFrames` property to `YES`.

The one exception to this is if you are recording, and you are very likely to be faster than real time.

When you set `alwaysDiscardsLateVideoFrames` to `YES`, it enforces a buffer queue size of 1 at the end of the video processing pipeline. This means if you don't pull a frame on time because you were late, it will never get further behind than the current frame — it will throw out the current frame, and append the new one. In effect, it is always giving you the latest frame. This keeps you from building up latency if you have a process that is taking too much time, and is doing so chronically. It saves you from periodically slow processing if you have a momentary glitch. You are still going to get all the frames, but you might miss a few when the glitch occurs.

It does not save you from chronically slow processing. If you are always slower than real time you are still going to drop a lot of frames, and as a result, provide a bad user experience.

[Back to Top](#)

## AVCaptureVideoDataOutput can report frame drops

You can use the `captureOutput(_:didDrop:from:)` delegate to determine when you are dropping frames as shown in Listing 1:

__Listing 1__  The `captureOutput(_:didDrop:from:)` delegate for determining when frames are dropped.

```swift
func captureOutput(_ captureOutput: AVCaptureOutput!, didDrop sampleBuffer: CMSampleBuffer!, from connection: AVCaptureConnection!) {
    // You just dropped a frame!
}
```

Delegates receive this message whenever a late video frame is dropped. This method is called once for each dropped frame.

This method provides a sample buffer for each frame dropped, but the sample buffer contains no image data because the image data is no longer available (it has been recycled). Instead, the sample buffer contains timing information, a format description, and attachments such as the dropped frame reason attachment `kCMSampleBufferAttachmentKey_DroppedFrameReason` which identifies the specific reason why the frame was dropped. The value for this key is one of the following:

- `kCMSampleBufferDroppedFrameReason_FrameWasLate`

  The video capture client has indicated that late video frames should be dropped (`alwaysDiscardsLateVideoFrames` is set to `YES`) and the current frame is late. This condition is typically caused by the client's video processing taking too long (the client is operating slower than real-time).
- `kCMSampleBufferDroppedFrameReason_OutOfBuffers`

  The client has indicated that late video frames should not be dropped (`alwaysDiscardsLateVideoFrames` is set to `NO`), and the video processing pipeline providing sample buffers has run out of source buffers. This condition is typically caused by the client holding onto buffers for too long, and can be alleviated by returning buffers to the provider.
- `kCMSampleBufferDroppedFrameReason_Discontinuity`

  The module providing sample buffers has experienced a discontinuity, and an unknown number of frames have been lost. This condition can occur for a number of reasons: the system is too busy, something unexpected happened, the capture system had to reset itself, something crashed, and so on. The result is some number of frames were lost, and the next video frame that arrives will have a much later timestamp than the one you are currently on.

[Back to Top](#)

## Frame drops can be mitigated by lowering the frame rate

As discussed in [AVCaptureVideoDataOutput can report frame drops](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytonrwgewugsbrfvke4vcbi4zq), the `captureOutput(_:didDrop:from:)` delegate lets you know when you are dropping frames and take an appropriate action. It is a great tool for this purpose. The action you take might be while you are developing your app you pay attention to frame drops, and notice on which devices you are dropping frames, so when you ship your app you've tuned it to know which frame rate to use on which devices.

You can also use it as a stop-gap measure. For example, if in the field in real-time you find you are still dropping frames, you can mitigate these by lowering the frame rate dynamically. The `AVCaptureVideoDataOutput` frame rate can be altered dynamically without stopping the session. It will gradually throttle down to the new frame rate you've set. There will be no glitches in the capture preview or output. By lowering the minimum and maximum frame rate you don't have to drop a lot of frames to catch back up. You can do it gradually, perhaps over a second, and get up to a reasonable quality of service where you can keep up.

You set the minimum and maximum frame rate by setting an `AVCaptureDevice`’s `activeVideoMinFrameDuration` and `activeVideoMaxFrameDuration` properties. Duration equals 1/(frame rate). An `AVCaptureDevice`'s `activeVideoMinFrameDuration` property is the reciprocal of its active maximum frame rate. To limit the maximum frame rate of the capture device, set this property to a value supported by one of the device's active formats (see the `AVCaptureDevice`'s `formats` property, an array of `AVCaptureDeviceFormat` objects supported by the device, each of which has a `videoSupportedFrameRateRanges` property indicating the format’s supported frame rate ranges). Similarly, an `AVCaptureDevice`'s `activeVideoMaxFrameDuration` property is the reciprocal of its active minimum frame rate. To limit the minimum frame rate of the capture device, set this property to a value supported by one of the device's active formats. See Listing 2:

__Listing 2__  Lowering the frame rate for the capture device to recover from slow processing.

```
/*
    Lower the frame rate for the capture device to recover from slow processing.

    Note: the new rate must be a value supported by one of the device's active formats.
*/

let session = <#An AVCaptureSession#>
let videoDevice = <#An AVCaptureDevice#>

do {
    session.beginConfiguration()
    try videoDevice.lockForConfiguration()

    // Minimum duration is 1 / (max frame rate).
    let currentFrameRate:Int32 = <#The current frame rate#>

    // Lower the min and max frame rate to recover from slow processing.
    let newFrameRate:Int32 = currentFrameRate - 1
    videoDevice.activeVideoMinFrameDuration = CMTimeMake(1, newFrameRate)
    videoDevice.activeVideoMaxFrameDuration = CMTimeMake(1, newFrameRate)

    videoDevice.unlockForConfiguration()
    session.commitConfiguration()
}
catch {
    print("Failed to lock the device for configuration: \(error)")
}
```

[Back to Top](#)

## References

- _[AVFoundation Programming Guide](../documentation/Audio%20Video/AVFoundation%20Programming%20Guide/About%20AVFoundation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcoby)_
- [AVCaptureVideoDataOutput](https://developer.apple.com/reference/avfoundation/avcapturevideodataoutput)
- [capture(_:didOutputSampleBuffer:from:)](https://developer.apple.com/reference/avfoundation/avcapturefileoutputdelegate/1390096-capture)
- [alwaysDiscardsLateVideoFrames](https://developer.apple.com/reference/avfoundation/avcapturevideodataoutput/1385780-alwaysdiscardslatevideoframes)
- [captureOutput(_:didDrop:from:)](https://developer.apple.com/reference/avfoundation/avcapturevideodataoutputsamplebufferdelegate/1388468-captureoutput)
- [activeVideoMinFrameDuration](https://developer.apple.com/reference/avfoundation/avcapturedevice/1389290-activevideominframeduration)
- [activeVideoMaxFrameDuration](https://developer.apple.com/reference/avfoundation/avcapturedevice/1387816-activevideomaxframeduration)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2017-07-12 | New document that discusses how to handle dropped frames while using AVCaptureVideoDataOutput to process frames from video being captured. |


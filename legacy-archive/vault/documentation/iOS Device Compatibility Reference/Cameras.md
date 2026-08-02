---
title: iOS Device Compatibility Reference
apple_id: TP40013599
resource_type: Guide
platform: iOS
topic: Data Management
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/Cameras/Cameras.html
archived_at: '2026-07-15T07:31:54.235321Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [iOS Device Compatibility Reference](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Graphics%20Processors.md)

# Cameras

Collectively, iPhone and iPad devices are some of the most popular still and video cameras in the world. In addition to capturing stills and movies, iOS offers a powerful platform for computational photography and computer vision applications. To make the most of iPhone and iPad cameras, you should be aware of the specific capabilities of each camera device. This chapter summarizes the special features of recent iPhone and iPad cameras and links to the APIs you’ll need to use those features in your app.

Recent iPhone and iPad models include a number of unique camera features, summarized in Table 4-1. For details on each feature, follow the links in the table to the corresponding sections below.

__Table 4-1__  iPhone Camera Features Summary

| Feature | iPhone 8  iPhone 8 Plus  iPhone X | iPhone 7  iPhone 7 Plus | iPhone 6s  iPhone 6s Plus | iPhone SE | iPhone 6  iPhone 6 Plus |
| [Maximum Still Image Resolution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrga) (back camera) | 4032 x 3024 pixels (12 MP) | 4032 x 3024 pixels (12 MP) | 4032 x 3024 pixels (12 MP) | 4032 x 3024 pixels (12 MP) | 3264 x 2448 pixels (8 MP) |
| [Maximum Still Image Resolution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrga) (front camera)  _Items in italic_: see [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) | _3088 x 2320 pixels (7 MP)_ | _3088 x 2320 pixels (7 MP)_ | _2576 x 1932 pixels (5 MP)_ | 1280 x 960 pixels (1.2 MP) | 1280 x 960 pixels (1.2 MP) |
| Notable [Video Resolutions and Frame Rates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrge) (back camera) | 2160p30 (4K)  2160p60 (4K)  1080p30  1080p60 | 2160p30 (4K)  1080p30  1080p60 | 2160p30 (4K)  1080p30  1080p60 | 2160p30 (4K)  1080p30  1080p60 | 1080p30  1080p60 |
| [High Frame Rate (HFR) / Slow Motion Video](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgi) Formats | 1080p240  1080p120  720p240 | 1080p120  720p240 | 1080p120  720p240 | 1080p120  720p240 | 720p240 |
| [Single-Shot / Video HDR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzz) Formats | No | No | Back camera: not supported  Front camera: most formats | No | Back camera: 540p30, 720p30, 1080p30, 1080p60  Front camera: all formats |
| [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) (back camera) | up to 4032 x 3024 pixels (12 MP) | up to 4032 x 3024 pixels (12 MP) | up to 3840 x 2160 pixels (8 MP) | up to 3840 x 2160 pixels (8 MP) | up to 3264 x 2448 pixels (8 MP) |
| [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) (front camera) | up to 3088 x 2320 pixels (7 MP) | up to 3088 x 2320 pixels (7 MP) | up to 2576 x 1932 pixels (5 MP) | no (same as video resolution) | no (same as video resolution) |
| [Optical Image Stabilization (OIS)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzu) | Still / bracketed / video capture | Still / bracketed / video capture | _iPhone 6s:_ No  _iPhone 6s Plus:_  Still / bracketed / video capture | No | _iPhone 6:_ No  _iPhone 6 Plus:_  Still image capture only |
| [RAW Photo Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztge)  (back camera only) | Yes | Yes | Yes | Yes | No |
| [Focus Pixels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzv) (back camera only) | Yes | Yes | Yes | Yes | Yes |
| [Cinematic Video Stabilization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzw) | Yes | Yes | Yes | Yes | Yes |
| [Retina Flash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzx) | Yes | Yes | Yes | Yes | No |
| [Live Photos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzy) | Yes | Yes | Yes | Yes | No |
| [Wide-Gamut Color Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgq) | Yes | Yes | No | No | No |
| [Dual Camera](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgi) | Yes  (iPhone 8 Plus and iPhone X)) | Yes  (iPhone 7 Plus only) | No | No | No |
| [TrueDepth Camera](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztha) | Yes  (iPhone X only) | No | No | No | No |

__Table 4-2__  iPad Camera Features Summary

| Feature | iPad Pro  10.5-inch  12.9-inch (2nd generation) | iPad  (5th generation) | iPad Pro  (12.9-inch) | iPad Pro  (9.7-inch) |
| [Maximum Still Image Resolution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrga) (back camera) | 4032 x 3024 pixels (12 MP) | 3264 x 2448 pixels (8 MP) | 3264 x 2448 pixels (8 MP) | 4032 x 3024 pixels (12 MP) |
| [Maximum Still Image Resolution](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrga) (front camera)  _Items in italic_: see [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) | _3088 x 2320 pixels (7 MP)_ | 1280 x 960 pixels (1.2 MP) | 1280 x 960 pixels (1.2 MP) | _2576 x 1932 pixels (5 MP)_ |
| Notable [Video Resolutions and Frame Rates](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrge) (back camera) | 2160p30 (4K)  1080p30  1080p60 | 1080p30  1080p60 | 1080p30  1080p60 | 2160p30 (4K)  1080p30 (preset)  1080p60 |
| [High Frame Rate (HFR) / Slow Motion Video](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgi) Formats | 1080p120  720p240 | 720p240 | 720p240 | 1080p120  720p240 |
| [Single-Shot / Video HDR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzz) Formats | No | No | Back camera: not supported  Front camera: all formats | Back camera: not supported  Front camera: most formats |
| [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) (back camera) | up to 4032 x 3024 pixels (12 MP) | up to 3264 x 2448 pixels (8 MP) | up to 3264 x 2448 pixels (8 MP) | up to 3840 x 2160 pixels (8 MP) |
| [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt) (front camera) | up to 3088 x 2320 pixels (7 MP) | no (same as video resolution) | no (same as video resolution) | up to 2576 x 1932 pixels (5 MP) |
| [Optical Image Stabilization (OIS)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzu) | Yes | No | No | No |
| [RAW Photo Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztge)  (back camera only) | Yes | No | No | Yes |
| [Focus Pixels](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzv) (back camera only) | Yes | No | No | Yes |
| [Cinematic Video Stabilization](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzw) | Yes | Yes | Yes | Yes |
| [Retina Flash](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzx) | Yes | Yes | No | Yes |
| [Live Photos](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzy) | Yes | Yes | No | Yes |
| [Wide-Gamut Color Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgq) | Yes | No | No | Yes |
| [Dual Camera](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgi) | No | No | No | No |
| [TrueDepth Camera](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztha) | No | No | No | No |

These subsections provide further details on the features listed in [Table 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzs) above.

Typically, you can set up a capture session using a session preset to quickly gain access to a common configuration of camera features, as described in [Use a Capture Session to Coordinate Data Flow](../Audio%20Video/AVFoundation%20Programming%20Guide/Still%20and%20Video%20Media%20Capture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydcobyfvbuqnjnknltcna). However, some specialized camera features—such as ultra high definition video, high frame rate, and the ability to capture high resolution stills during video capture—require an alternate approach. The [formats](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388738-formats) property of each [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object provides the full list of capture options for that device. To use specialized features, iterate through the `formats` array and examine the properties of each [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) object within to find the one whose features you want to use; then, set the device’s [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property to that format. (For details on the choice between session presets and capture formats, see _WWDC 2013: What’s New in Camera Capture_.)

By default, choosing the [AVCaptureSessionPresetPhoto](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetphoto) preset for the [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) [sessionPreset](https://developer.apple.com/documentation/avfoundation/avcapturesession/1389696-sessionpreset) property enables still image capture at the highest possible resolution for a device camera. To access lower-resolution formats, examine the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [formats](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388738-formats) array and choose a format to set as the [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) for the device.

For some devices, the front-facing camera does not output its maximum resolution for still images by default. To access the maximum still image resolution, see [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt).

If you configure capture using the [AVCaptureSessionPresetHigh](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1388084-high) preset, the captured video format is 1080p30 even on devices which support higher resolutions and frame rates. For 4K UHD resolution at 30 fps, use the [AVCaptureSessionPreset3840x2160](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1620474-hd4k3840x2160) preset.

To capture video at a higher frame rate in 1080p60 or 4K60 format, you must configure capture by choosing an appropriate [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) option for the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property. Note that the highest data rate formats (such as 4K60) require using the HEVC codec for recording.

To capture high frame rate video (and thus support smooth slow motion by playing back captured video at a lower frame rate), set the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice)[activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property to an [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) option whose [videoSupportedFrameRateRanges](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1387592-videosupportedframerateranges) property includes a high (120 FPS or greater) frame rate. Then, when capturing video, set the device’s [activeVideoMinFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389290-activevideominframeduration) and [activeVideoMaxFrameDuration](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1387816-activevideomaxframeduration) properties to reflect the frame rate you wish to use for capture. For example, to capture at 180 FPS on a device that supports 240 FPS capture, choose the format whose maximum frame rate is 240 FPS, then set the active min and max frame duration to `CMTimeMake(1, 180)`.

Note that the highest data rate formats (such as 1080p240) require using the HEVC codec for recording. To produce video files in a more compatible format, record in HEVC and then convert to a different format, or choose a format with a lower data rate (such as 1080p120).

On supported devices, the camera sensor itself provides continuous, streaming high-dynamic-range output, as opposed to the traditional method of fusing a bracket of still images with differing EV values into a single high dynamic range photo.

To enable or disable video HDR, use the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [automaticallyAdjustsVideoHDREnabled](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1624593-automaticallyadjustsvideohdrenab) property.

By default, photo and still image outputs capture images at the resolution specified by the [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property of the input [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) object. For example, while capturing a video at 640x480 resolution, still images are also captured at 640x480.

On supported devices, you can choose to capture high resolution still images during video capture. To enable this feature, use the [highResolutionPhotoEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648666-highresolutionphotoenabled) property in your photo settings for use with the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) class. The high resolution stills maintain the same aspect ratio and field of view as the active video format and are affected by video stabilization; use the [highResolutionStillImageDimensions](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/1624620-highresolutionstillimagedimensio) property of a capture format to find the dimensions used for still image capture.

Supported back-facing cameras include a mechanism to adjust the lens during capture to counter user hand-shake. Note that OIS is most effective for longer exposure times, and offers limited benefit for exposure times shorter than 1/30 second. To enable or disable image stabilization:

- For still images, use the [autoStillImageStabilizationEnabled](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/1648710-autostillimagestabilizationenabl) property in your photo settings for use with the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) class. When this property is enabled, supported devices employ both optical and digital image stabilization to achieve their best possible low-light performance.
- For bracketed capture of still images, on supported devices, see the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) [lensStabilizationDuringBracketedCaptureSupported](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/1648607-lensstabilizationduringbracketed) property and use the [AVCapturePhotoBracketSettings](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings) class to set up a bracketed capture. This controls optical stabilization separately from digital stabilization.
- For video capture, the [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection) [preferredVideoStabilizationMode](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620484-preferredvideostabilizationmode) property automatically enables both optical and digital stabilization on devices supporting video OIS.

In iOS 10 and later, the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) class enables capturing photos in RAW format on compatible devices. RAW formats provide minimally processed data from the camera’s image sensor, preserving much more of the color gamut, dynamic range, and other information for each pixel in the captured image.

For details on capturing in RAW format, see _[AVCapturePhotoOutput Class Reference](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput)_. To process captured RAW images, see _[Core Image Programming Guide](../Graphics%20Imaging/Core%20Image%20Programming%20Guide/About%20Core%20Image.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcobv)_.

On supported cameras, dedicated focus pixels provide depth information using phase detection. Continuous auto-focus changes are very fast and very subtle, so you can enable auto-focus during video recording without adding the throbbing effect of full focus scans to recorded video.

Focus pixels are always automatically enabled when the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [focusMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389191-focusmode) property is set to property to [AVCaptureFocusModeContinuousAutoFocus](https://developer.apple.com/documentation/avfoundation/avcapturefocusmode/avcapturefocusmodecontinuousautofocus).

To detect whether a capture format supports focus pixels, use the [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) property [autoFocusSystem](https://developer.apple.com/documentation/avfoundation/avcapturedeviceformat/1624600-autofocussystem). The value [AVCaptureAutoFocusSystemPhaseDetection](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/autofocussystem/phasedetection) corresponds to formats that support focus pixels.

All iPhone back-facing cameras supported by iOS 9 and later allow video stabilization. Some devices additionally support a more aggressive, dramatic, and fluid algorithm called cinematic video stabilization. This stabilization method reduces the camera’s field of view, introduces more latency in the video capture pipeline, and consumes more system memory compared to standard video stabilization; as such, you may wish to disable it in scenarios where you need more control over those aspects of the video capture process.

To enable or disable cinematic stabilization, use the [AVCaptureConnection](https://developer.apple.com/documentation/avfoundation/avcaptureconnection) [preferredVideoStabilizationMode](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620484-preferredvideostabilizationmode) property. In iOS 9 and later on supported devices, cinematic stabilization is the default when this property is set to [AVCaptureVideoStabilizationModeAuto](https://developer.apple.com/documentation/avfoundation/avcapturevideostabilizationmode/avcapturevideostabilizationmodeauto). After setting this property, use the [activeVideoStabilizationMode](https://developer.apple.com/documentation/avfoundation/avcaptureconnection/1620483-activevideostabilizationmode) property to determine whether cinematic stabilization was enabled—for formats that do not support cinematic stabilization, setting the preferred mode does not change the active mode.

On supported devices, the display brightness can briefly increase to 3 times its usual maximum illuminance for use as a flash for the front-facing camera. When using this feature, the display also varies its color output to achieve the same effect as the True Tone flash of the back-facing camera. No separate API controls this feature—on supported devices, the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [hasFlash](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388988-hasflash) property reflects the availability of Retina Flash for the front-facing camera. As with the back-facing camera, you can use the [isFlashModeSupported:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386434-isflashmodesupported) and [flashMode](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1388116-flashmode) properties to control the flash.

On supported devices, the built-in Camera app can produce pictures that include motion and sound from the moments just before and after capturing a still image. Use the [UIImagePickerController](https://developer.apple.com/documentation/uikit/uiimagepickercontroller) or [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) class to capture Live Photos and the [PHLivePhoto](https://developer.apple.com/documentation/photokit/phlivephoto) and [PHLivePhotoView](https://developer.apple.com/documentation/photokit/phlivephotoview) classes to work with and display Live Photo assets.

In iOS 10 and later, some devices and capture formats support capturing photos and video in the P3 color space, which covers a color gamut much broader than the sRGB color space. By default, a capture session automatically determines when to capture wide-gamut color, but you can also manually choose to capture in the sRGB or P3 color space.

When [AVCaptureSession](https://developer.apple.com/documentation/avfoundation/avcapturesession) [automaticallyConfiguresCaptureDeviceForWideColor](https://developer.apple.com/documentation/avfoundation/avcapturesession/1648764-automaticallyconfigurescapturede) property is enabled (the default), the session automatically chooses whether to enable wide-gamut capture and configures the capture pipeline accordingly, based on your session configuration. If this property is enabled on a device that supports wide-color capture:

- If your session includes an [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) object, the session automatically attempts to enable wide-color capture. However, adding other outputs to the session may disable automatic wide-color configuration, as noted below.
- If your session includes an [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput) object, the session does not automatically enable wide-color capture. (The [AVCaptureStillImageOutput](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput) class is deprecated in iOS 10.0; use the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) class instead to more easily support a broader set of photography features.)
- If your session includes an [AVCaptureVideoDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturevideodataoutput) object, and also includes an [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) and is using the [AVCaptureSessionPresetPhoto](https://developer.apple.com/documentation/avfoundation/avcapturesessionpresetphoto) session preset, the session automatically attempts to enable wide-color capture.
- If your session includes an [AVCaptureMovieFileOutput](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput) object, the session does not automatically enable wide-color capture.

For configurations listed above that don’t automatically enable wide-color capture, you can manually enable it by disabling the session’s [automaticallyConfiguresCaptureDeviceForWideColor](https://developer.apple.com/documentation/avfoundation/avcapturesession/1648764-automaticallyconfigurescapturede) property and setting the device’s [activeColorSpace](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1648668-activecolorspace) property.

In all of the above cases, if your session uses a session preset other than [AVCaptureSessionPresetInputPriority](https://developer.apple.com/documentation/avfoundation/avcapturesession/preset/1620473-inputpriority), the session automatically both enables wide-gamut color and selects a capture format that supports wide-gamut color. If you choose the input priority session preset (either directly or by setting the capture device’s [activeFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1389221-activeformat) property), the session automatically enables wide-color capture only if you’ve selected a capture format that supports wide color.

A dual camera is two separate back-facing cameras—one wide-angle, the other telephoto—that can work together as a single capture device. When setting up a capture session on a device with an dual camera, you can choose to use only the wide-angle camera, only the telephoto camera, or the dual camera. Choosing the dual camera capture device provides behavior similar to the built-in Camera app—the system automatically chooses which camera to use during capture, and can combine data from both cameras to improve capture output.

The [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [devices](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1386237-devices) and [devicesWithMediaType:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/1390520-devices) methods are deprecated in iOS 10 and later, and do not provide access to the dual camera device (instead, they provide only the wide-angle camera device). To determine whether a device contains a dual camera and select it for capture, you may either:

- Call the [AVCaptureDevice](https://developer.apple.com/documentation/avfoundation/avcapturedevice) [defaultDeviceWithDeviceType:mediaType:position:](https://developer.apple.com/documentation/avfoundation/avcapturedevice/2361508-default) method, passing the [AVCaptureDeviceTypeBuiltInDualCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevicetypebuiltindualcamera) device type. If this method returns non-`nil`, the iOS device contains a dual camera. (If this method returns `nil`, you can call it again, passing the [builtInWideAngleCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype/2361449-builtinwideanglecamera) device type, to obtain the default back camera.)
- Create an [AVCaptureDeviceDiscoverySession](https://developer.apple.com/documentation/avfoundation/avcapturedevicediscoverysession) object, passing the device attributes you want to use for capture, and enumerate its [devices](https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/2361002-devices) list to choose a device for your capture session.

When you use the dual camera capture device, [Optical Image Stabilization (OIS)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzu), [RAW Photo Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztge), [High Frame Rate (HFR) / Slow Motion Video](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgi), and most manual controls are not available. To use these features, specifically select either the wide or telephoto capture device. (For OIS, specifically select the wide-angle camera; the telephoto camera does not support optical image stabilization.)

In iOS 11, you can use the dual camera to capture depth maps as well as color imagery. See [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) and [AVCaptureDepthDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput).

The front-facing TrueDepth camera combines a high-resolution color camera with an infrared camera and structured light projector to create a single capture device capable of depth sensing as well as color imaging.

Use the following technologies to take advantage of high-level features provided by the TrueDepth camera:

- [ARKit](https://developer.apple.com/documentation/arkit): Create augmented reality experiences that interact with the user’s face in the front-facing camera image, or create animated characters whose face movements follow the user’s (as seen in the Animoji iMessage app).
- [LocalAuthentication](https://developer.apple.com/documentation/localauthentication): Authenticate the user with facial biometrics.

The AVFoundation framework provides two ways to access the TrueDepth camera:

- Selecting the front-facing camera with the [AVCaptureDeviceTypeBuiltInWideAngleCamera](https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype/2361449-builtinwideanglecamera) device type results in a capture device representing only the color camera component of the TrueDepth camera. This capture device is functionally equivalent to the front-facing cameras on other iOS devices, offering both photo and video capture.
- In iOS 11.1 and later, selecting the front-facing camera with the `AVCaptureDeviceTypeBuiltInTrueDepthCamera` device type returns a capture device representing the full capabilities of the TrueDepth camera. When you run a capture session using this device, you can use features of the [AVCapturePhotoOutput](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput) and [AVCaptureDepthDataOutput](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput) classes to enable capture of depth maps along with or instead of color imagery.

The tables below list all of the supported [AVCaptureDeviceFormat](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format) configurations for recent iPhone cameras in iOS 11. For an explanation of the data in each table column, see Table 4-3.

- iPhone 8, iPhone 8 Plus, and iPhone X: [Table 4-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzthe), [Table 4-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzuga), [Table 4-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzuge), [Table 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzugi), [Table 4-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzugm)
- iPhone 7 and iPhone 7 Plus: [Table 4-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgm), [Table 4-10](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgq), [Table 4-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgu), [Table 4-12](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztgy)
- iPhone 6s and iPhone 6s Plus: [Table 4-13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsgi), [Table 4-14](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsgm), [Table 4-15](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsha)
- iPhone 6 and iPhone 6 Plus: [Table 4-16](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsgq), [Table 4-17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsgu)
- iPhone SE: [Table 4-18](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsgy), [Table 4-19](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzsg4)
- iPad Pro (9.7-inch): [Table 4-25](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzshe), [Table 4-26](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvztga)

__Table 4-3__  Key to Device Capture Format Tables

| Column Name | Details |
| Type | The media subtype identifier for the format. |
| Dimensions | The pixel dimensions of captured video. |
| FPS | Frames Per Second: The range of video capture rates supported by the format. |
| HRSI | High Resolution Still Image: The pixel dimensions of still images that can be captured during video recording. (See [High Resolution Still Images During Video Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzt).) |
| FOV | Field Of View: The horizontal view angle for captured video. |
| Binned | Indicates whether the format produces video data in a binned format (a pixel-combining process that results in greater low-light sensitivity at the cost of reduced resolution). |
| VIS | Video Image Stabilization options supported:  S - Standard  C - Cinematic |
| Zoom | The maximum zoom factor for the format. |
| Upscales | The threshold at which increasing zoom factor causes the captured image to be upscaled (reducing image quality). |
| AF | Auto Focus system supported:  P - Phase detection (focus pixels; faster)  C - Contrast detection (slower) |
| ISO | The range of ISO exposure values supported by the format. |
| SS | The range of shutter speeds (in seconds) supported by the format. |
| VHDR | Indicates whether the format supports video / streaming HDR capture. (See [Single-Shot / Video HDR](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzz).) |
| Color | The widest-gamut color space the format supports for capture. (See [Wide-Gamut Color Capture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztkojzfvbuqmjqg4wvgvzrgq).) |

__Table 4-4__  iPhone 8 / iPhone 8 Plus / iPhone X Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 21.00 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 21.00 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-60 | 3696 x 3024 | 53.994 | NO |  | 189.00 | 10.50 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-60 | 3696 x 3024 | 53.994 | NO |  | 189.00 | 10.50 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 8.40 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 8.40 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 6.30 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 6.30 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 3.15 | C | 22-1760 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 640 x 480 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 3.15 | C | 22-1760 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4224 x 2376 | 60.983 | NO | S | 135.00 | 4.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4224 x 2376 | 60.983 | NO | S | 135.00 | 4.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-60 |  | 60.983 | YES | SC | 61.88 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-60 |  | 60.983 | YES | SC | 61.88 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 60.983 | YES | S | 67.50 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 60.983 | YES | S | 67.50 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1440 x 1080 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 1.40 | C | 22-1760 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1440 x 1080 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 1.40 | C | 22-1760 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 5-120 |  | 60.983 | NO | S | 135.00 | 2.00 | P | 22-880 | 0.000012 - 0.2 | NO | sRGB |
| 420f | 1920 x 1080 | 5-120 |  | 60.983 | NO | S | 135.00 | 2.00 | P | 22-880 | 0.000012 - 0.2 | NO | P3 |
| 420v | 1920 x 1080 | 6-240 |  | 60.983 | YES | S | 67.50 | 1.00 | C | 22-880 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1920 x 1080 | 6-240 |  | 60.983 | YES | S | 67.50 | 1.00 | C | 22-880 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.56 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.56 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.24 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.24 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 60.983 | NO | S | 9.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 60.983 | NO | S | 9.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-60 |  | 60.983 | NO | S | 135.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-60 |  | 60.983 | NO | S | 135.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.00 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.00 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |

__Table 4-5__  iPhone 8 / iPhone 8 Plus / iPhone X Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 16.08 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 192 x 144 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 16.08 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 352 x 288 | 2-30 | 2836 x 2320 | 51.943 | NO |  | 145.00 | 8.06 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 352 x 288 | 2-30 | 2836 x 2320 | 51.943 | NO |  | 145.00 | 8.06 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 480 x 360 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 6.43 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 480 x 360 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 6.43 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 640 x 480 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 4.82 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 4.82 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 640 x 480 | 2-60 | 1440 x 1080 | 42.612 | YES |  | 67.50 | 2.25 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-60 | 1440 x 1080 | 42.612 | YES |  | 67.50 | 2.25 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 960 x 540 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 4.00 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 960 x 540 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 4.00 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1280 x 720 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 3.00 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 720 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 3.00 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1280 x 720 | 2-60 | 1920 x 1080 | 67.284 | YES |  | 67.50 | 1.50 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 720 | 2-60 | 1920 x 1080 | 67.284 | YES |  | 67.50 | 1.50 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1440 x 1080 | 2-60 | 1440 x 1080 | 42.612 | YES |  | 67.50 | 1.00 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1440 x 1080 | 2-60 | 1440 x 1080 | 42.612 | YES |  | 67.50 | 1.00 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1920 x 1080 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 2.00 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1920 x 1080 | 2-30 | 3840 x 2160 | 67.564 | NO |  | 135.00 | 2.00 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |
| 420v | 3088 x 2320 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 1.00 |  | 19-1824 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 3088 x 2320 | 2-30 | 3088 x 2320 | 56.559 | NO |  | 145.00 | 1.00 |  | 19-1824 | 0.000013 - 0.5 | NO | P3 |

__Table 4-6__  iPhone 8 Plus / iPhone 10,3 Back Dual Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 21.00 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 21.00 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-60 | 3696 x 3024 | 53.994 | NO |  | 189.00 | 10.50 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-60 | 3696 x 3024 | 53.994 | NO |  | 189.00 | 10.50 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 8.40 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 8.40 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 6.30 | P | 22-1760 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-60 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 6.30 | P | 22-1760 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 3.15 | C | 22-1760 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 640 x 480 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 3.15 | C | 22-1760 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4224 x 2376 | 60.983 | NO | S | 135.00 | 4.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4224 x 2376 | 60.983 | NO | S | 135.00 | 4.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 24.00 | 3.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-60 |  | 60.983 | YES | SC | 61.88 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-60 |  | 60.983 | YES | SC | 61.88 | 1.50 | C | 22-880 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1440 x 1080 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 1.40 | C | 22-1760 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1440 x 1080 | 6-60 | 2016 x 1512 | 56.205 | YES |  | 94.50 | 1.40 | C | 22-1760 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4224 x 2376 | 60.983 | NO | SC | 16.00 | 2.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.56 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.56 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.24 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.24 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 60.983 | NO | S | 9.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 60.983 | NO | S | 9.00 | 1.00 | P | 22-880 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.00 | P | 22-2112 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 | 4032 x 3024 | 58.903 | NO |  | 189.00 | 1.00 | P | 22-2112 | 0.000020 - 0.333333 | NO | P3 |

__Table 4-7__  iPhone 8 Plus Back Telephoto Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 21.00 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 21.00 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-60 | 3696 x 3024 | 29.782 | NO |  | 189.00 | 10.50 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-60 | 3696 x 3024 | 29.782 | NO |  | 189.00 | 10.50 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 8.40 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 8.40 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 6.30 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-60 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 6.30 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 6-60 | 2016 x 1512 | 30.999 | YES |  | 94.50 | 3.15 | C | 20-1280 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 640 x 480 | 6-60 | 2016 x 1512 | 30.999 | YES |  | 94.50 | 3.15 | C | 20-1280 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4224 x 2376 | 33.907 | NO | S | 135.00 | 4.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4224 x 2376 | 33.907 | NO | S | 135.00 | 4.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-30 | 4224 x 2376 | 33.907 | NO | SC | 24.00 | 3.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4224 x 2376 | 33.907 | NO | SC | 24.00 | 3.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4224 x 2376 | 33.907 | NO | SC | 24.00 | 3.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4224 x 2376 | 33.907 | NO | SC | 24.00 | 3.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-60 |  | 33.907 | YES | SC | 61.88 | 1.50 | C | 20-640 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-60 |  | 33.907 | YES | SC | 61.88 | 1.50 | C | 20-640 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 33.907 | YES | S | 67.50 | 1.50 | C | 20-640 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 33.907 | YES | S | 67.50 | 1.50 | C | 20-640 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1440 x 1080 | 6-60 | 2016 x 1512 | 30.999 | YES |  | 94.50 | 1.40 | C | 20-1280 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1440 x 1080 | 6-60 | 2016 x 1512 | 30.999 | YES |  | 94.50 | 1.40 | C | 20-1280 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4224 x 2376 | 33.907 | NO | SC | 16.00 | 2.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4224 x 2376 | 33.907 | NO | SC | 16.00 | 2.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4224 x 2376 | 33.907 | NO | SC | 16.00 | 2.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4224 x 2376 | 33.907 | NO | SC | 16.00 | 2.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 5-120 |  | 33.907 | NO | S | 135.00 | 2.00 | P | 20-640 | 0.000012 - 0.2 | NO | sRGB |
| 420f | 1920 x 1080 | 5-120 |  | 33.907 | NO | S | 135.00 | 2.00 | P | 20-640 | 0.000012 - 0.2 | NO | P3 |
| 420v | 1920 x 1080 | 6-240 |  | 33.907 | YES | S | 67.50 | 1.00 | C | 20-640 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1920 x 1080 | 6-240 |  | 33.907 | YES | S | 67.50 | 1.00 | C | 20-640 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.56 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.56 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.24 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.24 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 33.907 | NO | S | 9.00 | 1.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 33.907 | NO | S | 9.00 | 1.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-60 |  | 33.907 | NO | S | 135.00 | 1.00 | P | 20-640 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-60 |  | 33.907 | NO | S | 135.00 | 1.00 | P | 20-640 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.00 | P | 20-1280 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 | 4032 x 3024 | 32.490 | NO |  | 189.00 | 1.00 | P | 20-1280 | 0.000020 - 0.333333 | NO | P3 |

__Table 4-8__  iPhone X Back Telephoto Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 21.00 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 21.00 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-60 | 3696 x 3024 | 29.710 | NO |  | 189.00 | 10.50 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-60 | 3696 x 3024 | 29.710 | NO |  | 189.00 | 10.50 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 8.40 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 8.40 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 6.30 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-60 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 6.30 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 6-60 | 2016 x 1512 | 30.924 | YES |  | 94.50 | 3.15 | C | 15-960 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 640 x 480 | 6-60 | 2016 x 1512 | 30.924 | YES |  | 94.50 | 3.15 | C | 15-960 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4224 x 2376 | 33.825 | NO | S | 135.00 | 4.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4224 x 2376 | 33.825 | NO | S | 135.00 | 4.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-30 | 4224 x 2376 | 33.825 | NO | SC | 24.00 | 3.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4224 x 2376 | 33.825 | NO | SC | 24.00 | 3.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4224 x 2376 | 33.825 | NO | SC | 24.00 | 3.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4224 x 2376 | 33.825 | NO | SC | 24.00 | 3.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-60 |  | 33.825 | YES | SC | 61.88 | 1.50 | C | 15-480 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-60 |  | 33.825 | YES | SC | 61.88 | 1.50 | C | 15-480 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 33.825 | YES | S | 67.50 | 1.50 | C | 15-480 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 33.825 | YES | S | 67.50 | 1.50 | C | 15-480 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1440 x 1080 | 6-60 | 2016 x 1512 | 30.924 | YES |  | 94.50 | 1.40 | C | 15-960 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1440 x 1080 | 6-60 | 2016 x 1512 | 30.924 | YES |  | 94.50 | 1.40 | C | 15-960 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4224 x 2376 | 33.825 | NO | SC | 16.00 | 2.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4224 x 2376 | 33.825 | NO | SC | 16.00 | 2.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4224 x 2376 | 33.825 | NO | SC | 16.00 | 2.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4224 x 2376 | 33.825 | NO | SC | 16.00 | 2.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 5-120 |  | 33.825 | NO | S | 135.00 | 2.00 | P | 15-480 | 0.000012 - 0.2 | NO | sRGB |
| 420f | 1920 x 1080 | 5-120 |  | 33.825 | NO | S | 135.00 | 2.00 | P | 15-480 | 0.000012 - 0.2 | NO | P3 |
| 420v | 1920 x 1080 | 6-240 |  | 33.825 | YES | S | 67.50 | 1.00 | C | 15-480 | 0.000011 - 0.166666 | NO | sRGB |
| 420f | 1920 x 1080 | 6-240 |  | 33.825 | YES | S | 67.50 | 1.00 | C | 15-480 | 0.000011 - 0.166666 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.56 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.56 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.24 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.24 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 33.825 | NO | S | 9.00 | 1.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 33.825 | NO | S | 9.00 | 1.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-60 |  | 33.825 | NO | S | 135.00 | 1.00 | P | 15-480 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-60 |  | 33.825 | NO | S | 135.00 | 1.00 | P | 15-480 | 0.000020 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.00 | P | 15-960 | 0.000020 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 | 4032 x 3024 | 32.411 | NO |  | 189.00 | 1.00 | P | 15-960 | 0.000020 - 0.333333 | NO | P3 |

__Table 4-9__  iPhone 7 Back Camera / iPhone 7 Plus Back (Wide-Angle) Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 59.680 | YES | S | 65.50 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 59.680 | YES | S | 65.50 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 6-120 |  | 59.680 | YES | S | 65.50 | 1.00 | C | 22-704 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1920 x 1080 | 6-120 |  | 59.680 | YES | S | 65.50 | 1.00 | C | 22-704 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 130.88 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 130.88 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |

__Table 4-10__  iPhone 7 Plus Back Telephoto Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 21.00 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 21.00 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 30.063 | NO |  | 189.00 | 10.50 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 30.063 | NO |  | 189.00 | 10.50 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 8.40 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 8.40 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 6.30 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 32.796 | NO |  | 189.00 | 6.30 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 33.280 | NO | S | 130.88 | 3.88 | P | 19-608 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 33.280 | NO | S | 130.88 | 3.88 | P | 19-608 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 33.280 | NO | SC | 120.00 | 2.91 | P | 19-608 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 33.280 | NO | SC | 120.00 | 2.91 | P | 19-608 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 33.280 | YES | S | 65.50 | 1.45 | C | 19-608 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 33.280 | YES | S | 65.50 | 1.45 | C | 19-608 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 33.280 | NO | SC | 16.00 | 1.94 | P | 19-608 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 33.280 | NO | SC | 16.00 | 1.94 | P | 19-608 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 33.280 | NO | SC | 16.00 | 1.94 | P | 19-608 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 33.280 | NO | SC | 16.00 | 1.94 | P | 19-608 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 6-120 |  | 33.280 | YES | S | 65.50 | 1.00 | C | 19-608 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1920 x 1080 | 6-120 |  | 33.280 | YES | S | 65.50 | 1.00 | C | 19-608 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.804 | NO |  | 189.00 | 1.56 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 32.804 | NO |  | 189.00 | 1.56 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.804 | NO |  | 189.00 | 1.24 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 32.804 | NO |  | 189.00 | 1.24 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 33.280 | NO | S | 130.88 | 1.00 | P | 19-608 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 33.280 | NO | S | 130.88 | 1.00 | P | 19-608 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 |  | 32.804 | NO |  | 189.00 | 1.00 | P | 19-1216 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 32.804 | NO |  | 189.00 | 1.00 | P | 19-1216 | 0.000005 - 0.333333 | NO | P3 |

__Table 4-11__  iPhone 7 Plus Back Dual Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 130.88 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 130.88 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |

__Table 4-12__  iPhone 7 / iPhone 7 Plus Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 16.08 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 192 x 144 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 16.08 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 352 x 288 | 2-30 | 2836 x 2320 | 49.778 | NO |  | 145.00 | 8.06 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 352 x 288 | 2-30 | 2836 x 2320 | 49.778 | NO |  | 145.00 | 8.06 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 480 x 360 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 6.43 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 480 x 360 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 6.43 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 640 x 480 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 4.82 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 4.82 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 960 x 540 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 4.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 960 x 540 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 4.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1280 x 720 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 3.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 720 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 3.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1920 x 1080 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 2.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1920 x 1080 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 2.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 3088 x 2320 | 2-30 |  | 54.201 | NO |  | 145.00 | 1.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 3088 x 2320 | 2-30 |  | 54.201 | NO |  | 145.00 | 1.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |

__Table 4-13__  iPhone 6s Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420f | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 4032 x 3024 | 3-30 |  | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |

__Table 4-14__  iPhone 6s Plus Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 52.900 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 52.900 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 57.710 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-30 | 4096 x 2304 | 58.640 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-30 | 4096 x 2304 | 58.640 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 58.640 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 58.640 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-30 | 4096 x 2304 | 58.640 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4096 x 2304 | 58.640 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 58.640 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 58.640 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 5-240 |  | 58.640 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420f | 1280 x 720 | 5-240 |  | 58.640 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.640 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.640 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.640 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.640 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-120 |  | 58.640 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-120 |  | 58.640 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.724 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.724 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.724 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.724 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3840 x 2160 | 3-30 |  | 58.640 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 58.640 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 4032 x 3024 | 3-30 |  | 57.724 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 57.724 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |

__Table 4-15__  iPhone 6s / iPhone 6s Plus Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 960 | 2-60 | 2576 x 1932 | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 960 | 2-60 | 2576 x 1932 | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | NO | sRGB |

__Table 4-16__  iPhone 6 / iPhone 6 Plus Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 17.00 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 192 x 144 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 17.00 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420v | 352 x 288 | 2-30 | 2992 x 2448 | 53.203 | NO |  | 153.00 | 8.50 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 352 x 288 | 2-30 | 2992 x 2448 | 53.203 | NO |  | 153.00 | 8.50 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420v | 480 x 360 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 6.80 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 480 x 360 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 6.80 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420v | 640 x 480 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 5.10 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 5.10 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420v | 960 x 540 | 2-30 | 3264 x 1836 | 58.040 | NO | S | 104.38 | 3.09 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420f | 960 x 540 | 2-30 | 3264 x 1836 | 58.040 | NO | S | 104.38 | 3.09 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420v | 1280 x 720 | 2-30 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 2.32 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420f | 1280 x 720 | 2-30 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 2.32 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420v | 1280 x 720 | 5-240 |  | 54.626 | YES | S | 49.12 | 1.09 | C | 29-928 | 0.000006 - 0.2 | NO | sRGB |
| 420f | 1280 x 720 | 5-240 |  | 54.626 | YES | S | 49.12 | 1.09 | C | 29-928 | 0.000006 - 0.2 | NO | sRGB |
| 420v | 1920 x 1080 | 2-30 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 1.55 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420f | 1920 x 1080 | 2-30 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 1.55 | P | 29-464 | 0.000025 - 0.5 | YES | sRGB |
| 420v | 1920 x 1080 | 2-60 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 1.55 | P | 29-464 | 0.000016 - 0.5 | YES | sRGB |
| 420f | 1920 x 1080 | 2-60 | 3264 x 1836 | 58.040 | NO | SC | 95.62 | 1.55 | P | 29-464 | 0.000016 - 0.5 | YES | sRGB |
| 420v | 2592 x 1936 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 1.26 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 2592 x 1936 | 2-30 | 3264 x 2448 | 58.040 | NO |  | 153.00 | 1.26 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420v | 3264 x 2448 | 2-30 |  | 58.040 | NO |  | 153.00 | 1.00 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |
| 420f | 3264 x 2448 | 2-30 |  | 58.040 | NO |  | 153.00 | 1.00 | P | 29-1856 | 0.000025 - 0.5 | NO | sRGB |

__Table 4-17__  iPhone 6 / iPhone 6 Plus Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 960 | 2-60 |  | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 960 | 2-60 |  | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |

__Table 4-18__  iPhone SE Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420f | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420v | 4032 x 3024 | 3-30 |  | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |

__Table 4-19__  iPhone SE Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 1-30 |  | 55.200 | NO |  | 60.00 | 6.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 192 x 144 | 1-30 |  | 55.200 | NO |  | 60.00 | 6.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 352 x 288 | 1-30 |  | 50.629 | NO |  | 60.00 | 3.33 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 352 x 288 | 1-30 |  | 50.629 | NO |  | 60.00 | 3.33 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 480 x 360 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 480 x 360 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 640 x 480 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 640 x 480 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 960 x 540 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.43 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 960 x 540 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.43 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 1280 x 720 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.08 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 1280 x 720 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.08 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 1280 x 960 | 1-30 |  | 55.200 | NO |  | 60.00 | 1.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 1280 x 960 | 1-30 |  | 55.200 | NO |  | 60.00 | 1.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |

__Table 4-20__  iPad Pro 12.9-inch (2nd generation) / iPad Pro 10.5-inch Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 21.00 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 54.060 | NO |  | 189.00 | 10.50 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 8.40 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 58.975 | NO |  | 189.00 | 6.30 | P | 22-1408 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 59.680 | NO | S | 130.88 | 3.88 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 120.00 | 2.91 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 6-60 |  | 59.680 | YES | SC | 60.00 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1280 x 720 | 6-60 |  | 59.680 | YES | SC | 60.00 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 1280 x 720 | 6-240 |  | 59.680 | YES | S | 65.50 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1280 x 720 | 6-240 |  | 59.680 | YES | S | 65.50 | 1.45 | C | 22-704 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 59.680 | NO | SC | 16.00 | 1.94 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 6-120 |  | 59.680 | YES | S | 65.50 | 1.00 | C | 22-704 | 0.000002 - 0.166667 | NO | sRGB |
| 420f | 1920 x 1080 | 6-120 |  | 59.680 | YES | S | 65.50 | 1.00 | C | 22-704 | 0.000002 - 0.166667 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.56 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 58.986 | NO |  | 189.00 | 1.24 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 9.00 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 59.680 | NO | S | 9.00 | 1.00 | P | 22-704 | 0.000005 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 |  | 58.986 | NO |  | 189.00 | 1.00 | P | 22-1760 | 0.000005 - 0.333333 | NO | P3 |

__Table 4-21__  iPad Pro 12.9-inch (2nd generation) / iPad Pro 10.5-inch Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 16.08 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 192 x 144 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 16.08 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 352 x 288 | 2-30 | 2836 x 2320 | 49.778 | NO |  | 145.00 | 8.06 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 352 x 288 | 2-30 | 2836 x 2320 | 49.778 | NO |  | 145.00 | 8.06 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 480 x 360 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 6.43 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 480 x 360 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 6.43 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 640 x 480 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 4.82 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 4.82 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 960 x 540 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 4.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 960 x 540 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 4.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1280 x 720 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 3.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 720 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 3.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 1920 x 1080 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 2.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1920 x 1080 | 2-30 | 3840 x 2160 | 64.164 | NO |  | 135.00 | 2.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |
| 420v | 3088 x 2320 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 1.00 |  | 23-2208 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 3088 x 2320 | 2-30 | 3088 x 2320 | 54.201 | NO |  | 145.00 | 1.00 |  | 23-2208 | 0.000013 - 0.5 | NO | P3 |

__Table 4-22__  iPad (5th generation) / iPad Pro (12.9-inch) Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 17.00 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 192 x 144 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 17.00 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 352 x 288 | 2-30 | 2992 x 2448 | 49.745 | NO |  | 153.00 | 8.50 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 352 x 288 | 2-30 | 2992 x 2448 | 49.745 | NO |  | 153.00 | 8.50 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 480 x 360 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 6.80 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 480 x 360 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 6.80 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 640 x 480 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 5.10 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 640 x 480 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 5.10 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 960 x 540 | 2-30 | 3264 x 1836 | 54.267 | NO | S | 104.38 | 3.09 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 960 x 540 | 2-30 | 3264 x 1836 | 54.267 | NO | S | 104.38 | 3.09 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 1280 x 720 | 2-30 | 3264 x 1836 | 54.267 | NO | SC | 95.62 | 2.32 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 1280 x 720 | 2-30 | 3264 x 1836 | 54.267 | NO | SC | 95.62 | 2.32 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 1280 x 720 | 3-60 |  | 54.267 | YES | SC | 47.75 | 1.16 | C | 24-768 | 0.000025 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 |  | 54.267 | YES | SC | 47.75 | 1.16 | C | 24-768 | 0.000025 - 0.333333 | NO | sRGB |
| 420v | 1280 x 720 | 3-120 |  | 54.267 | YES | S | 52.12 | 1.16 | C | 24-768 | 0.000025 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-120 |  | 54.267 | YES | S | 52.12 | 1.16 | C | 24-768 | 0.000025 - 0.333333 | NO | sRGB |
| 420v | 1920 x 1080 | 2-30 | 3264 x 1836 | 54.267 | NO | SC | 95.62 | 1.55 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 1920 x 1080 | 2-30 | 3264 x 1836 | 54.267 | NO | SC | 95.62 | 1.55 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 2592 x 1936 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 1.26 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 2592 x 1936 | 2-30 | 3264 x 2448 | 54.267 | NO |  | 153.00 | 1.26 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420v | 3264 x 2448 | 2-30 |  | 54.267 | NO |  | 153.00 | 1.00 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |
| 420f | 3264 x 2448 | 2-30 |  | 54.267 | NO |  | 153.00 | 1.00 | C | 24-768 | 0.000024 - 0.5 | NO | sRGB |

__Table 4-23__  iPad (5th generation) Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 1-30 |  | 55.200 | NO |  | 60.00 | 6.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 192 x 144 | 1-30 |  | 55.200 | NO |  | 60.00 | 6.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 352 x 288 | 1-30 |  | 50.629 | NO |  | 60.00 | 3.33 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 352 x 288 | 1-30 |  | 50.629 | NO |  | 60.00 | 3.33 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 480 x 360 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 480 x 360 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.67 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 640 x 480 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 640 x 480 | 1-30 |  | 55.200 | NO |  | 60.00 | 2.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 960 x 540 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.43 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 960 x 540 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.43 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 1280 x 720 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.08 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 1280 x 720 | 1-30 |  | 59.340 | NO |  | 48.50 | 1.08 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420v | 1280 x 960 | 1-30 |  | 55.200 | NO |  | 60.00 | 1.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |
| 420f | 1280 x 960 | 1-30 |  | 55.200 | NO |  | 60.00 | 1.00 |  | 47-1504 | 0.000031 - 1 | NO | sRGB |

__Table 4-24__  iPad Pro (12.9-inch) Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420v | 1280 x 960 | 2-60 |  | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 960 | 2-60 |  | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |

__Table 4-25__  iPad Pro (9.7-inch) Back Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 192 x 144 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 21.00 | P | 23-1472 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 352 x 288 | 3-30 | 3696 x 3024 | 52.893 | NO |  | 189.00 | 10.50 | P | 23-1472 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 480 x 360 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 8.40 | P | 23-1472 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 640 x 480 | 3-30 | 4032 x 3024 | 57.702 | NO |  | 189.00 | 6.30 | P | 23-1472 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-30 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 960 x 540 | 3-60 | 4096 x 2304 | 58.632 | NO | S | 130.88 | 3.88 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1280 x 720 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 120.00 | 2.91 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | sRGB |
| 420f | 1280 x 720 | 5-240 |  | 58.632 | YES | S | 65.50 | 1.45 | C | 23-736 | 0.000006 - 0.2 | NO | P3 |
| 420v | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-30 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-60 | 4096 x 2304 | 58.632 | NO | SC | 4.00 | 1.94 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 1920 x 1080 | 3-120 |  | 58.632 | YES | S | 65.50 | 1.00 | C | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 2592 x 1936 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.56 | P | 23-1840 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3264 x 2448 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.24 | P | 23-1840 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 3840 x 2160 | 3-30 |  | 58.632 | NO | S | 130.88 | 1.00 | P | 23-736 | 0.000013 - 0.333333 | NO | P3 |
| 420v | 4032 x 3024 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | sRGB |
| 420f | 4032 x 3024 | 3-30 | 4032 x 3024 | 57.716 | NO |  | 189.00 | 1.00 | P | 23-1840 | 0.000013 - 0.333333 | NO | P3 |

__Table 4-26__  iPad Pro (9.7-inch) Front Camera

| Type | Dimensions | FPS | HRSI | FOV | Binned | VIS | Zoom | Upscale | AF | ISO | SS | VHDR | Color |
| 420v | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 192 x 144 | 2-60 |  | 54.400 | NO |  | 60.00 | 6.67 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 352 x 288 | 2-60 |  | 49.895 | NO |  | 60.00 | 3.33 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 480 x 360 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.67 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 640 x 480 | 2-60 |  | 54.400 | NO |  | 60.00 | 2.00 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 960 x 540 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.43 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | sRGB |
| 420f | 1280 x 720 | 2-60 |  | 58.480 | NO |  | 48.50 | 1.08 |  | 34-2176 | 0.000013 - 0.5 | YES | P3 |
| 420v | 1280 x 960 | 2-60 | 2576 x 1932 | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | NO | sRGB |
| 420f | 1280 x 960 | 2-60 | 2576 x 1932 | 54.400 | NO |  | 60.00 | 1.00 |  | 34-2176 | 0.000013 - 0.5 | NO | P3 |

[Next](Document%20Revision%20History.md)[Previous](Graphics%20Processors.md)


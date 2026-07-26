---
title: AVCapturePhotoOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput.json'
content_hash: 'sha256:bc49b572ab5a2ac9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoOutput

<sub>Class</sub>

A capture output for still image, Live Photos, and other photography workflows.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCapturePhotoOutput
```

## Overview

[AVCapturePhotoOutput](avcapturephotooutput.md) provides an interface for capture workflows related to still photography. In addition to basic capture of still images, a photo output supports RAW-format capture, bracketed capture of multiple images, Live Photos, and wide-gamut color. You can output captured photos in a variety of formats and codecs, including RAW format DNG files, HEVC format HEIF files, and JPEG files.

To capture photos with the [AVCapturePhotoOutput](avcapturephotooutput.md) class, follow these steps:

1. Create an [AVCapturePhotoOutput](avcapturephotooutput.md) object. Use its properties to determine supported capture settings and to enable certain features (for example, whether to capture Live Photos).
2. Create and configure an [AVCapturePhotoSettings](avcapturephotosettings.md) object to choose features and settings for a specific capture (for example, whether to enable image stabilization or flash).
3. Capture an image by passing your photo settings object to the [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method along with a delegate object implementing the [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) protocol. The photo capture output then calls your delegate to notify you of significant events during the capture process.

Some photo capture settings, such as the [flashMode](avcapturephotosettings/flashmode.md) property, include options for automatic behavior. For such settings, the photo output determines whether to use that feature at the moment of capture—you don’t know when requesting a capture whether the feature will be enabled when the capture completes. When the photo capture output calls your [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) methods with information about the completed or in-progress capture, it also provides an [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md) object that details which automatic features are set for that capture. The resolved settings object’s [uniqueID](avcaptureresolvedphotosettings/uniqueid.md) property matches the [uniqueID](avcapturephotosettings/uniqueid.md) value of the [AVCapturePhotoSettings](avcapturephotosettings.md) object you used to request capture.

Enabling certain photo features (Live Photo capture and high resolution capture) requires a reconfiguration of the capture render pipeline. To opt into these features, set the [highResolutionCaptureEnabled](avcapturephotooutput/ishighresolutioncaptureenabled.md), [livePhotoCaptureEnabled](avcapturephotooutput/islivephotocaptureenabled.md), and [livePhotoAutoTrimmingEnabled](avcapturephotooutput/islivephotoautotrimmingenabled.md) properties before calling your [AVCaptureSession](avcapturesession.md) object’s [- startRunning](<avcapturesession/startrunning().md>) method. Changing any of these properties while the session is running disrupts the capture render pipeline: Live Photo captures in progress end immediately, unfulfilled photo requests abort, and video preview temporarily freezes.

Using a photo capture output adds other requirements to your [AVCaptureSession](avcapturesession.md) object:

- A capture session can’t support both Live Photo capture and movie file output. If your capture session includes an [AVCaptureMovieFileOutput](avcapturemoviefileoutput.md) object, the [livePhotoCaptureSupported](avcapturephotooutput/islivephotocapturesupported.md) property becomes [false](../swift/false.md). (As an alternative, you can use the [AVCaptureVideoDataOutput](avcapturevideodataoutput.md) class to output video buffers at the same resolution as a simultaneous Live Photo capture).
- A capture session can’t contain both an [AVCapturePhotoOutput](avcapturephotooutput.md) object and an [AVCaptureStillImageOutput](avcapturestillimageoutput.md) object. The [AVCapturePhotoOutput](avcapturephotooutput.md) class includes all functionality of (and deprecates) the [AVCaptureStillImageOutput](avcapturestillimageoutput.md) class.

The [AVCapturePhotoOutput](avcapturephotooutput.md) class implicitly supports wide-gamut color photography. If the source [AVCaptureDevice](avcapturedevice.md) object’s [activeColorSpace](avcapturedevice/activecolorspace.md) value is [AVCaptureColorSpace_P3_D65](avcapturecolorspace/p3_d65.md), the capture output produces photos with wide color information (unless your [AVCapturePhotoSettings](avcapturephotosettings.md) object specifies an output format that doesn’t support wide color).

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a photo output

- [- init](<avcapturephotooutput/init().md>) — Creates a new photo capture output object.

### Capturing a photo

- [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) — Initiates a photo capture using the specified settings.

### Managing responsive capture

- [captureReadiness](avcapturephotooutput/capturereadiness-swift.property.md) — A value that specifies whether the photo output is ready to respond to new capture requests in a timely manner.
- [CaptureReadiness](avcapturephotooutput/capturereadiness-swift.enum.md) — Constants that indicate whether the output is ready to receive capture requests.
- [autoDeferredPhotoDeliveryEnabled](avcapturephotooutput/isautodeferredphotodeliveryenabled.md) — A Boolean value that indicates the enabled state of automatic deferred photo delivery.
- [autoDeferredPhotoDeliverySupported](avcapturephotooutput/isautodeferredphotodeliverysupported.md) — A Boolean value that indicates whether the photo output supports deferred photo delivery.
- [fastCapturePrioritizationSupported](avcapturephotooutput/isfastcaptureprioritizationsupported.md) — A Boolean value that indicates whether the photo output supports fast capture prioritization.
- [fastCapturePrioritizationEnabled](avcapturephotooutput/isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the output enables fast capture prioritization.
- [responsiveCaptureSupported](avcapturephotooutput/isresponsivecapturesupported.md) — A Boolean value that indicates whether the photo output supports responsive capture.
- [responsiveCaptureEnabled](avcapturephotooutput/isresponsivecaptureenabled.md) — A Boolean value that indicates whether the photo output configuration enables responsive capture.
- [zeroShutterLagSupported](avcapturephotooutput/iszeroshutterlagsupported.md) — A Boolean value that indicates whether the photo output supports zero shutter lag.
- [zeroShutterLagEnabled](avcapturephotooutput/iszeroshutterlagenabled.md) — A Boolean value that indicates whether the photo output configuration enables zero shutter lag.

### Determining supported pixel formats

- [availablePhotoPixelFormatTypes](avcapturephotooutput/availablephotopixelformattypes-3ydgm.md) — The pixel formats the capture output supports for photo capture.
- [availableRawPhotoPixelFormatTypes](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md) — The pixel formats the capture output supports for RAW photo capture.
- [supportedPhotoPixelFormatTypes(for:)](<avcapturephotooutput/supportedphotopixelformattypes(for_).md>) — Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [supportedRawPhotoPixelFormatTypes(for:)](<avcapturephotooutput/supportedrawphotopixelformattypes(for_).md>) — Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [+ isAppleProRAWPixelFormat:](<avcapturephotooutput/isappleprorawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [+ isBayerRAWPixelFormat:](<avcapturephotooutput/isbayerrawpixelformat(__).md>) — Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.

### Determining supported codec types

- [availablePhotoCodecTypes](avcapturephotooutput/availablephotocodectypes.md) — The compression codecs this capture output currently supports for photo capture.
- [- supportedPhotoCodecTypesForFileType:](<avcapturephotooutput/supportedphotocodectypes(for_).md>) — Returns the list of photo codecs (such as JPEG or HEVC) supported for photo data in the specified file type.

### Determining supported file types

- [availablePhotoFileTypes](avcapturephotooutput/availablephotofiletypes.md) — The list of file types currently supported for photo capture and output.
- [availableRawPhotoFileTypes](avcapturephotooutput/availablerawphotofiletypes.md) — The list of file types currently supported for RAW format capture and output.

### Suppressing the shutter sound

- [shutterSoundSuppressionSupported](avcapturephotooutput/isshuttersoundsuppressionsupported.md) — A Boolean value that indicates whether the photo output supports suppressing the system shutter sound.

### Configuring ProRAW support

- [appleProRAWSupported](avcapturephotooutput/isappleprorawsupported.md) — A Boolean value that indicates whether the current device and configuration supports Apple ProRAW pixel formats.
- [appleProRAWEnabled](avcapturephotooutput/isappleprorawenabled.md) — A Boolean value that indicates whether you’ve configured the photo output to deliver Apple ProRAW formats.

### Determining available settings

- [contentAwareDistortionCorrectionSupported](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md) — A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [contentAwareDistortionCorrectionEnabled](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [lensStabilizationDuringBracketedCaptureSupported](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md) — A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [maxBracketedCapturePhotoCount](avcapturephotooutput/maxbracketedcapturephotocount.md) — The maximum number of images that the photo capture output can support in a single bracketed capture.
- [supportedFlashModes](avcapturephotooutput/supportedflashmodes-1n6nm.md) — A Swift array of flash settings this capture output currently supports.
- [autoRedEyeReductionSupported](avcapturephotooutput/isautoredeyereductionsupported.md) — A Boolean value indicating whether the capture output supports automatic red-eye reduction.

### Monitoring the visible scene

- [isFlashScene](avcapturephotooutput/isflashscene.md) — A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.
- [photoSettingsForSceneMonitoring](avcapturephotooutput/photosettingsforscenemonitoring.md) — A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.

### Configuring high-resolution still capture

- [maxPhotoDimensions](avcapturephotooutput/maxphotodimensions.md) — The maximum resolution of the requested photo.

### Configuring Live Photo capture

- [livePhotoCaptureSupported](avcapturephotooutput/islivephotocapturesupported.md) — A Boolean value that indicates whether the capture output currently supports Live Photo capture.
- [livePhotoCaptureEnabled](avcapturephotooutput/islivephotocaptureenabled.md) — A Boolean value that indicates whether to configure the capture pipeline for Live Photo capture.
- [livePhotoCaptureSuspended](avcapturephotooutput/islivephotocapturesuspended.md) — A Boolean value that indicates whether Live Photo capture is currently in a suspended state.
- [preservesLivePhotoCaptureSuspendedOnSessionStop](avcapturephotooutput/preserveslivephotocapturesuspendedonsessionstop.md) — A Boolean value that indicates whether to preserve the suspended state of Live Photo capture when the session stops.
- [livePhotoAutoTrimmingEnabled](avcapturephotooutput/islivephotoautotrimmingenabled.md) — A Boolean value that indicates whether to automatically trim Live Photo movie captures to avoid excessive movement.
- [availableLivePhotoVideoCodecTypes](avcapturephotooutput/availablelivephotovideocodectypes.md) — An array of video codecs currently available for Live Photo movie captures.

### Configuring depth data capture

- [depthDataDeliverySupported](avcapturephotooutput/isdepthdatadeliverysupported.md) — A Boolean value indicating whether the capture output currently supports depth data capture.
- [depthDataDeliveryEnabled](avcapturephotooutput/isdepthdatadeliveryenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for depth data capture.

### Configuring Portrait Effects matte capture

- [portraitEffectsMatteDeliveryEnabled](avcapturephotooutput/isportraiteffectsmattedeliveryenabled.md) — A Boolean value indicating whether the capture output generates a portrait effects matte.
- [portraitEffectsMatteDeliverySupported](avcapturephotooutput/isportraiteffectsmattedeliverysupported.md) — A Boolean value indicating whether the capture output currently supports delivery of a portrait effects matte.
- [portraitEffectsMatte](avcapturephoto/portraiteffectsmatte.md) — The portrait effects matte captured with the photo.

### Configuring constant color

- [constantColorSupported](avcapturephotooutput/isconstantcolorsupported.md) — A Boolean value that indicates whether a photo output supports constant color capture.
- [constantColorEnabled](avcapturephotooutput/isconstantcolorenabled.md) — A Boolean value that indicates whether the photo output configures the render pipeline to perform constant color capture.

### Configuring orientation compensation

- [cameraSensorOrientationCompensationSupported](avcapturephotooutput/iscamerasensororientationcompensationsupported.md)
- [cameraSensorOrientationCompensationEnabled](avcapturephotooutput/iscamerasensororientationcompensationenabled.md)

### Configuring virtual device capture

- [virtualDeviceFusionSupported](avcapturephotooutput/isvirtualdevicefusionsupported.md) — A Boolean value that indicates whether the device supports virtual device image fusion.
- [virtualDeviceConstituentPhotoDeliverySupported](avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.md) — A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.
- [virtualDeviceConstituentPhotoDeliveryEnabled](avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md) — A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.

### Preparing for resource-intensive captures

- [preparedPhotoSettingsArray](avcapturephotooutput/preparedphotosettingsarray.md) — An array of photo settings for which the photo output has prepared capture resources.
- [- setPreparedPhotoSettingsArray:completionHandler:](<avcapturephotooutput/setpreparedphotosettingsarray(__completionhandler_).md>) — Tells the photo capture output to prepare resources for future capture requests with the specified settings.

### Getting segmentation mattes

- [availableSemanticSegmentationMatteTypes](avcapturephotooutput/availablesemanticsegmentationmattetypes.md) — An array of semantic segmentation matte types that may be captured and delivered along with the primary photo.
- [enabledSemanticSegmentationMatteTypes](avcapturephotooutput/enabledsemanticsegmentationmattetypes.md) — The semantic segmentation matte types that the photo render pipeline delivers.

### Setting the capture prioritization

- [maxPhotoQualityPrioritization](avcapturephotooutput/maxphotoqualityprioritization.md) — The highest quality the photo output should prepare to deliver on a capture-by-capture basis.
- [QualityPrioritization](avcapturephotooutput/qualityprioritization.md) — Constants that indicate how to prioritize photo quality relative to capture speed.

### Determining calibration data delivery support

- [cameraCalibrationDataDeliverySupported](avcapturephotooutput/iscameracalibrationdatadeliverysupported.md) — A Boolean value that indicates whether the photo output currently supports the delivery of camera calibration data.

### Deprecated

- [Deprecated symbols](avcapturephotooutput-deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Instance properties

- [availableRawPhotoCodecTypes](avcapturephotooutput/availablerawphotocodectypes.md)

### Instance methods

- [- supportedRawPhotoCodecTypesForRawPhotoPixelFormatType:fileType:](<avcapturephotooutput/supportedrawphotocodectypes(forrawphotopixelformattype_filetype_).md>)

## See Also

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCapturePhoto](avcapturephoto.md) — A container for image data from a photo capture output.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — Methods for monitoring progress and receiving results from a photo capture output.
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

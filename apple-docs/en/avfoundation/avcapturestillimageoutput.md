---
title: AVCaptureStillImageOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput.json'
content_hash: 'sha256:a748409f5ce528da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureStillImageOutput

<sub>Class</sub>

A capture output for capturing still photos.

> [!warning] Deprecated
> Use [AVCapturePhotoOutput](avcapturephotooutput.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVCaptureStillImageOutput
```

## Relationships

- **Inherits From**: [AVCaptureOutput](avcaptureoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Capturing an image

- [- captureStillImageAsynchronouslyFromConnection:completionHandler:](<avcapturestillimageoutput/capturestillimageasynchronously(from_completionhandler_).md>) — Initiates a still image capture and returns immediately. _(deprecated)_
- [capturingStillImage](avcapturestillimageoutput/iscapturingstillimage.md) — Indicates whether a still image is being captured. _(deprecated)_

### Getting and setting image stabilization settings

- [stillImageStabilizationActive](avcapturestillimageoutput/isstillimagestabilizationactive.md) — Indicates whether still image stabilization is in use for the current capture. _(deprecated)_
- [automaticallyEnablesStillImageStabilizationWhenAvailable](avcapturestillimageoutput/automaticallyenablesstillimagestabilizationwhenavailable.md) — A Boolean value that indicates whether still image stabilization should be automatically enabled. _(deprecated)_
- [stillImageStabilizationSupported](avcapturestillimageoutput/isstillimagestabilizationsupported.md) — A Boolean value that indicates whether the  still image currently being captured supports still image stabilization. _(deprecated)_

### Configuring orientation compensation

- [cameraSensorOrientationCompensationSupported](avcapturestillimageoutput/iscamerasensororientationcompensationsupported.md) _(deprecated)_
- [cameraSensorOrientationCompensationEnabled](avcapturestillimageoutput/iscamerasensororientationcompensationenabled.md) _(deprecated)_

### Configuring image settings

- [highResolutionStillImageOutputEnabled](avcapturestillimageoutput/ishighresolutionstillimageoutputenabled.md) — A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property. _(deprecated)_
- [availableImageDataCVPixelFormatTypes](avcapturestillimageoutput/availableimagedatacvpixelformattypes.md) — The supported image pixel formats that can be specified as output settings. _(deprecated)_
- [availableImageDataCodecTypes](avcapturestillimageoutput/availableimagedatacodectypes.md) — The supported image codec formats that can be specified as output settings. _(deprecated)_
- [outputSettings](avcapturestillimageoutput/outputsettings.md) — The compression settings for the output. _(deprecated)_
- [Video settings](video-settings.md) — Configure video processing settings using standard key and value constants.

### Image format conversion

- [+ jpegStillImageNSDataRepresentation:](<avcapturestillimageoutput/jpegstillimagensdatarepresentation(__).md>) — Returns an `NSData` representation of a still image data and metadata attachments in a JPEG sample buffer. _(deprecated)_

### Still image bracketed capture

- [- captureStillImageBracketAsynchronouslyFromConnection:withSettingsArray:completionHandler:](<avcapturestillimageoutput/capturestillimagebracketasynchronously(from_withsettingsarray_completionhandler_).md>) — Captures a still image bracket. _(deprecated)_
- [maxBracketedCaptureStillImageCount](avcapturestillimageoutput/maxbracketedcapturestillimagecount.md) — Specifies the maximum number of still images that may be taken in a single bracket. _(deprecated)_
- [- prepareToCaptureStillImageBracketFromConnection:withSettingsArray:completionHandler:](<avcapturestillimageoutput/preparetocapturestillimagebracket(from_withsettingsarray_completionhandler_).md>) — Allows the receiver to prepare resources in advance of capturing a still image bracket. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureSupported](avcapturestillimageoutput/islensstabilizationduringbracketedcapturesupported.md) — A Boolean value that indicates whether the capture output supports lens stabilization across the duration of a bracketed capture. _(deprecated)_
- [lensStabilizationDuringBracketedCaptureEnabled](avcapturestillimageoutput/islensstabilizationduringbracketedcaptureenabled.md) — A Boolean value that specifies whether to stabilize the lens across the duration of a bracketed capture. _(deprecated)_

### Creating still image output

- [- init](<avcapturestillimageoutput/init().md>) — Creates new still image output. _(deprecated)_

## See Also

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCapturePhoto](avcapturephoto.md) — A container for image data from a photo capture output.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoOutput](avcapturephotooutput.md) — A capture output for still image, Live Photos, and other photography workflows.
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — Methods for monitoring progress and receiving results from a photo capture output.
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.

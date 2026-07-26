---
title: AVCapturePhoto
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto.json'
content_hash: 'sha256:7c94f10dd5255aeb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhoto

<sub>Class</sub>

A container for image data from a photo capture output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCapturePhoto
```

## Overview

When you capture photos with the [AVCapturePhotoOutput](avcapturephotooutput.md) class, your delegate object receives each resulting image and related data in the form of an [AVCapturePhoto](avcapturephoto.md) object. This object is an immutable wrapper from which you can retrieve various results of the photo capture.

In addition to the photo image pixel buffer, an AVCapturePhoto object can also contain a preview-sized pixel buffer, capture metadata, and, on supported devices, depth data and camera calibration data. From an [AVCapturePhoto](avcapturephoto.md) object, you can generate data appropriate for writing to a file, such as HEVC encoded image data containerized in the HEIC file format and including a preview image, depth data and other attachments.

An [AVCapturePhoto](avcapturephoto.md) instance wraps a single image result. For example, if you request a bracketed capture of three images, your callback is called three times, each time delivering a single [AVCapturePhoto](avcapturephoto.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Resolving photo capture requests

- [resolvedSettings](avcapturephoto/resolvedsettings.md) — The settings object that was used to request this photo capture.
- [photoCount](avcapturephoto/photocount.md) — The 1-based index of this photo capture relative to other results from the same capture request.
- [timestamp](avcapturephoto/timestamp.md) — The time at which the image was captured.

### Accessing photo pixel data

- [rawPhoto](avcapturephoto/israwphoto.md) — A Boolean value indicating whether this photo object contains RAW format data.
- [pixelBuffer](avcapturephoto/pixelbuffer.md) — The uncompressed or RAW image sample buffer for the photo, if requested.

### Accessing preview photo data

- [embeddedThumbnailPhotoFormat](avcapturephoto/embeddedthumbnailphotoformat.md) — A dictionary describing the data format for a preview-sized image accompanying the captured photo.
- [previewPixelBuffer](avcapturephoto/previewpixelbuffer.md) — The pixel data for a preview-sized version of the photo, if requested.

### Accessing photo metadata

- [depthData](avcapturephoto/depthdata.md) — Depth or disparity map data captured with the photo.
- [cameraCalibrationData](avcapturephoto/cameracalibrationdata.md) — Calibration information for the camera device that captured the photo.
- [sourceDeviceType](avcapturephoto/sourcedevicetype.md) — The type of device that captured the photo.
- [metadata](avcapturephoto/metadata.md) — A dictionary of metadata describing the captured image.
- [portraitEffectsMatte](avcapturephoto/portraiteffectsmatte.md) — The portrait effects matte captured with the photo.

### Packaging data for file output

- [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>) — Gets a customized representation of the photo data.
- [AVCapturePhotoFileDataRepresentationCustomizer](avcapturephotofiledatarepresentationcustomizer.md) — A protocol that defines the methods to implement to customize the packaging of photo data.
- [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) — Generates and returns a flat data representation of the photo and its attachments.
- [- CGImageRepresentation](<avcapturephoto/cgimagerepresentation().md>) — Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [- previewCGImageRepresentation](<avcapturephoto/previewcgimagerepresentation().md>) — Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<avcapturephoto/filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_

### Enabling constant color

- [constantColorCenterWeightedMeanConfidenceLevel](avcapturephoto/constantcolorcenterweightedmeanconfidencelevel.md) — A score that summarizes the overall confidence level of a constant color photo.
- [constantColorConfidenceMap](avcapturephoto/constantcolorconfidencemap.md) — A pixel buffer where each pixel value indicates how fully the system achieves the constant color effect in the corresponding region of the photo.
- [constantColorFallbackPhoto](avcapturephoto/isconstantcolorfallbackphoto.md) — A Boolean value that Indicates whether this photo is a fallback photo for a constant color capture.

### Examining bracketed capture information

- [bracketSettings](avcapturephoto/bracketsettings.md) — The variations available for bracketed capture settings for this photo.
- [sequenceCount](avcapturephoto/sequencecount.md) — The 1-based index of this photo in a bracketed capture sequence.
- [lensStabilizationStatus](avcapturephoto/lensstabilizationstatus.md) — Information about the use of lens stabilization during bracketed photo capture.
- [LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md) — Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.

### Accessing segmentation mattes

- [- semanticSegmentationMatteForType:](<avcapturephoto/semanticsegmentationmatte(for_).md>) — Retrieves the semantic segmentation matte associated with this photo.

## See Also

### Photo capture

- [Capturing consistent color images](capturing-consistent-color-images.md) — Add the power of a photography studio and lighting rig to your app with the new Constant Color API.
- [Capturing still and Live Photos](capturing-still-and-live-photos.md) — Configure and capture single or multiple still images, Live Photos, and other forms of photography.
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md) — Support professional photography workflows by enabling minimally processed image capture in your camera app.
- [Supporting Continuity Camera in Your Mac App](../appkit/supporting-continuity-camera-in-your-mac-app.md) — Incorporate scanned documents and pictures from a user’s iPhone, iPad, or iPod touch into your Mac app using Continuity Camera.
- [AVCaptureDeferredPhotoProxy](avcapturedeferredphotoproxy.md) — A lightly-processed photo with data that the system may use to process and fetch a higher-resolution asset at a later time.
- [AVCapturePhotoOutput](avcapturephotooutput.md) — A capture output for still image, Live Photos, and other photography workflows.
- [AVCapturePhotoCaptureDelegate](avcapturephotocapturedelegate.md) — Methods for monitoring progress and receiving results from a photo capture output.
- [AVCapturePhotoOutputReadinessCoordinator](avcapturephotooutputreadinesscoordinator.md) — An object that monitors changes to a photo output’s capture readiness.
- [AVCapturePhotoOutputReadinessCoordinatorDelegate](avcapturephotooutputreadinesscoordinatordelegate.md) — A delegate protocol to receive updates about a photo output’s capture readiness.
- [AVCaptureStillImageOutput](avcapturestillimageoutput.md) — A capture output for capturing still photos. _(deprecated)_

---
title: AVCapturePhotoBracketSettings
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotobracketsettings
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotobracketsettings.json'
content_hash: 'sha256:fd997c5dbab1fe24'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoBracketSettings

<sub>Class</sub>

A specification of the features and settings to use for a photo capture request that captures multiple images with varied settings.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class AVCapturePhotoBracketSettings
```

## Overview

To take a bracketed capture, you create and configure an [AVCapturePhotoBracketSettings](avcapturephotobracketsettings.md) object, using [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) objects to describe the individual captures in the bracket, and then pass it to the [AVCapturePhotoOutput](avcapturephotooutput.md) [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method.

To request a bracketed capture, follow these steps:

1. Create an array of [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) objects describing the number of images to capture in the bracket and the variations on capture settings between them.
2. Create a bracketed photo settings object with the [+ photoBracketSettingsWithRawPixelFormatType:processedFormat:bracketedSettings:](<avcapturephotobracketsettings/init(rawpixelformattype_processedformat_bracketedsettings_).md>) initializer, passing the array of bracketed still image settings, along with the processed format (such as JPEG) or RAW format to capture images in.
3. Configure other settings to share across all images in the bracket, such as the [lensStabilizationEnabled](avcapturephotobracketsettings/islensstabilizationenabled.md) property and certain inherited properties.

> [!important] Important
> Bracketed capture supports only the [highResolutionPhotoEnabled](avcapturephotosettings/ishighresolutionphotoenabled.md) and [previewPhotoFormat](avcapturephotosettings/previewphotoformat.md) settings defined by the [AVCapturePhotoSettings](avcapturephotosettings.md) superclass. Bracketed capture does not support flash, auto stabilization, or Live Photos—attempting to set any of the corresponding properties raises an exception.

1. Initiate capture by passing the bracketed photo settings object to your photo output’s [- capturePhotoWithSettings:delegate:](<avcapturephotooutput/capturephoto(with_delegate_).md>) method, along with a delegate object to receive messages about the progress and results of the capture.

> [!tip] Tip
> Capturing a multiple-image bracket may require allocation of additional resources. See the [- setPreparedPhotoSettingsArray:completionHandler:](<avcapturephotooutput/setpreparedphotosettingsarray(__completionhandler_).md>) method.

1. The photo output calls your delegate’s [- captureOutput:didFinishProcessingPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) or [- captureOutput:didFinishProcessingRawPhotoSampleBuffer:previewPhotoSampleBuffer:resolvedSettings:bracketSettings:error:](<avcapturephotocapturedelegate/photooutput(__didfinishprocessingrawphoto_previewphoto_resolvedsettings_bracketsettings_error_).md>) methods many times corresponding to the number of captures in the bracket. Each call provides the [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) object indicating which capture in the bracket the captured image corresponds to.

The following code example illustrates capturing a bracket of three RAW images with varying exposure value settings.

Listing 1. Capturing a Multi-Exposure Bracket

**Swift**

```swift
func captureRAWAutoExposureBracket() {
    guard myCapturePhotoOutput.maxBracketedCapturePhotoCount >= 3 else { return }
    
    // Specify a 3-shot bracket, where exposure compensation varies between each shot.
    let makeSettings = AVCaptureAutoExposureBracketedStillImageSettings.autoExposureSettingsWithExposureTargetBias
    let bracketedStillImageSettings = [-2, 0, 2].map { makeSettings(Float($0))! }
    let rawFormat = myCapturePhotoOutput.availableRawPhotoCVPixelFormatTypes.first!.unsignedIntValue as OSType
    
    let settings = AVCapturePhotoBracketSettings(format: nil, rawPixelFormatType: rawFormat, bracketedSettings: bracketedStillImageSettings)
    settings.lensStabilizationEnabled = myCapturePhotoOutput.lensStabilizationDuringBracketedCaptureSupported
    
    myCapturePhotoOutput.capturePhotoWithSettings(settings, delegate: self)
    // Three RAW photos will be delivered.
}
```

**Objective-C**

```objc
- (void)captureRAWAutoExposureBracket {
    if ( myCapturePhotoOutput.maxBracketedCapturePhotoCount < 3 ) { return; }
 
    // Specify a 3-shot bracket, where exposure compensation varies between each shot.
    NSArray *bracketedStillImageSettings = @[ [AVCaptureAutoExposureBracketedStillImageSettings autoExposureSettingsWithExposureTargetBias:-2.],
                              [AVCaptureAutoExposureBracketedStillImageSettings autoExposureSettingsWithExposureTargetBias:0.],
                              [AVCaptureAutoExposureBracketedStillImageSettings autoExposureSettingsWithExposureTargetBias:2.] ];
     OSType rawFormat = [[myCapturePhotoOutput.availableRawPhotoCVPixelFormatTypes firstObject] intValue];
 
    AVCapturePhotoBracketSettings *settings = [[AVCapturePhotoBracketSettings alloc] initWithFormat:nil rawPixelFormatType:rawFormat bracketedSettings:bracketedStillImageSettings];
    settings.lensStabilizationEnabled = myCapturePhotoOutput.isLensStabilizationDuringBracketedCaptureSupported;
 
    [myCapturePhotoOutput capturePhotoWithSettings:settings delegate:self];
    // Three RAW photos will be delivered to the delegate.
}
```

## Relationships

- **Inherits From**: [AVCapturePhotoSettings](avcapturephotosettings.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a bracket settings object

- [+ photoBracketSettingsWithRawPixelFormatType:rawFileType:processedFormat:processedFileType:bracketedSettings:](<avcapturephotobracketsettings/init(rawpixelformattype_rawfiletype_processedformat_processedfiletype_bracketedsettings_).md>) — Creates a photo settings object for capture in both RAW format and a processed format.
- [+ photoBracketSettingsWithRawPixelFormatType:processedFormat:bracketedSettings:](<avcapturephotobracketsettings/init(rawpixelformattype_processedformat_bracketedsettings_).md>) — Creates a photo settings object for the specified bracket of captures, in the specified formats.

### Working with bracketed settings

- [bracketedSettings](avcapturephotobracketsettings/bracketedsettings.md) — An array describing the number of and settings for images to produce in a bracketed capture.
- [lensStabilizationEnabled](avcapturephotobracketsettings/islensstabilizationenabled.md) — A Boolean value that specifies whether to stabilize the lens for the duration of the bracketed capture.

### Bracketed settings types

- [AVCaptureAutoExposureBracketedStillImageSettings](avcaptureautoexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of bias relative to automatic exposure.
- [AVCaptureManualExposureBracketedStillImageSettings](avcapturemanualexposurebracketedstillimagesettings.md) — A configuration for defining bracketed photo captures in terms of specific exposure and ISO values.
- [AVCaptureBracketedStillImageSettings](avcapturebracketedstillimagesettings.md) — The abstract superclass for bracketed photo capture settings.

## See Also

### Photo settings

- [AVCapturePhotoSettings](avcapturephotosettings.md) — A specification of the features and settings to use for a single photo capture request.
- [AVCaptureResolvedPhotoSettings](avcaptureresolvedphotosettings.md) — A description of the features and settings in use for an in-progress or complete photo capture request.

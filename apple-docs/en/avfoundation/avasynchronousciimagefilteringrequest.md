---
title: AVAsynchronousCIImageFilteringRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasynchronousciimagefilteringrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousciimagefilteringrequest.json'
content_hash: 'sha256:78bafd968c7a041a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAsynchronousCIImageFilteringRequest

<sub>Class</sub>

An object that supports using Core Image filters to process an individual video frame in a video composition.

> [!warning] Deprecated
> Use AVCIImageFilteringParameters instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAsynchronousCIImageFilteringRequest
```

## Overview

You use this class when creating a composition for Core Image filtering with the [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) method. In that method call, you provide a block to be called by AVFoundation as it processes each frame of video, and the block’s sole parameter is a [AVAsynchronousCIImageFilteringRequest](avasynchronousciimagefilteringrequest.md) object. Use that object both to the video frame image to be filtered and allows you to return a filtered image to AVFoundation for display or export. The code listing below shows an example of applying a filter to an asset.

**Swift**

```swift
guard let filter = CIFilter(name: "CIGaussianBlur") else { return }
let composition = AVVideoComposition(asset: asset) { request in
    // Clamp to avoid blurring transparent pixels at the image edges.
    let source = request.sourceImage.clampedToExtent()
    filter.setValue(source, forKey: kCIInputImageKey)

    // Vary filter parameters based on the video timing.
    let seconds = CMTimeGetSeconds(request.compositionTime)
    filter.setValue(seconds * 10.0, forKey: kCIInputRadiusKey)
            
    // Crop the blurred output to the bounds of the original image.
    if let output = filter.outputImage?.cropped(to: request.sourceImage.extent) {
        request.finish(with: output, context: nil)
    } else {
        request.finish(with: AppError.customError)
    }
}
```

**Objective-C**

```objc
CIFilter *filter = [CIFilter filterWithName:@"CIGaussianBlur"];
AVVideoComposition *composition = [AVVideoComposition videoCompositionWithAsset: asset
    applyingCIFiltersWithHandler:^(AVAsynchronousCIImageFilteringRequest *request){
        // Clamp to avoid blurring transparent pixels at the image edges
        CIImage *source = [request.sourceImage imageByClampingToExtent];
        [filter setValue:source forKey:kCIInputImageKey];
 
        // Vary filter parameters based on video timing
        Float64 seconds = CMTimeGetSeconds(request.compositionTime);
        [filter setValue:seconds * 10.0 forKey:kCIInputRadiusKey];
 
        // Crop the blurred output to the bounds of the original image
        CIImage *output = [filter.outputImage imageByCroppingToRect:request.sourceImage.extent];
 
        // Provide the filter output to the composition
        [request finishWithImage:output context:nil];
    }];
```

> [!tip] Tip
> To use the created video composition for playback, create an [AVPlayerItem](avplayeritem.md) object from the same asset used as the composition’s source, then assign the composition to the player item’s [videoComposition](avplayeritem/videocomposition.md) property. To export the composition to a new movie file, create an [AVAssetExportSession](avassetexportsession.md) object from the same source asset, then assign the composition to the export session’s [videoComposition](avassetexportsession/videocomposition.md) property.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the image to be filtered

- [sourceImage](avasynchronousciimagefilteringrequest/sourceimage.md) — The current video frame image. _(deprecated)_

### Getting contextual information for filtering

- [compositionTime](avasynchronousciimagefilteringrequest/compositiontime.md) — The time in the video composition corresponding to the frame being processed. _(deprecated)_
- [renderSize](avasynchronousciimagefilteringrequest/rendersize.md) — The width and height, in pixels, of the frame being processed. _(deprecated)_

### Returning the filtered image

- [- finishWithImage:context:](<avasynchronousciimagefilteringrequest/finish(with_context_).md>) — Provides the filtered video frame image to AVFoundation for further processing or display. _(deprecated)_
- [- finishWithError:](<avasynchronousciimagefilteringrequest/finish(with_).md>) — Notifies AVFoundation that you cannot fulfill the image filtering request. _(deprecated)_

## See Also

### Creating a video composition

- [init(configuration:)](<avvideocomposition/init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](avvideocomposition/configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<avvideocomposition/init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:completionHandler:](<avvideocomposition/videocomposition(with_applyingcifilterswithhandler_completionhandler_).md>) — Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_
- [AVCIImageFilteringParameters](avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<avvideocomposition/videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<avvideocomposition/init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<avvideocomposition/init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_

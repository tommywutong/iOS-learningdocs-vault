---
title: 'videoComposition(with:applyingCIFiltersWithHandler:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+（27.0 起废弃）, iPadOS 16.0+（27.0 起废弃）, Mac Catalyst 16.0+（27.0 起废弃）, macOS 13.0+（27.0 起废弃）, tvOS 16.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/videocomposition(with:applyingcifilterswithhandler:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/videocomposition%28with%3Aapplyingcifilterswithhandler%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:c105b9e24ab1662e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# videoComposition(with:applyingCIFiltersWithHandler:completionHandler:)

<sub>Type Method</sub>

Returns a new video composition that’s configured to apply Core Image filters to each video frame of the specified asset.

> [!warning] Deprecated
> Use init(applyingFiltersTo:applier:)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(with asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping @Sendable (AVAsynchronousCIImageFilteringRequest) -> Void, completionHandler: @escaping @Sendable (AVVideoComposition?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func videoComposition(with asset: AVAsset, applyingCIFiltersWithHandler applier: @escaping @Sendable (AVAsynchronousCIImageFilteringRequest) -> Void) async throws -> AVVideoComposition
```

## Parameters

- `asset` — The asset whose configuration matches the intended use of the video composition.

- `applier` — A block that AVFoundation calls when processing each video frame. The block takes a single parameter and has no return value: - **request** — An [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) object representing the frame to be processed.

- `completionHandler` — A block the system calls when it finishes creating the new video composition.

## Discussion

The composition calls the specified handler one time for each frame to display (or processed for export) from the asset’s first enabled video track. In that block, you access the video frame and return a filtered result using the provided [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) object. Use that object’s [sourceImage](../avasynchronousciimagefilteringrequest/sourceimage.md) property to get the video frame in the form of a [CIImage](../../coreimage/ciimage.md) object you can apply filters to. Pass the result of your filters to the `request` object’s [- finishWithImage:context:](<../avasynchronousciimagefilteringrequest/finish(with_context_).md>) method. (If your filter rendering fails, call the `request` object’s [- finishWithError:](<../avasynchronousciimagefilteringrequest/finish(with_).md>) method if you can’t apply filters).

```swift
guard let filter = CIFilter(name: "CIGaussianBlur") else { return }
let composition = try await AVVideoComposition.videoComposition(with: asset) { request in
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

Creating a composition with this method sets values for the following properties:

- The value of the [frameDuration](frameduration.md) property accommodates the [nominalFrameRate](../avassettrack/nominalframerate.md) value for the asset’s first enabled video track. If the nominal frame rate is zero, AVFoundation uses a default frame rate of 30 fps.
- The [renderSize](rendersize.md) property value a size that encompasses the asset’s first enabled video track, respecting the track’s [preferredTransform](../avassettrack/preferredtransform.md) property.
- The [renderScale](renderscale.md) property value is `1.0`.

## See Also

### Creating a video composition

- [init(configuration:)](<init(configuration_).md>) — Initialize an AVVideoComposition with a configuration.
- [Configuration](configuration.md) — Configurable properties for initializing a new AVVideoComposition instance.
- [init(applyingFiltersTo:applier:)](<init(applyingfiltersto_applier_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset.
- [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md) — An object that supports using Core Image filters to process an individual video frame in a video composition. _(deprecated)_
- [AVCIImageFilteringParameters](../avciimagefilteringparameters.md)
- [AVCIImageFilteringResult](../avciimagefilteringresult.md) — An output video frame processed with Core Image filtering.
- [+ videoCompositionWithPropertiesOfAsset:completionHandler:](<videocomposition(withpropertiesof_completionhandler_).md>) — Returns a new video composition that’s configured to present the video tracks of the specified asset.
- [+ videoCompositionWithPropertiesOfAsset:](<init(propertiesof_).md>) — Creates a video composition object configured to present the video tracks of the specified asset. _(deprecated)_
- [+ videoCompositionWithAsset:applyingCIFiltersWithHandler:](<init(asset_applyingcifilterswithhandler_).md>) — Creates a video composition configured to apply Core Image filters to each video frame of the specified asset. _(deprecated)_

---
title: 'determineValidity(for:timeRange:validationDelegate:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+（18.0 起废弃）, iPadOS 16.0+（18.0 起废弃）, Mac Catalyst 16.0+（18.0 起废弃）, macOS 13.0+（15.0 起废弃）, tvOS 16.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/determinevalidity(for:timerange:validationdelegate:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/determinevalidity%28for%3Atimerange%3Avalidationdelegate%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:e8f9b775b7e14206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# determineValidity(for:timeRange:validationDelegate:completionHandler:)

<sub>Instance Method</sub>

Determines whether the time ranges of the composition’s instructions conform to validation requirements.

> [!warning] Deprecated
> Use [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<isvalid(for_assetduration_timerange_validationdelegate_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func determineValidity(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?, completionHandler: @escaping @Sendable (Bool, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func isValid(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) async throws -> Bool
```

## Parameters

- `asset` — An asset object, if you require validating the time ranges of the instructions against the duration of the asset and the track IDs of the layer instructions against the asset’s tracks. Pass `nil` to skip that validation.

- `timeRange` — A time range over which to validate instructions. The method validates only instructions with time ranges that overlap with this time range. To validate all instructions that you can use for playback or other processing, regardless of time range, pass `CMTimeRange(start: .zero, duration: .positiveInfinity)`.

- `validationDelegate` — An object that adopts the [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md) protocol to receive detailed information about problematic sections of a video composition during processing. Pass `nil` if you don’t require the details.

- `completionHandler` — A block the system calls when it determines whether the video composition is valid.

## Discussion

During validation, the video composition calls the validation delegate, if one exists, with a reference to any trouble spots in the video composition.

This method raises an exception if the delegate modifies the video composition’s instructions, or the array of layer instructions of any [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md) object contained therein during validation.

## See Also

### Validating the time range

- [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<isvalid(for_assetduration_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md) — Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [- isValidForAsset:timeRange:validationDelegate:](<isvalid(for_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_

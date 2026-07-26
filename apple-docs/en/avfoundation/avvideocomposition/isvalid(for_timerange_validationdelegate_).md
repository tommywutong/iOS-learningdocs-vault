---
title: 'isValid(for:timeRange:validationDelegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（18.0 起废弃）, iPadOS 5.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.8+（15.0 起废弃）, tvOS 9.0+（18.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avvideocomposition/isvalid(for:timerange:validationdelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:timerange:validationdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/isvalid%28for%3Atimerange%3Avalidationdelegate%3A%29.json'
content_hash: 'sha256:584870cd7bf66a10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# isValid(for:timeRange:validationDelegate:)

<sub>Instance Method</sub>

Indicates whether the time ranges of the composition’s instructions conform to validation requirements.

> [!warning] Deprecated
> Use [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<isvalid(for_assetduration_timerange_validationdelegate_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isValid(for asset: AVAsset?, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool
```

## Parameters

- `asset` — An asset object, if you require validating the time ranges of the instructions against the duration of the asset and the track IDs of the layer instructions against the asset’s tracks. Pass `nil` to skip that validation.

- `timeRange` — A time range over which to validate instructions. The method validates only instructions with time ranges that overlap with this time range. To validate all instructions that you can use for playback or other processing, regardless of time range, pass `CMTimeRange(start: .zero, duration: .positiveInfinity)`.

- `validationDelegate` — An object that adopts the [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md) protocol to receive detailed information about problematic sections of a video composition during processing. Pass `nil` if you don’t require the details.

## Return Value

[true](../../swift/true.md) if the time ranges of the composition’s instructions conform to validation requirements, otherwise [false](../../swift/false.md).

## Discussion

Apple discourages using this method in iOS 16, tvOS 16, and macOS 13 or later. Use [- determineValidityForAsset:timeRange:validationDelegate:completionHandler:](<determinevalidity(for_timerange_validationdelegate_completionhandler_).md>) instead.

During validation, the video composition calls the validation delegate, if one exists, with a reference to any trouble spots in the video composition.

This method raises an exception if the delegate modifies the video composition’s instructions, or the array of layer instructions of any [AVVideoCompositionInstruction](../avvideocompositioninstruction-swift.class.md) object contained therein during validation.

## See Also

### Validating the time range

- [- isValidForTracks:assetDuration:timeRange:validationDelegate:](<isvalid(for_assetduration_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements.
- [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md) — Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [- determineValidityForAsset:timeRange:validationDelegate:completionHandler:](<determinevalidity(for_timerange_validationdelegate_completionhandler_).md>) — Determines whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_

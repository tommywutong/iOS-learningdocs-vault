---
title: 'isValid(for:assetDuration:timeRange:validationDelegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideocomposition/isvalid(for:assetduration:timerange:validationdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideocomposition/isvalid%28for%3Aassetduration%3Atimerange%3Avalidationdelegate%3A%29.json'
content_hash: 'sha256:4859436ba2768da2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVVideoComposition](../avvideocomposition.md)

# isValid(for:assetDuration:timeRange:validationDelegate:)

<sub>Instance Method</sub>

Indicates whether the time ranges of the composition’s instructions conform to validation requirements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func isValid(for tracks: [AVAssetTrack], assetDuration duration: CMTime, timeRange: CMTimeRange, validationDelegate: (any AVVideoCompositionValidationHandling)?) -> Bool
```

## Parameters

- `tracks` — Pass a reference to an asset’s tracks if you wish to validate the track IDs of the layer instructions against the asset’s tracks. Pass `nil` to skip that validation. This method throws an exception if the tracks aren’t all from the same asset.

- `duration` — Pass the asset duration to validate the time ranges of the instructions. Pass [invalid](../../coremedia/cmtime/invalid.md) to skip that validation.

- `timeRange` — The composition only validates those instructions with time ranges that overlap with the specified time range. To validate all instructions that the composition may use for playback or other processing, regardless of time range, pass `CMTimeRange(start: .zero, end: .positiveInfinity)`.

- `validationDelegate` — A delegate that handles validation requests. May be `nil`.

## Return Value

[true](../../swift/true.md) if the validation succeeds; otherwise; [false](../../swift/false.md).

## See Also

### Validating the time range

- [AVVideoCompositionValidationHandling](../avvideocompositionvalidationhandling.md) — Methods you can implement to indicate whether validation of a video composition should continue after specific errors are found.
- [- determineValidityForAsset:timeRange:validationDelegate:completionHandler:](<determinevalidity(for_timerange_validationdelegate_completionhandler_).md>) — Determines whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_
- [- isValidForAsset:timeRange:validationDelegate:](<isvalid(for_timerange_validationdelegate_).md>) — Indicates whether the time ranges of the composition’s instructions conform to validation requirements. _(deprecated)_

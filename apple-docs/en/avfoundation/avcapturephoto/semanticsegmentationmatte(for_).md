---
title: 'semanticSegmentationMatte(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephoto/semanticsegmentationmatte(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/semanticsegmentationmatte(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/semanticsegmentationmatte%28for%3A%29.json'
content_hash: 'sha256:dc42ecef75cf54e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# semanticSegmentationMatte(for:)

<sub>Instance Method</sub>

Retrieves the semantic segmentation matte associated with this photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func semanticSegmentationMatte(for semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType) -> AVSemanticSegmentationMatte?
```

## Parameters

- `semanticSegmentationMatteType` — The type of semantic segmentation matte to retrieve from the photo.

## Return Value

An instance of [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md), or `nil` of you didn’t request semantic segmentation matte delivery or if no mattes of the specified type were found.

## Discussion

If you requested one or more semantic segmentation mattes by calling [enabledSemanticSegmentationMatteTypes](../avcapturephotosettings/enabledsemanticsegmentationmattetypes.md) with a nonempty array of types, this property offers access to the resulting [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md) objects.

> [!note] Note
> Semantic segmentation mattes are only embedded in the photo’s internal file format container if you set [embedsSemanticSegmentationMattesInPhoto](../avcapturephotosettings/embedssemanticsegmentationmattesinphoto.md) to [true](../../swift/true.md).

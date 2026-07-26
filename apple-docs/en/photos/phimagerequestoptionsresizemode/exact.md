---
title: PHImageRequestOptionsResizeMode.exact
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsresizemode/exact
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode/exact'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsresizemode/exact.json'
content_hash: 'sha256:4e6825b86a32223f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md)

# PHImageRequestOptionsResizeMode.exact

<sub>Case</sub>

Photos resizes the image to match the target size exactly.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case exact
```

## Discussion

Resizing to exactly match a target size is less efficient than using the fast resizing option. The system doesn’t resize low-quality or degraded images that [PHImageRequestOptionsDeliveryModeOpportunistic](../phimagerequestoptionsdeliverymode/opportunistic.md) or [PHImageRequestOptionsDeliveryModeHighQualityFormat](../phimagerequestoptionsdeliverymode/highqualityformat.md) return.

You must choose this enumeration case if you use the [normalizedCropRect](../phimagerequestoptions/normalizedcroprect.md) property to request a cropped image.

## See Also

### Constants

- [PHImageRequestOptionsResizeModeNone](none.md) — Photos does not resize the image asset.
- [PHImageRequestOptionsResizeModeFast](fast.md) — Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.

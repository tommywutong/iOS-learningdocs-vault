---
title: burstIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/burstidentifier
source_url: 'https://developer.apple.com/documentation/photos/phasset/burstidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/burstidentifier.json'
content_hash: 'sha256:81cd7fe8d75d54ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# burstIdentifier

<sub>Instance Property</sub>

The unique identifier shared by photo assets from the same burst sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var burstIdentifier: String? { get }
```

## Discussion

When the user takes a sequence of photos in burst mode with the Camera app (on supported devices), the Photos app user interface groups the resulting assets together. The Photos framework identifies a burst sequence as a group of assets sharing the same burst identifier string.

## See Also

### Related Documentation

- [+ fetchAssetsWithBurstIdentifier:options:](<fetchassets(withburstidentifier_options_).md>) — Retrieves assets with the specified burst photo sequence identifier.

### Working with Burst Photo Assets

- [burstSelectionTypes](burstselectiontypes.md) — The selection type of the asset in a burst photo sequence.
- [PHAssetBurstSelectionType](../phassetburstselectiontype.md) — Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [burstSelectionTypes](burstselectiontypes.md) property.
- [representsBurst](representsburst.md) — A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.

---
title: representsBurst
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/representsburst
source_url: 'https://developer.apple.com/documentation/photos/phasset/representsburst'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/representsburst.json'
content_hash: 'sha256:ddbfb60d98bbdf25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# representsBurst

<sub>Instance Property</sub>

A Boolean value that indicates whether the asset is the representative photo from a burst photo sequence.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var representsBurst: Bool { get }
```

## Discussion

When the user takes a sequence of photos in burst mode with the Camera app (on supported devices), the Photos app user interface groups the resulting assets together. One asset represents the entire sequence in displayed collections.

## See Also

### Working with Burst Photo Assets

- [burstIdentifier](burstidentifier.md) — The unique identifier shared by photo assets from the same burst sequence.
- [burstSelectionTypes](burstselectiontypes.md) — The selection type of the asset in a burst photo sequence.
- [PHAssetBurstSelectionType](../phassetburstselectiontype.md) — Bit mask values indicating whether and how an asset is marked as a favorite member of a burst photo sequence. Used by the [burstSelectionTypes](burstselectiontypes.md) property.

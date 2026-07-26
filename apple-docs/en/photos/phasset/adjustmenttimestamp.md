---
title: adjustmentTimestamp
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/adjustmenttimestamp
source_url: 'https://developer.apple.com/documentation/photos/phasset/adjustmenttimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/adjustmenttimestamp.json'
content_hash: 'sha256:8c7b8df669a7bde6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# adjustmentTimestamp

<sub>Instance Property</sub>

The date when the asset was last edited.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var adjustmentTimestamp: Date? { get }
```

## Discussion

If the asset has never been edited, then this property is nil. If the asset was edited and later reverted, such that hasAdjustments is false, then `adjustmentTimestamp` is the timestamp of the revert operation.

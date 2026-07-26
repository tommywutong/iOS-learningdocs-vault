---
title: data
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phadjustmentdata/data
source_url: 'https://developer.apple.com/documentation/photos/phadjustmentdata/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phadjustmentdata/data.json'
content_hash: 'sha256:93f02434073b75a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAdjustmentData](../phadjustmentdata.md)

# data

<sub>Instance Property</sub>

Data that contains the information necessary to reconstruct the adjustment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var data: Data { get }
```

## Discussion

Use this property to resume working with the last edit that was made to an asset. For example, if your app applies Core Image filters to photos, this property may hold a serialized property list that describes the filters and their parameters. Use the [formatIdentifier](formatidentifier.md) and [formatVersion](formatversion.md) properties to determine whether the adjustment data saved with an asset is in a format that your app can understand.

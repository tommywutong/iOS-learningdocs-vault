---
title: formatIdentifier
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phadjustmentdata/formatidentifier
source_url: 'https://developer.apple.com/documentation/photos/phadjustmentdata/formatidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phadjustmentdata/formatidentifier.json'
content_hash: 'sha256:23c73e2df89149e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAdjustmentData](../phadjustmentdata.md)

# formatIdentifier

<sub>Instance Property</sub>

A string uniquely identifying the format of the adjustment data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var formatIdentifier: String { get }
```

## Discussion

Set this identifier when you create an adjustment object with the [- initWithFormatIdentifier:formatVersion:data:](<init(formatidentifier_formatversion_data_).md>) method. For best results, identify your organization or product using a reverse-DNS-style name, such as `com.example.myApp`.

Read this property, and the [formatVersion](formatversion.md) property, to determine whether the adjustment data saved with an asset was created by your app or is otherwise compatible with your app.

## See Also

### Identifying the Format of an Adjustment’s Data

- [formatVersion](formatversion.md) — A version number for the adjustment data format.

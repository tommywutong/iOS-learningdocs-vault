---
title: formatVersion
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phadjustmentdata/formatversion
source_url: 'https://developer.apple.com/documentation/photos/phadjustmentdata/formatversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phadjustmentdata/formatversion.json'
content_hash: 'sha256:c26d5e35708ed7d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAdjustmentData](../phadjustmentdata.md)

# formatVersion

<sub>Instance Property</sub>

A version number for the adjustment data format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var formatVersion: String { get }
```

## Discussion

Set this identifier when creating an adjustment object with the [- initWithFormatIdentifier:formatVersion:data:](<init(formatidentifier_formatversion_data_).md>) method.

Read this property, and the [formatIdentifier](formatidentifier.md) property, to determine whether the adjustment data saved with an asset was created by your app or is otherwise compatible with your app.

For example, in the first version of your app, you might save adjustment data using the identifier `com.example.myApp` and version `1.0`. If a later version of your app adds incompatible information to the adjustment data, you can use the same identifier and increase the version number to `2.0`.

## See Also

### Identifying the Format of an Adjustment’s Data

- [formatIdentifier](formatidentifier.md) — A string uniquely identifying the format of the adjustment data.

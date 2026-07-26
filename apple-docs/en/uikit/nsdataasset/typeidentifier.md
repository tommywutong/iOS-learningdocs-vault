---
title: typeIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdataasset/typeidentifier
source_url: 'https://developer.apple.com/documentation/uikit/nsdataasset/typeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdataasset/typeidentifier.json'
content_hash: 'sha256:c68447079f781ead'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDataAsset](../nsdataasset.md)

# typeIdentifier

<sub>Instance Property</sub>

The uniform type identifier for the data asset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var typeIdentifier: String { get }
```

## Discussion

A uniform type identifier is a string for identifying the type of data. This UTI is the same as the one specified in the asset catalog. For more information, see [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Getting data asset information

- [name](name.md) — The name of the data set in the asset catalog.
- [NSDataAssetName](../nsdataassetname.md) — The name of a data asset.

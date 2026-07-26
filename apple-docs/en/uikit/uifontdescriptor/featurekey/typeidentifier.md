---
title: typeIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+（15.0 起废弃）, iPadOS 7.0+（15.0 起废弃）, Mac Catalyst 13.1+（15.0 起废弃）, tvOS（15.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（8.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uifontdescriptor/featurekey/typeidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey/typeidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/featurekey/typeidentifier.json'
content_hash: 'sha256:8e342ef02e55fe79'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [FeatureKey](../featurekey.md)

# typeIdentifier

<sub>Type Property</sub>

A key for identifying the font feature selector.

> [!warning] Deprecated
> Use [selector](selector.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let typeIdentifier: UIFontDescriptor.FeatureKey
```

## Discussion

The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object specifying the ligature, character shape, or other font feature.

## See Also

### Deprecated

- [UIFontFeatureTypeIdentifierKey](featureidentifier.md) — A key for identifying a font feature type. _(deprecated)_

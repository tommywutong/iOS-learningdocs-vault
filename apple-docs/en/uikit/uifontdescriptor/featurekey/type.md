---
title: type
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifontdescriptor/featurekey/type
source_url: 'https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifontdescriptor/featurekey/type.json'
content_hash: 'sha256:e28bc36bd4edaa5c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIFontDescriptor](../../uifontdescriptor.md) · [FeatureKey](../featurekey.md)

# type

<sub>Type Property</sub>

A key for identifying the font feature type.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static let type: UIFontDescriptor.FeatureKey
```

## Discussion

The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object specifying the font feature type such as ligature, character shape, or other font feature.

## See Also

### Keys

- [selector](selector.md) — A key for identifying the font feature selector.

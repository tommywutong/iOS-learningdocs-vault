---
title: style
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponentsformatter/style-swift.property
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/style-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/style-swift.property.json'
content_hash: 'sha256:14bc4ded7ae945a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# style

<sub>Instance Property</sub>

The formatting style of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var style: PersonNameComponentsFormatter.Style { get set }
```

## Discussion

Styles specify which name components are used to create a string representation, and how. Examples of name components formatter styles include `long` and `abbreviated`.

## See Also

### Configuring Formatter Behavior

- [phonetic](isphonetic.md) — A Boolean value that specifies whether the receiver should use only the phonetic representations of name components.

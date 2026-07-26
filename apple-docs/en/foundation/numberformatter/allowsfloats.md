---
title: allowsFloats
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/allowsfloats
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/allowsfloats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/allowsfloats.json'
content_hash: 'sha256:452e812dd1a0c585'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# allowsFloats

<sub>Instance Property</sub>

Determines whether the receiver allows as input floating-point values (that is, values that include the period character [`.`]).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsFloats: Bool { get set }
```

## Discussion

By default, floating point values are allowed.

## See Also

### Managing Input and Output Attributes

- [minimum](minimum.md) — The lowest number allowed as input by the receiver.
- [maximum](maximum.md) — The highest number allowed as input by the receiver.

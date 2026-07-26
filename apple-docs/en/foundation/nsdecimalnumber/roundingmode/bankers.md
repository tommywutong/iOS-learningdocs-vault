---
title: NSDecimalNumber.RoundingMode.bankers
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdecimalnumber/roundingmode/bankers
source_url: 'https://developer.apple.com/documentation/foundation/nsdecimalnumber/roundingmode/bankers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdecimalnumber/roundingmode/bankers.json'
content_hash: 'sha256:05b0c518f99901e7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSDecimalNumber](../../nsdecimalnumber.md) · [RoundingMode](../roundingmode.md)

# NSDecimalNumber.RoundingMode.bankers

<sub>Case</sub>

Round to the closest possible return value; when halfway between two possibilities, return the possibility whose last digit is even.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case bankers
```

## Discussion

In practice, this means that, over the long run, numbers will be rounded up as often as they are rounded down; there will be no systematic bias.

## See Also

### Constants

- [NSRoundPlain](plain.md) — Round to the closest possible return value; when caught halfway between two positive numbers, round up; when caught between two negative numbers, round down.
- [NSRoundDown](down.md) — Round return values down.
- [NSRoundUp](up.md) — Round return values up.

---
title: isLenient
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/islenient
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/islenient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/islenient.json'
content_hash: 'sha256:cfb91c05c1905dfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# isLenient

<sub>Instance Property</sub>

Determines whether the receiver will use heuristics to guess at the number which is intended by a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLenient: Bool { get set }
```

## Discussion

If the formatter is set to be lenient, as with any guessing it may get the result number wrong (that is, a number other than that which was intended).

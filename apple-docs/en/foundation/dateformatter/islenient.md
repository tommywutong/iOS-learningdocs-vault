---
title: isLenient
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/islenient
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/islenient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/islenient.json'
content_hash: 'sha256:45ed74fa71e58bfe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# isLenient

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver uses heuristics when parsing a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isLenient: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver has been set to use heuristics when parsing a string to guess at the date which is intended, otherwise [false](../../swift/false.md).

If a formatter is set to be lenient, when parsing a string it uses heuristics to guess at the date which is intended. As with any guessing, it may get the result date wrong (that is, a date other than that which was intended).

## See Also

### Managing Natural Language Support

- [doesRelativeDateFormatting](doesrelativedateformatting.md) — A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.

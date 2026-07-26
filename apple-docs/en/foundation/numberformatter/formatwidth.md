---
title: formatWidth
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/formatwidth
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/formatwidth'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/formatwidth.json'
content_hash: 'sha256:c07b1d2e267f5e97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# formatWidth

<sub>Instance Property</sub>

The format width used by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formatWidth: Int { get set }
```

## Discussion

The format width is the number of characters of a formatted number within a string that is either left justified or right justified based on the value contained in  [paddingPosition](paddingposition.md).

## See Also

### Configuring Numeric Formats

- [format](format.md) — The receiver’s format.
- [formattingContext](formattingcontext.md) — The capitalization formatting context used when formatting a number.
- [negativeFormat](negativeformat.md) — The format the receiver uses to display negative values.
- [positiveFormat](positiveformat.md) — The format the receiver uses to display positive values.
- [multiplier](multiplier.md) — The multiplier of the receiver.

---
title: format
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/format
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/format'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/format.json'
content_hash: 'sha256:4584714e8416fbc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# format

<sub>Instance Property</sub>

The receiver’s format.

<sub>macOS</sub>

```swift
var format: String { get set }
```

## Discussion

The format string uses the format patterns from [Unicode Technical Standard #35](http://www.unicode.org/reports/tr35/tr35-numbers.html#Number_Format_Patterns).  For more information, see  [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i).

## See Also

### Configuring Numeric Formats

- [formattingContext](formattingcontext.md) — The capitalization formatting context used when formatting a number.
- [formatWidth](formatwidth.md) — The format width used by the receiver.
- [negativeFormat](negativeformat.md) — The format the receiver uses to display negative values.
- [positiveFormat](positiveformat.md) — The format the receiver uses to display positive values.
- [multiplier](multiplier.md) — The multiplier of the receiver.

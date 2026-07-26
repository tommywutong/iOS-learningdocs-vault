---
title: formattingContext
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/formattingcontext
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/formattingcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/formattingcontext.json'
content_hash: 'sha256:aafc47329ee39664'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# formattingContext

<sub>Instance Property</sub>

The capitalization formatting context used when formatting a number.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var formattingContext: Formatter.Context { get set }
```

## Discussion

Defaults to NSFormattingContextUnknown.

## See Also

### Configuring Numeric Formats

- [format](format.md) — The receiver’s format.
- [formatWidth](formatwidth.md) — The format width used by the receiver.
- [negativeFormat](negativeformat.md) — The format the receiver uses to display negative values.
- [positiveFormat](positiveformat.md) — The format the receiver uses to display positive values.
- [multiplier](multiplier.md) — The multiplier of the receiver.

---
title: numberStyle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/numberstyle
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/numberstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/numberstyle.json'
content_hash: 'sha256:f22d5494ea7312d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# numberStyle

<sub>Instance Property</sub>

The number style used by the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var numberStyle: NumberFormatter.Style { get set }
```

## Discussion

Styles are essentially predetermined sets of values for certain properties. Examples of number-formatter styles are those used for decimal values, percentage values, and currency.

## See Also

### Configuring Formatter Behavior and Style

- [formatterBehavior](formatterbehavior.md) — The formatter behavior of the receiver.
- [+ setDefaultFormatterBehavior:](<setdefaultformatterbehavior(__).md>) — Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) — Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [generatesDecimalNumbers](generatesdecimalnumbers.md) — Determines whether the receiver creates instances of [NSDecimalNumber](../nsdecimalnumber.md) when it converts strings to number objects.

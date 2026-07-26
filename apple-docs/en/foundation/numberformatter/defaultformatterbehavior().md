---
title: defaultFormatterBehavior()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/defaultformatterbehavior()
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/defaultformatterbehavior()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/defaultformatterbehavior%28%29.json'
content_hash: 'sha256:a75c8bf51ccb4998'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# defaultFormatterBehavior()

<sub>Type Method</sub>

Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func defaultFormatterBehavior() -> NumberFormatter.Behavior
```

## Return Value

An `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.

## See Also

### Configuring Formatter Behavior and Style

- [formatterBehavior](formatterbehavior.md) — The formatter behavior of the receiver.
- [+ setDefaultFormatterBehavior:](<setdefaultformatterbehavior(__).md>) — Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [numberStyle](numberstyle.md) — The number style used by the receiver.
- [generatesDecimalNumbers](generatesdecimalnumbers.md) — Determines whether the receiver creates instances of [NSDecimalNumber](../nsdecimalnumber.md) when it converts strings to number objects.

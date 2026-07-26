---
title: 'setDefaultFormatterBehavior(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatter/setdefaultformatterbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/setdefaultformatterbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/setdefaultformatterbehavior%28_%3A%29.json'
content_hash: 'sha256:7de015027b8abdbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# setDefaultFormatterBehavior(_:)

<sub>Type Method</sub>

Sets the default formatter behavior for new instances of `NSNumberFormatter` .

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func setDefaultFormatterBehavior(_ behavior: NumberFormatter.Behavior)
```

## Parameters

- `behavior` — An `NSNumberFormatterBehavior` constant that indicates the revision of the class providing the default behavior.

## See Also

### Configuring Formatter Behavior and Style

- [formatterBehavior](formatterbehavior.md) — The formatter behavior of the receiver.
- [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) — Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [numberStyle](numberstyle.md) — The number style used by the receiver.
- [generatesDecimalNumbers](generatesdecimalnumbers.md) — Determines whether the receiver creates instances of [NSDecimalNumber](../nsdecimalnumber.md) when it converts strings to number objects.

---
title: generatesDecimalNumbers
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numberformatter/generatesdecimalnumbers
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/generatesdecimalnumbers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/generatesdecimalnumbers.json'
content_hash: 'sha256:9a98b7320e078655'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# generatesDecimalNumbers

<sub>Instance Property</sub>

Determines whether the receiver creates instances of [NSDecimalNumber](../nsdecimalnumber.md) when it converts strings to number objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var generatesDecimalNumbers: Bool { get set }
```

## See Also

### Configuring Formatter Behavior and Style

- [formatterBehavior](formatterbehavior.md) — The formatter behavior of the receiver.
- [+ setDefaultFormatterBehavior:](<setdefaultformatterbehavior(__).md>) — Sets the default formatter behavior for new instances of `NSNumberFormatter` .
- [+ defaultFormatterBehavior](<defaultformatterbehavior().md>) — Returns an `NSNumberFormatterBehavior` constant that indicates default formatter behavior for new instances of `NSNumberFormatter`.
- [numberStyle](numberstyle.md) — The number style used by the receiver.

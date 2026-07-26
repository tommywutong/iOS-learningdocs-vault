---
title: defaultFormatterBehavior
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/defaultformatterbehavior
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/defaultformatterbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/defaultformatterbehavior.json'
content_hash: 'sha256:c2fdd45415dfeeb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# defaultFormatterBehavior

<sub>Type Property</sub>

Returns the default formatting behavior for instances of the class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var defaultFormatterBehavior: DateFormatter.Behavior { get set }
```

## Return Value

The default formatting behavior for instances of the class. For possible values, see [Behavior](behavior.md).

## Discussion

For iOS and for macOS applications linked against macOS 10.5 and later, the default is `NSDateFormatterBehavior10_4`.

## See Also

### Managing Behavior Version

- [formatterBehavior](formatterbehavior.md) — The formatter behavior for the receiver.

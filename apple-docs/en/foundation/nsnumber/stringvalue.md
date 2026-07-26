---
title: stringValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnumber/stringvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsnumber/stringvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnumber/stringvalue.json'
content_hash: 'sha256:184f5080cd868fc7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSNumber](../nsnumber.md)

# stringValue

<sub>Instance Property</sub>

The number object’s value expressed as a human-readable string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var stringValue: String { get }
```

## Discussion

The string is created by invoking [- descriptionWithLocale:](<description(withlocale_).md>) where locale is `nil`.

## See Also

### Retrieving String Representations

- [- descriptionWithLocale:](<description(withlocale_).md>) — Returns a string that represents the contents of the number object for a given locale.

---
title: assumesTopLevelDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsondecoder/assumestopleveldictionary
source_url: 'https://developer.apple.com/documentation/foundation/jsondecoder/assumestopleveldictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsondecoder/assumestopleveldictionary.json'
content_hash: 'sha256:2635a669f9803d15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [JSONDecoder](../jsondecoder.md)

# assumesTopLevelDictionary

<sub>Instance Property</sub>

Specifies that decoding assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with braces.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var assumesTopLevelDictionary: Bool { get set }
```

## Discussion

This is an extension to JSON5 that’s not part of the specification. [AttributedString](../attributedstring.md) uses this option, along with [allowsJSON5](allowsjson5.md), to support the use of JSON5 inside Markdown strings that use multiple custom attributes. Using [assumesTopLevelDictionary](assumestopleveldictionary.md) allows for the following syntax inside the parentheses of the custom attribute markup:

```swift
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute](factor: 10, other: true).
```

Without [assumesTopLevelDictionary](assumestopleveldictionary.md), the markup would have to use explicit enclosing braces to declare the contents of the parentheses to be a dictionary:

```swift
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute]({factor: 10, other: true}).
```

When you use braces, you must use matched pairs. This means that with [assumesTopLevelDictionary](assumestopleveldictionary.md) set, the syntax `({…})` and `(…)` are both legal, but `({…)` and `(…})` are not.

## See Also

### Customizing Decoding

- [keyDecodingStrategy](keydecodingstrategy-swift.property.md) — A value that determines how to decode a type’s coding keys from JSON keys.
- [KeyDecodingStrategy](keydecodingstrategy-swift.enum.md) — The values that determine how to decode a type’s coding keys from JSON keys.
- [userInfo](userinfo.md) — A dictionary you use to customize the decoding process by providing contextual information.
- [allowsJSON5](allowsjson5.md) — Specifies that decoding supports the JSON5 syntax.

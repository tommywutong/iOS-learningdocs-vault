---
title: FormatOutput
framework: Foundation
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstyle/formatoutput
source_url: 'https://developer.apple.com/documentation/foundation/formatstyle/formatoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstyle/formatoutput.json'
content_hash: 'sha256:529942fdbabfe7cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FormatStyle](../formatstyle.md)

# FormatOutput

<sub>Associated Type</sub>

The type this format style produces as output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
associatedtype FormatOutput
```

## Discussion

Conforming types in Foundation define this type as either [String](../../swift/string.md) or [AttributedString](../attributedstring.md).

## See Also

### Declaring input and output types

- [FormatInput](formatinput.md) — The type this format style accepts as input.

---
title: DateComponents.HTTPFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/datecomponents/httpformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/httpformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/httpformatstyle.json'
content_hash: 'sha256:759f53516f0d09e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# DateComponents.HTTPFormatStyle

<sub>Structure</sub>

Converts `DateComponents` into RFC 9110-compatible “HTTP date” `String`, and parses in the reverse direction. This parser does not do validation on the individual values of the components. An optional date can be created from the result using `Calendar(identifier: .gregorian).date(from: ...)`. When formatting, missing or invalid fields are filled with default values: `Sun`, `01`, `Jan`, `2000`, `00:00:00`, `GMT`. Note that missing fields may result in an invalid date or time. Other values in the `DateComponents` are ignored.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HTTPFormatStyle
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [ParseableFormatStyle](../parseableformatstyle.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init()](<httpformatstyle/init().md>)

---
title: FormatStyleCapitalizationContext
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatstylecapitalizationcontext
source_url: 'https://developer.apple.com/documentation/foundation/formatstylecapitalizationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatstylecapitalizationcontext.json'
content_hash: 'sha256:1a20d2c555302cce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FormatStyleCapitalizationContext

<sub>Structure</sub>

The capitalization formatting context used when formatting dates and times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyleCapitalizationContext
```

## Relationships

- **Conforms To**: [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Customizing Style Behavior

- [unknown](formatstylecapitalizationcontext/unknown.md)
- [standalone](formatstylecapitalizationcontext/standalone.md) — For stand-alone usage, such as an isolated name on a calendar page.
- [listItem](formatstylecapitalizationcontext/listitem.md) — For use in a UI list or menu item.
- [beginningOfSentence](formatstylecapitalizationcontext/beginningofsentence.md)
- [middleOfSentence](formatstylecapitalizationcontext/middleofsentence.md)

## See Also

### Data formatting in Swift

- [Language Introspector](language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [IntegerFormatStyle](integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FloatingPointFormatStyle](floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [FormatStyle](decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](stringstyle.md)
- [FormatStyle](url/formatstyle.md) — A structure that converts between URL instances and their textual representations.
- [Format Style Configurations](format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.

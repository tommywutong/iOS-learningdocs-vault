---
title: Date.AnchoredRelativeFormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/anchoredrelativeformatstyle
source_url: 'https://developer.apple.com/documentation/foundation/date/anchoredrelativeformatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/anchoredrelativeformatstyle.json'
content_hash: 'sha256:0cf40708de8ac579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Date](../date.md)

# Date.AnchoredRelativeFormatStyle

<sub>Structure</sub>

A relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AnchoredRelativeFormatStyle
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [DiscreteFormatStyle](../discreteformatstyle.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(anchor:allowedFields:presentation:unitsStyle:locale:calendar:capitalizationContext:)](<anchoredrelativeformatstyle/init(anchor_allowedfields_presentation_unitsstyle_locale_calendar_capitalizationcontext_).md>) — Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.
- [init(anchor:presentation:unitsStyle:locale:calendar:capitalizationContext:)](<anchoredrelativeformatstyle/init(anchor_presentation_unitsstyle_locale_calendar_capitalizationcontext_).md>) — Create a relative format style that is detached from the system time, and instead formats an anchor date relative to the format input.

### Instance Properties

- [allowedFields](anchoredrelativeformatstyle/allowedfields.md) — The fields that can be used in the formatted output.
- [anchor](anchoredrelativeformatstyle/anchor.md) — The date the formatted output refers to from the perspective of the input values.
- [calendar](anchoredrelativeformatstyle/calendar.md)
- [capitalizationContext](anchoredrelativeformatstyle/capitalizationcontext.md)
- [locale](anchoredrelativeformatstyle/locale.md)
- [presentation](anchoredrelativeformatstyle/presentation-swift.property.md)
- [unitsStyle](anchoredrelativeformatstyle/unitsstyle-swift.property.md)

### Type Aliases

- [Field](anchoredrelativeformatstyle/field.md)
- [Presentation](anchoredrelativeformatstyle/presentation-swift.typealias.md)
- [UnitsStyle](anchoredrelativeformatstyle/unitsstyle-swift.typealias.md)

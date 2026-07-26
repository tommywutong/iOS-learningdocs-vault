---
title: Duration.UnitsFormatStyle.UnitWidth
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct.json'
content_hash: 'sha256:e7ab20c5c6be4b06'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [UnitsFormatStyle](../unitsformatstyle.md)

# Duration.UnitsFormatStyle.UnitWidth

<sub>Structure</sub>

The width of a unit to use in formatting a duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UnitWidth
```

## Overview

Use the provided unit widths with the `width` parameter of the [UnitsFormatStyle](../unitsformatstyle.md) initializers to customize the display of units in a formatted string.

## Relationships

- **Conforms To**: [Decodable](../../decodable.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Duration unit widths

- [abbreviated](unitwidth-swift.struct/abbreviated.md) — An abbreviated unit name.
- [condensedAbbreviated](unitwidth-swift.struct/condensedabbreviated.md) — An abbreviated unit name, with condensed space between the value and name.
- [narrow](unitwidth-swift.struct/narrow.md) — The shortest possible unit name.
- [wide](unitwidth-swift.struct/wide.md) — The full unit name.

## See Also

### Working with unit widths

- [unitWidth](unitwidth-swift.property.md) — The width of the unit and the spacing between the value and the unit.

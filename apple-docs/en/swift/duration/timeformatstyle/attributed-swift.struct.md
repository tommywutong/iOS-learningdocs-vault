---
title: Duration.TimeFormatStyle.Attributed
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/duration/timeformatstyle/attributed-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/duration/timeformatstyle/attributed-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/duration/timeformatstyle/attributed-swift.struct.json'
content_hash: 'sha256:2eea2ab489041bab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Duration](../../duration.md) · [TimeFormatStyle](../timeformatstyle.md)

# Duration.TimeFormatStyle.Attributed

<sub>Structure</sub>

A format style that formats durations as attributed strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct Attributed
```

## Overview

Apply the [Attributed](attributed-swift.struct.md) property to a configured [TimeFormatStyle](../timeformatstyle.md) to produce an instance of this style. You can then format a duration with this style to create a formatted [AttributedString](../../../foundation/attributedstring.md). The formatted attributed string contains instances of [AttributeScopes.FoundationAttributes.DateFieldAttribute](../../../foundation/attributescopes/foundationattributes/datefieldattribute.md) for runs with formatted durations.

The following example formats a duration as an attributed string:

```swift
let duration = Duration.seconds(70 * 60 + 32) +
    Duration.milliseconds(400)
let style = Duration.TimeFormatStyle(pattern: .hourMinuteSecond).attributed
let attributedDuration = duration.formatted(style)
```

The resulting `attributedDuration`, representing the string `1:10:32` contains the following runs:

| Run | Attributes |
|---|---|
| `1` | `Foundation.DurationFormatAttribute = hours` |
| `:` | None |
| `10` | `Foundation.DurationFormatAttribute = minutes` |
| `:` | None |
| `32` | `Foundation.DurationFormatAttribute = seconds` |

## Relationships

- **Conforms To**: [Copyable](../../copyable.md), [Decodable](../../decodable.md), [DiscreteFormatStyle](../../../foundation/discreteformatstyle.md), [Encodable](../../encodable.md), [Equatable](../../equatable.md), [Escapable](../../escapable.md), [FormatStyle](../../../foundation/formatstyle.md), [Hashable](../../hashable.md), [Sendable](../../sendable.md), [SendableMetatype](../../sendablemetatype.md)

## Topics

### Formatting a duration

- [format(_:)](<attributed-swift.struct/format(__).md>) — Creates a locale-aware attributed string representation from a duration value.

### Working with locales

- [locale(_:)](<attributed-swift.struct/locale(__).md>) — Modifies the format style to use the specified locale.

### Instance Methods

- [grouping(_:)](<attributed-swift.struct/grouping(__).md>) — Returns a modified style that applies the given `grouping` rule to the highest field in the pattern.

### Subscripts

- [subscript(dynamicMember:)](<attributed-swift.struct/subscript(dynamicmember_)-32lo0.md>)
- [subscript(dynamicMember:)](<attributed-swift.struct/subscript(dynamicmember_)-8cksi.md>)

## See Also

### Formatting a duration as an attributed string

- [attributed](attributed-swift.property.md) — A property that formats the duration as an attributed string.

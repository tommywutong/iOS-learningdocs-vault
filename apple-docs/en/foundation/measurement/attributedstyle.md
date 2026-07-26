---
title: Measurement.AttributedStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/measurement/attributedstyle
source_url: 'https://developer.apple.com/documentation/foundation/measurement/attributedstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/measurement/attributedstyle.json'
content_hash: 'sha256:729a905e71fde08c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Measurement](../measurement.md)

# Measurement.AttributedStyle

<sub>Structure</sub>

A type that provides localized representations of measurements with an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct AttributedStyle
```

## Overview

Use either the [formatted()](<formatted().md>) or the [formatted(_:)](<formatted(__).md>) instance method of [Measurement](../measurement.md) to create an attributed string representation of a measurement.

The [formatted()](<formatted().md>) method generates a string using the default measurement format style.

## Relationships

- **Conforms To**: [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Formatting a Measurement

- [format(_:)](<attributedstyle/format(__).md>) — Creates a string representation of a measurement.

### Modififying a Measurement Attributed Style

- [locale(_:)](<attributedstyle/locale(__).md>) — Modifies the measurement format style to use the specified locale.

### Comparing Measurement Attributed Styles

- [==(_:_:)](<==(____).md>) — Compare two measurements of the same `Dimension`.

### Structures

- [ByteCount](attributedstyle/bytecount.md) — A format style that converts byte counts into attributed strings.

### Subscripts

- [subscript(dynamicMember:)](<attributedstyle/subscript(dynamicmember_)-83rva.md>)
- [subscript(dynamicMember:)](<attributedstyle/subscript(dynamicmember_)-c2b1.md>)

## See Also

### Formatting a Measurement

- [formatted()](<formatted().md>) — Generates a locale-aware string representation of a measurement using the default measurement format style.
- [formatted(_:)](<formatted(__).md>) — Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [FormatStyle](formatstyle.md) — A type that provides localized representations of measurements.

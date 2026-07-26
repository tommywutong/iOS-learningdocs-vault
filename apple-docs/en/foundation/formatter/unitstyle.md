---
title: Formatter.UnitStyle
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatter/unitstyle
source_url: 'https://developer.apple.com/documentation/foundation/formatter/unitstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/unitstyle.json'
content_hash: 'sha256:efe0a33d163e7637'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# Formatter.UnitStyle

<sub>Enumeration</sub>

Specifies the width of the unit, determining the textual representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum UnitStyle
```

## Overview

The unit is represented in the shortest notation available. For example, for English, when formatting “3 pounds”: [NSFormattingUnitStyleLong](unitstyle/long.md) is “3 pounds”; [NSFormattingUnitStyleMedium](unitstyle/medium.md) is “3 lb”; [NSFormattingUnitStyleShort](unitstyle/short.md) is “3#”.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSFormattingUnitStyleShort](unitstyle/short.md) — Specifies a short unit style.
- [NSFormattingUnitStyleMedium](unitstyle/medium.md) — Specifies a medium unit style.
- [NSFormattingUnitStyleLong](unitstyle/long.md) — Specifies a long unit style.

### Initializers

- [init(rawValue:)](<unitstyle/init(rawvalue_).md>)

## See Also

### Constants

- [Context](context.md) — The formatting context for a formatter.

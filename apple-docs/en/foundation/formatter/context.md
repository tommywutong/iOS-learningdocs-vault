---
title: Formatter.Context
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatter/context
source_url: 'https://developer.apple.com/documentation/foundation/formatter/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/context.json'
content_hash: 'sha256:a50fedd37b19fc3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# Formatter.Context

<sub>Enumeration</sub>

The formatting context for a formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Context
```

## Overview

Use formatting contexts to specify where the result of formatting will appear, so that the formatter can provide the most appropriate result.

For example, when formatting a date or date symbol for a French locale, you want the month name to be capitalized if it appears at the beginning of the sentence (“Juin est mon mois de naissance”), but not if it appears elsewhere (“Mon mois de naissance est juin”).

If the formatting context isn’t known ahead of time, specify [NSFormattingContextDynamic](context/dynamic.md) to have the system determine the context automatically.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSFormattingContextUnknown](context/unknown.md) — An unknown formatting context.
- [NSFormattingContextDynamic](context/dynamic.md) — A formatting context determined automatically at runtime.
- [NSFormattingContextStandalone](context/standalone.md) — The formatting context for stand-alone usage.
- [NSFormattingContextListItem](context/listitem.md) — The formatting context for a list or menu item.
- [NSFormattingContextBeginningOfSentence](context/beginningofsentence.md) — The formatting context for the beginning of a sentence.
- [NSFormattingContextMiddleOfSentence](context/middleofsentence.md) — The formatting context for the middle of a sentence.

### Initializers

- [init(rawValue:)](<context/init(rawvalue_).md>)

## See Also

### Constants

- [UnitStyle](unitstyle.md) — Specifies the width of the unit, determining the textual representation.

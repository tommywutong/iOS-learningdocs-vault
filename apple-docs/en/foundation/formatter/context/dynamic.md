---
title: Formatter.Context.dynamic
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/formatter/context/dynamic
source_url: 'https://developer.apple.com/documentation/foundation/formatter/context/dynamic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/context/dynamic.json'
content_hash: 'sha256:c0fb37e9b19b094e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Formatter](../../formatter.md) · [Context](../context.md)

# Formatter.Context.dynamic

<sub>Case</sub>

A formatting context determined automatically at runtime.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case dynamic
```

## Discussion

A [NSFormattingContextDynamic](dynamic.md) context is automatically determined to be one of the following: [NSFormattingContextStandalone](standalone.md), [NSFormattingContextBeginningOfSentence](beginningofsentence.md), or [NSFormattingContextMiddleOfSentence](middleofsentence.md).

When used in combination with [stringWithFormat:](../../nsstring/stringwithformat_.md), the formatter returns a string proxy, formats the string using [NSFormattingContextUnknown](unknown.md), determines context based on the proxy string’s location, and then reformats the string accordingly.

## See Also

### Constants

- [NSFormattingContextUnknown](unknown.md) — An unknown formatting context.
- [NSFormattingContextStandalone](standalone.md) — The formatting context for stand-alone usage.
- [NSFormattingContextListItem](listitem.md) — The formatting context for a list or menu item.
- [NSFormattingContextBeginningOfSentence](beginningofsentence.md) — The formatting context for the beginning of a sentence.
- [NSFormattingContextMiddleOfSentence](middleofsentence.md) — The formatting context for the middle of a sentence.

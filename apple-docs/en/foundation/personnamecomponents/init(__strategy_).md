---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponents/init(_:strategy:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/init(_:strategy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/init%28_%3Astrategy%3A%29.json'
content_hash: 'sha256:0b5a31ca69c44265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponents](../personnamecomponents.md)

# init(_:strategy:)

<sub>Initializer</sub>

Creates a person name components object from a given string by applying the provided parsing strategy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<S>(_ value: S.ParseInput, strategy: S) throws where S : ParseStrategy, S.ParseOutput == PersonNameComponents
```

## Parameters

- `value` — A string to parse into person name components.

- `strategy` — The strategy used to parse a string into person name components.

## Discussion

This method uses a combination of locale rules and the provided parse strategy object to determine the most likely name components for a particular string representation. Parsing name components from a representation created for an existing name components object may not produce equivalent results.

> [!important] Important
> The format style only parses names using Latin or CJK scripts.

## See Also

### Parsing Person Name Components

- [init(_:)](<init(__).md>) — Creates a person name components object from a given string.
- [parseStrategy](formatstyle/parsestrategy.md) — The strategy used to parse a string into person name components.

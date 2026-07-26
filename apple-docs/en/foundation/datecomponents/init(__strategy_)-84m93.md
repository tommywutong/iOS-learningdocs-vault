---
title: 'init(_:strategy:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/datecomponents/init(_:strategy:)-84m93'
source_url: 'https://developer.apple.com/documentation/foundation/datecomponents/init(_:strategy:)-84m93'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/datecomponents/init%28_%3Astrategy%3A%29-84m93.json'
content_hash: 'sha256:08ee843895168b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateComponents](../datecomponents.md)

# init(_:strategy:)

<sub>Initializer</sub>

Creates a new `DateComponents` by parsing the given representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ value: T.ParseInput, strategy: T) throws where T : ParseStrategy, T.ParseOutput == DateComponents
```

## Parameters

- `value` — A representation of a date. The type of the representation is specified by `ParseStrategy.ParseInput`.

- `strategy` — The parse strategy to parse `value` whose `ParseOutput` is `DateComponents`.

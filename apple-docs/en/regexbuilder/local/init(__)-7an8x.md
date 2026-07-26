---
title: 'init(_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/local/init(_:)-7an8x'
source_url: 'https://developer.apple.com/documentation/regexbuilder/local/init(_:)-7an8x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local/init%28_%3A%29-7an8x.json'
content_hash: 'sha256:18c0fe02e6dabc91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Local](../local.md)

# init(_:)

<sub>Initializer</sub>

Creates an atomic group with the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1, C2)
```

## Parameters

- `componentBuilder` — A builder closure that generates a regex component to wrap in an atomic group.

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
doc_path: '/documentation/regexbuilder/local/init(_:)-53gbl'
source_url: 'https://developer.apple.com/documentation/regexbuilder/local/init(_:)-53gbl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local/init%28_%3A%29-53gbl.json'
content_hash: 'sha256:391269b6e695be2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Local](../local.md)

# init(_:)

<sub>Initializer</sub>

Creates an atomic group with the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10)
```

## Parameters

- `componentBuilder` — A builder closure that generates a regex component to wrap in an atomic group.

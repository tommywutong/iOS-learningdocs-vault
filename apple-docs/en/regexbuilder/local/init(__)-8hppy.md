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
doc_path: '/documentation/regexbuilder/local/init(_:)-8hppy'
source_url: 'https://developer.apple.com/documentation/regexbuilder/local/init(_:)-8hppy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local/init%28_%3A%29-8hppy.json'
content_hash: 'sha256:0a775e347de30e13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Local](../local.md)

# init(_:)

<sub>Initializer</sub>

Creates an atomic group with the given regex component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6, C7, C8, C9>(_ component: some RegexComponent) where Output == (Substring, C1, C2, C3, C4, C5, C6, C7, C8, C9)
```

## Parameters

- `component` — The regex component to wrap in an atomic group.

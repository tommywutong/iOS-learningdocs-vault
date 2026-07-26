---
title: 'init(_:_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/zeroormore/init(_:_:)-1d98s'
source_url: 'https://developer.apple.com/documentation/regexbuilder/zeroormore/init(_:_:)-1d98s'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/zeroormore/init%28_%3A_%3A%29-1d98s.json'
content_hash: 'sha256:66a6761caad29aee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [ZeroOrMore](../zeroormore.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component zero or more times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2>(_ behavior: RegexRepetitionBehavior? = nil, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == (Substring, C1?, C2?)
```

## Parameters

- `behavior` — The repetition behavior to use when repeating `component` in the match. If `behavior` is `nil`, the default repetition behavior is used, which can be changed from `eager` by calling `repetitionBehavior(_:)` on the resulting `Regex`.

- `componentBuilder` — A builder closure that generates a regex component.

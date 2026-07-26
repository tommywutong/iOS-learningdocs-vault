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
doc_path: '/documentation/regexbuilder/zeroormore/init(_:_:)-3xl6h'
source_url: 'https://developer.apple.com/documentation/regexbuilder/zeroormore/init(_:_:)-3xl6h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/zeroormore/init%28_%3A_%3A%29-3xl6h.json'
content_hash: 'sha256:677df73f59b168fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [ZeroOrMore](../zeroormore.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component zero or more times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ behavior: RegexRepetitionBehavior? = nil, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent) where Output == Substring
```

## Parameters

- `behavior` — The repetition behavior to use when repeating `component` in the match. If `behavior` is `nil`, the default repetition behavior is used, which can be changed from `eager` by calling `repetitionBehavior(_:)` on the resulting `Regex`.

- `componentBuilder` — A builder closure that generates a regex component.

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
doc_path: '/documentation/regexbuilder/oneormore/init(_:_:)-6pzxz'
source_url: 'https://developer.apple.com/documentation/regexbuilder/oneormore/init(_:_:)-6pzxz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/oneormore/init%28_%3A_%3A%29-6pzxz.json'
content_hash: 'sha256:16983b18582478ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [OneOrMore](../oneormore.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component one or more times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1>(_ component: some RegexComponent, _ behavior: RegexRepetitionBehavior? = nil) where Output == (Substring, C1)
```

## Parameters

- `component` — The regex component.

- `behavior` — The repetition behavior to use when repeating `component` in the match. If `behavior` is `nil`, the default repetition behavior is used, which can be changed from `eager` by calling `repetitionBehavior(_:)` on the resulting `Regex`.

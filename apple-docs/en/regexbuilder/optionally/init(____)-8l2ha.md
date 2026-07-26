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
doc_path: '/documentation/regexbuilder/optionally/init(_:_:)-8l2ha'
source_url: 'https://developer.apple.com/documentation/regexbuilder/optionally/init(_:_:)-8l2ha'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/optionally/init%28_%3A_%3A%29-8l2ha.json'
content_hash: 'sha256:a9397f4cdaeae6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Optionally](../optionally.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component zero or one times.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4>(_ component: some RegexComponent, _ behavior: RegexRepetitionBehavior? = nil) where Output == (Substring, C1?, C2?, C3?, C4?)
```

## Parameters

- `component` — The regex component.

- `behavior` — The repetition behavior to use when repeating `component` in the match. If `behavior` is `nil`, the default repetition behavior is used, which can be changed from `eager` by calling `repetitionBehavior(_:)` on the resulting `Regex`.

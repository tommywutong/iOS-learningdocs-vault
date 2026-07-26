---
title: 'init(_:_:_:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/repeat/init(_:_:_:)-8574u'
source_url: 'https://developer.apple.com/documentation/regexbuilder/repeat/init(_:_:_:)-8574u'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/repeat/init%28_%3A_%3A_%3A%29-8574u.json'
content_hash: 'sha256:127ac61f4f8c6ccd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Repeat](../repeat.md)

# init(_:_:_:)

<sub>Initializer</sub>

Creates a regex component that matches the given component repeated a number of times specified by the given range expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, C6, C7>(_ component: some RegexComponent, _ expression: some RangeExpression<Int>, _ behavior: RegexRepetitionBehavior? = nil) where Output == (Substring, C1?, C2?, C3?, C4?, C5?, C6?, C7?)
```

## Parameters

- `component` — The regex component to repeat.

- `expression` — A range expression specifying the number of times that `component` can repeat.

- `behavior` — The repetition behavior to use when repeating `component` in the match. If `behavior` is `nil`, the default repetition behavior is used, which can be changed from `eager` by calling `repetitionBehavior(_:)` on the resulting `Regex`.

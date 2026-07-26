---
title: 'init(_:transform:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/capture/init(_:transform:)-qygd'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(_:transform:)-qygd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28_%3Atransform%3A%29-qygd.json'
content_hash: 'sha256:4fcd0e4ecbef47f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(_:transform:)

<sub>Initializer</sub>

Creates a capture for the given component, transforming with the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, NewCapture>(_ component: some RegexComponent, transform: @escaping (W) throws -> NewCapture) where Output == (Substring, NewCapture, C1, C2, C3, C4)
```

## Parameters

- `component` — The regex component to capture.

- `transform` — A closure that takes the substring matched by `component` and returns a new value to capture. If `transform` throws an error, matching is abandoned and the error is returned to the caller.

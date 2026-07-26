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
doc_path: '/documentation/regexbuilder/trycapture/init(_:transform:)-2o3dd'
source_url: 'https://developer.apple.com/documentation/regexbuilder/trycapture/init(_:transform:)-2o3dd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/trycapture/init%28_%3Atransform%3A%29-2o3dd.json'
content_hash: 'sha256:f8e0bdb7c96b2c6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [TryCapture](../trycapture.md)

# init(_:transform:)

<sub>Initializer</sub>

Creates a capture for the given component, attempting to transform with the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, C5, NewCapture>(@RegexComponentBuilder _ componentBuilder: () -> some RegexComponent, transform: @escaping (W) throws -> NewCapture?) where Output == (Substring, NewCapture, C1, C2, C3, C4, C5)
```

## Parameters

- `componentBuilder` — A builder closure that generates a regex component to capture.

- `transform` — A closure that takes the substring matched by `component` and returns a new value to capture, or `nil` if matching should proceed, backtracking if allowed. If `transform` throws an error, matching is abandoned and the error is returned to the caller.

---
title: 'init(_:as:transform:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/trycapture/init(_:as:transform:)-4kzw6'
source_url: 'https://developer.apple.com/documentation/regexbuilder/trycapture/init(_:as:transform:)-4kzw6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/trycapture/init%28_%3Aas%3Atransform%3A%29-4kzw6.json'
content_hash: 'sha256:d2dc7588d50c2f39'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [TryCapture](../trycapture.md)

# init(_:as:transform:)

<sub>Initializer</sub>

Creates a capture for the given component using the specified reference, attempting to transform with the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, NewCapture>(_ component: some RegexComponent, as reference: Reference<NewCapture>, transform: @escaping (W) throws -> NewCapture?) where Output == (Substring, NewCapture, C1, C2, C3)
```

## Parameters

- `component` — The regex component to capture.

- `reference` — The reference to use for anything captured by `component`.

- `transform` — A closure that takes the substring matched by `component` and returns a new value to capture, or `nil` if matching should proceed, backtracking if allowed. If `transform` throws an error, matching is abandoned and the error is returned to the caller.

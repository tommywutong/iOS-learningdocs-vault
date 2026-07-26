---
title: 'init(as:_:transform:)'
framework: RegexBuilder
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/regexbuilder/capture/init(as:_:transform:)-4elzn'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(as:_:transform:)-4elzn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28as%3A_%3Atransform%3A%29-4elzn.json'
content_hash: 'sha256:0c189eee41114ae3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(as:_:transform:)

<sub>Initializer</sub>

Creates a capture for the given component using the specified reference, transforming with the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, NewCapture>(as reference: Reference<NewCapture>, @RegexComponentBuilder _ componentBuilder: () -> some RegexComponent, transform: @escaping (W) throws -> NewCapture) where Output == (Substring, NewCapture, C1, C2, C3)
```

## Parameters

- `reference` — The reference to use for anything captured by `component`.

- `componentBuilder` — A builder closure that generates a regex component to capture.

- `transform` — A closure that takes the substring matched by `component` and returns a new value to capture. If `transform` throws an error, matching is abandoned and the error is returned to the caller.

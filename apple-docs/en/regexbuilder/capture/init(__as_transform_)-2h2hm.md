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
doc_path: '/documentation/regexbuilder/capture/init(_:as:transform:)-2h2hm'
source_url: 'https://developer.apple.com/documentation/regexbuilder/capture/init(_:as:transform:)-2h2hm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/capture/init%28_%3Aas%3Atransform%3A%29-2h2hm.json'
content_hash: 'sha256:ee73d4f8c01ed508'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Capture](../capture.md)

# init(_:as:transform:)

<sub>Initializer</sub>

Creates a capture for the given component using the specified reference, transforming with the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<W, C1, C2, C3, C4, NewCapture>(_ component: some RegexComponent, as reference: Reference<NewCapture>, transform: @escaping (W) throws -> NewCapture) where Output == (Substring, NewCapture, C1, C2, C3, C4)
```

## Parameters

- `component` — The regex component to capture.

- `reference` — The reference to use for anything captured by `component`.

- `transform` — A closure that takes the substring matched by `component` and returns a new value to capture. If `transform` throws an error, matching is abandoned and the error is returned to the caller.

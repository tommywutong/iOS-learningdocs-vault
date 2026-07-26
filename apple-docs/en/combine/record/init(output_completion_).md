---
title: 'init(output:completion:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/record/init(output:completion:)'
source_url: 'https://developer.apple.com/documentation/combine/record/init(output:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/init%28output%3Acompletion%3A%29.json'
content_hash: 'sha256:825cfbced5d74764'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Record](../record.md)

# init(output:completion:)

<sub>Initializer</sub>

Creates a record publisher to publish the provided elements, followed by the provided completion value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(output: [Output], completion: Subscribers.Completion<Failure>)
```

## Parameters

- `output` — An array of output elements to publish.

- `completion` — The completion value with which to end publishing.

## See Also

### Creating a record publisher

- [init(record:)](<init(record_).md>) — Creates a publisher to interactively record a series of outputs and a completion.
- [init(recording:)](<init(recording_).md>) — Creates a record publisher from an existing recording.

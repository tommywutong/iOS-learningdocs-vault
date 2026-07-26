---
title: 'init(record:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/record/init(record:)'
source_url: 'https://developer.apple.com/documentation/combine/record/init(record:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/init%28record%3A%29.json'
content_hash: 'sha256:78238b235dcd40fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Record](../record.md)

# init(record:)

<sub>Initializer</sub>

Creates a publisher to interactively record a series of outputs and a completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(record: (inout Record<Output, Failure>.Recording) -> Void)
```

## Parameters

- `record` — A recording instance that can be retrieved after completion to create new record publishers to replay the recording.

## See Also

### Creating a record publisher

- [init(output:completion:)](<init(output_completion_).md>) — Creates a record publisher to publish the provided elements, followed by the provided completion value.
- [init(recording:)](<init(recording_).md>) — Creates a record publisher from an existing recording.

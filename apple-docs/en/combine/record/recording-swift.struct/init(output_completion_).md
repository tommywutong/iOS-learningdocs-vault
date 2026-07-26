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
doc_path: '/documentation/combine/record/recording-swift.struct/init(output:completion:)'
source_url: 'https://developer.apple.com/documentation/combine/record/recording-swift.struct/init(output:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/recording-swift.struct/init%28output%3Acompletion%3A%29.json'
content_hash: 'sha256:1123bb654119310c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Record](../../record.md) · [Recording](../recording-swift.struct.md)

# init(output:completion:)

<sub>Initializer</sub>

Set up a complete recording with the specified output and completion.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(output: [Output], completion: Subscribers.Completion<Failure> = .finished)
```

## See Also

### Creating a recording

- [init()](<init().md>) — Set up a recording in a state ready to receive output.

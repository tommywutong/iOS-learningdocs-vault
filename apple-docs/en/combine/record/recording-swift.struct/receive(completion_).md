---
title: 'receive(completion:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/record/recording-swift.struct/receive(completion:)'
source_url: 'https://developer.apple.com/documentation/combine/record/recording-swift.struct/receive(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/recording-swift.struct/receive%28completion%3A%29.json'
content_hash: 'sha256:9484c3ddc7813e33'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Record](../../record.md) · [Recording](../recording-swift.struct.md)

# receive(completion:)

<sub>Instance Method</sub>

Add a completion to the recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func receive(completion: Subscribers.Completion<Failure>)
```

## Discussion

A `fatalError` will be raised if more than one completion is added.

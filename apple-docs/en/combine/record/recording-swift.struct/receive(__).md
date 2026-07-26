---
title: 'receive(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/record/recording-swift.struct/receive(_:)'
source_url: 'https://developer.apple.com/documentation/combine/record/recording-swift.struct/receive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/record/recording-swift.struct/receive%28_%3A%29.json'
content_hash: 'sha256:a9f77d5cf17a69db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Record](../../record.md) · [Recording](../recording-swift.struct.md)

# receive(_:)

<sub>Instance Method</sub>

Add an output to the recording.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func receive(_ input: Record<Output, Failure>.Recording.Input)
```

## Discussion

A `fatalError` will be raised if output is added after adding completion.

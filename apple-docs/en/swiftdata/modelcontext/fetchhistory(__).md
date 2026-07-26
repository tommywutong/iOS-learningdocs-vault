---
title: 'fetchHistory(_:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+, Swift 5.9+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftdata/modelcontext/fetchhistory(_:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/modelcontext/fetchhistory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/modelcontext/fetchhistory%28_%3A%29.json'
content_hash: 'sha256:2170b207993d15ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ModelContext](../modelcontext.md)

# fetchHistory(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fetchHistory<T>(_ descriptor: HistoryDescriptor<T>) throws -> [T] where T : HistoryTransaction
```

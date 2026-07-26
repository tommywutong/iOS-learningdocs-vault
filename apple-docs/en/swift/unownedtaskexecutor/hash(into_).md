---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unownedtaskexecutor/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/unownedtaskexecutor/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unownedtaskexecutor/hash%28into%3A%29.json'
content_hash: 'sha256:6427b1791194b08a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnownedTaskExecutor](../unownedtaskexecutor.md)

# hash(into:)

<sub>Instance Method</sub>

Hash the executor identity into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Discussion

This function is available independently from the `Hashable` conformance, allowing back-deployment to older runtimes when implementing `Hashable` in user code

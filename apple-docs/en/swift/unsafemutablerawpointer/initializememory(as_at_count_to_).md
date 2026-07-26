---
title: 'initializeMemory(as:at:count:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/initializememory(as:at:count:to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/initializememory(as:at:count:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/initializememory%28as%3Aat%3Acount%3Ato%3A%29.json'
content_hash: 'sha256:a6692e275ee1ae0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# initializeMemory(as:at:count:to:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func initializeMemory<T>(as type: T.Type, at offset: Int = 0, count: Int = 1, to repeatedValue: T) -> UnsafeMutablePointer<T>
```

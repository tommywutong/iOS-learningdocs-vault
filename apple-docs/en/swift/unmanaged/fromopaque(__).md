---
title: 'fromOpaque(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unmanaged/fromopaque(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/fromopaque(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/fromopaque%28_%3A%29.json'
content_hash: 'sha256:b234c7c60ea5d5e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# fromOpaque(_:)

<sub>Type Method</sub>

Unsafely turns an opaque C pointer into an unmanaged class reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func fromOpaque(_ value: UnsafeRawPointer) -> Unmanaged<Instance>
```

## Parameters

- `value` — An opaque C pointer.

## Return Value

An unmanaged class reference to `value`.

## Discussion

This operation does not change reference counts.

```swift
let str: CFString = Unmanaged.fromOpaque(ptr).takeUnretainedValue()
```

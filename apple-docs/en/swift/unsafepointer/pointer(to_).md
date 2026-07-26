---
title: 'pointer(to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafepointer/pointer(to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/pointer(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/pointer%28to%3A%29.json'
content_hash: 'sha256:6f889468d0c03618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# pointer(to:)

<sub>Instance Method</sub>

Obtain a pointer to the stored property referred to by a key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func pointer<Property>(to property: KeyPath<Pointee, Property>) -> UnsafePointer<Property>?
```

## Parameters

- `property` — A `KeyPath` whose `Root` is `Pointee`.

## Return Value

A pointer to the stored property represented by the key path, or `nil`.

## Discussion

If the key path represents a computed property, this function will return `nil`.

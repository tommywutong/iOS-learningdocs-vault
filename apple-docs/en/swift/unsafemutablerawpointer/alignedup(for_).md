---
title: 'alignedUp(for:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/alignedup(for:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/alignedup(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/alignedup%28for%3A%29.json'
content_hash: 'sha256:90fa94be57e171c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# alignedUp(for:)

<sub>Instance Method</sub>

Obtain the next pointer properly aligned to store a value of type `T`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func alignedUp<T>(for type: T.Type) -> UnsafeMutableRawPointer where T : ~Copyable, T : ~Escapable
```

## Parameters

- `type` — The type to be stored at the returned address.

## Return Value

A pointer properly aligned to store a value of type `T`.

## Discussion

If `self` is properly aligned for accessing `T`, this function returns `self`.

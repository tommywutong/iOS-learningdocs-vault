---
title: 'alignedUp(toMultipleOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawpointer/alignedup(tomultipleof:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawpointer/alignedup(tomultipleof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawpointer/alignedup%28tomultipleof%3A%29.json'
content_hash: 'sha256:fea1c505d83882d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawPointer](../unsaferawpointer.md)

# alignedUp(toMultipleOf:)

<sub>Instance Method</sub>

Obtain the next pointer whose bit pattern is a multiple of `alignment`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func alignedUp(toMultipleOf alignment: Int) -> UnsafeRawPointer
```

## Parameters

- `alignment` — The alignment of the returned pointer, in bytes. `alignment` must be a whole power of 2.

## Return Value

A pointer aligned to `alignment`.

## Discussion

If the bit pattern of `self` is a multiple of `alignment`, this function returns `self`.

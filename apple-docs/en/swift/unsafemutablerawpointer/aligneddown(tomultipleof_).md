---
title: 'alignedDown(toMultipleOf:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawpointer/aligneddown(tomultipleof:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/aligneddown(tomultipleof:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/aligneddown%28tomultipleof%3A%29.json'
content_hash: 'sha256:38bdca2a4f55f842'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# alignedDown(toMultipleOf:)

<sub>Instance Method</sub>

Obtain the preceding pointer whose bit pattern is a multiple of `alignment`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func alignedDown(toMultipleOf alignment: Int) -> UnsafeMutableRawPointer
```

## Parameters

- `alignment` — The alignment of the returned pointer, in bytes. `alignment` must be a whole power of 2.

## Return Value

A pointer aligned to `alignment`.

## Discussion

If the bit pattern of `self` is a multiple of `alignment`, this function returns `self`.

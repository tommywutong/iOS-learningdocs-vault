---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafepointer/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafepointer/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafepointer/subscript%28_%3A%29.json'
content_hash: 'sha256:84d6fe5a6f7b428d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafePointer](../unsafepointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the pointee at the specified offset from this pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> Pointee { get }
```

## Parameters

- `i` — The offset from this pointer at which to access an instance, measured in strides of the pointer’s `Pointee` type.

## Overview

For a pointer `p`, the memory at `p + i` must be initialized.

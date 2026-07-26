---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/staticbigint/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/staticbigint/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/staticbigint/subscript%28_%3A%29.json'
content_hash: 'sha256:9c6c9d46de22f6e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StaticBigInt](../staticbigint.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns a 32-bit or 64-bit word of this value’s binary representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(wordIndex: Int) -> UInt { get }
```

## Parameters

- `wordIndex` — A nonnegative zero-based offset.

## Overview

The words are ordered from least significant to most significant, with an infinite sign extension. Negative values are in two’s complement.

```swift
let negative: StaticBigInt = -0x0011223344556677_8899AABBCCDDEEFF
negative.signum()  //-> -1
negative.bitWidth  //-> 118
negative[0]        //-> 0x7766554433221101
negative[1]        //-> 0xFFEEDDCCBBAA9988
negative[2]        //-> 0xFFFFFFFFFFFFFFFF

let positive: StaticBigInt =  0x0011223344556677_8899AABBCCDDEEFF
positive.signum()  //-> +1
positive.bitWidth  //-> 118
positive[0]        //-> 0x8899AABBCCDDEEFF
positive[1]        //-> 0x0011223344556677
positive[2]        //-> 0x0000000000000000
```

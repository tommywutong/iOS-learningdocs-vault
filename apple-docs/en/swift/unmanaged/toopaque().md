---
title: toOpaque()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unmanaged/toopaque()
source_url: 'https://developer.apple.com/documentation/swift/unmanaged/toopaque()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged/toopaque%28%29.json'
content_hash: 'sha256:f63271e91cff8c38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Unmanaged](../unmanaged.md)

# toOpaque()

<sub>Instance Method</sub>

Unsafely converts an unmanaged class reference to a pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func toOpaque() -> UnsafeMutableRawPointer
```

## Return Value

An opaque pointer to the value of this unmanaged reference.

## Discussion

This operation does not change reference counts.

```swift
let str0 = "boxcar" as CFString
let bits = Unmanaged.passUnretained(str0)
let ptr = bits.toOpaque()
```

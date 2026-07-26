---
title: 'init(bitPattern:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/init(bitpattern:)-2i0qy'
source_url: 'https://developer.apple.com/documentation/swift/int/init(bitpattern:)-2i0qy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/init%28bitpattern%3A%29-2i0qy.json'
content_hash: 'sha256:ab53ee3fee660f8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# init(bitPattern:)

<sub>Initializer</sub>

Creates a new value with the bit pattern of the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<P>(bitPattern pointer: P?) where P : _Pointer
```

## Parameters

- `pointer` — The pointer to use as the source for the new integer.

## Discussion

The new value represents the address of the pointer passed as `pointer`. If `pointer` is `nil`, the result is `0`.

## See Also

### Working with Memory Addresses

- [init(bitPattern:)](<init(bitpattern_)-2o9co.md>) — Creates an integer that captures the full value of the given object identifier.
- [init(bitPattern:)](<init(bitpattern_)-5qm7a.md>) — Creates a new value with the bit pattern of the given pointer.

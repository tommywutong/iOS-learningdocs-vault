---
title: 'load(fromByteOffset:as:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/slice/load(frombyteoffset:as:)-45bko'
source_url: 'https://developer.apple.com/documentation/swift/slice/load(frombyteoffset:as:)-45bko'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/load%28frombyteoffset%3Aas%3A%29-45bko.json'
content_hash: 'sha256:13ce532622d3f9ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# load(fromByteOffset:as:)

<sub>Instance Method</sub>

Returns a new instance of the given type, read from the specified offset into the buffer pointer slice’s raw memory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load<T>(fromByteOffset offset: Int = 0, as type: T.Type) -> T
```

## Parameters

- `offset` — The offset into the slice’s memory, in bytes, at which to begin reading data for the new instance. The default is zero.

- `type` — The type to use for the newly constructed instance. The memory must be initialized to a value of a type that is layout compatible with `type`.

## Return Value

A new instance of type `T`, copied from the buffer pointer slice’s memory.

## Discussion

The memory at `offset` bytes into this buffer pointer slice must be properly aligned for accessing `T` and initialized to `T` or another type that is layout compatible with `T`.

You can use this method to create new values from the underlying buffer pointer’s bytes. The following example creates two new `Int32` instances from the memory referenced by the buffer pointer `someBytes`. The bytes for `a` are copied from the first four bytes of `someBytes`, and the bytes for `b` are copied from the next four bytes.

```swift
let a = someBytes[0..<4].load(as: Int32.self)
let b = someBytes[4..<8].load(as: Int32.self)
```

The memory to read for the new instance must not extend beyond the memory region represented by the buffer pointer slice—that is, `offset + MemoryLayout<T>.size` must be less than or equal to the slice’s `count`.

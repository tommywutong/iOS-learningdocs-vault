---
title: 'init(rebasing:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/init(rebasing:)-9mh4j'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/init(rebasing:)-9mh4j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/init%28rebasing%3A%29-9mh4j.json'
content_hash: 'sha256:c4e28229330e93e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# init(rebasing:)

<sub>Initializer</sub>

Creates a raw buffer over the same memory as the given raw buffer slice, with the indices rebased to zero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rebasing slice: Slice<UnsafeRawBufferPointer>)
```

## Parameters

- `slice` — The raw buffer slice to rebase.

## Discussion

The new buffer represents the same region of memory as the slice, but its indices start at zero instead of at the beginning of the slice in the original buffer. The following code creates `slice`, a slice covering part of an existing buffer instance, then rebases it into a new `rebased` buffer.

```swift
let slice = buffer[n...]
let rebased = UnsafeRawBufferPointer(rebasing: slice)
```

After this code has executed, the following are true:

- `rebased.startIndex == 0`
- `rebased[0] == slice[n]`
- `rebased[0] == buffer[n]`
- `rebased.count == slice.count`

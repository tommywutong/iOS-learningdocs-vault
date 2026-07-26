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
doc_path: '/documentation/swift/unsafemutablebufferpointer/init(rebasing:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/init(rebasing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/init%28rebasing%3A%29.json'
content_hash: 'sha256:a2bf1bc71b422b1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# init(rebasing:)

<sub>Initializer</sub>

Creates a buffer over the same memory as the given buffer slice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rebasing slice: Slice<UnsafeMutableBufferPointer<Element>>)
```

## Parameters

- `slice` — The buffer slice to rebase.

## Discussion

The new buffer represents the same region of memory as `slice`, but is indexed starting at zero instead of sharing indices with the original buffer. For example:

```swift
let buffer = returnsABuffer()
let n = 5
let slice = buffer[n...]
let rebased = UnsafeMutableBufferPointer(rebasing: slice)
```

After rebasing `slice` as the `rebased` buffer, the following are true:

- `rebased.startIndex == 0`
- `rebased[0] == slice[n]`
- `rebased[0] == buffer[n]`
- `rebased.count == slice.count`

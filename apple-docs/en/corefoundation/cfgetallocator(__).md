---
title: 'CFGetAllocator(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfgetallocator(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgetallocator(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgetallocator%28_%3A%29.json'
content_hash: 'sha256:b3e23ddd1f4431c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGetAllocator(_:)

<sub>Function</sub>

Returns the allocator used to allocate a Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFGetAllocator(_ cf: CFTypeRef!) -> CFAllocator!
```

## Parameters

- `cf` — The CFType object to examine.

## Return Value

The allocator used to allocate memory for `cf`.

## Discussion

When you are creating a Core Foundation object sometimes you want to ensure that the block of memory allocated for the object is from the same allocator used for another object. One way to do this is to reuse the allocator assigned to an existing Core Foundation object when you call a “creation” function.

## See Also

### Memory Management

- [CFGetRetainCount](<cfgetretaincount(__).md>) — Returns the reference count of a Core Foundation object.

---
title: 'CFGetRetainCount(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfgetretaincount(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgetretaincount(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgetretaincount%28_%3A%29.json'
content_hash: 'sha256:db97a806345659b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGetRetainCount(_:)

<sub>Function</sub>

Returns the reference count of a Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFGetRetainCount(_ cf: CFTypeRef!) -> CFIndex
```

## Parameters

- `cf` — The CFType object to examine.

## Return Value

A number representing the reference count of `cf`.

## Discussion

You increment the reference count using the [CFRetain](cfretain.md) function, and decrement the reference count using the [CFRelease](cfrelease.md) function.

This function may be useful for debugging memory leaks. You normally do not use this function, otherwise.

## See Also

### Memory Management

- [CFGetAllocator](<cfgetallocator(__).md>) — Returns the allocator used to allocate a Core Foundation object.

---
title: CFAllocatorGetDefault()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfallocatorgetdefault()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfallocatorgetdefault()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfallocatorgetdefault%28%29.json'
content_hash: 'sha256:72758adb69d5a413'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAllocatorGetDefault()

<sub>Function</sub>

Gets the default allocator object for the current thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAllocatorGetDefault() -> Unmanaged<CFAllocator>!
```

## Return Value

A reference to the default allocator for the current thread. If none has been explicitly set, returns the generic system allocator, [kCFAllocatorSystemDefault](kcfallocatorsystemdefault.md). Ownership follows [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

See the discussion for [CFAllocatorSetDefault](<cfallocatorsetdefault(__).md>) for more detail on the default allocator and for advice on how and when to set a custom allocator as the default.

## See Also

### Getting and Setting the Default Allocator

- [CFAllocatorSetDefault](<cfallocatorsetdefault(__).md>) — Sets the given allocator as the default for the current thread.

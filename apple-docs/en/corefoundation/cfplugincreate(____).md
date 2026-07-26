---
title: 'CFPlugInCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfplugincreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugincreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugincreate%28_%3A_%3A%29.json'
content_hash: 'sha256:31816280ba492ea9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInCreate(_:_:)

<sub>Function</sub>

Creates a CFPlugIn given its URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInCreate(_ allocator: CFAllocator!, _ plugInURL: CFURL!) -> CFPlugIn!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new plug-in. Pass `NULL` or kCFAllocatorDefault to use the default allocator.

- `plugInURL` — The location of the plug-in.

## Return Value

A new plug-in. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Plug-ins

- [CFPlugInInstanceCreate](<cfplugininstancecreate(______).md>) — Creates a `CFPlugIn` instance of a given type using a given factory.

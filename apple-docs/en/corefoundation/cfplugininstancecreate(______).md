---
title: 'CFPlugInInstanceCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfplugininstancecreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugininstancecreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugininstancecreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:b26ecc9e6ef0ec9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInInstanceCreate(_:_:_:)

<sub>Function</sub>

Creates a `CFPlugIn` instance of a given type using a given factory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInInstanceCreate(_ allocator: CFAllocator!, _ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> UnsafeMutableRawPointer!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the default allocator.

- `factoryUUID` — The UUID representing the factory function to use to create a plug-in of the given type.

- `typeUUID` — The UUID type.

## Return Value

Returns the IUnknown interface for the new plug-in.

## Discussion

The plug-in host uses this function to create an instance of the given type. Unless the plug-in is using dynamic registration, this function causes the plug-in’s code to be loaded into memory.

## See Also

### Creating Plug-ins

- [CFPlugInCreate](<cfplugincreate(____).md>) — Creates a CFPlugIn given its URL.

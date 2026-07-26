---
title: CFPlugInFactoryFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfpluginfactoryfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginfactoryfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginfactoryfunction.json'
content_hash: 'sha256:e023d0bb98b8cf6b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInFactoryFunction

<sub>Type Alias</sub>

Callback function that a plug-in author must implement to create a plug-in instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFPlugInFactoryFunction = (CFAllocator?, CFUUID?) -> UnsafeMutableRawPointer?
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the default allocator.

- `typeUUID` — The UUID type to instantiate.

## Discussion

The plug-in author’s implementation of this function is registered with `CFPlugIn` either statically in the plug-in’s information property list, or dynamically. This function is executed as a result of a call to [CFPlugInInstanceCreate](<cfplugininstancecreate(______).md>) by the plug-in host.

## See Also

### Callbacks

- [CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md) — A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [CFPlugInUnloadFunction](cfpluginunloadfunction.md) — Callback function that is called, if present, just before a plug-in’s code is unloaded.

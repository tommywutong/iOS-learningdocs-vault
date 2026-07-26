---
title: CFPlugInUnloadFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfpluginunloadfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginunloadfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginunloadfunction.json'
content_hash: 'sha256:b0bb658f89ceebdf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInUnloadFunction

<sub>Type Alias</sub>

Callback function that is called, if present, just before a plug-in’s code is unloaded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFPlugInUnloadFunction = (CFPlugIn?) -> Void
```

## Parameters

- `plugIn` — The `CFPlugIn` object that is about to be unloaded from memory. When writing in C++, this parameter functions as a `this` pointer for the plug-in.

## See Also

### Callbacks

- [CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md) — A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [CFPlugInFactoryFunction](cfpluginfactoryfunction.md) — Callback function that a plug-in author must implement to create a plug-in instance.

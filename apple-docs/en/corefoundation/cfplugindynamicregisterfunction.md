---
title: CFPlugInDynamicRegisterFunction
framework: Core Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfplugindynamicregisterfunction
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugindynamicregisterfunction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugindynamicregisterfunction.json'
content_hash: 'sha256:ff6e30334cbf4c6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInDynamicRegisterFunction

<sub>Type Alias</sub>

A callback which provides a plug-in the opportunity to dynamically register its types with a host.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias CFPlugInDynamicRegisterFunction = (CFPlugIn?) -> Void
```

## Parameters

- `plugIn` — The `CFPlugIn` object that is engaged in dynamic registration. When using in C++, this parameter functions as a `this` pointer for the plug-in.

## Discussion

This callback is called as a plug-in is being loaded. This provides the plugin the means to dynamically register its types and factories with a plug-in’s host. The call is triggered by the presence of [kCFPlugInDynamicRegistrationKey](kcfplugindynamicregistrationkey.md) in the plug-in’s information property list.

## See Also

### Callbacks

- [CFPlugInFactoryFunction](cfpluginfactoryfunction.md) — Callback function that a plug-in author must implement to create a plug-in instance.
- [CFPlugInUnloadFunction](cfpluginunloadfunction.md) — Callback function that is called, if present, just before a plug-in’s code is unloaded.

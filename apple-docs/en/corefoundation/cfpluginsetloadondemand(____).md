---
title: 'CFPlugInSetLoadOnDemand(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpluginsetloadondemand(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginsetloadondemand(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginsetloadondemand%28_%3A_%3A%29.json'
content_hash: 'sha256:c5b1fbe444d70a87'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInSetLoadOnDemand(_:_:)

<sub>Function</sub>

Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInSetLoadOnDemand(_ plugIn: CFPlugIn!, _ flag: Bool)
```

## Parameters

- `plugIn` — The plug-in to be loaded on demand.

- `flag` — `true` to enable load on demand, `false` otherwise.

## Discussion

Plug-ins that do static registration are load on demand by default. Plug-ins that do dynamic registration are not load on demand by default.

## See Also

### CFPlugIn Miscellaneous Functions

- [CFPlugInAddInstanceForFactory](<cfpluginaddinstanceforfactory(__).md>) — Registers a new instance of a type with `CFPlugIn`.
- [CFPlugInFindFactoriesForPlugInType](<cfpluginfindfactoriesforplugintype(__).md>) — Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [CFPlugInFindFactoriesForPlugInTypeInPlugIn](<cfpluginfindfactoriesforplugintypeinplugin(____).md>) — Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [CFPlugInGetBundle](<cfplugingetbundle(__).md>) — Returns a plug-in’s bundle.
- [CFPlugInGetTypeID](<cfplugingettypeid().md>) — Returns the type identifier for the `CFPlugIn` opaque type.
- [CFPlugInIsLoadOnDemand](<cfpluginisloadondemand(__).md>) — Determines whether or not a plug-in is loaded on demand.
- [CFPlugInRemoveInstanceForFactory](<cfpluginremoveinstanceforfactory(__).md>) — Unregisters an instance of a type with `CFPlugIn`.

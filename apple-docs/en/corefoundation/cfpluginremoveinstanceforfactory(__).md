---
title: 'CFPlugInRemoveInstanceForFactory(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpluginremoveinstanceforfactory(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginremoveinstanceforfactory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginremoveinstanceforfactory%28_%3A%29.json'
content_hash: 'sha256:3b4ec78b62c99886'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInRemoveInstanceForFactory(_:)

<sub>Function</sub>

Unregisters an instance of a type with `CFPlugIn`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInRemoveInstanceForFactory(_ factoryID: CFUUID!)
```

## Parameters

- `factoryID` — The `CFUUID` object representing the plug-in factory.

## Discussion

If the instance counts of every factory in a plug-in are zero, the plug-in can be unloaded.

## See Also

### CFPlugIn Miscellaneous Functions

- [CFPlugInAddInstanceForFactory](<cfpluginaddinstanceforfactory(__).md>) — Registers a new instance of a type with `CFPlugIn`.
- [CFPlugInFindFactoriesForPlugInType](<cfpluginfindfactoriesforplugintype(__).md>) — Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [CFPlugInFindFactoriesForPlugInTypeInPlugIn](<cfpluginfindfactoriesforplugintypeinplugin(____).md>) — Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [CFPlugInGetBundle](<cfplugingetbundle(__).md>) — Returns a plug-in’s bundle.
- [CFPlugInGetTypeID](<cfplugingettypeid().md>) — Returns the type identifier for the `CFPlugIn` opaque type.
- [CFPlugInIsLoadOnDemand](<cfpluginisloadondemand(__).md>) — Determines whether or not a plug-in is loaded on demand.
- [CFPlugInSetLoadOnDemand](<cfpluginsetloadondemand(____).md>) — Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).

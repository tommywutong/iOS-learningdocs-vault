---
title: CFPlugInGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfplugingettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugingettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugingettypeid%28%29.json'
content_hash: 'sha256:8d32bdec67d36300'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInGetTypeID()

<sub>Function</sub>

Returns the type identifier for the `CFPlugIn` opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the `CFPlugIn` opaque type.

## See Also

### CFPlugIn Miscellaneous Functions

- [CFPlugInAddInstanceForFactory](<cfpluginaddinstanceforfactory(__).md>) — Registers a new instance of a type with `CFPlugIn`.
- [CFPlugInFindFactoriesForPlugInType](<cfpluginfindfactoriesforplugintype(__).md>) — Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [CFPlugInFindFactoriesForPlugInTypeInPlugIn](<cfpluginfindfactoriesforplugintypeinplugin(____).md>) — Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [CFPlugInGetBundle](<cfplugingetbundle(__).md>) — Returns a plug-in’s bundle.
- [CFPlugInIsLoadOnDemand](<cfpluginisloadondemand(__).md>) — Determines whether or not a plug-in is loaded on demand.
- [CFPlugInRemoveInstanceForFactory](<cfpluginremoveinstanceforfactory(__).md>) — Unregisters an instance of a type with `CFPlugIn`.
- [CFPlugInSetLoadOnDemand](<cfpluginsetloadondemand(____).md>) — Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).

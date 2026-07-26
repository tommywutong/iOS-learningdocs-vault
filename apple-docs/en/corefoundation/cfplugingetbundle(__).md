---
title: 'CFPlugInGetBundle(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfplugingetbundle(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugingetbundle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugingetbundle%28_%3A%29.json'
content_hash: 'sha256:fe08d9ea865cb8c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInGetBundle(_:)

<sub>Function</sub>

Returns a plug-in’s bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInGetBundle(_ plugIn: CFPlugIn!) -> CFBundle!
```

## Parameters

- `plugIn` — The plug-in whose bundle to obtain.

## Return Value

The bundle for `plugIn`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

You should _always_ use this function to get a plug-in’s bundle. Never attempt to access the plug-in directly as a bundle.

## See Also

### CFPlugIn Miscellaneous Functions

- [CFPlugInAddInstanceForFactory](<cfpluginaddinstanceforfactory(__).md>) — Registers a new instance of a type with `CFPlugIn`.
- [CFPlugInFindFactoriesForPlugInType](<cfpluginfindfactoriesforplugintype(__).md>) — Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [CFPlugInFindFactoriesForPlugInTypeInPlugIn](<cfpluginfindfactoriesforplugintypeinplugin(____).md>) — Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [CFPlugInGetTypeID](<cfplugingettypeid().md>) — Returns the type identifier for the `CFPlugIn` opaque type.
- [CFPlugInIsLoadOnDemand](<cfpluginisloadondemand(__).md>) — Determines whether or not a plug-in is loaded on demand.
- [CFPlugInRemoveInstanceForFactory](<cfpluginremoveinstanceforfactory(__).md>) — Unregisters an instance of a type with `CFPlugIn`.
- [CFPlugInSetLoadOnDemand](<cfpluginsetloadondemand(____).md>) — Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).

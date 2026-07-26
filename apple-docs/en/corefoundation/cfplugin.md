---
title: CFPlugIn
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfplugin
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugin.json'
content_hash: 'sha256:2693f59843529eac'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugIn

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFPlugIn
```

## Overview

`CFPlugIn` provides a standard architecture for application extensions. With `CFPlugIn`, you can design your application as a host framework that uses a set of executable code modules called plug-ins to provide certain well-defined areas of functionality. This approach allows third-party developers to add features to your application without requiring access to your source code. You can also bundle together plug-ins for multiple platforms and let `CFPlugIn` transparently load the appropriate plug-in at runtime. You can use `CFPlugIn` to add plug-in capability to, or write a plug-in for, your application.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating Plug-ins

- [CFPlugInCreate](<cfplugincreate(____).md>) — Creates a CFPlugIn given its URL.
- [CFPlugInInstanceCreate](<cfplugininstancecreate(______).md>) — Creates a `CFPlugIn` instance of a given type using a given factory.

### Registration

- [CFPlugInRegisterFactoryFunction](<cfpluginregisterfactoryfunction(____).md>) — Registers a factory function and its UUID with a `CFPlugIn` object.
- [CFPlugInRegisterFactoryFunctionByName](<cfpluginregisterfactoryfunctionbyname(______).md>) — Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [CFPlugInRegisterPlugInType](<cfpluginregisterplugintype(____).md>) — Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [CFPlugInUnregisterFactory](<cfpluginunregisterfactory(__).md>) — Removes the given function from a plug-in’s list of registered factory functions.
- [CFPlugInUnregisterPlugInType](<cfpluginunregisterplugintype(____).md>) — Removes the given type from a plug-in’s list of registered types.

### CFPlugIn Miscellaneous Functions

- [CFPlugInAddInstanceForFactory](<cfpluginaddinstanceforfactory(__).md>) — Registers a new instance of a type with `CFPlugIn`.
- [CFPlugInFindFactoriesForPlugInType](<cfpluginfindfactoriesforplugintype(__).md>) — Searches all registered plug-ins for factory functions capable of creating an instance of the given type.
- [CFPlugInFindFactoriesForPlugInTypeInPlugIn](<cfpluginfindfactoriesforplugintypeinplugin(____).md>) — Searches the given plug-in for factory functions capable of creating an instance of the given type.
- [CFPlugInGetBundle](<cfplugingetbundle(__).md>) — Returns a plug-in’s bundle.
- [CFPlugInGetTypeID](<cfplugingettypeid().md>) — Returns the type identifier for the `CFPlugIn` opaque type.
- [CFPlugInIsLoadOnDemand](<cfpluginisloadondemand(__).md>) — Determines whether or not a plug-in is loaded on demand.
- [CFPlugInRemoveInstanceForFactory](<cfpluginremoveinstanceforfactory(__).md>) — Unregisters an instance of a type with `CFPlugIn`.
- [CFPlugInSetLoadOnDemand](<cfpluginsetloadondemand(____).md>) — Enables or disables load on demand for plug-ins that do dynamic registration (only when a client requests an instance of a supported type).

### Callbacks

- [CFPlugInDynamicRegisterFunction](cfplugindynamicregisterfunction.md) — A callback which provides a plug-in the opportunity to dynamically register its types with a host.
- [CFPlugInFactoryFunction](cfpluginfactoryfunction.md) — Callback function that a plug-in author must implement to create a plug-in instance.
- [CFPlugInUnloadFunction](cfpluginunloadfunction.md) — Callback function that is called, if present, just before a plug-in’s code is unloaded.

### Constants

- [Information Property List Keys](cfplugin-information-property-list-keys.md) — A plug-in’s information property list can contain these keys used for registering types, factories, and interfaces.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)

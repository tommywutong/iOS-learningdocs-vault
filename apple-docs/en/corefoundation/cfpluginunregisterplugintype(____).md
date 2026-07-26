---
title: 'CFPlugInUnregisterPlugInType(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpluginunregisterplugintype(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginunregisterplugintype(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginunregisterplugintype%28_%3A_%3A%29.json'
content_hash: 'sha256:e83c9d75de2bc053'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInUnregisterPlugInType(_:_:)

<sub>Function</sub>

Removes the given type from a plug-in’s list of registered types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInUnregisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool
```

## Parameters

- `factoryUUID` — The `CFUUID` object representing the factory function for the type to unregister.

- `typeUUID` — The UUID type to unregister.

## Return Value

`true` if the factory function was successfully unregistered, otherwise `false`.

## Discussion

Used by a plug-in or host when performing dynamic registration.

## See Also

### Registration

- [CFPlugInRegisterFactoryFunction](<cfpluginregisterfactoryfunction(____).md>) — Registers a factory function and its UUID with a `CFPlugIn` object.
- [CFPlugInRegisterFactoryFunctionByName](<cfpluginregisterfactoryfunctionbyname(______).md>) — Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [CFPlugInRegisterPlugInType](<cfpluginregisterplugintype(____).md>) — Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [CFPlugInUnregisterFactory](<cfpluginunregisterfactory(__).md>) — Removes the given function from a plug-in’s list of registered factory functions.

---
title: 'CFPlugInRegisterPlugInType(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpluginregisterplugintype(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginregisterplugintype(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginregisterplugintype%28_%3A_%3A%29.json'
content_hash: 'sha256:70517df96ecfe990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInRegisterPlugInType(_:_:)

<sub>Function</sub>

Registers a type and its corresponding factory function with a `CFPlugIn` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInRegisterPlugInType(_ factoryUUID: CFUUID!, _ typeUUID: CFUUID!) -> Bool
```

## Parameters

- `factoryUUID` — The `CFUUID` object representing the factory function that can create the type being registered.

- `typeUUID` — The UUID type to register.

## Return Value

`true` if the factory function was successfully registered, otherwise `false`.

## Discussion

This function is used by a plug-in or host when performing dynamic registration.

## See Also

### Registration

- [CFPlugInRegisterFactoryFunction](<cfpluginregisterfactoryfunction(____).md>) — Registers a factory function and its UUID with a `CFPlugIn` object.
- [CFPlugInRegisterFactoryFunctionByName](<cfpluginregisterfactoryfunctionbyname(______).md>) — Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.
- [CFPlugInUnregisterFactory](<cfpluginunregisterfactory(__).md>) — Removes the given function from a plug-in’s list of registered factory functions.
- [CFPlugInUnregisterPlugInType](<cfpluginunregisterplugintype(____).md>) — Removes the given type from a plug-in’s list of registered types.

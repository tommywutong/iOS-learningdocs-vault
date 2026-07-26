---
title: 'CFPlugInRegisterFactoryFunctionByName(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpluginregisterfactoryfunctionbyname(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpluginregisterfactoryfunctionbyname(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpluginregisterfactoryfunctionbyname%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d25c6fb4caa9b4b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInRegisterFactoryFunctionByName(_:_:_:)

<sub>Function</sub>

Registers a factory function with a `CFPlugIn` object using the function’s name instead of its UUID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInRegisterFactoryFunctionByName(_ factoryUUID: CFUUID!, _ plugIn: CFPlugIn!, _ functionName: CFString!) -> Bool
```

## Parameters

- `factoryUUID` — The `CFUUID` object representing the factory function to register.

- `plugIn` — The plug-in containing `functionName`.

- `functionName` — The name of the factory function to register.

## Return Value

`true` if the factory function was successfully registered, otherwise `false`.

## Discussion

This function is used by a plug-in or host when performing dynamic registration.

## See Also

### Registration

- [CFPlugInRegisterFactoryFunction](<cfpluginregisterfactoryfunction(____).md>) — Registers a factory function and its UUID with a `CFPlugIn` object.
- [CFPlugInRegisterPlugInType](<cfpluginregisterplugintype(____).md>) — Registers a type and its corresponding factory function with a `CFPlugIn` object.
- [CFPlugInUnregisterFactory](<cfpluginunregisterfactory(__).md>) — Removes the given function from a plug-in’s list of registered factory functions.
- [CFPlugInUnregisterPlugInType](<cfpluginunregisterplugintype(____).md>) — Removes the given type from a plug-in’s list of registered types.

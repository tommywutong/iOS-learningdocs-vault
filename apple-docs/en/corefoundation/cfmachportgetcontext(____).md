---
title: 'CFMachPortGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportgetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportgetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportgetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:28cfb9915735ea60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortGetContext(_:_:)

<sub>Function</sub>

Returns the context information for a CFMachPort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortGetContext(_ port: CFMachPort!, _ context: UnsafeMutablePointer<CFMachPortContext>!)
```

## Parameters

- `port` — The CFMachPort object to examine.

- `context` — A pointer to the structure into which the context information for `port` is to be copied. The information being returned is usually the same information you passed to [CFMachPortCreate](<cfmachportcreate(________).md>) or [CFMachPortCreateWithPort](<cfmachportcreatewithport(__________).md>) when creating `port`. However, if [CFMachPortCreateWithPort](<cfmachportcreatewithport(__________).md>) returned a cached CFMachPort object instead of creating a new object, `context` is filled with information from the original CFMachPort object instead of the information you passed to the function.

## Discussion

The context version number for CFMachPort objects is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## See Also

### Examining a CFMachPort Object

- [CFMachPortGetInvalidationCallBack](<cfmachportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMachPort object.
- [CFMachPortGetPort](<cfmachportgetport(__).md>) — Returns the native Mach port represented by a CFMachPort object.
- [CFMachPortIsValid](<cfmachportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

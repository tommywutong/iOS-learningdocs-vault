---
title: 'CFMachPortIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportisvalid%28_%3A%29.json'
content_hash: 'sha256:df2a119729fae383'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortIsValid(_ port: CFMachPort!) -> Bool
```

## Parameters

- `port` — The CFMachPort object to examine.

## Return Value

`true` if `port` can be used for communication, otherwise `false`.

## See Also

### Examining a CFMachPort Object

- [CFMachPortGetContext](<cfmachportgetcontext(____).md>) — Returns the context information for a CFMachPort object.
- [CFMachPortGetInvalidationCallBack](<cfmachportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMachPort object.
- [CFMachPortGetPort](<cfmachportgetport(__).md>) — Returns the native Mach port represented by a CFMachPort object.

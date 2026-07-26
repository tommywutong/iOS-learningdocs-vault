---
title: 'CFMachPortGetInvalidationCallBack(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportgetinvalidationcallback(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportgetinvalidationcallback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportgetinvalidationcallback%28_%3A%29.json'
content_hash: 'sha256:bc876b81c73d37fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortGetInvalidationCallBack(_:)

<sub>Function</sub>

Returns the invalidation callback function for a CFMachPort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortGetInvalidationCallBack(_ port: CFMachPort!) -> CFMachPortInvalidationCallBack!
```

## Parameters

- `port` — The CFMachPort object to examine.

## Return Value

The callback function invoked when `port` is invalidated. `NULL` if no callback has been set with [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>).

## See Also

### Examining a CFMachPort Object

- [CFMachPortGetContext](<cfmachportgetcontext(____).md>) — Returns the context information for a CFMachPort object.
- [CFMachPortGetPort](<cfmachportgetport(__).md>) — Returns the native Mach port represented by a CFMachPort object.
- [CFMachPortIsValid](<cfmachportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

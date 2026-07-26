---
title: 'CFMachPortGetPort(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportgetport(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportgetport(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportgetport%28_%3A%29.json'
content_hash: 'sha256:6b3444baea5c8665'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortGetPort(_:)

<sub>Function</sub>

Returns the native Mach port represented by a CFMachPort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortGetPort(_ port: CFMachPort!) -> mach_port_t
```

## Parameters

- `port` — The CFMachPort object to examine.

## Return Value

The native Mach port represented by `port`.

## See Also

### Examining a CFMachPort Object

- [CFMachPortGetContext](<cfmachportgetcontext(____).md>) — Returns the context information for a CFMachPort object.
- [CFMachPortGetInvalidationCallBack](<cfmachportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMachPort object.
- [CFMachPortIsValid](<cfmachportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMachPort object is valid and able to receive messages.

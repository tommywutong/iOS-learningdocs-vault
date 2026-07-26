---
title: 'CFMachPortInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportinvalidate%28_%3A%29.json'
content_hash: 'sha256:f1277c65d6c6fe1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortInvalidate(_:)

<sub>Function</sub>

Invalidates a CFMachPort object, stopping it from receiving any more messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortInvalidate(_ port: CFMachPort!)
```

## Parameters

- `port` — The CFMachPort object to invalidate.

## Discussion

Invalidating a CFMachPort object prevents the port from ever receiving any more messages. The CFMachPort object is not deallocated, though. If the port has not already been invalidated, the port’s invalidation callback function is invoked, if one has been set with [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>). The [CFMachPortContext](cfmachportcontext.md)  `info` information for `port` is also released, if a release callback was specified in the port’s context structure. Finally, if a run loop source was created for `port`, the run loop source is invalidated, as well.

If the underlying Mach port is destroyed, the CFMachPort object is automatically invalidated.

## See Also

### Configuring a CFMachPort Object

- [CFMachPortCreateRunLoopSource](<cfmachportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMachPort object.
- [CFMachPortSetInvalidationCallBack](<cfmachportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMachPort object is invalidated.

---
title: 'CFMachPortSetInvalidationCallBack(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmachportsetinvalidationcallback(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmachportsetinvalidationcallback(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmachportsetinvalidationcallback%28_%3A_%3A%29.json'
content_hash: 'sha256:c94ca588d29fdd98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMachPortSetInvalidationCallBack(_:_:)

<sub>Function</sub>

Sets the callback function invoked when a CFMachPort object is invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMachPortSetInvalidationCallBack(_ port: CFMachPort!, _ callout: CFMachPortInvalidationCallBack!)
```

## Parameters

- `port` — The CFMachPort object to modify.

- `callout` — The callback function to invoke when `port` is invalidated. Pass `NULL` to remove a callback.

## Discussion

If `port` is already invalid, `callout` is invoked immediately.

## See Also

### Configuring a CFMachPort Object

- [CFMachPortInvalidate](<cfmachportinvalidate(__).md>) — Invalidates a CFMachPort object, stopping it from receiving any more messages.
- [CFMachPortCreateRunLoopSource](<cfmachportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMachPort object.

---
title: 'CFMessagePortGetContext(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportgetcontext(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportgetcontext(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportgetcontext%28_%3A_%3A%29.json'
content_hash: 'sha256:d6f7bcf00af7f6c1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortGetContext(_:_:)

<sub>Function</sub>

Returns the context information for a CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortGetContext(_ ms: CFMessagePort!, _ context: UnsafeMutablePointer<CFMessagePortContext>!)
```

## Parameters

- `ms` — The message port to examine.

- `context` — A pointer to the structure into which the context information for `ms` is to be copied. The information being returned is usually the same information you passed to [CFMessagePortCreateLocal](<cfmessageportcreatelocal(__________).md>) when creating `ms`. However, if [CFMessagePortCreateLocal](<cfmessageportcreatelocal(__________).md>) returned a cached object instead of creating a new object, `context` is filled with information from the original message port instead of the information you passed to the function.

## Discussion

The context version number for message ports is currently `0`. Before calling this function, you need to initialize the `version` member of `context` to `0`.

## See Also

### Examining a Message Port

- [CFMessagePortGetInvalidationCallBack](<cfmessageportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMessagePort object.
- [CFMessagePortGetName](<cfmessageportgetname(__).md>) — Returns the name with which a CFMessagePort object is registered.
- [CFMessagePortIsRemote](<cfmessageportisremote(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [CFMessagePortIsValid](<cfmessageportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

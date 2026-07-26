---
title: 'CFMessagePortGetInvalidationCallBack(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportgetinvalidationcallback(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportgetinvalidationcallback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportgetinvalidationcallback%28_%3A%29.json'
content_hash: 'sha256:a0d06dc1a22a72b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortGetInvalidationCallBack(_:)

<sub>Function</sub>

Returns the invalidation callback function for a CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortGetInvalidationCallBack(_ ms: CFMessagePort!) -> CFMessagePortInvalidationCallBack!
```

## Parameters

- `ms` — The message port to examine.

## Return Value

The callback function invoked when `ms` is invalidated. `NULL` if no callback has been set with [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>).

## See Also

### Examining a Message Port

- [CFMessagePortGetContext](<cfmessageportgetcontext(____).md>) — Returns the context information for a CFMessagePort object.
- [CFMessagePortGetName](<cfmessageportgetname(__).md>) — Returns the name with which a CFMessagePort object is registered.
- [CFMessagePortIsRemote](<cfmessageportisremote(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [CFMessagePortIsValid](<cfmessageportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

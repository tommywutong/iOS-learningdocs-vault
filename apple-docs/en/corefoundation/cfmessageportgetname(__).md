---
title: 'CFMessagePortGetName(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportgetname(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportgetname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportgetname%28_%3A%29.json'
content_hash: 'sha256:c1ae09ebdc3c5056'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortGetName(_:)

<sub>Function</sub>

Returns the name with which a CFMessagePort object is registered.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortGetName(_ ms: CFMessagePort!) -> CFString!
```

## Parameters

- `ms` — The message port to examine.

## Return Value

The registered name of `ms`, `NULL` if unnamed. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Examining a Message Port

- [CFMessagePortGetContext](<cfmessageportgetcontext(____).md>) — Returns the context information for a CFMessagePort object.
- [CFMessagePortGetInvalidationCallBack](<cfmessageportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMessagePort object.
- [CFMessagePortIsRemote](<cfmessageportisremote(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.
- [CFMessagePortIsValid](<cfmessageportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

---
title: 'CFMessagePortIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportisvalid%28_%3A%29.json'
content_hash: 'sha256:df76cfcfd4ea62b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortIsValid(_ ms: CFMessagePort!) -> Bool
```

## Parameters

- `ms` — The message port to examine.

## Return Value

`true` if `ms` can be used for communication, otherwise `false`.

## See Also

### Examining a Message Port

- [CFMessagePortGetContext](<cfmessageportgetcontext(____).md>) — Returns the context information for a CFMessagePort object.
- [CFMessagePortGetInvalidationCallBack](<cfmessageportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMessagePort object.
- [CFMessagePortGetName](<cfmessageportgetname(__).md>) — Returns the name with which a CFMessagePort object is registered.
- [CFMessagePortIsRemote](<cfmessageportisremote(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.

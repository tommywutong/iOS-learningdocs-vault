---
title: 'CFMessagePortIsRemote(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportisremote(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportisremote(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportisremote%28_%3A%29.json'
content_hash: 'sha256:5a59ecb9063b1f92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortIsRemote(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFMessagePort object represents a remote port.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortIsRemote(_ ms: CFMessagePort!) -> Bool
```

## Parameters

- `ms` — The message port to examine.

## Return Value

`true` if `ms` is a remote port, otherwise `false`.

## See Also

### Examining a Message Port

- [CFMessagePortGetContext](<cfmessageportgetcontext(____).md>) — Returns the context information for a CFMessagePort object.
- [CFMessagePortGetInvalidationCallBack](<cfmessageportgetinvalidationcallback(__).md>) — Returns the invalidation callback function for a CFMessagePort object.
- [CFMessagePortGetName](<cfmessageportgetname(__).md>) — Returns the name with which a CFMessagePort object is registered.
- [CFMessagePortIsValid](<cfmessageportisvalid(__).md>) — Returns a Boolean value that indicates whether a CFMessagePort object is valid and able to send or receive messages.

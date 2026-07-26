---
title: 'CFSocketIsValid(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketisvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketisvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketisvalid%28_%3A%29.json'
content_hash: 'sha256:2ada0abcd64d7379'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketIsValid(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketIsValid(_ s: CFSocket!) -> Bool
```

## Parameters

- `s` — The CFSocket object to examine.

## Return Value

`true` if `s` can be used for communication, otherwise `false`.

## See Also

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketGetTypeID](<cfsocketgettypeid().md>) — Returns the type identifier for the CFSocket opaque type.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.

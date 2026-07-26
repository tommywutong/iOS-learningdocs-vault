---
title: CFSocketGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfsocketgettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketgettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketgettypeid%28%29.json'
content_hash: 'sha256:196ac01ace9ee3db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFSocket opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFSocket opaque type.

## See Also

### Using Sockets

- [CFSocketConnectToAddress](<cfsocketconnecttoaddress(______).md>) — Opens a connection to a remote socket.
- [CFSocketCreateRunLoopSource](<cfsocketcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFSocket object.
- [CFSocketInvalidate](<cfsocketinvalidate(__).md>) — Invalidates a CFSocket object, stopping it from sending or receiving any more messages.
- [CFSocketIsValid](<cfsocketisvalid(__).md>) — Returns a Boolean value that indicates whether a CFSocket object is valid and able to send or receive messages.
- [CFSocketSendData](<cfsocketsenddata(________).md>) — Sends data over a CFSocket object.

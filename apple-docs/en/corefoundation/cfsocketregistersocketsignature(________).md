---
title: 'CFSocketRegisterSocketSignature(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketregistersocketsignature(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketregistersocketsignature(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketregistersocketsignature%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8ecda248b8640a2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketRegisterSocketSignature(_:_:_:_:)

<sub>Function</sub>

Registers a socket signature with a CFSocket name server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketRegisterSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafePointer<CFSocketSignature>!) -> CFSocketError
```

## Parameters

- `nameServerSignature` — The socket signature for the name server. If `NULL`, this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>). If `nameServerSignature` is incomplete, the missing values are replaced with the default server’s values, if appropriate.

- `timeout` — The time to wait for the server to accept a connection and to reply to the registration request.

- `name` — The name with which to register `signature`.

- `signature` — The socket signature to register.

## Return Value

An error code indicating success or failure.

## Discussion

Once a socket signature is registered, other processes can retrieve it with [CFSocketCopyRegisteredSocketSignature](<cfsocketcopyregisteredsocketsignature(__________).md>) and then open a connection to your socket using [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>).

To remove a registered socket signature from the name server, use [CFSocketUnregister](<cfsocketunregister(______).md>).

## See Also

### Core Foundation Socket Name Server Utilities Miscellaneous Functions

- [CFSocketCopyRegisteredSocketSignature](<cfsocketcopyregisteredsocketsignature(__________).md>) — Returns a socket signature registered with a CFSocket name server.
- [CFSocketCopyRegisteredValue](<cfsocketcopyregisteredvalue(__________).md>) — Returns a value registered with a CFSocket name server.
- [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>) — Returns the default port number with which to connect to a CFSocket name server.
- [CFSocketRegisterValue](<cfsocketregistervalue(________).md>) — Registers a property-list value with a CFSocket name server.
- [CFSocketSetDefaultNameRegistryPortNumber](<cfsocketsetdefaultnameregistryportnumber(__).md>) — Sets the default port number with which to connect to a CFSocket name server.
- [CFSocketUnregister](<cfsocketunregister(______).md>) — Unregisters a value or socket signature with a CFSocket name server.

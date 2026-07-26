---
title: 'CFSocketCopyRegisteredSocketSignature(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcopyregisteredsocketsignature(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcopyregisteredsocketsignature(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcopyregisteredsocketsignature%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0d469fdf9019e9fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCopyRegisteredSocketSignature(_:_:_:_:_:)

<sub>Function</sub>

Returns a socket signature registered with a CFSocket name server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCopyRegisteredSocketSignature(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ signature: UnsafeMutablePointer<CFSocketSignature>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError
```

## Parameters

- `nameServerSignature` — The socket signature for the name server. If `NULL`, this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>). If `nameServerSignature` is incomplete, the missing values are replaced with the default server’s values, if appropriate.

- `timeout` — The time to wait for the server to accept a connection and to reply to the registration request.

- `name` — The name of the registered socket signature to retrieve.

- `signature` — A pointer to a [CFSocketSignature](cfsocketsignature.md) structure into which the retrieved socket signature is copied.

- `nameServerAddress` — A pointer to a CFData object into which the name server’s address is copied. Pass `NULL` if you do not want the server’s address.

## Return Value

An error code indicating success or failure.

## Discussion

Once you have the socket signature, you can open a connection to that socket with [CFSocketCreateConnectedToSocketSignature](<cfsocketcreateconnectedtosocketsignature(____________).md>).

## See Also

### Core Foundation Socket Name Server Utilities Miscellaneous Functions

- [CFSocketCopyRegisteredValue](<cfsocketcopyregisteredvalue(__________).md>) — Returns a value registered with a CFSocket name server.
- [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>) — Returns the default port number with which to connect to a CFSocket name server.
- [CFSocketRegisterSocketSignature](<cfsocketregistersocketsignature(________).md>) — Registers a socket signature with a CFSocket name server.
- [CFSocketRegisterValue](<cfsocketregistervalue(________).md>) — Registers a property-list value with a CFSocket name server.
- [CFSocketSetDefaultNameRegistryPortNumber](<cfsocketsetdefaultnameregistryportnumber(__).md>) — Sets the default port number with which to connect to a CFSocket name server.
- [CFSocketUnregister](<cfsocketunregister(______).md>) — Unregisters a value or socket signature with a CFSocket name server.

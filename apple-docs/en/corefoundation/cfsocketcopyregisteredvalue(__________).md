---
title: 'CFSocketCopyRegisteredValue(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketcopyregisteredvalue(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketcopyregisteredvalue(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketcopyregisteredvalue%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e11d340ebaf416c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketCopyRegisteredValue(_:_:_:_:_:)

<sub>Function</sub>

Returns a value registered with a CFSocket name server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketCopyRegisteredValue(_ nameServerSignature: UnsafePointer<CFSocketSignature>!, _ timeout: CFTimeInterval, _ name: CFString!, _ value: UnsafeMutablePointer<Unmanaged<CFPropertyList>?>!, _ nameServerAddress: UnsafeMutablePointer<Unmanaged<CFData>?>!) -> CFSocketError
```

## Parameters

- `nameServerSignature` — The socket signature for the name server. If `NULL`, this function contacts the default server, which is assumed to be a local process using TCP/IP to listen on the port number returned from [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>). If `nameServerSignature` is incomplete, the missing values are replaced with the default server’s values, if appropriate.

- `timeout` — The time to wait for the server to accept a connection and to reply to the registration request.

- `name` — The name of the registered value to return.

- `value` — A pointer to the property list object into which the retrieved value should be copied.

- `nameServerAddress` — A pointer to a CFData object into which the name server’s address is copied. Pass `NULL` if you do not want the server’s address.

## Return Value

An error code indicating success or failure.

## See Also

### Core Foundation Socket Name Server Utilities Miscellaneous Functions

- [CFSocketCopyRegisteredSocketSignature](<cfsocketcopyregisteredsocketsignature(__________).md>) — Returns a socket signature registered with a CFSocket name server.
- [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>) — Returns the default port number with which to connect to a CFSocket name server.
- [CFSocketRegisterSocketSignature](<cfsocketregistersocketsignature(________).md>) — Registers a socket signature with a CFSocket name server.
- [CFSocketRegisterValue](<cfsocketregistervalue(________).md>) — Registers a property-list value with a CFSocket name server.
- [CFSocketSetDefaultNameRegistryPortNumber](<cfsocketsetdefaultnameregistryportnumber(__).md>) — Sets the default port number with which to connect to a CFSocket name server.
- [CFSocketUnregister](<cfsocketunregister(______).md>) — Unregisters a value or socket signature with a CFSocket name server.

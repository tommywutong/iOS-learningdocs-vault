---
title: 'CFSocketSetDefaultNameRegistryPortNumber(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfsocketsetdefaultnameregistryportnumber(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfsocketsetdefaultnameregistryportnumber(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfsocketsetdefaultnameregistryportnumber%28_%3A%29.json'
content_hash: 'sha256:8bcb1c9af1ce75a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFSocketSetDefaultNameRegistryPortNumber(_:)

<sub>Function</sub>

Sets the default port number with which to connect to a CFSocket name server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFSocketSetDefaultNameRegistryPortNumber(_ port: UInt16)
```

## Parameters

- `port` — The port number to use to connect to the CFSocket name server.

## Discussion

If you do not provide a name server signature or leave out the socket address in the signature when calling one of the name registry functions, such as [CFSocketRegisterSocketSignature](<cfsocketregistersocketsignature(________).md>), `port` will be used for the connection.

## See Also

### Core Foundation Socket Name Server Utilities Miscellaneous Functions

- [CFSocketCopyRegisteredSocketSignature](<cfsocketcopyregisteredsocketsignature(__________).md>) — Returns a socket signature registered with a CFSocket name server.
- [CFSocketCopyRegisteredValue](<cfsocketcopyregisteredvalue(__________).md>) — Returns a value registered with a CFSocket name server.
- [CFSocketGetDefaultNameRegistryPortNumber](<cfsocketgetdefaultnameregistryportnumber().md>) — Returns the default port number with which to connect to a CFSocket name server.
- [CFSocketRegisterSocketSignature](<cfsocketregistersocketsignature(________).md>) — Registers a socket signature with a CFSocket name server.
- [CFSocketRegisterValue](<cfsocketregistervalue(________).md>) — Registers a property-list value with a CFSocket name server.
- [CFSocketUnregister](<cfsocketunregister(______).md>) — Unregisters a value or socket signature with a CFSocket name server.

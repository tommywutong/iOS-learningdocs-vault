---
title: SSLConnectionRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslconnectionref
source_url: 'https://developer.apple.com/documentation/security/sslconnectionref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslconnectionref.json'
content_hash: 'sha256:e8f6810c1c34dd54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLConnectionRef

<sub>Type Alias</sub>

A pointer to an opaque I/O connection object.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias SSLConnectionRef = UnsafeRawPointer
```

## Discussion

The I/O connection object refers to data that identifies a connection. The connection data is opaque to Secure Transport; you can set it to any value that your application can use in the callback functions [SSLReadFunc](sslreadfunc.md) and [SSLWriteFunc](sslwritefunc.md) to uniquely identify the connection, such as a socket or endpoint. Use the [SSLSetConnection](<sslsetconnection(____).md>) function to assign a value to the connection object.

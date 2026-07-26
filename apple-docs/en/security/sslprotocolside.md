---
title: SSLProtocolSide
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslprotocolside
source_url: 'https://developer.apple.com/documentation/security/sslprotocolside'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslprotocolside.json'
content_hash: 'sha256:c2207d802bd96e98'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLProtocolSide

<sub>Enumeration</sub>

The flags that indicate whether a context is for the server or client side of a connection.

<sub>Mac Catalyst, macOS</sub>

```swift
@frozen enum SSLProtocolSide
```

## Overview

Use one of these flags with the [SSLCreateContext](<sslcreatecontext(______).md>) function to indicate whether the context is intended for the server side or client side of a connection.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSSLServerSide](sslprotocolside/serverside.md) — Server side. _(deprecated)_
- [kSSLClientSide](sslprotocolside/clientside.md) — Client side. _(deprecated)_

### Initializers

- [init(rawValue:)](<sslprotocolside/init(rawvalue_).md>)

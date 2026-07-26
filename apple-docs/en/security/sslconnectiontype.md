---
title: SSLConnectionType
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sslconnectiontype
source_url: 'https://developer.apple.com/documentation/security/sslconnectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sslconnectiontype.json'
content_hash: 'sha256:04e9a6c38021e28f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SSLConnectionType

<sub>Enumeration</sub>

The flags that indicate whether a context is to be used for streaming or datagram-based communication.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SSLConnectionType
```

## Overview

Use one of these flags with the [SSLCreateContext](<sslcreatecontext(______).md>) function to indicate whether the context is intended for use in stream-based or datagram-based communication.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSSLStreamType](sslconnectiontype/streamtype.md) — Stream-based communication (TCP). _(deprecated)_
- [kSSLDatagramType](sslconnectiontype/datagramtype.md) — Datagram-based communication (UDP). _(deprecated)_

### Initializers

- [init(rawValue:)](<sslconnectiontype/init(rawvalue_).md>)

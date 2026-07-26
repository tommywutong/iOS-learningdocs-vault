---
title: TLS.PeerAuthentication
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/tls/peerauthentication
source_url: 'https://developer.apple.com/documentation/network/tls/peerauthentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls/peerauthentication.json'
content_hash: 'sha256:a687017cf7df1ffc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [TLS](../tls.md)

# TLS.PeerAuthentication

<sub>Enumeration</sub>

PeerAuthentication specifies how to authenticate the peer end of the connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PeerAuthentication
```

## Overview

For clients, the default is `none`. For servers, the default is `required`.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Enumeration Cases

- [TLS.PeerAuthentication.none](peerauthentication/none.md) — Do not authenticate the peer.
- [TLS.PeerAuthentication.optional](peerauthentication/optional.md) — Requests the peer certificate, but if none is provided, proceed with the connection.
- [TLS.PeerAuthentication.required](peerauthentication/required.md) — Always authenticate the peer.

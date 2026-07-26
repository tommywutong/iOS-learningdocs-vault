---
title: DTLS.PeerAuthentication
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/network/dtls/peerauthentication
source_url: 'https://developer.apple.com/documentation/network/dtls/peerauthentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/dtls/peerauthentication.json'
content_hash: 'sha256:8004b5f7202c9108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [DTLS](../dtls.md)

# DTLS.PeerAuthentication

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

- [DTLS.PeerAuthentication.none](peerauthentication/none.md) — Do not authenticate the peer. _(beta)_
- [DTLS.PeerAuthentication.optional](peerauthentication/optional.md) — Requests the peer certificate, but if none is provided, proceed with the connection. _(beta)_
- [DTLS.PeerAuthentication.required](peerauthentication/required.md) — Always authenticate the peer. _(beta)_

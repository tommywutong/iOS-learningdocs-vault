---
title: sec_protocol_verify_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_verify_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_verify_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_verify_t.json'
content_hash: 'sha256:ebc7a873562ba8f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_verify_t

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_verify_t = (sec_protocol_metadata_t, sec_trust_t, @escaping sec_protocol_verify_complete_t) -> Void
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `trust_ref` — A `sec_trust_t` instance.

- `complete` — A `sec_protocol_verify_finish_t` to be invoked when verification is complete.

## Discussion

Block to be invoked when the protocol instance must verify the peer.

```
 NOTE: this may be called one or more times for a given connection.
```

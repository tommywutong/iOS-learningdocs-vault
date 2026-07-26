---
title: sec_protocol_challenge_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_challenge_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_challenge_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_challenge_t.json'
content_hash: 'sha256:ac33bee4a345d77c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_challenge_t

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_challenge_t = (sec_protocol_metadata_t, @escaping sec_protocol_challenge_complete_t) -> Void
```

## Parameters

- `metadata` — A `sec_protocol_metadata_t` instance.

- `complete` — A `sec_protocol_challenge_complete_t` to be invoked when the challenge is complete.

## Discussion

Block to be invoked when the protocol instance is issued a challenge (e.g., a TLS certificate request).

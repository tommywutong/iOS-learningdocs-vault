---
title: sec_protocol_challenge_complete_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_challenge_complete_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_challenge_complete_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_challenge_complete_t.json'
content_hash: 'sha256:412a09da7108151b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_challenge_complete_t

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_challenge_complete_t = (sec_identity_t?) -> Void
```

## Parameters

- `identity` — A `sec_identity_t` containing the identity to use for this challenge.

## Discussion

Block to be invoked when an identity (authentication) challenge is complete.

```
 Note: prior to macOS 10.15, iOS 13.0, watchOS 6.0, and tvOS 13.0, calling this
 block with a NULL `identity` argument was prohibited.
```

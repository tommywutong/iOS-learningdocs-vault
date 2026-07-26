---
title: sec_protocol_verify_complete_t
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sec_protocol_verify_complete_t
source_url: 'https://developer.apple.com/documentation/security/sec_protocol_verify_complete_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_protocol_verify_complete_t.json'
content_hash: 'sha256:a3e897823f10643b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_protocol_verify_complete_t

<sub>Type Alias</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias sec_protocol_verify_complete_t = (Bool) -> Void
```

## Parameters

- `result` — A `bool` indicating if verification succeeded or failed.

## Discussion

Block to be invoked when verification is complete.

---
title: 'sec_identity_access_certificates(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_identity_access_certificates(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_identity_access_certificates(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_identity_access_certificates%28_%3A_%3A%29.json'
content_hash: 'sha256:0677786a8c5a646e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_identity_access_certificates(_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_identity_access_certificates(_ identity: sec_identity_t, _ handler: @escaping (sec_certificate_t) -> Void) -> Bool
```

## Parameters

- `identity` — A `sec_identity_t` instance.

- `handler` — A block to invoke one or more times with `sec_certificate_t` instances.

## Return Value

Returns true if the peer certificates were accessible, false otherwise.

## Discussion

Access the certificates associated with the `sec_identity_t` instance.

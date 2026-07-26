---
title: 'sec_identity_create(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_identity_create(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_identity_create(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_identity_create%28_%3A%29.json'
content_hash: 'sha256:e22e76e7e75bb63b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_identity_create(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_identity_create(_ identity: SecIdentity) -> sec_identity_t?
```

## Parameters

- `identity` — A `SecIdentityRef` instance.

## Return Value

A `sec_identity_t` instance.

## Discussion

Create an ARC-able `sec_identity_t` instance from a `SecIdentityRef`.

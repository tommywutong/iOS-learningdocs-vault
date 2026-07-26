---
title: 'sec_identity_copy_ref(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sec_identity_copy_ref(_:)'
source_url: 'https://developer.apple.com/documentation/security/sec_identity_copy_ref(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sec_identity_copy_ref%28_%3A%29.json'
content_hash: 'sha256:5293e6a8f0db2907'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# sec_identity_copy_ref(_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sec_identity_copy_ref(_ identity: sec_identity_t) -> Unmanaged<SecIdentity>?
```

## Parameters

- `identity` — A `sec_identity_t` instance.

## Return Value

The underlying `SecIdentityRef` instance.

## Discussion

Copy a retained reference to the underlying `SecIdentityRef` instance.

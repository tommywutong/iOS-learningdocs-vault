---
title: 'SecIdentitySetSystemIdentity(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitysetsystemidentity(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitysetsystemidentity(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitysetsystemidentity%28_%3A_%3A%29.json'
content_hash: 'sha256:2f9ea7c3be322f15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentitySetSystemIdentity(_:_:)

<sub>Function</sub>

Assigns the system identity to be associated with a specified domain.

<sub>macOS</sub>

```swift
func SecIdentitySetSystemIdentity(_ domain: CFString, _ idRef: SecIdentity?) -> OSStatus
```

## Parameters

- `domain` — The domain to which the specified identity will be assigned, typically in reverse DNS notation, such as `com.apple.security`.  You may also pass the values defined in [System Identity Domains](system-identity-domains.md).

- `idRef` — The identity to be assigned to the specified domain. Pass `NULL` to delete any currently-assigned identity for the specified domain; in this case, it is not an error if no identity exists for the specified domain.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The caller must be running as root.

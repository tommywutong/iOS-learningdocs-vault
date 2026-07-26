---
title: 'SecIdentityCopySystemIdentity(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycopysystemidentity(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycopysystemidentity(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycopysystemidentity%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f87cfa329e8ede09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCopySystemIdentity(_:_:_:)

<sub>Function</sub>

Obtains the system identity associated with a specified domain.

<sub>macOS</sub>

```swift
func SecIdentityCopySystemIdentity(_ domain: CFString, _ idRef: UnsafeMutablePointer<SecIdentity?>, _ actualDomain: UnsafeMutablePointer<CFString?>?) -> OSStatus
```

## Parameters

- `domain` — The domain for which you want to find an identity, typically in reverse DNS notation, such as `com.apple.security`. You may also pass the values defined in [System Identity Domains](system-identity-domains.md).

- `idRef` — On return, the identity object of the system-wide identity associated with the specified domain. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

- `actualDomain` — On return, the actual domain name of the returned identity object is returned here. This may be different from the requested domain. Pass `NULL` if you do not want this information.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If no system identity exists for the specified domain, a domain specific alternate may be returned instead. This is typically (but not exclusively) the system default identity. ([kSecIdentityDomainDefault](ksecidentitydomaindefault.md)).

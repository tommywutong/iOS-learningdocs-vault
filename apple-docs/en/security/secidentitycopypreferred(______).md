---
title: 'SecIdentityCopyPreferred(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secidentitycopypreferred(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secidentitycopypreferred(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitycopypreferred%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f8e7e5a08f0a9a50'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentityCopyPreferred(_:_:_:)

<sub>Function</sub>

Retrieves the preferred identity for the specified name and key use.

<sub>macOS</sub>

```swift
func SecIdentityCopyPreferred(_ name: CFString, _ keyUsage: CFArray?, _ validIssuers: CFArray?) -> SecIdentity?
```

## Parameters

- `name` — A string containing an email address (RFC 822) or other name for which a preferred identity is requested.

- `keyUsage` — An array containing a list of usage attributes ([kSecAttrCanEncrypt](ksecattrcanencrypt.md), for example), or `NULL` if you do not want to request an identity for a particular usage. See Attribute Item Keys for a complete list of possible usage attributes.

- `validIssuers` — An array of `CFDataRef` objects whose contents are the subject names of allowable issuers, as returned by a call to [SSLCopyDistinguishedNames](<sslcopydistinguishednames(____).md>). Pass `NULL` to allow any issuer.

## Return Value

Returns an identity, or `nil` if no identity from one of the specified issuers has been set as the preferred identity for the specified name and usage. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the identity’s memory when you are done with it.

## Discussion

If a preferred identity has not been set for the supplied name, this function returns `NULL`. Your code should then perform a search for possible identities by calling [SecItemCopyMatching](<secitemcopymatching(____).md>).

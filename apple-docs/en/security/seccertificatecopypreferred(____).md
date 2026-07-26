---
title: 'SecCertificateCopyPreferred(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopypreferred(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopypreferred(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopypreferred%28_%3A_%3A%29.json'
content_hash: 'sha256:aef2aad94aba4222'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyPreferred(_:_:)

<sub>Function</sub>

Returns the preferred certificate for the specified name and key usage.

<sub>macOS</sub>

```swift
func SecCertificateCopyPreferred(_ name: CFString, _ keyUsage: CFArray?) -> SecCertificate?
```

## Parameters

- `name` — A string containing an email address (RFC 822) or other name for which a preferred certificate is requested.

- `keyUsage` — An array containing a list of usage attributes ([kSecAttrCanEncrypt](ksecattrcanencrypt.md), for example), or `NULL` if you do not want to request a certificate based on a particular usage. See Attribute Item Keys for a complete list of possible usage attributes.

## Return Value

The preferred certificate for the specified name and key usage, or `NULL` if a matching certificate does not exist. In Objective-C, free the certificate with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.

## Discussion

This function is typically used to obtain the preferred encryption certificate for an email recipient. If a preferred certificate has not been set for the supplied name, this function returns `NULL`. Your code should then perform a search for possible certificates by calling [SecItemCopyMatching](<secitemcopymatching(____).md>).

---
title: 'SecCertificateSetPreferred(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatesetpreferred(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatesetpreferred(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatesetpreferred%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a29fe1437e17cb90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateSetPreferred(_:_:_:)

<sub>Function</sub>

Sets the certificate that should be preferred for the specified name and key use.

<sub>macOS</sub>

```swift
func SecCertificateSetPreferred(_ certificate: SecCertificate?, _ name: CFString, _ keyUsage: CFArray?) -> OSStatus
```

## Parameters

- `certificate` — The key to use as the preferred certificate for the specified name and key usage.

- `name` — A string containing an email address (RFC 822) or other name for which a preferred certificate is requested.

- `keyUsage` — An array containing a list of usage attributes ([kSecAttrCanEncrypt](ksecattrcanencrypt.md), for example), or `NULL` if you want this certificate to be preferred for any usage. See Attribute Item Keys for a complete list of possible usage attributes.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

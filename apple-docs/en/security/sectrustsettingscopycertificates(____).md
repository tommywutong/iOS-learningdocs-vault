---
title: 'SecTrustSettingsCopyCertificates(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingscopycertificates(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingscopycertificates(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingscopycertificates%28_%3A_%3A%29.json'
content_hash: 'sha256:66bc26ddf9747af0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsCopyCertificates(_:_:)

<sub>Function</sub>

Obtains an array of all certificates that have trust settings in a specific trust settings domain.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsCopyCertificates(_ domain: SecTrustSettingsDomain, _ certArray: UnsafeMutablePointer<CFArray?>?) -> OSStatus
```

## Parameters

- `domain` — The trust settings domain for which you want a list of certificates. For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

- `certArray` — On return, an array of `SecCertificateRef` objects representing the certificates that have trust settings in the specified domain. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecNoTrustSettings](errsecnotrustsettings.md) if no trust settings exist for the specified domain.

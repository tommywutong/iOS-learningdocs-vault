---
title: 'SecTrustSettingsCopyModificationDate(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingscopymodificationdate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingscopymodificationdate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingscopymodificationdate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:8c53a558655eaae3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsCopyModificationDate(_:_:_:)

<sub>Function</sub>

Obtains the date and time at which a certificate’s trust settings were last modified.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsCopyModificationDate(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain, _ modificationDate: UnsafeMutablePointer<CFDate?>) -> OSStatus
```

## Parameters

- `certRef` — The certificate for which you wish to obtain the modification time. Pass the value `kSecTrustSettingsDefaultRootCertSetting` to obtain the modification time for the default root certificate trust settings for the domain.

- `domain` — The trust settings domain of the trust settings for which you wish to obtain the modification time (it’s possible for a single certificate to have trust settings in more than one domain). For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

- `modificationDate` — On return, the date and time at which the certificate’s trust settings were last modified. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecItemNotFound](errsecitemnotfound.md) if no trust settings exist for the specified certificate and domain.

---
title: 'SecTrustSettingsRemoveTrustSettings(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingsremovetrustsettings(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingsremovetrustsettings(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingsremovetrustsettings%28_%3A_%3A%29.json'
content_hash: 'sha256:2118f5f29b58aa88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsRemoveTrustSettings(_:_:)

<sub>Function</sub>

Deletes the trust settings for a certificate.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsRemoveTrustSettings(_ certRef: SecCertificate, _ domain: SecTrustSettingsDomain) -> OSStatus
```

## Parameters

- `certRef` — The certificate whose trust settings you wish to remove. Pass the value [kSecTrustSettingsDefaultRootCertSetting](ksectrustsettingsdefaultrootcertsetting.md) to remove the default root certificate trust settings for the domain.

- `domain` — The trust settings domain for which you wish to remove the trust settings. For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecItemNotFound](errsecitemnotfound.md) if no trust settings exist for the certificate.

## Discussion

If a certificate has no trust settings, the certificate must be verified to a known, trusted certificate.

---
title: 'SecTrustSettingsImportExternalRepresentation(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingsimportexternalrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingsimportexternalrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingsimportexternalrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:445717fa8175486c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsImportExternalRepresentation(_:_:)

<sub>Function</sub>

Imports trust settings into a trust domain.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsImportExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: CFData) -> OSStatus
```

## Parameters

- `domain` — The trust settings domain into which you want to import trust settings. For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

- `trustSettings` — An external representation of the trust settings (created by the [SecTrustSettingsCreateExternalRepresentation](<sectrustsettingscreateexternalrepresentation(____).md>) function) that you want to import.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Trust settings for a certificate are associated with the hash of the certificate. Whenever the system encounters a certificate with the hash value associated with the trust settings, it applies those trust settings to the certificate. This function allows you to import trust settings in a portable data format that was exported from another machine. You can use this ability, for example, to clone trust settings to all the machines within an enterprise or university.

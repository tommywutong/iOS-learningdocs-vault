---
title: 'SecTrustSettingsCreateExternalRepresentation(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsettingscreateexternalrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingscreateexternalrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingscreateexternalrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:433d39b2746f027a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsCreateExternalRepresentation(_:_:)

<sub>Function</sub>

Obtains an external, portable representation of the specified domain’s trust settings.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecTrustSettingsCreateExternalRepresentation(_ domain: SecTrustSettingsDomain, _ trustSettings: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `domain` — The trust settings domain for which you want an external representation of trust settings. For possible values, see [SecTrustSettingsDomain](sectrustsettingsdomain.md).

- `trustSettings` — An external representation of the domain’s trust settings. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md). Returns [errSecNoTrustSettings](errsecnotrustsettings.md) if no trust settings exist for the specified domain.

## Discussion

Trust settings for a certificate are associated with the hash of the certificate. Whenever the system encounters a certificate with the hash value associated with the trust settings, it applies those trust settings to the certificate. This function allows you to export trust settings to a portable data format that can subsequently be imported on another machine. You can use this ability, for example, to clone trust settings to all the machines within an enterprise or university.

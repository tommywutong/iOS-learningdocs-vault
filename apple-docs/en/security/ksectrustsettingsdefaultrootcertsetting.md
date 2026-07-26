---
title: kSecTrustSettingsDefaultRootCertSetting
framework: Security
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksectrustsettingsdefaultrootcertsetting
source_url: 'https://developer.apple.com/documentation/security/ksectrustsettingsdefaultrootcertsetting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectrustsettingsdefaultrootcertsetting.json'
content_hash: 'sha256:29ca648c1156a7ef'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTrustSettingsDefaultRootCertSetting

<sub>Macro</sub>

A value indicating the default root certificate trust settings when used as a certificate object in a trust settings API function.

<sub>Mac Catalyst, macOS</sub>

```objc
#define kSecTrustSettingsDefaultRootCertSetting
```

## Discussion

Use this value with the [SecTrustSettingsSetTrustSettings](<sectrustsettingssettrustsettings(______).md>) function to set the default trust settings for root certificates. When evaluating trust settings for a root certificate in a given domain, if no matching explicit trust settings exist for that certificate, then the default value for the effective trust setting is returned (assuming that a default has been set and that the result is not [kSecTrustSettingsResultUnspecified](sectrustsettingsresult/unspecified.md)).

---
title: SecTrustSettingsResult
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustsettingsresult
source_url: 'https://developer.apple.com/documentation/security/sectrustsettingsresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsettingsresult.json'
content_hash: 'sha256:8cd4c02fa96ba7ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSettingsResult

<sub>Enumeration</sub>

Trust settings returned in usage constraints dictionaries.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecTrustSettingsResult
```

## Overview

These values appear in the usage constraints dictionaries returned by the [SecTrustSettingsCopyTrustSettings](<sectrustsettingscopytrustsettings(______).md>) and [SecTrustSettingsSetTrustSettings](<sectrustsettingssettrustsettings(______).md>) functions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecTrustSettingsResultInvalid](sectrustsettingsresult/invalid.md) — Never valid in a trust settings array or in an API call.
- [kSecTrustSettingsResultTrustRoot](sectrustsettingsresult/trustroot.md) — This root certificate is explicitly trusted.
- [kSecTrustSettingsResultTrustAsRoot](sectrustsettingsresult/trustasroot.md) — This non-root certificate is explicitly trusted as if it were a trusted root.
- [kSecTrustSettingsResultDeny](sectrustsettingsresult/deny.md) — This certificate is explicitly distrusted.
- [kSecTrustSettingsResultUnspecified](sectrustsettingsresult/unspecified.md) — This certificate is neither trusted nor distrusted. This value can be used to specify an “allowed error” without assigning trust to a specific certificate.

### Initializers

- [init(rawValue:)](<sectrustsettingsresult/init(rawvalue_).md>)

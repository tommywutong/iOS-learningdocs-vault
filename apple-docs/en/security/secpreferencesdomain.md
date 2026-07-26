---
title: SecPreferencesDomain
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secpreferencesdomain
source_url: 'https://developer.apple.com/documentation/security/secpreferencesdomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpreferencesdomain.json'
content_hash: 'sha256:f0e376284bc12307'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPreferencesDomain

<sub>Enumeration</sub>

The keychain preference domains.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecPreferencesDomain
```

## Overview

A preference domain is a set of security-related preferences, such as the default keychain and the current keychain search list. The default preference domain for system daemons (that is, for daemons running in the root session) is the system domain. The default preference domain for all other programs is the user domain. A common preference appears for all users and the system. For example, if you add a keychain to the keychain search list using [kSecPreferencesDomainCommon](secpreferencesdomain/common.md) for the preference domain, the keychain is added to the search list for all users and the system.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kSecPreferencesDomainUser](secpreferencesdomain/user.md) — Indicates the user preference domain preferences.
- [kSecPreferencesDomainSystem](secpreferencesdomain/system.md) — Indicates the system or daemon preference domain preferences.
- [kSecPreferencesDomainCommon](secpreferencesdomain/common.md) — Indicates the preferences are common to everyone.
- [kSecPreferencesDomainDynamic](secpreferencesdomain/dynamic.md) — Indicates a dynamic search list (typically provided by removable keychains such as smart cards).

### Initializers

- [init(rawValue:)](<secpreferencesdomain/init(rawvalue_).md>)

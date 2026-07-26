---
title: kSecGuestAttributeHash
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecguestattributehash
source_url: 'https://developer.apple.com/documentation/security/ksecguestattributehash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecguestattributehash.json'
content_hash: 'sha256:a4d16253f8593e85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecGuestAttributeHash

<sub>Global Variable</sub>

A key whose value is a data object containing the SHA-1 hash of the code directory.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecGuestAttributeHash: CFString
```

## Discussion

This hash can be used as a unique identifier to recognize this specific code in the future. This identifier is tied to the current version of the code, unlike the [kSecCodeInfoIdentifier](kseccodeinfoidentifier.md) identifier, which remains stable across developer-approved updates. If you are not passing this hash in the attribute dictionary when you call the [SecHostCreateGuest](sechostcreateguest.md) function, then you must pass the [kSecCSGenerateGuestHash](kseccsgenerateguesthash.md) flag to the function as well.

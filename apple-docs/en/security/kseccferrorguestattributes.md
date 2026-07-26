---
title: kSecCFErrorGuestAttributes
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorguestattributes
source_url: 'https://developer.apple.com/documentation/security/kseccferrorguestattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorguestattributes.json'
content_hash: 'sha256:f88d8c4728044190'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorGuestAttributes

<sub>Global Variable</sub>

A key whose value is a Core Foundation object containing an attribute that is unrecognized or that contains a value of the wrong type.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorGuestAttributes: CFString
```

## Discussion

This key is present when you pass a bad guest attribute to the [SecHostCreateGuest](sechostcreateguest.md) or [SecHostSetGuestStatus](sechostsetgueststatus.md) function.

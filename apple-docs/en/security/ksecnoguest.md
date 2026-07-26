---
title: kSecNoGuest
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/ksecnoguest
source_url: 'https://developer.apple.com/documentation/security/ksecnoguest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksecnoguest.json'
content_hash: 'sha256:60f1a136e5766fa6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecNoGuest

<sub>Global Variable</sub>

Not a valid `SecGuestRef` object.

<sub>Mac Catalyst, macOS</sub>

```swift
var kSecNoGuest: SecGuestRef { get }
```

## Discussion

Some functions in the API use this value to indicate that there is no guest, and some functions use it to indicate that the function applies to the host itself rather than to a guest.

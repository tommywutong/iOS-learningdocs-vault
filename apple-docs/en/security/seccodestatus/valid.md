---
title: valid
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccodestatus/valid
source_url: 'https://developer.apple.com/documentation/security/seccodestatus/valid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodestatus/valid.json'
content_hash: 'sha256:04679909db593d1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCodeStatus](../seccodestatus.md)

# valid

<sub>Type Property</sub>

The code is dynamically valid.

<sub>Mac Catalyst, macOS</sub>

```swift
static var valid: SecCodeStatus { get }
```

## Discussion

Code that’s dynamically valid is running code that started properly signed and has not been invalidated since it started. The valid bit can not be set on running code; it can only be cleared. If you do not set the `kSecCodeStatusValid` flag during creation of the guest with the [SecCodeGetTypeID](<../seccodegettypeid().md>) function, then the new guest is created dynamically invalid and can never become dynamically valid. Note that this bit does not make any representations about the static validity of the code.

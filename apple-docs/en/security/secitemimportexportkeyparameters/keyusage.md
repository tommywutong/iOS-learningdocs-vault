---
title: keyUsage
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters/keyusage
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/keyusage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/keyusage.json'
content_hash: 'sha256:2f4b08323be3c0da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# keyUsage

<sub>Instance Property</sub>

An array containing usage attributes applied to a key on import.

<sub>macOS</sub>

```swift
var keyUsage: Unmanaged<CFArray>?
```

## Discussion

The array may contain any of the following key usage constants:

- [kSecAttrCanEncrypt](../ksecattrcanencrypt.md)
- [kSecAttrCanDecrypt](../ksecattrcandecrypt.md)
- [kSecAttrCanDerive](../ksecattrcanderive.md)
- [kSecAttrCanSign](../ksecattrcansign.md)
- [kSecAttrCanVerify](../ksecattrcanverify.md)
- [kSecAttrCanWrap](../ksecattrcanwrap.md)
- [kSecAttrCanUnwrap](../ksecattrcanunwrap.md)

If the array is `NULL`, all operations are allowed by default.

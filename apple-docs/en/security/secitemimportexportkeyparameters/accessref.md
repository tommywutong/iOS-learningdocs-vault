---
title: accessRef
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters/accessref
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/accessref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/accessref.json'
content_hash: 'sha256:4f77f9c75e9d89e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# accessRef

<sub>Instance Property</sub>

Specifies the initial access controls of imported private keys.

<sub>macOS</sub>

```swift
var accessRef: Unmanaged<SecAccess>?
```

## Discussion

If more than one private key is being imported, all private keys get the same initial access controls. If this field is `NULL` when private keys are being imported, then the access object for the keychain item for an imported private key depends on the [kSecKeyNoAccessControl](../seckeyimportexportflags/noaccesscontrol.md) bit in the `flags` parameter. When that flag is `0` (or `keyParams` is `NULL`), the default access control is used. When the flag is `1`, no access object is attached to the keychain item for imported private keys.

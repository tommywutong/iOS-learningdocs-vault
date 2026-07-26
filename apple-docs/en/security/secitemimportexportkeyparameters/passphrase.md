---
title: passphrase
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secitemimportexportkeyparameters/passphrase
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/passphrase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/passphrase.json'
content_hash: 'sha256:05b5bb1e1606f891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# passphrase

<sub>Instance Property</sub>

The password to use during key import or export.

<sub>macOS</sub>

```swift
var passphrase: Unmanaged<CFTypeRef>?
```

## Discussion

You may specify either a [CFString](../../corefoundation/cfstring.md) or a [CFData](../../corefoundation/cfdata.md) instance for the passphrase. The PKCS12 format requires passwords in Unicode format, and passing in a [CFString](../../corefoundation/cfstring.md) as the password is the surest way to meet this requirement  (and ensure compatibility with other implementations). If you supply a [CFData](../../corefoundation/cfdata.md) instance as the password for a PKCS12 export operation, the data is assumed to be in UTF8 form and converted as appropriate.

When importing or exporting keys ([SecKey](../seckey.md) objects) in one of the wrapped formats ([kSecFormatWrappedOpenSSL](../secexternalformat/formatwrappedopenssl.md), [kSecFormatWrappedSSH](../secexternalformat/formatwrappedssh.md), or [kSecFormatWrappedPKCS8](../secexternalformat/formatwrappedpkcs8.md)) or in PKCS12 format, you must either explicitly specify the passphrase field or set the [kSecKeySecurePassphrase](../seckeyimportexportflags/securepassphrase.md) bit the flags field (to prompt the user to enter the password).

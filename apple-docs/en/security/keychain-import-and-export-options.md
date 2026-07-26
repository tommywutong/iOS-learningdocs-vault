---
title: Keychain Import and Export Options
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keychain-import-and-export-options
source_url: 'https://developer.apple.com/documentation/security/keychain-import-and-export-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keychain-import-and-export-options.json'
content_hash: 'sha256:2140ba91cf2e0df0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Identities](identities.md)

# Keychain Import and Export Options

<sub>API Collection</sub>

Use these constants when you pass dictionary-based arguments to import and export functions.

## Topics

### Constants

- [kSecImportExportPassphrase](ksecimportexportpassphrase.md) — A passphrase (represented by a `CFStringRef` object) to be used when exporting to or importing from PKCS#12 format.
- [kSecImportExportKeychain](ksecimportexportkeychain.md) — A keychain represented by a SecKeychainRef to be used as the target when importing or exporting.
- [kSecImportExportAccess](ksecimportexportaccess.md) — An initial access control list represented by a [SecAccess](secaccess.md) object.

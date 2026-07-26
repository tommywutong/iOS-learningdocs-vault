---
title: 'init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeyimportexportparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyimportexportparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyimportexportparameters/init%28version%3Aflags%3Apassphrase%3Aalerttitle%3Aalertprompt%3Aaccessref%3Akeyusage%3Akeyattributes%3A%29.json'
content_hash: 'sha256:aa126f7823e2de8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyImportExportParameters](../seckeyimportexportparameters.md)

# init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)

<sub>Initializer</sub>

Creates a new import/export parameter structure.

<sub>macOS</sub>

```swift
init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<CFTypeRef>?, alertTitle: Unmanaged<CFString>, alertPrompt: Unmanaged<CFString>, accessRef: Unmanaged<SecAccess>?, keyUsage: CSSM_KEYUSE, keyAttributes: CSSM_KEYATTR_FLAGS)
```

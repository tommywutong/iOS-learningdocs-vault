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
doc_path: '/documentation/security/secitemimportexportkeyparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:)'
source_url: 'https://developer.apple.com/documentation/security/secitemimportexportkeyparameters/init(version:flags:passphrase:alerttitle:alertprompt:accessref:keyusage:keyattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secitemimportexportkeyparameters/init%28version%3Aflags%3Apassphrase%3Aalerttitle%3Aalertprompt%3Aaccessref%3Akeyusage%3Akeyattributes%3A%29.json'
content_hash: 'sha256:8282534ab45ab079'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecItemImportExportKeyParameters](../secitemimportexportkeyparameters.md)

# init(version:flags:passphrase:alertTitle:alertPrompt:accessRef:keyUsage:keyAttributes:)

<sub>Initializer</sub>

<sub>macOS</sub>

```swift
init(version: UInt32, flags: SecKeyImportExportFlags, passphrase: Unmanaged<CFTypeRef>?, alertTitle: Unmanaged<CFString>?, alertPrompt: Unmanaged<CFString>?, accessRef: Unmanaged<SecAccess>?, keyUsage: Unmanaged<CFArray>?, keyAttributes: Unmanaged<CFArray>?)
```

---
title: 'SecTrustedApplicationSetData(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.10 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectrustedapplicationsetdata(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustedapplicationsetdata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustedapplicationsetdata%28_%3A_%3A%29.json'
content_hash: 'sha256:ff0968fe1ce7104f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustedApplicationSetData(_:_:)

<sub>Function</sub>

Sets the data of a given trusted app instance.

> [!warning] Deprecated
> SecKeychain is deprecated

<sub>macOS</sub>

```swift
func SecTrustedApplicationSetData(_ appRef: SecTrustedApplication, _ data: CFData) -> OSStatus
```

## Parameters

- `appRef` — A trusted application object.

- `data` — A reference to the data to set in the trusted application.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

If you use the [SecTrustedApplicationCopyData](<sectrustedapplicationcopydata(____).md>) method to extract the data from a trusted app instance for storage or transmission, you can use the [SecTrustedApplicationSetData](<sectrustedapplicationsetdata(____).md>) method to insert that data into a new trusted app. Doing so creates an object that identifies the same app as the original trusted app instance.

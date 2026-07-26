---
title: isEncrypted
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/isencrypted
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/isencrypted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/isencrypted.json'
content_hash: 'sha256:a7559eae9ddd6826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# isEncrypted

<sub>Instance Property</sub>

Returns whether the specified PDF file is encrypted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEncrypted: Bool { get }
```

## Discussion

If the document is encrypted, a password must be supplied before certain operations are enabled. For more information, see [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>).

## See Also

### Working with an Encrypted PDF Document

- [CGPDFDocumentAllowsCopying](allowscopying.md) — Returns whether the specified PDF document allows copying.
- [CGPDFDocumentAllowsPrinting](allowsprinting.md) — Returns whether a PDF document allows printing.
- [CGPDFDocumentIsUnlocked](isunlocked.md) — Returns whether the specified PDF document is currently unlocked.
- [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>) — Unlocks an encrypted PDF document when a valid password is supplied.

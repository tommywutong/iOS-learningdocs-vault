---
title: allowsPrinting
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/allowsprinting
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/allowsprinting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/allowsprinting.json'
content_hash: 'sha256:4e14dc342e1bffc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# allowsPrinting

<sub>Instance Property</sub>

Returns whether a PDF document allows printing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsPrinting: Bool { get }
```

## Discussion

If the document is encrypted and the current password doesn’t grant permission to perform printing, this returns [false](../../swift/false.md).

## See Also

### Working with an Encrypted PDF Document

- [CGPDFDocumentIsEncrypted](isencrypted.md) — Returns whether the specified PDF file is encrypted.
- [CGPDFDocumentAllowsCopying](allowscopying.md) — Returns whether the specified PDF document allows copying.
- [CGPDFDocumentIsUnlocked](isunlocked.md) — Returns whether the specified PDF document is currently unlocked.
- [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>) — Unlocks an encrypted PDF document when a valid password is supplied.

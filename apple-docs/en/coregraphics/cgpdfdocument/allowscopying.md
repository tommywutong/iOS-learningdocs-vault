---
title: allowsCopying
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/allowscopying
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/allowscopying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/allowscopying.json'
content_hash: 'sha256:5fe8de3a3aa1a541'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# allowsCopying

<sub>Instance Property</sub>

Returns whether the specified PDF document allows copying.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCopying: Bool { get }
```

## Discussion

If the document is encrypted and the current password doesn’t grant permission to perform copying, this returns [false](../../swift/false.md).

## See Also

### Working with an Encrypted PDF Document

- [CGPDFDocumentIsEncrypted](isencrypted.md) — Returns whether the specified PDF file is encrypted.
- [CGPDFDocumentAllowsPrinting](allowsprinting.md) — Returns whether a PDF document allows printing.
- [CGPDFDocumentIsUnlocked](isunlocked.md) — Returns whether the specified PDF document is currently unlocked.
- [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>) — Unlocks an encrypted PDF document when a valid password is supplied.

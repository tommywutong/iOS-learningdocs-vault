---
title: isUnlocked
framework: Core Graphics
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpdfdocument/isunlocked
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/isunlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/isunlocked.json'
content_hash: 'sha256:d3f86731931fcd8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# isUnlocked

<sub>Instance Property</sub>

Returns whether the specified PDF document is currently unlocked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isUnlocked: Bool { get }
```

## Discussion

There are two possible reasons why a PDF document is unlocked:

- The document is not encrypted.
- The document is encrypted, and a valid password was previously specified using [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>).

## See Also

### Working with an Encrypted PDF Document

- [CGPDFDocumentIsEncrypted](isencrypted.md) — Returns whether the specified PDF file is encrypted.
- [CGPDFDocumentAllowsCopying](allowscopying.md) — Returns whether the specified PDF document allows copying.
- [CGPDFDocumentAllowsPrinting](allowsprinting.md) — Returns whether a PDF document allows printing.
- [CGPDFDocumentUnlockWithPassword](<unlockwithpassword(__).md>) — Unlocks an encrypted PDF document when a valid password is supplied.

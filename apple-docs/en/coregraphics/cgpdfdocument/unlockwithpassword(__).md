---
title: 'unlockWithPassword(_:)'
framework: Core Graphics
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coregraphics/cgpdfdocument/unlockwithpassword(_:)'
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpdfdocument/unlockwithpassword(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpdfdocument/unlockwithpassword%28_%3A%29.json'
content_hash: 'sha256:27cf89fd6a188221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPDFDocument](../cgpdfdocument.md)

# unlockWithPassword(_:)

<sub>Instance Method</sub>

Unlocks an encrypted PDF document when a valid password is supplied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unlockWithPassword(_ password: UnsafePointer<CChar>) -> Bool
```

## Parameters

- `password` — A pointer to a string that contains the password.

## Return Value

A Boolean that, if [true](../../swift/true.md), indicates that the document has been successfully unlocked. If the value is [false](../../swift/false.md), the document has not been unlocked.

## Discussion

Given an encrypted PDF document and a password, this function does the following:

- Sets the lock state of the document, based on the validity of the password.
- Returns [true](../../swift/true.md) if the document is unlocked.
- Returns [false](../../swift/false.md) if the document cannot be unlocked with the specified password.

Unlocking a PDF document makes it possible to decrypt the document and perform other privileged operations. Different passwords enable different operations.

## See Also

### Working with an Encrypted PDF Document

- [CGPDFDocumentIsEncrypted](isencrypted.md) — Returns whether the specified PDF file is encrypted.
- [CGPDFDocumentAllowsCopying](allowscopying.md) — Returns whether the specified PDF document allows copying.
- [CGPDFDocumentAllowsPrinting](allowsprinting.md) — Returns whether a PDF document allows printing.
- [CGPDFDocumentIsUnlocked](isunlocked.md) — Returns whether the specified PDF document is currently unlocked.

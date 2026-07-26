---
title: PDFDocumentDidFindMatchNotification
framework: PDFKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/pdfkit/pdfdocumentdidfindmatchnotification
source_url: 'https://developer.apple.com/documentation/pdfkit/pdfdocumentdidfindmatchnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/pdfkit/pdfdocumentdidfindmatchnotification.json'
content_hash: 'sha256:96ed86193e5080a5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PDFKit](../pdfkit.md)

# PDFDocumentDidFindMatchNotification

<sub>Global Variable</sub>

A notification that a string match is found in a document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSNotificationName const PDFDocumentDidFindMatchNotification;
```

## Discussion

The notification object is the `PDFDocument` object itself. To determine the string selection found, use the `@”PDFDocumentFoundSelection”` key to obtain userinfo of type `PDFSelection *`

## See Also

### Notifications

- [PDFDocumentDidUnlockNotification](pdfdocumentdidunlocknotification.md) — A notification that a document unlocks after a [- unlockWithPassword:](<pdfdocument/unlock(withpassword_).md>) message.
- [PDFDocumentDidBeginFindNotification](pdfdocumentdidbeginfindnotification.md) — A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method begins finding.
- [PDFDocumentDidEndFindNotification](pdfdocumentdidendfindnotification.md) — A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method returns.
- [PDFDocumentDidBeginPageFindNotification](pdfdocumentdidbeginpagefindnotification.md) — A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidEndPageFindNotification](pdfdocumentdidendpagefindnotification.md) — A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidBeginWriteNotification](pdfdocumentdidbeginwritenotification.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndWriteNotification](pdfdocumentdidendwritenotification.md) — A notification that a write operation finishes working on a document.
- [PDFDocumentDidBeginPageWriteNotification](pdfdocumentdidbeginpagewritenotification.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidEndPageWriteNotification](pdfdocumentdidendpagewritenotification.md) — A notification that a write operation finishes working on a page in a document.

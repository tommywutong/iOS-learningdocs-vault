---
title: PDFDocumentDidBeginPageFindNotification
framework: PDFKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/pdfkit/pdfdocumentdidbeginpagefindnotification
source_url: 'https://developer.apple.com/documentation/pdfkit/pdfdocumentdidbeginpagefindnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/pdfkit/pdfdocumentdidbeginpagefindnotification.json'
content_hash: 'sha256:13ad83cbb5fd51c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PDFKit](../pdfkit.md)

# PDFDocumentDidBeginPageFindNotification

<sub>Global Variable</sub>

A notification that a find operation begins working on a new page of a document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSNotificationName const PDFDocumentDidBeginPageFindNotification;
```

## Discussion

You can use this notification to update a progress bar.

The notification object is the `PDFDocument` object itself. To determine the page, use the `@”PDFDocumentPageIndex”` key to obtain userinfo of type `NSNumber`.

## See Also

### Notifications

- [PDFDocumentDidUnlockNotification](pdfdocumentdidunlocknotification.md) — A notification that a document unlocks after a [- unlockWithPassword:](<pdfdocument/unlock(withpassword_).md>) message.
- [PDFDocumentDidBeginFindNotification](pdfdocumentdidbeginfindnotification.md) — A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method begins finding.
- [PDFDocumentDidEndFindNotification](pdfdocumentdidendfindnotification.md) — A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method returns.
- [PDFDocumentDidEndPageFindNotification](pdfdocumentdidendpagefindnotification.md) — A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidFindMatchNotification](pdfdocumentdidfindmatchnotification.md) — A notification that a string match is found in a document.
- [PDFDocumentDidBeginWriteNotification](pdfdocumentdidbeginwritenotification.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndWriteNotification](pdfdocumentdidendwritenotification.md) — A notification that a write operation finishes working on a document.
- [PDFDocumentDidBeginPageWriteNotification](pdfdocumentdidbeginpagewritenotification.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidEndPageWriteNotification](pdfdocumentdidendpagewritenotification.md) — A notification that a write operation finishes working on a page in a document.

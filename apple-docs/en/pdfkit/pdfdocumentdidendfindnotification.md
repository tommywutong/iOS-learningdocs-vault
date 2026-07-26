---
title: PDFDocumentDidEndFindNotification
framework: PDFKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/pdfkit/pdfdocumentdidendfindnotification
source_url: 'https://developer.apple.com/documentation/pdfkit/pdfdocumentdidendfindnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/pdfkit/pdfdocumentdidendfindnotification.json'
content_hash: 'sha256:bb0a0cee7d4e1798'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PDFKit](../pdfkit.md)

# PDFDocumentDidEndFindNotification

<sub>Global Variable</sub>

A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSNotificationName const PDFDocumentDidEndFindNotification;
```

## Discussion

The [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) method returns immediately, so this notification is posted when the “find” operation is finished.

You can use this notification to know when to close or hide a progress bar.

The notification object is the `PDFDocument` object itself.

## See Also

### Notifications

- [PDFDocumentDidUnlockNotification](pdfdocumentdidunlocknotification.md) — A notification that a document unlocks after a [- unlockWithPassword:](<pdfdocument/unlock(withpassword_).md>) message.
- [PDFDocumentDidBeginFindNotification](pdfdocumentdidbeginfindnotification.md) — A notification that the [- beginFindString:withOptions:](<pdfdocument/beginfindstring(__withoptions_).md>) or [- findString:withOptions:](<pdfdocument/findstring(__withoptions_).md>) method begins finding.
- [PDFDocumentDidBeginPageFindNotification](pdfdocumentdidbeginpagefindnotification.md) — A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidEndPageFindNotification](pdfdocumentdidendpagefindnotification.md) — A notification that a find operation finishes working on a page in a document.
- [PDFDocumentDidFindMatchNotification](pdfdocumentdidfindmatchnotification.md) — A notification that a string match is found in a document.
- [PDFDocumentDidBeginWriteNotification](pdfdocumentdidbeginwritenotification.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndWriteNotification](pdfdocumentdidendwritenotification.md) — A notification that a write operation finishes working on a document.
- [PDFDocumentDidBeginPageWriteNotification](pdfdocumentdidbeginpagewritenotification.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidEndPageWriteNotification](pdfdocumentdidendpagewritenotification.md) — A notification that a write operation finishes working on a page in a document.

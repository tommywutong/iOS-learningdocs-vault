---
title: PDFDocumentDidEndPageFind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidendpagefind
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidendpagefind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidendpagefind.json'
content_hash: 'sha256:8d1be5db40551dd3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# PDFDocumentDidEndPageFind

<sub>Type Property</sub>

A notification that a find operation finishes working on a page in a document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let PDFDocumentDidEndPageFind: NSNotification.Name
```

## Discussion

You can use this notification to update a progress bar.

The notification object is the `PDFDocument` object itself. To determine the page, use the `@”PDFDocumentPageIndex”` key to obtain userinfo of type `NSNumber`.

## See Also

### PDFKit

- [PDFDocumentDidBeginFind](pdfdocumentdidbeginfind.md) — A notification that the document began a find operation.
- [PDFDocumentDidBeginPageFind](pdfdocumentdidbeginpagefind.md) — A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidBeginPageWrite](pdfdocumentdidbeginpagewrite.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidBeginWrite](pdfdocumentdidbeginwrite.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndFind](pdfdocumentdidendfind.md) — A notification that the document finished a find operation.
- [PDFDocumentDidEndPageWrite](pdfdocumentdidendpagewrite.md) — A notification that a write operation finishes working on a page in a document.
- [PDFDocumentDidEndWrite](pdfdocumentdidendwrite.md) — A notification that a write operation finishes working on a document.
- [PDFDocumentDidFindMatch](pdfdocumentdidfindmatch.md) — A notification that a string match is found in a document.
- [PDFDocumentDidUnlock](pdfdocumentdidunlock.md) — A notification that a document unlocked.
- [PDFThumbnailViewDocumentEdited](pdfthumbnailviewdocumentedited.md)
- [PDFViewAnnotationHit](pdfviewannotationhit.md) — A notification posted when the user clicks on an annotation.
- [PDFViewAnnotationWillHit](pdfviewannotationwillhit.md) — A notification posted before the user clicks an annotation.
- [PDFViewChangedHistory](pdfviewchangedhistory.md) — A notification posted when the page history changes.
- [PDFViewCopyPermission](pdfviewcopypermission.md) — A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [PDFViewDisplayBoxChanged](pdfviewdisplayboxchanged.md) — A notification posted when the display box has changed.

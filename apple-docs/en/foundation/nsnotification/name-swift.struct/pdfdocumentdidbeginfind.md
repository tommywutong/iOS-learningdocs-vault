---
title: PDFDocumentDidBeginFind
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidbeginfind
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidbeginfind'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/pdfdocumentdidbeginfind.json'
content_hash: 'sha256:0196f567269c94d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# PDFDocumentDidBeginFind

<sub>Type Property</sub>

A notification that the document began a find operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let PDFDocumentDidBeginFind: NSNotification.Name
```

## Discussion

The document posts this notification when the [beginFindString(_:withOptions:)](<../../../pdfkit/pdfdocument/beginfindstring(__withoptions_).md>) or [findString(_:withOptions:)](<../../../pdfkit/pdfdocument/findstring(__withoptions_).md>) method begins finding.

The notification object is the `PDFDocument` object itself.

## See Also

### PDFKit

- [PDFDocumentDidBeginPageFind](pdfdocumentdidbeginpagefind.md) — A notification that a find operation begins working on a new page of a document.
- [PDFDocumentDidBeginPageWrite](pdfdocumentdidbeginpagewrite.md) — A notification that a write operation begins working on a page in a document.
- [PDFDocumentDidBeginWrite](pdfdocumentdidbeginwrite.md) — A notification that a write operation begins working on a document.
- [PDFDocumentDidEndFind](pdfdocumentdidendfind.md) — A notification that the document finished a find operation.
- [PDFDocumentDidEndPageFind](pdfdocumentdidendpagefind.md) — A notification that a find operation finishes working on a page in a document.
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

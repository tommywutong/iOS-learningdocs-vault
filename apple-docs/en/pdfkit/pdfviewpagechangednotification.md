---
title: PDFViewPageChangedNotification
framework: PDFKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 11.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/pdfkit/pdfviewpagechangednotification
source_url: 'https://developer.apple.com/documentation/pdfkit/pdfviewpagechangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/pdfkit/pdfviewpagechangednotification.json'
content_hash: 'sha256:0fde5be7d22ac4ff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PDFKit](../pdfkit.md)

# PDFViewPageChangedNotification

<sub>Global Variable</sub>

A notification posted when a new page becomes the current page.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern NSNotificationName const PDFViewPageChangedNotification;
```

## Discussion

The notification object is the `PDFView` object itself.

## See Also

### Notifications

- [PDFViewChangedHistoryNotification](pdfviewchangedhistorynotification.md) — A notification posted when the page history changes.
- [PDFViewDocumentChangedNotification](pdfviewdocumentchangednotification.md) — A notification posted when a new document is associated with the view.
- [PDFViewScaleChangedNotification](pdfviewscalechangednotification.md) — A notification posted when the scale factor changes.
- [PDFViewAnnotationHitNotification](pdfviewannotationhitnotification.md) — A notification posted when the user clicks on an annotation.
- [PDFViewCopyPermissionNotification](pdfviewcopypermissionnotification.md) — A notification posted when the user attempts to copy to the pasteboard without the appropriate permissions.
- [PDFViewPrintPermissionNotification](pdfviewprintpermissionnotification.md) — A notification posted when the user attempts to print without the appropriate permissions.
- [PDFViewAnnotationWillHitNotification](pdfviewannotationwillhitnotification.md) — A notification posted before the user clicks an annotation.
- [PDFViewSelectionChangedNotification](pdfviewselectionchangednotification.md) — A notification posted when the current selection has changed.
- [PDFViewDisplayModeChangedNotification](pdfviewdisplaymodechangednotification.md) — A notification posted when the display mode has changed.
- [PDFViewDisplayBoxChangedNotification](pdfviewdisplayboxchangednotification.md) — A notification posted when the display box has changed.
- [PDFViewVisiblePagesChangedNotification](pdfviewvisiblepageschangednotification.md) — A notification posted when the visible pages have changed.

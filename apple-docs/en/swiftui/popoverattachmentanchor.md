---
title: PopoverAttachmentAnchor
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/popoverattachmentanchor
source_url: 'https://developer.apple.com/documentation/swiftui/popoverattachmentanchor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/popoverattachmentanchor.json'
content_hash: 'sha256:4e64bd58dc337c55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PopoverAttachmentAnchor

<sub>Enumeration</sub>

An attachment anchor for a popover.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum PopoverAttachmentAnchor
```

## Topics

### Getting attachment anchors

- [PopoverAttachmentAnchor.point(_:)](<popoverattachmentanchor/point(__).md>) — The anchor point for the popover expressed as a unit point  that describes possible alignments relative to a SwiftUI view.
- [PopoverAttachmentAnchor.rect(_:)](<popoverattachmentanchor/rect(__).md>) — The anchor point for the popover relative to the source’s frame.

## See Also

### Showing a sheet, cover, or popover

- [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) — Presents a sheet when a binding to a Boolean value that you provide is true.
- [sheet(item:onDismiss:content:)](<view/sheet(item_ondismiss_content_).md>) — Presents a sheet using the given item as a data source for the sheet’s content.
- [fullScreenCover(isPresented:onDismiss:content:)](<view/fullscreencover(ispresented_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [fullScreenCover(item:onDismiss:content:)](<view/fullscreencover(item_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [popover(item:attachmentAnchor:arrowEdge:content:)](<view/popover(item_attachmentanchor_arrowedge_content_).md>) — Presents a popover using the given item as a data source for the popover’s content.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<view/popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.

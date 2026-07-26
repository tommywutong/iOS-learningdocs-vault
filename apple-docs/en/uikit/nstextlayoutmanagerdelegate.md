---
title: NSTextLayoutManagerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanagerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate.json'
content_hash: 'sha256:e904edb9fbafc5ad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextLayoutManagerDelegate

<sub>Protocol</sub>

Optional methods that delegates implement to respond to layout changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextLayoutManagerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to layout changes

- [- textLayoutManager:renderingAttributesForLink:atLocation:defaultAttributes:](<nstextlayoutmanagerdelegate/textlayoutmanager(__renderingattributesforlink_at_defaultattributes_).md>) — The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [- textLayoutManager:shouldBreakLineBeforeLocation:hyphenating:](<nstextlayoutmanagerdelegate/textlayoutmanager(__shouldbreaklinebefore_hyphenating_).md>) — The method the framework calls to determine the soft line break point.
- [- textLayoutManager:textLayoutFragmentForLocation:inTextElement:](<nstextlayoutmanagerdelegate/textlayoutmanager(__textlayoutfragmentfor_in_).md>) — The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

### Reusing text attachment view providers

- [- textLayoutManager:cacheTextAttachmentViewProvider:forTextAttachment:](<nstextlayoutmanagerdelegate/textlayoutmanager(__cachetextattachmentviewprovider_for_).md>) — Notifies the delegate that a view provider associated with a text attachment is about to be invalidated. _(beta)_
- [- textLayoutManager:retrieveCachedTextAttachmentViewProviderForTextAttachment:](<nstextlayoutmanagerdelegate/textlayoutmanager(__retrievecachedtextattachmentviewproviderfor_).md>) — Returns a cached `NSTextAttachmentViewProvider` to be associated with a particular attachment. _(beta)_

## See Also

### Managing the layout process

- [delegate](nstextlayoutmanager/delegate.md) — The delegate for the text layout manager object.

---
title: NSTextElementProvider
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextelementprovider
source_url: 'https://developer.apple.com/documentation/uikit/nstextelementprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelementprovider.json'
content_hash: 'sha256:1cad26d43ebab468'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextElementProvider

<sub>Protocol</sub>

A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextElementProvider : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextContentManager](nstextcontentmanager.md), [NSTextContentStorage](nstextcontentstorage.md)

## Topics

### Accessing the range of the text element

- [documentRange](nstextelementprovider/documentrange.md) — Describes the starting and ending locations for the document.

### Accessing and updating the text

- [- enumerateTextElementsFromLocation:options:usingBlock:](<nstextelementprovider/enumeratetextelements(from_options_using_).md>) — Enumerates text elements starting at the text location you provide.
- [EnumerationOptions](nstextlayoutfragment/enumerationoptions.md) — Values that describe options for enumerating text layout fragments.
- [- locationFromLocation:withOffset:](<nstextelementprovider/location(__offsetby_).md>) — Returns a new location from location with offset you provide.
- [- replaceContentsInRange:withTextElements:](<nstextelementprovider/replacecontents(in_with_).md>) — Replaces the characters specified by range with the text elements you provide.

### Adjusting the range of the text element

- [- adjustedRangeFromRange:forEditingTextSelection:](<nstextelementprovider/adjustedrange(from_foreditingtextselection_).md>) — A method you implement if the location backing store requires manual adjustment after editing.
- [- offsetFromLocation:toLocation:](<nstextelementprovider/offset(from_to_).md>) — Returns the offset between the two specified locations.

### Controlling synchronization with the backing store

- [- synchronizeToBackingStore:](<nstextelementprovider/synchronizetobackingstore(__).md>) — Synchronizes changes to the backing store.

## See Also

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [NSTextParagraph](nstextparagraph.md) — A class that represents a single paragraph backed by an attributed string as the contents.
- [NSTextListElement](nstextlistelement.md) — A class that represents a text list node.
- [NSTextElement](nstextelement.md) — An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.

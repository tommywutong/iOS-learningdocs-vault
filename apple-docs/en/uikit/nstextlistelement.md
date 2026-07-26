---
title: NSTextListElement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlistelement
source_url: 'https://developer.apple.com/documentation/uikit/nstextlistelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlistelement.json'
content_hash: 'sha256:843cf3a652e183a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextListElement

<sub>Class</sub>

A class that represents a text list node.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextListElement
```

## Relationships

- **Inherits From**: [NSTextParagraph](nstextparagraph.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Create a text list element

- [+ textListElementWithChildElements:textList:nestingLevel:](<nstextlistelement/init(children_textlist_nestinglevel_).md>) — Creates a text list element with the list elements and nesting level you provide.
- [+ textListElementWithContents:markerAttributes:textList:childElements:](<nstextlistelement/init(contents_markerattributes_textlist_children_).md>) — Creates a text list element with the list elements, nesting level, and marker attributes you provide.
- [- initWithParentElement:textList:contents:markerAttributes:childElements:](<nstextlistelement/init(parent_textlist_contents_markerattributes_children_).md>) — Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

### Accessing the text elements

- [textList](nstextlistelement/textlist.md) — The value that represents the text list.
- [parentElement](nstextlistelement/parent.md) — A text list element that refers to the enclosing text list element.
- [childElements](nstextlistelement/childelements.md) — An array that contains child text elements.

### Accessing the text list’s attributes

- [markerAttributes](nstextlistelement/markerattributes.md) — A dictionary of attributed string keys and IDs that represent the list’s marker attributes.

### Accessing the formatted string data

- [attributedString](nstextlistelement/attributedstring.md) — An attributed string that represents the string the framework displays for this element taking into account markers and the indentation level of the list element.
- [contents](nstextlistelement/contents.md) — The text list element contents without markers and formatting.

### Initializers

- [init(childElements:textList:nestingLevel:)](<nstextlistelement/init(childelements_textlist_nestinglevel_).md>)
- [init(contents:markerAttributes:textList:childElements:)](<nstextlistelement/init(contents_markerattributes_textlist_childelements_).md>)
- [init(parentElement:textList:contents:markerAttributes:childElements:)](<nstextlistelement/init(parentelement_textlist_contents_markerattributes_childelements_).md>)

## See Also

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [NSTextParagraph](nstextparagraph.md) — A class that represents a single paragraph backed by an attributed string as the contents.
- [NSTextElement](nstextelement.md) — An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [NSTextElementProvider](nstextelementprovider.md) — A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

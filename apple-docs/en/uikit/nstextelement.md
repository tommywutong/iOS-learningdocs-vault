---
title: NSTextElement
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextelement
source_url: 'https://developer.apple.com/documentation/uikit/nstextelement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextelement.json'
content_hash: 'sha256:8e9713c45838c24e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextElement

<sub>Class</sub>

An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextElement
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSTextParagraph](nstextparagraph.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a text element

- [- initWithTextContentManager:](<nstextelement/init(textcontentmanager_).md>) — Creates a new text element with the content manager you provide.

### Accessing the content manager

- [textContentManager](nstextelement/textcontentmanager.md) — The value that represents the current content manager.

### Accessing the text element range

- [elementRange](nstextelement/elementrange.md) — A range value that represents the range of the element inside the document.

### Accessing text elements

- [isRepresentedElement](nstextelement/isrepresentedelement.md) — A Boolean value that indicates whether this element is in the text layout.
- [parentElement](nstextelement/parent.md) — A value that represents the parent element if this text element is a child of an enclosing element.
- [childElements](nstextelement/childelements.md) — An array of zero or more child text elements.

## See Also

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [NSTextParagraph](nstextparagraph.md) — A class that represents a single paragraph backed by an attributed string as the contents.
- [NSTextListElement](nstextlistelement.md) — A class that represents a text list node.
- [NSTextElementProvider](nstextelementprovider.md) — A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

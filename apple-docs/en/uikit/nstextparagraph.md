---
title: NSTextParagraph
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextparagraph
source_url: 'https://developer.apple.com/documentation/uikit/nstextparagraph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextparagraph.json'
content_hash: 'sha256:cfde7f21bb59c77a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextParagraph

<sub>Class</sub>

A class that represents a single paragraph backed by an attributed string as the contents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class NSTextParagraph
```

## Relationships

- **Inherits From**: [NSTextElement](nstextelement.md)

- **Inherited By**: [NSTextListElement](nstextlistelement.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a paragraph

- [- initWithAttributedString:](<nstextparagraph/init(attributedstring_).md>) — Creates a new paragraph with the attributed string you provide.

### Getting paragraph characteristics

- [attributedString](nstextparagraph/attributedstring.md) — Returns the source attributed string.
- [paragraphContentRange](nstextparagraph/paragraphcontentrange.md) — Returns the range of the paragraph in the containing text’s attributed string.
- [paragraphSeparatorRange](nstextparagraph/paragraphseparatorrange.md) — Returns the range of the paragraph separator in the containing text’s attributed string.

## See Also

### Content elements

- [Enriching your text in text views](enriching-your-text-in-text-views.md) — Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [NSTextListElement](nstextlistelement.md) — A class that represents a text list node.
- [NSTextElement](nstextelement.md) — An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [NSTextElementProvider](nstextelementprovider.md) — A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.

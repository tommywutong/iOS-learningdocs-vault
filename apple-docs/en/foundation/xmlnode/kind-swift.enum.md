---
title: XMLNode.Kind
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/xmlnode/kind-swift.enum
source_url: 'https://developer.apple.com/documentation/foundation/xmlnode/kind-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmlnode/kind-swift.enum.json'
content_hash: 'sha256:8ad4d423923ec698'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLNode](../xmlnode.md)

# XMLNode.Kind

<sub>Enumeration</sub>

`NSXMLNode` declares the following constants of type NSXMLNodeKind for specifying a node’s kind in the initializer methods [- initWithKind:](<init(kind_).md>) and [- initWithKind:options:](<init(kind_options_).md>):

<sub>Mac Catalyst, macOS</sub>

```swift
enum Kind
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSXMLInvalidKind](kind-swift.enum/invalid.md) — Indicates a node object created without a valid kind being specified (as returned by the [kind](kind-swift.property.md) method).
- [NSXMLDocumentKind](kind-swift.enum/document.md) — Specifies a document node.
- [NSXMLElementKind](kind-swift.enum/element.md) — Specifies an element node.
- [NSXMLAttributeKind](kind-swift.enum/attribute.md) — Specifies an attribute node
- [NSXMLNamespaceKind](kind-swift.enum/namespace.md) — Specifies a namespace node.
- [NSXMLProcessingInstructionKind](kind-swift.enum/processinginstruction.md) — Specifies a processing-instruction node.
- [NSXMLCommentKind](kind-swift.enum/comment.md) — Specifies a comment node.
- [NSXMLTextKind](kind-swift.enum/text.md) — Specifies a text node.
- [NSXMLDTDKind](kind-swift.enum/dtdkind.md) — Specifies a document-type declaration (DTD) node.
- [NSXMLEntityDeclarationKind](kind-swift.enum/entitydeclaration.md) — Specifies an entity-declaration node.
- [NSXMLAttributeDeclarationKind](kind-swift.enum/attributedeclaration.md) — Specifies an attribute-list declaration node.
- [NSXMLElementDeclarationKind](kind-swift.enum/elementdeclaration.md) — Specifies an element declaration node.
- [NSXMLNotationDeclarationKind](kind-swift.enum/notationdeclaration.md) — Specifies a notation declaration node.

### Initializers

- [init(rawValue:)](<kind-swift.enum/init(rawvalue_).md>)

## See Also

### Constants

- [Options](options.md) — These constants are input and output options for all `NSXMLNode` objects (unless otherwise indicated), including [XMLDocument](../xmldocument.md) objects. You can specify these options in the `NSXMLNode` methods [- initWithKind:options:](<init(kind_options_).md>) and [- XMLStringWithOptions:](<xmlstring(options_).md>).

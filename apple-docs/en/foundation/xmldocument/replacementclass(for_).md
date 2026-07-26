---
title: 'replacementClass(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/replacementclass(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/replacementclass(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/replacementclass%28for%3A%29.json'
content_hash: 'sha256:8be2bfea8f18eb61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# replacementClass(for:)

<sub>Type Method</sub>

Overridden by subclasses to substitute a custom class for an NSXML class that the parser uses to create node instances.

<sub>Mac Catalyst, macOS</sub>

```swift
class func replacementClass(for cls: AnyClass) -> AnyClass
```

## Parameters

- `cls` — A `Class` object identifying an NSXML class that is to be replaced by your custom class.

## Return Value

The substituted class.

## Discussion

For example, if you have a custom subclass of [XMLElement](../xmlelement.md) that you want to be used in place of `NSXMLElement`, you would make the following override:

```objc
+ (Class)replacementClassForClass:(Class)currentClass {
    if ( currentClass == [NSXMLElement class] ) {
        return [MyCustomElementClass class];
    }
}
```

This method is invoked before a document is parsed. The substituted class must be a subclass of [XMLNode](../xmlnode.md), `NSXMLDocument`, `NSXMLElement`, [XMLDTD](../xmldtd.md), or [XMLDTDNode](../xmldtdnode.md).

## See Also

### Related Documentation

- [- setRootElement:](<setrootelement(__).md>) — Set the root element of the receiver.

### Initializing NSXMLDocument Objects

- [- initWithContentsOfURL:options:error:](<init(contentsof_options_).md>) — Initializes and returns an NSXMLDocument object created from the XML or HTML contents of a URL-referenced source
- [- initWithData:options:error:](<init(data_options_).md>) — Initializes and returns an `NSXMLDocument` object created from an [NSData](../nsdata.md) object.
- [- initWithRootElement:](<init(rootelement_).md>) — Returns an `NSXMLDocument` object initialized with a single child, the root element.
- [- initWithXMLString:options:error:](<init(xmlstring_options_)-65m2r.md>) — Initializes and returns an `NSXMLDocument` object created from a string containing XML markup text.

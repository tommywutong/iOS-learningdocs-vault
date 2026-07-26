---
title: 'CTLineCreateWithAttributedString(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/ctlinecreatewithattributedstring(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/ctlinecreatewithattributedstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctlinecreatewithattributedstring%28_%3A%29.json'
content_hash: 'sha256:b5fae9984986071b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTLineCreateWithAttributedString(_:)

<sub>Function</sub>

Creates a single immutable line object from an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTLineCreateWithAttributedString(_ attrString: CFAttributedString) -> CTLine
```

## Parameters

- `attrString` — The string that creates the line.

## Return Value

A reference to a [CTLine](ctline.md) object.

## Discussion

This function allows clients to create a line without creating a [CTTypesetter](cttypesetter.md) object. The framework provides a typesetter for single-line typesetting under the hood. Simple elements that don’t require line breaks, such as text labels, can use this API.

## See Also

### Related Documentation

- [CTTypesetterCreateWithAttributedString](<cttypesettercreatewithattributedstring(__).md>) — Creates an immutable typesetter object using an attributed string.
- [CTTypesetterCreateWithAttributedStringAndOptions](<cttypesettercreatewithattributedstringandoptions(____).md>) — Creates an immutable typesetter object using an attributed string and a dictionary of options.
- [CTTypesetterCreateLine](<cttypesettercreateline(____).md>) — Creates an immutable line from the typesetter.

### Creating Lines

- [CTLineCreateTruncatedLine](<ctlinecreatetruncatedline(________).md>) — Creates a truncated line from an existing line.
- [CTLineCreateJustifiedLine](<ctlinecreatejustifiedline(______).md>) — Creates a justified line from an existing line.

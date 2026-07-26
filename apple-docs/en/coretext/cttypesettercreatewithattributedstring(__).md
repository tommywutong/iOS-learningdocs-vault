---
title: 'CTTypesetterCreateWithAttributedString(_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttypesettercreatewithattributedstring(_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttypesettercreatewithattributedstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesettercreatewithattributedstring%28_%3A%29.json'
content_hash: 'sha256:5680e5f35a0c5292'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetterCreateWithAttributedString(_:)

<sub>Function</sub>

Creates an immutable typesetter object using an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTypesetterCreateWithAttributedString(_ string: CFAttributedString) -> CTTypesetter
```

## Parameters

- `string` — The attributed string to typeset. This parameter must be filled in with a valid CFAttributedString object.

## Return Value

A reference to a CTTypesetter object if the call was successful; otherwise, `NULL`.

## Discussion

The resultant typesetter can be used to create lines, perform line breaking, and do other contextual analysis based on the characters in the string.

## See Also

### Creating a Typesetter

- [CTTypesetterCreateWithAttributedStringAndOptions](<cttypesettercreatewithattributedstringandoptions(____).md>) — Creates an immutable typesetter object using an attributed string and a dictionary of options.

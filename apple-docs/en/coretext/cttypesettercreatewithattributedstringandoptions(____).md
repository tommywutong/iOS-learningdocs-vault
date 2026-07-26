---
title: 'CTTypesetterCreateWithAttributedStringAndOptions(_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttypesettercreatewithattributedstringandoptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttypesettercreatewithattributedstringandoptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesettercreatewithattributedstringandoptions%28_%3A_%3A%29.json'
content_hash: 'sha256:47435dc8f5926cc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetterCreateWithAttributedStringAndOptions(_:_:)

<sub>Function</sub>

Creates an immutable typesetter object using an attributed string and a dictionary of options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTypesetterCreateWithAttributedStringAndOptions(_ string: CFAttributedString, _ options: CFDictionary?) -> CTTypesetter?
```

## Parameters

- `string` — The attributed string to typeset. This parameter must be a valid `CFAttributedString` object.

- `options` — A dictionary of typesetter options, or `NULL` if there are none.

## Return Value

A reference to a typesetter object if the call is successful; otherwise, `NULL`.

## Discussion

Use the typesetter to create lines, perform line breaking, and do other contextual analysis according to the characters in the string.

> [!important] Important
> By default, this function returns `NULL` if the string requires unreasonable effort to typeset. To create a typesetter that always typesets the text, regardless of the amount of effort, set the [kCTTypesetterOptionAllowUnboundedLayout](kcttypesetteroptionallowunboundedlayout.md) option to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md).

## See Also

### Creating a Typesetter

- [CTTypesetterCreateWithAttributedString](<cttypesettercreatewithattributedstring(__).md>) — Creates an immutable typesetter object using an attributed string.

---
title: 'init(children:textList:nestingLevel:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlistelement/init(children:textlist:nestinglevel:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlistelement/init(children:textlist:nestinglevel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlistelement/init%28children%3Atextlist%3Anestinglevel%3A%29.json'
content_hash: 'sha256:bfc4477e024cff8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextListElement](../nstextlistelement.md)

# init(children:textList:nestingLevel:)

<sub>Initializer</sub>

Creates a text list element with the list elements and nesting level you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)
```

## Parameters

- `children` — An array of [NSTextListElement](../nstextlistelement.md) elements.

- `textList` — The [NSTextList](../nstextlist.md) to add elements to.

- `nestingLevel` — An integer value that describes the level of nesting of these elements.

## See Also

### Create a text list element

- [+ textListElementWithContents:markerAttributes:textList:childElements:](<init(contents_markerattributes_textlist_children_).md>) — Creates a text list element with the list elements, nesting level, and marker attributes you provide.
- [- initWithParentElement:textList:contents:markerAttributes:childElements:](<init(parent_textlist_contents_markerattributes_children_).md>) — Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

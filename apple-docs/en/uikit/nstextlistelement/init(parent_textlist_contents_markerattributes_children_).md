---
title: 'init(parent:textList:contents:markerAttributes:children:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlistelement/init(parent:textlist:contents:markerattributes:children:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlistelement/init(parent:textlist:contents:markerattributes:children:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlistelement/init%28parent%3Atextlist%3Acontents%3Amarkerattributes%3Achildren%3A%29.json'
content_hash: 'sha256:a690c8d8ab8eabbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextListElement](../nstextlistelement.md)

# init(parent:textList:contents:markerAttributes:children:)

<sub>Initializer</sub>

Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]? = nil, children: [NSTextListElement]?)
```

## Parameters

- `parent` — The parent `NSTextListElement` of this element, if any.

- `textList` — The [NSTextList](../nstextlist.md) to add elements to.

- `contents` — An [NSAttributedString](../../foundation/nsattributedstring.md) that contains the contents of the text list element.

- `markerAttributes` — A dictionary of [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) keys and IDs that describe the marker attributes.

- `children` — An array of [NSTextListElement](../nstextlistelement.md) elements.

## See Also

### Create a text list element

- [+ textListElementWithChildElements:textList:nestingLevel:](<init(children_textlist_nestinglevel_).md>) — Creates a text list element with the list elements and nesting level you provide.
- [+ textListElementWithContents:markerAttributes:textList:childElements:](<init(contents_markerattributes_textlist_children_).md>) — Creates a text list element with the list elements, nesting level, and marker attributes you provide.

---
title: 'init(textAlignment:location:options:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstexttab/init(textalignment:location:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstexttab/init(textalignment:location:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttab/init%28textalignment%3Alocation%3Aoptions%3A%29.json'
content_hash: 'sha256:cd2f2b4f04ccda51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextTab](../nstexttab.md)

# init(textAlignment:location:options:)

<sub>Initializer</sub>

Initializes a text tab with the specified text alignment, location, and options.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(textAlignment alignment: NSTextAlignment, location loc: CGFloat, options: [NSTextTab.OptionKey : Any] = [:])
```

## Parameters

- `alignment` — The alignment of the text.

- `loc` — The position of the text tab on the ruler, relative to the back margin.

- `options` — Options to apply to the text tab.

## Return Value

An initialized text tab.

## Discussion

The text alignment is used to determine the position of text inside the tab column. See [NSParagraphStyle.TextTabType](../../appkit/nsparagraphstyle/texttabtype.md) for a mapping between alignments and tab stop types

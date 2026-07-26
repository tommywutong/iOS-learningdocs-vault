---
title: 'textLayoutManager(_:textLayoutFragmentFor:in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:textlayoutfragmentfor:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager%28_%3Atextlayoutfragmentfor%3Ain%3A%29.json'
content_hash: 'sha256:fc4f477e605391ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)

# textLayoutManager(_:textLayoutFragmentFor:in:)

<sub>Instance Method</sub>

The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, textLayoutFragmentFor location: any NSTextLocation, in textElement: NSTextElement) -> NSTextLayoutFragment
```

## Parameters

- `textLayoutManager` — The text layout manager.

- `location` — The [NSTextLocation](../nstextlocation.md) of the link in the text element.

- `textElement` — The [NSTextElement](../nstextelement.md) that the method could return a custom [NSTextLayoutFragment](../nstextlayoutfragment.md) from.

## Return Value

An [NSTextLayoutFragment](../nstextlayoutfragment.md).

## Discussion

Use this to provide an [NSTextLayoutFragment](../nstextlayoutfragment.md) specialized for an [NSTextElement](../nstextelement.md) subclass targeted for the rendering surface.

## See Also

### Responding to layout changes

- [- textLayoutManager:renderingAttributesForLink:atLocation:defaultAttributes:](<textlayoutmanager(__renderingattributesforlink_at_defaultattributes_).md>) — The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [- textLayoutManager:shouldBreakLineBeforeLocation:hyphenating:](<textlayoutmanager(__shouldbreaklinebefore_hyphenating_).md>) — The method the framework calls to determine the soft line break point.

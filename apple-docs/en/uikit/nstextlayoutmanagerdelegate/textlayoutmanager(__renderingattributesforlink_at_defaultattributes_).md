---
title: 'textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:renderingattributesforlink:at:defaultattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager%28_%3Arenderingattributesforlink%3Aat%3Adefaultattributes%3A%29.json'
content_hash: 'sha256:b968b4fa8a49c427'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)

# textLayoutManager(_:renderingAttributesForLink:at:defaultAttributes:)

<sub>Instance Method</sub>

The method the framework calls to return a dictionary of attributes for rendering a link attribute name.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, renderingAttributesForLink link: Any, at location: any NSTextLocation, defaultAttributes renderingAttributes: [NSAttributedString.Key : Any] = [:]) -> [NSAttributedString.Key : Any]?
```

## Parameters

- `textLayoutManager` — The `NSTextLayoutManager`.

- `link` — The link.

- `location` — The [NSTextLocation](../nstextlocation.md) of the link.

- `renderingAttributes` — A dictionary of attributes whose keys are [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) values.

## Return Value

A dictionary of  attributes.

## See Also

### Responding to layout changes

- [- textLayoutManager:shouldBreakLineBeforeLocation:hyphenating:](<textlayoutmanager(__shouldbreaklinebefore_hyphenating_).md>) — The method the framework calls to determine the soft line break point.
- [- textLayoutManager:textLayoutFragmentForLocation:inTextElement:](<textlayoutmanager(__textlayoutfragmentfor_in_).md>) — The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

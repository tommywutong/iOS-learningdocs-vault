---
title: 'textLayoutManager(_:shouldBreakLineBefore:hyphenating:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager(_:shouldbreaklinebefore:hyphenating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanagerdelegate/textlayoutmanager%28_%3Ashouldbreaklinebefore%3Ahyphenating%3A%29.json'
content_hash: 'sha256:cd83b356458fbd20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManagerDelegate](../nstextlayoutmanagerdelegate.md)

# textLayoutManager(_:shouldBreakLineBefore:hyphenating:)

<sub>Instance Method</sub>

The method the framework calls to determine the soft line break point.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textLayoutManager(_ textLayoutManager: NSTextLayoutManager, shouldBreakLineBefore location: any NSTextLocation, hyphenating: Bool) -> Bool
```

## Parameters

- `textLayoutManager` — The text layout manager.

- `location` — The location of the proposed line break.

- `hyphenating` — A Boolean value that indicates the current hyphenation mode.

## Return Value

A Boolean value that indicates if the framework should break the line at the current location.

## Discussion

When `hyphenating` is `false`, `NSTextLayoutManager` tries to find the next line break opportunity before `location`. When `hyphenating` is `true`, it’s an auto-hyphenation point.

## See Also

### Responding to layout changes

- [- textLayoutManager:renderingAttributesForLink:atLocation:defaultAttributes:](<textlayoutmanager(__renderingattributesforlink_at_defaultattributes_).md>) — The method the framework calls to return a dictionary of attributes for rendering a link attribute name.
- [- textLayoutManager:textLayoutFragmentForLocation:inTextElement:](<textlayoutmanager(__textlayoutfragmentfor_in_).md>) — The method the framework calls to give the delegate an opportunity to return a custom text layout fragment.

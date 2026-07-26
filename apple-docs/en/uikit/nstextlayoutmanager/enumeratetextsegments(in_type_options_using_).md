---
title: 'enumerateTextSegments(in:type:options:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/enumeratetextsegments(in:type:options:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/enumeratetextsegments(in:type:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/enumeratetextsegments%28in%3Atype%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:815d30897ba1a919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# enumerateTextSegments(in:type:options:using:)

<sub>Instance Method</sub>

Enumerates text segments of a specific type and in the text range you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateTextSegments(in textRange: NSTextRange, type: NSTextLayoutManager.SegmentType, options: NSTextLayoutManager.SegmentOptions = [], using block: (NSTextRange?, CGRect, CGFloat, NSTextContainer) -> Bool)
```

## Parameters

- `textRange` — The range as an [NSTextRange](../nstextrange.md).

- `type` — One of the available [SegmentType](segmenttype.md) values.

- `options` — One or more of the [SegmentOptions](segmentoptions.md) options.

- `block` — A closure you provide to determine if the enumeration finishes early.

## Discussion

A text segment is a logically and visually contiguous portion of the text content inside a line fragment that you specify with a single text range. The framework enumerates the segments visually from left to right. Returning `false` breaks out of the enumeration.

## See Also

### Accessing the text storage

- [textContentManager](textcontentmanager.md) — Returns the text content manager associated with this text layout manager.
- [textContainer](textcontainer.md) — The text container object that provides geometric information for the layout destination.
- [textSelectionNavigation](textselectionnavigation.md) — Returns a text selection manager configured to have the text layout manager as its data source.
- [textSelections](textselections.md) — An array of text selections associated by the text layout manager.
- [usageBoundsForTextContainer](usageboundsfortextcontainer.md) — Returns the usage bounds for the text container.
- [- replaceTextContentManager:](<replace(__).md>) — Replaces the current text content manager with a new one you provide.
- [- replaceContentsInRange:withAttributedString:](<replacecontents(in_with_)-2elb.md>) — Replaces content at the location you specify with an attributed string you provide.
- [- replaceContentsInRange:withTextElements:](<replacecontents(in_with_)-80j0b.md>) — Replaces content at the location you specify with the text elements string you provide.

---
title: 'replaceContents(in:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/replacecontents(in:with:)-2elb'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/replacecontents(in:with:)-2elb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/replacecontents%28in%3Awith%3A%29-2elb.json'
content_hash: 'sha256:3b6d456c62a1a604'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# replaceContents(in:with:)

<sub>Instance Method</sub>

Replaces content at the location you specify with an attributed string you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replaceContents(in range: NSTextRange, with attributedString: NSAttributedString)
```

## Parameters

- `range` — The range of the content to replace.

- `attributedString` — An attribued string to replace the content at `range`.

## See Also

### Accessing the text storage

- [textContentManager](textcontentmanager.md) — Returns the text content manager associated with this text layout manager.
- [textContainer](textcontainer.md) — The text container object that provides geometric information for the layout destination.
- [textSelectionNavigation](textselectionnavigation.md) — Returns a text selection manager configured to have the text layout manager as its data source.
- [textSelections](textselections.md) — An array of text selections associated by the text layout manager.
- [usageBoundsForTextContainer](usageboundsfortextcontainer.md) — Returns the usage bounds for the text container.
- [- enumerateTextSegmentsInRange:type:options:usingBlock:](<enumeratetextsegments(in_type_options_using_).md>) — Enumerates text segments of a specific type and in the text range you provide.
- [- replaceTextContentManager:](<replace(__).md>) — Replaces the current text content manager with a new one you provide.
- [- replaceContentsInRange:withTextElements:](<replacecontents(in_with_)-80j0b.md>) — Replaces content at the location you specify with the text elements string you provide.

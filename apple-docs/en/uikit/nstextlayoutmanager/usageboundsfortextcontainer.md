---
title: usageBoundsForTextContainer
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/usageboundsfortextcontainer
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/usageboundsfortextcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/usageboundsfortextcontainer.json'
content_hash: 'sha256:b8611d34d44f9401'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# usageBoundsForTextContainer

<sub>Instance Property</sub>

Returns the usage bounds for the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var usageBoundsForTextContainer: CGRect { get }
```

## Discussion

Views can observe this property to trigger a resize operation. For example, `UIView or NSView` call [- setNeedsUpdateConstraints](<../uiview/setneedsupdateconstraints().md>) when the usage bounds changes. This property is KVO-compliant.

## See Also

### Accessing the text storage

- [textContentManager](textcontentmanager.md) — Returns the text content manager associated with this text layout manager.
- [textContainer](textcontainer.md) — The text container object that provides geometric information for the layout destination.
- [textSelectionNavigation](textselectionnavigation.md) — Returns a text selection manager configured to have the text layout manager as its data source.
- [textSelections](textselections.md) — An array of text selections associated by the text layout manager.
- [- enumerateTextSegmentsInRange:type:options:usingBlock:](<enumeratetextsegments(in_type_options_using_).md>) — Enumerates text segments of a specific type and in the text range you provide.
- [- replaceTextContentManager:](<replace(__).md>) — Replaces the current text content manager with a new one you provide.
- [- replaceContentsInRange:withAttributedString:](<replacecontents(in_with_)-2elb.md>) — Replaces content at the location you specify with an attributed string you provide.
- [- replaceContentsInRange:withTextElements:](<replacecontents(in_with_)-80j0b.md>) — Replaces content at the location you specify with the text elements string you provide.

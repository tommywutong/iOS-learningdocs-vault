---
title: linkRenderingAttributes
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextlayoutmanager/linkrenderingattributes
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/linkrenderingattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/linkrenderingattributes.json'
content_hash: 'sha256:500651b0d61d8d3d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# linkRenderingAttributes

<sub>Type Property</sub>

Returns the default set of attributes for rendering a link.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var linkRenderingAttributes: [NSAttributedString.Key : Any] { get }
```

## Discussion

The base [NSTextLayoutManager](../nstextlayoutmanager.md) class returns with [NSUnderlineStyleSingle](../nsunderlinestyle/single.md) for [underlineStyle](../../foundation/nsattributedstring/key/underlinestyle.md) in Swift or [NSUnderlineStyleAttributeName](../nsunderlinestyleattributename.md) in Objective-C, and the platform link color for [foregroundColor](../../foundation/nsattributedstring/key/foregroundcolor.md) in Swift or [NSForegroundColorAttributeName](../nsforegroundcolorattributename.md) in Objective-C. The platform color for macOS is `linkColor`. Other platforms uses `blueColor`.

## See Also

### Adjusting rendering

- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

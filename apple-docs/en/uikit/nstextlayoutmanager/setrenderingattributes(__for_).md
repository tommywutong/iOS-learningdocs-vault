---
title: 'setRenderingAttributes(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/setrenderingattributes(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/setrenderingattributes(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/setrenderingattributes%28_%3Afor%3A%29.json'
content_hash: 'sha256:69ba47227d2936e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# setRenderingAttributes(_:for:)

<sub>Instance Method</sub>

Sets the rendering attributes for the range you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setRenderingAttributes(_ renderingAttributes: [NSAttributedString.Key : Any], for textRange: NSTextRange)
```

## Parameters

- `renderingAttributes` — A dictionary of rendering attributes.

- `textRange` — The text range over which to apply `renderingAttributes`.

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.

---
title: 'invalidateRenderingAttributes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/invalidaterenderingattributes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/invalidaterenderingattributes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/invalidaterenderingattributes%28for%3A%29.json'
content_hash: 'sha256:da2eaad34263ce64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# invalidateRenderingAttributes(for:)

<sub>Instance Method</sub>

Invalidates the rendering attributes of the specified text range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func invalidateRenderingAttributes(for textRange: NSTextRange)
```

## Parameters

- `textRange` — The range of the text to invalidate.

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

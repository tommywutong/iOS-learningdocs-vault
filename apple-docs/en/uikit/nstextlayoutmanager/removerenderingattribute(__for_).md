---
title: 'removeRenderingAttribute(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/removerenderingattribute(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/removerenderingattribute(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/removerenderingattribute%28_%3Afor%3A%29.json'
content_hash: 'sha256:7e70f14248ad36e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# removeRenderingAttribute(_:for:)

<sub>Instance Method</sub>

Removes the rendering attribute from the specified text range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeRenderingAttribute(_ renderingAttribute: NSAttributedString.Key, for textRange: NSTextRange)
```

## Parameters

- `renderingAttribute` — The [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) attribute to remove

- `textRange` — The range over which to remove the rendering attribute.

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

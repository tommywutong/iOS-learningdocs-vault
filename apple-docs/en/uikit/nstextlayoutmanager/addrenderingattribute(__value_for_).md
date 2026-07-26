---
title: 'addRenderingAttribute(_:value:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/addrenderingattribute(_:value:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/addrenderingattribute(_:value:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/addrenderingattribute%28_%3Avalue%3Afor%3A%29.json'
content_hash: 'sha256:7900a35cd3c6969b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# addRenderingAttribute(_:value:for:)

<sub>Instance Method</sub>

Sets the rendering attribute for the value and range you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addRenderingAttribute(_ renderingAttribute: NSAttributedString.Key, value: Any?, for textRange: NSTextRange)
```

## Parameters

- `renderingAttribute` — The [NSAttributedString.Key](../../foundation/nsattributedstring/key.md) that represents the attribute.

- `value` — The value for the attribute.

- `textRange` — The range over which to apply the attribute.

## Discussion

Passing `nil` overrides the specified attribute by removing it from the final attributes the framework passes to the layout and rendering engine. This is a convenience method for [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>).

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

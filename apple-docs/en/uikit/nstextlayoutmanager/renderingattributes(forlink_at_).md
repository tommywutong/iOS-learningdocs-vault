---
title: 'renderingAttributes(forLink:at:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/renderingattributes(forlink:at:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/renderingattributes(forlink:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/renderingattributes%28forlink%3Aat%3A%29.json'
content_hash: 'sha256:e5ef24e82772690c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# renderingAttributes(forLink:at:)

<sub>Instance Method</sub>

Returns a dictionary of rendering attributes for rendering a link.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func renderingAttributes(forLink link: Any, at location: any NSTextLocation) -> [NSAttributedString.Key : Any]
```

## Parameters

- `link` — The link.

- `location` — The location of the link in the text.

## Return Value

A  dictionary of rendering attributes.

## Discussion

As with other rendering attributes, specifying [NSNull](../../foundation/nsnull.md) removes the attribute from the final attributes the framework uses for rendering. It has priority over the general rendering attributes.

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- enumerateRenderingAttributesFromLocation:reverse:usingBlock:](<enumeraterenderingattributes(from_reverse_using_).md>) — Enumerates the rendering attributes from a location you specify.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

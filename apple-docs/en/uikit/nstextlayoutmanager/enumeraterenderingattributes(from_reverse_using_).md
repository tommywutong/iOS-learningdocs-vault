---
title: 'enumerateRenderingAttributes(from:reverse:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlayoutmanager/enumeraterenderingattributes(from:reverse:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlayoutmanager/enumeraterenderingattributes%28from%3Areverse%3Ausing%3A%29.json'
content_hash: 'sha256:4a4105e4f9bcfb15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextLayoutManager](../nstextlayoutmanager.md)

# enumerateRenderingAttributes(from:reverse:using:)

<sub>Instance Method</sub>

Enumerates the rendering attributes from a location you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func enumerateRenderingAttributes(from location: any NSTextLocation, reverse: Bool, using block: (NSTextLayoutManager, [NSAttributedString.Key : Any], NSTextRange) -> Bool)
```

## Parameters

- `location` — The location at which to start the enumeration.

- `reverse` — Whether to start the enumeration from the end of the range.

- `block` — A closure you provide to determine if the enumeration finishes early.

## Discussion

This method only enumerates ranges with text that specify rendering attributes. Returning `false` from `block` breaks out of the enumeration.

## See Also

### Adjusting rendering

- [linkRenderingAttributes](linkrenderingattributes.md) — Returns the default set of attributes for rendering a link.
- [- addRenderingAttribute:value:forTextRange:](<addrenderingattribute(__value_for_).md>) — Sets the rendering attribute for the value and range you specify.
- [- renderingAttributesForLink:atLocation:](<renderingattributes(forlink_at_).md>) — Returns a dictionary of rendering attributes for rendering a link.
- [- invalidateRenderingAttributesForTextRange:](<invalidaterenderingattributes(for_).md>) — Invalidates the rendering attributes of the specified text range.
- [- removeRenderingAttribute:forTextRange:](<removerenderingattribute(__for_).md>) — Removes the rendering attribute from the specified text range.
- [- setRenderingAttributes:forTextRange:](<setrenderingattributes(__for_).md>) — Sets the rendering attributes for the range you specify.

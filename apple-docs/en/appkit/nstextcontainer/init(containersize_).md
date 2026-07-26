---
title: 'init(containerSize:)'
framework: AppKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/appkit/nstextcontainer/init(containersize:)'
source_url: 'https://developer.apple.com/documentation/appkit/nstextcontainer/init(containersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextcontainer/init%28containersize%3A%29.json'
content_hash: 'sha256:7d3ae94fcba83b2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextContainer](../nstextcontainer.md)

# init(containerSize:)

<sub>Initializer</sub>

Initializes a text container with a specified bounding rectangle.

> [!warning] Deprecated
> Use [- initWithSize:](<init(size_).md>) instead.

<sub>macOS</sub>

```swift
convenience init(containerSize aContainerSize: NSSize)
```

## Parameters

- `aContainerSize` — The size of the text container’s bounding rectangle.

## Return Value

The newly initialized text container.

## Discussion

The new text container must be added to an [NSLayoutManager](../nslayoutmanager.md) object before it can be used. The text container must also have an [NSTextView](../nstextview.md) object set for text to be displayed. This method is the designated initializer for the `NSTextContainer` class.

## See Also

### Deprecated

- [- lineFragmentRectForProposedRect:sweepDirection:movementDirection:remainingRect:](<linefragmentrect(forproposedrect_sweepdirection_movementdirection_remaining_).md>) — Calculates and returns the longest rectangle available in the proposed rectangle for displaying text. _(deprecated)_
- [- containsPoint:](<contains(__).md>) — Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle. _(deprecated)_
- [containerSize](containersize.md) — The size of the text container’s bounding rectangle. _(deprecated)_

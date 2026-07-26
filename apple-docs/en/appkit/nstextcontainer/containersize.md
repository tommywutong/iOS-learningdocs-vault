---
title: containerSize
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/appkit/nstextcontainer/containersize
source_url: 'https://developer.apple.com/documentation/appkit/nstextcontainer/containersize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextcontainer/containersize.json'
content_hash: 'sha256:cbc5369f75563093'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextContainer](../nstextcontainer.md)

# containerSize

<sub>Instance Property</sub>

The size of the text container’s bounding rectangle.

> [!warning] Deprecated
> Use [size](size.md) instead.

<sub>macOS</sub>

```swift
var containerSize: NSSize { get set }
```

## See Also

### Deprecated

- [- initWithContainerSize:](<init(containersize_).md>) — Initializes a text container with a specified bounding rectangle. _(deprecated)_
- [- lineFragmentRectForProposedRect:sweepDirection:movementDirection:remainingRect:](<linefragmentrect(forproposedrect_sweepdirection_movementdirection_remaining_).md>) — Calculates and returns the longest rectangle available in the proposed rectangle for displaying text. _(deprecated)_
- [- containsPoint:](<contains(__).md>) — Queries whether a point lies within the text container’s region or on the region’s edge—not simply within its bounding rectangle. _(deprecated)_

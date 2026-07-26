---
title: size
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/size
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/size'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/size.json'
content_hash: 'sha256:ac4cdeb53f1d683a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# size

<sub>Instance Property</sub>

The size of the text container’s bounding rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var size: CGSize { get set }
```

## Discussion

This property defines the maximum size for the layout area returned from [- lineFragmentRectForProposedRect:atIndex:writingDirection:remainingRect:](<linefragmentrect(forproposedrect_at_writingdirection_remaining_).md>). A value of `0.0` or less means no limitation.

If you don’t specify an explicit size when you initialize a text container, the system uses a default large size of (`10000000.0`, `10000000.0`).

## See Also

### Defining the container shape

- [exclusionPaths](exclusionpaths.md) — An array of path objects that represents the regions where text doesn’t display in the text container.
- [lineBreakMode](linebreakmode.md) — The behavior of the last line inside the text container.
- [widthTracksTextView](widthtrackstextview.md) — A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [heightTracksTextView](heighttrackstextview.md) — A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.

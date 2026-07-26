---
title: lineBreakMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/linebreakmode
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/linebreakmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/linebreakmode.json'
content_hash: 'sha256:ec4623675710524d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# lineBreakMode

<sub>Instance Property</sub>

The behavior of the last line inside the text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var lineBreakMode: NSLineBreakMode { get set }
```

## Discussion

The [NSLineBreakMode](../nslinebreakmode.md) constants specify what happens when a line is too long for its container. For example, wrapping can occur on word boundaries (the default) or character boundaries, or the line can be clipped or truncated. The default value of this property is [NSLineBreakByWordWrapping](../nslinebreakmode/bywordwrapping.md).

## See Also

### Defining the container shape

- [size](size.md) — The size of the text container’s bounding rectangle.
- [exclusionPaths](exclusionpaths.md) — An array of path objects that represents the regions where text doesn’t display in the text container.
- [widthTracksTextView](widthtrackstextview.md) — A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.
- [heightTracksTextView](heighttrackstextview.md) — A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.

---
title: widthTracksTextView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontainer/widthtrackstextview
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontainer/widthtrackstextview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontainer/widthtrackstextview.json'
content_hash: 'sha256:dc0b69c4edb04435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContainer](../nstextcontainer.md)

# widthTracksTextView

<sub>Instance Property</sub>

A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var widthTracksTextView: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the text container adjusts its width when the width of its text view changes. The default value of this property is [false](../../swift/false.md).

For more information about size tracking, see [Text System Storage Layer Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html#//apple_ref/doc/uid/10000087i).

## See Also

### Related Documentation

- [containerSize](../../appkit/nstextcontainer/containersize.md) — The size of the text container’s bounding rectangle. _(deprecated)_

### Defining the container shape

- [size](size.md) — The size of the text container’s bounding rectangle.
- [exclusionPaths](exclusionpaths.md) — An array of path objects that represents the regions where text doesn’t display in the text container.
- [lineBreakMode](linebreakmode.md) — The behavior of the last line inside the text container.
- [heightTracksTextView](heighttrackstextview.md) — A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.

---
title: containsStart
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectionrect/containsstart
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectionrect/containsstart'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectionrect/containsstart.json'
content_hash: 'sha256:933a78038d6eaf58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionRect](../uitextselectionrect.md)

# containsStart

<sub>Instance Property</sub>

A Boolean value that indicates whether the rectangle contains the start of the selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var containsStart: Bool { get }
```

## Discussion

The value of this property is used to determine the placement of the selection handles in bidirectional text. It provides a clue to the system about whether the start of the selection is in the specified rectangle.

## See Also

### Determining the Selection Status

- [containsEnd](containsend.md) — A Boolean value that indicates whether the rectangle contains the end of the selection.

---
title: isEmpty
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibezierpath/isempty
source_url: 'https://developer.apple.com/documentation/uikit/uibezierpath/isempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibezierpath/isempty.json'
content_hash: 'sha256:962d7a1b4692cf0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBezierPath](../uibezierpath.md)

# isEmpty

<sub>Instance Property</sub>

A Boolean value that indicates whether the path has any valid elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var isEmpty: Bool { get }
```

## Discussion

Valid path elements include commands to move to a specified point, draw a line or curve segment, or close the path. Thus, a path is not considered empty even if all you do is call the [- moveToPoint:](<move(to_).md>) method.

## See Also

### Performing hit-testing

- [- containsPoint:](<contains(__).md>) — Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [bounds](bounds.md) — The bounding rectangle of the path.

---
title: 'contains(_:eoFill:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/path/contains(_:eofill:)'
source_url: 'https://developer.apple.com/documentation/swiftui/path/contains(_:eofill:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/path/contains%28_%3Aeofill%3A%29.json'
content_hash: 'sha256:1f075cf4b043709e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Path](../path.md)

# contains(_:eoFill:)

<sub>Instance Method</sub>

Returns true if the path contains a specified point.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ p: CGPoint, eoFill: Bool = false) -> Bool
```

## Discussion

If `eoFill` is true, this method uses the even-odd rule to define which points are inside the path. Otherwise, it uses the non-zero rule.

## See Also

### Getting the path’s characteristics

- [boundingRect](boundingrect.md) — A rectangle containing all path segments.
- [cgPath](cgpath.md) — An immutable path representing the elements in the path.
- [currentPoint](currentpoint.md) — Returns the last point in the path, or nil if the path contains no points.
- [description](description.md) — A description of the path that may be used to recreate the path via `init?(_:)`.
- [isEmpty](isempty.md) — A Boolean value indicating whether the path contains zero elements.

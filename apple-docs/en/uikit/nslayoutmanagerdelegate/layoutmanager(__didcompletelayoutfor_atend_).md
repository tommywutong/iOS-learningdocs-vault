---
title: 'layoutManager(_:didCompleteLayoutFor:atEnd:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:didcompletelayoutfor:atend:)'
source_url: 'https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:didcompletelayoutfor:atend:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nslayoutmanagerdelegate/layoutmanager%28_%3Adidcompletelayoutfor%3Aatend%3A%29.json'
content_hash: 'sha256:6add915dc751b310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSLayoutManagerDelegate](../nslayoutmanagerdelegate.md)

# layoutManager(_:didCompleteLayoutFor:atEnd:)

<sub>Instance Method</sub>

Informs the delegate when the layout manager finishes laying out text in the specified text container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, didCompleteLayoutFor textContainer: NSTextContainer?, atEnd layoutFinishedFlag: Bool)
```

## Parameters

- `layoutManager` — The layout manager doing the layout.

- `textContainer` — The text container in which layout is complete. If `nil`, if there aren’t enough containers to hold all the text; the delegate can use this information as a cue to add another text container.

- `layoutFinishedFlag` — If [true](../../swift/true.md), `aLayoutManager` is finished laying out its text—this also means that `aTextContainer` is the final text container used by the layout manager. Delegates can use this information to show an indicator or background or to enable or disable a button that forces immediate layout of text.

## Discussion

This message is sent whenever a text container has been filled. This method can be useful for paginating.

## See Also

### Responding to text container layout

- [- layoutManager:textContainer:didChangeGeometryFromSize:](<layoutmanager(__textcontainer_didchangegeometryfrom_).md>) — Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.

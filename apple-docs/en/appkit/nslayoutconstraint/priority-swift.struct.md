---
title: NSLayoutConstraint.Priority
framework: AppKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nslayoutconstraint/priority-swift.struct
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutconstraint/priority-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutconstraint/priority-swift.struct.json'
content_hash: 'sha256:4bf66148c9af6678'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutConstraint](../nslayoutconstraint.md)

# NSLayoutConstraint.Priority

<sub>Structure</sub>

Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

<sub>macOS</sub>

```swift
struct Priority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Comparable](../../swift/comparable.md), [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLayoutPriorityRequired](priority-swift.struct/required.md) — A required constraint.
- [NSLayoutPriorityDefaultHigh](priority-swift.struct/defaulthigh.md) — Priority level with which a button resists compressing its content.
- [NSLayoutPriorityDragThatCanResizeWindow](priority-swift.struct/dragthatcanresizewindow.md) — Appropriate priority level for a drag that may end up resizing the window.
- [NSLayoutPriorityWindowSizeStayPut](priority-swift.struct/windowsizestayput.md) — Priority level for the window’s current size.
- [NSLayoutPriorityDragThatCannotResizeWindow](priority-swift.struct/dragthatcannotresizewindow.md) — Priority level at which a split view divider, say, is dragged.
- [NSLayoutPriorityDefaultLow](priority-swift.struct/defaultlow.md) — Priority level at which a button hugs its contents horizontally.
- [NSLayoutPriorityFittingSizeCompression](priority-swift.struct/fittingsizecompression.md) — When you send a [fittingSize](../nsview/fittingsize.md) message to a view, the smallest size that is large enough for the view’s contents is computed.

### Initializers

- [init(_:)](<priority-swift.struct/init(__).md>)
- [init(rawValue:)](<priority-swift.struct/init(rawvalue_).md>)

## See Also

### Getting the layout priority

- [priority](priority-swift.property.md) — The priority of the constraint.

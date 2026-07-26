---
title: UILayoutPriority
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uilayoutpriority
source_url: 'https://developer.apple.com/documentation/uikit/uilayoutpriority'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uilayoutpriority.json'
content_hash: 'sha256:7a88b24a1428432e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILayoutPriority

<sub>Structure</sub>

The layout priority is used to indicate to the constraint-based layout system which constraints are more important, allowing the system to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UILayoutPriority
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Comparable](../swift/comparable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UILayoutPriorityRequired](uilayoutpriority/required.md) — A required constraint.
- [UILayoutPriorityDefaultHigh](uilayoutpriority/defaulthigh.md) — The priority level with which a button resists compressing its content.
- [UILayoutPriorityDragThatCanResizeScene](uilayoutpriority/dragthatcanresizescene.md) — The priority level for a drag that may end up resizing the window’s scene.
- [UILayoutPrioritySceneSizeStayPut](uilayoutpriority/scenesizestayput.md) — The priority level at which the window’s scene prefers to stay the same size.
- [UILayoutPriorityDragThatCannotResizeScene](uilayoutpriority/dragthatcannotresizescene.md) — The priority level for a drag that won’t resize the window’s scene.
- [UILayoutPriorityDefaultLow](uilayoutpriority/defaultlow.md) — The priority level at which a button hugs its contents horizontally.
- [UILayoutPriorityFittingSizeLevel](uilayoutpriority/fittingsizelevel.md) — The priority level with which the view wants to conform to the target size in that computation.

### Initializers

- [init(_:)](<uilayoutpriority/init(__).md>) — Creates a layout priority structure.
- [init(rawValue:)](<uilayoutpriority/init(rawvalue_).md>) — Creates a layout priority structure with the specified raw value.

## See Also

### Getting the layout priority

- [priority](nslayoutconstraint/priority.md) — The priority of the constraint.
- [NSLayoutConstraint.Priority](../appkit/nslayoutconstraint/priority-swift.struct.md) — Layout priority used to indicate the relative importance of constraints, allowing Auto Layout to make appropriate tradeoffs when satisfying the constraints of the system as a whole.

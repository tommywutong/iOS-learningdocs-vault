---
title: UIScrollTypeMask
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrolltypemask
source_url: 'https://developer.apple.com/documentation/uikit/uiscrolltypemask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrolltypemask.json'
content_hash: 'sha256:c593569933f15c7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScrollTypeMask

<sub>Structure</sub>

A bit mask identifying the scroll type of a pan gesture.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIScrollTypeMask
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Scroll types

- [UIScrollTypeMaskAll](uiscrolltypemask/all.md) — A scroll type that’s either discrete or continuous.
- [UIScrollTypeMaskContinuous](uiscrolltypemask/continuous.md) — A continuous scroll type from a device, like a trackpad.
- [UIScrollTypeMaskDiscrete](uiscrolltypemask/discrete.md) — A discrete scroll type from a device, like a mouse.

### Initializer

- [init(rawValue:)](<uiscrolltypemask/init(rawvalue_).md>) — Creates a new scroll type mask from the raw value.

## See Also

### Tracking scroll events

- [allowedScrollTypesMask](uipangesturerecognizer/allowedscrolltypesmask.md) — A scroll type mask that enables recognition of scroll events.
- [UIScrollType](uiscrolltype.md) — Constants that define the type of the scroll.

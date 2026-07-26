---
title: UIScrollView.DecelerationRate
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscrollview/decelerationrate-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiscrollview/decelerationrate-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscrollview/decelerationrate-swift.struct.json'
content_hash: 'sha256:693091f53d277b08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScrollView](../uiscrollview.md)

# UIScrollView.DecelerationRate

<sub>Structure</sub>

Deceleration rates for the scroll view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct DecelerationRate
```

## Overview

You use these constants to set the value of the [decelerationRate](decelerationrate-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Deceleration rates

- [UIScrollViewDecelerationRateNormal](decelerationrate-swift.struct/normal.md) — The default deceleration rate for a scroll view.
- [UIScrollViewDecelerationRateFast](decelerationrate-swift.struct/fast.md) — A fast deceleration rate for a scroll view.

### Initializers

- [init(rawValue:)](<decelerationrate-swift.struct/init(rawvalue_).md>) — Creates a deceleration rate with the specified raw value.

## See Also

### Managing the scrolling state

- [tracking](istracking.md) — A Boolean value that indicates whether the user has touched the content to initiate scrolling.
- [dragging](isdragging.md) — A Boolean value that indicates whether the user has begun scrolling the content.
- [decelerating](isdecelerating.md) — A Boolean value that indicates whether the content is moving in the scroll view after the user lifted their finger.
- [scrollAnimating](isscrollanimating.md) — A Boolean value that indicates whether the scroll view is currently animating a scroll update.
- [- stopScrollingAndZooming](<stopscrollingandzooming().md>) — Stops active scroll and zoom animations.
- [decelerationRate](decelerationrate-swift.property.md) — A floating-point value that determines the rate of deceleration after the user lifts their finger.

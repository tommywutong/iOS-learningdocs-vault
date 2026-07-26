---
title: UISemanticContentAttribute
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisemanticcontentattribute
source_url: 'https://developer.apple.com/documentation/uikit/uisemanticcontentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisemanticcontentattribute.json'
content_hash: 'sha256:c0cc709c1177d332'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISemanticContentAttribute

<sub>Enumeration</sub>

A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UISemanticContentAttribute
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UISemanticContentAttributeUnspecified](uisemanticcontentattribute/unspecified.md) — The default value for views.
- [UISemanticContentAttributePlayback](uisemanticcontentattribute/playback.md) — A view representing the playback controls, such as Play, Rewind, or Fast Forward buttons or playhead scrubbers.
- [UISemanticContentAttributeSpatial](uisemanticcontentattribute/spatial.md) — A view representing a directional control, such as a segment control for text alignment, or a D-pad control for a game.
- [UISemanticContentAttributeForceLeftToRight](uisemanticcontentattribute/forcelefttoright.md) — A view that’s always displayed using a left-to-right layout.
- [UISemanticContentAttributeForceRightToLeft](uisemanticcontentattribute/forcerighttoleft.md) — A view that’s always displayed using a right-to-left layout.

### Initializers

- [init(rawValue:)](<uisemanticcontentattribute/init(rawvalue_).md>)

## See Also

### Constants

- [AnimationCurve](uiview/animationcurve.md) — Specifies the supported animation curves.
- [AnimationOptions](uiview/animationoptions.md) — Options for animating views using block objects.
- [AnimationTransition](uiview/animationtransition.md) — Animation transition options for use in an animation block object.
- [SystemAnimation](uiview/systemanimation.md) — Option to remove the views from the hierarchy when animation is complete.
- [KeyframeAnimationOptions](uiview/keyframeanimationoptions.md) — Options for configuring keyframe-based animations.
- [Axis](nslayoutconstraint/axis.md) — Keys that specify a horizontal or vertical layout constraint between objects.
- [TintAdjustmentMode](uiview/tintadjustmentmode-swift.enum.md) — The tint adjustment mode for the view.
- [UILayoutFittingCompressedSize](uiview/layoutfittingcompressedsize.md) — The option to use the smallest possible size.
- [UILayoutFittingExpandedSize](uiview/layoutfittingexpandedsize.md) — The option to use the largest possible size.
- [UIViewNoIntrinsicMetric](uiview/nointrinsicmetric.md) — The absence of an intrinsic metric for a given numeric view property.
- [AutoresizingMask](uiview/autoresizingmask-swift.struct.md) — Options for automatic view resizing.

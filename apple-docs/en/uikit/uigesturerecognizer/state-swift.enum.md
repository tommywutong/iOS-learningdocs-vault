---
title: UIGestureRecognizer.State
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/state-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/state-swift.enum.json'
content_hash: 'sha256:f1afe46ec6068550'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# UIGestureRecognizer.State

<sub>Enumeration</sub>

Constants that represent the current state a gesture recognizer is in.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum State
```

## Overview

Gesture recognizers recognize a discrete event such as a tap or a swipe but don’t report changes within the gesture. In other words, discrete gestures don’t transition through the Began and Changed states and they can’t fail or be canceled.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIGestureRecognizerStatePossible](state-swift.enum/possible.md) — The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizerStateBegan](state-swift.enum/began.md) — The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizerStateChanged](state-swift.enum/changed.md) — The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizerStateEnded](state-swift.enum/ended.md) — The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizerStateCancelled](state-swift.enum/cancelled.md) — The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizerStateFailed](state-swift.enum/failed.md) — The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [UIGestureRecognizerStateRecognized](state-swift.enum/recognized.md) — The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.

### Initializers

- [init(rawValue:)](<state-swift.enum/init(rawvalue_).md>)

## See Also

### Getting the recognizer’s state and view

- [state](state-swift.property.md) — The current state of the gesture recognizer.
- [view](view.md) — The view the gesture recognizer is attached to.
- [enabled](isenabled.md) — A Boolean property that indicates whether the gesture recognizer is enabled.
- [buttonMask](buttonmask.md) — A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags in the gesture represented by the gesture recognizer.

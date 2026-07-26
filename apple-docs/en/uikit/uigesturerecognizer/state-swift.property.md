---
title: state
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/state-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/state-swift.property.json'
content_hash: 'sha256:fd1f6eb66c567ce8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# state

<sub>Instance Property</sub>

The current state of the gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var state: UIGestureRecognizer.State { get set }
```

## Discussion

The possible states a gesture recognizer can be in are represented by the constants of type [State](state-swift.enum.md). Some of these states aren’t applicable to discrete gestures. The read-only version of the [state](state-swift.property.md) property is intended for clients of a gesture-recognizer class and not subclasses.

### Special considerations

Subclasses of [UIGestureRecognizer](../uigesturerecognizer.md) must use a read-write version of the state property. They get this redeclaration when they import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift):

```objc
@property(nonatomic,readwrite) UIGestureRecognizerState state;
```

Recognizers for discrete gestures transition from [UIGestureRecognizerStatePossible](state-swift.enum/possible.md) to [UIGestureRecognizerStateFailed](state-swift.enum/failed.md) or [UIGestureRecognizerStateRecognized](state-swift.enum/recognized.md). Recognizers for continuous gesture transition from [UIGestureRecognizerStatePossible](state-swift.enum/possible.md) to these phases in the given order: [UIGestureRecognizerStateBegan](state-swift.enum/began.md), [UIGestureRecognizerStateChanged](state-swift.enum/changed.md), and [UIGestureRecognizerStateEnded](state-swift.enum/ended.md). If, however, they receive a cancellation touch, they should transition to [UIGestureRecognizerStateCancelled](state-swift.enum/cancelled.md). If recognizers for continuous gestures can’t interpret a multi-touch sequence as their gesture, they transition to [UIGestureRecognizerStateFailed](state-swift.enum/failed.md).

## See Also

### Getting the recognizer’s state and view

- [State](state-swift.enum.md) — Constants that represent the current state a gesture recognizer is in.
- [view](view.md) — The view the gesture recognizer is attached to.
- [enabled](isenabled.md) — A Boolean property that indicates whether the gesture recognizer is enabled.
- [buttonMask](buttonmask.md) — A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags in the gesture represented by the gesture recognizer.

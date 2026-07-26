---
title: UIGestureRecognizer.State.ended
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/state-swift.enum/ended
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/ended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/state-swift.enum/ended.json'
content_hash: 'sha256:97c1a2b6f649275c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIGestureRecognizer](../../uigesturerecognizer.md) · [State](../state-swift.enum.md)

# UIGestureRecognizer.State.ended

<sub>Case</sub>

The gesture recognizer has received touches recognized as the end of a continuous gesture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case ended
```

## Discussion

The gesture recognizer sends its action message (or messages) at the next cycle of the run loop and resets its state to [UIGestureRecognizerStatePossible](possible.md).

## See Also

### Constants

- [UIGestureRecognizerStatePossible](possible.md) — The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.
- [UIGestureRecognizerStateBegan](began.md) — The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizerStateChanged](changed.md) — The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizerStateCancelled](cancelled.md) — The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizerStateFailed](failed.md) — The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [UIGestureRecognizerStateRecognized](recognized.md) — The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.

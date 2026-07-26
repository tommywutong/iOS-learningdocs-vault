---
title: UIGestureRecognizer.State.possible
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/state-swift.enum/possible
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/state-swift.enum/possible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/state-swift.enum/possible.json'
content_hash: 'sha256:4c92b904561ceb08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIGestureRecognizer](../../uigesturerecognizer.md) · [State](../state-swift.enum.md)

# UIGestureRecognizer.State.possible

<sub>Case</sub>

The gesture recognizer hasn’t yet recognized its gesture, but may be evaluating touch events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case possible
```

## Discussion

This is the default state.

## See Also

### Constants

- [UIGestureRecognizerStateBegan](began.md) — The gesture recognizer has received touch objects recognized as a continuous gesture.
- [UIGestureRecognizerStateChanged](changed.md) — The gesture recognizer has received touches recognized as a change to a continuous gesture.
- [UIGestureRecognizerStateEnded](ended.md) — The gesture recognizer has received touches recognized as the end of a continuous gesture.
- [UIGestureRecognizerStateCancelled](cancelled.md) — The gesture recognizer has received touches resulting in the cancellation of a continuous gesture.
- [UIGestureRecognizerStateFailed](failed.md) — The gesture recognizer has received a multi-touch sequence that it can’t recognize as its gesture.
- [UIGestureRecognizerStateRecognized](recognized.md) — The gesture recognizer has received a multitouch sequence that it recognizes as its gesture.

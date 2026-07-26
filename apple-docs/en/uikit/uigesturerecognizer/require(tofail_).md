---
title: 'require(toFail:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizer/require(tofail:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/require(tofail:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/require%28tofail%3A%29.json'
content_hash: 'sha256:92e5cb27bc44613f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# require(toFail:)

<sub>Instance Method</sub>

Creates a dependency relationship between the gesture recognizer and another gesture recognizer when the objects are created.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func require(toFail otherGestureRecognizer: UIGestureRecognizer)
```

## Parameters

- `otherGestureRecognizer` — Another gesture-recognizer object (an instance of a subclass of [UIGestureRecognizer](../uigesturerecognizer.md)).

## Discussion

This method works fine when gesture recognizers aren’t created elsewhere in the app — or in a framework — and the set of gesture recognizers remains the same. If you need to set up failure requirements lazily or in different view hierarchies, use [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldrequirefailureof_).md>) and [- gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:](<../uigesturerecognizerdelegate/gesturerecognizer(__shouldberequiredtofailby_).md>) instead. (Note that the [- shouldRequireFailureOfGestureRecognizer:](<shouldrequirefailure(of_).md>) and [- shouldBeRequiredToFailByGestureRecognizer:](<shouldberequiredtofail(by_).md>) methods let subclasses define class-wide failure requirements.)

This method creates a relationship with another gesture recognizer that delays the current gesture recognizer’s transition out of [UIGestureRecognizerStatePossible](state-swift.enum/possible.md). The state that the current gesture recognizer transitions to depends on what happens with `otherGestureRecognizer`:

- If `otherGestureRecognizer` transitions to [UIGestureRecognizerStateFailed](state-swift.enum/failed.md), the current gesture recognizer transitions to its normal next state.
- If `otherGestureRecognizer` transitions to [UIGestureRecognizerStateRecognized](state-swift.enum/recognized.md) or [UIGestureRecognizerStateBegan](state-swift.enum/began.md), the current gesture recognizer transitions to [UIGestureRecognizerStateFailed](state-swift.enum/failed.md).

An example where this method might be called is when you want a single-tap gesture require that a double-tap gesture fail.

## See Also

### Related Documentation

- [- shouldBeRequiredToFailByGestureRecognizer:](<shouldberequiredtofail(by_).md>) — Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [- shouldRequireFailureOfGestureRecognizer:](<shouldrequirefailure(of_).md>) — Overridden to indicate that the receiver requires the specified gesture recognizer to fail.

---
title: 'gestureRecognizer(_:shouldBeRequiredToFailBy:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer%28_%3Ashouldberequiredtofailby%3A%29.json'
content_hash: 'sha256:bd33fcef89cee39e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)

# gestureRecognizer(_:shouldBeRequiredToFailBy:)

<sub>Instance Method</sub>

Asks the delegate if a gesture recognizer should be required to fail by another gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

## Parameters

- `gestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md). This is the object sending the message to the delegate.

- `otherGestureRecognizer` — An instance of a subclass of the abstract base class [UIGestureRecognizer](../uigesturerecognizer.md).

## Return Value

[true](../../swift/true.md) to set up a dynamic failure requirement between `gestureRecognizer` and `otherGestureRecognizer`. The default implementation returns [false](../../swift/false.md)—`gestureRecognizer` isn’t required to fail by `otherGestureRecognizer`.

## Discussion

This method is called once per attempt to recognize, so failure requirements can be determined lazily and may be set up between recognizers across view hierarchies. Note that returning [true](../../swift/true.md) is guaranteed to set up the failure requirement; returning [false](../../swift/false.md), on the other hand, isn’t guaranteed to prevent or remove a failure requirement because `otherGestureRecognizer` might make itself a failure requirement by using its own subclass or delegate methods.

## See Also

### Setting up failure requirements

- [- gestureRecognizer:shouldRequireFailureOfGestureRecognizer:](<gesturerecognizer(__shouldrequirefailureof_).md>) — Asks the delegate if a gesture recognizer should require another gesture recognizer to fail.

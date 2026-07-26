---
title: 'touches(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uievent/touches(for:)-6krou'
source_url: 'https://developer.apple.com/documentation/uikit/uievent/touches(for:)-6krou'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/touches%28for%3A%29-6krou.json'
content_hash: 'sha256:9fb191e978c0b893'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# touches(for:)

<sub>Instance Method</sub>

Returns the touch objects that are being delivered to the specified gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touches(for gesture: UIGestureRecognizer) -> Set<UITouch>?
```

## Parameters

- `gesture` — An instance of a subclass of the abstract base class UIGestureRecognizer. This gesture-recognizer object must be attached to a view to receive the touches hit-tested to that view and its subviews.

## Return Value

A set of [UITouch](../uitouch.md) objects representing the touches being delivered to the specified gesture recognizer for the event represented by the receiver.

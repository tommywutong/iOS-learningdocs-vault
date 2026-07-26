---
title: numberOfTouches
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer/numberoftouches
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer/numberoftouches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer/numberoftouches.json'
content_hash: 'sha256:ddb7ff5cf0f08303'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIGestureRecognizer](../uigesturerecognizer.md)

# numberOfTouches

<sub>Instance Property</sub>

The number of touches involved in the gesture represented by the gesture recognizer.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfTouches: Int { get }
```

## Return Value

The number of [UITouch](../uitouch.md) objects in a private array maintained by the receiver. Each of these objects represents a touch in the current gesture.

## Discussion

Using the value returned by this method in a loop, you can ask for the location of individual touches using the [- locationOfTouch:inView:](<location(oftouch_in_).md>) method.

## See Also

### Getting the touches and location of a gesture

- [- locationInView:](<location(in_).md>) — Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [- locationOfTouch:inView:](<location(oftouch_in_).md>) — Returns the location of one of the gesture’s touches in the local coordinate system of a given view.

---
title: allTouches
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uievent/alltouches
source_url: 'https://developer.apple.com/documentation/uikit/uievent/alltouches'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/alltouches.json'
content_hash: 'sha256:5e28b2631ee43f47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# allTouches

<sub>Instance Property</sub>

All touches associated with the event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allTouches: Set<UITouch>? { get }
```

## Return Value

A set of [UITouch](../uitouch.md) objects representing all touches associated with the event.

## Discussion

If the touches of the event originate in different views and windows, the [UITouch](../uitouch.md) objects obtained from this method will be associated with different responder objects.

## See Also

### Getting the touches for an event

- [- touchesForView:](<touches(for_)-9neb4.md>) — Returns the touch objects from the event that belong to the specified given view.
- [- touchesForWindow:](<touches(for_)-767rm.md>) — Returns the touch objects from the event that belong to the specified window.
- [- coalescedTouchesForTouch:](<coalescedtouches(for_).md>) — Returns all of the touches associated with the specified main touch.
- [- predictedTouchesForTouch:](<predictedtouches(for_).md>) — Returns an array of touches that are predicted to occur for the specified touch.

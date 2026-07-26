---
title: 'touches(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uievent/touches(for:)-767rm'
source_url: 'https://developer.apple.com/documentation/uikit/uievent/touches(for:)-767rm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uievent/touches%28for%3A%29-767rm.json'
content_hash: 'sha256:21a095bf167b4c7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEvent](../uievent.md)

# touches(for:)

<sub>Instance Method</sub>

Returns the touch objects from the event that belong to the specified window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func touches(for window: UIWindow) -> Set<UITouch>?
```

## Parameters

- `window` — The [UIWindow](../uiwindow.md) object in which the touches originally occurred.

## Return Value

A set of [UITouch](../uitouch.md) objects representing the touches that belong to the specified window.

## See Also

### Getting the touches for an event

- [allTouches](alltouches.md) — All touches associated with the event.
- [- touchesForView:](<touches(for_)-9neb4.md>) — Returns the touch objects from the event that belong to the specified given view.
- [- coalescedTouchesForTouch:](<coalescedtouches(for_).md>) — Returns all of the touches associated with the specified main touch.
- [- predictedTouchesForTouch:](<predictedtouches(for_).md>) — Returns an array of touches that are predicted to occur for the specified touch.

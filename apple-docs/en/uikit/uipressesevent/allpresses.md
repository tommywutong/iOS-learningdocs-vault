---
title: allPresses
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipressesevent/allpresses
source_url: 'https://developer.apple.com/documentation/uikit/uipressesevent/allpresses'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipressesevent/allpresses.json'
content_hash: 'sha256:fa36bc338e21fa50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPressesEvent](../uipressesevent.md)

# allPresses

<sub>Instance Property</sub>

The state of all physical buttons in the event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allPresses: Set<UIPress> { get }
```

## Return Value

The set of [UIPress](../uipress.md) instances that participated in this event.

## See Also

### Reading the event button presses

- [- pressesForGestureRecognizer:](<presses(for_).md>) — Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

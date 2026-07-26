---
title: 'presentationTransitionDidEnd(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipresentationcontroller/presentationtransitiondidend(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationtransitiondidend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentationtransitiondidend%28_%3A%29.json'
content_hash: 'sha256:34b75529cf3a405b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentationTransitionDidEnd(_:)

<sub>Instance Method</sub>

Notifies the presentation controller that the presentation animations finished.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func presentationTransitionDidEnd(_ completed: Bool)
```

## Parameters

- `completed` — [true](../../swift/true.md) if the animations completed and the presented view controller is now visible or [false](../../swift/false.md) if the animations were canceled and the presenting view controller is still visible.

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to perform any required cleanup. For example, if the completed parameter is [false](../../swift/false.md), you would use this method to remove your presentation’s custom views from the view hierarchy.

For an example of how to implement this method, see [Add custom views to a presentation](../uipresentationcontroller.md#Add-custom-views-to-a-presentation).

## See Also

### Tracking the transition’s start and end

- [- presentationTransitionWillBegin](<presentationtransitionwillbegin().md>) — Notifies the presentation controller that the presentation animations are about to start.
- [- dismissalTransitionWillBegin](<dismissaltransitionwillbegin().md>) — Notifies the presentation controller that the dismissal animations are about to start.
- [- dismissalTransitionDidEnd:](<dismissaltransitiondidend(__).md>) — Notifies the presentation controller that the dismissal animations finished.

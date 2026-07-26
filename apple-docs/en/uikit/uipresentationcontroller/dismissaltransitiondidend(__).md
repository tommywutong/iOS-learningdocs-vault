---
title: 'dismissalTransitionDidEnd(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipresentationcontroller/dismissaltransitiondidend(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitiondidend(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/dismissaltransitiondidend%28_%3A%29.json'
content_hash: 'sha256:ea37c162777c4d1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# dismissalTransitionDidEnd(_:)

<sub>Instance Method</sub>

Notifies the presentation controller that the dismissal animations finished.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dismissalTransitionDidEnd(_ completed: Bool)
```

## Parameters

- `completed` — [true](../../swift/true.md) if the animations completed and the presented view controller was dismissed or [false](../../swift/false.md) if the animations were canceled and the presented view controller is still visible.

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to remove any custom views that the presentation controller added to the view hierarchy. Remove your views only if the `completed` parameter is [true](../../swift/true.md).

## See Also

### Tracking the transition’s start and end

- [- presentationTransitionWillBegin](<presentationtransitionwillbegin().md>) — Notifies the presentation controller that the presentation animations are about to start.
- [- presentationTransitionDidEnd:](<presentationtransitiondidend(__).md>) — Notifies the presentation controller that the presentation animations finished.
- [- dismissalTransitionWillBegin](<dismissaltransitionwillbegin().md>) — Notifies the presentation controller that the dismissal animations are about to start.

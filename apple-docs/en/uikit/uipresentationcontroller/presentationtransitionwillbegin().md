---
title: presentationTransitionWillBegin()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/presentationtransitionwillbegin()
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/presentationtransitionwillbegin()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/presentationtransitionwillbegin%28%29.json'
content_hash: 'sha256:cdd2b2c5538811d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# presentationTransitionWillBegin()

<sub>Instance Method</sub>

Notifies the presentation controller that the presentation animations are about to start.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func presentationTransitionWillBegin()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override it and use it to add custom views to the view hierarchy and to create any animations associated with those views. To perform your animations, get the transition coordinator of the presented view controller and call its [- animateAlongsideTransition:completion:](<../uiviewcontrollertransitioncoordinator/animate(alongsidetransition_completion_).md>) or [- animateAlongsideTransitionInView:animation:completion:](<../uiviewcontrollertransitioncoordinator/animatealongsidetransition(in_animation_completion_).md>) method. Calling those methods ensures that your animations are executed at the same time as any other transition animations.

For an example of how to implement this method, see [Add custom views to a presentation](../uipresentationcontroller.md#Add-custom-views-to-a-presentation).

## See Also

### Tracking the transition’s start and end

- [- presentationTransitionDidEnd:](<presentationtransitiondidend(__).md>) — Notifies the presentation controller that the presentation animations finished.
- [- dismissalTransitionWillBegin](<dismissaltransitionwillbegin().md>) — Notifies the presentation controller that the dismissal animations are about to start.
- [- dismissalTransitionDidEnd:](<dismissaltransitiondidend(__).md>) — Notifies the presentation controller that the dismissal animations finished.

---
title: dismissalTransitionWillBegin()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipresentationcontroller/dismissaltransitionwillbegin()
source_url: 'https://developer.apple.com/documentation/uikit/uipresentationcontroller/dismissaltransitionwillbegin()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipresentationcontroller/dismissaltransitionwillbegin%28%29.json'
content_hash: 'sha256:4174ec9df3d53270'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPresentationController](../uipresentationcontroller.md)

# dismissalTransitionWillBegin()

<sub>Instance Method</sub>

Notifies the presentation controller that the dismissal animations are about to start.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dismissalTransitionWillBegin()
```

## Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to configure any animations associated with your presentation’s custom views. To perform your animations, get the transition coordinator of the presented view controller and call its [- animateAlongsideTransition:completion:](<../uiviewcontrollertransitioncoordinator/animate(alongsidetransition_completion_).md>) or [- animateAlongsideTransitionInView:animation:completion:](<../uiviewcontrollertransitioncoordinator/animatealongsidetransition(in_animation_completion_).md>) method. Calling those methods ensures that your animations are executed at the same time as any other transition animations.

Do not use this method to remove your views from the view hierarchy. Remove your views in the [- dismissalTransitionDidEnd:](<dismissaltransitiondidend(__).md>) method instead.

## See Also

### Tracking the transition’s start and end

- [- presentationTransitionWillBegin](<presentationtransitionwillbegin().md>) — Notifies the presentation controller that the presentation animations are about to start.
- [- presentationTransitionDidEnd:](<presentationtransitiondidend(__).md>) — Notifies the presentation controller that the presentation animations finished.
- [- dismissalTransitionDidEnd:](<dismissaltransitiondidend(__).md>) — Notifies the presentation controller that the dismissal animations finished.

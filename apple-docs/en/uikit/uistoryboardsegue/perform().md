---
title: perform()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uistoryboardsegue/perform()
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboardsegue/perform()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboardsegue/perform%28%29.json'
content_hash: 'sha256:76585edc551fb199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboardSegue](../uistoryboardsegue.md)

# perform()

<sub>Instance Method</sub>

Performs the visual transition for the segue.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func perform()
```

## Discussion

Subclasses override this method and use it to perform the animations from the views in [sourceViewController](source.md) to the views in [destinationViewController](destination.md). Typically, you use UIKit or Core Animation to set up an animation from one set of views to the next. For more complex animations, you might take a snapshot image of the two view hierarchies and manipulate the images instead of the actual view objects.

Regardless of how you perform the animation, at the end of it, you’re responsible for installing the destination view controller (and its views) in the right place so that it can handle events. For example, if you were to implement a custom modal transition, you might perform your animations using snapshot images and then at the end call the [presentModalViewController:animated:](../uiviewcontroller/presentmodalviewcontroller_animated_.md) method (with animations disabled) to set up the appropriate modal relationship between the source and destination view controllers.

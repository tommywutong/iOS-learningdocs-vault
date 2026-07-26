---
title: gesturesForFailureRequirements
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinteraction/gesturesforfailurerequirements
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteraction/gesturesforfailurerequirements'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteraction/gesturesforfailurerequirements.json'
content_hash: 'sha256:979ca80934002769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInteraction](../uitextinteraction.md)

# gesturesForFailureRequirements

<sub>Instance Property</sub>

The list of gestures that the text interaction adds to the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var gesturesForFailureRequirements: [UIGestureRecognizer] { get }
```

## Discussion

If your app provides other gestures in the same view hierarchy, you may want to set up failure requirements between your app’s gestures and the gestures added by the text interaction. To do this, use the [- requireGestureRecognizerToFail:](<../uigesturerecognizer/require(tofail_).md>) method to relate your gestures to those listed in [gesturesForFailureRequirements](gesturesforfailurerequirements.md).

## See Also

### Getting interaction information

- [textInteractionMode](textinteractionmode.md) — The mode of the text interaction.
- [UITextInteractionMode](../uitextinteractionmode.md) — Modes that determine the selection behaviors that a text interaction provides.

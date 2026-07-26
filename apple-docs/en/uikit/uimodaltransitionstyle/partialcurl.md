---
title: UIModalTransitionStyle.partialCurl
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimodaltransitionstyle/partialcurl
source_url: 'https://developer.apple.com/documentation/uikit/uimodaltransitionstyle/partialcurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimodaltransitionstyle/partialcurl.json'
content_hash: 'sha256:b9e6d2c98e103a89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIModalTransitionStyle](../uimodaltransitionstyle.md)

# UIModalTransitionStyle.partialCurl

<sub>Case</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case partialCurl
```

## Discussion

When the view controller is presented, one corner of the current view curls up to reveal the presented view underneath. On dismissal, the curled up page unfurls itself back on top of the presented view. A view controller presented using this transition is itself prevented from presenting any additional view controllers.

This transition style is supported only if the parent view controller is presenting a full-screen view and you use the [UIModalPresentationFullScreen](../uimodalpresentationstyle/fullscreen.md) modal presentation style. Attempting to use a different form factor for the parent view or a different presentation style triggers an exception.

## See Also

### Constants

- [UIModalTransitionStyleCoverVertical](coververtical.md)
- [UIModalTransitionStyleFlipHorizontal](fliphorizontal.md)
- [UIModalTransitionStyleCrossDissolve](crossdissolve.md)

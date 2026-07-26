---
title: searchControllerObservedScrollView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 13.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchcontroller/searchcontrollerobservedscrollview
source_url: 'https://developer.apple.com/documentation/uikit/uisearchcontroller/searchcontrollerobservedscrollview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchcontroller/searchcontrollerobservedscrollview.json'
content_hash: 'sha256:8f9c8e78123abb26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchController](../uisearchcontroller.md)

# searchControllerObservedScrollView

<sub>Instance Property</sub>

The view with which the controller coordinates scrolling animations.

> [!warning] Deprecated
> Use [- setContentScrollView:forEdge:](<../uiviewcontroller/setcontentscrollview(__for_).md>) on the [searchResultsController](searchresultscontroller.md) instead.

<sub>tvOS</sub>

```swift
var searchControllerObservedScrollView: UIScrollView? { get set }
```

## See Also

### Deprecated

- [dimsBackgroundDuringPresentation](dimsbackgroundduringpresentation.md) — A Boolean indicating whether to dim the underlying content during a search. _(deprecated)_

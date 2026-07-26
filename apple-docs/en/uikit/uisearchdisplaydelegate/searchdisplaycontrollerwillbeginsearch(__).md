---
title: 'searchDisplayControllerWillBeginSearch(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch%28_%3A%29.json'
content_hash: 'sha256:2aa962a6c740edd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchDisplayDelegate](../uisearchdisplaydelegate.md)

# searchDisplayControllerWillBeginSearch(_:)

<sub>Instance Method</sub>

Tells the delegate that the controller is about to begin searching.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func searchDisplayControllerWillBeginSearch(_ controller: UISearchDisplayController)
```

## Parameters

- `controller` — The search display controller for which the receiver is the delegate.

## See Also

### Responding to search state change

- [- searchDisplayControllerDidBeginSearch:](<searchdisplaycontrollerdidbeginsearch(__).md>) — Tells the delegate that the controller has started searching. _(deprecated)_
- [- searchDisplayControllerWillEndSearch:](<searchdisplaycontrollerwillendsearch(__).md>) — Tells the delegate that the controller is about to end searching. _(deprecated)_
- [- searchDisplayControllerDidEndSearch:](<searchdisplaycontrollerdidendsearch(__).md>) — Tells the delegate that the controller has finished searching. _(deprecated)_

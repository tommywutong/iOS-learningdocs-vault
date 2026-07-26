---
title: preferredContentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/preferredcontentsize
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/preferredcontentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/preferredcontentsize.json'
content_hash: 'sha256:1b5fd54f9f37d327'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# preferredContentSize

<sub>Instance Property</sub>

The preferred size for the view controller’s view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredContentSize: CGSize { get set }
```

## Discussion

The value in this property is used primarily when displaying the view controller’s content in a popover but may also be used in other situations. Changing the value of this property while the view controller is being displayed in a popover animates the size change; however, the change is not animated if you specify a width or height of `0.0`.

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

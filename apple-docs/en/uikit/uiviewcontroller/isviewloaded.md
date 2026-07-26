---
title: isViewLoaded
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/isviewloaded
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/isviewloaded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/isviewloaded.json'
content_hash: 'sha256:f9efb405410d1bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# isViewLoaded

<sub>Instance Property</sub>

A Boolean value indicating whether the view is currently loaded into memory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isViewLoaded: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when the view is in memory or [false](../../swift/false.md) when it is not. Accessing this property does not attempt to load the view if it is not currently in memory.

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

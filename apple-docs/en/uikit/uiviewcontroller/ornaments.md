---
title: ornaments
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/ornaments
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/ornaments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/ornaments.json'
content_hash: 'sha256:1ab5f7a384baac83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# ornaments

<sub>Instance Property</sub>

SwiftUI ornaments to display adjacent to the view controller.

<sub>visionOS</sub>

```swift
@MainActor @preconcurrency var ornaments: [UIOrnament] { get set }
```

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.

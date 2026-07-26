---
title: title
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/title
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/title'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/title.json'
content_hash: 'sha256:a7ad6e8d88e12a48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# title

<sub>Instance Property</sub>

A localized string that represents the view this controller manages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var title: String? { get set }
```

## Discussion

Set the title to a human-readable string that describes the view. If the view controller has a valid navigation item or tab-bar item, assigning a value to this property updates the title text of those objects.

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

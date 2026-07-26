---
title: loadViewIfNeeded()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/loadviewifneeded()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/loadviewifneeded()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/loadviewifneeded%28%29.json'
content_hash: 'sha256:88a5574662b2f8a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# loadViewIfNeeded()

<sub>Instance Method</sub>

Loads the view controller’s view if it’s not loaded yet.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func loadViewIfNeeded()
```

## Discussion

Calling this method loads the view controller’s view from its storyboard file, or creates the view as needed based on the established rules.

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

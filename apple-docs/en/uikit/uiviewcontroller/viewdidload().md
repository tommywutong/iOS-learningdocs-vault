---
title: viewDidLoad()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/viewdidload()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/viewdidload()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/viewdidload%28%29.json'
content_hash: 'sha256:009f92140f895a9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# viewDidLoad()

<sub>Instance Method</sub>

Called after the controller’s view is loaded into memory.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func viewDidLoad()
```

## Discussion

This method is called after the view controller has loaded its view hierarchy into memory. This method is called regardless of whether the view hierarchy was loaded from a nib file or created programmatically in the [- loadView](<loadview().md>) method. You usually override this method to perform additional initialization on views that were loaded from nib files.

## See Also

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

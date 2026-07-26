---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/view
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/view.json'
content_hash: 'sha256:1a3f496b90480975'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# view

<sub>Instance Property</sub>

The view that the controller manages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var view: UIView! { get set }
```

## Discussion

This property represents the root view of the view controller’s view hierarchy. The default value of this property is `nil`.

If you access this property when its value is `nil`, the view controller automatically calls the [- loadView](<loadview().md>) method and returns the resulting view.

Each view controller is the sole owner of its view object. Don’t associate the same view object with multiple view controllers. The only exception is that a container view controller implementation may add another view controller’s view object to its own view hierarchy. Before adding the subview, the container must first call its [- addChildViewController:](<addchild(__).md>) method to create a parent-child relationship between the two view controller objects.

Because accessing this property can cause the view to be loaded automatically, you can use [viewLoaded](isviewloaded.md) to determine if the view is currently in memory. Unlike this property, [viewLoaded](isviewloaded.md) doesn’t force the loading of the view if it’s not currently in memory.

For more information about how a view controller loads and unloads its view, see [Managing your app’s life cycle](../managing-your-app-s-life-cycle.md).

## See Also

### Managing the view

- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- loadView](<loadview().md>) — Creates the view that the controller manages.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

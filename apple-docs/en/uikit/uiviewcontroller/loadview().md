---
title: loadView()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/loadview()
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/loadview()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/loadview%28%29.json'
content_hash: 'sha256:ec60e194b24b57ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# loadView()

<sub>Instance Method</sub>

Creates the view that the controller manages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func loadView()
```

## Discussion

You should never call this method directly. The view controller calls this method when its [view](view.md) property is requested but is currently `nil`. This method loads or creates a view and assigns it to the [view](view.md) property.

If the view controller has an associated nib file, this method loads the view from the nib file. A view controller has an associated nib file if the [nibName](nibname.md) property returns a non-`nil` value, which occurs if the view controller was instantiated from a storyboard, if you explicitly assigned it a nib file using the [- initWithNibName:bundle:](<init(nibname_bundle_).md>) method, or if iOS finds a nib file in the app bundle with a name based on the view controller’s class name. If the view controller does not have an associated nib file, this method creates a plain [UIView](../uiview.md) object instead.

If you use Interface Builder to create your views and initialize the view controller, you must not override this method.

You can override this method in order to create your views manually. If you choose to do so, assign the root view of your view hierarchy to the [view](view.md) property. The views you create should be unique instances and should not be shared with any other view controller object. Your custom implementation of this method should not call `super`.

If you want to perform any additional initialization of your views, do so in the [- viewDidLoad](<viewdidload().md>) method.

## See Also

### Related Documentation

- [nibName](nibname.md) — The name of the view controller’s nib file, if one was specified.

### Managing the view

- [view](view.md) — The view that the controller manages.
- [viewIfLoaded](viewifloaded.md) — The view controller’s view, or `nil` if the view isn’t yet loaded.
- [viewLoaded](isviewloaded.md) — A Boolean value indicating whether the view is currently loaded into memory.
- [- viewDidLoad](<viewdidload().md>) — Called after the controller’s view is loaded into memory.
- [- loadViewIfNeeded](<loadviewifneeded().md>) — Loads the view controller’s view if it’s not loaded yet.
- [title](title.md) — A localized string that represents the view this controller manages.
- [preferredContentSize](preferredcontentsize.md) — The preferred size for the view controller’s view.
- [ornaments](ornaments.md) — SwiftUI ornaments to display adjacent to the view controller.

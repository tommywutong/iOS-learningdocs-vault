---
title: 'viewDidAppear(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingcontroller/viewdidappear(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/viewdidappear(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/viewdidappear%28_%3A%29.json'
content_hash: 'sha256:60836dee8e75be72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# viewDidAppear(_:)

<sub>Instance Method</sub>

Notifies the view controller that its view has been added to a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency override dynamic func viewDidAppear(_ animated: Bool)
```

## Parameters

- `animated` — If `true`, the view is being added using an animation.

## Discussion

SwiftUI calls this method after adding the hosting controller’s root view to the view hierarchy. You can override this method to perform custom tasks associated with the appearance of the view. If you override this method, you must call `super` at some point in your implementation.

## See Also

### Responding to view-related events

- [loadView()](<loadview().md>)
- [viewWillAppear(_:)](<viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [viewWillDisappear(_:)](<viewwilldisappear(__).md>) — Notifies the view controller that its view will be removed from a view hierarchy.
- [viewDidDisappear(_:)](<viewdiddisappear(__).md>)
- [willMove(toParent:)](<willmove(toparent_).md>)
- [didMove(toParent:)](<didmove(toparent_).md>)
- [viewWillTransition(to:with:)](<viewwilltransition(to_with_).md>)
- [viewWillLayoutSubviews()](<viewwilllayoutsubviews().md>)
- [target(forAction:withSender:)](<target(foraction_withsender_).md>)
- [rootView](rootview.md) — The root view of the SwiftUI view hierarchy managed by this view controller.

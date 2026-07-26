---
title: rootView
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontroller/rootview
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/rootview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/rootview.json'
content_hash: 'sha256:fc314f5f4d4992c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# rootView

<sub>Instance Property</sub>

The root view of the SwiftUI view hierarchy managed by this view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency var rootView: Content { get set }
```

## See Also

### Responding to view-related events

- [loadView()](<loadview().md>)
- [viewWillAppear(_:)](<viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [viewDidAppear(_:)](<viewdidappear(__).md>) — Notifies the view controller that its view has been added to a view hierarchy.
- [viewWillDisappear(_:)](<viewwilldisappear(__).md>) — Notifies the view controller that its view will be removed from a view hierarchy.
- [viewDidDisappear(_:)](<viewdiddisappear(__).md>)
- [willMove(toParent:)](<willmove(toparent_).md>)
- [didMove(toParent:)](<didmove(toparent_).md>)
- [viewWillTransition(to:with:)](<viewwilltransition(to_with_).md>)
- [viewWillLayoutSubviews()](<viewwilllayoutsubviews().md>)
- [target(forAction:withSender:)](<target(foraction_withsender_).md>)

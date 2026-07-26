---
title: 'target(forAction:withSender:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/uihostingcontroller/target(foraction:withsender:)'
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller/target(foraction:withsender:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller/target%28foraction%3Awithsender%3A%29.json'
content_hash: 'sha256:c9b58dc3da0efedc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UIHostingController](../uihostingcontroller.md)

# target(forAction:withSender:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency override dynamic func target(forAction action: Selector, withSender sender: Any?) -> Any?
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
- [rootView](rootview.md) — The root view of the SwiftUI view hierarchy managed by this view controller.

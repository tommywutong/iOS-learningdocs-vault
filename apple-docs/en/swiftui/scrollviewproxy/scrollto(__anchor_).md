---
title: 'scrollTo(_:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollviewproxy/scrollto(_:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollviewproxy/scrollto%28_%3Aanchor%3A%29.json'
content_hash: 'sha256:a4e741539a2717b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollViewProxy](../scrollviewproxy.md)

# scrollTo(_:anchor:)

<sub>Instance Method</sub>

Scans all scroll views contained by the proxy for the first with a child view with identifier `id`, and then scrolls to that view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func scrollTo<ID>(_ id: ID, anchor: UnitPoint? = nil) where ID : Hashable
```

## Parameters

- `id` — The identifier of a child view to scroll to.

- `anchor` — The alignment behavior of the scroll action.

## Discussion

If `anchor` is `nil`, this method finds the container of the identified view, and scrolls the minimum amount to make the identified view wholly visible.

If `anchor` is non-`nil`, it defines the points in the identified view and the scroll view to align. For example, setting `anchor` to [top](../unitpoint/top.md) aligns the top of the identified view to the top of the scroll view. Similarly, setting `anchor` to [bottom](../unitpoint/bottom.md) aligns the bottom of the identified view to the bottom of the scroll view, and so on.

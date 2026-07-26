---
title: 'onDrop(of:delegate:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+（27.0 起废弃）, iPadOS 13.4+（27.0 起废弃）, Mac Catalyst 13.4+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/ondrop(of:delegate:)-2vr9o'
source_url: 'https://developer.apple.com/documentation/swiftui/view/ondrop(of:delegate:)-2vr9o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/ondrop%28of%3Adelegate%3A%29-2vr9o.json'
content_hash: 'sha256:caeb912bdf5ac33b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onDrop(of:delegate:)

<sub>Instance Method</sub>

Defines the destination for a drag and drop operation with the same size and position as this view, with behavior controlled by the given delegate.

> [!warning] Deprecated
> Use [onDrop(of:delegate:)](<ondrop(of_delegate_)-6lin8.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func onDrop(of supportedTypes: [String], delegate: any DropDelegate) -> some View

```

## Parameters

- `supportedTypes` — The uniform type identifiers that describe the types of content this view can accept through drag and drop. If the drag and drop operation doesn’t contain any of the supported types, then this drop destination doesn’t activate and `isTargeted` doesn’t update.

- `delegate` — A type that conforms to the `DropDelegate` protocol. You have comprehensive control over drop behavior when you use a delegate.

## Return Value

A view that provides a drop destination for a drag operation of the specified types.

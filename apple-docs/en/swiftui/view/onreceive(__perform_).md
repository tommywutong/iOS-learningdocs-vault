---
title: 'onReceive(_:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/onreceive(_:perform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onreceive(_:perform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onreceive%28_%3Aperform%3A%29.json'
content_hash: 'sha256:f0f136bdd40fca5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onReceive(_:perform:)

<sub>Instance Method</sub>

Adds an action to perform when this view detects data emitted by the given publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func onReceive<P>(_ publisher: P, perform action: @escaping (P.Output) -> Void) -> some View where P : Publisher, P.Failure == Never

```

## Parameters

- `publisher` — The publisher to subscribe to.

- `action` — The action to perform when an event is emitted by `publisher`. The event emitted by publisher is passed as a parameter to `action`.

## Return Value

A view that triggers `action` when `publisher` emits an event.

## See Also

### Responding to data changes

- [onChange(of:initial:_:)](<onchange(of_initial___).md>) — Adds a modifier for this view that fires an action when a specific value changes.

---
title: 'recordingEditor(_:)'
framework: ScreenCaptureKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/recordingeditor(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/recordingeditor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/recordingeditor%28_%3A%29.json'
content_hash: 'sha256:b555805c797ca1ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# recordingEditor(_:)

<sub>Instance Method</sub>

Presents the recording editor for the given recording URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func recordingEditor(_ item: Binding<URL?>) -> some View

```

## Parameters

- `item` — A binding to an optional URL. Non-nil presents the editor; nil dismisses it.

## Discussion

When `item` is non-nil, the editor is presented for that URL. When the user dismisses, the framework sets `item` back to `nil`.

```swift
.recordingEditor($recordingURL)
```

## See Also

### Screen capture

- [recordingEditor(_:mode:)](<recordingeditor(__mode_).md>) — Presents the recording editor for the given recording URL with a specific mode. _(beta)_

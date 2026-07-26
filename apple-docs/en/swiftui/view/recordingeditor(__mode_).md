---
title: 'recordingEditor(_:mode:)'
framework: ScreenCaptureKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/recordingeditor(_:mode:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/recordingeditor(_:mode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/recordingeditor%28_%3Amode%3A%29.json'
content_hash: 'sha256:7418c78c82a1898d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# recordingEditor(_:mode:)

<sub>Instance Method</sub>

Presents the recording editor for the given recording URL with a specific mode.

<sub>tvOS</sub>

```swift
@MainActor @preconcurrency func recordingEditor(_ item: Binding<URL?>, mode: SCRecordingEditor.Mode) -> some View

```

## Parameters

- `item` — A binding to an optional URL. Non-nil presents the editor; nil dismisses it.

- `mode` — The editor mode (`.preview` or `.share`).

## See Also

### Screen capture

- [recordingEditor(_:)](<recordingeditor(__).md>) — Presents the recording editor for the given recording URL. _(beta)_

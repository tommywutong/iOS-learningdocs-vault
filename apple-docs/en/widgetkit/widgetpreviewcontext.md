---
title: WidgetPreviewContext
framework: WidgetKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 26.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/widgetkit/widgetpreviewcontext
source_url: 'https://developer.apple.com/documentation/widgetkit/widgetpreviewcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/widgetkit/widgetpreviewcontext.json'
content_hash: 'sha256:668e1a68031e800c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [WidgetKit](../widgetkit.md)

# WidgetPreviewContext

<sub>Structure</sub>

A specification for the context of a widget preview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct WidgetPreviewContext
```

## Overview

To create a preview for a widget in Xcode, use [previewContext(_:)](<../swiftui/view/previewcontext(__).md>) and pass `WidgetPreviewContext` initialized with the appropriate `WidgetFamily`.

```swift
struct Widget_Previews: PreviewProvider {
    static var previews: some View {
        Group {
            MyWidgetView()
                .previewContext(WidgetPreviewContext(family: .systemSmall))
        }
    }
}
```

## Relationships

- **Conforms To**: [PreviewContext](../swiftui/previewcontext.md)

## Topics

### Creating a Preview Context

- [init(family:)](<widgetpreviewcontext/init(family_).md>) — Creates a context for previewing a widget or a widget’s view.

## See Also

### Previews and debugging

- [Previewing widgets and Live Activities in Xcode](previewing-widgets-and-live-activities-in-xcode.md) — Use Xcode previews to iteratively develop, fine-tune, and troubleshoot widgets and Live Activities.
- [Preview macros](preview-macros.md) — Use Swift macros to create widget previews in Xcode.

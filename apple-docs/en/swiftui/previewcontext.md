---
title: PreviewContext
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewcontext
source_url: 'https://developer.apple.com/documentation/swiftui/previewcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewcontext.json'
content_hash: 'sha256:2e2586deaf64b923'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreviewContext

<sub>Protocol</sub>

A context type for use with a preview.

> [!warning] Deprecated
> Use [Preview(_:body:)](<preview(__body_).md>) with a WidgetKit timeline provider or entries instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PreviewContext
```

## Topics

### Accessing a preview context

- [subscript(_:)](<previewcontext/subscript(__).md>) — Returns the context’s value for a key, or a the key’s default value if the context doesn’t define a value for the key. _(deprecated)_

## See Also

### Setting a context

- [previewContext(_:)](<view/previewcontext(__).md>) — Declares a context for the preview. _(deprecated)_
- [PreviewContextKey](previewcontextkey.md) — A key type for a preview context. _(deprecated)_

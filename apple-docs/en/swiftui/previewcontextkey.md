---
title: PreviewContextKey
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/previewcontextkey
source_url: 'https://developer.apple.com/documentation/swiftui/previewcontextkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewcontextkey.json'
content_hash: 'sha256:493da69d12d26590'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreviewContextKey

<sub>Protocol</sub>

A key type for a preview context.

> [!warning] Deprecated
> Use [Preview(_:body:)](<preview(__body_).md>) with a WidgetKit timeline provider or entries instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PreviewContextKey
```

## Overview

The default value is `nil`.

## Topics

### Setting a default

- [defaultValue](previewcontextkey/defaultvalue.md) — The default value of the key. _(deprecated)_
- [Value](previewcontextkey/value.md) — The type of the value returned by the key. _(deprecated)_

## See Also

### Setting a context

- [previewContext(_:)](<view/previewcontext(__).md>) — Declares a context for the preview. _(deprecated)_
- [PreviewContext](previewcontext.md) — A context type for use with a preview. _(deprecated)_

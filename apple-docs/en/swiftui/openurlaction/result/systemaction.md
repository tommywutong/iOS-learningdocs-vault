---
title: systemAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openurlaction/result/systemaction
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/result/systemaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/result/systemaction.json'
content_hash: 'sha256:a792a21cb20a6b66'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [OpenURLAction](../../openurlaction.md) · [Result](../result.md)

# systemAction

<sub>Type Property</sub>

The handler asks the system to open the original URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let systemAction: OpenURLAction.Result
```

## Discussion

The action invokes its completion handler with a value that depends on the outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

- [discarded](discarded.md) — The handler discarded the URL.
- [handled](handled.md) — The handler opened the URL.
- [systemAction(_:)](<systemaction(__).md>) — The handler asks the system to open the modified URL.

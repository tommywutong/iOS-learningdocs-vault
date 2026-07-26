---
title: discarded
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openurlaction/result/discarded
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/result/discarded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/result/discarded.json'
content_hash: 'sha256:853abcfe2d2b3900'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [OpenURLAction](../../openurlaction.md) · [Result](../result.md)

# discarded

<sub>Type Property</sub>

The handler discarded the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let discarded: OpenURLAction.Result
```

## Discussion

The action invokes its completion handler with `false` when your handler returns this value.

## See Also

### Getting the results

- [handled](handled.md) — The handler opened the URL.
- [systemAction](systemaction.md) — The handler asks the system to open the original URL.
- [systemAction(_:)](<systemaction(__).md>) — The handler asks the system to open the modified URL.

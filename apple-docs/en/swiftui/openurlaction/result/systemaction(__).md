---
title: 'systemAction(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/openurlaction/result/systemaction(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/result/systemaction(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/result/systemaction%28_%3A%29.json'
content_hash: 'sha256:b594c4c84ca3a0ee'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [OpenURLAction](../../openurlaction.md) · [Result](../result.md)

# systemAction(_:)

<sub>Type Method</sub>

The handler asks the system to open the modified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func systemAction(_ url: URL) -> OpenURLAction.Result
```

## Parameters

- `url` — The URL that the handler asks the system to open.

## Discussion

The action invokes its completion handler with a value that depends on the outcome of the system’s attempt to open the URL.

## See Also

### Getting the results

- [discarded](discarded.md) — The handler discarded the URL.
- [handled](handled.md) — The handler opened the URL.
- [systemAction](systemaction.md) — The handler asks the system to open the original URL.

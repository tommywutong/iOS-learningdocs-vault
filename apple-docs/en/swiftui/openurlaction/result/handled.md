---
title: handled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openurlaction/result/handled
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/result/handled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/result/handled.json'
content_hash: 'sha256:4d38af86c52cb806'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [OpenURLAction](../../openurlaction.md) · [Result](../result.md)

# handled

<sub>Type Property</sub>

The handler opened the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let handled: OpenURLAction.Result
```

## Discussion

The action invokes its completion handler with `true` when your handler returns this value.

## See Also

### Getting the results

- [discarded](discarded.md) — The handler discarded the URL.
- [systemAction](systemaction.md) — The handler asks the system to open the original URL.
- [systemAction(_:)](<systemaction(__).md>) — The handler asks the system to open the modified URL.

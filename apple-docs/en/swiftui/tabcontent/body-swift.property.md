---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/tabcontent/body-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/tabcontent/body-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabcontent/body-swift.property.json'
content_hash: 'sha256:76686dd2dd52dba7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TabContent](../tabcontent.md)

# body

<sub>Instance Property</sub>

The value of this type’s nested content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@TabContentBuilder<Self.TabValue> @MainActor @preconcurrency var body: Self.Body { get }
```

## See Also

### Setting tab content

- [Body](body-swift.associatedtype.md) — The type of content representing the body of this content type.
- [TabValue](tabvalue.md) — The type used to drive selection for the containing tab view.

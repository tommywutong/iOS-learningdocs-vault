---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/searchscopeactivation/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/searchscopeactivation/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/searchscopeactivation/automatic.json'
content_hash: 'sha256:b20198352659eb0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SearchScopeActivation](../searchscopeactivation.md)

# automatic

<sub>Type Property</sub>

The automatic activation of the scope bar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var automatic: SearchScopeActivation { get }
```

## Discussion

By default, this is [onTextEntry](ontextentry.md) in iOS and [onSearchPresentation](onsearchpresentation.md) in macOS.

## See Also

### Getting search scope activiation types

- [onSearchPresentation](onsearchpresentation.md) — An activation where the system shows search scopes after presenting search and hides search scopes after search cancellation.
- [onTextEntry](ontextentry.md) — An activation where the system shows search scopes when typing begins in the search field and hides search scopes after search cancellation.

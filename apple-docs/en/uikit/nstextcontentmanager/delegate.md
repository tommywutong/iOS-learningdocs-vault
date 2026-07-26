---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentmanager/delegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentmanager/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentmanager/delegate.json'
content_hash: 'sha256:4e82920a09bf95f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentManager](../nstextcontentmanager.md)

# delegate

<sub>Instance Property</sub>

The delegate for the content manager object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any NSTextContentManagerDelegate)? { get set }
```

## See Also

### Customizing and validating text elements

- [NSTextContentManagerDelegate](../nstextcontentmanagerdelegate.md) — The optional methods that delegates of content manager objects implement for customizing or validating text elements.
- [EnumerationOptions](enumerationoptions.md) — Values that control the order in which the framework enumerates text elements.

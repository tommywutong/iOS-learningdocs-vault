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
doc_path: /documentation/uikit/nstextcontentstorage/delegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstorage/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstorage/delegate.json'
content_hash: 'sha256:c4b083ac396544e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextContentStorage](../nstextcontentstorage.md)

# delegate

<sub>Instance Property</sub>

The delegate for the content storage object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var delegate: (any NSTextContentStorageDelegate)? { get set }
```

## See Also

### Accessing paragraphs

- [NSTextContentStorageDelegate](../nstextcontentstoragedelegate.md) — The optional methods that delegates of content storage objects implement to handle content processing.

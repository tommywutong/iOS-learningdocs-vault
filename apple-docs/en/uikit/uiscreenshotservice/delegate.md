---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreenshotservice/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscreenshotservice/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreenshotservice/delegate.json'
content_hash: 'sha256:65dc3a19f70f0f9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreenshotService](../uiscreenshotservice.md)

# delegate

<sub>Instance Property</sub>

The custom object you use to provide PDF data for a screenshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
weak var delegate: (any UIScreenshotServiceDelegate)? { get set }
```

## Discussion

Assign an object to this property early in the life cycle of your window scene. The object must conform to the [UIScreenshotServiceDelegate](../uiscreenshotservicedelegate.md) protocol.

## See Also

### Responding to screenshot requests

- [UIScreenshotServiceDelegate](../uiscreenshotservicedelegate.md) — Methods you use to generate PDF data that accompanies a user-requested screenshot.

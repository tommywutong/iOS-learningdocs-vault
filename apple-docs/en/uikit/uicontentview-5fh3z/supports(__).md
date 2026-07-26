---
title: 'supports(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontentview-5fh3z/supports(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontentview-5fh3z/supports(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentview-5fh3z/supports%28_%3A%29.json'
content_hash: 'sha256:bd05ae1bb2667b6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentView](../uicontentview-5fh3z.md)

# supports(_:)

<sub>Instance Method</sub>

Determines whether the view is compatible with the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor func supports(_ configuration: any UIContentConfiguration) -> Bool
```

## Parameters

- `configuration` — The new configuration to test for compatibility.

## Return Value

[true](../../swift/true.md) if the view supports this configuration being set to its [configuration](configuration.md) property and is capable of updating itself for the configuration; otherwise, [false](../../swift/false.md).

## Discussion

The default implementation assumes the view is compatible with configuration types that match the type of the view’s existing configuration.

## Default Implementations

### UIContentView Implementations

- [supports(_:)](<supports(__)-q5rd.md>)

---
title: 'resolvedValue(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisheetpresentationcontroller/detent/resolvedvalue(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/detent/resolvedvalue(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/detent/resolvedvalue%28in%3A%29.json'
content_hash: 'sha256:395e738960f72628'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISheetPresentationController](../../uisheetpresentationcontroller.md) · [Detent](../detent.md)

# resolvedValue(in:)

<sub>Instance Method</sub>

Resolves a detent to its value.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func resolvedValue(in context: any UISheetPresentationControllerDetentResolutionContext) -> CGFloat?
```

## Parameters

- `context` — A context for resolving custom detent values. This context is available in the `resolver` closure of [custom(identifier:resolver:)](<custom(identifier_resolver_).md>).

## Return Value

A [CGFloat](../../../corefoundation/cgfloat-swift.struct.md) that represents the value of the detent, or `nil` if the detent is inactive in the provided context.

## Discussion

You can use this method to get the values of the system [UISheetPresentationControllerDetentIdentifierMedium](identifier-swift.struct/medium.md) and [UISheetPresentationControllerDetentIdentifierLarge](identifier-swift.struct/large.md) detents, or the value of a custom detent. Use this method inside [custom(identifier:resolver:)](<custom(identifier_resolver_).md>) to construct a custom detent according to the values of known detents.

## See Also

### Creating a custom detent

- [custom(identifier:resolver:)](<custom(identifier_resolver_).md>) — Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [UISheetPresentationControllerDetentResolutionContext](../../uisheetpresentationcontrollerdetentresolutioncontext.md) — A context for resolving custom detent values.

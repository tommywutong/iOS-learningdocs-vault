---
title: 'resolvedValueInContext:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisheetpresentationcontrollerdetent/resolvedvalueincontext:'
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontrollerdetent/resolvedvalueincontext:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontrollerdetent/resolvedvalueincontext%3A.json'
content_hash: 'sha256:77adf7acea94c184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [Detent](../uisheetpresentationcontroller/detent.md)

# resolvedValueInContext:

<sub>Instance Method</sub>

Resolves a detent to its value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (CGFloat) resolvedValueInContext:(id<UISheetPresentationControllerDetentResolutionContext>) context;
```

## Parameters

- `context` — A context for resolving custom detent values. This context is available in the `resolver` block of [customDetentWithIdentifier:resolver:](customdetentwithidentifier_resolver_.md).

## Return Value

A [CGFloat](../../corefoundation/cgfloat-swift.struct.md) that represents the value of the detent, or [UISheetPresentationControllerDetentInactive](../uisheetpresentationcontrollerdetentinactive.md) if the detent is inactive in the provided context.

## Discussion

You can use this method to get the values of the system [UISheetPresentationControllerDetentIdentifierMedium](../uisheetpresentationcontroller/detent/identifier-swift.struct/medium.md) and [UISheetPresentationControllerDetentIdentifierLarge](../uisheetpresentationcontroller/detent/identifier-swift.struct/large.md) detents, or the value of a custom detent. Use this method inside [customDetentWithIdentifier:resolver:](customdetentwithidentifier_resolver_.md) to construct a custom detent according to the values of known detents.

## See Also

### Creating a custom detent

- [customDetentWithIdentifier:resolver:](customdetentwithidentifier_resolver_.md) — Creates a custom detent for a sheet by computing its value according to the properties of the provided context.
- [UISheetPresentationControllerDetentResolutionContext](../uisheetpresentationcontrollerdetentresolutioncontext.md) — A context for resolving custom detent values.
- [UISheetPresentationControllerDetentInactive](../uisheetpresentationcontrollerdetentinactive.md) — A value that represents an inactive detent.

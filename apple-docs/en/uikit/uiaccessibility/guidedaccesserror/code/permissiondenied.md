---
title: UIAccessibility.GuidedAccessError.Code.permissionDenied
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccesserror/code/permissiondenied
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror/code/permissiondenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccesserror/code/permissiondenied.json'
content_hash: 'sha256:ee8265d8e2286d8c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIAccessibility](../../../uiaccessibility.md) · [GuidedAccessError](../../guidedaccesserror.md) · [Code](../code.md)

# UIAccessibility.GuidedAccessError.Code.permissionDenied

<sub>Case</sub>

An error that indicates the app isn’t authorized to perform the requested action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case permissionDenied
```

## Discussion

For example, this error might indicate that your app is requesting a configuration change but isn’t locked into Single App Mode through a configuration profile.

## See Also

### Errors

- [UIGuidedAccessErrorFailed](failed.md) — An error that indicates a failure for an unspecified reason.

---
title: permissionDenied
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccesserror/permissiondenied
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror/permissiondenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccesserror/permissiondenied.json'
content_hash: 'sha256:713441ec24a01b1a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIAccessibility](../../uiaccessibility.md) · [GuidedAccessError](../guidedaccesserror.md)

# permissionDenied

<sub>Type Property</sub>

An error that indicates the app isn’t authorized to perform the requested action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var permissionDenied: UIAccessibility.GuidedAccessError.Code { get }
```

## Discussion

For example, this error might indicate that your app is requesting a configuration change but isn’t locked into Single App Mode through a configuration profile.

## See Also

### Accessing error codes

- [failed](failed.md) — An error that indicates a failure for an unspecified reason.
- [Code](code.md) — Error codes for Guided Access.

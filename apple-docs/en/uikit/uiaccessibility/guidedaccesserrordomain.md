---
title: guidedAccessErrorDomain
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, tvOS 12.2+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccesserrordomain
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccesserrordomain.json'
content_hash: 'sha256:ca534caa21f549fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# guidedAccessErrorDomain

<sub>Type Property</sub>

A string that identifies the Guided Access error domain.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let guidedAccessErrorDomain: String
```

## See Also

### Guided Access

- [UIAccessibilityIsGuidedAccessEnabled](isguidedaccessenabled.md) — A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIGuidedAccessConfigureAccessibilityFeatures](<configureforguidedaccess(features_enabled_completionhandler_).md>) — Enables or disables the specified accessibility features while using Guided Access.
- [UIGuidedAccessRestrictionStateForIdentifier](<guidedaccessrestrictionstate(foridentifier_).md>) — Returns the restriction state for the specified guided access restriction.
- [GuidedAccessRestrictionState](guidedaccessrestrictionstate.md) — Constants that describe the state of a restriction, either allow or deny.
- [GuidedAccessError](guidedaccesserror.md) — A Guided Access error.

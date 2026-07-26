---
title: UIAccessibility.GuidedAccessError
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccesserror
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccesserror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccesserror.json'
content_hash: 'sha256:206c6431062cf7a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.GuidedAccessError

<sub>Structure</sub>

A Guided Access error.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct GuidedAccessError
```

## Relationships

- **Conforms To**: [CustomNSError](../../foundation/customnserror.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing error codes

- [permissionDenied](guidedaccesserror/permissiondenied.md) — An error that indicates the app isn’t authorized to perform the requested action.
- [failed](guidedaccesserror/failed.md) — An error that indicates a failure for an unspecified reason.
- [Code](guidedaccesserror/code.md) — Error codes for Guided Access.

### Getting error information

- [errorDomain](guidedaccesserror/errordomain.md) — The Guided Access error domain.

## See Also

### Guided Access

- [UIAccessibilityIsGuidedAccessEnabled](isguidedaccessenabled.md) — A Boolean value that indicates whether the Guided Access setting is in an enabled state.
- [UIAccessibilityGuidedAccessStatusDidChangeNotification](guidedaccessstatusdidchangenotification.md) — A notification that indicates when a Guided Access session starts or ends.
- [UIAccessibilityRequestGuidedAccessSession](<requestguidedaccesssession(enabled_completionhandler_).md>) — Transitions the app to or from Single App mode asynchronously.
- [UIGuidedAccessConfigureAccessibilityFeatures](<configureforguidedaccess(features_enabled_completionhandler_).md>) — Enables or disables the specified accessibility features while using Guided Access.
- [UIGuidedAccessRestrictionStateForIdentifier](<guidedaccessrestrictionstate(foridentifier_).md>) — Returns the restriction state for the specified guided access restriction.
- [GuidedAccessRestrictionState](guidedaccessrestrictionstate.md) — Constants that describe the state of a restriction, either allow or deny.
- [UIGuidedAccessErrorDomain](guidedaccesserrordomain.md) — A string that identifies the Guided Access error domain.

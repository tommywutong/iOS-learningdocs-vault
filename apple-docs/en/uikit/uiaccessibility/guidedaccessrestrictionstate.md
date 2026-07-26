---
title: UIAccessibility.GuidedAccessRestrictionState
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibility/guidedaccessrestrictionstate
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibility/guidedaccessrestrictionstate.json'
content_hash: 'sha256:9eefed5afc7debdd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAccessibility](../uiaccessibility.md)

# UIAccessibility.GuidedAccessRestrictionState

<sub>Enumeration</sub>

Constants that describe the state of a restriction, either allow or deny.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum GuidedAccessRestrictionState
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIGuidedAccessRestrictionStateAllow](guidedaccessrestrictionstate/allow.md) — The app should allow the user to perform the action controlled by the restriction.
- [UIGuidedAccessRestrictionStateDeny](guidedaccessrestrictionstate/deny.md) — The app should deny the user from performing the action controlled by the restriction.

### Initializers

- [init(rawValue:)](<guidedaccessrestrictionstate/init(rawvalue_).md>)

## See Also

### Implementing restrictions

- [- guidedAccessRestrictionWithIdentifier:didChangeState:](<../uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier_didchange_).md>) — Tells the delegate that the restriction associated with the identifier has changed state.

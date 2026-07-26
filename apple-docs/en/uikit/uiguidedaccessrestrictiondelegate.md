---
title: UIGuidedAccessRestrictionDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiguidedaccessrestrictiondelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiguidedaccessrestrictiondelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiguidedaccessrestrictiondelegate.json'
content_hash: 'sha256:2d5f98cb8f752951'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGuidedAccessRestrictionDelegate

<sub>Protocol</sub>

A set of methods you use to add custom restrictions for the Guided Access feature in iOS.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIGuidedAccessRestrictionDelegate : NSObjectProtocol
```

## Overview

Custom restrictions are represented by string identifiers provided by the developer in the [guidedAccessRestrictionIdentifiers](uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.md) method. Each identifier represents an operation in the app that the developer wishes to allow users to restrict using Guided Access. The default for all operations is allow. Users can deny operations using the normal Guided Access user interface. See [http://support.apple.com/kb/HT5509](http://support.apple.com/kb/HT5509) for a description of how to enable and configure Guided Access on iOS.

Apps describe their custom restrictions by implementing the [- textForGuidedAccessRestrictionWithIdentifier:](<uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier_).md>) and [- detailTextForGuidedAccessRestrictionWithIdentifier:](<uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier_).md>) methods to return appropriate localized, human-readable strings.

For example, a photo editing app might allow users to disable deleting photos. The app would return an identifier representing this restriction in its [guidedAccessRestrictionIdentifiers](uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.md) method. It would also implement [- textForGuidedAccessRestrictionWithIdentifier:](<uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier_).md>) to provide a human-readable description of the restriction. Finally, the app would implement [- guidedAccessRestrictionWithIdentifier:didChangeState:](<uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier_didchange_).md>) to notice when a user indicates that they want to enable the restriction. When the app sees the state change to “deny”, it would configure itself to prevent the deletion of photos by any means. Similarly, when the app sees the state change to “allow”, it would configure itself to allow photo deletion.

Apps can use the [UIGuidedAccessRestrictionStateForIdentifier](<uiaccessibility/guidedaccessrestrictionstate(foridentifier_).md>) function to check the state of a restriction at any time.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying custom Guided Access restrictions

- [guidedAccessRestrictionIdentifiers](uiguidedaccessrestrictiondelegate/guidedaccessrestrictionidentifiers.md) — An array of strings identifying custom restrictions.
- [- textForGuidedAccessRestrictionWithIdentifier:](<uiguidedaccessrestrictiondelegate/textforguidedaccessrestriction(withidentifier_).md>) — Provides a succinct description of the restriction for the specified identifier.
- [- detailTextForGuidedAccessRestrictionWithIdentifier:](<uiguidedaccessrestrictiondelegate/detailtextforguidedaccessrestriction(withidentifier_).md>) — Provides more detailed information about the restriction for the specified identifier.

### Implementing restrictions

- [- guidedAccessRestrictionWithIdentifier:didChangeState:](<uiguidedaccessrestrictiondelegate/guidedaccessrestriction(withidentifier_didchange_).md>) — Tells the delegate that the restriction associated with the identifier has changed state.
- [GuidedAccessRestrictionState](uiaccessibility/guidedaccessrestrictionstate.md) — Constants that describe the state of a restriction, either allow or deny.

## See Also

### Guided Access

- [UIGuidedAccessRestrictionStateForIdentifier](<uiaccessibility/guidedaccessrestrictionstate(foridentifier_).md>) — Returns the restriction state for the specified guided access restriction.

---
title: alwaysAuthorizationDenied
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clservicesessiondiagnostic/alwaysauthorizationdenied
source_url: 'https://developer.apple.com/documentation/corelocation/clservicesessiondiagnostic/alwaysauthorizationdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clservicesessiondiagnostic/alwaysauthorizationdenied.json'
content_hash: 'sha256:27be065083f429d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLServiceSessionDiagnostic](../clservicesessiondiagnostic.md)

# alwaysAuthorizationDenied

<sub>Instance Property</sub>

A Boolean value that indicates someone has not granted the always authorization to your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) BOOL alwaysAuthorizationDenied;
```

## Discussion

This property is `true` in the `CLServiceSessionDiagnostic` of a `CLServiceSession` created with an [CLServiceSession.AuthorizationRequirement.always](../clservicesession-pt7n/authorizationrequirement/always.md)  goal if someone denies the app that authorization; otherwise `false`.

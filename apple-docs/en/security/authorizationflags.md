---
title: AuthorizationFlags
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationflags
source_url: 'https://developer.apple.com/documentation/security/authorizationflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationflags.json'
content_hash: 'sha256:befe7cf24291c064'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationFlags

<sub>Structure</sub>

The flags used to specify authorization options.

<sub>Mac Catalyst, macOS</sub>

```swift
struct AuthorizationFlags
```

## Overview

These flags instruct the Security Server how to proceed with the function in which you pass them. You bitwise `OR` them together to specify more than one at a time. Set all unused bits to `0` to allow for future expansion.

Use these flags in calls to the [AuthorizationCreate](<authorizationcreate(________).md>), [AuthorizationFree](<authorizationfree(____).md>), [AuthorizationCopyRights](<authorizationcopyrights(__________).md>), and [AuthorizationCopyRightsAsync](<authorizationcopyrightsasync(__________).md>) functions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<authorizationflags/init(rawvalue_).md>) — Initializes an authorization flags structure.

### Type Properties

- [kAuthorizationFlagInteractionAllowed](authorizationflags/interactionallowed.md) — A flag that permits user interaction as needed.
- [kAuthorizationFlagExtendRights](authorizationflags/extendrights.md) — A flag that permits the Security Server to attempt to grant the rights requested.
- [kAuthorizationFlagPartialRights](authorizationflags/partialrights.md) — A flag that permits the Security Server to grant rights on an individual basis.
- [kAuthorizationFlagDestroyRights](authorizationflags/destroyrights.md) — A flag that instructs the Security Server to revoke authorization.
- [kAuthorizationFlagPreAuthorize](authorizationflags/preauthorize.md) — A flag that instructs the Security Server to preauthorize the rights requested.
- [kAuthorizationFlagNoData](authorizationflags/nodata.md) — Private flag. Do not use.
- [kAuthorizationFlagSkipInternalAuth](authorizationflags/skipinternalauth.md)

---
title: 'init(authorization:fullAccuracyPurposeKey:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clservicesession-pt7n/init(authorization:fullaccuracypurposekey:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clservicesession-pt7n/init(authorization:fullaccuracypurposekey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clservicesession-pt7n/init%28authorization%3Afullaccuracypurposekey%3A%29.json'
content_hash: 'sha256:2e1b6945e540bd0c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLServiceSession](../clservicesession-pt7n.md)

# init(authorization:fullAccuracyPurposeKey:)

<sub>Initializer</sub>

Creates a services session by using the authorization mode and purpose key you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(authorization: CLServiceSession.AuthorizationRequirement, fullAccuracyPurposeKey: String)
```

## Discussion

Passing `.none` for authorization requirement and omitting any accuracy requirement creates a session object that doesn’t request a person’s authorization to access Location Services, but the object meets a requested Explicit Service Session requirement if the framework has already has authorization.

Passing an authorization requirement other than `.none` causes Location Services to request a person’s permission for the corresponding level of authorization when possible — for example, when your app is in the foreground, when a person hasn’t denied an earlier authorization request, or if parental control settings don’t restrict changes to the ability to request a person’s location.

## See Also

### Creating a session

- [init(authorization:)](<init(authorization_).md>) — Creates a services session by using the authorization mode you specify.
- [AuthorizationRequirement](authorizationrequirement.md) — Values that describe when the service session needs to request authorization.

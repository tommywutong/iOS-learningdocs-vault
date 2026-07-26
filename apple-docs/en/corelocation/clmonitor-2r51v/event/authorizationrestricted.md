---
title: authorizationRestricted
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/event/authorizationrestricted
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/authorizationrestricted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/event/authorizationrestricted.json'
content_hash: 'sha256:08f6637f6d79bba3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLMonitor](../../clmonitor-2r51v.md) · [Event](../event.md)

# authorizationRestricted

<sub>Instance Property</sub>

A Boolean value that indicates whether the app can make authorization changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var authorizationRestricted: Bool { get }
```

## See Also

### Event states

- [accuracyLimited](accuracylimited.md) — A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDenied](authorizationdenied.md) — A Boolean value that indicates whether the app has local authorization.
- [authorizationDeniedGlobally](authorizationdeniedglobally.md) — A Boolean value that indicates whether the app has system-wide authorization.
- [authorizationRequestInProgress](authorizationrequestinprogress.md)
- [conditionLimitExceeded](conditionlimitexceeded.md) — A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [conditionUnsupported](conditionunsupported.md) — A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [insufficientlyInUse](insufficientlyinuse.md) — A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [persistenceUnavailable](persistenceunavailable.md) — A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](servicesessionrequired.md)

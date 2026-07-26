---
title: authorizationDenied
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/event/authorizationdenied
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/authorizationdenied'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/event/authorizationdenied.json'
content_hash: 'sha256:4e425526fb9621d0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLMonitor](../../clmonitor-2r51v.md) · [Event](../event.md)

# authorizationDenied

<sub>Instance Property</sub>

A Boolean value that indicates whether the app has local authorization.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var authorizationDenied: Bool { get }
```

## Discussion

If this property is [true](../../../swift/true.md), then the app isn’t receiving location updates because it’s denied local authorization.

## See Also

### Event states

- [accuracyLimited](accuracylimited.md) — A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDeniedGlobally](authorizationdeniedglobally.md) — A Boolean value that indicates whether the app has system-wide authorization.
- [authorizationRequestInProgress](authorizationrequestinprogress.md)
- [authorizationRestricted](authorizationrestricted.md) — A Boolean value that indicates whether the app can make authorization changes.
- [conditionLimitExceeded](conditionlimitexceeded.md) — A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [conditionUnsupported](conditionunsupported.md) — A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [insufficientlyInUse](insufficientlyinuse.md) — A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [persistenceUnavailable](persistenceunavailable.md) — A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](servicesessionrequired.md)

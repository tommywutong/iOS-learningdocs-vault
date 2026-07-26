---
title: insufficientlyInUse
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/event/insufficientlyinuse
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/insufficientlyinuse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/event/insufficientlyinuse.json'
content_hash: 'sha256:d1ca52f272b3df89'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLMonitor](../../clmonitor-2r51v.md) · [Event](../event.md)

# insufficientlyInUse

<sub>Instance Property</sub>

A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var insufficientlyInUse: Bool { get }
```

## Discussion

If this property is [true](../../../swift/true.md), then the app isn’t receiving location updates because it’s insufficiently in use.

## See Also

### Event states

- [accuracyLimited](accuracylimited.md) — A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDenied](authorizationdenied.md) — A Boolean value that indicates whether the app has local authorization.
- [authorizationDeniedGlobally](authorizationdeniedglobally.md) — A Boolean value that indicates whether the app has system-wide authorization.
- [authorizationRequestInProgress](authorizationrequestinprogress.md)
- [authorizationRestricted](authorizationrestricted.md) — A Boolean value that indicates whether the app can make authorization changes.
- [conditionLimitExceeded](conditionlimitexceeded.md) — A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [conditionUnsupported](conditionunsupported.md) — A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [persistenceUnavailable](persistenceunavailable.md) — A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](servicesessionrequired.md)

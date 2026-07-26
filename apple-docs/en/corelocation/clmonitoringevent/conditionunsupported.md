---
title: conditionUnsupported
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringevent/conditionunsupported
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringevent/conditionunsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringevent/conditionunsupported.json'
content_hash: 'sha256:cd8ecf8482b83c2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringEvent](../clmonitoringevent.md)

# conditionUnsupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the app receives location updates based on the supported condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) BOOL conditionUnsupported;
```

## Discussion

If this property is [true](../../swift/true.md), then the app isn’t receiving location updates because it’s monitoring a type of condition that isn’t supported.

## See Also

### Event states

- [accuracyLimited](accuracylimited.md) — A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDenied](authorizationdenied.md) — A Boolean value that indicates whether the app has local authorization.
- [authorizationDeniedGlobally](authorizationdeniedglobally.md) — A Boolean value that indicates whether the app has system-wide authorization.
- [authorizationRequestInProgress](authorizationrequestinprogress.md)
- [authorizationRestricted](authorizationrestricted.md) — A Boolean value that indicates whether the app can make authorization changes.
- [conditionLimitExceeded](conditionlimitexceeded.md) — A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [insufficientlyInUse](insufficientlyinuse.md) — A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [persistenceUnavailable](persistenceunavailable.md) — A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](servicesessionrequired.md)

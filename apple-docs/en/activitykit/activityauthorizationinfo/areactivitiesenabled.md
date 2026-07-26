---
title: areActivitiesEnabled
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityauthorizationinfo/areactivitiesenabled
source_url: 'https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/areactivitiesenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityauthorizationinfo/areactivitiesenabled.json'
content_hash: 'sha256:9b70a7bf87101686'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAuthorizationInfo](../activityauthorizationinfo.md)

# areActivitiesEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether your app can start a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final var areActivitiesEnabled: Bool { get }
```

## See Also

### Observing Live Activity permission changes

- [activityEnablementUpdates](activityenablementupdates-swift.property.md) — An asynchronous sequence you use to observe whether your app can start a Live Activity.
- [ActivityEnablementUpdates](activityenablementupdates-swift.struct.md) — A structure that offers functionality to observe whether your app can start a Live Activity.
- [init()](<init().md>) — Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.

---
title: activityEnablementUpdates
framework: ActivityKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.property
source_url: 'https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityauthorizationinfo/activityenablementupdates-swift.property.json'
content_hash: 'sha256:a300fba029212221'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAuthorizationInfo](../activityauthorizationinfo.md)

# activityEnablementUpdates

<sub>Instance Property</sub>

An asynchronous sequence you use to observe whether your app can start a Live Activity.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
final let activityEnablementUpdates: ActivityAuthorizationInfo.ActivityEnablementUpdates
```

## See Also

### Observing Live Activity permission changes

- [areActivitiesEnabled](areactivitiesenabled.md) — A Boolean value that indicates whether your app can start a Live Activity.
- [ActivityEnablementUpdates](activityenablementupdates-swift.struct.md) — A structure that offers functionality to observe whether your app can start a Live Activity.
- [init()](<init().md>) — Creates an object you use to observe user authorizations for starting Live Activities and updating them with ActivityKit push notifications.

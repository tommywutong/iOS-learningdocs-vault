---
title: ActivityAuthorizationError.targetMaximumExceeded
framework: ActivityKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.1+, iPadOS 16.1+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/activitykit/activityauthorizationerror/targetmaximumexceeded
source_url: 'https://developer.apple.com/documentation/activitykit/activityauthorizationerror/targetmaximumexceeded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/activitykit/activityauthorizationerror/targetmaximumexceeded.json'
content_hash: 'sha256:318cd7196b2eb126'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [ActivityKit](../../activitykit.md) · [ActivityAuthorizationError](../activityauthorizationerror.md)

# ActivityAuthorizationError.targetMaximumExceeded

<sub>Case</sub>

The app has already started the maximum number of concurrent Live Activities.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case targetMaximumExceeded
```

## See Also

### Error codes

- [ActivityAuthorizationError.attributesTooLarge](attributestoolarge.md) — The provided Live Activity attributes exceeded the maximum size of 4KB.
- [ActivityAuthorizationError.denied](denied.md) — A person deactivated Live Activities in Settings.
- [ActivityAuthorizationError.globalMaximumExceeded](globalmaximumexceeded.md) — The device reached the maximum number of ongoing Live Activities.
- [ActivityAuthorizationError.malformedActivityIdentifier](malformedactivityidentifier.md) — The provided activity identifier is malformed.
- [ActivityAuthorizationError.missingProcessIdentifier](missingprocessidentifier.md) — The process that tried to start the Live Activity is missing a process identifier.
- [ActivityAuthorizationError.persistenceFailure](persistencefailure.md) — The system couldn’t persist the Live Activity.
- [ActivityAuthorizationError.reconnectNotPermitted](reconnectnotpermitted.md) — The process that tried to recreate the Live Activity is not the process that originally created the Live Activity.
- [ActivityAuthorizationError.unentitled](unentitled.md) — The app doesn’t have the required entitlement to start a Live Activity.
- [ActivityAuthorizationError.unsupported](unsupported.md) — The device doesn’t support Live Activities.
- [ActivityAuthorizationError.unsupportedTarget](unsupportedtarget.md) — The app doesn’t have the required entitlement to start a Live Activities.
- [ActivityAuthorizationError.visibility](visibility.md) — The app tried to start the Live Activity while it was in the background.

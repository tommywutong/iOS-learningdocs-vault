---
title: Suspending authorization requests
framework: Core Location
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/suspending-authorization-requests
source_url: 'https://developer.apple.com/documentation/corelocation/suspending-authorization-requests'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/suspending-authorization-requests.json'
content_hash: 'sha256:d582e688a9d429df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# Suspending authorization requests

<sub>Article</sub>

Defer the system’s authorization request dialog until your app is ready.

## Overview

If your app has an onboarding flow that includes obtaining location updates, you may want to defer the Core Location’s request for authorization from the user. You can inhibit the auto-prompting in your app by creating a [CLServiceSession](clservicesession-pt7n.md) at a convenient time in your app, then iterating over its diagnostics property to determine the level of authorization the person using your app selects. The following code snippet demonstrates how to defer the prompting.

```swift
func doPromptingFlow() async {
    await showHelloPrompt()

    // Obtain a session. This causes Core Location to display the authorization prompt.
    let session = CLServiceSession.session(authorization: .whenInUse)

    // Wait for interaction with the prompot to complete (successfully or with denial).
    for try await diagnostic in session.diagnostics {
        if !diagnostic.authorizationRequestInProgress {
            // A denial occurred.
            break
        }
    }

    await doFurtherWork()
}
```

Add the `CLRequireExplicitServiceSession` property to your app’s Info.plist file to opt into this control behavior.

## See Also

### Authorization

- [Requesting authorization to use location services](requesting-authorization-to-use-location-services.md) — Obtain authorization to use location services and manage changes to your app’s authorization status.
- [CLAuthorizationStatus](clauthorizationstatus.md) — Constants that indicate the app’s authorization to use location services.
- [CLAccuracyAuthorization](claccuracyauthorization.md) — Constants that indicate the level of location accuracy the app has authorization to use.
- [NSLocationAlwaysAndWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](../bundleresources/information-property-list/nslocationwheninuseusagedescription.md) — A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationUsageDescription](../bundleresources/information-property-list/nslocationusagedescription.md) — A message that tells people why the app is requesting access to their location information. _(deprecated)_
- [NSLocationDefaultAccuracyReduced](../bundleresources/information-property-list/nslocationdefaultaccuracyreduced.md) — A Boolean value that indicates whether the app requests reduced location accuracy by default.
- [NSLocationAlwaysUsageDescription](../bundleresources/information-property-list/nslocationalwaysusagedescription.md) — A message that tells people why the app is requesting access to their location at all times. _(deprecated)_

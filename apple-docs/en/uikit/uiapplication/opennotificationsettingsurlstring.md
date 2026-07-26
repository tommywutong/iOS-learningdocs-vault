---
title: openNotificationSettingsURLString
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/opennotificationsettingsurlstring
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/opennotificationsettingsurlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/opennotificationsettingsurlstring.json'
content_hash: 'sha256:58d606e39e1d3d82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# openNotificationSettingsURLString

<sub>Type Property</sub>

The URL string you use to deep link to your app’s notification settings in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let openNotificationSettingsURLString: String
```

## Discussion

Create a URL from this value and pass it to the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method to launch the Settings app and display your app’s notification settings, if it has any.

```swift
// Create the URL that deep links to your app's notification settings.
if let url = URL(string: UIApplication.openNotificationSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

## See Also

### Deep linking to custom settings

- [UIApplicationOpenSettingsURLString](opensettingsurlstring.md) — The URL string you use to deep link to your app’s custom settings in the Settings app.
- [UIApplicationOpenNotificationSettingsURLString](../uiapplicationopennotificationsettingsurlstring.md) — A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app. _(deprecated)_
- [UIApplicationOpenDefaultApplicationsSettingsURLString](opendefaultapplicationssettingsurlstring.md) — The URL string used to select a default app in the Settings app.

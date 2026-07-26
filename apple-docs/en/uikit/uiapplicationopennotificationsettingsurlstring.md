---
title: UIApplicationOpenNotificationSettingsURLString
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 15.4+（16.0 起废弃）, iPadOS 15.4+（16.0 起废弃）, Mac Catalyst 15.4+（16.0 起废弃）, tvOS 15.4+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 8.5+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiapplicationopennotificationsettingsurlstring
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationopennotificationsettingsurlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationopennotificationsettingsurlstring.json'
content_hash: 'sha256:dc4e51c9a93399e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationOpenNotificationSettingsURLString

<sub>Global Variable</sub>

A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app.

> [!warning] Deprecated
> In Swift, use [openNotificationSettingsURLString](uiapplication/opennotificationsettingsurlstring.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated let UIApplicationOpenNotificationSettingsURLString: String
```

## Discussion

Create a URL from this value and pass it to the [- openURL:options:completionHandler:](<uiapplication/open(__options_completionhandler_).md>) method to launch the Settings app and display your app’s notification settings, if it has any.

```objc
// Create the URL that deep links to your app's notification settings.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenNotificationSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

## See Also

### Deep linking to custom settings

- [UIApplicationOpenSettingsURLString](uiapplication/opensettingsurlstring.md) — The URL string you use to deep link to your app’s custom settings in the Settings app.
- [openNotificationSettingsURLString](uiapplication/opennotificationsettingsurlstring.md) — The URL string you use to deep link to your app’s notification settings in the Settings app.
- [UIApplicationOpenDefaultApplicationsSettingsURLString](uiapplication/opendefaultapplicationssettingsurlstring.md) — The URL string used to select a default app in the Settings app.

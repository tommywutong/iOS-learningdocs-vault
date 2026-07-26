---
title: openSettingsURLString
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/opensettingsurlstring
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/opensettingsurlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/opensettingsurlstring.json'
content_hash: 'sha256:95057649929ace63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# openSettingsURLString

<sub>Type Property</sub>

The URL string you use to deep link to your app’s custom settings in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let openSettingsURLString: String
```

## Discussion

Create a URL from this value and pass it to the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method to launch the Settings app and display your app’s custom settings, if it has any.

**Swift**

```swift
// Create the URL that deep links to your app's custom settings.
if let url = URL(string: UIApplication.openSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

**Objective-C**

```objc
// Create the URL that deep links to your app's custom settings.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/app-architecture/settings/).

## See Also

### Deep linking to custom settings

- [openNotificationSettingsURLString](opennotificationsettingsurlstring.md) — The URL string you use to deep link to your app’s notification settings in the Settings app.
- [UIApplicationOpenNotificationSettingsURLString](../uiapplicationopennotificationsettingsurlstring.md) — A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app. _(deprecated)_
- [UIApplicationOpenDefaultApplicationsSettingsURLString](opendefaultapplicationssettingsurlstring.md) — The URL string used to select a default app in the Settings app.

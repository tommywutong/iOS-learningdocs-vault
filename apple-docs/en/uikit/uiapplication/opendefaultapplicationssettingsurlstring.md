---
title: openDefaultApplicationsSettingsURLString
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.3+, iPadOS 18.3+, Mac Catalyst 18.3+, tvOS 18.3+, visionOS 2.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/opendefaultapplicationssettingsurlstring
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/opendefaultapplicationssettingsurlstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/opendefaultapplicationssettingsurlstring.json'
content_hash: 'sha256:db9c05069962ccac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# openDefaultApplicationsSettingsURLString

<sub>Type Property</sub>

The URL string used to select a default app in the Settings app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let openDefaultApplicationsSettingsURLString: String
```

## Discussion

Create a URL from this value and pass it to the [- openURL:options:completionHandler:](<open(__options_completionhandler_).md>) method to launch the Settings app and display your app’s custom settings, if it has any:

**Swift**

```swift
// Create the URL that links to the Settings app for default app selection.
if let url = URL(string: UIApplication.openDefaultApplicationsSettingsURLString) {
    // Ask the system to open that URL.
    await UIApplication.shared.open(url)
}
```

**Objective-C**

```objc
// Create the URL that links to the Settings app for default app selection.
NSURL *url = [[NSURL alloc] initWithString:UIApplicationOpenDefaultApplicationsSettingsURLString];
// Ask the system to open that URL.
[[UIApplication sharedApplication] openURL:url
                                   options:@{}
                         completionHandler:nil];
```

For design guidance, see Human Interface Guidelines \> [Settings](https://developer.apple.com/design/human-interface-guidelines/).

## See Also

### Deep linking to custom settings

- [UIApplicationOpenSettingsURLString](opensettingsurlstring.md) — The URL string you use to deep link to your app’s custom settings in the Settings app.
- [openNotificationSettingsURLString](opennotificationsettingsurlstring.md) — The URL string you use to deep link to your app’s notification settings in the Settings app.
- [UIApplicationOpenNotificationSettingsURLString](../uiapplicationopennotificationsettingsurlstring.md) — A constant that provides the URL string you use to deep link to your app’s notification settings in the Settings app. _(deprecated)_

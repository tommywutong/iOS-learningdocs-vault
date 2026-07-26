---
title: 'init(suiteName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/userdefaults/init(suitename:)'
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults/init(suitename:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults/init%28suitename%3A%29.json'
content_hash: 'sha256:c4786c9d418c2d3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [UserDefaults](../userdefaults.md)

# init(suiteName:)

<sub>Initializer</sub>

Creates a new defaults object and initializes it with the settings from the specified database.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(suiteName suitename: String?)
```

## Parameters

- `suitename` — The name of the app group or suite to add to the search list. To read and write settings for a shared app group, specify the app group identifier. Don’t specify the [NSGlobalDomain](globaldomain.md) or your app’s bundle identifier. If you specify `nil`, this method returns a defaults object that reads and writes from the current app’s settings.

## Discussion

Use this method to create a defaults object that reads settings from the custom domain you specify. For example, you might use this method to access settings you share among multiple apps or between your app and an app extension. The returned object writes settings to the domain you specified. Every instance of ``UserDefaults shares the contents of the argument and registration domains.

The `suiteName` parameter matches the domain parameter of the corresponding CFPreferences APIs, except when translating between Foundation and Core Foundation constants. The following example shows two equivalent statements. For more details, see [Preferences Utilities](../../corefoundation/preferences-utilities.md).

Equivalent statements using NSUserDefaults and CFPreferences APIs

**Swift**

```swift
let userDefaultsValue = UserDefaults(suiteName: "someDomain")?.object(forKey: "someKey")
let preferencesValue = CFPreferencesCopyAppValue("someKey" as CFString, "someDomain" as CFString)
// userDefaultsValue and preferencesValue are equal
```

**Objective-C**

```objc
id userDefaultsValue = [[[NSUserDefaults alloc] initWithSuiteName:@"someDomain"] objectForKey:@"someKey"];
id preferencesValue = CFPreferencesCopyAppValue(@"someKey", @"someDomain");
// userDefaultsValue and preferencesValue are equal
```

In macOS, specify another app’s bundle identifier to search that app’s settings. You can’t search another app’s settings if either app runs in an [App Sandbox](../../security/app-sandbox.md) and you don’t have the proper entitlements.

## See Also

### Creating a user defaults object

- [standardUserDefaults](standard.md) — The shared defaults object for the current app.
- [- init](<init().md>) — Creates a new defaults object and initializes it with the app’s current settings.

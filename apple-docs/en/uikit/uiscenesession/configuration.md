---
title: configuration
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesession/configuration
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesession/configuration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesession/configuration.json'
content_hash: 'sha256:b9007f9180a7271f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSession](../uiscenesession.md)

# configuration

<sub>Instance Property</sub>

The configuration data for creating the scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var configuration: UISceneConfiguration { get }
```

## Discussion

Before the creation of a scene, UIKit creates a [UISceneConfiguration](../uisceneconfiguration.md) object and fills it with details from your app’s `Info.plist` file. (Normally, UIKit chooses the first scene of the appropriate type listed in your scene configuration data.) If the [- application:configurationForConnectingSceneSession:options:](<../uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method of your app delegate returns a new [UISceneConfiguration](../uisceneconfiguration.md) object, UIKit copies that object to this property.

## See Also

### Getting the scene configuration details

- [UISceneConfiguration](../uisceneconfiguration.md) — Information about the objects and storyboard for UKit to use when creating a particular scene.

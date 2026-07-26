---
title: UIApplicationSupportsTabbedSceneCollection
framework: Bundle Resources
symbol_kind: typealias
role: symbol
role_heading: Property List Key
platforms: [Mac Catalyst 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.json'
content_hash: 'sha256:67ee60b1bd6103bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Bundle Resources](../../../bundleresources.md) · [Information Property List](../../information-property-list.md) · [UIApplicationSceneManifest](../uiapplicationscenemanifest.md)

# UIApplicationSupportsTabbedSceneCollection

<sub>Property List Key</sub>

A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.

## Discussion

By default, the tabbing mode for an app built with Mac Catalyst that support multiple scenes is [NSWindow.TabbingMode.automatic](../../../appkit/nswindow/tabbingmode-swift.enum/automatic.md). Starting with macOS 12, you can disable this behavior by adding the [UIApplicationSupportsTabbedSceneCollection](uiapplicationsupportstabbedscenecollection.md) key with a value of [false](../../../swift/false.md) to the [UIApplicationSceneManifest](../uiapplicationscenemanifest.md) key in your app’s `Info.plist` file.

## See Also

### Multiple windows

- [UIApplicationSupportsMultipleScenes](uiapplicationsupportsmultiplescenes.md) — A Boolean value indicating whether the app supports two or more scenes simultaneously.

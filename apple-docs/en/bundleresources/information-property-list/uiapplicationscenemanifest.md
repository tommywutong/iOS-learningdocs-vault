---
title: UIApplicationSceneManifest
framework: Bundle Resources
symbol_kind: dictionary
role: symbol
role_heading: Property List Key
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/bundleresources/information-property-list/uiapplicationscenemanifest
source_url: 'https://developer.apple.com/documentation/bundleresources/information-property-list/uiapplicationscenemanifest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/bundleresources/information-property-list/uiapplicationscenemanifest.json'
content_hash: 'sha256:0733c1735adc1edb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Bundle Resources](../../bundleresources.md) · [Information Property List](../information-property-list.md)

# UIApplicationSceneManifest

<sub>Property List Key</sub>

The information about the app’s scene-based life-cycle support.

## Discussion

The presence of this key indicates that the app supports scenes and doesn’t use an app delegate object to manage transitions to and from the foreground or background.

## Topics

### Multiple windows

- [UIApplicationSupportsMultipleScenes](uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) — A Boolean value indicating whether the app supports two or more scenes simultaneously.
- [UIApplicationSupportsTabbedSceneCollection](uiapplicationscenemanifest/uiapplicationsupportstabbedscenecollection.md) — A Boolean value indicating whether an app built with Mac Catalyst supports automatic tabbing mode.

### CarPlay

- [CPSupportsDashboardNavigationScene](uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md) — A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.
- [CPSupportsInstrumentClusterNavigationScene](uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md) — A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.

### Configuration

- [UISceneConfigurations](uiapplicationscenemanifest/uisceneconfigurations.md) — The default configuration details the system uses to create new scenes.

## See Also

### Main user interface

- [UIApplicationPreferredDefaultSceneSessionRole](uiapplicationpreferreddefaultscenesessionrole.md) — The preferred initial scene session role for your app.
- [NSMainStoryboardFile](nsmainstoryboardfile.md) — The name of an app’s storyboard resource file.
- [UIMainStoryboardFile](uimainstoryboardfile.md) — The name of the app’s main storyboard file.
- [NSMainNibFile](nsmainnibfile.md) — The name of an app’s main user interface file.
- [LSUIElement](lsuielement.md) — A Boolean value indicating whether the app is an agent app that runs in the background and doesn’t appear in the Dock.
- [UISupportsTrueScreenSizeOnMac](uisupportstruescreensizeonmac.md) — A Boolean value that indicates whether your iPad app supports arbitrary screen sizes and resolutions when running on a Mac.

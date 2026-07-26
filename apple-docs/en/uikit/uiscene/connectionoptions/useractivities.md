---
title: userActivities
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/connectionoptions/useractivities
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/connectionoptions/useractivities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/connectionoptions/useractivities.json'
content_hash: 'sha256:5f6aef11251e7e6a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [ConnectionOptions](../connectionoptions.md)

# userActivities

<sub>Instance Property</sub>

Information about user activities that you can use to configure your scene’s interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var userActivities: Set<NSUserActivity> { get }
```

## Discussion

If this property contains one or more [NSUserActivity](../../../foundation/nsuseractivity.md) objects, use those objects to configure your scene’s interface when the scene connects. These activity objects represent the user activities that are available at the time the scene connects, like from search results, other apps, or [- requestSceneSessionActivation:userActivity:options:errorHandler:](<../../uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>). For example, if the user was browsing a web page, an activity object might contain the URL of that page.

This property doesn’t contain user activity objects related to Handoff. At connection time, UIKit delivers only the type of a Handoff interaction in the [handoffUserActivityType](handoffuseractivitytype.md) property. Later, it calls additional methods of [UISceneDelegate](../../uiscenedelegate.md) to deliver the [NSUserActivity](../../../foundation/nsuseractivity.md) object itself.

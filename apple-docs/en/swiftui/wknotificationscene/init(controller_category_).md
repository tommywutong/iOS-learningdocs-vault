---
title: 'init(controller:category:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/wknotificationscene/init(controller:category:)'
source_url: 'https://developer.apple.com/documentation/swiftui/wknotificationscene/init(controller:category:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wknotificationscene/init%28controller%3Acategory%3A%29.json'
content_hash: 'sha256:ac04eb38243c3ae0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WKNotificationScene](../wknotificationscene.md)

# init(controller:category:)

<sub>Initializer</sub>

Creates a scene that appears in response to receiving a specific category of remote or local notifications.

<sub>watchOS</sub>

```swift
nonisolated init(controller: Controller.Type = Controller.self, category: String)
```

## Parameters

- `controller` — The type of [WKUserNotificationHostingController](../wkusernotificationhostingcontroller.md) to display upon receipt of the specified notification category.

- `category` — The category of notifications to listen for.

## Discussion

Use a watch notification instance to add support for one or more Apple Watch notification scenes that appear on receipt of the local or remote notification categories you specify. The example below, adds two notification scenes to the app declaration:

```swift
@main
struct PopQuizApp : App {
    var body: some Scene {
        MainScene {
            RootView()
        }

        WKNotificationScene(
            controller: QuizTimeController.self,
            category: "com.example.quiztime"
        )

        WKNotificationScene(
            controller: QuizResultsController.self,
            category: "com.example.results"
        )
    }
}
```

Each [WKNotificationScene](../wknotificationscene.md) declaration references a [WKUserNotificationHostingController](../wkusernotificationhostingcontroller.md) and a category string that you provide. The hosting controller displays your notification’s content view upon receipt of a local or a [PushKit](../../pushkit.md) notification. The category string you specify corresponds to the category name in the notification’s dictionary and describes a specific notification that contains the content displayed by the notification view.

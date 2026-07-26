---
title: 'groupActivityAssociation(_:)'
framework: GroupActivities
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/groupactivityassociation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/groupactivityassociation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/groupactivityassociation%28_%3A%29.json'
content_hash: 'sha256:cf8df75c6b0e0e0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# groupActivityAssociation(_:)

<sub>Instance Method</sub>

Specifies how a view should be associated with the current SharePlay group activity.

<sub>visionOS</sub>

```swift
nonisolated func groupActivityAssociation(_ kind: GroupActivityAssociationKind?) -> some View

```

## Parameters

- `kind` — If given, the kind of group activity association. You can dynamically remove the group activity’s association with a view by setting the given `kind` to `nil` instead of `.primary(_:)`.

## Discussion

When a group of people join a SharePlay activity with their spatial Personas, the system selects a common, primary scene to arrange their spatial Personas around. This association between the group activity and a primary scene in your app creates a shared space for the spatial Personas to interact in; enabling participants to gesture at the associated scene and understand each other. For more information about spatial Personas and  SharePlay on visionOS, see [Adding spatial Persona support to an activity](../../groupactivities/adding-spatial-persona-support-to-an-activity.md).

By default, the system uses your scene’s activation conditions in concert with your activity’s `SceneAssociationBehavior` to select a scene to associate with the activity. You can specify a different scene or dynamically change the associated scene by using this modifier to set a view’s group activity association to `GroupActivityAssociationKind/primary`.

> [!tip] Tip
> When building a custom `SpatialTemplate`, the scene with the primary association is the `SpatialTemplateElementPosition/app` that each seat’s position is relative to.

```swift
struct MyApp: App {
    var body: some Scene {
        ...
        Window("Game Window") {
            GameView()
                .groupActivityAssociation(.primary("game-window"))
        }
    }
}
```

If there are multiple scenes that are simultaneously configured with the primary group activity association, the most recently associated scene will be used. For example, if your app defines two windows and both contain views with the primary association kind, the most recently opened one will be used as the primary scene. If that second window is subsequently closed, the original window will be used again.

You can dynamically remove the group activity’s association with a view by setting the given kind to `nil` instead of `.primary`.

```swift
@State var activityState: ActivityState

var body: some Scene {
    WindowGroup {
        TeamSelectionView()
            .groupActivityAssociation(activityState == .teamSelection ? .primary("team-selection") : nil)
    }

    WindowGroup {
        CardGameVolume()
            .groupActivityAssociation(activityState == .inGame ? .primary("in-game") : nil)
    }
    .windowStyle(.volumetric)
}
```

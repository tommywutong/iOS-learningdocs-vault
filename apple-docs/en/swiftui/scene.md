---
title: Scene
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scene
source_url: 'https://developer.apple.com/documentation/swiftui/scene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scene.json'
content_hash: 'sha256:217a9fd16e8f79d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Scene

<sub>Protocol</sub>

A part of an app’s user interface with a life cycle managed by the system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol Scene
```

## Overview

You create an [App](app.md) by combining one or more instances that conform to the `Scene` protocol in the app’s [body](app/body-swift.property.md). You can use the built-in scenes that SwiftUI provides, like [WindowGroup](windowgroup.md), along with custom scenes that you compose from other scenes. To create a custom scene, declare a type that conforms to the `Scene` protocol. Implement the required [body](scene/body-swift.property.md) computed property and provide the content for your custom scene:

```swift
struct MyScene: Scene {
    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
    }
}
```

A scene acts as a container for a view hierarchy that you want to display to the user. The system decides when and how to present the view hierarchy in the user interface in a way that’s platform-appropriate and dependent on the current state of the app. For example, for the window group shown above, the system lets the user create or remove windows that contain `MyRootView` on platforms like macOS and iPadOS. On other platforms, the same view hierarchy might consume the entire display when active.

Read the [scenePhase](environmentvalues/scenephase.md) environment value from within a scene or one of its views to check whether a scene is active or in some other state. You can create a property that contains the scene phase, which is one of the values in the [ScenePhase](scenephase.md) enumeration, using the [Environment](environment.md) attribute:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase

    // ...
}
```

The `Scene` protocol provides scene modifiers, defined as protocol methods with default implementations, that you use to configure a scene. For example, you can use the [onChange(of:perform:)](<scene/onchange(of_perform_).md>) modifier to trigger an action when a value changes. The following code empties a cache when all of the scenes in the window group have moved to the background:

```swift
struct MyScene: Scene {
    @Environment(\.scenePhase) private var scenePhase
    @StateObject private var cache = DataCache()

    var body: some Scene {
        WindowGroup {
            MyRootView()
        }
        .onChange(of: scenePhase) { newScenePhase in
            if newScenePhase == .background {
                cache.empty()
            }
        }
    }
}
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [AlertScene](alertscene.md), [AssistiveAccess](assistiveaccess.md), [DocumentGroup](documentgroup.md), [DocumentGroupLaunchScene](documentgrouplaunchscene.md), [Group](group.md), [ImmersiveSpace](immersivespace.md), [MenuBarExtra](menubarextra.md), [ModifiedContent](modifiedcontent.md), [RemoteImmersiveSpace](remoteimmersivespace.md), [Settings](settings.md), [UtilityWindow](utilitywindow.md), [WKNotificationScene](wknotificationscene.md), [Window](window.md), [WindowGroup](windowgroup.md)

## Topics

### Creating a scene

- [body](scene/body-swift.property.md) — The content and behavior of the scene.
- [Body](scene/body-swift.associatedtype.md) — The type of scene that represents the body of this scene.

### Watching for changes

- [onChange(of:initial:_:)](<scene/onchange(of_initial___).md>) — Adds an action to perform when the given value changes.
- [handlesExternalEvents(matching:)](<scene/handlesexternalevents(matching_).md>) — Specifies the external events for which SwiftUI opens a new instance of the modified scene.

### Creating background tasks

- [backgroundTask(_:action:)](<scene/backgroundtask(__action_).md>) — Runs the specified action when the system provides a background task.

### Managing app storage

- [defaultAppStorage(_:)](<scene/defaultappstorage(__).md>) — The default store used by `AppStorage` contained within the scene and its view content.

### Setting commands

- [commands(content:)](<scene/commands(content_).md>) — Adds commands to the scene.
- [commandsRemoved()](<scene/commandsremoved().md>) — Removes all commands defined by the modified scene.
- [commandsReplaced(content:)](<scene/commandsreplaced(content_).md>) — Replaces all commands defined by the modified scene with the commands from the builder.
- [keyboardShortcut(_:)](<scene/keyboardshortcut(__).md>) — Defines a keyboard shortcut for opening new scene windows.
- [keyboardShortcut(_:modifiers:localization:)](<scene/keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut for opening new scene windows.

### Sizing and positioning the scene

- [defaultPosition(_:)](<scene/defaultposition(__).md>) — Sets a default position for a window.
- [defaultSize(_:)](<scene/defaultsize(__).md>) — Sets a default size for a window.
- [defaultSize(width:height:)](<scene/defaultsize(width_height_).md>) — Sets a default width and height for a window.
- [defaultSize(width:height:depth:)](<scene/defaultsize(width_height_depth_).md>) — Sets a default size for a volumetric window.
- [defaultSize(_:in:)](<scene/defaultsize(__in_).md>) — Sets a default size for a volumetric window.
- [defaultSize(width:height:depth:in:)](<scene/defaultsize(width_height_depth_in_).md>) — Sets a default size for a volumetric window.
- [defaultWindowPlacement(_:)](<scene/defaultwindowplacement(__).md>) — Defines a function used for determining the default placement of windows.
- [windowResizability(_:)](<scene/windowresizability(__).md>) — Sets the kind of resizability to use for a window.
- [windowIdealSize(_:)](<scene/windowidealsize(__).md>) — Specifies how windows derived form this scene should determine their size when zooming.
- [windowIdealPlacement(_:)](<scene/windowidealplacement(__).md>) — Provides a function which determines a placement to use when windows of a scene zoom.
- [windowManagerRole(_:)](<scene/windowmanagerrole(__).md>) — Configures the role for windows derived from `self` when participating in a managed window context, such as full screen or Stage Manager.

### Interacting with volumes

- [volumeWorldAlignment(_:)](<scene/volumeworldalignment(__).md>) — Specifies how a volume should be aligned when moved in the world.
- [defaultWorldScaling(_:)](<scene/defaultworldscaling(__).md>) — Specify the world scaling behavior for the window.

### Configuring scene visibility

- [defaultLaunchBehavior(_:)](<scene/defaultlaunchbehavior(__).md>) — Sets the default launch behavior for this scene.
- [restorationBehavior(_:)](<scene/restorationbehavior(__).md>) — Sets the restoration behavior for this scene.
- [persistentSystemOverlays(_:)](<scene/persistentsystemoverlays(__).md>) — Sets the preferred visibility of the non-transient system views overlaying the app.

### Styling the scene

- [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) — Sets the style for an immersive space.
- [menuBarExtraStyle(_:)](<scene/menubarextrastyle(__).md>) — Sets the style for menu bar extra created by this scene.
- [upperLimbVisibility(_:)](<scene/upperlimbvisibility(__).md>) — Sets the preferred visibility of the user’s upper limbs, while an [ImmersiveSpace](immersivespace.md) scene is presented.
- [windowStyle(_:)](<scene/windowstyle(__).md>) — Sets the style for windows created by this scene.
- [windowLevel(_:)](<scene/windowlevel(__).md>) — Sets the window level of this scene.
- [windowToolbarStyle(_:)](<scene/windowtoolbarstyle(__).md>) — Sets the style for the toolbar defined within this scene.
- [windowToolbarLabelStyle(_:)](<scene/windowtoolbarlabelstyle(__).md>) — Sets the label style of items in a toolbar and enables user customization.
- [windowToolbarLabelStyle(fixed:)](<scene/windowtoolbarlabelstyle(fixed_).md>) — Sets the label style of items in a toolbar.

### Configuring a document launcher scene

- [documentBrowserContextMenu(_:)](<scene/documentbrowsercontextmenu(__).md>) — Adds to a `DocumentGroupLaunchScene` actions that accept a list of selected files as their parameter.
- [documentLaunchTitle(_:)](<scene/documentlaunchtitle(__).md>) — Sets the title displayed on the document launch card. _(beta)_
- [documentLaunchSubtitle(_:)](<scene/documentlaunchsubtitle(__).md>) — Sets the subtitle displayed beneath the title on the document launch card. _(beta)_

### Configuring a data model

- [modelContext(_:)](<scene/modelcontext(__).md>) — Sets the model context in this scene’s environment.
- [modelContainer(_:)](<scene/modelcontainer(__).md>) — Sets the model container and associated model context in this scene’s environment.
- [modelContainer(for:inMemory:isAutosaveEnabled:isUndoEnabled:onSetup:)](<scene/modelcontainer(for_inmemory_isautosaveenabled_isundoenabled_onsetup_).md>) — Sets the model container in this scene for storing the provided model type, creating a new container if necessary, and also sets a model context for that container in this scene’s environment.

### Managing the environment

- [environment(_:)](<scene/environment(__).md>) — Places an observable object in the scene’s environment.
- [environment(_:_:)](<scene/environment(____).md>) — Sets the environment value of the specified key path to the given value.
- [environmentObject(_:)](<scene/environmentobject(__).md>) — Supplies an `ObservableObject` to a view subhierarchy.
- [transformEnvironment(_:transform:)](<scene/transformenvironment(__transform_).md>) — Transforms the environment value of the specified key path with the given function.

### Interacting with dialogs

- [dialogIcon(_:)](<scene/dialogicon(__).md>) — Configures the icon used by alerts.
- [dialogSeverity(_:)](<scene/dialogseverity(__).md>) — Sets the severity for alerts.
- [dialogSuppressionToggle(isSuppressed:)](<scene/dialogsuppressiontoggle(issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.
- [dialogSuppressionToggle(_:isSuppressed:)](<scene/dialogsuppressiontoggle(__issuppressed_).md>) — Enables user suppression of an alert with a custom suppression message.

### Supporting drag behavior

- [windowBackgroundDragBehavior(_:)](<scene/windowbackgrounddragbehavior(__).md>) — Configures the behavior of dragging a window by its background.

### Configuring immersive scenes

- [immersiveContentBrightness(_:)](<scene/immersivecontentbrightness(__).md>) — Sets the content brightness of an immersive space.
- [immersiveEnvironmentBehavior(_:)](<scene/immersiveenvironmentbehavior(__).md>) — Sets the immersive environment behavior that should apply when this scene opens.

### Deprecated symbols

- [onChange(of:perform:)](<scene/onchange(of_perform_).md>) — Adds an action to perform when the given value changes. _(deprecated)_

## See Also

### Creating scenes

- [SceneBuilder](scenebuilder.md) — A result builder for composing a collection of scenes into a single composite scene.

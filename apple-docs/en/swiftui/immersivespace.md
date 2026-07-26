---
title: ImmersiveSpace
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/immersivespace
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace.json'
content_hash: 'sha256:8b6208607a37a819'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ImmersiveSpace

<sub>Structure</sub>

A scene that presents its content in an unbounded space.

<sub>visionOS</sub>

```swift
nonisolated struct ImmersiveSpace<Content, Data> where Content : ImmersiveSpaceContent, Data : Decodable, Data : Encodable, Data : Hashable
```

## Overview

Use an immersive space as a container for a view hierarchy that your app presents. The hierarchy that you declare as the immersive space’s content serves as a template for it:

```swift
@main
struct SolarSystemApp: App {
    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
    }
}
```

If you want to create a bounded scene instead, use one of the types that creates a window or a volume, like [WindowGroup](windowgroup.md) or [DocumentGroup](documentgroup.md).

### Style the immersive space

By default, immersive spaces use the [mixed](immersionstyle/mixed.md) style which places virtual content in a person’s surroundings. You can select a different style for the immersive space by adding the [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) scene modifier to the scene. For example, you can completely control the visual experience using the [full](immersionstyle/full.md) immersion style:

```swift
@main
struct SolarSystemApp: App {
    @State private var style: ImmersionStyle = .full

    var body: some Scene {
        ImmersiveSpace {
            SolarSystem()
        }
        .immersionStyle(selection: $style, in: .full)
    }
}
```

You can change the immersion style after presenting the immersive space by changing the modifier’s `selection` input, although you can only use one of the values that you specify in the modifier’s second parameter. For any style of immersion, the other parts of your app’s interface — namely its windows — remain visible. However, the immersion style affects how windows interact with virtual objects in the environment:

- For the [mixed](immersionstyle/mixed.md) style, a virtual object obscures part or all of a window that’s behind the object. Similarly, a window obscures a virtual object that’s behind the window.
- For other styles, windows always render in front of virtual content, no matter how someone positions the window or the content. This helps people to avoid losing track of windows behind virtual content when passthrough is partially or completely off.

### Open an immersive space

You can programmatically open an immersive space by giving it an identifier. For example, you can label the solar system view from the previous example:

```swift
ImmersiveSpace(id: "solarSystem") {
    SolarSystem()
}
```

Elsewhere in your code, you use the [openImmersiveSpace](environmentvalues/openimmersivespace.md) environment value to get the instance of the [OpenImmersiveSpaceAction](openimmersivespaceaction.md) structure for a given [Environment](environment.md). You call the instance directly — for example, from a button’s closure, like in the following code — using the identifier:

```swift
struct NewSolarSystemImmersiveSpace: View {
    var solarSystem: SolarSystem
    @Environment(\.openImmersiveSpace) private var openImmersiveSpace

    var body: some View {
        Button("Present Solar System") {
            Task {
                await openImmersiveSpace(id: "solarSystem")
            }
        }
    }
}
```

Mark the call to the action with `await` because it executes asynchronously. When your app opens an immersive space, the system hides all other visible apps. The system allows only one immersive space to be open at a time. Be sure to close the open immersive space before opening another one.

### Dismiss an immersive space

You can dismiss an immersive space by calling the [dismissImmersiveSpace](environmentvalues/dismissimmersivespace.md) action from the environment. For example, you can define a button that dismisses an immersive space:

```swift
struct DismissImmersiveSpaceButton: View {
    @Environment(\.dismissImmersiveSpace)
    private var dismissImmersiveSpace

    var body: some View {
        Button("Close Solar System") {
            Task {
                await dismissImmersiveSpace()
            }
        }
    }
}
```

The dismiss action runs asynchronously, like the open action. You don’t need to specify an identifier when dismissing an immersive space because there can only be one immersive space open at a time.

### Present an immersive space at launch

When an app launches, it opens an instance of the first scene that’s listed in the app’s body. However, to open an immersive space at launch, you need to provide additional configuration information in your app’s `Info.plist` file. In particular, set the [UIApplicationPreferredDefaultSceneSessionRole](../bundleresources/information-property-list/uiapplicationpreferreddefaultscenesessionrole.md) key in the scene manifest to the value [UISceneSessionRoleImmersiveSpaceApplication](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication.md).

To configure the style of the immersive space that opens at launch, add a scene configuration to the scene session role. Use the [UISceneInitialImmersionStyle](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiscenesessionroleimmersivespaceapplication/uisceneinitialimmersionstyle.md) key together with a value that indicates one of the mixed, full, or progressive styles. See the initial immersion style key for more information.

## Relationships

- **Conforms To**: [Scene](scene.md)

## Topics

### Creating an immersive space

- [init(content:)](<immersivespace/init(content_).md>) — Creates an immersive space.

### Identifying an immersive space

- [init(id:content:)](<immersivespace/init(id_content_).md>) — Creates the immersive space associated with the specified identifier. _(deprecated)_

### Creating a data-driven immersive space

- [init(for:content:)](<immersivespace/init(for_content_).md>) — Creates the immersive space for a specified type of presented data.
- [init(id:for:content:)](<immersivespace/init(id_for_content_).md>) — Creates the immersive space associated with an identifier for a specified type of presented data.

### Providing default data to an immersive space

- [init(for:content:defaultValue:)](<immersivespace/init(for_content_defaultvalue_).md>) — Creates an immersive space.
- [init(id:for:content:defaultValue:)](<immersivespace/init(id_for_content_defaultvalue_).md>) — Creates the immersive space associated with an identifier for a specified type of presented data, and a default value, if the data is not set.

### Supporting types

- [ImmersiveSpaceViewContent](immersivespaceviewcontent.md) — Immersive space content that uses a SwiftUI view hierarchy as the content.
- [ImmersiveSpaceContent](immersivespacecontent.md) — A type that you can use as the content of an immersive space.

### Initializers

- [init(for:makeContent:)](<immersivespace/init(for_makecontent_).md>)
- [init(for:makeContent:defaultValue:)](<immersivespace/init(for_makecontent_defaultvalue_).md>)
- [init(foveatedStreaming:)](<immersivespace/init(foveatedstreaming_).md>) — Creates an immersive space to display foveated streaming content.
- [init(foveatedStreaming:content:)](<immersivespace/init(foveatedstreaming_content_).md>) — Creates an immersive space to display foveated streaming content alongside `RealityKit` content.
- [init(id:for:makeContent:)](<immersivespace/init(id_for_makecontent_).md>)
- [init(id:for:makeContent:defaultValue:)](<immersivespace/init(id_for_makecontent_defaultvalue_).md>)
- [init(id:makeContent:)](<immersivespace/init(id_makecontent_).md>) — Creates the immersive space associated with the specified identifier.
- [init(makeContent:)](<immersivespace/init(makecontent_).md>)

## See Also

### Creating an immersive space

- [ImmersiveSpaceContentBuilder](immersivespacecontentbuilder.md) — A result builder for composing a collection of immersive space elements.
- [immersionStyle(selection:in:)](<scene/immersionstyle(selection_in_).md>) — Sets the style for an immersive space.
- [ImmersionStyle](immersionstyle.md) — The styles that an immersive space can have.
- [immersiveSpaceDisplacement](environmentvalues/immersivespacedisplacement.md) — The displacement that the system applies to the immersive space when moving the space away from its default position, in meters.
- [ImmersiveEnvironmentBehavior](immersiveenvironmentbehavior.md) — The behavior of the system-provided immersive environments when a scene is opened by your app.
- [ProgressiveImmersionAspectRatio](progressiveimmersionaspectratio.md)

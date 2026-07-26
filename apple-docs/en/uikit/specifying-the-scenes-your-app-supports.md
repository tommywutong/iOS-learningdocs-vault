---
title: Specifying the scenes your app supports
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/specifying-the-scenes-your-app-supports
source_url: 'https://developer.apple.com/documentation/uikit/specifying-the-scenes-your-app-supports'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/specifying-the-scenes-your-app-supports.json'
content_hash: 'sha256:981c806dbc2ca8cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Scenes](scenes.md)

# Specifying the scenes your app supports

<sub>Article</sub>

Tell the system about your app’s scenes, including the objects you use to manage each scene and its initial user interface.

## Overview

Add support for scenes to your app to receive scene-specific life-cycle events that UIKit provides, and use scene objects and methods to manage your user interface. If you enable support for multiple windows as part of your app’s scene configuration, people can create multiple copies of your app’s UI on platforms that support it. For each copy of your app’s UI, you use a scene object to manage the window, views, and view controllers that present the UI onscreen.

When your app or user requests a new scene, UIKit creates the corresponding scene object and handles its initial setup. To do that, UIKit relies on information that you provide. In your app’s Xcode project, declare one or more types of scenes that your app supports and the objects that your app uses to manage those scenes. You can do that statically in Xcode’s Info tab for your app’s target or dynamically at runtime.

### Enable scene support in your project settings

Update your app’s configuration settings to opt in to scenes:

1. Open your Xcode project.
2. Navigate to the Info settings tab for your app target.
3. Add the [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) dictionary key in the Custom iOS Target Properties section.

The value of this key is a dictionary, which initially contains the [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) key and the [UISceneConfigurations](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md) key.

Set the value of the [UIApplicationSupportsMultipleScenes](../bundleresources/information-property-list/uiapplicationscenemanifest/uiapplicationsupportsmultiplescenes.md) key to [true](../swift/true.md) to tell the system if your app supports multiple simultaneous scenes, or [false](../swift/false.md) if you want to display only one scene at a time. Supporting multiple scenes requires extra work on your part to ensure that your scenes don’t interfere with each other. For example, if your scenes use the same shared data structures, they must coordinate access to those structures to preserve the integrity of your app’s data.

### Configure the details for each scene

UIKit handles the creation of your app’s scenes using information that you provide. The simplest way to provide this information is in your app’s Info settings:

1. Open your Xcode project and navigate to the Info settings tab for your app target.
2. Expand the Application Scene Manifest entry. This entry corresponds to the [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) key. If it isn’t present, add it as described in [Enable scene support in your project settings](specifying-the-scenes-your-app-supports.md#Enable-scene-support-in-your-project-settings).
3. In the Scene Configuration entry, click the Add (+) button.
4. Select Window Application Session Role to add a main scene to your app.
5. Fill in the scene details in the provided entry.

Most apps need only one main scene, but you may add multiple scenes and configure each differently. For example, you might include a second scene specifically to display notification-related content. UIKit requires the following information for each scene:

- The class name of the scene, which is [UIWindowScene](uiwindowscene.md).
- The class name of the custom delegate object your app uses to manage the scene. The class must adopt the [UIWindowSceneDelegate](uiwindowscenedelegate.md) protocol.
- A unique name that your app uses to identify the scene internally.
- The name of the storyboard containing the scene’s initial UI. Specify the name without the `.storyboard` filename extension.

For more information about how to configure your scenes, see [UISceneConfigurations](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations.md).

### Create the interface for your scene

You specify the UI for your scene using storyboards. The storyboard you assign to the [UISceneStoryboardFile](../bundleresources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/uiwindowscenesessionroleapplication/uiscenestoryboardfile.md) key contains the initial view controller you want to display for your scene. In addition to creating the scene object, UIKit creates a window for your scene automatically and installs the initial view controller from your storyboard in it. You can replace that view controller programmatically using the methods of your [UIWindowSceneDelegate](uiwindowscenedelegate.md) object.

> [!important] Important
> Don’t forget to designate an initial view controller in your storyboard. UIKit relies on the presence of this view controller when configuring your UI.

### Change your scene’s configuration dynamically

Before actually creating your scene object, UIKit calls the [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method of your app delegate to let you change the scene-related details. You might use this method to adjust the scene configuration based on the options that UIKit provides. For example, when the system passes a notification response to your scene, you might specify a different storyboard with your notification-related interface.

If you don’t implement or configure scenes dynamically, UIKit uses the information in your app’s `Info.plist` file to create your scenes.

### Adopt scene-based life-cycle semantics

Adding support for scenes changes how your app responds to life-cycle events. In an app that doesn’t use the scene life-cycle objects, the app delegate object handles transitions to the foreground or background. When you add scene support to your app, UIKit shifts that responsibility to your scene delegate objects. Scene life cycles are independent of one another, and independent of the app itself, so your scene delegate objects must handle the transitions.

For information about how to handle life-cycle events, see [Managing your app’s life cycle](managing-your-app-s-life-cycle.md).

## See Also

### Configuration

- [UIApplicationSceneManifest](../bundleresources/information-property-list/uiapplicationscenemanifest.md) — The information about the app’s scene-based life-cycle support.
- [UISceneConfiguration](uisceneconfiguration.md) — Information about the objects and storyboard for UKit to use when creating a particular scene.
- [UISceneSession](uiscenesession.md) — An object that contains information about one of your app’s scenes.

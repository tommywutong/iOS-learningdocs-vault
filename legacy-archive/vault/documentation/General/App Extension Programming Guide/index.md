---
title: App Extension Programming Guide
apple_id: TP40014214
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2017-10-19'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html
archived_at: '2026-07-15T07:34:03.182537Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## App Extensions Increase Your Impact

An app extension lets you extend custom functionality and content beyond your app and make it available to users while they’re interacting with other apps or the system.

You create an app extension to enable a specific task. For example, to let users post to your social service from a web browser, you can provide a Share extension. Or, to let users catch up on their favorite team, you can provide a Today widget that displays current sports scores in Notification Center. You can even create an app extension that provides a custom keyboard that users can use in place of the iOS system keyboard.

### There Are Several Types of App Extensions

iOS and macOS define several types of app extensions, each of which is tied to a single, well-scoped area of the system, such as sharing, Notification Center, and the iOS keyboard. A system area that enables extensions is called an _extension point_. Each extension point defines usage policies and provides APIs that you use when you create an app extension for that area. You choose an extension point based on the functionality you want to provide.

Table 1-1 lists the extension points in iOS and macOS and gives an example of tasks you might enable in an app extension for each extension point.

__Table 1-1__Extension points on Apple platforms

| Extension point | Typical app extension functionality |
| --- | --- |
| Action (iOS and macOS; UI and non-UI variants) | Manipulate or view content originating in a host app. |
| Audio Unit (iOS and macOS; UI and non-UI variants) | Generates an audio stream to send to a host app, or modifies an audio stream from a host app and sends it back to the host app. |
| Broadcast UI (iOS and tvOS) |  |
| Broadcast Upload (iOS and tvOS) |  |
| Call Directory (iOS) | Identify and block incoming callers by their phone number. To learn more, see _[CallKit Framework Reference](https://developer.apple.com/documentation/callkit)_. |
| Content Blocker (iOS and macOS) | Indicate to WebKit that your content-blocking app has updated its rules.  (This app extension has no user interface.) |
| Custom Keyboard (iOS) | Replace the iOS system keyboard with a custom keyboard for use in all apps. |
| Document Provider (iOS; UI and non-UI variants) | Provide access to and manage a repository of files. |
| Finder Sync (macOS) | Present information about file sync state directly in Finder.  (This app extension has no user interface.) |
| Game App (watchOS) | Provide a game app for Apple Watch, as described in _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_.  (The Game App template is a version of the WatchKit App template, configured for game content.) |
| iMessage (iOS) | Interact with the Messages app. To learn more, see [Messages](https://developer.apple.com/reference/messages). |
| Intents (iOS) | Handle tasks related to supporting Siri integration with your app. To learn more, see _SiriKit Programming Guide_. |
| Intents UI (iOS) | Customize the Siri or Maps interface after handling a task related to supporting Siri integration with your app. To learn more, see _SiriKit Programming Guide_. |
| Notification Content (iOS) |  |
| Notification Service (iOS) |  |
| Photo Editing (iOS and macOS) | Edit a photo or video within the Photos app. |
| Share (iOS and macOS) | Post to a sharing website or share content with others. |
| Smart Card Token (macOS) |  |
| Spotlight Index (iOS) | Index content within your app while it isn’t running. To learn more, see [Index App Content](../App%20Search%20Programming%20Guide/AppContent.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dgmbyfvbuqny). |
| Sticker Pack (iOS) | Provide a set of stickers that users can use within the Messages app. To learn more, see [Messages](https://developer.apple.com/reference/messages). |
| Today (iOS and macOS) | Get a quick update or perform a quick task in the Today view of Notification Center.  (A Today extension is called a _widget_.) |
| TV Services (tvOS) |  |
| VPN (iOS and macOS) | Create clients for your business’s custom, remote-access VPN servers using the Packet Tunnel Provider or App Proxy Provider extension points.  Create content filtering for managed devices, such as for school environments, using the Filter Control Provider and Filter Data Provider extension points. |
| WatchKit App (watchOS) | Provide an app or a notification UI for Apple Watch, as described in _[App Programming Guide for watchOS](https://developer.apple.com/library/archive/documentation/General/Conceptual/WatchKitProgrammingGuide/index.html#//apple_ref/doc/uid/TP40014969)_. |
| Xcode Source Editor (macOS) |  |

Because the system defines specific areas for app extensions, it’s important to choose the area that best matches the functionality you want to deliver. For example, if you want to create an extension that enables a sharing experience, use the Share extension point, starting with the _Share Extension_ Xcode template.

> [!IMPORTANT]
> 

### Xcode and the App Store Help You Create and Deliver App Extensions

An app extension is different from an app. Although you must use an app to contain and deliver your extensions, each extension is a separate binary that runs independent of the app used to deliver it.

You create an app extension by adding a new [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) to an app. As with any target, an extension target specifies settings and files that combine to build a product within your app project. You can add multiple extension targets to a single app (an app that contains one or more extensions is called a _containing app_).

The best way to start developing an app extension is to use one of the templates that Xcode provides for each extension point on both platforms. Each template includes extension point–specific implementation files and settings, and produces a separate binary that gets added to your containing app’s bundle.

To distribute app extensions to users, you submit a containing app to the App Store. When a user installs your containing app, the extensions it contains are also installed.

After installing an app extension, a user must take action to enable it. Often, users can enable an extension within the context of their current task. If your extension is a Today widget, for example, users can edit the Today view in Notification Center to enable your extension. In other cases, users can use Settings (in iOS) or System Preferences (in macOS) to enable and manage the extensions they install.

### Users Experience App Extensions in Different Contexts

Although each type of app extension enables a different type of task, there are some parts of the user experience that are common to most extensions. As you think about designing an extension, it’s important to understand the user experience that’s intended by the extension point you choose. At a high level, the best user experience for all extensions is quick, streamlined, and focused on a single task.

Users open your app extension by interacting with some system-provided user interface (UI). For example, a user accesses a Share extension by activating the system-provided Share button in an app and choosing the extension from the list that’s displayed.

Although most app extensions provide at least some custom UI elements, users don’t see your custom UI until they enter your extension. When users enter your extension, your custom UI can help to show them that they’re shifting into a new context. Because users can distinguish your extension from the current app, they can appreciate the unique functionality that you provide. Users’ awareness of extensions as separate entities also means that they can identify and remove extensions that misbehave or don’t perform well.

To give users a smooth transition into your app extension, you generally want to balance your custom design with the UI that’s associated with the extension point. For example, it’s a good idea to make your widget look like it belongs in the Today view. Similarly, in your Photo Editing extension, it works well to create a UI that harmonizes with Photos in iOS.

> [!NOTE]
> 

[Understand How an App Extension Works](ExtensionOverview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrnknlte)

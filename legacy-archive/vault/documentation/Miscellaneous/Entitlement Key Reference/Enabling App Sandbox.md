---
title: Entitlement Key Reference
apple_id: TP40011195
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingAppSandbox.html
archived_at: '2026-07-15T08:17:10.414056Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Entitlement Key Reference](About%20Entitlements.md)


[Next](App%20Sandbox%20Temporary%20Exception%20Entitlements.md)[Previous](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/ApplePayandPassKitEntitlements/ApplePayandPassKitEntitlements.html)

# Enabling App Sandbox

In your macOS Xcode project, configure fine-grained security permissions by enabling settings in the Summary tab of the [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor. These settings, in turn, add Boolean values to entitlement keys in the target’s `.entitlements` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file. The values are then incorporated into the target’s code signature when you build the project.

You can think of using App Sandbox entitlements as a two-step process:

1. Sandbox a target, which removes most capabilities for interacting with the system
2. Restore capabilities to the sandboxed target, as needed, by configuring App Sandbox entitlements

At runtime, if a target requires a capability or a system resource for which the target isn’t entitled, the sandbox daemon (`sandboxd`) logs a violation message to the console.

For more information about App Sandbox, read _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

This section describes the keys you can use to confer capabilities to a sandboxed app in macOS. The first key enables App Sandbox; the others configure the sandbox. If App Sandbox is not enabled, the other keys in this section are meaningless.

The value to use for any of these keys is a Boolean `YES` or `NO`, with the default value in each case being `NO`. If you are editing the `.entitlements` file directly in a text editor, the corresponding Boolean values to use are `<true/>` and `<false/>`. The default value for each key is false, so you can (and generally should) leave out the entitlement entirely rather than specifying a false value.

In cases where there are read-only and read/write entitlement key pairs, use of either key in the pair is mutually exclusive with the other.

Add these keys by using the Summary tab of the Xcode [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor. You can also add them directly to a target’s `.entitlements` file with the Xcode [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) editor.

For information on additional entitlements for handling special circumstances, see [App Sandbox Temporary Exception Entitlements](App%20Sandbox%20Temporary%20Exception%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnjnknltc).

For each key in this table, providing a Boolean value of `YES` enables the corresponding capability (unless otherwise noted).

Entitlement keyCapability

com.apple.security.app-sandbox

Enables App Sandbox for a target in an Xcode project

com.apple.security.application-groups

Allows access to group containers that are shared among multiple apps produced by a single development team, and allows certain additional interprocess communication between the apps

Supported in macOS v10.7.5 and in v10.8.3 and later. The format for this attribute is described in [Adding an App to an App Group](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoi).

com.apple.security.assets.movies.read-only

Read-only access to the user’s Movies folder and iTunes movies

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.assets.movies.read-write

Read/write access to the user’s Movies folder and iTunes movies

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.assets.music.read-only

Read-only access to the user’s Music folder

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.assets.music.read-write

Read/write access to the user’s Music folder

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.assets.pictures.read-only

Read-only access to the user’s Pictures folder

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.assets.pictures.read-write

Read/write access to the user’s Pictures folder

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.device.audio-video-bridging

Communication with AVB devices

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.bluetooth

Interaction with Bluetooth devices

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.camera

Capture of movies and still images using the built-in camera, if available

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.firewire

Interaction with FireWire devices (currently, does not support interaction with audio/video devices such as DV cameras)

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.audio-input

Recording of audio using the built-in microphone, if available, along with access to audio input using any Core Audio API that supports audio input

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.serial

Interaction with serial devices

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.device.usb

Interaction with USB devices, including HID devices such as joysticks

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.files.downloads.read-write

Read/write access to the user’s Downloads folder

For details, see [Enabling Access to Files in Standard Locations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlto).

com.apple.security.files.bookmarks.app-scope

Use of app-scoped bookmarks and URLs

For details, see [Enabling Security-Scoped Bookmark and URL Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoa).

com.apple.security.files.bookmarks.document-scope

Use of document-scoped bookmarks and URLs

For details, see [Enabling Security-Scoped Bookmark and URL Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoa).

com.apple.security.files.user-selected.read-only

Read-only access to files the user has selected using an Open or Save dialog

For details, see [Enabling User-Selected File Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltm).

com.apple.security.files.user-selected.read-write

Read/write access to files the user has selected using an Open or Save dialog

For details, see [Enabling User-Selected File Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltm).

com.apple.security.files.user-selected.executable

Allows apps to write executable files.

For details, see [Enabling User-Selected File Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltm).

com.apple.security.inherit

Child process inheritance of the parent’s sandbox

For details, see [Enabling App Sandbox Inheritance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcni).

com.apple.security.network.client

Network socket for connecting to other machines

For details, see [Enabling Network Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlts).

com.apple.security.network.server

Network socket for listening for incoming connections initiated by other machines

For details, see [Enabling Network Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlts).

com.apple.security.personal-information.addressbook

Read/write access to contacts in the user’s address book; allows apps to infer the default address book if more than one is present on a system

For details, see [Enabling Personal Information Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmy).

com.apple.security.personal-information.calendars

Read/write access to the user’s calendars

For details, see [Enabling Personal Information Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmy).

com.apple.security.personal-information.location

Use of the Core Location framework for determining the computer’s geographical location

For details, see [Enabling Personal Information Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmy).

com.apple.security.print

Printing

For details, see [Enabling Hardware Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcmi).

com.apple.security.scripting-targets

Ability to use specific AppleScript scripting access groups within a specific scriptable app

For details, see [Enabling Scripting of Other Apps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknlteni).

You enable App Sandbox individually for each [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) in an macOS Xcode project. For example, you may design a project as a main app, and some helpers in the form of XPC services. You then enable and configure the sandbox for each target individually.

To learn how to enable App Sandbox for your macOS app, which includes performing code signing, see [App Sandbox Quick Start](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxQuickStart/AppSandboxQuickStart.html#//apple_ref/doc/uid/TP40011183-CH2) in _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_. The essential step is to ensure that the target editor checkbox named in Table 4-1 is selected.

__Table 4-1__  Xcode setting for enabling App Sandbox

| Setting | Entitlement key |
| Enable App Sandboxing | `com.apple.security.app-sandbox` |

Xcode provides a pop-up menu, in the Summary tab of the [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor, with choices to enable read-only or read/write access to files and folders that the user explicitly selects. When you enable user-selected file access, you gain programmatic access to files and folders that the user opens using an [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) object, and files the user saves using an [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) object.

Certain other user interactions, such as dragging items to your app or choosing items from the Open Recent menu, automatically expand your sandbox to include those items. Similarly, when macOS resumes an app after a reboot, the sandbox is automatically expanded to include any items that are automatically opened.

To enable user-selected file access in your app, use the Xcode target editor setting shown in Table 4-2.

__Table 4-2__  Xcode setting for user-selected file and folder access

| Setting | Entitlement keys |
| User Selected File | `com.apple.security.files.user-selected.read-only`  `com.apple.security.files.user-selected.read-write` |

In addition to granting user-selected file access, you can employ entitlements to grant programmatic file access to the following user folders:

- Downloads
- Music
- Movies
- Pictures

The Xcode control for enabling Downloads folder access is a checkbox; the controls for enabling access to these other folders are pop-up menus.

When you enable programmatic access to the user’s Movies folder, you also gain access to their iTunes movies.

Reopening of files by macOS using Resume does not require the presence of any entitlement key.

To enable programmatic access to specific folders, use the Xcode [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor settings shown in Table 4-3.

__Table 4-3__  Xcode settings for programmatic file and folder access

| Setting | Entitlement keys |
| Downloads Folder | `com.apple.security.files.downloads.read-write` |
| Music Folder | `com.apple.security.assets.music.read-only`  `com.apple.security.assets.music.read-write` |
| Movies Folder | `com.apple.security.assets.movies.read-only`  `com.apple.security.assets.movies.read-write` |
| Pictures Folder | `com.apple.security.assets.pictures.read-only`  `com.apple.security.assets.pictures.read-write` |

If you want to provide your sandboxed app with persistent access to file system resources, you must enable security-scoped bookmark and URL access. Security-scoped bookmarks are available starting in macOS v10.7.3.

To add the `bookmarks.app-scope` or `bookmarks.document-scope` entitlement, edit the [target’s](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) `.entitlements` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file using the Xcode property list editor. Use the entitlement keys shown in Table 4-4, depending on which type of access you want. Use a value of `<true/>` for each entitlement you want to enable. You can enable either or both entitlements.

For more information on security-scoped bookmarks, read [Security-Scoped Bookmarks and Persistent Resource Access](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3-SW16) in _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

__Table 4-4__  Entitlement keys for enabling security-scoped bookmark and URL access

| Entitlement key | Description |
| `com.apple.security.files.bookmarks.app-scope` | Enables use of app-scoped bookmarks and URLs |
| `com.apple.security.files.bookmarks.document-scope` | Enables use of document-scoped bookmarks and URLs.  Version note: in macOS v10.7.3, this entitlement key was named `com.apple.security.files.bookmarks.collection-scope` |

Xcode’s Network checkboxes in the Summary tab of the [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor let you enable network access for your app.

To enable your app to connect to a server process running on another machine (or on the same machine), enable outgoing network connections.

To enable opening a network listening socket so that other computers can connect to your app, allow incoming network connections.

To enable network access, use the Xcode target editor settings shown in Table 4-5.

__Table 4-5__  Xcode settings for network access

| Setting | Entitlement key |
| Allow Incoming Connections | `com.apple.security.network.server` |
| Allow Outgoing Connections | `com.apple.security.network.client` |

To allow a sandboxed [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) to access hardware services on a system—USB, printing, or the built-in camera and microphone—enable the corresponding setting in the Summary tab of the Xcode target editor.

- _Camera access_ enables access to video and still image capture using the built-in camera, if available.
- _Microphone access_ enables access to audio recording using the built-in microphone, if available.
- _USB access_ enables the ability to interact with USB devices using USB device access APIs. On violation, `sandboxd` names the I/O Kit class your code tried to access.
- _Printing access_ is required if you want to provide a target with the ability to print.

To enable access to hardware, use the Xcode target editor settings shown in Table 4-6.

__Table 4-6__  Xcode settings for hardware access

| Setting | Entitlement key |
| Allow Camera Access | `com.apple.security.device.camera` |
| Allow Microphone Access | `com.apple.security.device.audio-input` |
| Allow USB Access | `com.apple.security.device.usb` |
| Allow Printing | `com.apple.security.print` |

To allow access to hardware devices for which no checkbox exists in Xcode’s user interface, you must manually add the appropriate entitlement to your app’s entitlements property list. These additional entitlements are listed in [Table 4-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltemi). All of these keys take a Boolean value.

__Table 4-7__  Other entitlement keys for accessing hardware

| Entitlement key | Description |
| `com.apple.security.device.audio-video-bridging` | Interaction with AVB devices by using the Audio Video Bridging framework |
| `com.apple.security.device.bluetooth` | Interaction with Bluetooth devices |
| `com.apple.security.device.firewire` | Interaction with FireWire devices (currently, does not support interaction with audio/video devices such as DV cameras) |
| `com.apple.security.device.serial` | Interaction with serial devices |

A user’s personal information is inaccessible to your sandboxed app unless you grant access using the appropriate settings.

- _Address Book_ access enables read/write access to contacts in the user’s address book.
- _Location Services_ access enables use of the Core Location framework to determine the computer’s geographic position.
- _Calendar access_ enables read/write access to the user’s calendars.

To enable access to personal information, use the Xcode [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) editor settings shown in Table 4-8.

__Table 4-8__  Xcode settings for access to a user’s personal information

| Setting | Entitlement key |
| Allow Address Book Data Access | `com.apple.security.personal-information.addressbook` |
| Allow Location Services Access | `com.apple.security.personal-information.location` |
| Allow Calendar Data Access | `com.apple.security.personal-information.calendars` |

The `com.apple.security.application-groups` (available in macOS v10.7.5 and v10.8.3 and later) allows multiple apps produced by a single development team to share access to a special group container. This container is intended for content that is not user-facing, such as shared caches or databases.

In addition, this attribute allows the apps within the group to share Mach and POSIX semaphores and to use certain other IPC mechanisms among the group’s members. For additional details and naming conventions, read “Mach IPC and POSIX Semaphores and Shared Memory” in _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

The value for this key must be of type `array`, and must contain one or more `string` values, each of which must consist of your development team ID, followed by a period, followed by an arbitrary name chosen by your development team. For example:

```
<key>com.apple.security.application-groups</key>
<array>
    <string>DG29478A379Q6483R9214.HolstFirstAppSuite</string>
    <string>DG29478A379Q6483R9214.HolstSecondAppSuite</string>
</array>
```

The group containers are automatically created or added into each app’s sandbox container as determined by the existence of these keys. The group containers are stored in `~/Library/Group Containers/<application-group-id>`, where `<application-group-id>` is one of the strings from the array. Your app can obtain the path to the group containers by calling the [containerURLForSecurityApplicationGroupIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1412643-containerurlforsecurityapplicati) method of [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager).

If your app employs a child process created with either the [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn) function or the [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask) class, you can configure the child process to inherit the sandbox of its parent. However, using a child process does not provide the security afforded by using an XPC service.

To enable sandbox inheritance, a child [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) must use exactly two App Sandbox entitlement keys: `com.apple.security.app-sandbox` and `com.apple.security.inherit`. If you specify any other App Sandbox entitlement, the system aborts the child process. You can, however, confer other capabilities to a child process by way of iCloud and notification entitlements.

The main app in an Xcode project must never have a `YES` value for the `inherit` entitlement.

To add the `inherit` entitlement, edit the target’s `.entitlements` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file using the Xcode property list editor. Use the entitlement key shown in Table 4-9 with a value of `<true/>`.

__Table 4-9__  Entitlement key for inheriting the parent process’s App Sandbox

| Entitlement key | Description |
| `com.apple.security.inherit` | Enables App Sandbox inheritance |

If your app needs to control another scriptable app, your app can use the scripting targets entitlement to request access to one or more of the scriptable app’s scripting access groups.

__Table 4-10__  Entitlement key for accessing scripting targets

| Entitlement key | Description |
| `com.apple.security.scripting-targets` | Ability to use specific AppleScript scripting access groups within a specific scriptable app |

The scripting target entitlement contains a dictionary where each entry has the target app’s code signing identifier as the key, and an array of scripting access groups as the value. Scripting access groups are identified by strings and are specific to an app. For example, the following entry would grant access to composing mail messages with Apple’s Mail app:

```
<key>com.apple.security.scripting-targets</key>
    <dict>
        <key>com.apple.mail</key>
        <array>
            <string>com.apple.mail.compose</string>
        </array>
    </dict>
```

For more information about how to add scripting access groups to an app, watch _WWDC 2012: Secure Automation Techniques in OS X_ and read the manual page for `sdef`.

[Next](App%20Sandbox%20Temporary%20Exception%20Entitlements.md)[Previous](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/ApplePayandPassKitEntitlements/ApplePayandPassKitEntitlements.html)


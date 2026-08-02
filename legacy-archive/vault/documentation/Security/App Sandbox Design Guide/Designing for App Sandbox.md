---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/DesigningYourSandbox/DesigningYourSandbox.html
archived_at: '2026-07-27T06:57:08.379410Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Next](Migrating%20an%20App%20to%20a%20Sandbox.md)[Previous](App%20Sandbox%20in%20Depth.md)

# Designing for App Sandbox

There’s a common, basic workflow for designing or converting an app for App Sandbox. The specific steps to take for your particular app, however, are as unique as your app. To create a work plan for adopting App Sandbox, use the process outlined here, along with the conceptual understanding you have from the earlier chapters in this document.

## Six Steps for Adopting App Sandbox

The workflow to convert an macOS app to work in a sandbox typically consists of the following six steps:

1. Determine whether your app is suitable for sandboxing.
2. Design a development and distribution strategy.
3. Resolve API incompatibilities.
4. Apply the App Sandbox entitlements you need.
5. Add privilege separation using XPC.
6. Implement a migration strategy.

__Note:__ It is not sufficient to perform this task for the main app in your app bundle. For apps distributed through the Mac App Store, all included helper apps and tools must also be sandboxed. For apps distributed through other mechanisms, you should sandbox each executable in your app bundle if at all possible.

For a list of all executable binaries in your app bundle, type the following command in Terminal:

```
find -H YourAppBundle.app -print0 | xargs -0 file | grep "Mach-O .*executable"
```

where `YourAppBundle.app` should be replaced by the path to your app bundle.

## Determine Whether Your App Is Suitable for Sandboxing

Most macOS apps are fully compatible with App Sandbox. If you need behavior in your app that App Sandbox does not allow, consider an alternative approach. For example, if your app depends on hard-coded paths to locations in the user’s home directory, consider the advantages of using Cocoa and Core Foundation path-finding APIs, which use the sandbox container instead.

If you choose to not sandbox your app now, or if you determine that you need a temporary exception entitlement, use Apple’s [bug reporting system](https://bugreport.apple.com/) to let Apple know what’s not working for you. Apple considers feature requests as it develops the macOS platform. Also, if you request a temporary exception, be sure to use the Review Notes field in iTunes Connect to explain why the exception is needed.

The following app behaviors are _incompatible_ with App Sandbox:

- Use of Authorization Services

  With App Sandbox, you cannot do work with the functions described in _[Authorization Services C Reference](https://developer.apple.com/documentation/security/authorization_services)_.
- Use of accessibility APIs in assistive apps

  With App Sandbox, you can and should enable your app for accessibility, as described in _[Accessibility Programming Guide for OS X](../../Accessibility%20Programming%20Guide%20for%20OS%20X/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanzy)_. However, you cannot sandbox an assistive app such as a screen reader, and you cannot sandbox an app that controls another app.
- Sending Apple events to arbitrary apps

  With App Sandbox, you can receive Apple events and respond to Apple events, but you cannot send Apple events to arbitrary apps.

  However, for applications that specifically provide scripting access groups, you can send appropriate Apple events to those apps if your app includes a scripting targets entitlement.

  For other applications, by using a temporary exception entitlement, you can enable the sending of Apple events to a list of specific apps that you specify, as described in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

  Finally, your app can use the subclasses of [NSUserScriptTask](https://developer.apple.com/documentation/foundation/nsuserscripttask) class to run user-provided AppleScript scripts out of a special directory, [NSApplicationScriptsDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsapplicationscriptsdirectory) (`~/Library/Application Scripts/`_code-signing-identifier_`/`). Although your app can read files within this directory, it cannot write files into this directory; the user must manually place scripts here. For details, see the documentation for [NSUserScriptTask](https://developer.apple.com/documentation/foundation/nsuserscripttask) and _WWDC 2012: Secure Automation Techniques in OS X_.
- Posting keyboard or mouse events to another app

  You cannot sandbox an app that controls another app. Posting keyboard or mouse events using functions like [CGEventPost](https://developer.apple.com/documentation/coregraphics/cgevent/1456527-post) offers a way to circumvent this restriction, and is therefore not allowed from a sandboxed app.
- Sending user-info dictionaries in distributed notifications to other tasks

  With App Sandbox, you _cannot_ include a `userInfo` dictionary when posting to an [NSDistributedNotificationCenter](https://developer.apple.com/documentation/foundation/nsdistributednotificationcenter) object for messaging other tasks. (You _can_, as usual, include a `userInfo` dictionary when messaging other parts of your app by way of posting to an [NSNotificationCenter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNotificationCenter/Description.html#//apple_ref/occ/cl/NSNotificationCenter) object.)
- Loading kernel extensions

  Loading of kernel extensions is prohibited with App Sandbox.
- Simulation of user input in Open and Save dialogs

  If your app depends on programmatically manipulating Open or Save dialogs to simulate or alter user input, your app is unsuitable for sandboxing.
- Accessing or setting preferences on other apps

  With App Sandbox, each app maintains its preferences inside its container. Normally, your app has no access to the preferences of other apps.

  However, if your app requires access to the preferences files of other applications, there are temporary exception entitlements available that allow you to specify a list of named preference domains that your app needs to access. For details, see _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.
- Configuring network settings

  With App Sandbox, your app cannot modify the system’s network configuration (whether with the System Configuration framework, the CoreWLAN framework, or other similar APIs) because doing so requires administrator privileges.
- Terminating other apps

  With App Sandbox, you cannot use the [NSRunningApplication](https://developer.apple.com/documentation/appkit/nsrunningapplication) class to terminate other apps.

## Resolve API Incompatibilities

If you are using macOS APIs in ways that were not intended, or in ways that expose user data to attack, you may encounter incompatibilities with App Sandbox. This section provides some examples of app design that are incompatible with App Sandbox and suggests what you can do instead.

### Opening, Saving, and Tracking Documents

If you are managing documents using any technology other than the [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) class, you should convert to using this class to benefit from its built-in App Sandbox support. The `NSDocument` class automatically works with Powerbox. `NSDocument` also provides support for keeping documents within your sandbox if the user moves them using the Finder.

Remember that the inheritance path of the [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) classes is different when your app is sandboxed. See [Open and Save Dialog Behavior with App Sandbox](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltq).

If you don’t use the `NSDocument` class to manage your app’s documents, you can craft your own file-system support for App Sandbox by using the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) class and the [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter) protocol, but this requires a lot of extra work.

### Retaining Access to File System Resources

If your app depends on persistent access to file system resources outside of your app’s container, you need to adopt security-scoped bookmarks as described in [Security-Scoped Bookmarks and Persistent Resource Access](App%20Sandbox%20in%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcnq).

### Creating a Login Item for Your App

To create a login item for your sandboxed app, use the [SMLoginItemSetEnabled](https://developer.apple.com/documentation/servicemanagement/1501557-smloginitemsetenabled) function (declared in `ServiceManagement/SMLoginItem.h`) as described in [Adding Login Items Using the Service Management Framework](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/Adding%20Login%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2jnknltklktk4yq).

(With App Sandbox, you cannot create a login item using functions in the `LSSharedFileList.h` header file. For example, you cannot use the function `LSSharedFileListInsertItemURL`. Nor can you manipulate the state of Launch Services, such as by using the function [LSRegisterURL](https://developer.apple.com/documentation/coreservices/1446350-lsregisterurl).)

### Accessing User Data

Most macOS path-finding APIs return paths relative to the container instead of relative to the user’s home directory. If your app, before you sandbox it, accesses locations in the user’s actual home directory (`~`) and you are using Cocoa or Core Foundation APIs, then, after you enable sandboxing, your path-finding code automatically uses your app’s container instead.

For first launch of your sandboxed app, macOS automatically migrates your app’s main preferences file. If your app uses additional support files, perform a one-time migration of those files to the container, as described in [Migrating an App to a Sandbox](Migrating%20an%20App%20to%20a%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltc).

If you are using a POSIX function such as [getpwuid](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getpwuid.3.html#//apple_ref/doc/man/3/getpwuid) to obtain the path to the user’s actual home directory from Directory Services (rather than by using the `HOME` environment variable), consider instead using a Cocoa or Core Foundation symbol such as the [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) function. By using Cocoa or Core Foundation, you support the App Sandbox restriction against directly accessing the user’s home directory.

If your app requires access to the user’s home directory in order to function, let Apple know about your needs using the Apple [bug reporting system](https://bugreport.apple.com/). In addition, be sure to follow the guidance regarding entitlements provided on the [iTunes Connect](https://itunesconnect.apple.com/) website.

### Accessing Preferences of Other Apps

Because App Sandbox directs path-finding APIs to the container for your app, reading or writing to the user’s preferences takes place within the container. Preferences for other sandboxed apps are inaccessible. Preferences for apps that are not sandboxed are placed in the `~/Library/Preferences` directory, which is also inaccessible to your sandboxed app.

If your app requires access to another app’s preferences in order to function—for example, if it requires access to the playlists that a user has defined for iTunes—let Apple know about your needs using the Apple [bug reporting system](https://bugreport.apple.com/). In addition, be sure to follow the guidance regarding entitlements provided on the [iTunes Connect](https://itunesconnect.apple.com/) website.

### Using HTML5 Embedded Video in Web Views

If you are compiling an app that uses the WebKit framework, and your target is OS X 10.7, you must also link your app against the AV Foundation framework. If you do not do so, because of the way App Sandbox interacts with CoreMedia, your app will be unable to play HTML5 embedded videos.

This additional linking step is not required for apps that run only on macOS 10.8 and later.

## Apply the App Sandbox Entitlements You Need

To adopt App Sandbox for a target in an Xcode project, apply the `<true/>` value to the `com.apple.security.app-sandbox` entitlement key for that target. Do this in the Xcode target editor by selecting the Enable App Sandboxing checkbox.

Apply other entitlements as needed. For a complete list, refer to _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

__Important:__ App Sandbox protects user data most effectively when you minimize the entitlements you request. Take care not to request entitlements for privileges your app does not need. Consider whether making a change in your app could eliminate the need for an entitlement.

## Add Privilege Separation Using XPC

When developing for App Sandbox, look at your app’s behaviors in terms of privileges and access. Consider the potential benefits to security and robustness of separating high-risk operations into their own XPC services.

When you determine that a feature should be placed into an XPC service, do so by referring to [Creating XPC Services](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/Creating%20XPC%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2jnknltm) in _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

## Implement a Migration Strategy

Ensure that customers who are currently using a pre-sandbox version of your app experience a painless upgrade when they install the sandboxed version. For details on how to implement a container migration manifest, read [Migrating an App to a Sandbox](Migrating%20an%20App%20to%20a%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltc).

[Next](Migrating%20an%20App%20to%20a%20Sandbox.md)[Previous](App%20Sandbox%20in%20Depth.md)

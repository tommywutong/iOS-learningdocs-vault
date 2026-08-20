---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html
archived_at: '2026-07-27T06:57:08.366345Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Next](Designing%20for%20App%20Sandbox.md)[Previous](App%20Sandbox%20Quick%20Start.md)

# App Sandbox in Depth

The specific steps you take to adopt App Sandbox are unique to your app, but the access control mechanisms used by App Sandbox to protect user data remain consistent:

- __Entitlements.__ Communicate to macOS the specific system resources your app needs to get its job done, and no more.
- __Containers.__ Access only the files and directories considered safe for your app.
- __Persistent Resource Access.__ Retain security-scoped bookmarks across launches of your app to any additional files to which the user has specifically granted your app access.
- __Code Signing.__ Unambiguously identify your app to the system so another app cannot masquerade as yours.
- __Privilege Separation.__ Split your app into smaller parts, each with its own resource privileges, minimizing the damage if any one part becomes compromised.

## The Need for a Last Line of Defense

You secure your app against attack from malware by following the practices recommended in _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_. But despite your best efforts to build an invulnerable barrier—by avoiding buffer overflows and other memory corruptions, preventing exposure of user data, and eliminating other vulnerabilities—your app can be exploited by malicious code. An attacker needs only to find a single hole in your defenses, or in any of the frameworks and libraries that you link against, to gain control of your app’s interactions with the system.

App Sandbox is designed to confront this scenario head on by letting you describe your app’s intended interactions with the system. The system then grants your app only the access your app needs to get its job done. If malicious code gains control of a properly sandboxed app, it is left with access to only the files and resources in the app’s sandbox.

To successfully adopt App Sandbox, use a different mindset than you might be accustomed to, as suggested in Table 2-1.

__Table 2-1__  The App Sandbox mindset

| When developing… | When adopting App Sandbox… |
| Add features | Minimize system resource use |
| Take advantage of access throughout your app | Partition functionality, then distrust each part |
| Use the most convenient API | Use the most secure API |
| View restrictions as limitations | View restrictions as safeguards |

## Entitlements and System Resource Access

An app that is not sandboxed has access to all user-accessible system resources—including the built-in camera and microphone, network sockets, printing, and most of the file system. If successfully attacked by malicious code, such an app can behave as a hostile agent with wide-ranging potential to inflict harm.

When you enable App Sandbox for your app, you remove all but a minimal set of privileges and then deliberately restore them, one-by-one, using entitlements. An _entitlement_ is a key-value pair that identifies a specific capability, such as the capability to open an outbound network socket.

One special entitlement—Enable App Sandboxing—turns on App Sandbox. When you enable sandboxing, Xcode creates a `.entitlements` [property list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) file and shows it in the project navigator.

If your app requires a capability, request it by adding the corresponding entitlement to your Xcode project using the Summary tab of the target editor. If you don’t require a capability, take care to not include the corresponding entitlement.

You request entitlements on a target-by-target basis. If your app has a single target—the main application—you request entitlements only for that target. If you design your app to use a main application along with helpers (in the form of XPC services), you request entitlements individually, and as appropriate, for each target. You learn more about this in [External Tools, XPC Services, and Privilege Separation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknlte).

You may require finer-grained control over your app’s entitlements than is available in the Xcode target editor. For example, you might request a temporary exception entitlement because App Sandbox does not support a capability your app needs, such as the ability to send an Apple event to an app that does not yet provide any scripting access groups. To work with temporary exception entitlements, use the Xcode property list editor to edit a target’s `.entitlements` property list file directly.

__Note:__ If you request a temporary exception entitlement, be sure to follow the guidance regarding entitlements provided on the [iTunes Connect](https://itunesconnect.apple.com/) website. In particular, file a bug asking for the functionality that you need, and use the Review Notes field in iTunes Connect to explain why your app needs the temporary exception. Be sure to provide the bug number.

macOS App Sandbox entitlements are described in [Enabling App Sandbox](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqna) in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_. For a walk-through of requesting an entitlement for a target in an Xcode project, see [App Sandbox Quick Start](App%20Sandbox%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmrnknltg).

## Container Directories and File System Access

When you adopt App Sandbox, your application has access to the following locations:

- __The app container directory.__ Upon first launch, the operating system creates a special directory for use by your app—and only by your app—called a _container_. Each user on a system gets an individual container for your app, within their home directory; your app has unfettered read/write access to the container for the user who ran it.
- __App group container directories.__ A sandboxed app can specify an entitlement that gives it access to one or more app group container directories, each of which is shared among all apps with that entitlement.
- __User-specified files.__ A sandboxed app (with an appropriate entitlement) automatically obtains access to files in arbitrary locations when those files are explicitly opened by the user or are dragged and dropped onto the application by the user.
- __Related items.__ With the appropriate entitlement, your app can access a file with the same name as a user-specified file, but a different extension. This can be used for accessing files that are functionally related (such as a subtitle file associated with a movie) or for saving modified files in a different format (such as re-saving an RTF flat file as an RTFD container after the user added a picture).
- __Temporary directories, command-line tool directories, and specific world-readable locations.__ A sandboxed app has varying degrees of access to files in certain other well-defined locations.

These policies are detailed further in the sections that follow.

### The App Sandbox Container Directory

The app sandbox container directory has the following characteristics:

- It is located at a system-defined path, within the user’s home directory. In a sandboxed app, this path is returned when your app calls the [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) function.
- Your app has unrestricted read/write access to the container and its subdirectories.
- macOS path-finding APIs (above the POSIX layer) refer to locations that are specific to your app.

  Most of these path-finding APIs refer to locations relative to your app’s container. For example, the container includes an individual `Library` directory (specified by the [NSLibraryDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nslibrarydirectory) search path constant) for use only by your app, with individual `Application Support` and `Preferences` subdirectories.

  Using your container for support files requires no code change (from the pre-sandbox version of your app) but may require one-time migration, as explained in [Migrating an App to a Sandbox](Migrating%20an%20App%20to%20a%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqnrnknltc).

  Some path-finding APIs (above the POSIX layer) refer to app-specific locations outside of the user’s home directory. In a sandboxed app, for example, the [NSTemporaryDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSTemporaryDirectory) function provides a path to a directory that is outside of the user’s home directory but specific to your app and within your sandbox; you have unrestricted read/write access to it for the current user. The behavior of these path-finding APIs is suitably adjusted for App Sandbox and no code change is needed.
- macOS establishes and enforces the connection between your app and its container by way of your app’s code signature.
- The container is in a hidden location, and so users do not interact with it directly. Specifically, the container is not for user documents. It is for files that your app uses, along with databases, caches, and other app-specific data.

  For a shoebox-style app, in which you provide the only user interface to the user’s content, that content goes in the container and your app has full access to it.

  __iOS Note:__ Because it is not for user documents, a macOS container differs from an iOS container. In addition, unlike in macOS, an iOS container contains the app itself.

  __iCloud Note:__ Apple’s iCloud technology, as described in _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_, uses the name “container” as well. There is no functional connection between an iCloud container and an App Sandbox container.

Thanks to code signing, no other sandboxed app can gain access to your container, even if it attempts to masquerade as your app by using your bundle identifier. Future versions of your app, however—provided that you use the same code signature and bundle identifier—do reuse your app’s container.

For each user, a sandboxed app’s container directory is created automatically when that user first runs the app. Because a container is within a user’s home directory, each user on a system gets their own container for your app.

### The Application Group Container Directory

In addition to per-app containers, in macOS 10.7.5 and 10.8.3 and later, an app can use the `com.apple.security.application-groups` entitlement to request access to one or more shared containers common to multiple apps produced by the same development team. The entitlement is an array of group identifier strings, each of which names a different group to which the app belongs. Group containers are intended for content that is not user-facing, such as shared caches or databases.

__Note:__ Apps that are members of an application group also gain the ability to share Mach and POSIX semaphores and to use certain other IPC mechanisms in conjunction with other group members. See [IPC and POSIX Semaphores and Shared Memory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltena) for more details.

An app’s sandbox is automatically enlarged to include all of the app’s group containers. The containers themselves are stored in `~/Library/Group Containers/<application-group-id>`, where `<application-group-id>` is the name of a group, as specified in one of the entitlement’s group identifier strings. Group identifiers must begin with your development team ID, followed by a period.

Beginning in macOS 10.8.3, your app can obtain the path to a group container by calling the [containerURLForSecurityApplicationGroupIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1412643-containerurlforsecurityapplicati) method of [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) with a valid group identifier.

__Note:__ In macOS 10.9, calling this method creates the group container directory automatically, along with `Library/Preferences`, `Library/Caches`, and `Library/Application Support` folders within that group container directory.

In previous versions, although the group container directory is part of your sandbox, the directory itself is not created automatically. Your app must create this directory as shown in Listing 2-1:

__Listing 2-1__  Creating an app group container directory

```
    NSFileManager *fm = [NSFileManager defaultManager];
    NSString *appGroupName = @"Z123456789.com.example.app-group"; /* For example */

    NSURL *groupContainerURL = [fm containerURLForSecurityApplicationGroupIdentifier:appGroupName];
    NSError* theError = nil;
    if (![fm createDirectoryAtURL: groupContainerURL withIntermediateDirectories:YES attributes:nil error:&theError]) {
        // Handle the error.
    }
```

You should organize the contents of this directory in the same way that any other `Library` folder is organized, using standard folder names—`Preferences`, `Application Support`, and so on—as needed.

For more details, see [Adding an Application to an Application Group](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoi) in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

### Powerbox and File System Access Outside of Your Container

Your sandboxed app can access file system locations outside of its container in the following three ways:

- At the specific direction of the user
- By using entitlements for specific file-system locations (described in [Entitlements and System Resource Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltc))
- When the file system location is in certain directories that are world readable

The macOS security technology that interacts with the user to expand your sandbox is called _Powerbox_. Powerbox has no API. Your app uses Powerbox transparently when you use the [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) classes. You enable Powerbox by setting an entitlement using Xcode, as described in [Enabling User-Selected File Access](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltm) in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

When you invoke an Open or Save dialog from your sandboxed app, the window that appears is presented not by AppKit but by Powerbox. Using Powerbox is automatic when you adopt App Sandbox—it requires no code change from the pre-sandbox version of your app. Accessory panels that you’ve implemented for opening or saving are faithfully rendered and used.

__Note:__ When you adopt App Sandbox, there are some important behavioral differences for the `NSOpenPanel` and `NSSavePanel` classes, described in [Open and Save Dialog Behavior with App Sandbox](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltq).

The security benefit provided by Powerbox is that it cannot be manipulated programmatically—specifically, there is no mechanism for hostile code to use Powerbox for accessing the file system. Only a user, by interacting with Open and Save dialogs via Powerbox, can use those dialogs to reach portions of the file system outside of your previously established sandbox. For example, if a user saves a new document, Powerbox expands your sandbox to give your app read/write access to the document.

When a user of your app specifies they want to use a file or a folder, the system adds the associated path to your app’s sandbox. Say, for example, a user drags the `~/Documents` folder onto your app’s Dock tile (or onto your app’s Finder icon, or into an open window of your app), thereby indicating they want to use that folder. In response, the system makes the `~/Documents` folder, its contents, and its subfolders available to your app.

If a user instead opens a specific file, or saves to a new file, the system makes the specified file, and that file alone, available to your app.

In addition, the system automatically permits a sandboxed app to:

- Connect to system input methods
- Invoke services chosen by the user from the Services menu.

  Some services are not sandbox safe. For example, the Finder app’s Open service might enable a compromised app to programmatically open an arbitrary file anywhere on the system, thus escaping its sandbox. Service providers are encouraged to mark these kinds of services as restricted (services are not restricted by default), in which case the service is still available to sandboxed apps, but only after the user is warned and gives explicit permission to continue. See the _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_ for more information.
- Open files chosen by the user from the Open Recent menu
- Participate with other apps by way of user-invoked copy and paste
- Read files that are world readable, in certain directories, including the following directories:

  - /bin
  - /sbin
  - /usr/bin
  - /usr/lib
  - /usr/sbin
  - /usr/share
  - /System
- Read and write files in directories created by calling [NSTemporaryDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSTemporaryDirectory).

  __Note:__ The `/tmp` directory is _not_ accessible from sandboxed apps. Use the `NSTemporaryDirectory` function to obtain a temporary location for your app’s temporary files.

After a user has specified a file they want to use, that file is within your app’s sandbox. The file is then vulnerable to attack if your app is exploited by malicious code: App Sandbox provides no protection. To provide protection for the files within your sandbox, follow the recommendations in _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_.

By default, files opened or saved by the user remain within your sandbox until your app terminates, except for files that were open _at the time_ that your app terminates. Such files reopen automatically by way of the macOS Resume feature the next time your app launches, and are automatically added back to your app’s sandbox.

To provide persistent access to resources located outside of your container, in a way that doesn’t depend on Resume, use security-scoped bookmarks as explained in [Security-Scoped Bookmarks and Persistent Resource Access](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltcnq).

### Related Items

The related items feature of App Sandbox lets your app access files that have the same name as a user-chosen file, but a different extension. This feature consists of two parts: a list of related extensions in the application’s `Info.plist` file and code to tell the sandbox what you’re doing.

There are two common scenarios where this makes sense:

- __Scenario 1:__

  Your app needs to be able to save a file with a different extension than that of the original file. For example, when you paste an image into an RTF file in TextEdit and save it, TextEdit changes the file’s extension from `.rtf` to `.rtfd` (and it becomes a directory).

  To handle this situation, you must use an [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) object to coordinate access to the file. Before you rename the file, call the [itemAtURL:willMoveToURL:](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1408668-itematurl) method. After you rename the file, call the [itemAtURL:didMoveToURL:](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1410328-item) method.
- __Scenario 2:__

  Your app needs to be able to open or save multiple related files with the same name and different extensions (for example, to automatically open a subtitle file with the same name as a movie file, or to allow for a SQLite journal file).

  To gain access to that secondary file, create a class that conforms to the [NSFilePresenter](https://developer.apple.com/documentation/foundation/nsfilepresenter) protocol. This object should provide the main file’s URL as its [primaryPresentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1415415-primarypresenteditemurl) property, and should provide the secondary file’s URL as its [presentedItemURL](https://developer.apple.com/documentation/foundation/nsfilepresenter/1414861-presenteditemurl) property.

  After the user opens the main file, your file presenter object should call the [addFilePresenter:](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1417120-addfilepresenter) class method on the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) class to register itself.

  __Note:__ In the case of a SQLite journal file, beginning in 10.8.2, journal files, write-ahead logging files, and shared memory files are automatically added to the related items list if you open a SQLite database, so this step is unnecessary.

In both scenarios, you must make a small change to the application’s `Info.plist` file. Your app should already declare a Document Types (`CFBundleDocumentTypes`) array that declares the file types your app can open.

For each file type dictionary in that array, if that file type should be treated as a potentially related type for open and save purposes, add the key `NSIsRelatedItemType` with a boolean value of `YES`.

To learn more about file presenters and file coordinators, read _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

### Open and Save Dialog Behavior with App Sandbox

Certain [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) methods behave differently when App Sandbox is enabled for your app:

- You cannot invoke the OK button using the [ok:](https://developer.apple.com/documentation/appkit/nssavepanel/1535364-ok) method.
- You cannot rewrite the user’s selection using the [panel:userEnteredFilename:confirmed:](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate/1524630-panel) method from the [NSOpenSavePanelDelegate](https://developer.apple.com/documentation/appkit/nsopensavepaneldelegate) protocol.

In addition, the effective, runtime inheritance path for the `NSOpenPanel` and `NSSavePanel` classes is different with App Sandbox, as illustrated in Table 2-2.

__Table 2-2__  Open and Save class inheritance with App Sandbox

| Without App Sandbox | NSOpenPanel : NSSavePanel : NSPanel : NSWindow : NSResponder : NSObject |
| With App Sandbox | NSOpenPanel : NSSavePanel : NSObject |

Because of this runtime difference, an `NSOpenPanel` or `NSSavePanel` object inherits fewer methods with App Sandbox. If you attempt to send a message to an `NSOpenPanel` or `NSSavePanel` object, and that method is defined in the [NSPanel](https://developer.apple.com/documentation/appkit/nspanel), [NSWindow](https://developer.apple.com/documentation/appkit/nswindow), or [NSResponder](https://developer.apple.com/documentation/appkit/nsresponder) classes, the system raises an exception. The Xcode compiler does _not_ issue a warning or error to alert you to this runtime behavior.

## Security-Scoped Bookmarks and Persistent Resource Access

Your app’s access to file-system locations outside of its container—as granted to your app by way of user intent, such as through Powerbox—does not automatically persist across app launches or system restarts. When your app reopens, you have to start over. (The one exception to this is for files open _at the time_ that your app terminates, which remain in your sandbox thanks to the macOS Resume feature).

Starting in macOS 10.7.3, you can retain access to file-system resources by employing a security mechanism, known as _security-scoped bookmarks_, that preserves user intent. Here are a few examples of app features that can benefit from this:

- A user-selected download, processing, or output folder
- An image browser library file, which points to user-specified images at arbitrary locations
- A complex document format that supports embedded media stored in other locations

### Two Distinct Types of Security-Scoped Bookmark

_Security-scoped bookmarks_, available starting in macOS 10.7.3, support two distinct use cases:

- An _app-scoped bookmark_ provides your sandboxed app with persistent access to a user-specified file or folder.

  For example, if your app employs a download or processing folder that is outside of the app container, obtain initial access by presenting an [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) dialog to obtain the user’s intent to use a specific folder. Then, create an app-scoped bookmark for that folder and store it as part of the app’s configuration (perhaps in a property list file or using the [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) class). With the app-scoped bookmark, your app can obtain future access to the folder.
- A _document-scoped bookmark_ provides a specific document with persistent access to a file.

  For example, a video editing app typically supports the notion of a project document that refers to other files and needs persistent access to those files. Such a project document can store security-scoped bookmarks to the files it refers to.

  Obtain initial access to a referred item by asking for user intent to use that item. Then, create a document-scoped bookmark for the item and store the bookmark as part of the document’s data.

  A document-scoped bookmark can be resolved by any app that has access to the bookmark data itself and to the document that owns the bookmark. This supports portability, allowing a user, for example, to send a document to another user; the document’s secure bookmarks remain usable for the recipient. The document can be a single flat file or a package containing multiple files.

  A document-scoped bookmark can point only to a file, not a folder, and only to a file that is not in a location used by the system (such as `/private` or `/Library`).

### Using Security-Scoped Bookmarks

To use either type of security-scoped bookmark requires you to perform five steps:

1. Set the appropriate entitlement in the [target](https://developer.apple.com/library/archive/featuredarticles/XcodeConcepts/Concept-Targets.html#//apple_ref/doc/uid/TP40009328-CH4) that needs to use security-scoped bookmarks.

   Do this once per target as part of configuring your Xcode project.
2. Create a security-scoped bookmark.

   Do this when a user has indicated intent (such as via Powerbox) to use a file-system resource outside of your app’s container, and you want to preserve your app’s ability to access the resource.
3. Resolve the security-scoped bookmark.

   Do this when your app later (for example, after app relaunch) needs access to a resource you bookmarked in step 2. The result of this step is a security-scoped URL.
4. Explicitly indicate that you want to use the file-system resource whose URL you obtained in step 3.

   Do this immediately after obtaining the security-scoped URL (or, when you later want to regain access to the resource after having relinquished your access to it).
5. When done using the resource, explicitly indicate that you want to stop using it.

   Do this as soon as you know that you no longer need access to the resource (typically, after you close it).

   After you relinquish access to a file-system resource, to use that resource again you must return to step 4 (to again indicate you want to use the resource).

   If your app is relaunched, you must return to step 3 (to resolve the security-scoped bookmark).

The first step in the preceding list, requesting entitlements, is the prerequisite for using either type of security-scoped bookmark. Perform this step as follows:

- To use app-scoped bookmarks in a target, set the `com.apple.security.files.bookmarks.app-scope` entitlement value to `true`.
- To use document-scoped bookmarks in a target, set the `com.apple.security.files.bookmarks.document-scope` entitlement value to `true`.

You can request either or both of these entitlements in a target, as needed. These entitlements are available starting in macOS 10.7.3 and are described in [Enabling Security-Scoped Bookmark and URL Access](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoa).

With the appropriate entitlements, you can create a security-scoped bookmark by calling the [bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions) method of the [NSURL](https://developer.apple.com/documentation/foundation/nsurl) class.

When you later need access to a bookmarked resource, resolve its security-scoped bookmark by calling the the [URLByResolvingBookmarkData:options:relativeToURL:bookmarkDataIsStale:error:](https://developer.apple.com/documentation/foundation/nsurl/1572035-urlbyresolvingbookmarkdata) method of the `NSURL` class.

In a sandboxed app, you cannot access the file-system resource that a security-scoped URL points to until you call the [startAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1417051-startaccessingsecurityscopedreso) method on the URL.

When you no longer need access to a resource that you obtained using security scope (typically, after you close the resource) you must call the [stopAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou) method on the resource’s URL.

Calls to start and stop access are not nested. When you call the [stopAccessingSecurityScopedResource](https://developer.apple.com/documentation/foundation/nsurl/1413736-stopaccessingsecurityscopedresou) method, you immediately lose access to the resource. If you call this method on a URL whose referenced resource you do not have access to, nothing happens.

__Warning:__ If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources are leaked, your app loses its ability to add file-system locations to its sandbox, such as via Powerbox or security-scoped bookmarks, until relaunched.

For detailed descriptions of the methods, constants, and entitlements to use for implementing security-scoped bookmarks in your app, read _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_, and read [Enabling Security-Scoped Bookmark and URL Access](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoa) in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

__Note:__ The Core Foundation framework also provides equivalent C functions for working with security-scoped bookmarks. For details, see the documentation for [CFURLCreateBookmarkData](https://developer.apple.com/documentation/corefoundation/1542923-cfurlcreatebookmarkdata), [CFURLCreateByResolvingBookmarkData](https://developer.apple.com/documentation/corefoundation/1543252-cfurlcreatebyresolvingbookmarkda),[CFURLStartAccessingSecurityScopedResource](https://developer.apple.com/documentation/corefoundation/1543318-cfurlstartaccessingsecurityscope), and [CFURLStopAccessingSecurityScopedResource](https://developer.apple.com/documentation/corefoundation/1542381-cfurlstopaccessingsecurityscoped) in _[CFURL Reference](https://developer.apple.com/documentation/corefoundation/cfurl-rd7)_.

## App Sandbox and Code Signing

In order to adopt App Sandbox, you also adopt code signing. Without a code signature, many of the features of App Sandbox, such as restricting your app to its own file system container, make little sense, because the system cannot unambiguously identify your app. More fundamentally, entitlements, including the one that activates App Sandbox in the first place, are physically stored in an app’s code signature. An app that is not code signed has no way to even ask to be put into a sandbox. Put simply, _unsigned code is not sandboxed_, regardless of what entitlements you request in the target build settings.

Modern Xcode makes it easy to adopt code signing for your app. You provide your developer program credentials, and Xcode handles most of the rest automatically. For more about code signing, including descriptions of both how it works and how you use it, read _[Code Signing Guide](../Code%20Signing%20Guide/About%20Code%20Signing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrz)_.

macOS enforces a tie between an app’s container and the app’s code signature. This important security feature ensures that no other sandboxed app can access your container. The mechanism works as follows:

1. When the system creates a container for an app, it sets an access control list (ACL) on that container. The initial access control entry in that list contains the app’s Designated Requirement (DR), which is part of the app’s signature that describes how future versions of the app can be recognized. See [Code Requirements](../Code%20Signing%20Guide/Understanding%20the%20Code%20Signature.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqmznknlti) in _[Code Signing Guide](../Code%20Signing%20Guide/About%20Code%20Signing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrz)_ for a description of the DR.
2. Each time an app with the same bundle ID launches, the system checks that the app’s code signature matches the designated requirements specified in one of the entries in the container’s ACL. If the system does not find a match, it prevents the app from launching.

macOS’s enforcement of container integrity impacts your development and distribution cycle. This is because, in the course of creating and distributing an app, the app is code signed using various signatures. Here’s how the process works:

1. Before you create a project, you obtain three code signing certificates from Apple: a development certificate, a distribution certificate, and (optionally) a Developer ID certificate.

   When used in conjunction with the corresponding private keys from your keychain, these certificates form three separate digital identities. For development and testing, you sign your app with your development identity. When you submit a version to the app store, you use your distribution identity. If you are distributing a version outside the app store, you use your Developer ID identity.
2. When the Mac App Store distributes your app, it is signed with an Apple code signature.

For testing and debugging, you may want to run both versions of your app: the version you sign and the version Apple signs. But macOS sees the Apple-signed version of your app as an intruder and won’t allow it to launch: Its code signature does not match the one expected by your app’s existing container.

If you try to run the Apple-signed version of your app, you get a crash report containing a statement similar to this:

```
Exception Type:  EXC_BAD_INSTRUCTION (SIGILL)
```

The solution is to adjust the access control list (ACL) on your app’s container to recognize the Apple-signed version of your app. Specifically, you add the designated code requirement of the Apple-signed version of your app to the app container’s ACL.

![bullet](attachments/Resources/1282/Images/task_2x.png)To adjust an ACL to recognize an Apple-signed version of your app

1. Open Terminal (in `/Applications/Utilities)`.
2. Open a Finder window that contains the Apple-signed version of your app.
3. In Terminal, enter the following command:

   ```
   asctl container acl add -file <path/to/app>
   ```

   In place of the `<path/to/app>` placeholder, substitute the path to the Apple-signed version of your app. Instead of manually typing the path, you can drag the app’s Finder icon to the Terminal window.

The container’s ACL now includes the designated code requirements for both versions of your app. macOS then allows you to run either version of your app.

You can use this same technique to share a container between (1) a version of an app that you initially signed with a development identity, such as the one you used in [App Sandbox Quick Start](App%20Sandbox%20Quick%20Start.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmrnknltg), and (2) a released version downloaded from the Mac App Store.

You can view the list of code requirements in a container’s ACL. For example, after adding the designated code requirement for the Apple-signed version of your app, you can confirm that the container’s ACL lists two permissible code requirements.

![bullet](attachments/Resources/1282/Images/task_2x.png)To display the list of code requirements in a container’s ACL

1. Open Terminal (in `/Applications/Utilities)`.
2. In Terminal, enter the following command:

   ```
   asctl container acl list -bundle <container name>
   ```

   In place of the `<container name>` placeholder, substitute the name of your app’s container directory. (The name of your app’s container directory is typically the same as your app’s bundle identifier.)

For more information about working with App Sandbox container access control lists and their code requirements, read the man page for the `asctl` (App Sandbox control) tool.

## External Tools, XPC Services, and Privilege Separation

Some app operations are more likely to be targets of malicious exploitation. Examples are the parsing of data received over a network, and the decoding of video frames. By using XPC, you can improve the effectiveness of the damage containment offered by App Sandbox by separating such potentially dangerous activities into their own address spaces.

Your app can also launch existing helper apps using Launch Services, but only if certain conditions are met.

__Important:__ While a child process spawned by an app (using `fork`, for example) simply inherits its parent’s sandbox, helper apps do not. Therefore, if you are submitting your app to the Mac App Store, verify that any embedded helper apps are also individually sandboxed.

To do this, run the following command on each embedded executable in your app bundle and confirm that each one has an App Sandbox entitlement:

```
codesign -dvvv --entitlements :- <executable-path>
```

where `<executable-path>` is the complete path to an executable binary in your app bundle.

The sections below explain these concepts in more detail.

### XPC Services

_XPC_ is an macOS interprocess communication technology that complements App Sandbox by enabling privilege separation. _Privilege separation_, in turn, is a development strategy in which you divide an app into pieces according to the system resource access that each piece needs. The component pieces that you create are called _XPC services_.

You create an XPC service as an individual target in your Xcode project. Typically, each service gets its own sandbox—specifically, it gets its own container and its own set of entitlements. In fact, if you are distributing your app in the Mac App Store, XPC services must be sandboxed. For apps distributed elsewhere, for example using Developer ID, sandboxing XPC services is optional, but strongly recommended.

__Note:__ In rare cases, your app might have a small piece of functionality that cannot be sandboxed. Rather than abandon App Sandbox altogether, you might relegate the ineligible code to an XPC service that is not sandboxed. It is easier to secure a smaller piece of code than a larger one, and in this way, the bulk of your app enjoys the benefits of App Sandbox.

In addition, an XPC service that you include with your app is accessible only by your app. These advantages add up to making XPC the best technology for implementing privilege separation in an macOS app.

By contrast, a child process created by using the [posix_spawn](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/posix_spawn.2.html#//apple_ref/doc/man/2/posix_spawn) function, by calling `fork` and [exec](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/exec.3.html#//apple_ref/doc/man/3/exec) (discouraged), or by using the [NSTask](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSTask/Description.html#//apple_ref/occ/cl/NSTask) class simply inherits the sandbox of the process that created it. You cannot configure a child process’s entitlements. For these reasons, child processes do not provide effective privilege separation.

To use XPC with App Sandbox:

- Confer minimal privileges to each XPC service, according to its needs.
- Design the data transfers between the main app and each XPC service to be secure.
- Structure your app’s bundle appropriately.

The life cycle of an XPC service, and its integration with Grand Central Dispatch (GCD), is managed entirely by the system. To obtain this support, you need only to structure your app’s bundle correctly.

For more on XPC, see [Creating XPC Services](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/Creating%20XPC%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2jnknltm) in _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

### Launching Helpers with Launch Services

A sandboxed app is allowed to launch a helper using Launch Services if at least one of these conditions has been met:

- Both the app and helper pass the Gatekeeper assessment. By default that means both are signed by the Mac App Store or with Developer ID.

  __Note:__ This does _not_ include your development ("Mac Developer") or distribution ("3rd Party Mac Developer Application") signing identities.
- The app is installed in `/Applications` and the app bundle and all contents are owned by root.
- The helper has been (manually) run at least once by the user.

If none of these conditions have been met, you'll see errors like the following:

- "Not allowing process 19920 to launch '/Applications/Main.app/Contents/Resources/Helper.app' because the security assessment verdict was denied."

  This message means that the Gatekeeper assessment was denied. You can confirm that with the `spctl` tool as follows:

  ```shell
  $ spctl --assess -vvvv /Applications/Main.app/

  /Applications/Main.app/: rejected
  origin=Mac Developer: Developer Name

  $ spctl --assess -vvvv /Applications/Main.app/Contents/Resources/Helper.app/

  /Applications/Main.app/Contents/Resources/Helper.app/: rejected
  origin=Mac Developer: Developer Name
  ```
- "The application “Helper” could not be launched because it is corrupt."

  "The operation couldn’t be completed. (OSStatus error -10827.)"

  This is the typical error if none of the above conditions have been fulfilled.

The results are the same whether you use Launch Services directly (by calling [LSOpenCFURLRef](https://developer.apple.com/documentation/coreservices/1442850-lsopencfurlref), for example) or indirectly (by calling the [launchApplicationAtURL:options:configuration:error:](https://developer.apple.com/documentation/appkit/nsworkspace/1534810-launchapplicationaturl) method in [NSWorkspace](https://developer.apple.com/documentation/appkit/nsworkspace), for example).

In addition, upon failure, in OS X 10.7.5 and earlier, you will also see a bogus `deny file-write-data /Applications/Main.app/Contents/Resources/Helper.app` sandbox violation. This error has no functional impact and can be ignored.

## IPC and POSIX Semaphores and Shared Memory

Normally, sandboxed apps cannot use Mach IPC, POSIX semaphores and shared memory, or UNIX domain sockets (usefully). However, by specifying an entitlement that requests membership in an application group, an app can use these technologies to communicate with other members of that application group.

__Note:__ System V semaphores are not supported in sandboxed apps.

UNIX domain sockets are straightforward; they work just like any other file.

Any semaphore or Mach port that you wish to access within a sandboxed app must be named according to a special convention:

- POSIX semaphores and shared memory names must begin with the application group identifier, followed by a slash (`/`), followed by a name of your choosing.
- Mach port names must begin with the application group identifier, followed by a period (`.`), followed by a name of your choosing.

For example, if your application group’s name is `Z123456789.com.example.app-group`, you might create two semaphores named `Z123456789.myappgroup/rdyllwflg` and `Z123456789.myappgroup/bluwhtflg`. You might create a Mach port named `Z123456789.com.example.app-group.Port_of_Kobe`.

__Note:__ The maximum length of a POSIX semaphore name is only 31 bytes, so if you need to use POSIX semaphores, you should keep your app group names _short_.

To learn more about application groups, read [The Application Group Container Directory](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobtfvbuqmznknltemi), then read [Adding an Application to an Application Group](../../Miscellaneous/Entitlement%20Key%20Reference/Enabling%20App%20Sandbox.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojvfvbuqnbnknltcoi) in _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

[Next](Designing%20for%20App%20Sandbox.md)[Previous](App%20Sandbox%20Quick%20Start.md)

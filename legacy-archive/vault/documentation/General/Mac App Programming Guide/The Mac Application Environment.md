---
title: Mac App Programming Guide
apple_id: TP40010543
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/MOSXAppProgrammingGuide/AppRuntime/AppRuntime.html
archived_at: '2026-07-15T07:34:20.626643Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mac App Programming Guide](About%20OS%20X%20App%20Design.md)


[Next](The%20Core%20App%20Design.md)[Previous](About%20OS%20X%20App%20Design.md)

# The Mac Application Environment

OS X incorporates the latest technologies for creating powerful and fun-to-use apps. But the technologies by themselves are not enough to make every app great. What sets an app apart from its peers is how it helps the user achieve some tangible goal. After all, users are not going to care what technologies an app uses, as long as it helps them do what they need to do. An app that gets in the user’s way is going to be forgotten, but one that makes work (or play) easier and more fun is going to be remembered.

You use Cocoa to write apps for OS X. Cocoa gives you access to all of the features of OS X and allows you to integrate your app cleanly with the rest of the system. This chapter covers the key parts of OS X that help you create great apps. In particular, this chapter describes some of the important ease-of-use technologies introduced in OS X v10.7. For a more thorough list of technologies available in OS X, see _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

OS X strives to provide an environment that is transparent to users and as easy to use as possible. By making hard tasks simple and getting out of the way, the system makes it easier for the user to be creative and spend less time worrying about the steps needed to make the computer work. Of course, simplifying tasks means your app has to do more of the work, but OS X provides help in that respect too.

As you design your app, you should think about the tasks that users normally perform and find ways to make them easier. OS X supports powerful ease-of-use features and design principles. For example:

- Users should not have to save their work manually. The document model in Cocoa provides support for saving the user’s file-based documents without user interaction; see [The Document Architecture Provides Many Capabilities for Free](The%20Core%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmznknltkmi).
- Apps should restore the user’s work environment at login time. Cocoa provides support for archiving the current state of the app’s interface (including the state of unsaved documents) and restoring that state at launch time; see [User Interface Preservation](The%20Core%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmznknltenq).
- Apps should support automatic termination so that the user never has to quit them. Automatic termination means that when the user closes an app’s windows, the app appears to quit but actually just moves to the background quietly. The advantage is that subsequent launches are nearly instant as the app simply moves back to the foreground; see [Automatic and Sudden Termination of Apps Improve the User Experience](The%20Core%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmznknltemq)
- You should consider providing your users with an immersive, full-screen experience by implementing a full-screen version of your user interface. The full-screen experience eliminates outside distractions and allows the user to focus on their content; see [Implementing the Full-Screen Experience](Implementing%20the%20Full-Screen%20Experience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqnrnknltc).
- Support trackpad gestures for appropriate actions in your app. Gestures provide simple shortcuts for common tasks and can be used to supplement existing controls and menu commands. OS X provides automatic support for reporting gestures to your app through the normal event-handling mechanism; see _[Cocoa Event Handling Guide](../../Cocoa/Cocoa%20Event%20Handling%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga3da2i)_.
- Consider minimizing or eliminating the user’s interactions with the raw file system. Rather than expose the entire file system to the user through the open and save panels, some apps, in the manner of iPhoto and iTunes, can provide a better user experience by presenting the user’s content in a simplified browser designed specifically for the app’s content. OS X uses a well-defined file system structure that allows you to place and find files easily and includes many technologies for accessing those files; see [The File System](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknlts).
- For apps that support custom document types, provide a Quick Look plug-in so that users can view your documents from outside of your app; see _[Quick Look Programming Guide](../../User%20Experience/Quick%20Look%20Programming%20Guide/Introduction%20to%20Quick%20Look%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamrq)_.
- Apps should support the fundamental features for the OS X user experience that make apps elegant and intuitive, such as direct manipulation and drag-and-drop. Users should remain in control, receive consistent feedback, and be able to explore because the app is forgiving with reversible actions; see _OS X Human Interface Guidelines_.

All of the preceding features are supported by Cocoa and can be incorporated with relatively little effort.

High-quality graphics and animation make your app look great and can convey a lot of information to the user. Animations in particular are a great way to provide feedback about changes to your user interface. So as you design your app, keep the following ideas in mind:

- Use animations to provide feedback and convey changes. Cocoa provides mechanisms for creating sophisticated animations quickly in both the AppKit and Core Animation frameworks. For information about creating view-based animations, see _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_. For information about using Core Animation to create your animations, see _[Core Animation Programming Guide](../../Cocoa/Core%20Animation%20Programming%20Guide/About%20Core%20Animation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmju)_.
- Include high-resolution versions of your art and graphics. OS X automatically loads high-resolution image resources when an app runs on a screen whose scaling factor is greater than 1.0. Including such image resources makes your app’s graphics look even sharper and crisper on those higher-resolution screens.

For information about the graphics technologies available in OS X, see [Media Layer](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/MediaLayer/MediaLayer.html#//apple_ref/doc/uid/TP40001067-CH273) in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

When you are ready to begin writing actual code, there are a lot of technologies available to make your life easier. OS X supports all of the basic features such as memory management, file management, networking, and concurrency that you need to write your code. In some cases, though, OS X also provides more sophisticated services (or specific coding conventions) that, when followed, can make writing your code even easier.

OS X is powered by a 64-bit Mach kernel, which manages processor resources, memory, and other low-level behaviors. On top of the kernel sits a modified version of the Berkeley Software Distribution (BSD) operating system, which provides interfaces that apps can use to interact with the lower-level system. This combination of Mach and BSD provides the following system-level support for your apps:

- _Preemptive multitasking_—All processes share the CPU efficiently. The kernel schedules processes in a way that ensures they all receive the time they need to run. Even background apps continue to receive CPU time to execute ongoing tasks.
- _Protected memory_—Each process runs in its own protected memory space, which prevents processes from accidentally interfering with each other. (Apps can share part of their memory space to implement fast interprocess communication but take responsibility for synchronizing and locking that memory appropriately.)
- _Virtual memory_—64-bit apps have a virtual address space of approximately 18 exabytes (18 billion billion bytes). (If you create a 32-bit app, the amount of virtual memory is only 4 GB.) When an app’s memory usage exceeds the amount of free physical memory, the system transparently writes pages to disk to make more room. Written out pages remain on disk until they are needed in memory again or the app exits.
- _Networking_ and _Bonjour_—OS X provides support for the standard networking protocols and services in use today. BSD sockets provide the low-level communication mechanism for apps, but higher-level interfaces also exist. Bonjour simplifies the user networking experience by providing a dynamic way to advertise and connect to network services over TCP/IP.

For detailed information about the underlying environment of OS X, see [Kernel and Device Drivers Layer](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/OSX_Technology_Overview/SystemTechnology/SystemTechnology.html#//apple_ref/doc/uid/TP40001067-CH207) in _[Mac Technology Overview](../../Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx)_.

Each process starts off with a single thread of execution and can create more threads as needed. Although you can create threads directly using POSIX and other higher-level interfaces, for most types of work it is better to create them indirectly using [block objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) with _Grand Central Dispatch (GCD)_ or _operation objects_, a Cocoa concurrency technology implemented by the `NSOperation` class.

GCD and operation objects are an alternative to raw threads that simplify or eliminate many of the problems normally associated with threaded programming, such as synchronization and locking. Specifically, they define an asynchronous programming model in which you specify only the work to be performed and the order in which you want it performed. The system then handles the tedious work required to schedule the necessary threads and execute your tasks as efficiently as possible on the current hardware. You should not use GCD or operations for work requiring time-sensitive data processing (such as audio or video playback), but you can use them for most other types of tasks.

For more information on using GCD and operation objects to implement concurrency in your apps, see _[Concurrency Programming Guide](../Concurrency%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojr)_.

The file system in OS X is structured to provide a better experience for users. Rather than exposing the entire file system to the user, the Finder hides any files and directories that an average user should not need to use, such as the contents of low-level UNIX directories. This is done to provide a simpler interface for the end user (and only in places like the Finder and the open and save panels). Apps can still access any files and directories for which they have valid permissions, regardless of whether they are hidden by the Finder.

When creating apps, you should understand and follow the conventions associated with the OS X file system. Knowing where to put files and how to get information out of the file system ensures a better user experience.

The OS X file system is organized in a way that groups related files and data together in specific places. Every file in the file system has its place and apps need to know where to put the files they create. This is especially important if you are distributing your app through the App Store, which expects you to put your app’s data files in specific directories.

Table 1-1 lists the directories with which apps commonly interact. Some of these directories are inside the home directory, which is either the user’s home directory or, if the app adopts App Sandbox, the app’s container directory as described in [App Sandbox and XPC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknlto). Because the actual paths can differ based on these conditions, use the [URLsForDirectory:inDomains:](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory) method of the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class to retrieve the actual directory path. You can then add any custom directory and filename information to the returned URL object to complete the path.

__Table 1-1__  Key directories for Mac apps

| Directory | Description |
| Applications directory | This is the installation directory for your app [bundle](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Bundle.html#//apple_ref/doc/uid/TP40008195-CH4). The path for the global Applications directory is `/Applications` but each user directory may have a local applications directory containing user-specific apps. Regardless, you should not need to use this path directly. To access resources inside your application bundle, use an [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) object instead.  For more information about the structure of your application bundle and how you locate resources, see [The OS X Application Bundle](Build-Time%20Configuration%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqobnknlte). |
| Home directory | The configuration of your app determines the location of the home directory seen by your app:   - For apps running in a sandbox in OS X v10.7 and later, the home directory is the app’s container directory. For more information about the container directory, see [The Keychain](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknltcny). - For apps running outside of a sandbox (including those running in versions of OS X before 10.7), the home directory is the user-specific subdirectory of `/Users` that contains the user’s files.   To retrieve the path to the home directory, use the [NSHomeDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSHomeDirectory) function. |
| Library directory | The Library directory is the top-level directory for storing private app-related data and preferences. There are several Library directories scattered throughout the system but you should always use the one located inside the current home directory.  Do not store files directly at the top-level of the Library directory. Instead, store them in one of the specific subdirectories described in this table.  In OS X v10.7 and later, the Finder hides the Library directory in the user’s home folder by default. Therefore, you should never store files in this directory that you want the user to access.  To get the path to this directory use the [NSLibraryDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nslibrarydirectory) search path key with the `NSUserDomainMask` domain. |
| Application Support directory | The Application Support directory is where your app stores any type of file that supports the app but is not required for the app to run, such as document templates or configuration files. The files should be app-specific but should never store user data. This directory is located inside the Library directory.  Never store files at the top level of this directory: Always put them in a subdirectory named for your app or company.  If the resources apply to all users on the system, such as document templates, place them in `/Library/Application Support`. To get the path to this directory use the [NSApplicationSupportDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/applicationsupportdirectory) search path key with the `NSLocalDomainMask` domain. If the resources are user-specific, such as workspace configuration files, place them in the current user’s `~/Library/Application Support` directory. To get the path to this directory use the [NSApplicationSupportDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/applicationsupportdirectory) search path key with the [NSUserDomainMask](https://developer.apple.com/documentation/foundation/nssearchpathdomainmask/nsuserdomainmask) domain. |
| Caches directory | The Caches directory is where you store cache files and other temporary data that your app can re-create as needed. This directory is located inside the Library directory.  Never store files at the top level of this directory: Always put them in a subdirectory named for your app or company. Your app is responsible for cleaning out cache data files when they are no longer needed. The system does not delete files from this directory.  To get the path to this directory use the [NSCachesDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nscachesdirectory) search path key with the `NSUserDomainMask` domain. |
| Movies directory | The Movies directory contains the user’s video files.  To get the path to this directory use the [NSMoviesDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nsmoviesdirectory) search path key with the `NSUserDomainMask` domain. |
| Music directory | The Music directory contains the user’s music and audio files.  To get the path to this directory use the [NSMusicDirectory](https://developer.apple.com/documentation/foundation/filemanager/searchpathdirectory/musicdirectory) search path key with the `NSUserDomainMask` domain. |
| Pictures directory | The Pictures directory contains the user’s images and photos.  To get the path to this directory use the [NSPicturesDirectory](https://developer.apple.com/documentation/foundation/nssearchpathdirectory/nspicturesdirectory) search path key with the `NSUserDomainMask` domain. |
| Temporary directory | The Temporary directory is where you store files that do not need to persist between launches of your app. You normally use this directory for scratch files or other types of short-lived data files that are not related to your app’s persistent data. This directory is typically hidden from the user.  Your app should remove files from this directory as soon as it is done with them. The system may also purge lingering files from this directory at system startup.  To get the path to this directory use the [NSTemporaryDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSTemporaryDirectory) function. |

Listing 1-1 shows an example of how to retrieve the base path to the `Application Support` directory and then append a custom app directory to it.

__Listing 1-1__  Getting the path to the `Application Support` directory

```
NSFileManager* fileManager = [NSFileManager defaultManager];
NSURL* appSupportDir = nil;

NSArray *urls = [fileManager URLsForDirectory:NSApplicationSupportDirectory inDomains:NSUserDomainMask];
if ([paths count] > 0) {
   appSupportDir = [[urls objectAtIndex:0] URLByAppendingPathComponent:@"com.example.MyApp"];
}
```

For more information about how to access files in well known system directories, see _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

In OS X, other processes may have access to the same files that your app does. Therefore, when working with files, you should use the file coordination interfaces introduced in OS X v10.7 to be notified when other processes (including the Finder) attempt to read or modify files your app is currently using. For example, coordinating file access is critical when your app adopts iCloud storage.

The file coordination APIs allow you to assert ownership over files and directories that your app cares about. Any time another process attempts to touch one of those items, your app is given a chance to respond. For example, when an app attempts to read the contents of a document your app is editing, you can write unsaved changes to disk before the other process is allowed to do its reading.

Using iCloud document storage, for example, you must incorporate file coordination because multiple apps can access your document files in iCloud. The simplest way to incorporate file coordination into your app is to use the `NSDocument` class, which handles all of the file-related management for you. See _[Document-Based App Programming Guide for Mac](../../Data%20Management/Document-Based%20App%20Programming%20Guide%20for%20Mac/About%20the%20Cocoa%20Document%20Architecture.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzz)_.

On the other hand, if you're writing a library-style (or “shoebox”) app, you must use the file coordination interfaces directly, as described in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

Disks in Macintosh computers are formatted using the HFS+ file system by default. However, Macintosh computers can interact with disks that use other formats so you should never code specifically to any one file system. Table 1-2 lists some of the basic file system attributes you may need to consider in your app and how you should handle them.

__Table 1-2__  Attributes for the OS X file system

| Attribute | Description |
| Case sensitivity | The HFS+ file system is case-insensitive but also case-preserving. Therefore, when specifying filenames and directories in your code, it is best to assume case-sensitivity. |
| Path construction | Construct paths using the methods of the [NSURL](https://developer.apple.com/documentation/foundation/nsurl) and [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) classes. The `NSURL` class is preferred for path construction because of its ability to specify not only paths in the local file system but paths to network resources. |
| File attributes | Many file-related attributes can be retrieved using the [getResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1408874-getresourcevalue) method of the `NSURL` class. You can also use an `NSFileManager` object to retrieve many file-related attributes. |
| File permissions | File permissions are managed using access control lists (ACLs) and BSD permissions. The system uses ACLs whenever possible to specify precise permissions for files and directories, but it falls back to using BSD permissions when no ACLs are specified.  By default, any files your app creates are owned by the current user and given appropriate permissions. Thus, your app should always be able to read and write files it creates explicitly. In addition, the app’s sandbox may allow it to access other files in specific situations. For more information about the sandbox, see [App Sandbox and XPC](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknlto). |
| Tracking file changes | Apps that cannot use the File Coordination interfaces (see [Coordinating File Access with Other Processes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknltcnq)) to track changes to files and directories can use the FSEvents API instead. This API provides a lower-level interface for tracking file system interactions and is available in OS X v10.5 and later.  For information on how to use the FSEvents API, see _[File System Events Programming Guide](../../Darwin/File%20System%20Events%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2teobz)_. |

To promote a more consistent user experience, applications submitted to the Mac App Store must follow certain rules about where they write files. Users can be confused when applications cause unexpected side effects on the file system (for example, storing databases in the user’s Documents folder, storing files in the user’s Library folder that are not recognizably associated with your application, storing user data in the user’s Library folder, and so on).

Your application must adhere to the following requirements:

- You may use Apple frameworks such as User Defaults, Calendar Store, and Address Book that implicitly write to files in specific locations, including locations your application is not allowed to access directly.
- Your application may write to temporary paths that you acquire using the appropriate Apple programming interfaces, such as the [NSTemporaryDirectory](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Functions/FoundationFunctions/Description.html#//apple_ref/c/func/NSTemporaryDirectory) function.
- Your application may write to the following directories:

  - `~/Library/Application Support/<app-identifier>`
  - `~/Library/<app-identifier>`
  - `~/Library/Caches/<app-identifier>`

  where _<app-identifier>_ is your application's bundle identifier, its name, or your company’s name. This must exactly match what is in App Store Connect for the application.

  Always use Apple programming interfaces such as the [URLsForDirectory:inDomains:](https://developer.apple.com/documentation/foundation/nsfilemanager/1407726-urlsfordirectory) function to locate these paths rather than hardcoding them. For more information, see _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.
- If your application manages libraries of pictures, music, or movies, the application may also write to the following directories:

  - `~/Pictures/<app-identifier>`
  - `~/Music/<app-identifier>`
  - `~/Movies/<app-identifier>`
- If the user explicitly chooses to save data in an alternate location (using a Save As dialog), your application may write to the chosen location.

The security technologies in OS X help you safeguard sensitive data created or managed by your app, and help minimize damage caused by successful attacks from hostile code. These technologies impact how your app interacts with system resources and the file system.

You secure your app against attack from malware by following the practices recommended in _[Secure Coding Guide](../../Security/Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_. But an attacker needs only to find a single hole in your defenses, or in any of the frameworks and libraries that you link against, to gain control of your app along with all of its privileges.

_App Sandbox_ provides a last line of defense against stolen, corrupted, or deleted user data if malicious code exploits your app. App Sandbox also minimizes the damage from coding errors. Its strategy is twofold:

1. App Sandbox enables you to describe how your app interacts with the system. The system then grants your app the access it needs to get its job done, and no more. For your app to provide the highest level of damage containment, the best practice is to adopt the tightest sandbox possible.
2. App Sandbox allows the user to transparently grant your app additional access by way of Open and Save dialogs, drag and drop, and other familiar user interactions.

You describe your app’s interaction with the system by way of setting entitlements in Xcode. An _entitlement_ is a key-value pair, defined in a [property list file](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44), that confers a specific capability or security permission to a target. For example, there are entitlement keys to indicate that your app needs access to the camera, the network, and user data such as the Address Book. For details on all the entitlements available in OS X, see _[Entitlement Key Reference](../../Miscellaneous/Entitlement%20Key%20Reference/About%20Entitlements.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcojv)_.

When you adopt App Sandbox, the system provides a special directory for use by your app—and only by your app—called a _container_. Your app has unfettered read/write access to the container. All OS X path-finding APIs, above the POSIX layer, are relative to the container instead of to the user’s home directory. Other sandboxed apps have no access to your app’s container, as described further in [Code Signing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbtfvbuqmrnknltq).

Your sandboxed app can access paths outside of its container in the following three ways:

- At the specific direction of the user
- By you configuring your app with entitlements for specific file-system locations, such as the Movies folder
- When a path is in any of certain directories that are world readable

The OS X security technology that interacts with the user to expand your sandbox is called _Powerbox_. Powerbox has no API. Your app uses Powerbox transparently when, for example, you use the [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) and [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) classes, or when the user employs drag and drop with your app.

Some app operations are more likely to be targets of malicious exploitation. Examples are the parsing of data received over a network, and the decoding of video frames. By using XPC, you can improve the effectiveness of the damage containment offered by App Sandbox by separating such potentially dangerous activities into their own address spaces.

_XPC_ is an OS X interprocess communication technology that complements App Sandbox by enabling privilege separation. _Privilege separation_, in turn, is a development strategy in which you divide an app into pieces according to the system resource access that each piece needs. The component pieces that you create are called _XPC services_. For details on adopting XPC, see _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

For a complete explanation of App Sandbox and how to use it, read _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

OS X employs the security technology known as [code signing](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AppSigning.html#//apple_ref/doc/uid/TP40008195-CH63) to allow you to certify that your app was indeed created by you. After an app is code signed, the system can detect any change to the app—whether the change is introduced accidentally or by malicious code. Various security technologies, including App Sandbox and parental controls, depend on code signing.

In most cases, you can rely on Xcode’s automatic code signing, which requires only that you specify a code signing identity in the build settings for your project. The steps to take are described in Code Signing Your App in _Tools Workflow Guide for Mac_. If you need to incorporate code signing into an automated build system, or if you link your app against third-party frameworks, refer to the procedures described in _[Code Signing Guide](../../Security/Code%20Signing%20Guide/About%20Code%20Signing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrz)_.

When you adopt App Sandbox, you must code sign your app. This is because entitlements (including the special entitlement that enables App Sandbox) are built into an app’s code signature.

OS X enforces a tie between an app’s container and the app’s code signature. This important security feature ensures that no other sandboxed app can access your container. The mechanism works as follows: After the system creates a container for an app, each time an app with the same bundle ID launches, the system checks that the app’s code signature matches a code signature expected by the container. If the system detects a mismatch, it prevents the app from launching.

For a complete explanation of code signing in the context of App Sandbox, read [App Sandbox in Depth](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxInDepth/AppSandboxInDepth.html#//apple_ref/doc/uid/TP40011183-CH3) in _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_.

A keychain is a secure, encrypted container for storing a user’s passwords and other secrets. It is designed to help a user manage their multiple logins, each with its own ID and password. You should always use keychain to store sensitive credentials for your app.

For more on the keychain, see Keychain Services Concepts in _Keychain Services Programming Guide_.

[Next](The%20Core%20App%20Design.md)[Previous](About%20OS%20X%20App%20Design.md)


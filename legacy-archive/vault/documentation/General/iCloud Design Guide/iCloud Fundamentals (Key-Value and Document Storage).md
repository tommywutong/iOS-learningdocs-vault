---
title: iCloud Design Guide
apple_id: TP40012094
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/iCloudFundametals.html
archived_at: '2026-07-15T07:34:40.454026Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Design Guide](About%20Incorporating%20iCloud%20into%20Your%20App.md)


[Next](Designing%20for%20Key-Value%20Data%20in%20iCloud.md)[Previous](About%20Incorporating%20iCloud%20into%20Your%20App.md)

# iCloud Fundamentals (Key-Value and Document Storage)

From the perspective of users, iCloud is a simple feature that automatically makes their personal content available on all their devices. To allow your app to participate in this “magic,” you design and implement your app somewhat differently than you would otherwise; in particular, you need to learn about your app’s roles when it participates with iCloud.

These roles, and the specifics of your iCloud adoption process, depend on your app. You design how your app manages its data, so only you can decide which iCloud supporting technologies your app needs and which ones it does not.

This chapter gets you started with the fundamental elements of iCloud key-value and document storage that all developers need to know.

To start developing an iCloud app, you must create an [App ID](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AppID.html#//apple_ref/doc/uid/TP40008195-CH64) and provisioning profile, described in _App Distribution Quick Start_. Then enable the iCloud service you want to use, described in Adding iCloud Support in _App Distribution Guide_. For a list of the app services that are available for your platform and type of developer program membership, see Supported Capabilities.

For most iCloud services, your app does not communicate directly with iCloud servers. Instead, the operating system initiates and manages uploading and downloading of data for the devices attached to an iCloud account. For all iCloud services, the high-level process for using those services is as follows:

1. Configure the access to your app’s _iCloud containers_. Configuration involves requesting entitlements and programmatically initializing those containers before using them.
2. Design your app to respond appropriately to changes in the availability of iCloud (such as if a user signs out of iCloud) and to changes in the locations of files (because instances of your app on other devices can rename, move, duplicate, or delete files).
3. Read and write using the APIs of the technology you are using.
4. The operating system coordinates the transfer of data to and from iCloud as needed.

The iCloud services encrypt data prior to transit and iCloud servers continue to store the data in an encrypted format, using secure tokens for authentication. For more information about data security and privacy concerns related to iCloud, see [iCloud security and privacy overview](http://support.apple.com/kb/HT4865).

To save data to iCloud, your app places data in special file system locations known as iCloud containers. An _iCloud container_ (also referred to as a _ubiquity container_) serves as the local representation of the corresponding iCloud storage. It is separate from the rest of your app’s data, as shown in Figure 1-1.

__Figure 1-1__  Your app’s main iCloud (ubiquity) container in context

!

To enable access to any iCloud containers, you request the appropriate entitlements.

The Capabilities tab of your Xcode project manages the creation of the entitlements and containers your app needs to access iCloud. After enabling the iCloud capability, Xcode creates an entitlements file (if one does not already exist) and configures it with the entitlements for the services you selected. As needed, Xcode can also handle any additional configuration, such as the creation of your app’s associated containers.

When you enable iCloud Documents, Xcode configures your app to access the iCloud container whose name is based on the app’s bundle ID. Most apps should only need access to the default container. If your apps share data among each other, configure your targets to share containers, described in Specifying Custom Containers. When an app has access to multiple container IDs, the first ID in the access list is special because it is the app’s primary iCloud container. In OS X, it is also the container whose contents are displayed in the `NSDocument` open and save dialogs.

For information about how to choose the correct iCloud technology for your app, see [Choose the Proper iCloud Storage API](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknlteoa).

In the Xcode target editor’s Summary pane, you can request access to as many iCloud containers as you need for your app. This feature is useful if you want multiple apps to share documents. For example, if you provide a free and paid version of your app, you might want users to retain access to their iCloud documents when they upgrade from the free version to the paid version. In such a scenario, configure both apps to write their data to the same iCloud container.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To configure a common iCloud container

1. Designate one of your iCloud-enabled apps as the primary app. That app’s iCloud container becomes the common container.

   For example, in the case of a free and paid app, you might designate the paid app as the primary app.
2. Enable the iCloud capability for each app.
3. Configure the primary app with only the default container identifier.
4. For each secondary app, enable the “Specify custom container identifiers” option and add the container identifier of the primary app to the list of containers.

When reading and writing files in both your primary and secondary apps, build URLs and search for files only in the common storage container. To retrieve the URL for the common storage container, pass the container identifier of your primary app to the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method of `NSFileManager`. Do not pass `nil` to that method because doing so returns the app’s default container, which is different for each app. Explicitly specifying the container identifier always yields the correct container directory.

For more information about how to configure app capabilities, see Adding Capabilities in _App Distribution Guide_.

If you provide a free and paid version of your app, and want to use the same key-value storage for both, you can do that.

![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To configure common key-value storage for multiple apps

1. Designate one of your iCloud-enabled apps as the primary app.

   That app’s iCloud container becomes the common container. For example, in the case of a free and paid app, you might designate the paid app as the primary app.
2. Enable the iCloud capability for each app.
3. Enable the key-value storage option for both apps.

   Xcode automatically adds entitlements to each app and assigns an iCloud container based on the app’s bundle ID.
4. For all but the primary app, change the iCloud container ID manually in the app’s `.entitlements` file.

   Set the value of the `com.apple.developer.ubiquity-kvstore-identifier` key to the ID of your primary app.

The structure of a newly created iCloud container is minimal—having only a `Documents` subdirectory. For document storage, you can arrange files inside the container in whatever way you choose. This allows you to define the structure as needed for your app, such as by adding custom directories and custom files at the top level of the container, as indicated in Figure 1-2.

__Figure 1-2__  The structure of an iCloud container directory

!

You can write files and create subdirectories within the `Documents` subdirectory. You can create files or additional subdirectories in any directory you create. Perform all such operations using an [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) object using file coordination. See [The Role of File Coordinators and Presenters](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileCoordinators/FileCoordinators.html#//apple_ref/doc/uid/TP40010672-CH11) in _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

The `Documents` subdirectory is the public face of an iCloud container. When a user examines the iCloud storage for your app (using Settings in iOS or System Preferences in OS X), files or file packages in the `Documents` subdirectory are listed and can be deleted individually. Files outside of the `Documents` subdirectory are treated as private to your app. If users want to delete anything outside of the `Documents` subdirectories of your iCloud containers, they must delete _everything_ outside of those subdirectories.

To see the user’s view of iCloud storage, do the following, first ensuring that you have at least one iCloud-enabled app installed:

- In iOS, open Settings. Then navigate to iCloud > Storage & Backup > Manage Storage.
- In OS X, open System Preferences. Then open the iCloud preferences pane and click Manage.

Each iCloud user receives an allotment of complimentary storage space and can purchase more as needed. Because this space is shared by a user’s iCloud-enabled iOS and Mac apps, a user with many apps can run out of space. For this reason, to be a good iCloud citizen, it’s important that your app saves to iCloud only what is needed in iCloud. Specifically:

- __DO__ store the following in iCloud:

  - User documents
  - App-specific files containing user-created data
  - Preferences and app state (using key-value storage, which does not count against a user’s iCloud storage allotment)
  - Change log files for a SQLite database (a SQLite database’s store file must never be stored in iCloud)
- __DO NOT__ store the following in iCloud:

  - Cache files
  - Temporary files
  - App support files that your app creates and can recreate
  - Large downloaded data files

There may be times when a user wants to delete content from iCloud. Provide UI to help your users understand that deleting a document from iCloud removes it from the user’s iCloud account _and_ from all of their iCloud-enabled devices. Provide users with the opportunity to confirm or cancel deletion.

One way to prevent files and directories from being stored in iCloud is to add the `.nosync` extension to the file or directory name. When iCloud encounters files and directories with that extension in the local container directory, it does not transfer them to the server. You might use this extension on temporary files that you want to store inside a file package, but that you do not want transferred with the rest of that package’s contents. Although items with the `.nosync` extension are not transferred to the server, they are still bound to their parent directory. When you delete the parent directory in iCloud, or when you evict the parent directory and its contents locally, the entire contents of that directory are deleted, including any `.nosync` items.

iCloud data lives on Apple’s iCloud servers, but the system maintains a local cache of data on each of the user’s devices, as shown in Figure 1-3. Local caching of iCloud data allows users to continue working even when the network is unavailable, such as when they turn on airplane mode.

__Figure 1-3__  iCloud files are cached on local devices and stored in iCloud

!

Because the local cache of iCloud data shares space with the other files on a device, in some cases there is not sufficient local storage available for all of a user’s iCloud data. The system addresses this issue by maintaining an optimized subset of files and other data objects locally. At the same time, the system keeps all file-related metadata local, thereby ensuring that your app’s users can access all their files, local or not. For example, the system might evict a file from its iCloud container if that file is not being used and local space is needed for another file that the user wants now; but updated metadata for the evicted file remains local. The user can still see the name and other information for the evicted file, and, if connected to the network, can open it.

Document-based apps usually do not need to manage the local availability of iCloud files and should let the system handle eviction of files. There are two exceptions:

- If a user file is not currently needed and unlikely to be needed soon, you can help the system by explicitly evicting that file from the iCloud container by calling the `NSFileManager` method [evictUbiquitousItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1409696-evictubiquitousitematurl).
- Conversely, if you explicitly want to ensure that a file is available locally, you can initiate a download to an iCloud container by calling the `NSFileManager` method [startDownloadingUbiquitousItemAtURL:error:](https://developer.apple.com/documentation/foundation/nsfilemanager/1410377-startdownloadingubiquitousitemat). For more information about this process, see [App Responsibilities for Using iCloud Documents](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlte).

When users launch your iCloud-enabled app for the first time, invite them to use iCloud. The choice should be all-or-none. In particular, it is best practice to:

- Use iCloud exclusively or use local storage exclusively; in other words, do not attempt to mirror documents between your iCloud container and your app’s local data container.
- Don’t prompt users again about whether they want to use iCloud vs. local storage, unless they delete and reinstall your app.

Early in your app launch process—in the [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method (iOS) or [applicationDidFinishLaunching:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428385-applicationdidfinishlaunching) method (OS X)—check for iCloud availability by getting the value of the [ubiquityIdentityToken](https://developer.apple.com/documentation/foundation/nsfilemanager/1408036-ubiquityidentitytoken) property of `NSFileManager`, as shown in Listing 1-1.

__Listing 1-1__  Obtaining the iCloud token

```
NSFileManager* fileManager = [NSFileManager defaultManager];
id currentiCloudToken = fileManager.ubiquityIdentityToken;
```

Access this property from your app’s main thread. The value of the property is a unique token representing the currently active iCloud account. You can compare tokens to detect if the current account is different from the previously used one, as explained in [Handle Changes in iCloud Availability](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknltm). To enable comparisons, archive the newly acquired token in the [user defaults](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Preferences.html#//apple_ref/doc/uid/TP40009071-CH20) database, using code like that shown in Listing 1-2. This code takes advantage of the fact that the `ubiquityIdentityToken` property conforms to the [NSCoding](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Protocols/NSCoding/Description.html#//apple_ref/occ/intf/NSCoding) protocol.

__Listing 1-2__  Archiving iCloud availability in the user defaults database

```
 if (currentiCloudToken) {
    NSData *newTokenData =
            [NSKeyedArchiver archivedDataWithRootObject: currentiCloudToken];
    [[NSUserDefaults standardUserDefaults]
            setObject: newTokenData
               forKey: @"com.apple.MyAppName.UbiquityIdentityToken"];
} else {
    [[NSUserDefaults standardUserDefaults]
            removeObjectForKey: @"com.apple.MyAppName.UbiquityIdentityToken"];
}
```

If the user enables airplane mode on a device, iCloud itself becomes inaccessible but the current iCloud account remains signed in. Even in airplane mode, the `ubiquityIdentityToken` property contains the token for the current iCloud account.

If a user signs out of iCloud, such as by turning off Documents & Data in Settings, the value of the `ubiquityIdentityToken` property changes to `nil`. To detect when a user signs in or out of iCloud, register as an observer of the [NSUbiquityIdentityDidChangeNotification](https://developer.apple.com/documentation/foundation/nsubiquityidentitydidchangenotification) notification, using code such as that shown in Listing 1-3. Execute this code at launch time or at any point before actively using iCloud.

__Listing 1-3__  Registering for iCloud availability change notifications

```
[[NSNotificationCenter defaultCenter]
    addObserver: self
       selector: @selector (iCloudAccountAvailabilityChanged:)
           name: NSUbiquityIdentityDidChangeNotification
         object: nil];
```

After obtaining and archiving the iCloud token and registering for the iCloud notification, your app is ready to invite the user to use iCloud. If this is the user’s first launch of your app with an iCloud account available, display an alert by using code like that shown in Listing 1-4. Save the user’s choice to the user defaults database and use that value to initialize the `firstLaunchWithiCloudAvailable` variable during subsequent launches. This code in the listing is simplified to focus on the sort of language you would display. In an app you intend to provide to customers, you would internationalize this code by using the [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) (or similar) macro, rather than using strings directly.

__Listing 1-4__  Inviting the user to use iCloud

```
if (currentiCloudToken && firstLaunchWithiCloudAvailable) {
    UIAlertView *alert = [[UIAlertView alloc]
                            initWithTitle: @"Choose Storage Option"
                                  message: @"Should documents be stored in iCloud and
                                                available on all your devices?"
                                 delegate: self
                        cancelButtonTitle: @"Local Only"
                        otherButtonTitles: @"Use iCloud", nil];
    [alert show];
}
```

Although the `ubiquityIdentityToken` property lets you know if a user is signed in to an iCloud account, it does not prepare iCloud for use by your app. In iOS, apps that use document storage must call the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method of the `NSFileManager` method for each supported iCloud container. Always call the `URLForUbiquityContainerIdentifier:` method from a background thread—not from your app’s main thread. This method depends on local and remote services and, for this reason, does not always return immediately. Listing 1-5 shows an example of how to initialize your app’s default container on a background thread.

__Listing 1-5__  Obtaining the URL to your iCloud container

```
dispatch_async (dispatch_get_global_queue (DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^(void) {
    myContainer = [[NSFileManager defaultManager]
            URLForUbiquityContainerIdentifier: nil];
    if (myContainer != nil) {
        // Your app can write to the iCloud container

    dispatch_async (dispatch_get_main_queue (), ^(void) {
        // On the main thread, update UI and state as appropriate
    });
    }
});
```

This example assumes that you have previously defined `myContainer` as an instance variable of type [NSURL](https://developer.apple.com/documentation/foundation/nsurl) prior to executing this code.

There are times when iCloud may not be available to your app, such as when the user disables the Documents & Data feature or signs out of iCloud. If the current iCloud account becomes unavailable while your app is running or in the background, your app must remove references to user-specific iCloud files and data and to reset or refresh user interface elements that show that data, as depicted in Figure 1-4.

__Figure 1-4__  Timeline for responding to changes in iCloud availability

!

To handle changes in iCloud availability, register to receive the [NSUbiquityIdentityDidChangeNotification](https://developer.apple.com/documentation/foundation/nsubiquityidentitydidchangenotification) notification. The handler method you register must do the following:

1. Retrieve the new value from the [ubiquityIdentityToken](https://developer.apple.com/documentation/foundation/nsfilemanager/1408036-ubiquityidentitytoken) property.
2. Compare the new value to the previous value, to find out if the user signed out of the account or signed in to a different account.
3. If the values are different, the previously used account is now unavailable. Discard any changes, empty your iCloud-related data caches, and refresh all iCloud-related user interface elements.

   If you want to allow users to continue creating content with iCloud unavailable, store that content in your app’s local data container. When the account is again available, move the new content to iCloud. It’s usually best to do this without notifying the user or requiring any interaction from the user.

Apple provides the following iCloud storage APIs, each with a different purpose:

- __Key-value storage__ is for discrete values such as preferences, settings, and simple app state.

  Use iCloud key-value storage for small amounts of data: stocks or weather information, locations, bookmarks, a recent documents list, settings and preferences, and simple game state. Every app submitted to the App Store or Mac App Store should take advantage of key-value storage.
- __iCloud document storage__ is for user-visible file-based content, Core Data storage, or for other complex file-based content.

  Use iCloud document storage for apps that work with file-based content, such as word-processing documents, diagrams or drawings, or games that need to keep track of complex game state.
- __CloudKit storage__ is for storing data as individual records in a private or public database accessible by all your app’s users.

  Use CloudKit in situations where key-value storage and document storage are insufficient for your needs. To learn more about CloudKit, read [Designing for CloudKit](Designing%20for%20CloudKit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqojnknltc).

Many apps benefit from using key-value storage with other types of storage. For example, say you develop a task management app that lets users apply keywords for organizing their tasks. You could employ iCloud document storage to store the task information and use key-value storage to save the user-entered keywords.

If your app uses Core Data, either for documents or for a shoebox-style app like iPhoto, use iCloud document storage. To learn how to adopt iCloud in your Core Data app, see [Designing for Core Data in iCloud](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html#//apple_ref/doc/uid/TP40012094-CH3-SW1).

If your app needs to store passwords, do not use iCloud storage APIs for that. The correct API for storing and managing passwords is Keychain Services, as described in _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_.

Use Table 1-1 to help you pick the iCloud storage scheme that is right for each of your app’s needs.

__Table 1-1__  Differences between document and key-value storage

| Element | iCloud document storage | Key-value storage | CloudKit |
| Purpose | User documents, complex private app data, and files containing complex app- or user-generated data. | Preferences and configuration data that can be expressed using simple data types. | Complex private app data and files, structured data, user-generated data, data that you want to share among users. |
| Entitlement keys | `com.apple.developer.``icloud-services`, `com.apple.developer.``icloud-container-identifiers` | `com.apple.developer.``ubiquity-kvstore-identifier` | `com.apple.developer.``icloud-services`, `com.apple.developer.``icloud-container-identifiers` |
| Data format | Files and file packages | [Property-list](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) data types only (numbers, strings, dates, and so on) | Records, represented as collections of key-value pairs where values are a subset of property-list data types, files, or references to other records. |
| Capacity | Limited only by the space available in the user’s iCloud account. | Limited to a total of 1 MB per app, with a per-key limit of 1 MB. | Limited only by the space available in the user’s iCloud account (private database) and the app’s allotted storage quota (public database). |
| Detecting availability | Call the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method for one of your ubiquity containers. If the method returns `nil`, document storage is not available. | Key-value storage is effectively always available. If a device is not attached to an account, changes created on the device are pushed to iCloud as soon as the device is attached to the account. | The public database is always available. The private database is available only when the value in the [ubiquityIdentityToken](https://developer.apple.com/documentation/foundation/filemanager/1408036-ubiquityidentitytoken) property is not `nil`. |
| Locating data | Use an [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) object to obtain live-updated information on available iCloud files. | Use the shared [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) object to retrieve values. | Use a [CKQuery](https://developer.apple.com/documentation/cloudkit/ckquery) object with a [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation) to search for records matching the predicate you specify. Use other operation objects to fetch records by ID. |
| Managing data | Use the [NSFileManager](https://developer.apple.com/documentation/foundation/filemanager) class to work directly with files and directories. | Use the default `NSUbiquitousKeyValueStore` object to manipulate values. | Use the classes of the CloudKit framework to manage data. |
| Resolving conflicts | Documents, as file presenters, automatically handle conflicts; in OS X, `NSDocument` presents versions to the user if necessary. For files, you manually resolve conflicts using file presenters. | The most recent value set for a key wins and is pushed to all devices attached to the same iCloud account. The timestamps provided by each device are used to compare modification times. | When saving records, assign an appropriate value to the [savePolicy](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/1447488-savepolicy) property of a `CKModifyRecordsOperation` object to specify how you want to handle conflicts. |
| Data transfer | In iOS, perform a coordinated read to get a local copy of an iCloud file; data is then automatically pushed to iCloud in response to local file system changes.  In OS X, iCloud files are always automatically pushed to iCloud in response to local file system changes. | Automatic, in response to local file system changes. | Use operation objects (or the convenience methods of the [CKOperation](https://developer.apple.com/documentation/cloudkit/ckoperation) and [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase) classes) to initiate data transfers. |
| Metadata transfer | Automatic, in response to local file system changes. | Not applicable (key-value storage doesn’t use metadata). | Not applicable |
| User interface | None provided by iOS. Your app is responsible for displaying information about iCloud data, if desired; do so seamlessly and with minimal changes to your app’s pre-iCloud UI.  In OS X, `NSDocument` provides iCloud UI. | Not applicable. Users don’t need to know that key-value data is stored in iCloud. | Your app is responsible for providing the interface needed to display data obtained from records. |

[Next](Designing%20for%20Key-Value%20Data%20in%20iCloud.md)[Previous](About%20Incorporating%20iCloud%20into%20Your%20App.md)


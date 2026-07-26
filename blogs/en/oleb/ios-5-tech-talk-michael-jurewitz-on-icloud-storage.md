---
title: 'iOS 5 Tech Talk: Michael Jurewitz on iCloud Storage'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2011/11/ios5-tech-talk-michael-jurewitz-on-icloud-storage/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:67d9d02d12b5e60c'
translated: false
---

> 原文：[iOS 5 Tech Talk: Michael Jurewitz on iCloud Storage](https://oleb.net/blog/2011/11/ios5-tech-talk-michael-jurewitz-on-icloud-storage/)　·　Ole Begemann

# iOS 5 Tech Talk: Michael Jurewitz on iCloud Storage

The next session I attended at the iOS 5 Tech Talk was [Michael Jurewitz’s](https://twitter.com/Jury) two-part talk titled **Adopting iCloud Storage.** Michael is Apple’s Developer Evangelist for Mac and iOS Application Frameworks, Developer Tools and Performance. The abstract of the iCloud session was:

> iCloud Storage enables your apps to keep user documents and data in iCloud, so your users can access the same content from all their computers and iOS devices. Gain a practical understanding of how iCloud Storage works and how to take advantage of it in your app. Learn how to use the Key-Value Store and see how UIDocument works with iCloud to store your app’s documents.

Michael began with a general overview of iCloud and its features. He then proceeded quickly to the provisioning side of things: what do developers have to do to set up their projects for iCloud?

# Provisioning and Entitlements

The process is really quite simple. First, you have to visit the [iOS Provisioning Portal](http://developer.apple.com/ios/manage/overview/index.action) and create a new App ID for your app. When you configure the App ID, make sure to check the “Enable for iCloud” option.

[![iOS Provisioning Portal: Enable for iCloud](https://oleb.net/media/ios-provisioning-portal-enable-for-icloud.png)](https://oleb.net/media/ios-provisioning-portal-enable-for-icloud.png)

Next, switch to the Provisioning section and create a new Development Provisioning Profile for the App ID you just generated. Once you have downloaded the provisioning profile and imported it into Xcode, you can close the browser.

The last step is to configure your Xcode project for iCloud. The way to do this is to create a so-called “Entitlements” file that contains the key(s) of the iCloud Storage containers. Normally, all you have to do is navigate to the Project settings in Xcode, select your Target and then the “Summary” tab. Scroll down and check the “Enable Entitlements” checkbox. If you have set the correct bundle ID and unless you have specific requirements (such as writing to the same section in your iCloud container from multiple apps), Xcode should have filled in all fields correctly.

[![iCloud entitlements in Xcode 4.2](https://oleb.net/media/xcode-4-2-icloud-entitlements.png)](https://oleb.net/media/xcode-4-2-icloud-entitlements.png)

# The iCloud Key-Value Store

> **Even if you don't care about the rest of iCloud, every app should adopt the key-value store to sync settings across devices.**

The key-value store is the iCloud component that is easiest to implement. Michael stressed several times during his talk that, even if you don’t want to use iCloud for anything else, you should seriously consider using the key-value store to sync your app’s preferences between devices. In fact, according to Michael, _every_ app should adopt it.

The key-value store is represented by the [`NSUbiquitousKeyValueStore`](http://developer.apple.com/library/ios/#documentation/Foundation/Reference/NSUbiquitousKeyValueStore_class/Reference/Reference.html) class and its API works a lot like the well-known `NSUserDefaults`.

It is important to note that you cannot rely on the presence of your data in `NSUbiquitousKeyValueStore`. Therefore, you always keep your app’s preferences in `NSUserDefaults` and only copy the values to the iCloud key-value store when they change. Also, the maximum size per key-value store (and also per key) is 64 KB. This should be more than enough to store your app’s settings but makes it clear that the key-value store is not meant for large data sets.

Your app should subscribe to the unambiguously named `NSUbiquitousKeyValueStoreDidChangeExternallyNotification` notification in order to get notified about remote changes to the data in the key-value store. The notification’s `userInfo` dictionary contains a key named `NSUbiquitousKeyValueStoreChangeReasonKey` (indicating a change on the remote server, an initial sync, or a storage space quota violation by your app). The `NSUbiquitousKeyValueStoreChangedKeysKey` key points to an array of keys whose values have changed in the external key-value store.

# iCloud Storage with UIDocument

Next, Michael talked about using iCloud storage in a document-based app such as Pages, Numbers and Keynote. If you build such an app, you should subclass [`UIDocument`](http://developer.apple.com/library/ios/#documentation/UIKit/Reference/UIDocument_Class/UIDocument/UIDocument.html) to create your own document class because `UIDocument` handles much of the stuff that is required to play nicely with iCloud.

How you store your document data internally is up to you. Your document subclass should override the `loadFromContents:ofType:error:` and `contentsForType:error:` methods, in which you read from or write to an `NSData` object, typically by using keyed archiving. Michael advised the audience to plan ahead from the beginning and include a version specifier in your document data. For example:

```
[encoder encodeObject:@"1.0" forKey:@"version"];
```

That way, should the user later try to open a document that was created with a newer version of the app, you can show them a helpful error message and ask them to update the app on the current device, too.

## Locating the Ubiquity Container

Before you can move any documents into the cloud, the first task in any app is to get a URL that points to the iCloud storage container (called the Ubiquity Container by Apple). Typically, you would add code like the following to `application:didFinishLaunchingWithOptions:`:

```
dispatch_queue_t globalQueue = dispatch_get_global_queue(QUEUE_PRIORITY_DEFAULT, 0);
dispatch_asynch(globalQueue, ^{
    NSFileManager *fileManager = [[NSFileManager alloc] init];
    NSURL *ubiquityContainer = [fileManager URLForUbiquityContainerIdentifier:nil];

    dispatch_queue_t mainQueue = dispatch_get_main_queue();
    dispatch_async(mainQueue, ^{
        [self updateWithUbiquityContainer:ubiquityContainer];
    });
});
```

It is important to do this asynchronously because the call to `URLForUbiquityContainerIdentifier:` can possibly block for a long time. And you never want to block the main thread. The `NSFileManager` method `URLForUbiquityContainerIdentifier:` is at the same time the method to call when you want to know whether iCloud is available or not. It returns `nil` if iCloud storage is unavailable for the current user or device.

## Use `NSMetadataQuery` to Discover Changes in the Ubiquity Container

When your app works with iCloud, it needs to be notified of external changes to the ubiquity container. The way to set this up is to run a [`NSMetadataQuery`](http://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSMetadataQuery_Class/Reference/Reference.html), which uses notifications to tell us about changes. You must set both a search scope and a predicate for the query:

```
NSMetadataQuery *query = [[NSMetadataQuery alloc] init];
[query setSearchScopes:[NSArray arrayWithObjects:NSMetadataQueryUbiquitousDocumentsScope, nil]];
[query setPredicate:[NSPredicate predicateWithFormat:@"NSMetadataItemFSNameKey == '*.txt'"]];

// Subscribe to update notifications
NSNotificationCenter *notificationCenter = [NSNotificationCenter defaultCenter];
[notificationCenter addObserver:self selector:@selector(metadataQueryDidUpdate:) name:NSMetadataQueryDidUpdateNotification object:query];
[notificationCenter addObserver:self selector:@selector(metadataQueryDidFinish:) name:NSMetadataQueryDidFinishGatheringNotification object:query];

[query startQuery];
```

Notice how you can work with wildcards in the predicate to filter the filenames you are interested in. The query’s search scope can either be `NSMetadataQueryUbiquitousDocumentsScope`, which limits the search to the _Documents_ directory inside the ubiquity container or `NSMetadataQueryUbiquitousDataScope`, which searches everywhere else in the ubiquity container.

Generally, you are free to store your documents anywhere you want in the ubiquity container. If you want to store files in directories, you have to create them and all intermediate directories yourself.

## Creating a Document in the Ubiquity Container

This is very simple. Once you have the location of the ubiquity container, create a URL that points to a file inside (consider using [UUIDs](https://en.wikipedia.org/wiki/Uuid) for your filenames) and create the new document at that location:

```
// saveLocation should be a URL in the ubiquity container
MyDocument *newDocument = [[MyDocument alloc] initWithFileURL:saveLocation];
[newDocument saveToURL:newDocument.fileURL forSaveOperation:UIDocumentSaveForCreating] completionHandler:^(BOOL success) {
    if (success) {
        // Saving succeeded
        ...
    } else {
        // Saving failed
        ...
    }
}];
```

### Updating a Document

The controller managing the document should subscribe to `UIDocumentStateChangedNotification` to discover changes to the state of the document in iCloud:

```
[[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(documentStateChanged:) name:UIDocumentStateChangedNotification object:self.document];
```

When your controller receives this notification, it should check the new `documentState` and react accordingly:

```
// Handle document state changes
- (void)documentStateChanged:(NSNotification *)notification
{
    UIDocumentState state = self.document.documentState;
    if (state & UIDocumentStateEditingDisabled) {
        // Disable editing in your UI
        ...
    }

    if (state & UIDocumentStateInConflict) {
        // Show a discrete indication of a merge conflict
        ...
    }

    if (state & UIDocumentStateSavingError) {
        // Document could not be saved
        ...
    }

    if (state & UIDocumentStateNormal) {
        // Document is normal
        // Clear any conflict/error indicators in your UI
        ...
    }
}
```

Michael advised developers to handle version conflicts as discretely as possible. Users don’t like conflict or merge dialogs.

## Core Data

In the third part of the session, Michael talked about integrating Core Data with iCloud. Specifically, imagine you have a “shoebox-style” app such as iTunes or iPhoto where the user interacts with a single library of items (that the app manages with Core Data) as opposed to multiple documents.

### Getting Started

It turns out that getting started with iCloud in this case is surprisingly easy. All you have to do is specify two additional options when creating your persistent store:

- `NSPersistentStoreUbiquitousContentNameKey`: This one is required. The value must be a unique string that identifies your store file.
- `NSPersistentStoreUbiquitousContentURLKey`: Not required but recommended. Its value indicates where in the ubiquity container the Core Data transaction logs should be stored.

That last sentence already hints at how iCloud storage works with Core Data. Instead of copying the SQLite database file between devices, Core Data only stores transaction logs in iCloud. These logs can then be used to recreate the database file on another device. This process is not only much safer (SQLite files are not designed to be accessed from multiple processes), it also saves bandwidth because only the recent changes have to be transferred via the cloud (and Apple has optimized the transaction logs to be very small).

While technically not necessary, Michael recommended to store the actual Core Data data store file also in the ubiquity container. You should place it into a directory ending with the _.nosync_ extension to tell iCloud that it should not sync the folder’s contents between devices.

As in the cases discussed before, the aptly named `NSPersistentStoreDidImportUbiquitousContentChangesNotification` notification serves as your app’s interface to discover remote changes to the data store. When you receive the notification, your app should basically refresh all data views to make sure it displays the most recent content.

### Merging iCloud Changes

A great advantage of Core Data over your own `UIDocument` storage is the potential for intelligent data merging. If a user edits a “normal” document on two devices while the network is down and then resyncs with iCloud, the system usually has no other option than to mark these changes as a conflict. It is up to your app to intelligently merge these changes into the canonical version of the document, which is a very hard problem.

A Core Data-based store is much more granular, however. As long as the user does not edit the same field of the same record on both devices, you can accept that Core Data will be able to merge the changes from both devices automatically.

The important thing to note is that you have to set a merge policy on your managed object context. The default merge policy of `NSErrorMergePolicy` would just raise an error on every conflict, which is probably not what you want. Michael recommended to set the merge policy to `NSMergeByPropertyObjectTrumpMergePolicy`.

## Going It Alone

> **Did I mention that UIDocument does all this for you automatically?**

Towards the end of his talk, Michael explained what you have to do if you want to use iCloud storage with files that are not based on `UIDocument`. I will not repeat everything he mentioned here because this post is already long enough. Let me just say here that the main problem is that a data file that resides in iCloud can possibly be accessed for both reading and writing by multiple processes at the same time. To avoid data corruption, the system has to coordinate every read and write access to that file.

To play along with this requirement, your app must use the [`NSFileCoordinator`](http://developer.apple.com/library/ios/#documentation/Foundation/Reference/NSFileCoordinator_class/Reference/Reference.html) class whenever it wants to access a file in iCloud storage. It must also implement the [`NSFilePresenter`](http://developer.apple.com/library/ios/#documentation/Foundation/Reference/NSFilePresenter_protocol/Reference/Reference.html) protocol to be notified of remote changes.

During this part of the talk, every second sentence Michael said was, Did I mention that UIDocument does all this for you automatically?

# Tips and Tricks

## Moving a File into or out of the Ubiquity Container

Use the `NSFileManager` method [`setUbiquitous:itemAtURL:destinationURL:error:`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/nsfilemanager_Class/Reference/Reference.html#//apple_ref/doc/uid/20000305-SW75) to move files between iCloud and your application sandbox. Call the method with `YES` and `destinationURL` being a URL inside the ubiquity container to move a file into the container. Pass `NO` as the first argument and a URL in your app’s sandbox to `destinationURL` to move a file out. The latter call will download the file onto the device and remove it from iCloud storage.

Note that you must call this method inside a `dispatch_async()` block because it can block the thread for a significant amount of time.

## Sharing a Document in iCloud

You can obtain a URL for sharing an iCloud document with the `NSFileManager` method [`URLForPublishingUbiquitousItemAtURL:expirationDate:error:`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/nsfilemanager_Class/Reference/Reference.html#//apple_ref/doc/uid/20000305-SW73). You can share the URL returned by this method with other users to allow them to download a copy of a cloud-based file. Note that this method makes a copy of the file. It is not possible for other users to edit the original.

## Telling the State of a File

`NSURL` has several new constants that can be used to query the state of an iCloud-based file: `NSURLIsUbiquitousItemKey`, `NSURLUbiquitousItemHasUnresolvedConflictsKey`, `NSURLUbiquitousItemIsDownloadedKey`, `NSURLUbiquitousItemIsDownloadingKey`; `NSURLUbiquitousItemIsUploadedKey`, `NSURLUbiquitousItemIsUploadingKey` `NSURLUbiquitousItemPercentDownloadedKey`, `NSURLUbiquitousItemPercentUploadedKey`.

Use the [`resourceValuesForKeys:error:`](http://developer.apple.com/library/ios/documentation/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/doc/uid/20000301-SW40) method to query the state of these attributes.

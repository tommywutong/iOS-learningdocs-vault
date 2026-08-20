---
title: 'Your Third iOS App: iCloud'
apple_id: TP40011317
resource_type: Guide
platform: iOS
topic: General
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloud101/NextSteps/NextSteps.html
archived_at: '2026-07-15T07:34:35.914043Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Your Third iOS App: iCloud](About%20Your%20Third%20iOS%20App.md)


[Next](Code%20Listings.md)[Previous](Troubleshooting.md)

# Next Steps

In this tutorial, you created a sophisticated iOS app that used iCloud to save its documents. Designing an app to support iCloud involves many decisions, though, and this tutorial only scratches the surface. This chapter suggests some directions you might take next as you continue to learn about integrating iCloud into your apps.

Apps that store documents in iCloud must be prepared to handle conflicts between different versions of that document. Conflicts can occur when changes are made to the same document on two different devices. For example, a conflict can occur when the user edits the same document on two different devices that are currently in Airplane Mode, because they are unable to transmit changes to the iCloud servers.

Although conflicts do not happen too often, apps need to be prepared to handle them. To detect conflicts in a document-based app, you must register for the state change notifications of the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class. If the document enters the [UIDocumentStateInConflict](https://developer.apple.com/documentation/uikit/uidocumentstate/uidocumentstateinconflict) state, your app needs to retrieve the conflicting document versions and decide how best to proceed.

For more information about handling version conflicts, see _[iCloud Design Guide](../iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_.

For documents that grow to be large, you might want to provide some feedback to the user when sent to and from iCloud. Instances of the [NSURL](https://developer.apple.com/documentation/foundation/nsurl) class maintain attributes that tell you the current transfer status of the underlying file. You can use these values to determine whether a file is downloaded to the local device and whether changes have been uploaded to iCloud. You can also use these values to check the current progress of download and upload operations.

For information about accessing the iCloud status attributes, see _[NSURL Class Reference](https://developer.apple.com/documentation/foundation/nsurl)_.

One of the advantages of calling the [URLForUbiquityContainerIdentifier:](https://developer.apple.com/documentation/foundation/nsfilemanager/1411653-urlforubiquitycontaineridentifie) method shortly after launch is that it lets you determine whether iCloud is available early in the life of your app. A return value of `nil` from the method means that the iCloud container directory could not be reached—usually because the user’s device is not configured to use iCloud. (During development, being unable to access iCloud usually means there is an error in the configuration of your app’s iCloud entitlements.)

Your app should provide a smooth fallback position in cases when iCloud is unavailable. For example, you might store new user documents in the local sandbox and transfer them to iCloud at the first opportunity. You should do this quietly and not bother the user.

You should also be aware that the user can turn off your app’s access to iCloud altogether by turning off the Documents & Data option or by deleting the current iCloud account. Although this should not happen often, you should still code your apps defensively and be prepared for this kind of change while your app is suspended or running in the background. Specifically, after having moved to the background and returned to the foreground, call the `URLForUbiquityContainerIdentifier:` method to verify that iCloud is still available before attempting to access any files or documents in your app’s container directory.

The Simple Text Editor app searches for documents and presents them in the order in which they are discovered. However, you might want to provide a more deterministic way of presenting documents in your own apps. For example, you could display them in alphabetical order or maintain a record of the current order and write that information to iCloud as well.

The tutorial used a combination of a static name and a dynamic number for new document names, but your own apps should be more creative. Here are some tips for creating good document names:

- Use an initial name that is indicative of the content your app creates. Do not just create “Untitled” documents. Make the document names more specific. For example, a painting program might use “My Creation” or “Canvas” for the base document name.
- Provide a simple but unobtrusive way for the user to change document names. Let the user tap the document name and edit it in place. Do not post alerts or use an interface that pulls the user out of the current context.
- For documents with text content, consider using that content (instead of the filename) to identify the document. This approach is similar to the way the Notes app displays information. Because users do not have direct access to the underlying file system, displaying the initial document content is often better than displaying a file name.

If you want your app to share preferences and other noncritical configuration data, use the [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) class to do so using iCloud. This class behaves in a similar way to the `NSUserDefaults` class. It provides a simple interface for setting key-value pair data in iCloud.

For more information about using the `NSUbiquitousKeyValueStore` class, see _[Preferences and Settings Programming Guide](../../Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_.

Core Data provides a set of sophisticated tools for modeling your app’s data structures and managing them efficiently in your app. Unlike live SQLite databases, Core Data stores can be shared among a user’s devices through iCloud. Core Data manages this operation by sending only the changes to iCloud, so that they can be incorporated into local databases on each device.

For more information about using Core Data with iCloud, see [Designing for Core Data in iCloud](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html#//apple_ref/doc/uid/TP40012094-CH3).

At some point, you might need to understand more about the role file coordinators play in iCloud. Although the [UIDocument](https://developer.apple.com/documentation/uikit/uidocument) class provides the file coordinator for many actions, some actions may require you to create a file coordinator yourself. For example, when deleting files in Simple Text Editor, you had to create a file coordinator of your own and use it to perform the operation. Therefore, it is important that you understand the role file coordinators play in your app and when you might need to use them.

For more information about when to use file coordinators, see _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

[Next](Code%20Listings.md)[Previous](Troubleshooting.md)


---
title: Document Picker Programming Guide
apple_id: TP40014451
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentPickerProgrammingGuide/CreatinganOutstandingUserExperience/CreatinganOutstandingUserExperience.html
archived_at: '2026-07-15T07:31:55.712445Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Picker Programming Guide](About%20the%20Document%20Picker.md)


[Next](Document%20Revision%20History.md)[Previous](Accessing%20Documents.md)

# Creating an Outstanding User Experience

Users will demand the extra flexibility that the open and move operations provide; however, this additional flexibility creates a more complex user experience. Users can now “save” files in different locations, using different document providers or containers inside iCloud Drive. Users must, therefore, remember where they stashed their files. Furthermore, your app no longer has complete control over these files. Users can log into (and log out of) services such as iCloud. The network or remote server may not be available. Files may appear and disappear.

It’s vitally important that your app manage and mitigate all of these additional sources of complexity, providing your users with the best experience possible.

The document picker gives your app four different operations for transferring files: import, export, open and move. Unfortunately, most users won’t be aware of the subtile differences between these options. If you simply place all four in the same toolbar or action sheet, most users wont understand why they should choose one option over another.

Instead, your app should guide the user toward the correct operation based on the user’s current context. For example, you may want to place the open operation inside the list of recently used documents.

Import and open operations are part of your app’s document handling and should be grouped with similar features. Export and move operations affect the document itself and should be attached to the document.

Your app also needs to clearly distinguish between operations that copy the documents and operations that provide access to external documents. In many cases, you may want to simplify your app by removing the import and export operations entirely. The open and move operations give the user the most power and flexibility when it comes to working with their documents. Your app should emphasize these operations over simple imports and exports.

Users should use the document picker only to open new documents. After users have opened a document once, your app should provide an easier way to access that document again. For example, have your app present a list of recently opened documents, including both local and external documents. This list lets users reopen a document without having to remember where it is stored.

You can use an [NSMetadataQuery](https://developer.apple.com/documentation/foundation/nsmetadataquery) object to search for files that have been accessed from iCloud Drive—this would include the public iCloud container and any other app’s iCloud container. To gather this data, use the query’s [NSMetadataQueryAccessibleUbiquitousExternalDocumentsScope](https://developer.apple.com/documentation/foundation/nsmetadataqueryaccessibleubiquitousexternaldocumentsscope) constant for the scope.

When the user opens a file from an external iCloud container (or moves a file to that container), the system creates an external document reference for the file inside your app’s local iCloud container. The query identifies these references and returns a list of the files they refer to.

By default, the query returns security-scoped URLs for all external documents. You can access the URL to the local reference from the [NSMetadataItem](https://developer.apple.com/documentation/foundation/nsmetadataitem) attributes using the `NSMetadataUbiquitousItemURLInLocalContainerKey` key. In general, you use the local URLs only when you need to move or reorganize the references.

An `NSMetadataQuery` instance can gather information only on files accessed through iCloud Drive. If the user accesses a file using a third-party document provider, you must save a secure bookmark for that file instead. When the document picker returns a URL, check the URL’s [NSURLIsUbiquitousItemKey](https://developer.apple.com/documentation/foundation/urlresourcekey/1416894-isubiquitousitemkey) key. If the URL is not a ubiquitous URL, save a bookmark to the file using the [bookmarkDataWithOptions:includingResourceValuesForKeys:relativeToURL:error:](https://developer.apple.com/documentation/foundation/nsurl/1417795-bookmarkdatawithoptions) method and passing in the [NSURLBookmarkCreationWithSecurityScope](https://developer.apple.com/documentation/foundation/nsurlbookmarkcreationoptions/nsurlbookmarkcreationwithsecurityscope) option. Calling this method creates a bookmark containing a security-scoped URL that you can use to open the file without further user intervention.

URLs returned by an open or move operation or a metadata query can refer to placeholders instead of actual files. When you attempt to access a placeholder with a coordinated read, the system automatically downloads the file. If it is a large file (or the user is on a slow network) the user may experience unexpected delays before the file becomes available. As much as possible, you want your app to let the user know when a choice might trigger a download and also let them know when a download is in progress.

When displaying a list of these files, make it clear whether the URL points to an existing file that the user can open immediately or to a placeholder that the user must download. Check to see whether a file exists at the given URL. If it doesn’t, the URL is a placeholder.

Also, set the user’s expectations for the download by displaying the file’s size from the placeholder’s metadata. There are two ways to access the placeholder’s metadata. First, you can use the [NSURL](https://developer.apple.com/documentation/foundation/nsurl) instance’s [getPromisedItemResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1414238-getpromiseditemresourcevalue) method.

You can avoid these race conditions by using a file coordinator. Use the [NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly](https://developer.apple.com/documentation/foundation/nsfilecoordinator/readingoptions/1411727-immediatelyavailablemetadataonly) option to access a placeholder’s metadata without downloading the file. You can then access the metadata on the URL passed into the accessor block. You still need to use [getPromisedItemResourceValue:forKey:error:](https://developer.apple.com/documentation/foundation/nsurl/1414238-getpromiseditemresourcevalue) to access the metadata, however.

Although using a file coordinator avoids the race conditions mentioned above, it does not completely prevent the problem. Files can still be deleted, renamed, or moved after the query returns but before you set up the [NSFileCoordinator](https://developer.apple.com/documentation/foundation/nsfilecoordinator) instance. Therefore, you must still handle some error cases.

As soon as you start working with files outside your app’s sandbox, you no longer have complete control over that file. Other processes can also access the file. These processes include your app itself, the Document Provider extension that provides access to the file, and the document provider’s containing app.

Because multiple processes may be reading and writing to this URL concurrently, always use a file coordinator when accessing these URLs. Keep in mind that file coordination does more than just provide safe access. When you perform a coordinated read on a placeholder, you trigger the creation of the actual file. The system asks the Document Provider extension to produce the document. The extension then downloads or otherwise makes the file accessible. Errors that occur during this process are returned to your app’s file coordinator.

For all of these reasons, your app must be prepared to handle file coordination errors and provide reasonable feedback to the user. Remember that these errors may be coming from third-party extensions that you have never heard about. So be careful when making assumptions about the error’s contents.

Finally, coordinated reads and writes may trigger file transfers that can take an arbitrarily long amount of time. Be sure to perform these reads and writes on a background thread or use the asynchronous [coordinateAccessWithIntents:queue:byAccessor:](https://developer.apple.com/documentation/foundation/nsfilecoordinator/1411533-coordinate)method. Also, be sure to give some visual indication that a download is in progress, and give the user some way to cancel this download.

Files outside your app’s sandbox can change even while you are presenting them. Therefore you want to update the user interface as soon as new information is available. Whenever you present a document’s contents to the user, use a file presenter to track changes and conflicts.

File presenters notify you when any of the following conditions occur:

- __Another process has performed a coordinated write, changing the contents of the file.__ You must reread the file and update your content.
- __Another process is performing a coordinated read.__ The file coordinator notifies you, giving you a chance to save any unsaved changes before the read occurs.
- __Another process has moved the file.__ You must update your URL.
- __Another process has deleted the file.__ You must notify the user and either save a copy locally or stop displaying the file.
- __Conflicts have been detected between different versions of the file.__ You must be prepared to handle these conflicts.

  Note that conflicts should only occur when using iCloud Drive. Third-party document providers cannot add versions to a file; therefore, they have no way of signaling when a conflict occurs. This means that third-party document providers must either defer back to their containing app or upload the local changes to their server and handle the conflict there.

For more information about file providers, see [The Role of File Coordinators and Presenters](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/FileCoordinators/FileCoordinators.html#//apple_ref/doc/uid/TP40010672-CH11) in _[File System Programming Guide](../File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

[Next](Document%20Revision%20History.md)[Previous](Accessing%20Documents.md)


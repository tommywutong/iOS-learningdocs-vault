---
title: Changes To App Containers In iOS 8
apple_id: DTS40014932
resource_type: Technical Note
platform: iOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/technotes/tn2406/_index.html
archived_at: '2026-07-26T19:54:14.836801Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2406

# Changes To App Containers In iOS 8

Beginning in iOS 8, the Documents and Library directories are no longer siblings of your application's bundle. This document describes how to ensure your app is not affected by these changes.

iOS 8 changes the locations of the standard directories used for storing user and app data (e.g. Documents, Library). While the locations of these directories have always been an implementation detail, some applications improperly assume that the Documents and Library directories reside in the same directory as the application's bundle. iOS 8 splits the data of an application from the application bundle. Code which attempts to derive the path to the Documents or Library directories will return an invalid path on iOS 8. Attempting to access this path will fail, and may terminate your app.

__Important:__ This change affects all applications, regardless of when they were built.

If your application or framework accesses the Documents directory, the Library directory, or any of the other standard directories, follow the recommendations listed under [Locating The Standard Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojtgiwugsbrfvge6q2dj5gq) when building a URL or path to your data.

[Locating The Standard Directories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojtgiwugsbrfvge6q2dj5gq)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojtgiwugsbrfvdfkusujbcvex2sivauiskoi4)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytiojtgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Locating The Standard Directories

Applications should always call the system to get the locations of the standard directories.

__Listing 1__  Using NSFileManager to retrieve the location of the Documents directory.

```objc
// Returns the URL to the application's Documents directory.
- (NSURL *)applicationDocumentsDirectory
{
    return [[[NSFileManager defaultManager] URLsForDirectory:NSDocumentDirectory inDomains:NSUserDomainMask] lastObject];
}
```

The `NSFileManager` class provides the `-URLsForDirectory:inDomains:` and `-URLForDirectory:inDomain:appropriateForURL:create:error:` methods to retrieve the url of the given standard directory. Refer to the values listed under `NSSearchPathDirectory` in the [Foundation Constants Reference](https://developer.apple.com/library/ios/documentation/cocoa/reference/foundation/Miscellaneous/Foundation_Constants/Reference/reference.html) for the complete list of standard directories that can be located using these APIs. Note that not all of the listed values are relevant on iOS.

While URLs are the preferred format for referencing locations on disk, your application may require a path when interfacing with C-based APIs. If you have a file system URL (that is, -isFileURL returns YES), you can call -path to extract the path from the URL. The resulting path is guaranteed to be compatible with path-based APIs.

__Note:__ Always ask for the URL of the standard directory that is closest to your data. For example, if your data resides in `Library/Application Support` then you should pass `NSApplicationSupportDirectory` to `-URLForDirectory:inDomain:appropriateForURL:create:error:`.

[Back to Top](#)

## Further Reading

[Accessing Files and Directories](https://developer.apple.com/library/ios/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/AccessingFilesandDirectories/AccessingFilesandDirectories.html) in the "File System Programming Guide".

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-28 | New document that describes how to locate the standard directories in iOS 8. |


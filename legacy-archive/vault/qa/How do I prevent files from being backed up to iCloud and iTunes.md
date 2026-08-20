---
title: How do I prevent files from being backed up to iCloud and iTunes?
apple_id: DTS40011342
resource_type: QA
platform: iOS
topic: Data Management
technology: System
published: '2016-05-16'
source_url: https://developer.apple.com/library/archive/qa/qa1719/_index.html
archived_at: '2026-07-27T07:25:59.539456Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1719

# How do I prevent files from being backed up to iCloud and iTunes?

## Q:  My app has a number of files that need to be stored on the device permanently for my app to function properly offline. However, those files do not contain user data and don't need to be backed up. How can I prevent them from being backed up?

A: On iOS, apps are responsible for ensuring that only user data and not application data is backed up to iCloud and iTunes. The exact steps necessary vary between iOS version, so this QA will describe the process for each version of iOS. For more information on exactly what data should or should not be backed up, see the [App Backup Best Practices section of the iOS App Programming Guide](https://developer.apple.com/library/ios/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/PerformanceTips/PerformanceTips.html#//apple_ref/doc/uid/TP40007072-CH7-SW17).

__Important:__ Apps should avoid mingling app data and user data in the same file. Doing so will unnecessarily increase backup sizes and can be considered a violation of the iOS Data Storage Guidelines.

## iOS 5.1 and later

Starting in iOS 5.1, apps can use either [NSURLIsExcludedFromBackupKey](https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/Foundation/Classes/NSURL_Class/Reference/Reference.html#//apple_ref/c/data/NSURLIsExcludedFromBackupKey) or [kCFURLIsExcludedFromBackupKey](https://developer.apple.com/library/ios/#documentation/CoreFoundation/Reference/CFURLRef/Reference/reference.html#//apple_ref/c/data/kCFURLIsExcludedFromBackupKey) file system properties to exclude files and directories from backups. Apps that need to exclude a large number of files can exclude them by creating their own sub-directory and marking that directory as excluded. Apps should create their own directories for exclusion, rather than excluding the system defined directories. Either of these APIs is preferred over the older, deprecated approach of directly setting an extended attribute. All apps running on iOS 5.1 and later should use these APIs to exclude data from backups.

__Listing 1__  Excluding a File from Backups on iOS 5.1 and later (Objective C)

```objc
- (BOOL)addSkipBackupAttributeToItemAtPath:(NSString *) filePathString
{
    NSURL* URL= [NSURL fileURLWithPath: filePathString];
    assert([[NSFileManager defaultManager] fileExistsAtPath: [URL path]]);

    NSError *error = nil;
    BOOL success = [URL setResourceValue: [NSNumber numberWithBool: YES]
                                  forKey: NSURLIsExcludedFromBackupKey error: &error];
    if(!success){
        NSLog(@"Error excluding %@ from backup %@", [URL lastPathComponent], error);
    }
    return success;
}
```

__Listing 2__  Excluding a File from Backups on iOS 5.1 and later (Swift)

```swift
 func addSkipBackupAttributeToItemAtURL(filePath:String) -> Bool
    {
        let URL:NSURL = NSURL.fileURLWithPath(filePath)

        assert(NSFileManager.defaultManager().fileExistsAtPath(filePath), "File \(filePath) does not exist")

        var success: Bool
        do {
            try URL.setResourceValue(true, forKey:NSURLIsExcludedFromBackupKey)
            success = true
        } catch let error as NSError {
            success = false
            print("Error excluding \(URL.lastPathComponent) from backup \(error)");
        }

        return success
    }
```

[Back to Top](#)

## iOS 5.0.1

If your app must support iOS 5.0.1, you can use the following method to set the "do not back up" extended attribute. Whenever you create a file or folder that should not be backed up, write the data to the file and then call this method, passing in a URL to the file.

__Warning:__ The code that follows has been deprecated and should only be used on iOS 5.0.1 or earlier. When running in iOS 5.1, apps should use the `NSURL` and `CFURL` keys described above.

__Listing 3__  Setting the Extended Attribute on iOS 5.0.1

```objc
#import <sys/xattr.h>
- (BOOL)addSkipBackupAttributeToItemAtPath:(NSString *) filePathString
{
    assert([[NSFileManager defaultManager] fileExistsAtPath: filePathString]);

    const char* filePath = [filePathString fileSystemRepresentation];

    const char* attrName = "com.apple.MobileBackup";
    u_int8_t attrValue = 1;

    int result = setxattr(filePath, attrName, &attrValue, sizeof(attrValue), 0, 0);
    return result == 0;
}
```

[Back to Top](#)

## iOS 5.0

It is not possible to exclude data from backups on iOS 5.0. If your app must support iOS 5.0, then you will need to store your app data in `Caches` to avoid that data being backed up. iOS will delete your files from the `Caches` directory when necessary, so your app will need to degrade gracefully if its data files are deleted.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-05-16 | Added a how-to code snippet in Swift |
| 2015-08-03 | Fixed typo |
| 2015-03-11 | Modified code snippets to use a string argument instead of URLs. Updated link to the App Backup Best Practices section in App Programming guide. |
| 2012-04-23 | Updated for iOS 5.1 |
| 2011-11-10 | -Fixed critical bug in code snippet. |
|  | New document that describes how an app can prevent files from being backed up to iCloud and iTunes. |

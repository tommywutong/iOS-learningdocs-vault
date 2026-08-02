---
title: Why can't I save data to my application's bundle when running on the device?
apple_id: DTS40009181
resource_type: QA
platform: iOS
topic: Data Management
technology: Foundation
published: '2012-11-06'
source_url: https://developer.apple.com/library/archive/qa/qa1662/_index.html
archived_at: '2026-07-18T02:33:22.444966Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1662

# Why can't I save data to my application's bundle when running on the device?

## Q:  My application saves data to the application's bundle, which works fine in the iPhone Simulator. However, when I run on a device, my data cannot be saved. What's going on?

A: The different behaviors you are seeing are due to differences between the iPhone Simulator and the actual device. In the simulator, your application bundle is saved in a location that allows you full read/write access, so your code succeeds in writing and saving the preference data to the bundle. However, on the device, your application bundle cannot be modified. The [File System Programming Guide](https://developer.apple.com/library/ios/#documentation/FileManagement/Conceptual/FileSystemProgrammingGUide/Introduction/Introduction.html) contains information on the writeable locations in your application directory.

Your iPhone application's home directory contains a subdirectory for preferences (`<Application_Home>/Library/Preferences`). However, you should not create preferences files directly, but should instead use the [NSUserDefaults](https://developer.apple.com/iphone/library/documentation/Cocoa/Reference/Foundation/Classes/NSUserDefaults_Class/index.html#//apple_ref/doc/uid/TP40003764) or [CFPreferences](https://developer.apple.com/iphone/library/documentation/CoreFoundation/Reference/CFPreferencesUtils/Reference/reference.html) to get and set application preferences.

Alternately, you can save application specific data to the `<Application_Home>/Documents` subdirectory of your application's home directory. Use the `NSFileManager` `URLsForDirectory:inDomains:` method to get a URL to this directory.

Both of the above techniques also have the additional advantage that they will preserve the users data when the application is updated.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2012-11-06 | Editorial |
| 2009-08-25 | New document that describes why you can't save data to your application's bundle when running on the device. |


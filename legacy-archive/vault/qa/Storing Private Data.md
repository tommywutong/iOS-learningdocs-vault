---
title: Storing Private Data
apple_id: DTS40010197
resource_type: QA
platform: iOS
topic: Data Management
technology: System
published: '2010-07-22'
source_url: https://developer.apple.com/library/archive/qa/qa1699/_index.html
archived_at: '2026-07-18T02:34:12.272635Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1699

# Storing Private Data

## Q:  I'm adding file sharing support to my app, but I have some private data I don't want the user to be able to access. Where should I store that data?

A: I'm adding file sharing support to my app, but I have some private data I don't want the user to be able to access. Where should I store that data?

Starting with iOS 3.2, applications can choose to allow users to add files to their app documents directory by adding the key `UIFileSharingEnabled` to their `Info.plist`. When that key is set, the contents of the directory `<Application Home>/Documents` will be accessible in iTunes where the user can add or remove files at will. Applications that set `UIFileSharingEnabled` but also need to maintain data that will not be visible to the user will need to store that data in another directory.

In addition to the directories documented previously, the entire `<Application_Home>/Library` directory has always been preserved during updates and backups, except for `<Application_Home>/Library/Caches`. Because of this, applications can create their own directories in `<Application_Home>/Library/` and those directories will be preserved in backups and across updates. To minimize the risk of name collisions, we recommend that you name this directory carefully. For example, a directory named `Private Documents` would be a good choice.

For more information about sharing file with the user, see [Sharing Files With the User](https://developer.apple.com/iphone/library/documentation/iphone/conceptual/iphoneosprogrammingguide/StandardBehaviors/StandardBehaviors.html#//apple_ref/doc/uid/TP40007072-CH4-SW10).

For more information on how backups and updates are handled, see [Backup and Restore](https://developer.apple.com/iphone/library/documentation/iphone/conceptual/iphoneosprogrammingguide/RuntimeEnvironment/RuntimeEnvironment.html#//apple_ref/doc/uid/TP40007072-CH2-SW1).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-22 | New document that describes how applications should store documents and data that should not be accessible to the user. |


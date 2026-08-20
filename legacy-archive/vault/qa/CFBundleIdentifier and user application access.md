---
title: CFBundleIdentifier and user application access
apple_id: DTS10003393
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreFoundation
published: '2005-02-08'
source_url: https://developer.apple.com/library/archive/qa/qa1373/_index.html
archived_at: '2026-07-18T02:30:27.467069Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1373

# CFBundleIdentifier and user application access

## Q:  My application will not stay selected when trying to limit a user's access to it in the Accounts preference pane. What is wrong?

A: My application will not stay selected when trying to limit a user's access to it in the Accounts preference pane. What is wrong?

Your application is probably missing the `CFBundleIdentifier` key from its Info.plist file. This key is a unique identifier for your application on the system. It has a String value, recommended to resemble a Java package, such as `com.mycompany.MyApp`.

The "Accounts" preference pane allows an Administrator to limit a user's access to specific applications. This access control is currently implemented using the `CFBundleIdentifier` key. If this key is undefined, or not unique in your application, System Preferences will not know how to find or identify your application. As a result, your application will stay unchecked the next time you open the Accounts pane, even if it was checked by an Administrator. This also means, then, that the desired access control for your application will not occur.

This problem is one of many reasons to make sure your application has an existing and unique `CFBundleIdentifier` value. Other areas of the system, such as the CFBundle and CFPreferences APIs, also depend on this key to function properly.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-02-08 | New document that describes the role of CFBundleIdentifier in limiting a user's application access. |


---
title: iCloud Design Guide
apple_id: TP40012094
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesigningForKey-ValueDataIniCloud.html
archived_at: '2026-07-15T07:34:38.923063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Design Guide](About%20Incorporating%20iCloud%20into%20Your%20App.md)


[Next](Designing%20for%20Documents%20in%20iCloud.md)[Previous](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md)

# Designing for Key-Value Data in iCloud

To store discrete values in iCloud for app preferences, app configuration, or app state, use iCloud key-value storage. _Key-value storage_ is similar to the local [user defaults](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Preferences.html#//apple_ref/doc/uid/TP40009071-CH20) database; but values that you place in key-value storage are available to every instance of your app on all of a user’s various devices. If one instance of your app changes a value, the other instances see that change and can use it to update their configuration, as depicted in Figure 2-1.

__Figure 2-1__  iCloud key-value storage

!

Zooming in on the key-value storage interactions for a single device, as shown in Figure 2-2, you can see that your app accesses key-value storage using the shared [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) object.

__Figure 2-2__  iCloud key-value storage access

!

As you do with an [NSUserDefaults](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSUserDefaults/Description.html#//apple_ref/occ/cl/NSUserDefaults) object, use the iCloud key-value store to save and retrieve scalar values (such as `BOOL`) and property-list object types: `NSNumber`, `NSString`, `NSDate`, `NSData`, `NSArray`, and `NSDictionary`. Array and dictionary values can hold any of these value types. The [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) class provides methods for reading and writing each of these types, as described in _[NSUbiquitousKeyValueStore Class Reference](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)_.

Each time you write key-value data, the operation succeeds or fails atomically; either all of the data is written or none of it is. You can take advantage of this behavior when your app needs to ensure that a set of values is saved together to ensure validity: place the mutually dependent values within a dictionary and call the [setDictionary:forKey:](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1417155-setdictionary) method.

Before you can use key-value storage, your app must have the appropriate entitlement, as explained in [Request Access to iCloud Using Xcode Capabilities](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqnrnknltcmy). And that is all the setup you need.

Any device running your app, and attached to a user’s iCloud account, can upload key-value changes to that account. To keep track of such changes, register for the [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) notification during app launch. Then, to ensure your app starts off with the newest available data, obtain the keys and values from iCloud by calling the [synchronize](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1415989-synchronize) method. (You need never call the `synchronize` method again during your app’s life cycle, unless your app design requires fast-as-possible upload to iCloud after you change a value.)

The following code snippet shows how to prepare your app to use the iCloud key-value store. Place code like this within your [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method (iOS) or [applicationDidFinishLaunching:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428385-applicationdidfinishlaunching) method (OS X).

```
// register to observe notifications from the store
[[NSNotificationCenter defaultCenter]
    addObserver: self
       selector: @selector (storeDidChange:)
           name: NSUbiquitousKeyValueStoreDidChangeExternallyNotification
         object: [NSUbiquitousKeyValueStore defaultStore]];

// get changes that might have happened while this
// instance of your app wasn't running
[[NSUbiquitousKeyValueStore defaultStore] synchronize];
```

In your handler method for the `NSUbiquitousKeyValueStoreDidChangeExternallyNotification` notification, examine the user info dictionary and determine if you want to write the changes to your app’s local [user defaults](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Preferences.html#//apple_ref/doc/uid/TP40009071-CH20) database. It’s important to decide deliberately whether or not to change your app’s settings based on iCloud-originated changes, as explained next.

When a device attached to an iCloud account tries to write a value to key-value storage, iCloud checks to see if any recent changes have been made to the key-value store by other devices. If no changes have been made recently, the [NSUbiquitousKeyValueStore](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore) object writes the pending local changes to the server. If changes were made recently, it does not write the local values to the server. Instead, it generates a [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) notification to force your app to update itself based on the updated server values.

When your handler for the `NSUbiquitousKeyValueStoreDidChangeExternallyNotification` notification runs, validate the new values coming from the server to be sure that they make sense. If the new data does not match the local state of your app, consider whether data coming from another device might be out of date. For example, if the user is on level 13 of a game on one device and on level 1 on another device, the instance of the game set to level 13 might want to write its changes again.

The total space available in your app’s iCloud key-value storage is 1 MB per user. The maximum number of keys you can specify is 1024, and the size limit for each value associated with a key is 1 MB. For example, if you store a single large value of exactly 1 MB for a single key, that fully consumes your quota for a given user of your app. If you store 1 KB of data for each key, you can use 1000 key-value pairs.

The maximum length for a key string is 64 bytes using UTF8 encoding. The data size of your cumulative key strings does _not_ count against your 1 MB total quota for iCloud key-value storage; rather, your key strings (which at maximum consume 64 KB) count against a user’s total iCloud allotment.

If your app has exceeded its quota in key-value storage, the iCloud key-value store posts the [NSUbiquitousKeyValueStoreDidChangeExternallyNotification](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore/1412267-didchangeexternallynotification) notification with a value of [NSUbiquitousKeyValueStoreQuotaViolationChange](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestorequotaviolationchange) in its user info dictionary.

For more on how to use iCloud key-value storage in your app, see [Storing Preferences in iCloud](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/UserDefaults/StoringPreferenceDatainiCloud/StoringPreferenceDatainiCloud.html#//apple_ref/doc/uid/10000059i-CH7) in _[Preferences and Settings Programming Guide](../../Cocoa/Preferences%20and%20Settings%20Programming%20Guide/About%20Preferences%20and%20Settings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2ts2i)_, and refer to _[NSUbiquitousKeyValueStore Class Reference](https://developer.apple.com/documentation/foundation/nsubiquitouskeyvaluestore)_.

Although you can place an `NSData` object in your app’s key-value store, do so sparingly. The biggest problem is space. Apps may store only 1 MB of data in their key-value storage. If your data objects are potentially large, your app might exceed its storage limit quickly. So if you are close to the 1 MB limit, you might want to consider document storage for that data instead.

Every time you make a small change to a large data object, the entire data object must be sent to iCloud. Rather than bundle lots of data into a single data object, it is better to break that data into small pieces and store that data separately, preferably using more transparent types such as numbers and strings. Storing data more granularly using other types of property-list objects minimizes the amount of data that must be transferred when you make small changes.

Because data objects are custom objects, only your app knows how to read them. As you make changes to your data formats, older versions of your app might break when trying to read data objects that use a new format. To prevent older versions of your app from breaking, you might need to include version information in the data objects, as explained in [Design for Robustness and Cross-Platform Compatibility](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknltq).

Every app submitted to the App Store or Mac App Store should adopt key-value storage, but some types of data are not appropriate for key-value storage. In a document-based app, for example, it is usually _not_ appropriate to use key-value storage for state information about each document, such as current page or current selection. Instead, store document-specific state, as needed, with each document, as described in [Design for Persistent Document State](Designing%20for%20Documents%20in%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaojufvbuqmrnknlto).

In addition, avoid using key-value storage for data essential to your app’s behavior when offline; instead, store such data directly into the local user defaults database.

[Next](Designing%20for%20Documents%20in%20iCloud.md)[Previous](iCloud%20Fundamentals%20%28Key-Value%20and%20Document%20Storage%29.md)


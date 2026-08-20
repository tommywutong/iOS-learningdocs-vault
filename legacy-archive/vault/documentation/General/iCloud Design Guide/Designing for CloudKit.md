---
title: iCloud Design Guide
apple_id: TP40012094
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2015-12-17'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/DesigningforCloudKit/DesigningforCloudKit.html
archived_at: '2026-07-15T07:34:42.502172Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iCloud Design Guide](About%20Incorporating%20iCloud%20into%20Your%20App.md)


[Next](Testing%20and%20Debugging%20%28Key-Value%20and%20Document%20Storage%29.md)[Previous](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html)

# Designing for CloudKit

CloudKit provides a way to store data as records in a database that users of your app can share. Record types are used to differentiate between records storing different types of information. Each record is a dictionary of key-value pairs, with each key representing one field of the record. Fields can contain simple types (such as strings, numbers, and dates) or more complex types (such as locations, references, and assets).

You can represent all the persistent model objects in your app using a CloudKit schema. However, the CloudKit framework should not be used to replace model objects in your app and should not be used for storing objects locally. It is a service for moving data to and from iCloud and sharing data between users of your app. It’s your responsibility to convert model objects to records that you save using CloudKit, and to fetch changes made by other users and apply those changes to your model objects.

With CloudKit, you decide when to move data from your app to iCloud and from iCloud to your app. Although CloudKit provides facilities to keep you informed when changes occur, you must still fetch those changes explicitly. Because you decide when to fetch and save data, you are responsible for ensuring that data is fetched at the right times and in the right order, and you are responsible for handling any errors that arise.

Once you have a native CloudKit app, you can provide a web app that accesses the same containers as your native CloudKit app. To get started creating a native CloudKit app and using the developer tools, read _[CloudKit Quick Start](../../Data%20Management/CloudKit%20Quick%20Start/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2dsobx)_. To create a web app, see _[CloudKit JS Reference](https://developer.apple.com/documentation/cloudkitjs)_ or _[CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240)_.

Before you can use CloudKit, you must enable your app’s target in the Xcode project to use iCloud and CloudKit. Using Xcode to configure CloudKit adds the necessary entitlements to your app and configures your app to use a default container based on its bundle ID. You can create additional containers and also share them between your apps. As soon as Xcode creates the containers for you, you can access them using the CloudKit Dashboard web tool. To enable CloudKit in your Xcode project and to use CloudKit Dashboard, read [Enabling CloudKit in Your App](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/EnablingiCloudandConfiguringCloudKit/EnablingiCloudandConfiguringCloudKit.html#//apple_ref/doc/uid/TP40014987-CH2).

Like other iCloud technologies, CloudKit organizes data using containers. A container represents your app’s iCloud storage. At runtime, you can perform tasks against a specific container using a [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer) object.

Each container is divided into public and private databases, each of which is represented by a [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase) object. Any data written to the private database is visible only to the current user and is stored in that user’s iCloud account. Data written to the public database is visible to all users of the app and is stored in the app’s iCloud storage.

For a running CloudKit app, a container’s public database is always readable, even when the user is not signed in to their iCloud account on the device. Saving records to the public database and accessing the private database requires that the user be signed in. If your app does more than read data from the public database, check to see whether the user is signed in before saving records. To avoid errors, disable the parts of your user interface that save records until the user signs in.

To check the iCloud credentials for a CloudKit app, read [Alert the User to Enter iCloud Credentials](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/CreatingaSchemabySavingRecords/CreatingaSchemabySavingRecords.html#//apple_ref/doc/uid/TP40014987-CH3-SW8).

Inside the public and private databases, you organize your app’s data using records, represented by instances of the [CKRecord](https://developer.apple.com/documentation/cloudkit/ckrecord) class. You fetch and save records using either operation objects or convenience methods in the [CKContainer](https://developer.apple.com/documentation/cloudkit/ckcontainer) and [CKDatabase](https://developer.apple.com/documentation/cloudkit/ckdatabase) classes. Operation objects can operate on multiple records at once and can be configured with dependencies to ensure that records are saved in the proper order. Operation objects are based on the [NSOperation](https://developer.apple.com/documentation/foundation/nsoperation) class and can be integrated with your app’s other workflows.

If you know the ID of the record you want, use a fetch operation. If you do not know the ID of a record, CloudKit provides the ability to query for records using a predicate. A predicate-based query lets you locate records whose fields contain certain values. You use this predicate with a [CKQuery](https://developer.apple.com/documentation/cloudkit/ckquery) object to specify both the search criteria and sorting options for the returned records. You then execute the query using a [CKQueryOperation](https://developer.apple.com/documentation/cloudkit/ckqueryoperation) object.

Alternatively, use subscriptions to let the server notify you when certain parts of the database change. Subscriptions act like a persistent query on the server. You configure a [CKSubscription](https://developer.apple.com/documentation/cloudkit/cksubscription) object much as you do a `CKQuery` object, but instead of executing that query explicitly, you save the subscription to the server. After that, the server sends push notifications to your app whenever a change occurs that matches the predicate. For example, you can use subscriptions to detect the creation or deletion of records or to detect when the field of a record changes to a specific value. Upon receiving the push notification from the server, you can fetch the changed record and update your object model.

To save and fetch records, read [Creating a Database Schema by Saving Records](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/CreatingaSchemabySavingRecords/CreatingaSchemabySavingRecords.html#//apple_ref/doc/uid/TP40014987-CH3) and [Fetching Records](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/FetchingRecords/FetchingRecords.html#//apple_ref/doc/uid/TP40014987-CH4). To subscribe to record changes, read [Subscribing to Record Changes](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/SubscribingtoRecordChanges/SubscribingtoRecordChanges.html#//apple_ref/doc/uid/TP40014987-CH8).

CloudKit provides separate development and production environments for storing your container’s schema and records. The development environment is a more flexible environment that is available to members of your development team. In the development environment, your app can save records. Or you can add fields to records that aren’t in the schema and then CloudKit creates the corresponding record types and fields for you. This feature is not available in the production environment.

When you are ready to distribute your app for testing, you migrate the development schema to the production environment using CloudKit Dashboard. (CloudKit Dashboard does not copy the records from the development to the production environment.) After you deploy the schema to the production environment, you can still modify the schema in the development environment but can’t delete record types and fields that were previously deployed. When exporting your app from Xcode to distribute it for testing, you can choose whether to target the CloudKit development or production environment.

When you are ready to upload your app to iTunes Connect to distribute your app using TestFlight or the store, Xcode automatically configures your app to use the production environment. An app uploaded to iTunes Connect can be configured to use only the production environment.

To perform these tasks, read [Testing Your CloudKit App](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/TestingYourApp/TestingYourApp.html#//apple_ref/doc/uid/TP40014987-CH9) and [Deploying the Schema](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/DeployingYourCloudKitApp/DeployingYourCloudKitApp.html#//apple_ref/doc/uid/TP40014987-CH10).

Most CloudKit operations are performed asynchronously and require that you provide a completion handler to process the results. All operations rely on the user being connected to the network, so you should be prepared to handle errors that may occur. Your app should also be mindful of the number of requests it makes and size of the data that is transmitted back and forth to iCloud. Here’s the basic workflow of a typical CloudKit app:

1. Fetch records needed to launch your app and initially present data to the user.
2. Perform queries based on the user’s actions or preferences.
3. Save changes to either the private or public database.
4. Batch multiple save and fetch operations in a single operation.
5. Create subscriptions to receive push notifications when records of interest change.
6. Update the object model and views when the app receives changes to records.
7. Handle errors that may occur when executing asynchronous operations.

CloudKit saves each record atomically. If you need to save a group of records in a single atomic transaction, save them to a custom zone, which you can create using the [CKRecordZone](https://developer.apple.com/documentation/cloudkit/ckrecordzone) class. Zones are a useful way to arrange a discrete group of records, but they are supported only in private databases. Zones cannot be created in a public database.

To batch operations, read [Batch Operations to Save and Fetch Multiple Records](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/MaintainingaLocalCacheofCloudKitRecords/MaintainingaLocalCacheofCloudKitRecords.html#//apple_ref/doc/uid/TP40014987-CH12-SW1).

When defining your app’s record types, it helps to understand how you use those record types in your app. Here are some tips to help you make better choices during the design process:

- __Organize your records around a central record type.__ A good organization strategy is to define one primary record type and additional record types to support the primary type. Using this type of organization lets you focus your queries on your primary record type and then fetch any supporting objects as needed. For example, a calendar app might define a single calendar record (the primary record type), as well as multiple event records (a secondary record type) corresponding to events on that calendar.
- __Use references to represent relationships between your model objects.__ Use a [CKReference](https://developer.apple.com/documentation/cloudkit/ckreference) object to represent a formal one-to-one or one-to-many relationship between model objects. References also let you establish an ownership model between records that can make deleting records easier.
- __Include version information in your records.__ A version number can help you decide at runtime what information might be available in a given record.
- __Handle missing keys gracefully in your code.__ For each record you create, you are not required to provide values for all keys contained in the record type. For any keys you do not specify, CloudKit sets the corresponding value to `nil`. Your app should be able to handle keys with `nil` values in an appropriate way. Being able to handle these “missing keys” becomes important when new versions of your app access records created by an older version.
- __Avoid complex graphs of records.__ Creating a complex network of references between records may result in problems later when you need to update or delete records. If the owner references among your records are complex, it might be difficult to delete records later without leaving other records in an inconsistent state.
- __Use assets for discrete data files.__ When you want to associate images or other discrete files with a record, use an Asset type (a [CKAsset](https://developer.apple.com/documentation/cloudkit/ckasset) object in your code) to represent that field in the record. The total size of a record’s data is limited to 1 MB, though assets do not count against that limit.

To add references to your record types, read [Adding Reference Fields](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/MaintainingaLocalCacheofCloudKitRecords/MaintainingaLocalCacheofCloudKitRecords.html#//apple_ref/doc/uid/TP40014987-CH12). To store large files or location data, read [Using Asset and Location Fields](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/AddingAssetsandLocations/AddingAssetsandLocations.html#//apple_ref/doc/uid/TP40014987-CH6). For data size limits, see “Data Size Limits” in _[CloudKit Web Services Reference](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/index.html#//apple_ref/doc/uid/TP40015240)_.

As you design the record types for your app, make sure those records meet your needs but do not restrict you from making changes to the schema in the future. After you deploy the schema to the production environment, you can add fields to a record, but you cannot delete a field or change its data type. Follow these tips to make updating your schema easier in the future:

- __Add new fields to represent new data types.__ A new version of your app can add the missing keys to records as it fetches and saves them to the database.
- __Define record types that do not lose data integrity easily.__ Each new version of your app must create records that do not break older versions of the app. The best way to ensure data integrity is to minimize the amount of validation required for a record:

  - Avoid fields that have a narrow range of acceptable values, the changing of which might cause older versions of the app to treat the data as invalid.
  - Avoid fields whose values are dependent on the values of other fields. Creating dependent fields means you have to write validation logic to ensure the values of those fields are correct. Once created, this kind of validation logic is difficult to change later without breaking older versions of your app.
  - Minimize the number of required fields for a given record. As soon as you require the presence of a field, every version of your app after that must populate that field with data. Treating fields as optional gives you more flexibility to modify your schema later.
- __Handle missing keys gracefully.__ If a record is missing a key, add it in the background.

To modify your schema using CloudKit Dashboard, read [Using CloudKit Dashboard to Manage Databases](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/EditingSchemesUsingCloudKitDashboard/EditingSchemesUsingCloudKitDashboard.html#//apple_ref/doc/uid/TP40014987-CH5).

[Next](Testing%20and%20Debugging%20%28Key-Value%20and%20Document%20Storage%29.md)[Previous](https://developer.apple.com/library/archive/documentation/General/Conceptual/iCloudDesignGuide/Chapters/DesignForCoreDataIniCloud.html)


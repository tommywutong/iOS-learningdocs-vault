---
title: iCloud Programming Guide for Core Data
apple_id: TP40013491
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Data Management
technology: CoreData
published: '2017-06-06'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/UsingCoreDataWithiCloudPG/Introduction/Introduction.html
archived_at: '2026-07-15T07:24:01.238744Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Using%20the%20SQLite%20Store%20with%20iCloud.md)

# About Using iCloud with Core Data

iCloud is a cloud service that gives your users a consistent and seamless experience across all of their iCloud-enabled devices. iCloud works with ubiquity containers—special folders that your app stores data in—to manage your app’s cloud storage. When you add, delete, or make changes to a file in your app’s ubiquity container, the system uploads the changes to iCloud. Other peers download the changes to keep your app up to date.

To help you persist managed objects to the cloud, iCloud is integrated with Core Data. To use Core Data with iCloud, you simply tell Core Data to create an iCloud-enabled persistent store. The iCloud service and Core Data take care of the rest: The system manages the files in the ubiquity container that make up your persistent store, and Core Data helps you keep your app up to date. To let you know when the content in your container changes, Core Data posts notifications.

When you use Core Data, you have several storage models to choose from. Using Core Data with iCloud, you have a subset of these options, as follows:

- Atomic stores (for example, the binary store) load and save all of your managed objects in one go. Atomic stores work best for smaller storage requirements.
- Transactional stores (for example, the SQLite store) load and save only the managed objects that you’re using and offer high–performance querying and merging. Transactional stores work best for larger, more complex storage requirements.
- Document storage (iOS only) works best for apps designed to use a document-based design paradigm. Use document storage in combination with either an atomic or a transactional store.

When you decide on a storage model, consider the strengths of each store as well as the iCloud-specific strengths discussed below.

### Use Core Data Atomic Stores for Small, Simple Storage

iCloud supports XML (OS X only) and binary atomic persistent stores. Useful for small, simple storage requirements, Core Data’s atomic-store support sacrifices merging and network efficiency for simplicity of use for when your data rarely changes. When you use iCloud with an atomic persistent store, you work directly in the ubiquity container. Binary (and XML) store files are themselves transferred to the iCloud servers; so whenever a change is made to the data, the system uploads the entire store and pushes it to all connected devices. This means that changes on one peer can overwrite changes made on the others.

iCloud treats Core Data atomic stores like any other file added to your app’s ubiquity container. You can learn more about managing files in your app’s ubiquity container in _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_.

### Use Core Data Transactional Stores for Large, Complex Storage

Core Data provides ubiquitous persistent storage for SQLite-backed stores. Core Data takes advantage of the SQLite transactional persistence mechanism, saving and retrieving transaction logs—logs of changes—in your app’s ubiquity container. The Core Data framework’s reliability and performance extend to iCloud, resulting in dependable, fault-tolerant storage across multiple peers. Continue reading this document to learn more about how to use iCloud with an SQLite store.

### (iOS Only) Use Core Data Document Stores to Manage Documents in iCloud

The [UIManagedDocument](https://developer.apple.com/documentation/uikit/uimanageddocument) class is the primary mechanism through which Core Data stores managed documents in iCloud on iOS. The `UIManagedDocument` class manages the entire Core Data stack for each document in a document-based app. Changes to managed documents are automatically persisted to iCloud. By default, managed documents are backed by SQLite-type persistent stores, but you can choose to use atomic stores instead. While the steps you take to integrate the `UIManagedDocument` class into your app differ, the model-specific guidelines and best practices you follow are generally the same. You can find additional implementation strategies and tips in [Using Document Storage with iCloud](Using%20Document%20Storage%20with%20iCloud.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztiojrfvbuqnjnknltc).

iCloud is a service that stores your app’s data in the cloud and makes it available to your users’ iCloud-enabled devices. Before using Core Data’s iCloud integration, you should read more about iCloud in _[iCloud Design Guide](../../General/iCloud%20Design%20Guide/About%20Incorporating%20iCloud%20into%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdaoju)_. In addition, this guide assumes a working knowledge of Core Data, a powerful object graph and data persistence framework. For more information about the Core Data framework, see Introduction to Core Data Programming Guide in _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_.

[Next](Using%20the%20SQLite%20Store%20with%20iCloud.md)


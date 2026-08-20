---
title: CloudKit Quick Start
apple_id: TP40014987
resource_type: Guide
platform: Xcode Developer Tools
topic: Data Management
technology: CloudKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitQuickStart/Glossary/Glossary.html
archived_at: '2026-07-15T07:23:29.479841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Quick Start](About%20This%20Document.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __ad hoc provisioning profile__

  A type of distribution provisioning profile used for distributing iOS, tvOS, and watchOS apps for testing.

- __Apple Developer Program__

  Subscription services that offer Apple developers access to technical resources and support to develop iOS, watchOS, tvOS, and Mac apps for the store.

- __Apple Push Notification service (APNs)__

  Apple service for propagating information to apps running on different platform devices.

- __Apple ID__

  An Apple-issued developer account with a name and password. Developers use their Apple ID credentials to sign in to any of the Apple Developer Program tools. A developer or Apple ID can belong to multiple teams.

- __CloudKit__

  An app service that stores structured application and user data in iCloud.

- __container__

  A data store containing multiple database used by one or more apps. The default container ID matches the app’s bundle ID.

- __container ID__

  A unique identifier for an app’s iCloud container.

- __database__

  The portion of a container used to store records. There’s one public database for the app and multiple private databases—one private database for each user.

- __development environment__

  Databases used to develop your app and evolve the schema that is not accessible by apps sold on the store.

- __field__

  A property of a record type that can be set using a key-value pair.

- __iOS App file__

  A type of OS X file that can be installed on iOS and tvOS devices.

- __just-in-time schema__

  Development environment feature that allows an app to create a schema by saving records.

- __predicate__

  An object that defines logical conditions for searching for objects conforming to key-value coding.

- __private database__

  A database for storing records owned by the current user that are not readable by the app unless the user enters their iCloud credentials on the device.

- __production environment__

  Databases accessed by apps sold on the store.

- __public database__

  A database for storing records owned by the app that are shared between users. An iCloud account is not required to read records but is required to write records.

- __push notifications__

  A notification from a provider to a device transported by APNs.

- __record__

  An instance of a record type that can be created, read, and written to a database.

- __record identifier__

  An identifier for the location of a record in a database. Contains a record name and zone.

- __record name__

  A unique identifier for a record within a given zone. The record name is supplied by the app and can be used as a foreign key in another data source.

- __record type__

  A template for a set of records that have common fields.

- __record zone__

  A partition of a database to store records. Each database has a default zone and allows additional custom zones.

- __relationship__

  A record type field that associates one record to another.

- __schema__

  A collection of metadata that describes the organization of records, fields, and relationships in a database. In CloudKit, the schema includes record types, security roles, and subscription types.

- __security role__

  Permissions for a group of users to create, read, and write records in the public database. The possible roles are world, authenticated, and creator.

- __store__

  Used as a short form of the App Store, Apple TV App Store, or the Mac App Store when there’s no distinction between them.

- __subscription__

  A persistent query on the server that triggers notifications when records change.

- __to-many relationship__

  An association between a single record and one or more other records.

- __to-one relationship__

  An association between a single record and another single record.

- __tvOS__

  The operating system the runs on an Apple TV device.

[Previous](Document%20Revision%20History.md)


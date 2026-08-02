---
title: Entitlement Key Reference
apple_id: TP40011195
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/EntitlementKeyReference/Chapters/EnablingiCloud.html
archived_at: '2026-07-15T08:17:10.444913Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Entitlement Key Reference](About%20Entitlements.md)


[Next](Enabling%20Push%20Notifications.md)[Previous](About%20Entitlements.md)

# Enabling iCloud Storage

To enable your app to use iCloud document or key-value storage, set values for the appropriate entitlements using Xcode.

The following table describes the entitlement keys that you set values for to enable iCloud storage:

iCloud entitlement keyCapability

com.apple.developer.ubiquity-container-identifiers

iCloud document storage

com.apple.developer.ubiquity-kvstore-identifier

iCloud key-value storage

To support iCloud storage of user documents, use the iCloud Containers setting in the Xcode target editor.

As the value for this entitlement, provide an array of one or more strings. One of these strings must be the bundle identifier for your app, or for another app that you submit using the same team identifier. In the `.entitlements` file, this string has the following form:

```
$(TeamIdentifierPrefix)com.mycompany.myapplication
```

If you are using the graphical interface of the Xcode target editor to provide a value for the iCloud container entitlement, there is no need to include the `$(TeamIdentifierPrefix)` variable. Xcode supplies the prefix in the `.entitlements` file automatically.

If you want to confer access to documents created by other apps published by your team, use additional strings to specify the bundle identifiers of those apps.

You must not use a wildcard (“`*`”) character in the string for an iCloud container entitlement value.

__Table 1-1__  Xcode setting for iCloud document storage

| Setting | Entitlement key |
| iCloud Containers | `com.apple.developer.ubiquity-container-identifiers` |

To support iCloud storage of key-value information for your app, use the iCloud Key-Value Store setting in the Xcode target editor.

As the value for this entitlement key, provide the bundle identifier for your app, such as:

```
$(TeamIdentifierPrefix)com.mycompany.myapplication
```

If you are using the graphical interface of the target editor to provide a value for the iCloud key-value store entitlement, there is no need to include the `$(TeamIdentifierPrefix)` variable. Xcode supplies the prefix in the `.entitlements` file automatically.

__Table 1-2__  Xcode setting for iCloud key-value storage

| Setting | Entitlement key |
| iCloud Key-Value Store | `com.apple.developer.ubiquity-kvstore-identifier` |

[Next](Enabling%20Push%20Notifications.md)[Previous](About%20Entitlements.md)


---
title: ubiquityIdentityToken
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/ubiquityidentitytoken
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/ubiquityidentitytoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/ubiquityidentitytoken.json'
content_hash: 'sha256:8bfba5864610b685'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# ubiquityIdentityToken

<sub>Instance Property</sub>

An opaque token that represents the current user’s iCloud Drive Documents identity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@NSCopying var ubiquityIdentityToken: (any NSCoding & NSCopying & NSObjectProtocol)? { get }
```

## Discussion

In iCloud Drive Documents, when iCloud is available, this property contains an opaque object representing the identity of the current user. If iCloud is unavailable or there is no logged-in user, the value of this property is `nil`. Accessing the value of this property is relatively fast, so you can check the value at launch time from your app’s main thread.

You can use the token in this property, together with the [NSUbiquityIdentityDidChangeNotification](../nsnotification/name-swift.struct/nsubiquityidentitydidchange.md) notification, to detect when the user logs in or out of iCloud and to detect changes to the active iCloud account. When the user logs in with a different iCloud account, the identity token changes, and the system posts the notification. If you stored or archived the previous token, compare that token to the newly obtained one using the [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) method to determine if the users are the same or different.

Accessing the token in this property doesn’t connect your app to its ubiquity containers. To establish access to a ubiquity container, call the [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) method. In macOS, you can instead use an [NSDocument](../../appkit/nsdocument.md) object, which establishes access automatically.

CloudKit clients should not use this token as a way to identify whether the iCloud account is logged in. Instead, use [accountStatus(completionHandler:)](<../../cloudkit/ckcontainer/accountstatus(completionhandler_).md>) or [fetchUserRecordID(completionHandler:)](<../../cloudkit/ckcontainer/fetchuserrecordid(completionhandler_).md>).

## See Also

### Managing iCloud-based items

- [- URLForUbiquityContainerIdentifier:](<url(forubiquitycontaineridentifier_).md>) — Returns the URL for the iCloud container associated with the specified identifier and establishes access to that container.
- [- isUbiquitousItemAtURL:](<isubiquitousitem(at_).md>) — Returns a Boolean indicating whether the item is targeted for storage in iCloud.
- [- setUbiquitous:itemAtURL:destinationURL:error:](<setubiquitous(__itemat_destinationurl_).md>) — Indicates whether the item at the specified URL should be stored in iCloud.
- [- startDownloadingUbiquitousItemAtURL:error:](<startdownloadingubiquitousitem(at_).md>) — Starts downloading (if necessary) the specified item to the local system.
- [- evictUbiquitousItemAtURL:error:](<evictubiquitousitem(at_).md>) — Removes the local copy of the specified item that’s stored in iCloud.
- [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) — Returns a URL that can be emailed to users to allow them to download a copy of a flat file item from iCloud.

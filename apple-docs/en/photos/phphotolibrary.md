---
title: PHPhotoLibrary
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phphotolibrary
source_url: 'https://developer.apple.com/documentation/photos/phphotolibrary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phphotolibrary.json'
content_hash: 'sha256:749782b1d4928c68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHPhotoLibrary

<sub>Class</sub>

An object that manages access and changes to the user’s photo library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHPhotoLibrary
```

## Overview

The object represents the entire set of assets and collections that the Photos app manages, including assets stored on the local device and those stored in iCloud Photos. Use this object for the following tasks:

- Retrieving or verifying the user’s permission for your app to access Photos content
- Making changes to assets and collections; for example, editing asset metadata or content, inserting new assets, or rearranging the members of a collection
- Determining which records change since a previous state of the Photos library
- Registering for update messages the system sends when the library changes

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Verifying Authorization

- [+ authorizationStatusForAccessLevel:](<phphotolibrary/authorizationstatus(for_).md>) — Returns the app’s authorization to access the user’s photo library for the specified access level.
- [+ requestAuthorizationForAccessLevel:handler:](<phphotolibrary/requestauthorization(for_handler_).md>) — Prompts the user to grant the app permission to access the photo library.
- [PHAccessLevel](phaccesslevel.md) — The app’s level of access to the user’s photo library.
- [PHAuthorizationStatus](phauthorizationstatus.md) — Information about your app’s authorization to access the user’s photo library.
- [+ authorizationStatus](<phphotolibrary/authorizationstatus().md>) — Returns information about your app’s authorization to access the user’s photo library. _(deprecated)_
- [+ requestAuthorization:](<phphotolibrary/requestauthorization(__).md>) — Requests the user’s permission, if needed, to access the photo library. _(deprecated)_

### Accessing the Shared Library

- [+ sharedPhotoLibrary](<phphotolibrary/shared().md>) — Retrieves the shared photo library object.

### Presenting the Limited Library Picker

- [- presentLimitedLibraryPickerFromViewController:](<phphotolibrary/presentlimitedlibrarypicker(from_).md>) — Prompts the user to update their limited library selection.
- [- presentLimitedLibraryPickerFromViewController:completionHandler:](<phphotolibrary/presentlimitedlibrarypicker(from_completionhandler_).md>) — Prompts the user to update their limited library selection with a callback providing newly selected identifiers.

### Updating the Library

- [Requesting Changes to the Photo Library](../photokit/requesting-changes-to-the-photo-library.md) — Create, delete, or modify assets and collections in a photo library by making change requests.
- [- performChanges:completionHandler:](<phphotolibrary/performchanges(__completionhandler_).md>) — Asynchronously runs a block that requests changes to the photo library.
- [- performChangesAndWait:error:](<phphotolibrary/performchangesandwait(__).md>) — Synchronously runs a block that requests changes to be performed in the photo library.
- [PHChangeRequest](phchangerequest.md) — The abstract base class of the framework’s photo library change requests.
- [PHAssetChangeRequest](phassetchangerequest.md) — A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [PHAssetCollectionChangeRequest](phassetcollectionchangerequest.md) — A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [PHCollectionListChangeRequest](phcollectionlistchangerequest.md) — A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [PHObjectPlaceholder](phobjectplaceholder.md) — A read-only proxy object that represents a Photos asset or collection to create.

### Fetching Change History

- [- fetchPersistentChangesSinceToken:error:](<phphotolibrary/fetchpersistentchanges(since_).md>) — Retrieves the Photos library changes since the token you specify.
- [PHPersistentChangeFetchResult](phpersistentchangefetchresult.md) — An object that represents a fetch result and allows you to enumerate a very large set of change records.
- [currentChangeToken](phphotolibrary/currentchangetoken.md) — The opaque token that represents the current state of the Photos library.
- [PHPersistentChangeToken](phpersistentchangetoken.md) — An opaque object that tracks the state of the Photos library between runs, and that you can copy and serialize for future use.

### Observing Library Changes

- [Observing Changes in the Photo Library](../photokit/observing-changes-in-the-photo-library.md) — Register an observer to be notified of changes to the photo library.
- [- registerChangeObserver:](<phphotolibrary/register(__)-6y3b9.md>) — Registers an object to receive messages when objects in the photo library change.
- [- unregisterChangeObserver:](<phphotolibrary/unregisterchangeobserver(__).md>) — Unregisters an object so that it no longer receives change messages.
- [PHPhotoLibraryChangeObserver](phphotolibrarychangeobserver.md) — A protocol to adopt to have the system notify your app of changes to the photo library.
- [PHChange](phchange.md) — A description of a change that occurred in the photo library.
- [PHObjectChangeDetails](phobjectchangedetails.md) — A description of changes that occurred in an asset or collection object.
- [PHFetchResultChangeDetails](phfetchresultchangedetails.md) — A description of changes that occurred in the set of asset or collection objects listed in a fetch result.

### Observing Library Availability

- [- registerAvailabilityObserver:](<phphotolibrary/register(__)-gm0a.md>) — Registers an object to observe changes to the photo library’s availability.
- [- unregisterAvailabilityObserver:](<phphotolibrary/unregisteravailabilityobserver(__).md>) — Unregisters an object from observing changes to the photo library’s availability.
- [PHPhotoLibraryAvailabilityObserver](phphotolibraryavailabilityobserver.md) — A protocol to adopt to have the system notify your app when the availability of a photo library changes.
- [unavailabilityReason](phphotolibrary/unavailabilityreason.md) — An error that describes the reason the photo library isn’t available.

### Converting Between Local and iCloud Identifiers

- [cloudIdentifierMappings(forLocalIdentifiers:)](<phphotolibrary/cloudidentifiermappings(forlocalidentifiers_).md>) — Retrieves the cloud identifier mappings for the list of local identifiers.
- [localIdentifierMappings(for:)](<phphotolibrary/localidentifiermappings(for_).md>) — Retrieves the local identifier mappings for the list of cloud identifiers.
- [PHCloudIdentifier](phcloudidentifier.md) — An object that identifies an asset or collection that syncs through iCloud Photos.
- [- cloudIdentifiersForLocalIdentifiers:](<phphotolibrary/cloudidentifiers(forlocalidentifiers_).md>) — Retrieves the equivalent iCloud identifiers for the list of local identifiers. _(deprecated)_
- [- localIdentifiersForCloudIdentifiers:](<phphotolibrary/localidentifiers(for_).md>) — Retrieves the equivalent local identifiers for the list of iCloud identifiers. _(deprecated)_
- [PHLocalIdentifierNotFound](phlocalidentifiernotfound.md) — A constant value that indicates that the system can’t resolve a local object from a global identifier. _(deprecated)_

### Enabling an Upload Job Extension

- [uploadJobExtensionEnabled](phphotolibrary/uploadjobextensionenabled.md) — A Boolean value that indicates whether background asset resource uploading is enabled.
- [- setUploadJobExtensionEnabled:error:](<phphotolibrary/setuploadjobextensionenabled(__).md>) — Enables or disables the background asset resource upload job feature.

### Instance Methods

- [localIdentifierMappings(forSynced:)](<phphotolibrary/localidentifiermappings(forsynced_).md>)
- [- registerPersistentChangesObserver:](<phphotolibrary/register(__)-7lhue.md>) — Registers an observer to be notified when persistent changes occur in the photo library. _(beta)_
- [- unregisterPersistentChangesObserver:](<phphotolibrary/unregisterpersistentchangesobserver(__).md>) — Unregisters a previously registered persistent changes observer. _(beta)_

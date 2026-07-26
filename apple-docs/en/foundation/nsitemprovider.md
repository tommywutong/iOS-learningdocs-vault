---
title: NSItemProvider
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsitemprovider
source_url: 'https://developer.apple.com/documentation/foundation/nsitemprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemprovider.json'
content_hash: 'sha256:0b58b921b14a8cda'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSItemProvider

<sub>Class</sub>

An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSItemProvider
```

## Overview

Starting in iOS 11, item providers play a central role in drag and drop, and in copy and paste. They continue to play a role with app extensions.

The system uses an internal queue when calling the completion blocks for the `NSItemProvider` class. When using an item provider with drag and drop, ensure that UI updates take place on the main queue as follows:

```swift
DispatchQueue.main.async {
    // Work that impacts the user interface.
}
```

### App extension support

An app extension typically encounters item providers when examining the [attachments](nsextensionitem/attachments.md) property of an [NSExtensionItem](nsextensionitem.md) object. During that examination, the extension can use the [- hasItemConformingToTypeIdentifier:](<nsitemprovider/hasitemconformingtotypeidentifier(__).md>) method to look for data that it recognizes. Item providers use [Uniform Type Identifiers](../uniformtypeidentifiers.md) values to identify the data they contain. After finding a type of data that your extension can use, it calls the [- loadItemForTypeIdentifier:options:completionHandler:](<nsitemprovider/loaditem(fortypeidentifier_options_completionhandler_).md>) method to load the actual data, which is delivered to the provided completion handler.

You can create item providers to vend data to another process. An extension that modifies an original data item can create a new `NSItemProvider` object to send back to the host app. When creating data items, you specify your data object and the type of that object. You can optionally use the [previewImageHandler](nsitemprovider/previewimagehandler.md) property to generate a preview image for your data.

A single item provider may use custom blocks to provide its data in many different formats. When configuring an item provider, use the [- registerItemForTypeIdentifier:loadHandler:](<nsitemprovider/registeritem(fortypeidentifier_loadhandler_).md>) method to register your blocks and the formats each one supports. When a client requests data in a particular format, the item provider executes the corresponding block, which is then responsible for coercing the data to the appropriate type and returning it to the client.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an item provider

- [- initWithContentsOfURL:](<nsitemprovider/init(contentsof_).md>) — Provides data-backed content from an existing file.
- [init(contentsOf:contentType:openInPlace:coordinated:visibility:)](<nsitemprovider/init(contentsof_contenttype_openinplace_coordinated_visibility_).md>) — Provides data-backed content from an existing file with the specified parameters.
- [- initWithItem:typeIdentifier:](<nsitemprovider/init(item_typeidentifier_).md>) — Creates an item provider with an object, according to the item provider type coercion policy. _(deprecated)_
- [- init](<nsitemprovider/init().md>) — Creates an empty item provider to which you can later register a data or file representation.
- [- initWithObject:](<nsitemprovider/init(object_).md>) — Creates a new item provider, employing a specified object’s type identifiers to specify the data representations eligible for the provider to load.

### Configuring the provider

- [preferredPresentationSize](nsitemprovider/preferredpresentationsize.md) — The ideal presentation size of the item.
- [preferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.property.md) — The preferred style for presenting the item provider’s data.
- [PreferredPresentationStyle](nsitemprovider/preferredpresentationstyle-swift.enum.md) — The presentation styles that determine how a view shows an item provider’s data.
- [suggestedName](nsitemprovider/suggestedname.md) — The filename to use when writing the provided data to a file on disk.
- [teamData](nsitemprovider/teamdata.md) — The collection of data an app uses to hold private team information during drag and drop.

### Querying the provider’s contents

- [- canLoadObjectOfClass:](<nsitemprovider/canloadobject(ofclass_)-3eig9.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [canLoadObject(ofClass:)](<nsitemprovider/canloadobject(ofclass_)-40grc.md>) — Returns a Boolean value indicating whether an item provider can load objects of a specified class.
- [- hasItemConformingToTypeIdentifier:](<nsitemprovider/hasitemconformingtotypeidentifier(__).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier file options parameter with a value of zero.
- [- hasRepresentationConformingToTypeIdentifier:fileOptions:](<nsitemprovider/hasrepresentationconforming(totypeidentifier_fileoptions_).md>) — Returns a Boolean value indicating whether an item provider contains a data representation conforming to a specified universal type identifier and to specified open-in-place behavior.
- [registeredTypeIdentifiers](nsitemprovider/registeredtypeidentifiers.md) — Returns the array of type identifiers for the item provider, in the same order they were registered.
- [- registeredTypeIdentifiersWithFileOptions:](<nsitemprovider/registeredtypeidentifiers(fileoptions_).md>) — Returns an array with a subset of type identifiers for the item provider, according to the specified file options, in the same order they were registered.

### Loading the provider’s contents

- [- loadItemForTypeIdentifier:options:completionHandler:](<nsitemprovider/loaditem(fortypeidentifier_options_completionhandler_).md>) — Loads the item’s data and coerces it to the specified type. _(deprecated)_
- [- loadDataRepresentationForTypeIdentifier:completionHandler:](<nsitemprovider/loaddatarepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously copies the provided, typed data into a generic data object, returning a progress object.
- [loadDataRepresentation(for:completionHandler:)](<nsitemprovider/loaddatarepresentation(for_completionhandler_).md>) — Asynchronously copies the universal type data into a generic data object, returning a progress object.
- [- loadFileRepresentationForTypeIdentifier:completionHandler:](<nsitemprovider/loadfilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously writes a copy of the provided, typed data to a temporary file, returning a progress object.
- [loadFileRepresentation(for:openInPlace:completionHandler:)](<nsitemprovider/loadfilerepresentation(for_openinplace_completionhandler_).md>) — Asynchronously writes a copy of the universal type data to a temporary file, returning a progress object.
- [- loadInPlaceFileRepresentationForTypeIdentifier:completionHandler:](<nsitemprovider/loadinplacefilerepresentation(fortypeidentifier_completionhandler_).md>) — Asynchronously opens a file in place, if possible, returning a progress object.
- [- loadObjectOfClass:completionHandler:](<nsitemprovider/loadobject(ofclass_completionhandler_)-8ak5d.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadObject(ofClass:completionHandler:)](<nsitemprovider/loadobject(ofclass_completionhandler_)-6pysm.md>) — Asynchronously loads an object of a specified class to an item provider, returning a progress object.
- [loadTransferable(type:completionHandler:)](<nsitemprovider/loadtransferable(type_completionhandler_).md>) — Asynchronously loads an object of a specified transferable type to an item provider, returning a progress object.

### Loading a preview image

- [- loadPreviewImageWithOptions:completionHandler:](<nsitemprovider/loadpreviewimage(options_completionhandler_).md>) — Loads the preview image for the item that the item provider represents.
- [previewImageHandler](nsitemprovider/previewimagehandler.md) — The custom preview image handler block for the item provider.

### Registering CloudKit shares

- [- registerCloudKitShare:container:](<nsitemprovider/registercloudkitshare(__container_).md>) — Registers a CloudKit share for the user to modify.
- [- registerCloudKitShareWithPreparationHandler:](<nsitemprovider/registercloudkitshare(preparationhandler_).md>) — Registers a handler that prepares a new CloudKit share.
- [registerCKShare(_:container:allowedSharingOptions:)](<nsitemprovider/registerckshare(__container_allowedsharingoptions_).md>) — Registers an existing collaboration object on a server.
- [registerCKShare(container:allowedSharingOptions:preparationHandler:)](<nsitemprovider/registerckshare(container_allowedsharingoptions_preparationhandler_).md>) — Creates and registers a new collaboration object using a collection of records to share.

### Registering content types

- [registeredContentTypes](nsitemprovider/registeredcontenttypes.md) — Registered content types in the order the app registers each type.
- [registeredContentTypesForOpenInPlace](nsitemprovider/registeredcontenttypesforopeninplace.md) — Registered content types that the system can load as open-in-place files.
- [- registeredContentTypesConformingToContentType:](<nsitemprovider/registeredcontenttypes(conformingto_).md>) — Returns an array of registered content types that conform to a specified content type.

### Registering data

- [- registerDataRepresentationForTypeIdentifier:visibility:loadHandler:](<nsitemprovider/registerdatarepresentation(fortypeidentifier_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [registerDataRepresentation(for:visibility:loadHandler:)](<nsitemprovider/registerdatarepresentation(for_visibility_loadhandler_).md>) — Registers a data-backed representation for an item, specifiying item visibility and a load handler.
- [- registerItemForTypeIdentifier:loadHandler:](<nsitemprovider/registeritem(fortypeidentifier_loadhandler_).md>) — Lazily registers an item, according to the item provider type coercion policy. _(deprecated)_

### Registering files

- [- registerFileRepresentationForTypeIdentifier:fileOptions:visibility:loadHandler:](<nsitemprovider/registerfilerepresentation(fortypeidentifier_fileoptions_visibility_loadhandler_).md>) — Registers a file-backed representation for an item, specifying file options, item visibility, and a load handler.
- [registerFileRepresentation(for:visibility:openInPlace:loadHandler:)](<nsitemprovider/registerfilerepresentation(for_visibility_openinplace_loadhandler_).md>) — Registers a file-backed representation for an item with item visibility, an open-in-place option, and a load handler.

### Registering group activities

- [registerGroupActivity(_:)](<nsitemprovider/registergroupactivity(__).md>) — Registers a group activity instance with the specificed options.
- [registerGroupActivity(preparationHandler:)](<nsitemprovider/registergroupactivity(preparationhandler_).md>) — Registers a group activity instance asynchronously with the specified options.

### Registering objects

- [- registerObject:visibility:](<nsitemprovider/registerobject(__visibility_).md>) — Adds representations of a specified object to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [- registerObjectOfClass:visibility:loadHandler:](<nsitemprovider/registerobject(ofclass_visibility_loadhandler_)-9sndn.md>) — Lazily adds representations of a specified object class to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [registerObject(ofClass:visibility:loadHandler:)](<nsitemprovider/registerobject(ofclass_visibility_loadhandler_)-133rx.md>) — Lazily adds representations of a specified object type to an item provider, based on the object’s implementation of the item provider writing protocol, and adhering to a visibility specification.
- [register(_:)](<nsitemprovider/register(__).md>) — Adds representations of a specified transferable type to an item provider.

### Getting the provider’s frame

- [sourceFrame](nsitemprovider/sourceframe.md) — The rectangle that the item occupies in the host app’s source window.
- [containerFrame](nsitemprovider/containerframe.md) — The rectangle of the item’s visible content.

### Constants

- [CompletionHandler](nsitemprovider/completionhandler.md) — A block that receives the item provider’s data.
- [LoadHandler](nsitemprovider/loadhandler.md) — A block that loads the item provider’s data and coerces it to the specified type.
- [Options Dictionary Key](options-dictionary-key.md) — Keys indicating options to use when generating the item provider’s data.
- [Keys for Items Accessed in JavaScript Code](keys-for-items-accessed-in-javascript-code.md) — Keys in property list items that the system recieves from or sends to JavaScript code.
- [NSItemProviderErrorDomain](nsitemprovider/errordomain.md) — The error domain associated with the item provider.
- [NSItemProviderFileOptions](nsitemproviderfileoptions.md) — Data-access specifications that declare how to handle items.
- [NSItemProviderReading](nsitemproviderreading.md) — The protocol for implementing a class to allow an item provider to create an instance of the class.
- [NSItemProviderWriting](nsitemproviderwriting.md) — The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [NSItemProviderRepresentationVisibility](nsitemproviderrepresentationvisibility.md) — Specifications that control which categories of processes can see an item.
- [ErrorCode](nsitemprovider/errorcode.md) — The error codes that describe problems with consuming data from an item provider.

### Initializers

- [init(contentsOfURL:)](<nsitemprovider/init(contentsofurl_).md>)

## See Also

### Attachments

- [NSExtensionItem](nsextensionitem.md) — An immutable collection of values representing different aspects of an item for an extension to act upon.
- [Add Functionality to Finder with Action Extensions](../appkit/add-functionality-to-finder-with-action-extensions.md) — Implement Action Extensions to provide quick access to commonly used features of your app.

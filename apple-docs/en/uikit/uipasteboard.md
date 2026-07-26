---
title: UIPasteboard
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard.json'
content_hash: 'sha256:fee9e8f2d50d17da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPasteboard

<sub>Class</sub>

An object that helps a user share data from one place to another within your app, and from your app to other apps.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIPasteboard
```

## Overview

For sharing data with any other app, use the systemwide general pasteboard. For sharing data with another app from your team — that has the same team ID as the app to share from — configure an App Group. For more information about configuring an App Group, see [Configuring app groups](../xcode/configuring-app-groups.md).

In typical usage, an object in your app writes data to a pasteboard when the user requests a copy, cut, or duplicate operation on a selection in the user interface. Another object in the same or different app then reads that data from the pasteboard and presents it to the user at a new location. This usually happens when the user requests a paste operation.

> [!important] Important
> Starting in iOS 14, the system notifies the user when an app gets general pasteboard content that originates in a different app without _user intent_. The system determines user intent based on user interactions, such as tapping a system-provided control or pressing Command-V. Use the properties and methods below to determine whether pasteboard items match various patterns, such as web search terms, URLs, or numbers, without notifying the user.

### The general pasteboard and named pasteboards

The system identifies the systemwide general pasteboard with the [UIPasteboardNameGeneral](uipasteboard/name-swift.struct/general.md) pasteboard name, and you can use it for any type of data. Obtain the general pasteboard from the [generalPasteboard](uipasteboard/general.md) shared system pasteboard object.

You can create named pasteboards with the class methods [+ pasteboardWithName:create:](<uipasteboard/init(name_create_).md>) and [+ pasteboardWithUniqueName](<uipasteboard/withuniquename().md>) for sharing data within your app, and from your app to other apps that have the same Team ID.

### Using pasteboards

The [UIPasteboard](uipasteboard.md) class provides methods for reading and writing individual pasteboard items, as well as methods for reading and writing multiple pasteboard items at once. For more information, see [Getting and setting pasteboard items](uipasteboard.md#Getting-and-setting-pasteboard-items) in the topic groups below. The data to write to a pasteboard can be in one of the following forms:

- If the data is an object that conforms to [NSItemProviderWriting](../foundation/nsitemproviderwriting.md), use [- setItemProviders:localOnly:expirationDate:](<uipasteboard/setitemproviders(__localonly_expirationdate_).md>) to write it to the pasteboard.
- If you can represent the data with a common object — such as [NSString](../foundation/nsstring.md), [NSArray](../foundation/nsarray.md), [NSDictionary](../foundation/nsdictionary.md), [NSDate](../foundation/nsdate.md), [NSNumber](../foundation/nsnumber.md), [UIImage](uiimage.md), or [NSURL](../foundation/nsurl.md) — you can write it to the pasteboard as a value using a method such as [- setValue:forPasteboardType:](<uipasteboard/setvalue(__forpasteboardtype_).md>).
- If the data is binary, use the [- setData:forPasteboardType:](<uipasteboard/setdata(__forpasteboardtype_).md>) method to write it to the pasteboard.

The [UIPasteboard](uipasteboard.md) class provides convenience methods for writing and reading strings, images, URLs, and colors to and from single or multiple pasteboard items. See [Getting and setting pasteboard items of standard data types](uipasteboard.md#Getting-and-setting-pasteboard-items-of-standard-data-types) in the topic groups below.

> [!note] Note
> Before you attempt to read a particular data type from a pasteboard by using the methods in [Getting and setting pasteboard items of standard data types](uipasteboard.md#Getting-and-setting-pasteboard-items-of-standard-data-types) in the topic groups below, check for the presence of data of the type you want. Do this by using the type-checking methods.

[UIPasteboard](uipasteboard.md) provides properties for directly checking whether specific data types are present on a pasteboard, see [Checking for data types on a pasteboard](uipasteboard.md#Checking-for-data-types-on-a-pasteboard) in the topic groups below. Use these properties, rather than attempting to read pasteboard data, to avoid causing the system to needlessly attempt to fetch data before necessary, or when the data might not be present. For example, use the [hasStrings](uipasteboard/hasstrings.md) property to determine whether to present a string-data paste option in the user interface, using code like the following:

```objc
if UIPasteboard.general.hasStrings {
    // Enable string-related control...
}
```

Use the following properties to avoid user notifications and alerts when the system doesn’t establish user intent:

- [numberOfItems](uipasteboard/numberofitems.md)
- [pasteboardTypes](uipasteboard/types.md), [- pasteboardTypesForItemSet:](<uipasteboard/types(foritemset_).md>)
- [- itemSetWithPasteboardTypes:](<uipasteboard/itemset(withpasteboardtypes_).md>)
- [hasColors](uipasteboard/hascolors.md), [hasImages](uipasteboard/hasimages.md), [hasStrings](uipasteboard/hasstrings.md), [hasURLs](uipasteboard/hasurls.md)
- [canLoadObject(ofClass:)](<../foundation/nsitemprovider/canloadobject(ofclass_)-3eig9.md>), [canLoadObject(ofClass:)](<../foundation/nsitemprovider/canloadobject(ofclass_)-40grc.md>)
- any of the pattern-detection methods in the [Detecting patterns of content in pasteboard items](uipasteboard.md#Detecting-patterns-of-content-in-pasteboard-items) group in the topic groups below

The system notifies the user when you access properties or call methods that pull data from the pasteboard if the system doesn’t determine that the user intends to access that data.

### Pasteboard items and representation types

When you write an object to a pasteboard, the pasteboard stores it as a _pasteboard item_. A pasteboard item consists of one or more key-value pairs in which the key identifies the representation type (sometimes called a _pasteboard type_) of the value.

A uniform type identifier frequently functions as the key for a representation type. For example, you can use the [UTTypeJPEG](../uniformtypeidentifiers/uttypejpeg.md) uniform type identifier (a constant for `public.jpeg`) as a representation type key for JPEG data.

For a discussion of uniform type identifiers, and a list of common ones, see [Uniform Type Identifiers](../uniformtypeidentifiers.md).

Your app can use any string to name a representation type; however, for app-specific data types, it’s best practice to use reverse-DNS notation to ensure the uniqueness of the type (for example, `com.myCompany.myApp.myType`).

You can provide flexibility for data sharing by providing multiple representation types for a pasteboard item during a copy or cut operation. Various contexts within your app or other apps can then make use of an appropriate representation type. For example, when a user copies an image, your app can write multiple representation types, such as in the PNG, JPEG, and GIF data formats, to a pasteboard. If the original image is in PNG format, but the receiving app can handle only GIF images, it can still use the pasteboard data.

For more about representation types, read the discussion for the [pasteboardTypes](uipasteboard/types.md) instance method.

### Sharing pasteboards between devices

When a user signs into iCloud, the general pasteboard automatically transfers its contents to nearby devices that use the same iCloud account. You can control Handoff behavior when writing contents to the general pasteboard, and can set an expiration for items, using the [- setItemProviders:localOnly:expirationDate:](<uipasteboard/setitemproviders(__localonly_expirationdate_).md>), [- setObjects:localOnly:expirationDate:](<uipasteboard/setobjects(__localonly_expirationdate_)-3h3iz.md>), or [- setItems:options:](<uipasteboard/setitems(__options_).md>) methods, as follows:

- To exclude a pasteboard from Handoff, specify [false](../swift/false.md) for the `localOnly` parameter, or call the [- setItems:options:](<uipasteboard/setitems(__options_).md>) method with the [UIPasteboardOptionLocalOnly](uipasteboard/optionskey/localonly.md) option.
- To indicate an expiration time and date for copied data, provide the `expirationDate` parameter, or call the [- setItems:options:](<uipasteboard/setitems(__options_).md>) method with the [UIPasteboardOptionExpirationDate](uipasteboard/optionskey/expirationdate.md) option. At the time and date that you set, the system removes the pasteboard items from the pasteboard.

### Using pasteboards with other objects

Although the [UIPasteboard](uipasteboard.md) class is central to copy, paste, and duplicate operations, you can employ protocols and instances of other UIKit classes in these operations as well, such as the following:

- [UIEditMenuInteraction](uieditmenuinteraction.md) — Displays a menu with edit actions, such as Copy, Cut, Paste, Select, and Select All, above or below the selection.
- [UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md) — Objects implement this protocol to indicate that they support copying and sharing data.
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — Objects implement this protocol to indicate whether they support pasting with a specific [UIPasteConfiguration](uipasteconfiguration.md).
- [UIResponder](uiresponder.md) — Responders implement [- canPerformAction:withSender:](<uiresponder/canperformaction(__withsender_).md>) to enable or disable commands in the above-mentioned menu based on the current context.
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md) — Responders implement methods that this informal protocol declares to handle the chosen menu commands (for example, `copy:` and `paste:`).

A typical app that implements copy, paste, and duplicate operations also manages and presents related selections in its user interface. In addition, your app needs to coordinate changes in pasteboard content with changes to its data model, as appropriate for your app.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting and removing pasteboards

- [generalPasteboard](uipasteboard/general.md) — The systemwide general pasteboard, which you use for general copy-paste operations.
- [+ pasteboardWithName:create:](<uipasteboard/init(name_create_).md>) — Returns a pasteboard that you identify by name, optionally creating it if it doesn’t exist.
- [+ pasteboardWithUniqueName](<uipasteboard/withuniquename().md>) — Returns an app pasteboard that you identify by a unique system-generated name.
- [+ removePasteboardWithName:](<uipasteboard/remove(withname_).md>) — Invalidates the designated app pasteboard.

### Getting and setting pasteboard attributes

- [name](uipasteboard/name-swift.property.md) — The name of the pasteboard.
- [changeCount](uipasteboard/changecount.md) — The number of times the pasteboard’s contents change.

### Detecting patterns of content in pasteboard items

- [detectPatterns(for:completionHandler:)](<uipasteboard/detectpatterns(for_completionhandler_)-23vwn.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:)](<uipasteboard/detectedpatterns(for_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard, and return the patterns that it matches.
- [detectPatterns(for:inItemSet:completionHandler:)](<uipasteboard/detectpatterns(for_initemset_completionhandler_)-7ubl1.md>) — Requests that the data detection system identify the patterns that you specify for the pasteboard items, and provide the patterns that it matches to your closure.
- [detectedPatterns(for:inItemSet:)](<uipasteboard/detectedpatterns(for_initemset_).md>) — Requests that the data detection system asynchronously identify the patterns that you specify for the pasteboard items, and return the patterns that it matches.
- [detectValues(for:completionHandler:)](<uipasteboard/detectvalues(for_completionhandler_)-6adre.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard, and provide the values that it matches to your closure.
- [detectedValues(for:)](<uipasteboard/detectedvalues(for_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard, and return the values that it matches.
- [detectValues(for:inItemSet:completionHandler:)](<uipasteboard/detectvalues(for_initemset_completionhandler_)-pm9l.md>) — Requests that the data detection system identify the types of data that you specify for the pasteboard items, and provide the values that it matches to your closure.
- [detectedValues(for:inItemSet:)](<uipasteboard/detectedvalues(for_initemset_).md>) — Requests that the data detection system asynchronously identify the types of values that you specify for the pasteboard item, and return the values that it matches for each pasteboard.
- [DetectedValues](uipasteboard/detectedvalues.md) — An object that contains common types of data that the data detection system matches for a pasteboard.
- [DetectionPattern](uipasteboard/detectionpattern.md) — An object that represents a pattern to detect for the pasteboard, such as a URL, text, or a number.

### Determining types of pasteboard items

- [pasteboardTypes](uipasteboard/types.md) — The types of the first item on the pasteboard.
- [- pasteboardTypesForItemSet:](<uipasteboard/types(foritemset_).md>) — Returns an array of representation types for each specified pasteboard item.
- [- containsPasteboardTypes:](<uipasteboard/contains(pasteboardtypes_).md>) — Returns whether the pasteboard holds data of the specified representation type.
- [- containsPasteboardTypes:inItemSet:](<uipasteboard/contains(pasteboardtypes_initemset_).md>) — Returns whether the specified pasteboard items contain data of the given representation types.
- [- itemSetWithPasteboardTypes:](<uipasteboard/itemset(withpasteboardtypes_).md>) — Returns an index set identifying pasteboard items having the specified representation types.

### Getting and setting pasteboard items

- [numberOfItems](uipasteboard/numberofitems.md) — The number of items for the pasteboard.
- [items](uipasteboard/items.md) — The pasteboard items on the pasteboard.
- [- addItems:](<uipasteboard/additems(__).md>) — Appends pasteboard items to the current contents of the pasteboard.
- [- setItems:options:](<uipasteboard/setitems(__options_).md>) — Adds an array of items to a pasteboard, and sets privacy options for all the items on the pasteboard.
- [- dataForPasteboardType:](<uipasteboard/data(forpasteboardtype_).md>) — Returns the data on the pasteboard for the given representation type.
- [- dataForPasteboardType:inItemSet:](<uipasteboard/data(forpasteboardtype_initemset_).md>) — Returns the data objects in the indicated pasteboard items that have the given representation type.
- [- setData:forPasteboardType:](<uipasteboard/setdata(__forpasteboardtype_).md>) — Puts data on the pasteboard for the specified representation type.
- [- valueForPasteboardType:](<uipasteboard/value(forpasteboardtype_).md>) — Returns an object on the pasteboard for the given representation type.
- [- valuesForPasteboardType:inItemSet:](<uipasteboard/values(forpasteboardtype_initemset_).md>) — Returns the objects on the indicated pasteboard items that have the given representation type.
- [- setValue:forPasteboardType:](<uipasteboard/setvalue(__forpasteboardtype_).md>) — Puts an object on the pasteboard for the specified representation type.

### Getting and setting pasteboard items of standard data types

- [string](uipasteboard/string.md) — The string value of the first pasteboard item.
- [strings](uipasteboard/strings.md) — An array of strings in all pasteboard items.
- [image](uipasteboard/image.md) — The image object of the first pasteboard item.
- [images](uipasteboard/images.md) — An array of image objects in all pasteboard items.
- [URL](uipasteboard/url.md) — The URL object of the first pasteboard item.
- [URLs](uipasteboard/urls.md) — An array of URL objects in all pasteboard items.
- [color](uipasteboard/color.md) — The color object of the first pasteboard item.
- [colors](uipasteboard/colors.md) — An array of color objects in all pasteboard items.

### Checking for data types on a pasteboard

- [hasColors](uipasteboard/hascolors.md) — A Boolean value that indicates whether the pasteboard contains contains a nonempty array of colors.
- [hasImages](uipasteboard/hasimages.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of images.
- [hasStrings](uipasteboard/hasstrings.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of strings.
- [hasURLs](uipasteboard/hasurls.md) — A Boolean value that indicates whether the pasteboard contains a nonempty array of URLs.

### Getting and setting item providers

- [itemProviders](uipasteboard/itemproviders.md) — An array of item providers for the pasteboard.
- [- setItemProviders:localOnly:expirationDate:](<uipasteboard/setitemproviders(__localonly_expirationdate_).md>) — Sets and configures an explicit array of item providers for the pasteboard.
- [- setObjects:](<uipasteboard/setobjects(__)-lljo.md>) — Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [setObjects(_:)](<uipasteboard/setobjects(__)-fjg8.md>) — Sets an array of item providers for the pasteboard, based on a specified array of objects.
- [- setObjects:localOnly:expirationDate:](<uipasteboard/setobjects(__localonly_expirationdate_)-3h3iz.md>) — Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.
- [setObjects(_:localOnly:expirationDate:)](<uipasteboard/setobjects(__localonly_expirationdate_)-26u8o.md>) — Sets and configures an array of item providers for the pasteboard, based on a specified array of objects.

### Constants

- [Name](uipasteboard/name-swift.struct.md) — Constants that identify the name of a pasteboard.
- [Pasteboard Names](pasteboard-names.md) — Names identifying the system pasteboards.
- [OptionsKey](uipasteboard/optionskey.md) — Options for describing pasteboard privacy.
- [Pasteboard Data Type Representations](pasteboard-data-type-representations.md) — Pasteboard-item representation types, as for a given object value.
- [UserInfo Dictionary Keys](userinfo-dictionary-keys.md) — Use these keys to access the representation types of pasteboard items that you add to, or remove from, a pasteboard.

### Notifications

- [UIPasteboardChangedNotification](uipasteboard/changednotification.md) — A notification that a pasteboard object posts when its contents change.
- [UIPasteboardRemovedNotification](uipasteboard/removednotification.md) — A notification that a pasteboard object posts just before an app removes it.

### Deprecated

- [Deprecated symbols](uipasteboard-deprecated-symbols.md) — Review unsupported symbols and their replacements.

### Structures

- [ChangedMessage](uipasteboard/changedmessage.md)
- [RemovedMessage](uipasteboard/removedmessage.md)

## See Also

### Pasteboard

- [UIPasteControl](uipastecontrol.md) — A button that a person taps to place pasteboard contents in your app.
- [Configuration](uipastecontrol/configuration-swift.class.md) — An object that determines a paste button’s color, corner style, icon, and text.
- [DisplayMode](uipastecontrol/displaymode.md) — Options that determine whether a paste button composes an icon, textual label, or both.
- [UIPasteConfiguration](uipasteconfiguration.md) — The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md) — The interface that determines whether a responder object supports paste configuration.

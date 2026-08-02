---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/Exporting/Exporting.html
archived_at: '2026-07-15T07:32:28.031042Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X Workflows Developer Guide](About%20Final%20Cut%20Pro%20X%20Workflows.md)


[Next](Working%20with%20Custom%20Metadata.md)[Previous](Importing.md)

# Exporting

Final Cut Pro X can export the following to another application:

- Rendered media of the edited timeline
- A description of the edit as FCPXML
- An archived library and associated FCPXML

The user initiates an export with the share command in Final Cut Pro X. If applicable, Final Cut Pro X interacts with the target application to control certain aspects of the export operation.

Starting with version 10.2.2, Final Cut Pro X can transfer an archived library along with its library XML.

In addition, the user can export FCPXML in the following two ways:

- Manually export an FCPXML document
- Drag and drop objects from Final Cut Pro X to another application (new in version 10.3)

Final Cut Pro X can export FCPXML in two DTD versions: the latest, and the one prior to the latest.

The user selects a share destination when initiating the export process through the Final Cut Pro X File > Share menu item. Final Cut Pro X manages export configurations as share destinations. A share destination can have a target application that receives the export output and also influences the export operation. Refer to [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for details on managing and using share destinations.

When exporting to a share destination:

- Final Cut Pro X exports the rendered timeline as a media file, either transcoding it into a particular format or leaving it in the render format (that is, Apple ProRes). The exported media file has a set of metadata, referred to as _Share Metadata_, that you can choose and specify values for when you start the export operation.
- Final Cut Pro X can export its events, projects, or an entire library as FCPXML. Final Cut Pro X can include metadata associated with a project or an asset in the exported FCPXML. Only metadata items in the selected metadata view are included in the output. You can specify a metadata view to control the set of metadata items that go into the output.
- If your application requests a library archive, Final Cut Pro X checks that the state of the library bundle is consistent and copies the content of the bundle into the location specified, excluding temporary files and various cached data that can be regenerated. Media is not included in the archive even if you chose to manage the media inside the library.

Your application, when specified as the target of a share destination, can influence the export operation, as discussed in [Custom Share Destination](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltk).

Final Cut Pro X allows you to transfer the following items from your Final Cut Pro X project or library to another application as FCPXML:

- A single library
- A group of events
- A group of clips
- A group of collections

You can also include metadata from a metadata view in the exported FCPXML. You must specify the metadata view upon export.

To export an FCPXML document, select one of the supported items listed above and choose File > Export XML.

Final Cut Pro X supports drag-and-drop of the following items from Final Cut Pro X to another application that supports drag-and-drop as FCPXML:

- A single library in the Final Cut Pro X sidebar—The exported FCPXML contains the entire library.
- A group of events in the Final Cut Pro X sidebar—The exported FCPXML contains only the list of the events; information about the library is not included.
- A group of items in the Final Cut Pro X browser, including projects and clips—The exported FCPXML contains a list of the dragged items, either projects or clips; information about the event is not included.
- A group of collection items in the Final Cut Pro X sidebar—The exported FCPXML contains a list of the collection items; information about the event is not included.

When a user selects one or more objects in the Final Cut Pro X sidebar or browser and starts dragging them, Final Cut Pro X creates a _promise_ in the pasteboard—see _[Pasteboard Programming Guide](../../Cocoa/Pasteboard%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4daojz)_. When the user drops the dragged objects into an application, and the application accepts the drop, Final Cut Pro X creates an FCPXML representation of the objects for the application to retrieve.

The dragged objects are represented as an FCPXML document in the latest DTD version with Unicode text, and the pasteboard type is `com.apple.finalcutpro.xml`. If applicable, the exported FCPXML document includes metadata items from the currently selected metadata view in the inspector pane.

Final Cut Pro X uses a share destination to manage information associated with a particular type of export or share. Refer to [Final Cut Pro X Help](http://help.apple.com/finalcutpro/) for more information.

You can create your own custom share destination and include the following information:

- Export settings—The choice of codec, file format, and so forth.
- Target application—The target application where the exported files are to be sent.

Final Cut Pro X queries the target application for the following export control details when the user performs an export operation through a custom share destination:

- Whether to export the project’s rendered media using the user’s export settings.
- Whether to export the description of the project as project XML along with a metadata view set (that determines the metadata keys to include in the XML).
- Which DTD version to use for the exported FCPXML (current or previous).
- Whether to include an archive of the project’s library, along with the library XML that includes the list of media used in the project.

To create a custom share destination, refer to the [Final Cut Pro X Help](http://help.apple.com/finalcutpro/).

Final Cut Pro X supports a mechanism for distributing custom share destinations to other Final Cut Pro X users or workstations as `.fcpxdest` files.

To transfer a destination to another Final Cut Pro X workstation:

1. Drag a destination from the Destinations list in the Destinations pane of the Final Cut Pro X Preference window to a location on your system.
2. Drag the `.fcpxdest` file into the list of share destinations on another Final Cut Pro X workstation.

Refer to the _Share destinations between Final Cut Pro X users_ section in the _Final Cut Pro X Help_. Alternatively, you can install `.fcpxdest` files in either of the following locations:

- `/Library/Application Support/ProApps/Share Destinations/`
- `~/Library/Application Support/ProApps/Share Destinations/`

When the user exports a project timeline through a custom share destination with a target application specified, Final Cut Pro X first determines whether the application is capable of responding to inquiries from Final Cut Pro X. It does this by inspecting the bundle plist of the application. The information that should be in the bundle plist is discussed in [Signaling Application Capabilities](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltemi).

Assuming Final Cut Pro X has determined that your application is capable of responding to its queries, it sends a _Create Asset_ Apple event requesting a new placeholder asset to which the export output should be associated. This request also includes the name of the asset, the set of share metadata, and a list of metadata views. The reason for providing metadata views here is to let the application decide the set of metadata that goes into the project XML. Your application is expected to return an object specifier identifying the newly created placeholder asset object.

![../Art/exportcontrolprotocol_createasset_2x.png](attachments/Art/exportcontrolprotocol_createasset_2x.png)

After the new asset object is successfully created in the target application, Final Cut Pro X asks the application for the following:

- The location for the export output files.
- Whether the application wants the following export outputs:

  - Rendered/transcoded project media
  - Project XML as a description of edits
  - Library archive along with the library XML
- An updated set of share metadata.
- The metadata view to include in the project XML.

Final Cut Pro X asks the application for the above information by sending a series of _Get Property_ Apple events. The application is expected to return the appropriate property values.

![../Art/exportcontrolprotocol_getpropertyinfo_2x.png](attachments/Art/exportcontrolprotocol_getpropertyinfo_2x.png)

With these pieces of information, Final Cut Pro X performs the export operation and places the relevant output files at the location returned from the application. When the export is complete, Final Cut Pro X notifies the application that the export output files are available by sending an _Open Document_ Apple event. This event has the file URLs of the export output files.

![../Art/exportcontrolprotocol_opendocument_2x.png](attachments/Art/exportcontrolprotocol_opendocument_2x.png)

The target application can control the export operation through the interaction outlined above. To do so, the application must do the following:

- Indicate in its bundle plist that it can respond to inquiries from Final Cut Pro X.
- Respond to Apple events sent by Final Cut Pro X.

The most important requirement is being able to respond to Apple events sent from Final Cut Pro X. Consult the _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_ for details of how an application implements such functionality in general. In particular, the following are required:

- Define the scripting terminology including the events, the object classes, and the record types.
- Implement command-handler classes that are referenced from the scripting terminology definitions.
- Implement the object classes and associated properties according to key-value coding (KVC) and other required conventions documented in the _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_.

Refer to [Appendix A: ProVideo Asset Management Suite](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqnjnknltc) for more information on the scripting terminology definitions.

This section discusses what your application needs to implement in order to interact with Final Cut Pro X to influence the export process.

Your application must do the following when the user initiates the export operation:

- Indicate your application’s capabilities—See [Signaling Application Capabilities](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltemi).
- Define your application’s scripting terminology—See [Scripting Definition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltemy).
- Interact with Final Cut Pro X using Apple events—See [Interaction Through Apple Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltena).

Final Cut Pro X needs to know up front whether the application understands the protocol. To indicate this capability, the application must have the following entry in its bundle plist:

```
<key>com.apple.proapps.MediaAssetProtocol</key>
<dict>
</dict>
```


The application needs to have a scripting terminology definition that defines the events, object classes, and record types described in this section. Refer to the _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_ for details. Also, refer to [Appendix A: ProVideo Asset Management Suite](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqnjnknltc) for the scripting definition Final Cut Pro X uses.

__Record Type: asset location__

Describes where files associated with an object of class `asset` (discussed later in this section) are located.

| Property | Type | Description |
| --- | --- | --- |
| `folder` | file | The containing folder path. |
| `base name` | text | The base name for the export output files. This name must match the asset name. |
| `has description` | boolean | Set to `true` if the application expects XML as the exported output. |
| `has media` | boolean | Set to `true` if the application expects media as the exported output. |

__Record Type: library location__

Describes where library files associated with an asset are located.

| Property | Type | Description |
| --- | --- | --- |
| `library folder` | file | The containing folder path. |
| `library base name` | text | The base name for the export output files. |
| `has archive` | boolean | Set to `true` if the application expects a library archive as the exported output. |
| `has library description` | boolean | Set to `true` if the application expects library XML as the exported output. |

__Object Class Type: asset__

Represents an asset object corresponding to the export output in the application.

| Property | Type | Description |
| --- | --- | --- |
| `id` | text | The unique asset identifier. |
| `name` | text | The asset name. |
| `location info` | asset location | The location of files associated with the asset. |
| `library info` | library location | The location of the library files associated with the asset. |
| `metadata` | user defined record | The shared metadata set associated with the asset. |
| `data options` | user defined record | The options set for the asset data. |

__Event Type: make__

Creates a new object, specifically an asset object.

| Parameter | Type | Description |
| --- | --- | --- |
| `new` | type | The new object’s class. |
| `at` | location specifier | The location in which to insert the new object. |
| `with data` | any | The initial contents of the object. |
| `with properties` | record | A list of object properties used to initialize the new object, including the following:   - `name` (text)—The asset name. - `metadata` (record)—The metadata set associated with the asset object. - `data options` (record)—The option set used to create the asset data. |

To enable access from a sandboxed application to the objects and the events in your application, the application must specify the `com.apple.assetmanagement.import` access group for the asset object class and for the respective element in its container, and must also specify the same access group for the _Create Asset_ event. See [Appendix A: ProVideo Asset Management Suite](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqnjnknltc) for more details.

Once Final Cut Pro X confirms that the application is capable of interacting with Final Cut Pro X for the export operation, it sends a series of Apple events in the order described below. Your application is expected to handle these events and return the appropriate information.

Refer to [Appendix B: AppleScript Example](Appendix%20B-%20AppleScript%20Example.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqnrnknltc) for a script example and a sample log of events and responses that illustrate the interaction.

1. _Create Asset_ event.

```
make new asset with properties { name: <asset name>, metadata: <metadata record>, data options: <options record> }
```

   Final Cut Pro X sends a _Create Asset_ event when the user initiates the share operation. The application is expected to create a placeholder asset object that represents the output of the share operation and to return an object specifier that Final Cut Pro X uses to reference the asset object in subsequent Apple events.

   While handling this event, the application has an opportunity to bring up its UI, before a possibly time-consuming transcode operation starts. This UI can be used to let the user specify information relevant to the operation the application is about to perform on the export output. This information may include custom metadata to be stored along with the media or data that determines the location of the output.

   The event parameters include the following asset object properties:

| Property | Description |
| --- | --- |
| `name` | The asset name. Final Cut Pro X derives this from the project name. |
| `metadata` | A record representing the set of share metadata, where the keys are the reverse DNS style metadata keys and the values are the associated metadata values. |
| `data options` | A record containing the export output options. This record holds the available choices for the options below.  - __Key:__ availableMetadataSets - __Type:__ list - __Description:__ A list of available metadata views in Final Cut Pro X. - __Key:__ availableDescriptionVersions - __Type:__ list - __Description:__ A list of available DTD versions Final Cut Pro X can export. Your application should indicate its choice in response to another Apple event, sent later, that asks for the value of the data options property. Refer to the _[Cocoa Scripting Guide](../../Cocoa/Cocoa%20Scripting%20Guide/Introduction%20to%20Cocoa%20Scripting%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnru)_ for details. |

   The return value for this Apple event is an object specifier for the new asset object created.
2. _Get Location Info Property_ event.

```
get location info of <asset object specifier>
```

   Once a new asset object is created in the application, Final Cut Pro X sends a _Get Location Info Property_ event asking for the location of the export output files. The application is expected to return an __asset location__ record as described in [Scripting Definition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltemy). In particular, the `folder` property of the record specifies the folder location where the export output files are placed. The `base name` property is used as the base name of the export output files. The media file has an extension based on the file format, and the XML file has the `.fcpxml` extension. If the application expects the XML file, be sure to set the `has description` property to _true_ in the asset location record. If the application expects the media file, be sure to set the `has media` property to _true_ in the asset location record.
3. _Get Library Info Property_ event.

```
get library info of <asset object specifier>
```

   Final Cut Pro X sends a _Get Library Info Property_ event asking for the location of the library output files. The application is expected to return a __library location__ record as described in [Scripting Definition](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltemy). In particular, the `library folder` property of the record specifies the folder location where the library output files are placed. The `library base name` property is used as the base name of the library output files. The library archive has the `.fcpbundle` extension, and the XML file has the `.fcpxml` extension. If the application expects the library files, be sure to set the `has archive` and/or `has library description` properties to `true` in the library location record.

   If the `library folder` property is not specified, the asset location folder is used. If the base name property is not specified, the asset name is used with a suffix as if it was for the “library” role, to distinguish the library XML from the project URL.

   This event is sent after the `get location info` event. If the application does not respond to this event, Final Cut Pro X assumes that the application does not want the library files.
4. _Get Metadata Property_ event.

```
get metadata of <asset object specifier>
```

   Final Cut Pro X sends a _Get Metadata Property_ event asking for an updated set of metadata. Final Cut Pro X then updates the project and includes the updated metadata into the export output. Final Cut Pro X previously supplied the original set of metadata through the _Create New Asset_ event. The application is expected to return a user record that has metadata keys and their values.

   In particular, the metadata key `com.apple.proapps.share.id` represents the unique ID of the media asset. The application can generate a unique ID for its own purposes and include that ID in the updated metadata set. Final Cut Pro X includes this ID in the export output so that the application can use it to track the files associated to a particular asset.
5. _Get Data Options Property_ event.

```
get data options of <asset object specifier>
```

   Final Cut Pro X sends a _Get Data Options Property_ event requesting the data options to be used in generating the export output. The application is expected to return a user record with the following keys and their associated values:

| Key | Type | Description |
| --- | --- | --- |
| `descriptionVersion` | text | The DTD version to use for XML export. The default version is the version used in the last XML export. |
| `metadataSet` | text | The name of the metadata view containing the metadata items to be included in the project XML. |
6. _Open Document_ event.

```
open <list of export output files>
```

   Once the export operation has completed, Final Cut Pro X sends the paths to the exported output files through the _Open Document_ event. The expected return value is the object specifier for the asset object. The application is expected to associate the files to the asset it has created, using the folder and the base name of the files to match against the location information of the asset.

This section provides additional information regarding application implementation details.

A media asset may correspond to a document in some applications, while in others it may just be an element of a larger entity (such as a media asset database) which itself may be a document. The protocol between Final Cut Pro X and your application through Apple events is intended to be agnostic to the object containment hierarchy in your application, as far as your application returns an object specifier with which Final Cut Pro X can access a specific asset object.

The scripting definition (see [Appendix A: ProVideo Asset Management Suite](Appendix%20A-%20ProVideo%20Asset%20Management%20Suite.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqnjnknltc)) defines an asset as a document element, but it does not have to be that way.

When an asset object is not a document, handling an _Open Document_ Apple event to associate files to an asset might be a bit awkward. Because Cocoa handles the _Open Document_ Apple event, you would need a custom document controller to override the behavior of Cocoa when your application opens a file, and associate a file with either an existing asset object or a new asset object if necessary. The association should be based on matching the URL of the asset.

Applications using Cocoa Scripting Support to handle Apple events sent by Final Cut Pro X must support conversions between the Apple event descriptor types used by Final Cut Pro X and the respective Foundation classes as Objective-C categories (as listed below), since they are not currently implemented by Cocoa. Use the following code snippet as necessary.

- Apple event record descriptor (_typeAERecord_) and _NSDictionary_

```objc
@interface NSDictionary (UserDefinedRecord)
  +(NSDictionary*)scriptingUserDefinedRecordWithDescriptor:(NSAppleEventDescriptor*)desc;
  -(NSAppleEventDescriptor*)scriptingUserDefinedRecordDescriptor;
@end
```
- Apple event list descriptor (_typeAEList_) and _NSArray_

```objc
@interface NSArray (UserList)
  +(NSArray*)scriptingUserListWithDescriptor:(NSAppleEventDescriptor*)desc;
  -(NSAppleEventDescriptor*)scriptingUserListDescriptor;
@end
```
- Apple event generic descriptor (list, record, etc.) and _id_

```objc
@interface NSAppleEventDescriptor (GenericObject)
  +(NSAppleEventDescriptor*)descriptorWithObject:(id)object;
  -(id)objectValue;
@end
```

Refer to [Appendix D: Scripting Support Categories](Appendix%20D-%20Scripting%20Support%20Categories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqobnknltc) for sample implementations of these categories.

To avoid initiating user interactions while handling Apple events sent by an automated workflow, make sure your application handling the events checks the user interaction level of events. You can do this within your scripting command handler by getting the current Apple event and its `keyInteractLevelAttr` attribute.

The value of the `keyInteractLevelAttr` attribute can be one of the following:

```
kAENeverInteract    = 0x00000010, /* server should not interact with user */
kAECanInteract      = 0x00000020, /* server may try to interact with user */
kAEAlwaysInteract   = 0x00000030, /* server should always interact with user where appropriate */
kAECanSwitchLayer   = 0x00000040, /* interaction may switch layer */
```

Consult _[NSAppleEventManager Class Reference](https://developer.apple.com/documentation/foundation/nsappleeventmanager)_ for details on getting the current Apple event.

[Next](Working%20with%20Custom%20Metadata.md)[Previous](Importing.md)


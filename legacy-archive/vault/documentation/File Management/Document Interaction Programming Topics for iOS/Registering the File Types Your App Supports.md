---
title: Document Interaction Programming Topics for iOS
apple_id: TP40010403
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/RegisteringtheFileTypesYourAppSupports.html
archived_at: '2026-07-15T07:31:54.694508Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Interaction Programming Topics for iOS](About%20Document%20Interaction.md)


[Next](Opening%20Supported%20File%20Types.md)[Previous](Previewing%20and%20Opening%20Files.md)

# Registering the File Types Your App Supports

If your app is capable of opening specific types of files, you should register that support with the system. This allows other apps, through the iOS document interaction technology, to offer the user the option to hand off those files to your app.

To declare its support for file types, your app must include the `CFBundleDocumentTypes` key in its `Info.plist` [property list file](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/InfoPlist.html#//apple_ref/doc/uid/TP40008195-CH61). (See [Core Foundation Keys](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html#//apple_ref/doc/uid/TP40009249).) The system adds this information to a registry that other apps can access through a document interaction controller.

The `CFBundleDocumentTypes` key contains an array of dictionaries, each of which identifies information about a specific document type. A document type usually has a one-to-one correspondence with a particular file type. However, if your app treats more than one file type the same way, you can group those file types together to be treated by your app as a single document type. For example, if you have an old and new file format for your application’s native document type, you could group both together in a single document type entry. This way, old and new files would appear to be the same document type and would be treated the same way.

Each dictionary in the `CFBundleDocumentTypes` array can include the following keys:

- `CFBundleTypeName` specifies the name of the document type.
- `CFBundleTypeIconFiles` is an array of filenames for the image resources to use as the document’s icon.
- `LSItemContentTypes` contains an array of strings with the [UTI types](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/UniformTypeIdentifier.html#//apple_ref/doc/uid/TP40008195-CH60) that represent the supported file types in this group.
- `LSHandlerRank` describes whether this application owns the document type or is merely able to open it. (For a list of values for `LSHandlerRank`, see [CFBundleDocumentTypes](../../General/Information%20Property%20List%20Key%20Reference/Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv).)

From your app’s perspective, a document is a file type (or file types) that the application supports and treats as a single entity. For example, an image processing application might treat different image file formats as different document types so that it can fine tune the behavior associated with each one. Conversely, a word processing application might not care about the underlying image formats and just manage all image formats using a single document type.

Listing 1 shows a sample XML snippet from the `Info.plist` of an app capable of opening a custom file type. The `LSItemContentTypes` key identifies the UTI associated with the file format and the `CFBundleTypeIconFiles` key points to the icon resources to use when displaying it.

__Listing 1__  Document type information for a custom file format

```
<dict>
   <key>CFBundleTypeName</key>
   <string>My File Format</string>
   <key>CFBundleTypeIconFiles</key>
       <array>
           <string>MySmallIcon.png</string>
           <string>MyLargeIcon.png</string>
       </array>
   <key>LSItemContentTypes</key>
       <array>
           <string>com.example.myformat</string>
       </array>
   <key>LSHandlerRank</key>
   <string>Owner</string>
</dict>
```

For more information about the contents of the `CFBundleDocumentTypes` key, see the description of that key in _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

[Next](Opening%20Supported%20File%20Types.md)[Previous](Previewing%20and%20Opening%20Files.md)


---
title: Document Interaction Programming Topics for iOS
apple_id: TP40010403
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/OpeningSupportedFileTypes.html
archived_at: '2026-07-15T07:31:54.678016Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Interaction Programming Topics for iOS](About%20Document%20Interaction.md)


[Next](Using%20the%20Quick%20Look%20Framework.md)[Previous](Registering%20the%20File%20Types%20Your%20App%20Supports.md)

# Opening Supported File Types

The system may ask your application to open a specific file and present it to the user. This typically occurs because another application encountered the file and used a document interaction controller to handle it. You receive information about the file to be opened in the [application:willFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623032-application) or [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method of your application delegate. If your application handles custom file types, you must implement this delegate method (instead of the `applicationDidFinishLaunching:` method) and use it to initialize your application.

The options [dictionary](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) passed to the `application:willFinishLaunchingWithOptions:` or `application:didFinishLaunchingWithOptions:` method contains information about the file to be opened. Specifically, your application should look in this dictionary for the following keys:

- [UIApplicationLaunchOptionsURLKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622996-url) contains an `NSURL` object that specifies the file to open.
- [UIApplicationLaunchOptionsSourceApplicationKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1623064-sourceapplication) contains an `NSString` with the bundle identifier of the application that initiated the open request.
- [UIApplicationLaunchOptionsAnnotationKey](https://developer.apple.com/documentation/uikit/uiapplicationlaunchoptionsannotationkey) contains a [property list object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44) that the source application wanted to associate with the file when it was opened.

If the [UIApplicationLaunchOptionsURLKey](https://developer.apple.com/documentation/uikit/uiapplication/launchoptionskey/1622996-url) key is present, your application must open the file referenced by that key and present its contents immediately. You can use the other keys in the dictionary to gather information about the circumstances surrounding the opening of the file.

[Next](Using%20the%20Quick%20Look%20Framework.md)[Previous](Registering%20the%20File%20Types%20Your%20App%20Supports.md)


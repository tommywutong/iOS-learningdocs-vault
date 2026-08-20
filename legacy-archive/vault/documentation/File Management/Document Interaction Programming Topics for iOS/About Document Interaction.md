---
title: Document Interaction Programming Topics for iOS
apple_id: TP40010403
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Introduction/Introduction.html
archived_at: '2026-07-15T07:31:54.710266Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Previewing%20and%20Opening%20Files.md)

# About Document Interaction

iOS provides technologies for displaying previews of files that your app doesn’t directly support. iOS also provides a systemwide registry of file type associations, allowing your app to handle the opening of files from other installed apps. These powerful technologies include the `UIDocumentInteractionController` class from the UIKit framework, described in _[UIDocumentInteractionController Class Reference](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller)_, and the Quick Look framework, described in _Quick Look Framework Reference for iOS_.

Starting in iOS 4.2, the Quick Look framework provides built-in printing support for many document types. If you want to provide customized printing and copying, you can add that support to a document interaction controller by implementing methods in its delegate.

For code that demonstrates use of the [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) and [QLPreviewController](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller) classes, view the _[DocInteraction](../../../samplecode/DocInteraction/DocInteraction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambvgi)_ sample code project.

Use a document interaction controller (an instance of the [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) class) to provide users with options for working with files that your application doesn’t directly support, such iWork documents, PDF files, image files, and so on. A document interaction controller can modally present a file preview, and can present a menu containing various options for using the file—such as for opening it in another application or printing the file using AirPrint.

If your app can open specific file types, you can register that capability in your Xcode project’s `Info.plist` file. When another application asks the system for help opening an item of those types, your application will be included in the options menu presented to the user.

The system may ask your app to open a specific file and present it to the user. This typically occurs because another app encountered a file of a type that you have registered to support. In this scenario, the system provides your app with a URL to the file and brings your app to the foreground.

To gain even more control over file previews, you can use the Quick Look framework directly. You can choose the style of animation to use when presenting a preview, and can preview a list of items as well as a single item. A Quick Look preview controller also provides built-in AirPrint printing of supported file types.

[Next](Previewing%20and%20Opening%20Files.md)


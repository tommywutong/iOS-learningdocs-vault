---
title: Document Interaction Programming Topics for iOS
apple_id: TP40010403
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/UsingtheQuickLookFramework.html
archived_at: '2026-07-15T07:31:54.702437Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Interaction Programming Topics for iOS](About%20Document%20Interaction.md)


[Next](Document%20Revision%20History.md)[Previous](Opening%20Supported%20File%20Types.md)

# Using the Quick Look Framework

To gain even more control over file previews, you can use the Quick Look framework directly. The framework’s primary class is [QLPreviewController](https://developer.apple.com/documentation/quicklook/qlpreviewcontroller). It relies on a [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) for responding to preview actions, and on a data source for providing the preview items.

In iOS 4.2 and later, the specialized view presented by a Quick Look preview controller includes an action button with a Print item. If the controller can provide a preview of a file, it can also print it. There is no printing code for you to write.

To display a Quick Look preview controller you can use any of these options:

- Push it into view using a [UINavigationController](https://developer.apple.com/documentation/uikit/uinavigationcontroller) object.
- Present it modally, full screen, using the [presentModalViewController:animated:](https://developer.apple.com/documentation/uikit/uiviewcontroller/1621465-presentmodalviewcontroller) method of its parent class, [UIViewController](https://developer.apple.com/documentation/uikit/uiviewcontroller).
- Present a document interaction controller (as described in [Previewing and Opening Files](Previewing%20and%20Opening%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimjqfvjvomi). The user can then invoke a Quick Look preview controller by choosing Quick Look from the document interaction controller’s options menu.

When presenting a Quick Look preview controller yourself, choose the display option that best fits the visual and navigation style of your application. Modal, full-screen display might work best if your app doesn’t use a navigation bar. If your app uses iPhone-style navigation, you might want to opt for pushing your preview into view.

A displayed preview includes a title taken from the last path component of the item URL. You can override this by implementing a [previewItemTitle](https://developer.apple.com/documentation/quicklook/qlpreviewitem/1419911-previewitemtitle)[accessor](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2) for the preview item.

A Quick Look preview controller can display previews for the following items:

- iWork documents
- Microsoft Office documents (Office ‘97 and newer)
- Rich Text Format (RTF) documents
- PDF files
- Images
- Text files whose uniform type identifier (UTI) conforms to the `public.text` type (see _[Uniform Type Identifiers Reference](../../Miscellaneous/Uniform%20Type%20Identifiers%20Reference/Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjx)_)
- Comma-separated value (csv) files

To use a Quick Look preview controller, you must provide a data source object using the methods described in _[QLPreviewControllerDataSource Protocol Reference](https://developer.apple.com/documentation/quicklook/qlpreviewcontrollerdatasource)_. The data source provides preview items to the controller and tells it how many items to include in a preview navigation list. If there is more than one item in the list, a modally-presented (that is, full-screen) controller displays navigation arrows to let the user switch among the items. For a Quick Look preview controller pushed using a navigation controller, you can provide buttons in the navigation bar for moving through the preview-item list.

For a complete description of the Quick Look framework, see _Quick Look Framework Reference for iOS_.

[Next](Document%20Revision%20History.md)[Previous](Opening%20Supported%20File%20Types.md)


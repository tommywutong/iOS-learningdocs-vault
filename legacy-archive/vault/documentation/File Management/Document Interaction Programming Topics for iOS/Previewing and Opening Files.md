---
title: Document Interaction Programming Topics for iOS
apple_id: TP40010403
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2010-11-15'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/DocumentInteraction_TopicsForIOS/Articles/PreviewingandOpeningItems.html
archived_at: '2026-07-15T07:31:54.685957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Document Interaction Programming Topics for iOS](About%20Document%20Interaction.md)


[Next](Registering%20the%20File%20Types%20Your%20App%20Supports.md)[Previous](About%20Document%20Interaction.md)

# Previewing and Opening Files

When your app needs to interact with files it cannot preview or open on its own, use a [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) object to manage those interactions. A document interaction controller works with the Quick Look framework to determine whether a file can be previewed in place, opened by another app, or both. Your app, in turn, works with the document interaction controller to present the available options to the user at appropriate times.

To use a document interaction controller, do the following:

1. [Create an instance](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) of the `UIDocumentInteractionController` class for each file you want to interact with.
2. Provide a representation of the file in your app’s user interface. (Typically, you would do this by displaying the file name or an icon)
3. When the user interacts with the file representation, such as by tapping it, ask the document interaction controller to present one of the following interfaces:

   - A file preview that displays the contents of the file.
   - A menu containing options to preview the file or open it using another app. You can add copying and printing options to this menu by implementing appropriate methods in the delegate of the document interaction controller.
   - A menu prompting the user only to open it using another app.

   A document interaction controller provides built-in gesture recognizers that makes implementing these actions straightforward.

Any app that interacts with files can use a document interaction controller. The most likely candidates to need these capabilities are apps that download files from the network. For example, an email app might use document interaction controllers to preview or open files attached to an email.

Document interaction controllers are also useful for some apps that do not download files. If your app supports file sharing, for example (see UI State Preservation and the _[DocInteraction](../../../samplecode/DocInteraction/DocInteraction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambvgi)_ sample code project), you can use a document interaction controller with a file that was synced to your app’s `Documents/Shared` directory.

To [create](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39) a new document interaction controller, [initialize](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) a [UIDocumentInteractionController](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller) instance with the file you want it to manage, and assign a [delegate object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14). The delegate is responsible for providing the controller with information it needs to present its views and, optionally, for performing additional actions when those views are displayed or the user interacts with them.

The following code creates a new document interaction controller and sets the delegate to the current object. Note that the caller of this method needs to [retain](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MemoryManagement.html#//apple_ref/doc/uid/TP40008195-CH27) the returned object.

```objc
- (UIDocumentInteractionController *) setupControllerWithURL: (NSURL) fileURL
    usingDelegate: (id <UIDocumentInteractionControllerDelegate>) interactionDelegate {

    UIDocumentInteractionController *interactionController =
        [UIDocumentInteractionController interactionControllerWithURL: fileURL];
    interactionController.delegate = interactionDelegate;

    return interactionController;
}
```

Once you have a document interaction controller, you can use its [properties](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) to get information about the associated file including its name, type, and URL. The controller also has an [icons](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616801-icons) property that contains [UIImage](https://developer.apple.com/documentation/uikit/uiimage) objects representing the document’s icon in various sizes. All this information can be useful when representing the file in your user interface.

If you plan to let the user open the file in another app, you can use the [annotation](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616820-annotation) property of the document interaction controller to pass custom information to the opening app. It is up to you to provide information in a format that the other app will recognize. For example, this property can be used by app in an application suite. When one app wants to communicate additional information about a file to other apps in the suite, it does so by way of the `annotation` property. The opening app sees the annotation data as the value associated with the [UIApplicationLaunchOptionsAnnotationKey](https://developer.apple.com/documentation/uikit/uiapplicationlaunchoptionsannotationkey) key of the options [dictionary](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) that is passed to it.

You can use a document interaction controller to display a file preview or to prompt the user to choose an action for a file.

- To modally display a file preview, call the [presentPreviewAnimated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616828-presentpreview) method.
- To prompt the user with a set of options, including an option to open the file in another app, call the [presentOptionsMenuFromRect:inView:animated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616814-presentoptionsmenu) or [presentOptionsMenuFromBarButtonItem:animated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616811-presentoptionsmenufrombarbuttoni) method.
- To prompt the user only to open the file in another app, call the [presentOpenInMenuFromRect:inView:animated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616807-presentopeninmenufromrect) or [presentOpenInMenuFromBarButtonItem:animated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616827-presentopeninmenufrombarbuttonit) method.

Each of these methods attempts to display a view—either a document preview or a menu. When calling any of these methods, check the return value. A return value of `NO` indicates that the requested view would have contained no content, and so is not displayed. For example, the `presentOpenInMenuFromRect:inView:animated:` method returns `NO` if there are no installed apps capable of opening the file.

If you call a method to display a file preview, your delegate object must implement the [documentInteractionControllerViewControllerForPreview:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontrollerdelegate/1616799-documentinteractioncontrollervie) method. Previews are displayed modally, so the [view controller](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ControllerObject.html#//apple_ref/doc/uid/TP40008195-CH11) that you return from this method becomes the parent for the preview. If you do not implement this method, if your implementation returns `nil`, or if the view controller that your implementation returns is unable to present another modal view controller, the document preview is not displayed.

A document interaction controller automatically handles the dismissal of the view it presents. However, you can dismiss the view programmatically as needed by calling the [dismissMenuAnimated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616816-dismissmenu) or [dismissPreviewAnimated:](https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/1616815-dismisspreview) methods.

For sample code that demonstrates how to present a document interaction controller using gesture recognizers, view the _[DocInteraction](../../../samplecode/DocInteraction/DocInteraction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytambvgi)_ sample code project.

[Next](Registering%20the%20File%20Types%20Your%20App%20Supports.md)[Previous](About%20Document%20Interaction.md)


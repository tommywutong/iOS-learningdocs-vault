---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printlayoutpanel/osxp_printlayoutpanel.html
archived_at: '2026-07-15T07:17:46.686644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](Document%20Revision%20History.md)[Previous](Managing%20Print%20Information%20Objects.md)

# Managing Page Layout Objects

An `NSPageLayout` object creates a panel that queries the user for information such as paper size and orientation. This information is stored in an `NSPrintInfo` object which is used when printing.

When the user chooses the Page Setup menu command from the File menu, the `runPageLayout:` the system sends the message up the responder chain and creates an `NSPageLayout` object. Either an `NSApplication` or an `NSDocument` object receives the message. Upon receipt, the Page Layout user interface is displayed to the user. An `NSApplication` object displays the page layout user interface as a modal panel, whereas an `NSDocument` object displays the page layout user interface as a sheet. The message handling and display is done automatically by the system with no code needed by your app.

If the default implementation is not sufficient you can handle the Page Setup panel yourself. You create an `NSPageLayout` object by invoking the `pageLayout` method. To display the Page Setup user interface app-modally, use the `runModal` or `runModalWithPrintInfo:` methods. To display the Page Setup user interface document-modally as a sheet, use the `beginSheetWithPrintInfo:modalForWindow:delegate:didEndSelector:contextInfo:` method.

You rarely need to subclass `NSPageLayout` because you can augment its display by adding your own accessory view using the `addAccessoryController:` method. Place controls for setting app-specific print settings in your accessory view.

The accessory view is displayed when the user chooses the appropriate entry—which is the name of your app—in the Settings pop-up menu in the Page Setup panel. The panel automatically resizes in the vertical direction to accommodate the height of the view you add. You must make sure the width of your accessory view fits with the maximum width of the Page Setup panel. If possible, you should make your accessory view the same size as the standard views in the panel.

When running an app that is not document based, you must override the `runPageLayout:` method of the `NSApplication` class. You can also implement the method earlier in the responder chain. If you want to add an accessory view, your `runPageLayout:` method needs to call the [addAccessoryController:](https://developer.apple.com/documentation/appkit/nspagelayout/1397790-addaccessorycontroller) method.

When running a document-based app, the `NSDocument` class default implementation of `runPageLayout:` creates the page layout panel and then passes the object to its `preparePageLayout:` method. Override the `preparePageLayout:` method to add an accessory view. `NSDocument` then runs the panel as a sheet attached to its window.

The `NSDocument` class implements the `runPageLayout:` method to handle the Page Setup menu command instead of letting `NSApplication` handle it. When the document receives this message, it gets the document’s `NSPrintInfo` object and invokes the method `runModalPageLayoutWithPrintInfo:delegate:didRunSelector:contextInfo:` to display the Page Setup panel. To give your `NSDocument` subclass an opportunity to customize the `NSPageLayout` object, the printing system passes the `NSPageSetup` object to `preparePageLayout:` before displaying the panel. Override this method if you want to add an accessory view to the panel.

When the panel is dismissed with the OK button, `NSDocument` checks the return value of its `shouldChangePrintInfo:` method. If it returns `YES`(the default) the printing system updates the `NSPrintInfo` object to reflect the new print settings. You can override this method to validate the new settings and return `NO` if the new settings should be discarded.

[Next](Document%20Revision%20History.md)[Previous](Managing%20Print%20Information%20Objects.md)


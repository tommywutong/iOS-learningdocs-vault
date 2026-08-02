---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printingapi/osxp_printingapi.html
archived_at: '2026-07-15T07:17:46.364443Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](Printing%20From%20Your%20App.md)[Previous](Printing%20System%20Workflow%20and%20User%20Interface.md)

# The AppKit Printing API

The AppKit framework publishes the programmatic interface that supports printing in your app. The API includes five classes and one formal protocol. Objects of these classes and the delegate implementing the protocol have the runtime relationships shown in Figure 2-1.

__Figure 2-1__  The classes and protocol in the AppKit printing API

!

These classes are in a layer above Core Printing, which is a C API used to create command-line tools or to perform printing tasks that don’t display a user interface. The `NSPrintInfo` class provides direct access to Core Printing functionality. In Cocoa apps, Core Printing can be used to extend the functionality of the AppKit printing classes. However most apps shouldn’t need to use the Core Printing API, so it is not discussed further in this document. If you want to find out more about Core Printing, see the sample code project _[Cocoa Printing using Core Printing](../../../samplecode/Cocoa%20Printing%20using%20Core%20Printing/Cocoa%20Printing%20using%20Core%20Printing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojvha)_ and the technical note _[Using Cocoa and Core Printing Together](https://developer.apple.com/library/archive/technotes/tn2248/_index.html#//apple_ref/doc/uid/DTS40008838)_.

Objects of the AppKit printing classes have specific roles and responsibilities.

An `NSPrintOperation` object is central to printing; without it, your app can’t print. It displays the Print panel, optionally spawns a new thread to process the print job, sets up the print environment, and tells the `NSView` to print itself, and hands off the resulting content to the CUPS layer of the system. It can also generate Portable Document Format (PDF) data instead of sending the results to a printer.

`NSPrintOperation` works together with two other objects: an `NSPrintInfo` object, which specifies how the code should be generated, and an `NSView` object, which performs the actual code generation. You must specify a view when you create an `NSPrintOperation` object. You can optionally specify an `NSPrintInfo` object.

Print information includes the paper size, number of copies, print margins, whether to use a header and footer, and so on. The printing system automatically creates a shared `NSPrintInfo` object that holds defaults settings used by other objects of the printing system.

Normally you don’t set `NSPrintInfo` attributes directly—this is done by instances of `NSPageLayout` and `NSPrintPanel`. The `NSView` that generates the printing content might also supersede some `NSPrintInfo` settings, such as the pagination and orientation attributes.

Your app should not create an `NSPrintInfo` object unless it needs to modify the default settings or save and restore custom settings. See [Managing Print Information Objects](Managing%20Print%20Information%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dilkciffeershivca).

This class manages the standard system Print panel. Your app does not need to create an `NSPrintPanel` object unless you want to manage the printing workflow yourself or add custom print settings for your app (using an accessory view). If you create an instance of `NSPrintPanel` you need to display it and subsequently initiate the desired printing behavior.

If you add an accessory view to the Print panel to display app-specific options, you must adopt the `NSPrintPanelAccessorizing` protocol. See [Managing and Extending the Print Panel](Managing%20and%20Extending%20the%20Print%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3delkciffeershivca).

The `NSPrintPanelAccessorizing` protocol declares two methods that the `NSPrintPanel` class uses to get information from a printing accessory controller. You are required to implement the [localizedSummaryItems](https://developer.apple.com/documentation/appkit/nsprintpanelaccessorizing/1490521-localizedsummaryitems) method, which returns an array of dictionaries that contain the localized summary strings for the setting in your accessory view. It is optional for you to implement [keyPathsForValuesAffectingPreview](https://developer.apple.com/documentation/appkit/nsprintpanelaccessorizing/1490516-keypathsforvaluesaffectingprevie).

See [Managing and Extending the Print Panel](Managing%20and%20Extending%20the%20Print%20Panel.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3delkciffeershivca).

This class manages the standard system Page Setup panel. Your app does not need to create an `NSPageLayout` object unless you want to manage the printing workflow yourself. If your app really needs to mange the Page Setup panel, it must display the Page Setup panel and subsequently initiate the desired printing behavior.

It is not typical for apps to create `NSPageLayout` objects. See [Managing Page Layout Objects](Managing%20Page%20Layout%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dglkciffeershivca).

As with screen-based drawing, the [NSView](https://developer.apple.com/documentation/appkit/nsview) class provides the underlying canvas for drawing printed content. If you have an app that already uses views to draw in your app’s windows—which most Cocoa apps do—then you already have the basic code you need to draw printed content. By default, the printing workflows handle printing by taking the same views embedded in your windows and simply redirecting the output to a different destination.

In addition to drawing your custom content, the `NSView` class has methods for:

- Drawing header and footer content
- Paginating content
- Specifying alignment marks or virtual sheet borders on each logical page
- Specifying drawing crop marks or fold lines on each printed sheet

For more information on drawing content to `NSView` objects, see _[Cocoa Drawing Guide](../Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_.

If your app supports printing text, you also need to be familiar with using the Cocoa Text System (see _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_). If you want to control text layout on the page, you need to use the [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) class (see _[Text Layout Programming Guide](../Text%20Layout%20Programming%20Guide/Introduction%20to%20Text%20Layout%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge2tq2i)_).

In a Cocoa app, printing is generally initiated by the user choosing the Print menu command, which usually sends either a `print:` or `printDocument:` message up the responder chain. Which message is sent depends on whether or not the app is document-based. The app receives the message either in a custom `NSView` object (if it has the keyboard focus), a window delegate, or an `NSDocument` object.

After receiving the message to print, the general workflow is as follows:

1. Create an `NSPrintOperation` object to manage the print job, providing the view that contains the content to print.
2. (Optional) Add an accessory view to the job’s print panel.
3. Run the print operation.
4. (Optional) For a multipage job, override how the view is divided between multiple pages by using the methods of the `NSView` class.

The view’s `drawRect:` method draws the view’s contents.

Implementing printing in your app can be as easy as writing these few lines of code:

```objc
- (IBAction)print:(id)sender {
      NSPrintOperation *op;
      op = [NSPrintOperation printOperationWithView:self];
      if (op)
           [op runOperation];
      else
          // handle error here
}
```

OS X printing also provides support for custom formatting and layout. When you add those tasks, the workflow is a bit more complex, but straightforward. See [Printing From Your App](Printing%20From%20Your%20App.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha3dclkciffeershivca) and [Laying Out Page Content](Laying%20Out%20Page%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tclkcijbuqscbjbeq).

[Next](Printing%20From%20Your%20App.md)[Previous](Printing%20System%20Workflow%20and%20User%20Interface.md)


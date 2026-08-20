---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_printapps/osxp_printapps.html
archived_at: '2026-07-15T07:17:46.349107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](Laying%20Out%20Page%20Content.md)[Previous](The%20AppKit%20Printing%20API.md)

# Printing From Your App

An `NSPrintOperation` object controls the process that creates a print job. Print jobs are normally sent to a printer, but they can also be used to generate Portable Document Format (PDF) data for your app. An `NSPrintOperation` object controls the overall process, relying on an `NSView` object to generate the actual code. Once created, a print operation can be configured in several ways.

In a Cocoa App, there are two classes that provide infrastructure to handle printing:

- `NSView`
- `NSDocument`

The methods your app uses to handle printing depend on which class it uses for its content.

Printing in apps that are not document-based works best for apps that have only one printable view (that is, an `NSView` object) in its main window that can be the first responder. For example, in a simple text editor, only the view holding the text document can have focus, so it is straightforward to implement printing in the text view. You can see an example of this architecture in the _[TextEdit](../../../samplecode/TextEdit/TextEdit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytcnzuge)_ sample code project.

When your user interface contains multiple views that can have focus, such as multiple `NSTextField` objects, view-based printing doesn’t work well. When the user chooses the Print command, the view that receives the `print:` message prints itself, but nothing else. If the focus is in a text field, for example, only the contents of that text field are printed. This probably is not the desired behavior. Instead, your app needs to take a more document-based approach. See [Printing in an App That Uses NSDocument](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2teljrge4tcmjx).

In a view-based app, your app receives a `print:` message when the user chooses Print from the File menu. In your implementation of the `print:` method, you create an `NSPrintOperation` object initialized with the view to print and, optionally, the `NSPrintInfo` object holding the print settings.

The print operation is not started, until you invoke one of the `runOperation` methods of `NSPrintOperation` as shown in Listing 3-1.

__Listing 3-1__  A simple implementation of the print: method for a view-based app

```objc
- (void)print:(id)sender {
    [[NSPrintOperation printOperationWithView:self] runOperation];
}
```

This implementation of `print:` starts by creating an `NSPrintOperation` object, which manages the process of generating proper code for a printer device. When run, the `NSPrintOperation` object creates and displays a Print panel (which is an `NSPrintPanel` object created automatically by the printing system) to obtain the print settings from the user. The app’s shared `NSPrintInfo` object is used for the initial settings.

An app that uses the `NSDocument` class to manage its documents gains additional infrastructure to handle document printing. Because print settings may be different for different documents, each instance of `NSDocument` has its own `NSPrintInfo` object, which is accessed with the `printInfo` and `setPrintInfo:` methods.

In a document-based app, when the user chooses Print from the File menu, the printing system sends a `printDocument:` message, which only the `NSDocument` class implements. The `NSDocument` object associated with the app’s main window receives the message and invokes the method [printDocumentWithSettings:showPrintPanel:delegate:didPrintSelector:contextInfo:](https://developer.apple.com/documentation/appkit/nsdocument/1515058-printdocumentwithsettings) with `YES` as the argument for `showPrintPanel`.

If you specify to show the Print panel, the method presents it and prints only if the user approves the panel. The method adds the `NSPrintInfo` attributes, from the `printSettings` dictionary you pass, to a copy of the document's print info, and the resulting print info settings are used for the operation. When printing is complete or canceled, the method sends the message selected by `didPrintSelector` to the delegate, with the `contextInfo` as the last argument. The method selected by `didPrintSelector` must have the same signature as:

```objc
- (void)document:(NSDocument *)document didPrint:(BOOL)didPrintSuccessfully  contextInfo: (void *)contextInfo;
```

The default implementation of [printDocumentWithSettings:showPrintPanel:delegate:didPrintSelector:contextInfo:](https://developer.apple.com/documentation/appkit/nsdocument/1515058-printdocumentwithsettings) invokes [printOperationWithSettings:error:](https://developer.apple.com/documentation/appkit/nsdocument/1515070-printoperationwithsettings). You must override this method to enable printing in your app; the default implementation raises an exception.

If the [printDocumentWithSettings:showPrintPanel:delegate:didPrintSelector:contextInfo:](https://developer.apple.com/documentation/appkit/nsdocument/1515058-printdocumentwithsettings) returns `nil`, it presents the error to the user before messaging the delegate. Otherwise it invokes this line of code:

```
[thePrintOperation setShowsPrintPanel:showPrintPanel];
```

followed by this code:

```
[self runModalPrintOperation:thePrintOperation
                    delegate:delegate
              didRunSelector:didPrintSelector
                 contextInfo:contextInfo];
```


In some cases it might be preferable for your app to send content to the printer that is not identical to that drawn onscreen. For example, the main window of a database app might contain an interface for browsing and editing the database, while the printed data needs to be formatted as a table. In this case, the document needs separate views for drawing in a window and for printing to a printer. If you have a good Model-View-Controller design, you can easily create a custom view that can draw the printer-specific version of your data model and use it when creating the print operation

You have two options for customizing content for the printed page:

1. In your app’s drawRect: method, branch the code as shown here:

```objc
- (void)drawRect:(NSRect)r {
    if ( [NSGraphicsContext currentContextDrawingToScreen] ) {
        // Draw screen-only elements here
    } else {
        // Draw printer-only elements here
    }
    // Draw common elements here
}
```
2. Create a view that’s used only for printing.

When printing to a view object that your app uses only for printing you need to:

- Create a view that will be used only for printing, making sure you size it appropriately.
- Create a print operation using the print view.

```
NSPrintOperation *printOp = [NSPrintOperation printOperationWithView:myPrintingView
                          printInfo:[self printInfo]];
```
- Ideally, also specify that the print operation can run in a separate thread. This causes the print progress panel to appear as a sheet on the document window.

```
[printOp setCanSpawnSeparateThread:YES];
```

You might also need to adjust your drawing based on an attribute in the print operation’s `NSPrintInfo` object. You can get the current print operation with the `NSPrintOperation` class method `currentOperation` and then get its `NSPrintInfo` object from the `printInfo` method.

```
NSPrintOperation *op = [NSPrintOperation currentOperation];
NSPrintInfo *pInfo = [op printInfo];
```


A print operation does not have to send its results to a printer. You can have the operation generate PDF data and write the data either to an `NSMutableData` object you provide or to a file at a path you specify. To do so, use the `PDFOperation` class method to create the `NSPrintOperation` object instead of one of the `printOperation` methods. You can identify whether a print operation is generating PDF data by sending it an `isCopyingOperation` message, which returns `YES` in this case; it returns `NO` if the data are being sent to a printer.

The `NSView` class provides several convenience methods for generating PDF data. The data can be returned in an `NSData` object or written to a pasteboard. The `NSView` class implements `dataWithPDFInsideRect:` and `writePDFInsideRect:toPasteboard:`.

These methods create and run an `NSPrintOperation` object, just as the `print:` method does, but the print panel is not displayed. They still use the shared `NSPrintInfo` object if one is provided, but do not allow the user to modify the defaults.

By default, the print operation performs the data generation on the current thread. This thread is normally the app’s main thread, or the thread that processes user events. You can tell the print operation to instead spawn a new thread and generate the print job on it, using the `setCanSpawnSeparateThread:` method. This allows your app to continue processing events, instead of blocking. (Print operations that create PDF data always run on the current thread.)

[Next](Laying%20Out%20Page%20Content.md)[Previous](The%20AppKit%20Printing%20API.md)


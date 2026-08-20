---
title: Application Architecture Overview
apple_id: 10000005i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2011-06-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppArchitecture/Tasks/GracefulAppTermination.html
archived_at: '2026-07-15T05:25:31.395841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application Architecture Overview](Introduction%20to%20Application%20Architecture.md)


[Next](Document%20Revision%20History.md)[Previous](Undo%20and%20Redo.md)

# Graceful Application Termination

When a user quits an application (by choosing the Quit command or pressing Command–Q) or when a user logs out, restarts, or shuts down the system, an application should do whatever is necessary to terminate itself gracefully. It should ensure that all data associated with the application and its documents is properly saved, all state (such as user preferences) is stored, and that all necessary clean-up takes place. What graceful termination entails depends on the type of application. For example, an application with multiple documents to save must do a lot more than a simple document-less application that needs only to free allocated resources.

In Cocoa, all raw events requiring application termination result in the invocation of the `NSApplication` delegation method `applicationShouldTerminate:`. If the delegate does not implement this method, the application is terminated regardless of any unsaved documents. Moreover, quitting, logging out, restarting, or shutting down does _not_ automatically lead to the invocation of the `NSWindow` delegation method `windowShouldClose:` in any of the application’s windows. This method is immediately invoked when users click the close box or choose the Close command. It is typically the place the window’s (NSWindow) delegate displays a sheet asking users if they want to save any data associated with the window. To gracefully terminate your application (assuming it has data to save) you must ensure that `windowShouldClose:` is invoked for each of your windows, or that the behavior commonly implemented in this method occurs elsewhere in your application.

An application that gracefully terminates can be one of several kinds:

- multi-document applications based on Cocoa’s document architecture
- multi-document applications not based on the document architecture
- single-document applications
- applications that need to save state and do any clean-up tasks not handled by the application itself

The procedure differs for each of these kinds of application. The following discussion focuses primarily on the second type of application— multi-document applications that are not based on the document architecture—because the procedure is most comprehensive. The code examples used to illustrate the procedure come from the Text Edit example application located at `/Developer/Examples/AppKit/TextEdit/`.

If your multi-document application uses Cocoa’s document architecture—that is, the constellation of `NSDocument`, `NSWindowController`, and `NSDocumentController` objects, along with their delegates—the good news is that you have to do absolutely nothing to effect a graceful termination of the application. This “free” behavior is implemented largely in `NSDocumentController`.

In case you don’t use the default `NSDocumentController` object, or want to create a subclass of it, you may need to know more about how the `NSDocumentController` class gracefully terminates execution; here is a summary:

1. In `applicationShouldTerminate:`, if there are multiple unsaved documents, `NSDocumentController` calls a method with an impossibly long name: `reviewUnsavedDocumentsWithAlertTitle:cancellable:delegate:didReviewAllSelector:contextInfo:`. This method displays an alert dialog containing buttons for reviewing unsaved documents, quitting despite unsaved documents, and canceling the impending save operation.
2. If the user chooses to cancel, `NSDocumentController` simply returns `NSTerminateCancel`.
3. If the user chooses to quit without saving or if there are no documents to save, the method identified by the `didReviewAllSelector` selector is invoked with a parameter of `YES`, allowing the specified delegate to do whatever is necessary before terminating.
4. If the user chooses to review unsaved documents, `NSDocumentController` calls `closeAllDocumentsWithDelegate:didCloseAllSelector:contextInfo:`. This method simply displays a sheet, in order, for each of the windows with unsaved document data.

For more information on Cocoa’s document architecture, see the programming topic _Document-Based Applications Overview_.

A multi-document application that is not based on Cocoa’s document architecture has to do much more of the termination work itself. This work is similar to what `NSDocumentController` does, as described in [Applications Based on the Document Architecture](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4daljrgaydcobugi). In summary, the steps are the following:

1. The application delegate should implement `applicationShouldTerminate:` to handle any request to quit the application or log out, restart, or shut down the system.
2. In `applicationShouldTerminate:` the delegate should get an array of the application’s windows and determine if any associated documents have unsaved data.
3. If there are unsaved documents, the delegate displays an alert dialog asking the user if he or she wants to save the documents before quitting, discard any changes (and quit), or cancel the operation.

   Of course, if there are no unsaved documents, the delegate should return `NSTerminateNow`, which tells the application object to proceed with termination (closing all windows, and so on).
4. If users want to review changes and save document data, the application delegate should, in `applicationShouldTerminate:`, initiate the window-save procedure and return `NSTerminateLater`. Otherwise, it should return `NSTerminateNow` or `NSTerminateCancel`, as appropriate.
5. In a window-save routine, each window with unsaved data should display a sheet asking users if they wish to save the document, close the window without saving, or cancel the operation. Each window should display its sheet in an orderly sequence, not all at once, and should respond appropriately to the user’s choice.

   Because the goals are the same (saving document data), the code used for this purpose can be the same code that is executed when the user closes the window (typically invoked by the window’s delegate in `windowShouldClose:`).
6. After all document data has been saved (or when users choose “close without saving”), send `replyToApplicationShouldTerminate:` to the application object (`NSApp`) with an argument of `YES`.

   If the user is logging out, or is restarting or shutting down the system, You need to send `replyToApplicationShouldTerminate:` within two minutes after returning `NSTerminateLater` in `applicationShouldTerminate:` or the procedure will time out.
7. When the application object gets the go-ahead for termination, it closes any open window (among other things). This results in the invocation of the `NSWindow` delegation method `windowWillClose:` in which the delegate can perform any necessary tasks (clean-up, for example) related to the window.
8. Just before the application ceases execution, the application delegate method `applicationWillTerminate:` is invoked; here the delegate can perform any tasks related to the application itself, such as writing out application preferences.

The following section, An Example: Text Edit, illustrates the procedure outlined above and points out details of implementation.

When you install the Developer package for Mac OS X, the Text Edit application, which is included in a standard user installation of Mac OS X, is also included as an example Cocoa Application project (`/Developer/Examples/AppKit/TextEdit/`). Even though Text Edit is a multi-document application it does not (currently, at least) make use of the document architecture. Given this, how it handles graceful application termination is instructive.

Listing 1 shows how Text Edit’s application delegate—which is its application controller object (`Controller.m`)—implements `applicationShouldTerminate:`.

__Listing 1__  Implementing applicationShouldTerminate:

```objc
- (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)app {
    NSArray *windows = [app windows];
    unsigned count = [windows count];
    unsigned needsSaving = 0;

    // Determine if there are any unsaved documents...
    while (count--) {
        NSWindow *window = [windows objectAtIndex:count];
        Document *document = [Document documentForWindow:window];
        if (document && [document isDocumentEdited]) needsSaving++;
    }
    if (needsSaving > 0) {
        int choice = NSAlertDefaultReturn;  // Meaning, review changes
    if (needsSaving > 1) { // If we only have 1 unsaved document,
                          // we skip the "review changes?" panel
            NSString *title = [NSString stringWithFormat:
                NSLocalizedString(@"You have %d documents with unsaved
                changes. Do you want to review these changes before
                quitting?", @"Title of alert panel which comes up when user
                chooses Quit and there are multiple unsaved documents."),
                needsSaving];
        choice = NSRunAlertPanel(title,
            NSLocalizedString(@"If you don't review your documents, all
                changes will be lost.", @"Warning in the alert panel which
                comes up when user chooses Quit and there are unsaved
                documents."),
            NSLocalizedString(@"Review Changes...", @"Choice (on a button)
                given to user which allows him/her to review all unsaved
                documents if he/she quits the application without saving
                them all first."),
            NSLocalizedString(@"Discard Changes", @"Choice (on a button)
                given to user which allows him/her to quit the application
                even though there are unsaved documents."),
            NSLocalizedString(@"Cancel", @"Button choice allowing user to
                cancel."));
            if (choice == NSAlertOtherReturn) return NSTerminateCancel; /* Cancel */
        }
        if (choice == NSAlertDefaultReturn) { /* Review unsaved; Quit Anyway falls through */
            [Document reviewChangesAndQuitEnumeration:YES];
            return NSTerminateLater;
        }
    }
    return NSTerminateNow;
}
```

In this method, the delegate obtains the application object’s array of windows and queries the document associated with each for its edited (or “dirty”) status. If there are no dirty documents, it returns `NSTerminateNow`. If there are multiple dirty documents, it displays a dialog asking the user if he or she wants to review changes, discard changes, or cancel the operation. Based on the user’s response, the delegate returns an appropriate constant: `NSTerminateLater`, `NSTerminateNow`, or `NSTerminateCancel`. If the user wants to review the windows and their documents, or if there is only one window with a dirty document, the delegate sends the `reviewChangesAndQuitEnumeration:` message to the Document class before returning the `NSTerminateLater` constant.

The `reviewChangesAndQuitEnumeration:` cycles through the applications windows and, for each window with unsaved document data, it calls `askToSave:` to have the window’s “do you want to save?” sheet displayed. What’s important is that it does this in a controlled sequence (instead of having all windows with their alert sheets displayed at the same time). Listing 2 illustrates how Text Edit (in its Document class) implements this class method.

__Listing 2__  Recursively reviewing document changes

```objc
+ (void)reviewChangesAndQuitEnumeration:(BOOL)cont {
    if (cont) {
        NSArray *windows = [NSApp windows];
        unsigned count = [windows count];
        while (count--) {
            NSWindow *window = [windows objectAtIndex:count];
            Document *document = [Document documentForWindow:window];
            if (document) {
                if ([document isDocumentEdited]) {
                    [document askToSave:@selector(reviewChangesAndQuitEnumeration:)];
                    return;
                }
            }
        }
    }
    [NSApp replyToApplicationShouldTerminate:cont];
}
```

Text Edit accomplishes the orderly sequencing of window alert sheets by having `reviewChangesAndQuitEnumeration:` invoked recursively (as will be shown). The flag passed into the method (_cont_), if `NO`, signals that the user has canceled the termination; if `YES`, the method processes the next unsaved document. When there are no more documents to review, or if _cont_ is `NO`, `replyToApplicationShouldTerminate:` is sent to the application object with the appropriate flag.

The value passed into `askToSave:` is a selector, in this case identifying the `reviewChangesAndQuitEnumeration:` method. As shown in Listing 3, Text Edit simply implements `askToSave:` to make the current document window visible and key and call the `NSBeginAlertSheet` function, which displays the alert sheet asking if the user wants to save the document before closing the window. Note that it passes the selector into this function as the context-information parameter.

__Listing 3__  Displaying and handling a sheet for saving a document

```objc
- (void)askToSave:(SEL)callback {
    [[self window] makeKeyAndOrderFront:nil];
    NSBeginAlertSheet(NSLocalizedString(@"Do you want to save changes
        to this document before closing?", @"Title in the alert panel when
        the user tries to close a window containing an unsaved document."),
        NSLocalizedString(@"Save",
        @"Button choice which allows the user to save the document."),
        NSLocalizedString(@"Don't Save",
        @"Button choice which allows the user to abort the save of a
        document which is being closed."),
        NSLocalizedString(@"Cancel",
        @"Button choice allowing user to cancel."),
         [self window], self,
        @selector(willEndCloseSheet:returnCode:contextInfo:),
        @selector(didEndCloseSheet:returnCode:contextInfo:),
        (void *)callback,
        NSLocalizedString(@"If you don't save, your changes will be lost.",
        @"Subtitle in the alert panel when the user tries to close a
        window containing an unsaved document."));
}
```

The Cocoa API for sheets specifies two callback methods that are potentially invoked in the modal delegate as a result of the `NSBeginAlertSheet` call. The first, called the did-end method, is invoked after the user clicks a button in the alert sheet but before the sheet is dismissed; the second, called the did-dismiss method, is invoked after the sheet is dismissed. The function parameters identifying them are selectors. The methods must conform to a certain signature. (See the programming topic _[Sheet Programming Topics](../Sheet%20Programming%20Topics/Introduction%20to%20Sheets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgayde2i)_ for further information.)

The `askToSave:` implementation makes use of both callback methods. For the _contextInfo_ parameter of `NSBeginAlertSheet` it passes the selector passed it, which in this case identifies the class method `reviewChangesAndQuitEnumeration:`. Then, for the modal delegate (`self`), it implements (as shown in Listing 4) the did-end callback method `willEndCloseSheet:returnCode:contextInfo:` and the did-dismiss method `didEndCloseSheet:returnCode:contextInfo:`.

__Listing 4__  Callback methods for NSBeginAlertSheet

```objc
- (void)willEndCloseSheet:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {
    if (returnCode == NSAlertAlternateReturn) {     /* "Don't Save" */
        [[self window] close];
        if (contextInfo) ((void (*)(id, SEL, BOOL))objc_msgSend)([self class], (SEL)contextInfo, YES);         // Send callback (YES means continue save
    }
}

- (void)didEndCloseSheet:(NSWindow *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {
    if (returnCode == NSAlertDefaultReturn) {       /* "Save" */
        [self saveDocument:NO rememberName:YES shouldClose:YES whenDone:(SEL)contextInfo];
    } else if (returnCode == NSAlertOtherReturn) {  /* "Cancel" */
        if (contextInfo) ((void (*)(id, SEL, BOOL))objc_msgSend)([self class], (SEL)contextInfo, NO);          // Send callback indicating save cancel
    }
}
```

Text Edit implements the `willEndCloseSheet:returnCode:contextInfo:` method for the case where the user want to close the window regardless of unsaved data. In this case, it wants the preferred user experience of the window closing before the sheet slides back up “under” the title bar. Note what this callback method does after it closes the window. Using the Objective-C runtime function `objc_msgSend`, `willEndCloseSheet:returnCode:contextInfo:` sends the message identified by the passed-in selector, `reviewChangesAndQuitEnumeration:`, to the Document class with a parameter of `YES`, thus causing the display of the next window’s alert sheet.

The `didEndCloseSheet:returnCode:contextInfo:` handles the remaining button-identifying constants potentially sent by the `NSBeginAlertSheet` function. If the user clicks the button to save the window’s document, it invokes a method that not only saves the document (displaying the save browser, if necessary), but afterwards closes the window and calls `reviewChangesAndQuitEnumeration:` with a parameter of `YES`. (This detail is not shown.) If the user wants to cancel the termination operation, `didEndCloseSheet:returnCode:contextInfo:` uses the `objc_msgSend` function to send `reviewChangesAndQuitEnumeration:` to the Document class, this time with a parameter of `NO`.

Text Edit ties in the relevant portions of its application-termination code with the code that is invoked when users explicitly close a window. The delegate for a document window implements `windowShouldClose:` in a way that results in the invocation of `askToSave:` if the document has unsaved data. This time `NULL` is passed instead of a selector, so `reviewChangesAndQuitEnumeration:` is invoked only once. Listing 5 illustrates how Text Edit does this.

__Listing 5__  Handling the explicit closing of a window

```objc
- (BOOL)windowShouldClose:(id)sender {
    return [self canCloseDocument];
}

- (BOOL)canCloseDocument {
    if (isDocumentEdited) {
        [self askToSave:NULL];
        return NO;
    }
    return YES;
}
```


In terminating your application gracefully, there is really not much you typically need to do after saving document data. The objects that comprise an application generally take care of freeing used objects and allocated resources. There are a couple exceptions to this. One is to make sure that objects such as windows with external references have those references removed. One such case is a delegate. In Text Edit’s `windowWillClose:` method (which is invoked right after `windowShouldClose:`), the delegate of the window removes itself as a reference on the window (Listing 6).

__Listing 6__  Removing a reference in windowWillClose:

```objc
- (void)windowWillClose:(NSNotification *)notification {
    NSWindow *window = [self window];
    [window setDelegate:nil];
    [self release];
}
```

Another case where final tidying up might be necessary is when you need to save persistent data. User preferences are one such case, and `applicationWillTerminate:` is an ideal place to save them. Listing 7 illustrates how Text Edit makes use of `applicationWillTerminate:`.

__Listing 7__  Saving user preferences in applicationWillTerminate:

```objc
- (void)applicationWillTerminate:(NSNotification *)notification {
    [Preferences saveDefaults];
}
```

[Next](Document%20Revision%20History.md)[Previous](Undo%20and%20Redo.md)


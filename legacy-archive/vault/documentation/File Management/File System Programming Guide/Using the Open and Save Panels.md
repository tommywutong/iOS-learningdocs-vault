---
title: File System Programming Guide
apple_id: TP40010672
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/FileSystemProgrammingGuide/UsingtheOpenandSavePanels/UsingtheOpenandSavePanels.html
archived_at: '2026-07-15T07:32:00.432229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [File System Programming Guide](About%20Files%20and%20Directories.md)


[Next](Managing%20Files%20and%20Directories.md)[Previous](iCloud%20File%20Management.md)

# Using the Open and Save Panels

When working with user documents and files in macOS, the user should decide where those files reside in the file system. The standard Open and Save panels provide you with an interface to use whenever you interact with the user’s files. You present the Open panel when you want the user to select one or more existing files or directories. Present the Save panel when you have a new user document that you need to write to disk.

You use the [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) class when you want to prompt the user to select one or more files or directories. Exactly how you use this class depends on what you plan to do with the selected items:

- To open a document in a new window, present the Open panel modally relative to the app.
- To choose files or directories and use them in conjunction with an already open document or window, present the panel as a sheet attached to the corresponding window.

When you want to ask the user to select a document to display in a new window, display the standard Open panel modally. Document-based apps normally provide this behavior for you automatically, providing the infrastructure needed to respond to the Open command in the menu. To display this panel in other situations, you can implement your own method to display the panel. The steps for creating and presenting an Open panel yourself are as follows:

1. Use the [openPanel](https://developer.apple.com/documentation/appkit/nsopenpanel/1584365-openpanel) class method of `NSOpenPanel` to retrieve an Open panel object.
2. Present the panel using the [beginWithCompletionHandler:](https://developer.apple.com/documentation/appkit/nssavepanel/1527007-begin) method.
3. Use your completion handler to process the results.

Listing 5-1 shows a custom method that presents the standard Open panel to the user. This panel uses the default configuration options, which support the selection of a single file from all available file types. The `beginWithCompletionHandler:` method displays the panel in a detached window and returns immediately. The panel runs modally relative to the app and calls the supplied completion handler on the app’s main thread when an item is selected. Upon the successful selection of a document, you need to provide the code to open the document and present its window.

__Listing 5-1__  Presenting the Open panel to the user

```objc
- (IBAction)openExistingDocument:(id)sender {
   NSOpenPanel* panel = [NSOpenPanel openPanel];

   // This method displays the panel and returns immediately.
   // The completion handler is called when the user selects an
   // item or cancels the panel.
   [panel beginWithCompletionHandler:^(NSInteger result){
      if (result == NSFileHandlingPanelOKButton) {
         NSURL*  theDoc = [[panel URLs] objectAtIndex:0];

         // Open  the document.
      }

   }];
}
```

In a document-based app, requests to display the Open panel are handled by the [openDocument:](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/1515005-opendocument) method of the app’s document controller object, which is part of the app’s default responder chain. Instead of implementing your own Open panel code, you might consider calling the `openDocument:` method instead. Doing so ensures that your custom code and the default app infrastructure always display the same Open panel. Customizing the panel at a later time also becomes easier because you have to make changes in only one place.

For more information about implementing a document-based app, see _[Mac App Programming Guide](../../General/Mac%20App%20Programming%20Guide/About%20OS%20X%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbt)_.

To choose files or directories that relate to the current window, configure the standard Open panel as a Choose panel and use it to retrieve the user’s selection. The main difference between the standard Open panel and a Choose panel is how you present it. Whereas you present the standard Open panel as a standalone modal panel, you almost always attach a Choose panel to one of your existing windows. Attaching the panel to a window makes it modal to the window but not to your whole app. Other differences relate to the configuration of the panel itself. A Choose panel can be configured to allow the selection of directories, multiple items, or hidden items among other options.

The [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) object returned by the [openPanel](https://developer.apple.com/documentation/appkit/nsopenpanel/1584365-openpanel) method is configured with the following default options:

- File selection: enabled
- Directory selection: disabled
- Resolve aliases: enabled
- Multiple selection: disabled
- Show hidden files: disabled
- File packages treated as directories: disabled
- Can create directories: disabled

Listing 5-2 shows a method you might implement in one of your [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) subclasses to import some files and associate them with the document. After configuring the panel, this method uses the [beginSheetModalForWindow:completionHandler:](https://developer.apple.com/documentation/appkit/nssavepanel/1535870-beginsheetmodal) method to present the panel as a sheet attached to the document’s main window. If the user selects some files, the [URLs](https://developer.apple.com/documentation/appkit/nsopenpanel/1529845-urls) method contains the corresponding file and directory references to incorporate.

__Listing 5-2__  Associating an Open panel with a window

```objc
- (IBAction)importFilesAndDirectories:(id)sender {
   // Get the main window for the document.
   NSWindow* window = [[[self windowControllers] objectAtIndex:0] window];

   // Create and configure the panel.
   NSOpenPanel* panel = [NSOpenPanel openPanel];
   [panel setCanChooseDirectories:YES];
   [panel setAllowsMultipleSelection:YES];
   [panel setMessage:@"Import one or more files or directories."];

   // Display the panel attached to the document's window.
   [panel beginSheetModalForWindow:window completionHandler:^(NSInteger result){
      if (result == NSFileHandlingPanelOKButton) {
         NSArray* urls = [panel URLs];

         // Use the URLs to build a list of items to import.
      }

    }];
}
```

For single-window apps, associate the open panel with your app’s main window. For document-based apps, associate it with the main window of the current document.

For document-based apps, requests to save the current document should be handled by the document object itself. The [NSDocument](https://developer.apple.com/documentation/appkit/nsdocument) class implements sophisticated infrastructure to manage both the Save panel and save-related operations, such as autosaving. As a result, the document object often customizes the default Save panel significantly and making additional customizations is not recommended except through the existing `NSDocument` methods. You could still use a custom Save panel to handle the exporting of files using different file formats.

If you are not using the `NSDocument` infrastructure, you can create your own Save panels and display them at appropriate times. The [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) class provides methods for creating and customizing the default Save panel. When implementing your own document infrastructure, restrict your use of a Save panel to documents the user creates and wants to save. Do not use a Save panel for files your app creates and manages implicitly. For example, iPhoto does not prompt the user to specify the location of its main library file; it creates the file in a well-known location without any user interactions. However, iPhoto does present a Save panel when the user exports an image to disk.

Listing 5-3 shows a method that a document object might call when exporting a file to a new type. This method assembles a new filename from the document’s existing name and the new type being saved. It then presents the Save panel with the new name set as the default value and initiates the save operation as appropriate.

__Listing 5-3__  Saving a file with a new type

```objc

- (void)exportDocument:(NSString*)name toType:(NSString*)typeUTI
{
   NSWindow*       window = [[[self windowControllers] objectAtIndex:0] window];

   // Build a new name for the file using the current name and
   // the filename extension associated with the specified UTI.
   CFStringRef newExtension = UTTypeCopyPreferredTagWithClass((CFStringRef)typeUTI,
                                   kUTTagClassFilenameExtension);
   NSString* newName = [[name stringByDeletingPathExtension]
                       stringByAppendingPathExtension:(NSString*)newExtension];
   CFRelease(newExtension);

   // Set the default name for the file and show the panel.
   NSSavePanel*    panel = [NSSavePanel savePanel];
   [panel setNameFieldStringValue:newName];
   [panel beginSheetModalForWindow:window completionHandler:^(NSInteger result){
        if (result == NSFileHandlingPanelOKButton)
        {
            NSURL*  theFile = [panel URL];

            // Write the contents in the new format.
        }
    }];
}
```

For more information about implementing a document-based app, see _[Mac App Programming Guide](../../General/Mac%20App%20Programming%20Guide/About%20OS%20X%20App%20Design.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknbt)_.

If your app is able to open only specific file types, you can use filtering to restrict the user’s selections to the subset of files your app actually supports. The Open panel does not restrict the types of files the user can select by default. To prevent the user from selecting files your app cannot handle, install one or more filters on the Open panel. Files that do not match the provided filters are dimmed by the Open panel and cannot be selected by the user. You can also install filters on the Save panel to dim unknown file types.

You specify filters as UTIs, filename extensions, or a combination of the two. After collecting your filter strings into an array, you assign them to the panel using the [setAllowedFileTypes:](https://developer.apple.com/documentation/appkit/nssavepanel/1534419-allowedfiletypes) method. The panel handles the actual filtration of files for you. You can change the filters while the panel is visible.

Listing 5-4 shows an example of how to configure the Open panel to allow the selection of image types only. The [NSImage](https://developer.apple.com/documentation/appkit/nsimage) class provides a convenience method for retrieving the supported image types. Because the strings in the returned array are UTIs, the results are handed directly to the panel.

__Listing 5-4__  Filtering for image file types

```objc
- (IBAction)askUserForImage:(id)sender {
   NSOpenPanel*    panel = [NSOpenPanel openPanel];

   // Let the user select any images supported by
   // the NSImage class.
   NSArray* imageTypes = [NSImage imageTypes];
   [panel setAllowedFileTypes:imageTypes];

   [panel beginWithCompletionHandler:^(NSInteger result){
      if (result == NSFileHandlingPanelOKButton) {
         // Open the image.
      }

   }];
}
```


To present the user with additional options when opening or saving files, add an accessory view to the standard Open and Save panels. Normally, the Open and Save panels process events and handle all interactions until the user cancels or accepts the results. An _accessory view_ lets you add custom controls and views for gathering information or modify the behavior of the panel itself. For example, you might use custom controls to change the set of filters used by the panel or change the options your own code uses when opening or saving a file.

The basic process for adding an accessory view to an Open or Save panel is as follows:

1. Load the accessory view from a nib file. (You can create accessory views programmatically too, but using a nib file is often easier.)
2. Create the panel.
3. Associate your view with the panel using the [setAccessoryView:](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview) method.
4. Show the panel.

Compare the preceding steps to displaying a panel normally and the only difference is loading your view and calling the [setAccessoryView:](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview) method. All of the other work required to manage an accessory view and respond to events is your responsibility.

Because an accessory view is just another view, you define it the way you define other views in your app. An accessory view always consists of a single main view that may itself contain any number of subviews. The most common configuration for an accessory view is as a host for one or more controls. When the user interacts with the controls in your accessory view, those controls use the [target-action](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/TargetAction.html#//apple_ref/doc/uid/TP40009448-CH3) design pattern to call your app’s custom code. You can then use that code to store configuration options or take any relevant actions.

A nib file is the simplest way to define an accessory view. Before setting up the nib file, you need to know which object in your app is going to present the panel. For example, in a document-based app, your `NSDocument` subclass is usually responsible for displaying any Open and Save panels. In general, the object that presents the panel should also own the contents of the accessory view. With that in mind, the configuration of your nib file would be as follows:

1. Create a new nib file whose contents are a single view.
2. Set the File’s Owner of the nib file to the object that presents the panel.
3. Configure the contents of the nib file’s top-level view object.

   - Add any subviews, such as checkboxes, that you want to include in the accessory view.
   - You can change the class of the top-level view object if you want, but doing so is not required. If you use a generic view as the main view, the underlying panel provides the appropriate background appearance for the rest of your content.
4. Connect actions (as appropriate) to your views to facilitate interactions with your custom code. You should implement the action methods themselves in the object you assigned as File’s Owner.
5. Connect outlets (as appropriate) for any controls you use to gather data passively from the user. The completion handler for the panel can then use the outlets to access the data in the controls.
6. Size your accessory view to be as small as possible while still showing all subviews in their entirety.
7. Save the nib file.

When displaying an accessory view, the Open and Save panels show your entire accessory view. If your accessory view is larger than the panel itself, the panel grows to accommodate your view. If the panel grows too large, it could look strange or could cause problems on smaller screens. Most accessory views should have only a few controls anyway. So if you find yourself adding more than ten controls, you might want to consider whether an accessory view is appropriate or if there is a better way to gather the information.

For more detail on the process of building a user interface and creating and configuring interface builder files, see [Xcode Help](https://help.apple.com/xcode).

Immediately before displaying an Open or Save panel, load (or create) your accessory view and attach it to the panel using the [setAccessoryView:](https://developer.apple.com/documentation/appkit/nssavepanel/1525544-accessoryview) method. If you create your accessory view programmatically, you normally create it right before presenting the panel itself. If you store your accessory view in a nib file, you load that nib file first.

Loading the nib file for an accessory view is relatively simple as long as the nib file itself is configured properly. The easiest way to configure the nib file is to assign the object that presents the panel as the File’s Owner of the nib file itself. That way, any outlets and actions defined on the object are connected automatically and ready to use as soon as the nib file is loaded into memory. Listing 5-5 shows an example of how this works. The method in this example is implemented on an `NSDocument` object. When called, the method presents an Open panel with an accessory view attached to the document’s main window. The accessory view itself contains a single checkbox that is connected to a custom `optionCheckbox` [outlet](https://developer.apple.com/library/archive/documentation/General/Devpedia-CocoaApp-MOSX/Outlet.html#//apple_ref/doc/uid/TP40009448-CH4) that the document object defines. (The outlet itself is implemented using a [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13). ) The handler block uses the value of the checkbox to determine how to open the file.

__Listing 5-5__  Loading a nib file with an accessory view

```objc
- (IBAction)openFileWithOptions:(id)sender {
   NSOpenPanel*    panel = [NSOpenPanel openPanel];
   NSWindow*       window = [[[self windowControllers] objectAtIndex:0] window];

   // Load the nib file with the accessory view and attach it to the panel.
   if ([NSBundle loadNibNamed:@"MyAccessoryView" owner:self])
      [panel setAccessoryView:self.accessoryView];

   // Show the open panel and process the results.
   [panel beginSheetModalForWindow:window completionHandler:^(NSInteger result){
      if (result == NSFileHandlingPanelOKButton) {
         BOOL option1 = ([self.optionCheckbox state] == NSOnState);

         // Open the selected file using the specified option...
      }
   }];
}
```

If you create your accessory view programmatically, replace the `if` statement containing the call to the [loadNibNamed:owner:](https://developer.apple.com/documentation/foundation/nsbundle/1402904-loadnibnamed) method with your custom view-creation code.

For more information on how to load objects from nib files, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_.

[Next](Managing%20Files%20and%20Directories.md)[Previous](iCloud%20File%20Management.md)


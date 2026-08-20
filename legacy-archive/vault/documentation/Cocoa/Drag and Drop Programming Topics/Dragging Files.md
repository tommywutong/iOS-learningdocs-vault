---
title: Drag and Drop Programming Topics
apple_id: 10000069i
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: AppKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DragandDrop/Tasks/DraggingFiles.html
archived_at: '2026-07-15T07:15:06.882525Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Drag and Drop Programming Topics](Introduction%20to%20Drag%20and%20Drop.md)


[Next](Frequently%20Asked%20Questions.md)[Previous](Receiving%20Drag%20Operations.md)

# Dragging Files

When dragging files, the dragging pasteboard can transfer the files in four different ways. The pasteboard can hold a list of file paths, a single URL, a file’s complete contents, or a promise to create files at a location to be determined by the destination. Each style corresponds to a separate NSPasteboard data type and has a different method for reading and writing the dragged data. The following sections describe each style and how to handle them, whether you are the dragging source or destination.

Files can also be specified by their URLs. A file’s URL is stored in a pasteboard with the type `NSURLPboardType`. Unlike the `NSFilenamesPboardType`, which holds an array of file paths, the `NSURLPboardType` type holds a single NSURL object. It is not possible to store more than one URL on the pasteboard using this pasteboard type, so you cannot drag more than one file with a URL.

To initiate a drag operation on a file using its URL, you need to use the NSView or NSWindow method `dragImage:at:offset:event:pasteboard:source:slideBack:`. You must place the file’s URL onto the pasteboard yourself, using the NSURL method `writeToPasteboard:`. You must declare the `NSURLPboardType` before calling this method, though. This allows you to place both a file path and a file URL onto the pasteboard. The drag operation can then be dropped on destinations that registered for either drag type, or both. The following sample code shows a possible implementation for writing the data to the pasteboard.

```
// Write data to the pasteboard
NSURL *fileURL; // Assume this exists
NSPasteboard *pboard = [NSPasteboard pasteboardWithName:NSDragPboard];
[pboard declareTypes:[NSArray arrayWithObject:NSURLPboardType] owner:nil];
[fileURL writeToPasteboard:pboard];
```

See [Dragging File Paths](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dqljrgaytenjy) for more complete sample code on starting the drag operation.

After a drag operation is dropped, the dragging destination receives a `performDragOperation:` message. To extract the `NSURLPboardType` data from the pasteboard, use the NSURL class method `URLFromPasteboard:`.

```objc
- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSPasteboard *pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSURLPboardType] ) {
        NSURL *fileURL = [NSURL URLFromPasteboard:pboard];
        // Perform operation using the file’s URL
    }
    return YES;
}
```


Files do not need to be dragged using references to the file only; a file’s contents can be placed directly onto the pasteboard and dragged using the `NSFileContentsPboardType`. Use this pasteboard type when you want to supply the contents of a file instead of its location in the file system. The destination can choose to extract the data directly to a location in the file system that it specifies or into a file wrapper in memory.

To initiate a drag operation on a file’s contents, you need to use the NSView or NSWindow method `dragImage:at:offset:event:pasteboard:source:slideBack:`. You must place the file’s contents onto the pasteboard yourself. You can write the data to the pasteboard using either the `writeFileContents:` method, which reads the data directly from the file system, or the `writeFileWrapper:` method, which reads the data from an NSFileWrapper object that you have already created. The following sample code shows a possible implementation for writing the data to the pasteboard.

```
// Write data to the pasteboard
NSString *filename; // Assume this exists
NSPasteboard *pboard = [NSPasteboard pasteboardWithName:NSDragPboard];
[pboard writeFileContents:filename];
```

See [Dragging File Paths](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4dqljrgaytenjy) for more complete sample code on starting the drag operation.

In addition to writing the file’s contents to the pasteboard with the general type `NSFileContentsPboardType`, the `writeFileContents:` and `writeFileWrapper:` methods write the data with a more specific type based on the file’s filename extension, if it exists. The drag destination can register for this more specific type instead of the generic type to restrict drags to files of a particular type, such as `mp3` or `mov` files. You can obtain the name of this specific pasteboard type by passing the filename extension to the `NSCreateFileContentsPboardType` function, which returns an NSString. The following code sample shows how a view could register to receive only QuickTime movie files.

```
NSString *pboardType = NSCreateFileContentsPboardType(@"mov");
NSArray *dragTypes = [NSArray arrayWithObject:pboardType];
[self registerForDraggedTypes:dragTypes];
```

After a drag operation is dropped, the dragging destination receives a `performDragOperation:` message. To extract the file contents from the pasteboard, use either the `readFileContentsType:toFile:` method, which copies the data from the pasteboard and writes it to the file path you specify, or the `readFileWrapper` method, which creates an NSFileWrapper object from the pasteboard data.

```objc
- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSPasteboard *pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSFileContentsPboardType] ) {
        NSFileWrapper *fileContents = [pboard readFileWrapper];
        // Perform operation using the file’s contents
    }
    return YES;
}
```


In some cases, you may want to drag a file before it actually exists within the file system. You may have a new document that hasn’t been saved, yet, or perhaps the file exists on a remote system, such as a web server, to which the dragging destination may not have access. (Typically, the destination is the Finder.) In these cases, the drag operation serves as a technique for specifying a location at which to save the new file. When the drag operation is dropped, the dragging destination tells the source where it wants the files saved and the dragging source creates the files. This type of file drag is called an HFS promise, because, in essence, the drag operation contains a promise from the source to the destination that the source will create the specified files if the drag operation is accepted. The data on the pasteboard has the type `NSFilesPromisePboardType`.

To initiate an HFS promise drag operation on one or more files, you need to use the NSView method `dragPromisedFilesOfTypes:fromRect:source:slideBack:event:`. The first argument is an array listing the file types of all the files the source promises to create. The types can be specified as filename extensions or as HFS file types encoded using the `NSFileTypeForHFSTypeCode` function. If a directory hierarchy is being dragged, only the top-level files and directories need to be listed in the type array. The `dragPromisedFiles...` method places the file type array onto the dragging pasteboard with the `NSFilesPromisePboardType` pasteboard type and starts the drag operation.

```objc
- (void)mouseDown:(NSEvent *)theEvent
{
    NSPoint dragPosition;
    NSRect imageLocation;

    dragPosition = [self convertPoint:[theEvent locationInWindow]
                        fromView:nil];
    dragPosition.x -= 16;
    dragPosition.y -= 16;
    imageLocation.origin = dragPosition;
    imageLocation.size = NSMakeSize(32,32);
    [self dragPromisedFilesOfTypes:[NSArray arrayWithObject:@"pdf"]
            fromRect:imageLocation
            source:self
            slideBack:YES
            event:theEvent];
}
```

When dragging HFS promises, the dragging source must also implement the `namesOfPromisedFilesDroppedAtDestination:` method. This method is invoked when the destination accepts the drag operation. The single argument is an NSURL object that identifies the location within the file system that the source should create the files. The method returns a list of the filenames (not full paths) of all the files the source promised to create. If a directory hierarchy is being dragged, only the top-level objects need to be listed in the returned array.

For short operations, you can create the promised files within the `namesOfPromisedFilesDroppedAtDestination:` method. For long operations, however, you should defer the creation of the files until later to avoid blocking the destination application. One technique is to cache the destination URL and create the files in your source’s `draggedImage:endedAt:operation:` method. Alternatively, you could spawn a background thread to create the files or delay the action on the current thread using an NSTimer, an NSNotificationQueue, or the NSObject method `performSelector:withObject:afterDelay:`.

Before the drag is actually dropped, a potential dragging destination does not have access to the filenames of the files being promised. Only the file types are available from the pasteboard. The destination can obtain the file types by requesting the pasteboard’s `NSFilesPromisePboardType` data using the `propertyListForType:` method. The returned array contains the file types that the source passed to the `dragPromisedFiles...` method. The destination can then accept or reject a drag operation based on the contents of the types array.

After a drag operation is dropped, the dragging destination receives a `performDragOperation:` message. To specify the drop location and to obtain the filenames of the promised files, use the dragging information object’s `namesOfPromisedFilesDroppedAtDestination:` method, passing the NSURL for the drop location as the one argument. The return value is an array of the filenames (not full paths) of the files that the source will create. The dragging destination must invoke this method only within `performDragOperation:` or else the source may create the files in the incorrect location.

```objc
NSURL *dropLocation; // Assume this exists

- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSPasteboard *pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSFilesPromisePboardType] ) {
        NSArray *filenames = [sender
                namesOfPromisedFilesDroppedAtDestination:dropLocation];
        // Perform operation using the files’ names, but without the
        // files actually existing yet
    }
    return YES;
}
```


Historically, some apps supported dragging files by transmitting a list of the files’ paths. The dragging source creates an NSArray containing NSString objects of all the paths of the files to be dragged and places the array onto the pasteboard with the data type `NSFilenamesPboardType`. The dragging destination then reads the array from the pasteboard and performs the requested operation using the paths that it holds.

To initiate a drag operation for a single file, you can use the NSView method `dragFile:fromRect:slideBack:event:` when the user clicks in the view representing the file. The first argument is the path of the file to drag. This method places the file’s path onto the dragging pasteboard with the `NSFilenamesPboardType` pasteboard type and starts the drag operation.

To initiate a drag operation on multiple files, you need to use the NSView or NSWindow method `dragImage:at:offset:event:pasteboard:source:slideBack:`. You must place the array of file paths onto the pasteboard yourself, using the NSPasteboard method `setPropertyList:forType:`. The following sample code shows a possible implementation.

```objc
NSString *filePath1, *filePath2; // Assume these exist

- (void)mouseDown:(NSEvent *)theEvent
{
    NSImage *dragImage;
    NSPoint dragPosition;

    // Write data to the pasteboard
    NSArray *fileList = [NSArray arrayWithObjects:filePath1, filePath2, nil];
    NSPasteboard *pboard = [NSPasteboard pasteboardWithName:NSDragPboard];
    [pboard declareTypes:[NSArray arrayWithObject:NSFilenamesPboardType]
            owner:nil];
    [pboard setPropertyList:fileList forType:NSFilenamesPboardType];

    // Start the drag operation
    dragImage = [[NSWorkspace sharedWorkspace] iconForFile:filePath1];
    dragPosition = [self convertPoint:[theEvent locationInWindow]
                        fromView:nil];
    dragPosition.x -= 16;
    dragPosition.y -= 16;
    [self dragImage:dragImage
            at:dragPosition
            offset:NSZeroSize
            event:theEvent
            pasteboard:pboard
            source:self
            slideBack:YES];
}
```

After a drag operation is dropped, the dragging destination receives a `performDragOperation:` message. To extract the `NSFilenamesPboardType` data from the pasteboard, use the `propertyListForType:` method. Even if only one file is being dragged, the file’s path is stored in an NSArray.

```objc
- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSPasteboard *pboard = [sender draggingPasteboard];

    if ( [[pboard types] containsObject:NSFilenamesPboardType] ) {
        NSArray *files = [pboard propertyListForType:NSFilenamesPboardType];
        int numberOfFiles = [files count];
        // Perform operation using the list of files
    }
    return YES;
}
```

[Next](Frequently%20Asked%20Questions.md)[Previous](Receiving%20Drag%20Operations.md)


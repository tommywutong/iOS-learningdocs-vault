---
title: IKImageView with drag and drop
apple_id: DTS40014787
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2014-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1866/_index.html
archived_at: '2026-07-18T02:35:09.455330Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1866

# IKImageView with drag and drop

## Q:  The `IKImageView` has the ability to receive drags. How can I add the ability to perform outgoing drags? What flavor should I use to drag images to instances of `IKImageView`?

A: `IKImageView` provides drag and drop handlers for receiving images by way of the `NSFilenamesPboardType` pasteboard flavor. They are able to receive drag and dropped image files, but they do not have a built in ability to provide outgoing drags. You can add that ability yourself by adding a -`mouseDown`: (or -`mouseMoved`:) handler to a subclass of `IKImageView` that you can use to initiate outgoing drags.

The `NSFilenamesPboardType` requires special handling because it must reference image files saved on disk and is not the same as just adding image data to the pasteboard. If you would like to provide drag and drop data to instances of `IKImageView` in your own windows or in other application's windows, then you will need to implement your own outgoing drags using the `NSFilenamesPboardType` flavor and manage the files yourself.

The listing below shows an example of how to initiate a drag from inside a -`mouseDown`: handler on a subclass of `IKImageView` that will allow you to drag images to other instances of `IKImageView`.

__Listing 1__  Initiating an outgoing drag from an `IKImageView`

```objc
- (void)mouseDown:(NSEvent*)event
{
  NSLog(@"%s",__FUNCTION__);

  // if there is an image to drag around...
  if ( [self image] != NULL ) {

    // generate a file name, path, and url
    NSString *fileName = [NSString stringWithFormat:@"%@-%@",
        [[NSProcessInfo processInfo] globallyUniqueString],
        @"dragfile.png"];
    NSString *filePath =
        [NSTemporaryDirectory() stringByAppendingPathComponent:fileName];
    NSURL *fileURL = [NSURL fileURLWithPath:filePath];


    // create a temporary file to house the image
    CGImageDestinationRef destination = CGImageDestinationCreateWithURL(
        (__bridge CFURLRef) fileURL, kUTTypePNG, 1, NULL);
    if ( destination != NULL ) {
      CGImageDestinationAddImage(destination, [self image], nil);
      if ( CGImageDestinationFinalize(destination) ) {

        // add a reference to the file path to the drag pasteboard
        // using the special NSFilenamesPboardType type
        NSPasteboard *dragPasteboard =
            [NSPasteboard pasteboardWithName:NSDragPboard];
        [dragPasteboard declareTypes:@[NSFilenamesPboardType] owner:nil];
        [dragPasteboard setPropertyList:@[filePath]
            forType:NSFilenamesPboardType];

        // calculate the drag image and position
        NSImage* dragImage = [[NSWorkspace sharedWorkspace]
            iconForFile:filePath];
        NSPoint dragPosition = [self convertPoint:[event locationInWindow]
            fromView:nil];

        // perform the drag operation
        // this method call runs synchronously
        // so we can delete the file after it is
        // compete
        [self dragImage:dragImage
            at:dragPosition
            offset:NSZeroSize
            event:event
            pasteboard: dragPasteboard
            source:self
            slideBack:YES];

        // the above dragImage method runs synchronously, so when we return
        // here the drag operation is technically complete, the receiver will
        // have been called, etc.... However, some receivers will only have
        // made note of the drag operation and they may not be finished
        // with the file just yet so it's important not to delete it right away.
        // In this sample we maintain the file on disk for a short time
        // before deleting it.
        const uint64_t kSecondsToKeepFile = 3, kNanosecondsPerSecond = 1000000000;
        dispatch_queue_t mainqueue =
            dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
        dispatch_time_t when =
            dispatch_time(0, kNanosecondsPerSecond*kSecondsToKeepFile);
        dispatch_after(when, mainqueue,
          ^{  NSError *error;
            if (![[NSFileManager defaultManager] removeItemAtPath:filePath error:&error]) {
              NSLog(@"error removing %@ %@", filePath, error);
            }
          });
      }

      // done with the image destination
      CFRelease(destination);
    }

  }
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-05 | New document that explains how to use drag and drop with the IKImageView. |


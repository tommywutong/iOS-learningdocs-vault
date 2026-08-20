---
title: 'ImageBrowser: Using IKImageBrowserView to display images'
apple_id: DTS10003997
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/ImageBrowser/Listings/ImageBrowserController_m.html
archived_at: '2026-07-18T03:12:19.285176Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImageBrowser: Using IKImageBrowserView to display images](ImageBrowser-%20Using%20IKImageBrowserView%20to%20display%20images.md)


[Next](ImageBrowserController.h.md)[Previous](main.m.md)

# ImageBrowserController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
  See LICENSE.txt for this sample’s licensing information

  Abstract:
  IKImageBrowserView is a view that can display and browse images and movies.
   This sample code demonstrate how to use it in a Cocoa Application. 
 */

@import Quartz;   // for IKImageBrowserView

#import "ImageBrowserController.h"

// our data source object for the image browser
@interface myImageObject : NSObject

@property (strong) NSURL *url;

@end


#pragma mark -

@implementation myImageObject

#pragma mark - IKImageBrowserItem

// Required methods of the IKImageBrowserItem protocol.

// Let the image browser knows we use a URL representation.
- (NSString *)imageRepresentationType
{
    return IKImageBrowserNSURLRepresentationType;
}

// Give our representation to the image browser.
- (id)imageRepresentation
{
    return self.url;
}

// Use the absolute filepath of our URL as identifier.
- (NSString *)imageUID
{
    return self.url.path;
}

@end


#pragma mark -

@interface ImageBrowserController ()

@property (weak) IBOutlet IKImageBrowserView *imageBrowser;

@property (strong) NSMutableArray *images;
@property (strong) NSMutableArray *importedImages;

@property (assign) NSDragOperation currentDragOperation;

@end


#pragma mark -

@implementation ImageBrowserController

// -------------------------------------------------------------------------
//  viewDidLoad
// -------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // Create two arrays : the first one is our datasource representation,
    // the second one are temporary imported images (for thread safeness).
    //
    _images = [[NSMutableArray alloc] init];
    _importedImages = [[NSMutableArray alloc] init];

    // Allow reordering, animations et set draggind destination delegate.
    [self.imageBrowser setAllowsReordering:YES];
    [self.imageBrowser setAnimates:YES];
    [self.imageBrowser setDraggingDestinationDelegate:self];

    _currentDragOperation = NSDragOperationNone;
}

// -------------------------------------------------------------------------
//  updateDatasource
//
//  Entry point for reloading image-browser's data and setNeedsDisplay.
// -------------------------------------------------------------------------
- (void)updateDatasource
{
    // Update our datasource, add recently imported items.
    [self.images addObjectsFromArray:self.importedImages];

    // Empty our temporary array.
    [self.importedImages removeAllObjects];

    // Reload the image browser and set needs display.
    [self.imageBrowser reloadData];
}


#pragma mark - Import images from file system

// -------------------------------------------------------------------------
//  isImageFile:filePath
//
//  This utility method indicates if the file located at 'filePath' is
//  an image file based on the UTI. It relies on the ImageIO framework for the
//  supported type identifiers.
// -------------------------------------------------------------------------
- (BOOL)isImageFile:(NSString *)filePath
{
    BOOL isImageFile = NO;
    NSError *error = nil;
    NSURL *fileURL = [NSURL fileURLWithPath:filePath];

    NSDictionary *resourceValueDict =
        [fileURL resourceValuesForKeys:@[NSURLTypeIdentifierKey] error:&error];
    if (resourceValueDict != nil)
    {
        // Verify that this is a file that the ImageIO framework supports.
        NSString *fileUTI = resourceValueDict[NSURLTypeIdentifierKey];
        if (fileUTI != nil) {
            CFArrayRef supportedTypes = CGImageSourceCopyTypeIdentifiers();
            CFIndex idx, typeCount = CFArrayGetCount(supportedTypes);
            for (idx = 0; idx < typeCount; idx++)
            {
                if (UTTypeConformsTo((__bridge CFStringRef _Nonnull)(fileUTI),
                                     (CFStringRef)CFArrayGetValueAtIndex(supportedTypes, idx)))
                {
                    isImageFile = YES;
                    break;
                }
            }
            CFRelease(supportedTypes);
        }
    }
    return isImageFile;
}

// -------------------------------------------------------------------------
//  addImagesWithPathURL:url
// -------------------------------------------------------------------------
- (void)addImagesWithPathURL:(NSURL *)url
{
    BOOL dir = NO;
    [[NSFileManager defaultManager] fileExistsAtPath:url.path isDirectory:&dir];
    if (dir)
    {
        // We are being passed a directory URL, add all the images in that directory.
        NSError *error = nil;
        NSArray *content = [[NSFileManager defaultManager] contentsOfDirectoryAtURL:url
                                                         includingPropertiesForKeys:@[]
                                                                            options:0
                                                                              error:&error];
        if (error == nil)
        {
            for (NSURL *imageURL in content)
            {
                [self addAnImageWithPath:imageURL];
            }
        }
    }
    else
    {
        // We are being passed an image URL, just load the one.
        [self addAnImageWithPath:url];
    }
}

// -------------------------------------------------------------------------
//  addAnImageWithPath:url
// -------------------------------------------------------------------------
- (void)addAnImageWithPath:(NSURL *)url
{
    BOOL addObject = NO;

    NSDictionary *fileAttribs = [[NSFileManager defaultManager] attributesOfItemAtPath:url.path error:nil];
    if (fileAttribs != nil)
    {
        // Check for packages.
        if ([NSFileTypeDirectory isEqualTo:fileAttribs[NSFileType]])
        {
            if ([[NSWorkspace sharedWorkspace] isFilePackageAtPath:url.path] == NO)
            {
                addObject = YES; // If it is a file, it's OK to add.
            }
        }
        else
        {
            addObject = YES; // It is a file, so it's OK to add.
        }
    }

    if (addObject && [self isImageFile:url.path])
    {
        // Add a path to the temporary images array.
        myImageObject *p = [[myImageObject alloc] init];
        p.url = url;
        [self.importedImages addObject:p];
    }
}


#pragma mark - Actions

// -------------------------------------------------------------------------
//  addImageButtonClicked:sender
//
//  The user clicked the Add Photos button.
// -------------------------------------------------------------------------
- (IBAction)addImageButtonClicked:(id)sender
{
    NSOpenPanel *openPanel = [NSOpenPanel openPanel];
    openPanel.canChooseDirectories = YES;
    openPanel.allowsMultipleSelection = YES;

    void (^openPanelHandler)(NSInteger) = ^(NSInteger returnCode) {
        if (returnCode == NSModalResponseOK)
        {
            // Asynchronously process all URLs from our open panel.
            dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
                for (NSURL *url in openPanel.URLs)
                {
                    [self addImagesWithPathURL:url];
                }
                // Back on the main queue update the data source in the main thread.
                dispatch_async(dispatch_get_main_queue(), ^(void) {
                    [self updateDatasource];
                });
            });
        }
    };

    [openPanel beginSheetModalForWindow:self.view.window completionHandler:openPanelHandler];
}

// -------------------------------------------------------------------------
//  zoomSliderDidChange:sender:
//
//  Action called when the zoom slider did change.
// -------------------------------------------------------------------------
- (IBAction)zoomSliderDidChange:(id)sender
{
    // Update the zoom value to scale images.
    [self.imageBrowser setZoomValue:[sender floatValue]];

    // Redisplay.
    [self.imageBrowser setNeedsDisplay:YES];
}


#pragma mark - IKImageBrowserDataSource

// -------------------------------------------------------------------------
//  numberOfItemsInImageBrowser:view:
//
//  Our datasource representation is a simple mutable array.
// -------------------------------------------------------------------------
- (NSUInteger)numberOfItemsInImageBrowser:(IKImageBrowserView *)view
{
    // Item count to display is our datasource item count.
    return self.images.count;
}

// -------------------------------------------------------------------------
//  imageBrowser:view:index:
// -------------------------------------------------------------------------
- (id)imageBrowser:(IKImageBrowserView *)view itemAtIndex:(NSUInteger)index
{
    return self.images[index];
}


#pragma mark - IKImageBrowserDataSource

// Implement some optional methods of the image browser  datasource protocol to allow
// for removing and reodering items.

// -------------------------------------------------------------------------
//  removeItemsAtIndexes:indexes:
//
//  The user wants to delete images, so remove these entries from our datasource.
// -------------------------------------------------------------------------
- (void)imageBrowser:(IKImageBrowserView *)view removeItemsAtIndexes:(NSIndexSet *)indexes
{
    [self.images removeObjectsAtIndexes:indexes];
}

// -------------------------------------------------------------------------
//  moveItemsAtIndexes:indexes:destinationIndex:
//
//  The user wants to reorder images, update our datasource and the browser will reflect our changes.
// -------------------------------------------------------------------------
- (BOOL)imageBrowser:(IKImageBrowserView *)view moveItemsAtIndexes:(NSIndexSet *)indexes toIndex:(NSUInteger)destinationIndex
{
      NSMutableArray *temporaryArray = [[NSMutableArray alloc] init];

      // First remove items from the datasource and keep them in a temporary array.
      for (NSUInteger index = indexes.lastIndex; index != NSNotFound; index = [indexes indexLessThanIndex:index])
      {
          if (index < destinationIndex)
          {
              destinationIndex --;
          }

          id obj = self.images[index];
          [temporaryArray addObject:obj];
          [self.images removeObjectAtIndex:index];
      }

      // Then insert removed items at the good location.
      for (NSUInteger index = 0; index < temporaryArray.count; index++)
      {
          [self.images insertObject:temporaryArray[index] atIndex:destinationIndex];
      }

      return YES;
}


#pragma mark - Drag and Drop

// -------------------------------------------------------------------------
//  dragOperation:sender
// -------------------------------------------------------------------------
- (NSDragOperation)dragOperation:(id <NSDraggingInfo>)sender
{
    NSDragOperation result = NSDragOperationNone;

    NSPasteboard *pboard = [sender draggingPasteboard];
    NSArray *filenames = [pboard propertyListForType:NSFilenamesPboardType];

    BOOL dragNotAccepted = NO;

    for (NSString *fileName in filenames)
    {
        if (![self isImageFile:fileName])
        {
            dragNotAccepted = YES;
            break;
        }
    }

    if (!dragNotAccepted)
    {
        result = NSDragOperationCopy;
    }

    return result;
}

// -------------------------------------------------------------------------
//  draggingEntered:sender
//
//  Accept dropping of images.
// -------------------------------------------------------------------------
- (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender
{
    _currentDragOperation = [self dragOperation:sender];

    return [self dragOperation:sender];
}

// -------------------------------------------------------------------------
//  draggingUpdated:sender
// -------------------------------------------------------------------------
- (NSDragOperation)draggingUpdated:(id <NSDraggingInfo>)sender
{
    return self.currentDragOperation;
}

// -------------------------------------------------------------------------
//  performDragOperation:sender
// -------------------------------------------------------------------------
- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSData *data = nil;
    NSPasteboard *pasteboard = [sender draggingPasteboard];

    // Look for paths in pasteboard.
    if ([pasteboard.types containsObject:NSFilenamesPboardType])
    {
        data = [pasteboard dataForType:NSFilenamesPboardType];
    }

    if (data != nil)
    {
        // Retrieves paths.
        NSError *error;
        NSArray *filenames =
            [NSPropertyListSerialization propertyListWithData:data
                                                      options:NSPropertyListImmutable
                                                       format:nil
                                                        error:&error];

        // Add these file paths to our data source as URLs.
        for (NSString *filePath in filenames)
        {
            [self addAnImageWithPath:[NSURL fileURLWithPath:filePath]];
        }

        // Make the image browser reload our datasource.
        [self updateDatasource];
    }

    // We accepted the drag operation.
    return YES;
}

@end
```

[Next](ImageBrowserController.h.md)[Previous](main.m.md)


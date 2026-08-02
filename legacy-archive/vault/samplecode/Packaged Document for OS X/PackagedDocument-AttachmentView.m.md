---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_AttachmentView_m.html
archived_at: '2026-07-18T03:18:44.705389Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-AttachmentView.h.md)[Previous](PackagedDocument-WindowController.m.md)

# PackagedDocument/AttachmentView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom view holding the image to attach to our document.
 */

#import "AttachmentView.h"
#import "ViewController.h"

@interface AttachmentView ()

@property BOOL highlightForDragAcceptence;

@end


#pragma mark -

@implementation AttachmentView

- (void)commonInit
{
    // Register for all the image types we can display - include NSFilenamesPboardType for Finder drags.
    NSMutableArray *dragTypes = [[NSImage imageTypes] mutableCopy];
    [dragTypes addObject:NSFilenamesPboardType];
    [self registerForDraggedTypes:dragTypes];

    [self setKeyboardFocusRingNeedsDisplayInRect:self.bounds];

    self.highlightForDragAcceptence = NO;
}

- (instancetype)initWithCoder:(NSCoder *)coder
{
    // Init method called for Interface Builder objects.
    self = [super initWithCoder:coder];
    if (self)
    {
        [self commonInit];
    }
    return self;
}

- (instancetype)initWithFrame:(NSRect)frame
{
    self = [super initWithFrame:frame];
    if (self)
    {
        [self commonInit];
    }

    return self;
}

- (void)drawRect:(NSRect)rect
{
    [super drawRect:rect];

    // Draw the focus frame if necessary.
    if (self.highlightForDragAcceptence)
    {
        [NSGraphicsContext saveGraphicsState];
        NSSetFocusRingStyle(NSFocusRingOnly);
        [[NSBezierPath bezierPathWithRect: NSInsetRect(self.bounds,3,3)] fill];
        [NSGraphicsContext restoreGraphicsState];
    }
}

- (void)dealloc
{
    [self unregisterDraggedTypes];
}

- (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender
{
    NSDragOperation dragOperation = NSDragOperationNone;

    if ((NSDragOperationCopy & [sender draggingSourceOperationMask]) == NSDragOperationCopy)
    {
        self.highlightForDragAcceptence = YES;
        [self setNeedsDisplay:YES];

        // The sender is offering the type of operation we want,
        // return that we want the NSDragOperationCopy (cursor has a + image).
        //
        dragOperation = NSDragOperationCopy;
    }

    return dragOperation;
}

- (void)draggingExited:(id <NSDraggingInfo>)sender
{
    // User has left our drag area, erase our focus frame.
    self.highlightForDragAcceptence = NO;
    [self setNeedsDisplay:YES];
}

- (NSDragOperation)draggingUpdated:(id <NSDraggingInfo>)sender
{
    NSDragOperation dragOperation = NSDragOperationNone;

    if ((NSDragOperationCopy & [sender draggingSourceOperationMask]) == NSDragOperationCopy)
    {
        // The sender is offering the type of operation we want,
        // return that we want the NSDragOperationCopy (cursor has a + image).
        //
        dragOperation = NSDragOperationCopy;
    }

    return dragOperation;
}

- (void)draggingEnded:(id <NSDraggingInfo>)sender
{
    //..
}

- (BOOL)prepareForDragOperation:(id <NSDraggingInfo>)sender
{
    return YES;
}

- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender
{
    NSPasteboard *paste = [sender draggingPasteboard];

    // Gets the dragging-specific pasteboard from the sender.
    NSArray *types = @[NSTIFFPboardType, NSFilenamesPboardType];

    // A list of types that we can accept.
    NSString *desiredType = [paste availableTypeFromArray:types];
    NSData *carriedData = [paste dataForType:desiredType];

    if (carriedData == nil)
    {
        // The drag operation failed.
        return NO;
    }
    else
    {
        // the pasteboard was able to give us some meaningful data.
        if ([desiredType isEqualToString:NSTIFFPboardType])
        {
            // We have TIFF bitmap data in the NSData object.
            // Keep a reference to the image for drawing.
            self.image = [[NSImage alloc] initWithData:carriedData];

        }
        else if ([desiredType isEqualToString:NSFilenamesPboardType])
        {
            // We have a list of file names in an NSData object.
            NSArray *fileArray = [paste propertyListForType:@"NSFilenamesPboardType"];

            NSString *path = fileArray[0];

            // Assume that we can ignore all but the first path in the list.
            NSImage *newImage = [[NSImage alloc] initWithContentsOfFile:path];
            if (newImage == nil)
            {
                // Failed to open the file.
                return NO;
            }
            else
            {
                // Keep a reference to the image for drawing.
                self.image = newImage;

                // Tell our window controller that a new image was dragged in by the user.
                ViewController *viewController = (ViewController *)self.window.contentViewController;
                [viewController updateImage:newImage];
            }
        }
        else
        {
            return NO;
        }
    }

    // Erase the drag acceptance highlight, and draws the new image.
    self.highlightForDragAcceptence = NO;
    [self setNeedsDisplay:YES];

    return YES;
}

@end
```

[Next](PackagedDocument-AttachmentView.h.md)[Previous](PackagedDocument-WindowController.m.md)


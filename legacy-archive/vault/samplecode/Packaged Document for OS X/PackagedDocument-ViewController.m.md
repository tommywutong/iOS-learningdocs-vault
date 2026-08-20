---
title: Packaged Document for OS X
apple_id: DTS40012955
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-03-09'
source_url: https://developer.apple.com/library/archive/samplecode/PackagedDocument/Listings/PackagedDocument_ViewController_m.html
archived_at: '2026-07-18T03:18:45.089467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Packaged Document for OS X](Packaged%20Document%20for%20OS%20X.md)


[Next](PackagedDocument-MyTextPictDocument.h.md)[Previous](PackagedDocument-ViewController.h.md)

# PackagedDocument/ViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Primary NSViewController content for our document window.
 */

#import "ViewController.h"
#import "MyTextPictDocument.h"
#import "AttachmentView.h"
#import "WindowController.h"
#import "ImageView.h"

@import QuartzCore;   // for CAMediaTimingFunction

NSString *kClipImageName = @"clip";

@interface ViewController () <ImageViewDelegate>

@property (assign) NSInteger discloseDelta;

@property (weak) IBOutlet ImageView *imageView;
@property (weak) IBOutlet NSTextField *imageViewLabel;
@property (weak) IBOutlet AttachmentView *attachmentView;
@property (weak) IBOutlet NSImageView *attachedImageView;
@property (weak) IBOutlet NSButton *disclosureButton;

@property (strong) IBOutlet NSLayoutConstraint *attachmentViewheightConstraint;

@end


#pragma mark -

@implementation ViewController

// -------------------------------------------------------------------------------
//  viewDidLoad
//
//  Use this method to handle any initialization after this view controller's window has
//  been loaded from the storyboard.
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    [self.textView setAllowsUndo:YES];

    // The entire attachment view determines the drag operation, we don't want these image views to accept drags.
    [self.imageView unregisterDraggedTypes];
    [self.attachedImageView unregisterDraggedTypes];

    // We want to be notified when our image view changes (via cut, paste, delete).
    self.imageView.delegate = self;
}

// -------------------------------------------------------------------------------
//  viewWillAppear
// -------------------------------------------------------------------------------
- (void)viewWillAppear
{
    [super viewWillAppear];

    MyTextPictDocument *document = [self ourDocument];
    if (document != nil)
    {
        // Ask our document to update our text view and image view with it's model.
        [document updateTextView:self.textView];
        [document updateImageView:self.imageView];

        // If we have an image, update our clip image indicator.
        if (document.image != nil)
        {
            self.attachedImageView.image = [NSImage imageNamed:kClipImageName];
        }

        // Hide the image label if we have an image.
        self.imageViewLabel.hidden = (document.image != nil);
    }

    // Compute the amount to disclose/hide when the disclosure control is clicked.
    _discloseDelta =
        self.attachmentView.frame.size.height -
        (self.attachmentView.frame.size.height - self.disclosureButton.frame.origin.y) - 8;

    if (!(self.disclosureButton.state == self.disclosed))
    {
        // Disclose the attachment view only if our disclosure button is out of sync.
        self.disclosureButton.state = self.disclosed;
        [self disclose:NO];
    }

    // Initially key focus on the text view.
    [self.view.window makeFirstResponder:self.textView];
}

// -------------------------------------------------------------------------------
//  ourDocument
//
//  Accessor to reference our associated NSDocument through our window controller.
// -------------------------------------------------------------------------------
- (MyTextPictDocument *)ourDocument
{
    WindowController *windowController = (WindowController *)self.view.window.windowController;
    return windowController.document;
}


#pragma mark - Actions

// -------------------------------------------------------------------------------
//  imageDidChange:sender
//
//  User dragged an image to the imageView.
// -------------------------------------------------------------------------------
- (void)imageDidChange:(id)sender
{
    // Draw the paper clip image if we received a valid image.
    self.attachedImageView.image = (self.imageView.image != nil) ? [NSImage imageNamed:kClipImageName] : nil;

    MyTextPictDocument *document = [self ourDocument];
    [document updateImageModel:self.imageView.image];

    // Hide the image label if we have an image.
    self.imageViewLabel.hidden = (document.image != nil);
}

// -------------------------------------------------------------------------------
//  disclose:animated
// -------------------------------------------------------------------------------
- (void)disclose:(BOOL)animated
{
    CGFloat discloseAmount = self.imageView.frame.size.height;

    // Adjust the height constraint by the amount of the image view's height,
    // causing the bottom of the header to be flush with the bottom of the overall disclosure view.
    //
    if (animated)
    {
        [NSAnimationContext runAnimationGroup:^(NSAnimationContext *context) {
            context.timingFunction = [CAMediaTimingFunction functionWithName:kCAMediaTimingFunctionEaseInEaseOut];

            self.imageView.animator.hidden = !self.disclosureButton.state;

            if (self.disclosureButton.state)
            {
                self.attachmentViewheightConstraint.animator.constant += discloseAmount;
            }
            else
            {
                self.attachmentViewheightConstraint.animator.constant -= discloseAmount;
            }
        } completionHandler:^{

        }];
    }
    else
    {
        self.imageView.hidden = !self.disclosureButton.state;
        if (self.disclosureButton.state)
        {
            self.attachmentViewheightConstraint.constant += discloseAmount;
        }
        else
        {
            self.attachmentViewheightConstraint.constant -= discloseAmount;
        }
    }

    // Call our delegate (MyTextPictDocument) notifying the attachment view disclosure state changed,
    // so we can save this state as part of the document data.
    //
    [self.delegate viewController:self didDiscloseImage:self.disclosureButton.state];
}

// -------------------------------------------------------------------------------
//  discloseAction:sender
//
//  User clicked the disclosure control to expand/shrink the attachment view.
// -------------------------------------------------------------------------------
- (IBAction)discloseAction:(id)sender
{
    [self disclose:YES];
}


#pragma mark - NSTextDelegate

// -------------------------------------------------------------------------------
//  textDidChange:aNotification
//
//  The text view content had changed, update our data model.
// -------------------------------------------------------------------------------
- (void)textDidChange:(NSNotification *)aNotification
{
    MyTextPictDocument *document = [self ourDocument];
    NSString *str = self.textView.textStorage.string;
    [document updateTextModel:str];
}

// -------------------------------------------------------------------------------
//  updateImage:image
//
//  Our AttachmentView wants to set our image attachment update our data model.
// -------------------------------------------------------------------------------
- (void)updateImage:(NSImage *)image
{
    self.imageView.image = image;
    self.imageViewLabel.hidden = YES;
    [self imageDidChange:self];
}


#pragma mark - ImageViewDelegate

// -------------------------------------------------------------------------------
//  imageView:didChangeImage
//
//  Called by our NSImageView subclass to inform us the image has changed (via cut, copy, or delete).
// -------------------------------------------------------------------------------
- (void)imageView:(ImageView *)imageView didChangeImage:(NSImage *)image
{
    [self updateImage:image];
}


#pragma mark - Version browser support

// -------------------------------------------------------------------------------
//  windowWillEnterVersionBrowser
//
//  Use this method to customize this window for the versions browser.
// -------------------------------------------------------------------------------
- (void)windowWillEnterVersionBrowser:(NSNotification *)notification
{ }

// -------------------------------------------------------------------------------
//  windowDidExitVersionBrowser
//
//  Use this method to undo the customization of this window (done in windowWillEnterVersionBrowser).
// -------------------------------------------------------------------------------
- (void)windowDidExitVersionBrowser:(NSNotification *)notification
{ }

// -------------------------------------------------------------------------------
//  willResizeForVersionBrowserWithMaxPreferredSize:maxPreferredFrameSize:maxAllowedFrameSize
//
//  Help determine the optimal size for the version browser.
//  Windows entering the version browser will be resized to the size returned by this method.
// -------------------------------------------------------------------------------
- (NSSize)window:(NSWindow *)window willResizeForVersionBrowserWithMaxPreferredSize:(NSSize)maxPreferredFrameSize maxAllowedSize:(NSSize)maxAllowedFrameSize
{
    NSSize contentSize = self.textView.enclosingScrollView.documentView.bounds.size;
    contentSize = [self.textView.enclosingScrollView.documentView convertSize:contentSize toView:self.textView.enclosingScrollView];

    Class horizScrollerClass = [self.textView.enclosingScrollView.horizontalScroller class];
    Class vertScrollerClass = [self.textView.enclosingScrollView.verticalScroller class];

    NSSize windowContentSize = [NSScrollView frameSizeForContentSize:contentSize
                                             horizontalScrollerClass:horizScrollerClass
                                               verticalScrollerClass:vertScrollerClass
                                                          borderType:self.textView.enclosingScrollView.borderType
                                                         controlSize:NSControlSizeRegular
                                                       scrollerStyle:NSScrollerStyleLegacy]; 
    NSRect frameRect = [window frameRectForContentRect:(NSRect){ NSZeroPoint, windowContentSize }];
    return frameRect.size;
}

@end
```

[Next](PackagedDocument-MyTextPictDocument.h.md)[Previous](PackagedDocument-ViewController.h.md)


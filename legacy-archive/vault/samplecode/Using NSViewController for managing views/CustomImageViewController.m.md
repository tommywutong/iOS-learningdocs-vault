---
title: Using NSViewController for managing views
apple_id: DTS10004233
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2014-04-24'
source_url: https://developer.apple.com/library/archive/samplecode/ViewController/Listings/CustomImageViewController_m.html
archived_at: '2026-07-18T03:27:56.625082Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Using NSViewController for managing views](Using%20NSViewController%20for%20managing%20views.md)


[Next](CustomTableViewController.h.md)[Previous](CustomImageViewController.h.md)

# CustomImageViewController.m

```objc
/*
     File: CustomImageViewController.m 
 Abstract: The view controller for displaying images. 
  Version: 1.2 

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple 
 Inc. ("Apple") in consideration of your agreement to the following 
 terms, and your use, installation, modification or redistribution of 
 this Apple software constitutes acceptance of these terms.  If you do 
 not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software. 

 In consideration of your agreement to abide by the following terms, and 
 subject to these terms, Apple grants you a personal, non-exclusive 
 license, under Apple's copyrights in this original Apple software (the 
 "Apple Software"), to use, reproduce, modify and redistribute the Apple 
 Software, with or without modifications, in source and/or binary forms; 
 provided that if you redistribute the Apple Software in its entirety and 
 without modifications, you must retain this notice and the following 
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. may 
 be used to endorse or promote products derived from the Apple Software 
 without specific prior written permission from Apple.  Except as 
 expressly stated in this notice, no other rights or licenses, express or 
 implied, are granted by Apple herein, including but not limited to any 
 patent rights that may be infringed by your derivative works or by other 
 works in which the Apple Software may be incorporated. 

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE 
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION 
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS 
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND 
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS. 

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL 
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, 
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED 
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), 
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE 
 POSSIBILITY OF SUCH DAMAGE. 

 Copyright (C) 2014 Apple Inc. All Rights Reserved. 

 */

#import "CustomImageViewController.h"

@implementation CustomImageViewController

// -------------------------------------------------------------------------------
//  configureImage:imagePathStr
// -------------------------------------------------------------------------------
- (void)configureImage:(NSString *)imagePathStr
{
    // load the image from the given path string and set is to the NSImageView
    NSImage* image = [[NSImage alloc] initWithContentsOfFile:imagePathStr];
    [imageView setImage:image];
    [image release];
    [textView setStringValue:[imagePathStr lastPathComponent]]; // display the file name
}

// -------------------------------------------------------------------------------
//  awakeFromNib
// -------------------------------------------------------------------------------
- (void)awakeFromNib
{
    // load the default image from our bundle
    NSString *imagePathStr = [[NSBundle mainBundle] pathForResource:@"LakeDonPedro" ofType:@"jpg"];
    [self configureImage:imagePathStr];
}

// -------------------------------------------------------------------------------
//  openImageAction:sender
//
//  User clicked the "Open" button, open the NSOpenPanel to choose an image.
// -------------------------------------------------------------------------------
- (IBAction)openImageAction:(id)sender
{
    NSOpenPanel *openPanel = [NSOpenPanel openPanel];

    NSArray *fileTypes = [NSArray arrayWithObjects:@"jpg", @"gif", @"png", @"tiff", nil];
    [openPanel setAllowsMultipleSelection:NO];
    [openPanel setMessage:@"Choose an image file to display:"];
    [openPanel setAllowedFileTypes:fileTypes];
    [openPanel setDirectoryURL:[NSURL fileURLWithPath:@"/Library/Desktop Pictures/"]];
    [openPanel beginSheetModalForWindow:self.view.window completionHandler:^(NSInteger result) {
        if (result == NSOKButton)
        {
            if ([[openPanel URL] isFileURL])
            {
                [self configureImage:[[openPanel URL] path]];
            }
        }
    }];
}

@end
```

[Next](CustomTableViewController.h.md)[Previous](CustomImageViewController.h.md)


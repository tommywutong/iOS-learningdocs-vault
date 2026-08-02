---
title: ImagePicker
apple_id: DTS10003996
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2006-07-25'
source_url: https://developer.apple.com/library/archive/samplecode/ImagePicker/Listings/MyController_m.html
archived_at: '2026-07-18T03:12:45.092379Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ImagePicker](ImagePicker.md)


[Next](Document%20Revision%20History.md)[Previous](MyController.h.md)

# MyController.m

```objc
/*

File: MyController.m

Abstract: The image-picker is a panel that allows users to choose and 
  crop an image. It supports browsing of the file system and includes 
  a recents popup-menu. The IKImagePicker lets the user to crop a choosen 
  image or to take snapshot from a camera like the built-in iSight. This 
  Sample code demonstrate a very basic use of the image-picker to help 
  developers getting started.

Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Computer, Inc. ("Apple") in consideration of your agreement to the
following terms, and your use, installation, modification or
redistribution of this Apple software constitutes acceptance of these
terms.  If you do not agree with these terms, please do not use,
install, modify or redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software. 
Neither the name, trademarks, service marks or logos of Apple Computer,
Inc. may be used to endorse or promote products derived from the Apple
Software without specific prior written permission from Apple.  Except
as expressly stated in this notice, no other rights or licenses, express
or implied, are granted by Apple herein, including but not limited to
any patent rights that may be infringed by your derivative works or by
other works in which the Apple Software may be incorporated.

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

Copyright © 2006 Apple Computer, Inc., All Rights Reserved

*/

#import "MyController.h"



@implementation MyController

- (void) awakeFromNib
{
    /* retrieve the imagePicker shared instance */
    IKImagePicker *picker = [IKImagePicker imagePicker];

    /* set a default image to start */
    [picker setInputImage:[[[NSImage alloc] initByReferencingFile:@"/Library/Desktop Pictures/Nature/Ladybug.jpg"] autorelease]];        

    /* configure the image picker to your needs */
    //[picker setValue:[NSNumber numberWithBool:NO] forKey:IKImagePickerAllowsVideoCaptureKey];
    //[picker setValue:[NSNumber numberWithBool:NO] forKey:IKImagePickerAllowsFileChoosingKey];
    //[picker setValue:[NSNumber numberWithBool:NO] forKey:IKImagePickerShowRecentPictureKey];
    //[picker setValue:[NSNumber numberWithBool:NO] forKey:IKImagePickerUpdateRecentPictureKey];
    //[picker setValue:[NSNumber numberWithBool:NO] forKey:IKImagePickerAllowsEditingKey];
    //[picker setValue:[NSString stringWithString:@"Drop an Image Here"] forKey:IKImagePickerInformationalTextKey];
    //[picker setValue:[NSValue valueWithSize:NSMakeSize(256,256)] forKey:IKImagePickerOutputImageMaxSizeKey];
    //[picker setValue:[NSValue valueWithSize:NSMakeSize(100, 100)] forKey:IKImagePickerCropAreaSizeKey];
}

- (void) launchImagePicker:(id)sender
{
    /* retrieve the imagePicker shared instance */
    IKImagePicker *picker = [IKImagePicker imagePicker];

    /* configure the image picker to show effects */
    [picker setValue:[NSNumber numberWithBool:YES] forKey:IKImagePickerShowEffectsKey];

    /* launch the imagePicker as a panel */
    [picker beginImagePickerWithDelegate:self didEndSelector:@selector(imagePickerValidated:code:contextInfo:) contextInfo:nil];
}

#pragma mark -
#pragma mark delegate

- (void) imagePickerValidated:(IKImagePicker*) imagePicker code:(int) returnCode contextInfo:(void*) ctxInf
{
    if(returnCode == NSOKButton){
        /* retrieve the output image */
        NSImage *outputImage = [imagePicker outputImage];

        /* change the displayed image */
        [_imageView setImage:outputImage];
    }
    else{
        /* the user canceled => nothing to do here */
    }
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](MyController.h.md)


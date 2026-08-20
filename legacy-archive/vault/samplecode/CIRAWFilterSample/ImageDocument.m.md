---
title: CIRAWFilterSample
apple_id: DTS40009217
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2009-09-08'
source_url: https://developer.apple.com/library/archive/samplecode/CIRAWFilterSample/Listings/ImageDocument_m.html
archived_at: '2026-07-18T03:02:40.601116Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CIRAWFilterSample](CIRAWFilterSample.md)


[Next](ImageDocumentController.h.md)[Previous](ImageDocument.h.md)

# ImageDocument.m

```objc
/*

 @file ImageDocument.m

 @abstract Represents an opening image document. Handles open / save.

 @version 1.1

 ©  Copyright 2006-2009 Apple, Inc. All rights reserved.

 IMPORTANT: This Apple software is supplied to you by Apple Computer,
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms,
 and subject to these terms, Apple grants you a personal,
 non-exclusive license, under Apple's copyrights in this original
 Apple software (the "Apple Software"), to use, reproduce, modify and
 redistribute the Apple Software, with or without modifications, in
 source and/or binary forms; provided that if you redistribute the
 Apple Software in its entirety and without modifications, you must
 retain this notice and the following text and disclaimers in all such
 redistributions of the Apple Software.  Neither the name, trademarks,
 service marks or logos of Apple Computer, Inc. may be used to endorse
 or promote products derived from the Apple Software without specific
 prior written permission from Apple.  Except as expressly stated in
 this notice, no other rights or licenses, express or implied, are
 granted by Apple herein, including but not limited to any patent
 rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND
 FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS
 USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT,
 INCIDENTAL OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE,
 REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE,
 HOWEVER CAUSED AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING
 NEGLIGENCE), STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN
 ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

 */

#import "ImageDocument.h"

#import <QuartzCore/QuartzCore.h>
#import <QuartzCore/CIRAWFilter.h>
#import <Quartz/Quartz.h>
#import <libkern/OSAtomic.h>

#import "ImageView.h"
#import "ImageWindowController.h"
#import "CIFilter+Additions.h"

@interface ImageDocument ( Private )

/*! Creates a CIRawFilter for the image at the given URL. */
- (BOOL)setupRawFilterForURL:(NSURL *)imageURL;

/*! ImageIO needs a CGImage for saving. This method creates a fullsize CGImage from our CIImage with the same settings as what the user sees on-screen. */
- (CGImageRef)renderedImage;

/*! Returns an sRGB color space. We need this profile for export. */
+ (CGColorSpaceRef)sharedSRGBColorSpace;

/*! Links the outputs to the inputs in the stack of CIFilters. */
- (void)linkAllFilters;

/*! Updates the NSObjectController content to be the last filter in the stack of CIFilters. */
- (void)updateFilterControllerContent;

@end

@implementation ImageDocument

- (id)init
{
    self = [super init];
    if (self != nil) {
        filters = [[NSMutableArray alloc] init];
    }
    return self;
}

- (void) dealloc
{
    [saveOptions release], saveOptions = nil;
    [rawFilter release], rawFilter = nil;
    [filters release], filters = nil;
    [outputFilterController release], outputFilterController = nil;
    [super dealloc];
}


- (void)makeWindowControllers
{
    ImageWindowController *controller = [[[ImageWindowController alloc] init] autorelease];
    [self addWindowController:controller];
}

- (BOOL)readFromURL:(NSURL *)absoluteURL ofType:(NSString *)typeName error:(NSError **)outError
{
    return [self setupRawFilterForURL:absoluteURL];
}

- (BOOL)prepareSavePanel:(NSSavePanel *)savePanel
{
    // Here we let ImageKit take care of the output format switching. 
    // Note that the shown implementation doesn't support PDF, 
    // even if the user chooses PDF from the popup.
    NSString * extension = (NSString *) UTTypeCopyPreferredTagWithClass((CFStringRef)[self fileType], kUTTagClassFilenameExtension);
    [extension autorelease];
    [savePanel setRequiredFileType: extension];

    if (saveOptions == nil) {
        saveOptions = [[IKSaveOptions alloc] initWithImageProperties:[NSDictionary dictionary]
                                                         imageUTType:[self fileType]];
    }

    [saveOptions addSaveOptionsAccessoryViewToSavePanel:savePanel];
    [savePanel setDelegate:self];

    return YES;
}

- (BOOL)writeToURL:(NSURL *)absoluteURL ofType:(NSString *)typeName error:(NSError **)outError
{
    // note that this sample does not support saving as PDF.
    BOOL success = NO;

    NSDictionary *saveAsOptions = [saveOptions userSelection];
    NSString *saveAsDocumentType = [saveAsOptions objectForKey:@"documentType"];

    CGImageRef image = [self renderedImage];
    if (image != NULL)
    {
        // This dictionary has been initialized by ImageKit by running the SavePanel
        CGImageDestinationRef destination = CGImageDestinationCreateWithURL((CFURLRef) absoluteURL, (CFStringRef)saveAsDocumentType, 1, NULL);
        CFMakeCollectable(destination);
        if (destination != NULL)
        {
            CFDictionaryRef imageProperties = (CFDictionaryRef) [saveOptions imageProperties];
            CGImageDestinationAddImage(destination, image, (CFDictionaryRef) imageProperties);
            success = CGImageDestinationFinalize(destination);
        }
        CGImageRelease(image);
    }
    return success;
}

@synthesize rawFilter;

- (CIImage *)outputImage
{
    return [outputFilterController valueForKeyPath:@"content.outputImage"];
}

- (NSObjectController *)outputFilterController
{
    return outputFilterController;
}

- (NSMutableArray *)filters
{
    return filters;
}

- (void)setFilters:(NSMutableArray *)newFilters
{
    if (newFilters != filters)
        filters = [[NSMutableArray alloc] initWithArray:newFilters];
    [self linkAllFilters];
    [self updateFilterControllerContent];
}

- (void)insertObject:(NSObject *)newFilter inFiltersAtIndex:(NSUInteger)index
{
    [filters insertObject:newFilter atIndex:index];
    [self linkAllFilters];
    if (index == ([filters count] - 1))
        [self updateFilterControllerContent];
}

- (void)removeObjectFromFiltersAtIndex:(NSUInteger)index
{
    // We need to unbind the filter, that is going to be removed:
    CIFilter *oldFilter = [[[filters objectAtIndex:index] retain] autorelease];
    [oldFilter unbindImageInputs];
    [filters removeObjectAtIndex:index];
    [self linkAllFilters];
    if (index >= [filters count])
    {
        [self linkAllFilters];
        [self updateFilterControllerContent];
    }
}

@end

@implementation ImageDocument ( Private )

- (BOOL)setupRawFilterForURL:(NSURL *)imageURL
{
    CIFilter *newFilter = [CIFilter filterWithImageURL:imageURL options:[NSDictionary dictionary]];
    [self setRawFilter:newFilter];

    [outputFilterController release], outputFilterController = nil;
    outputFilterController = [[NSObjectController alloc] init];
    [outputFilterController setObjectClass:[CIFilter class]];
    [outputFilterController setAutomaticallyPreparesContent:NO];
    [outputFilterController setContent:[self rawFilter]];

    return ([self rawFilter] != nil);
}

- (CGImageRef)renderedImage
{
    CGImageRef resultingImage = NULL;

    CIImage *ciImage = nil;
    {
        NSNumber *originalScale = [rawFilter valueForKey:kCIInputScaleFactorKey];
        [rawFilter setValue:[NSNumber numberWithDouble:1.f] forKey:kCIInputScaleFactorKey];
        ciImage = [self outputImage];
        [rawFilter setValue:originalScale forKey:kCIInputScaleFactorKey];
    }

    CGSize const size = [ciImage extent].size;
    CGFloat const imageWidth = size.width;
    CGFloat const imageHeight = size.height;

    if ((imageHeight <= 0) || (imageWidth <= 0))
        return NULL;

    {
        // In this particular case, we export the image in sRGB color space. It's up to the application to let the user choose the destination profile. Similarly, we are creating an 8-bit target bitmap. Other depths, including float, are conceivable.
        NSInteger const bitsPerComponent = 8;
        NSInteger const bytesPerPixel = 4;
        size_t const bytesPerRow = imageWidth * bytesPerPixel;
        void * const data = [[NSMutableData dataWithLength:(bytesPerRow * imageHeight)] mutableBytes];
        if (data == NULL)
            return NULL;
        CGColorSpaceRef colorSpace = [[self class] sharedSRGBColorSpace];
        CGContextRef cgBitmapContext = CGBitmapContextCreate(data, imageWidth, imageHeight, bitsPerComponent, bytesPerRow, colorSpace, kCGImageAlphaNoneSkipFirst);

        CIContext *context = [CIContext contextWithCGContext:cgBitmapContext options:nil];
        CGRect inRect = CGRectMake(0, 0, imageWidth, imageHeight);
        [context drawImage:ciImage inRect:inRect fromRect:[ciImage extent]];
        CGContextFlush(cgBitmapContext);

        resultingImage = CGBitmapContextCreateImage(cgBitmapContext);
        CGContextRelease(cgBitmapContext);

    }
    return resultingImage;
}

+ (CGColorSpaceRef)sharedSRGBColorSpace;
{
    static CGColorSpaceRef sRGB = NULL;
    if (sRGB == NULL)
    {
        CMProfileRef profref;
        CMGetDefaultProfileBySpace('sRGB', &profref);
        CGColorSpaceRef newColorSpace = CGColorSpaceCreateWithPlatformColorSpace(profref);
        if (!OSAtomicCompareAndSwapPtrBarrier(NULL, newColorSpace, (void **) &sRGB)) {
            CFRelease(newColorSpace);
        }
    }
    return sRGB;
}

- (void)linkAllFilters
{
    NSMutableArray *filterStack = [NSMutableArray arrayWithObject:rawFilter];
    [filterStack addObjectsFromArray:filters];

    CIFilter *inputFilter = nil;
    for (CIFilter *outputFilter in filterStack)
    {
        if (inputFilter != nil)
        {
            [outputFilter bindImageInputsToFilter:inputFilter];
        }
        inputFilter = outputFilter;
    }
}

- (void)updateFilterControllerContent
{
    CIFilter *lastFilter = [filters lastObject];
    if (lastFilter == nil)
    {
        lastFilter = rawFilter;
    }
    [[self outputFilterController] setContent:lastFilter];
}

@end
```

[Next](ImageDocumentController.h.md)[Previous](ImageDocument.h.md)


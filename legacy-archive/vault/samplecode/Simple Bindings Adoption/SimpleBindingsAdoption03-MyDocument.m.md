---
title: Simple Bindings Adoption
apple_id: DTS10004326
resource_type: Sample Code
platform: macOS
topic: General
technology: null
published: '2014-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleBindingsAdoption/Listings/SimpleBindingsAdoption_03_MyDocument_m.html
archived_at: '2026-07-18T03:23:54.439195Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simple Bindings Adoption](Simple%20Bindings%20Adoption.md)


[Next](SimpleBindingsAdoption03-Track.h.md)[Previous](SimpleBindingsAdoption03-MyDocument.h.md)

# SimpleBindingsAdoption_03/MyDocument.m

```objc
/*
     File: MyDocument.m
 Abstract: A document class to manage a single track object.

  Version: 1.1

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

#import "MyDocument.h"
#import "Track.h"

@implementation MyDocument

/*
 sets track's volume to 0
 */
- (IBAction)muteTrack:(id)sender
{
    self.track.volume = 0.0;
}


#pragma mark - methods common to all implementations

/*
 * These methods are the same for all implementations
 */

/*
 standard init method
 creates an instance of Track and sets its volume to 5.0
 */
- (id)init
{
    self = [super init];
    if (self != nil)
    {
        _track = [[Track alloc] init];
        self.track.volume = 5.0;
    }
    return self;    
}

/*
 NSDocument method to return the name of the nib file for the document
 */
- (NSString *)windowNibName
{
    return @"MyDocument";
}


#pragma mark - Read and Write

/*
 Insert code here to read your document from the given data of the specified type.
 */
- (BOOL)readFromData:(NSData *)data ofType:(NSString *)typeName error:(NSError **)outError
{
    self.track.volume = *(float *)[data bytes];

    return YES;
}

/*
 Insert code here to write your document to data of the specified type.
 */
- (NSData *)dataOfType:(NSString *)typeName error:(NSError **)outError
{
    float volume = self.track.volume;
    return [NSData dataWithBytes:&volume length:sizeof(float)];
}

@end
```

[Next](SimpleBindingsAdoption03-Track.h.md)[Previous](SimpleBindingsAdoption03-MyDocument.h.md)


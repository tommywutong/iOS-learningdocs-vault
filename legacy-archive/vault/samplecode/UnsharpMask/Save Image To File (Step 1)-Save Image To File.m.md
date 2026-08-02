---
title: UnsharpMask
apple_id: DTS10003724
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: Automator
published: '2005-06-06'
source_url: https://developer.apple.com/library/archive/samplecode/UnsharpMask/Listings/Save_Image_To_File__Step_1__Save_Image_To_File_m.html
archived_at: '2026-07-18T03:27:35.703998Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [UnsharpMask](UnsharpMask.md)


[Next](Save%20Image%20To%20File%20%28Step%202%29-Save%20Image%20To%20File.h.md)[Previous](Save%20Image%20To%20File%20%28Step%201%29-Save%20Image%20To%20File.h.md)

# Save Image To File (Step 1)/Save Image To File.m

```objc

#import "Save Image To File.h"
#import <ExtendedCoreImage/ExtendedCoreImage.h>

@implementation SaveImageToFile

- (id)runWithInput:(id)input fromAction:(AMAction *)anAction error:(NSDictionary **)errorInfo
{
    // Add your code here, returning the data to be passed to the next action.

    return input;
}

@end

/*
 Save Image To File.m
 Save Image To File

 Copyright (c) 2005, Apple Computer, Inc., all rights reserved.

 IMPORTANT:  This Apple software is supplied to you by Apple Computer, Inc. ("Apple") in
 consideration of your agreement to the following terms, and your use, installation, 
 modification or redistribution of this Apple software constitutes acceptance of these 
 terms.  If you do not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and subject to these 
 terms, Apple grants you a personal, non-exclusive license, under Apple’s copyrights in 
 this original Apple software (the "Apple Software"), to use, reproduce, modify and 
 redistribute the Apple Software, with or without modifications, in source and/or binary 
 forms; provided that if you redistribute the Apple Software in its entirety and without 
 modifications, you must retain this notice and the following text and disclaimers in all 
 such redistributions of the Apple Software.  Neither the name, trademarks, service marks 
 or logos of Apple Computer, Inc. may be used to endorse or promote products derived from 
 the Apple Software without specific prior written permission from Apple. Except as expressly
 stated in this notice, no other rights or licenses, express or implied, are granted by Apple
 herein, including but not limited to any patent rights that may be infringed by your 
 derivative works or by other works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO WARRANTIES, 
 EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, 
 MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS 
 USE AND OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR CONSEQUENTIAL 
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS 
 OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, 
 REPRODUCTION, MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND 
 WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE), STRICT LIABILITY OR 
 OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
```

[Next](Save%20Image%20To%20File%20%28Step%202%29-Save%20Image%20To%20File.h.md)[Previous](Save%20Image%20To%20File%20%28Step%201%29-Save%20Image%20To%20File.h.md)


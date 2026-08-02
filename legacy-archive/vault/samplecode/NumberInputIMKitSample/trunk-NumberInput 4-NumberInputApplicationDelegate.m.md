---
title: NumberInput_IMKit_Sample
apple_id: DTS40007466
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: InputMethodKit
published: '2008-03-17'
source_url: https://developer.apple.com/library/archive/samplecode/NumberInput_IMKit_Sample/Listings/trunk_NumberInput_4_NumberInputApplicationDelegate_m.html
archived_at: '2026-07-18T03:17:08.962196Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NumberInput_IMKit_Sample](NumberInputIMKitSample.md)


[Next](trunk-NumberInput%204-NumberInputController.h.md)[Previous](trunk-NumberInput%204-NumberInputApplicationDelegate.h.md)

# trunk/NumberInput 4/NumberInputApplicationDelegate.m

```objc
/*

File:NumberInputApplicationDelegate.m

Abstract: The input method's application delegate object.

Version: 1.0

Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
Apple Inc. ("Apple") in consideration of your agreement to the
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
Neither the name, trademarks, service marks or logos of Apple Inc. 
may be used to endorse or promote products derived from the Apple
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

Copyright (C) 2007 Apple Inc. All Rights Reserved.

*/
#import "NumberInputApplicationDelegate.h"


@implementation NumberInputApplicationDelegate

-(ConversionEngine*)conversionEngine
{
    return _conversionEngine;
}


//this method is added so that our controllers can access the shared NSMenu.
-(NSMenu*)menu
{
    return _menu;
}


//add an awakeFromNib item so that we can set the action method.  Note that any menuItems without an action will be disabled when
//displayed in the Text Input Menud.
-(void)awakeFromNib
{
    NSMenuItem*     preferences = [_menu itemWithTag:1];

    if ( preferences ) {
        [preferences setAction:@selector(showPreferences:)];
    }

}

@end
```

[Next](trunk-NumberInput%204-NumberInputController.h.md)[Previous](trunk-NumberInput%204-NumberInputApplicationDelegate.h.md)


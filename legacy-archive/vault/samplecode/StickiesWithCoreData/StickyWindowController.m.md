---
title: StickiesWithCoreData
apple_id: DTS40009052
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_StickiesWithCoreData/Listings/StickyWindowController_m.html
archived_at: '2026-07-18T03:25:55.881381Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [StickiesWithCoreData](StickiesWithCoreData.md)


[Next](Document%20Revision%20History.md)[Previous](StickyWindowController.h.md)

# StickyWindowController.m

```objc
/*

 File: StickyWindowController.m

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

 Copyright © 2005-2009 Apple Computer, Inc., All Rights Reserved.

 */

#import "StickyWindowController.h"
#import "StickyTitleBarView.h"
#import "Sticky.h"
#import "AppDelegate.h"


@interface StickyWindowController (ForwardDeclarations)
- (void)startObserving;
- (void)stopObserving;
@end


@implementation StickyWindowController

- (id)initWithSticky:(Sticky *)sticky
{
    _sticky = [sticky retain];
    return [super initWithWindowNibName:@"Sticky"];
}

- (void)dealloc
{
    [self stopObserving];
    [_sticky release];
    [super dealloc];
}

- (Sticky *)sticky
{
    return _sticky;
}



#pragma mark

- (void)updateStickyFrame
{
    if (!_isUpdatingWindowFrame) {
        NSRect oldFrame = [[self window] frame];
        [_sticky setValue:[NSNumber numberWithInteger:oldFrame.origin.x] forKey:@"originX"];
        [_sticky setValue:[NSNumber numberWithInteger:oldFrame.origin.y] forKey:@"originY"];
        [_sticky setValue:[NSNumber numberWithInteger:oldFrame.size.width] forKey:@"width"];
        [_sticky setValue:[NSNumber numberWithInteger:oldFrame.size.height] forKey:@"height"];
    }
}

- (void)updateWindowFrame
{
    if (nil == [_sticky valueForKey:@"originX"] || nil == [_sticky valueForKey:@"originY"] || nil == [_sticky valueForKey:@"width"] || nil == [_sticky valueForKey:@"height"]) {
        // Must be a new sticky so set the frame using the nib values
        [self updateStickyFrame];
    } else {
        NSInteger origin_x = [[_sticky valueForKey:@"originX"] integerValue];
        NSInteger origin_y = [[_sticky valueForKey:@"originY"] integerValue];
        NSInteger width = [[_sticky valueForKey:@"width"] integerValue];
        NSInteger height = [[_sticky valueForKey:@"height"] integerValue];

        // This will trigger my windowDidMove:/windowDidResize: callback and I want to avoid re-updating the sticky frame
        _isUpdatingWindowFrame = YES;
        [[self window] setFrame:NSMakeRect(origin_x, origin_y, width, height) display:YES];
        _isUpdatingWindowFrame = NO;
    }
}

- (void)updateWindowColor
{
    NSData *colorData = [_sticky valueForKey:@"color"];
    if (nil == colorData) {
        // Must be a new sticky so set the color value using the version in the nib
        [_sticky setValue:[NSArchiver archivedDataWithRootObject:[contents backgroundColor]] forKey:@"color"];
        [titleBar setBackgroundColor:[contents backgroundColor]];

    } else {
        // Set the
        NSColor *aColor = [NSUnarchiver unarchiveObjectWithData:colorData];
        if ((aColor != nil) && [aColor isKindOfClass:[NSColor class]]){
            [titleBar setBackgroundColor:aColor];
            [contents setBackgroundColor:aColor];
        }
    }
}

- (void)updateWindowTranslucency
{
    if (nil == [_sticky valueForKey:@"translucent"]) {
        // Must be a new sticky so set the translucent value to my default
        [_sticky setValue:[NSNumber numberWithBool:NO] forKey:@"translucent"];
    } else {
        if ([[_sticky valueForKey:@"translucent"] boolValue] == YES) {
            [[self window] setAlphaValue:0.5];
        } else {
            [[self window] setAlphaValue:1.0];
        }
    }
}






#pragma mark

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    // There are no built-in bindings for these values so I have to maintain them myself
    if ([@"originX" isEqualToString:keyPath] || [@"originY" isEqualToString:keyPath] ||[@"width" isEqualToString:keyPath] || [@"height" isEqualToString:keyPath]) {
        [self updateWindowFrame];

    } else if ([@"color" isEqualToString:keyPath]) {
        [self updateWindowColor];

    } else if ([@"translucent" isEqualToString:keyPath]) {
        [self updateWindowTranslucency];
    }
}

- (void)startObserving
{
    // Register for KVO on the sticky's frame rect so that the window will redraw if we change the frame
    [_sticky addObserver:self forKeyPath:@"originX" options:NSKeyValueObservingOptionNew context:NULL];    
    [_sticky addObserver:self forKeyPath:@"originY" options:NSKeyValueObservingOptionNew context:NULL];    
    [_sticky addObserver:self forKeyPath:@"width" options:NSKeyValueObservingOptionNew context:NULL];    
    [_sticky addObserver:self forKeyPath:@"height" options:NSKeyValueObservingOptionNew context:NULL];

    // Track changes to the colour and translucency
    [_sticky addObserver:self forKeyPath:@"color" options:NSKeyValueObservingOptionNew context:NULL];    
    [_sticky addObserver:self forKeyPath:@"translucent" options:NSKeyValueObservingOptionNew context:NULL];    
}

- (void)stopObserving
{
    [_sticky removeObserver:self forKeyPath:@"originX"];    
    [_sticky removeObserver:self forKeyPath:@"originY"];    
    [_sticky removeObserver:self forKeyPath:@"width"];    
    [_sticky removeObserver:self forKeyPath:@"height"];
    [_sticky removeObserver:self forKeyPath:@"color"];    
    [_sticky removeObserver:self forKeyPath:@"translucent"];    
}




#pragma mark

- (void)windowDidMove:(NSNotification *)aNotification
{
    [self updateStickyFrame];
}

- (void)windowDidResize:(NSNotification *)aNotification 
{
    [self updateStickyFrame];
}

- (void)windowWillClose:(NSNotification *)notification;
{
    // Closing the window => delete the sticky
    [[NSApp delegate] removeSticky:_sticky];
    [self stopObserving];
    [_sticky release];
    _sticky = nil;
}

- (void)windowDidLoad
{
    [super windowDidLoad];
    [self setShouldCascadeWindows:NO];

    // Make sure the sticky has a text value, otherwise we can't save it
    if (nil == [_sticky valueForKey:@"text"]) {
        NSAttributedString *string = [[NSAttributedString alloc] initWithString:@"My fancy sticky!"];
        [_sticky setValue:[NSArchiver archivedDataWithRootObject:string] forKey:@"text"];
    }        

    [self updateWindowColor];
    [self updateWindowTranslucency];
    [self updateWindowFrame];

    [self startObserving];
}


@end
```

[Next](Document%20Revision%20History.md)[Previous](StickyWindowController.h.md)


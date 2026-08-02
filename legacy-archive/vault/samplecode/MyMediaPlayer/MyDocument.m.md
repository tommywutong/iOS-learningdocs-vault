---
title: MyMediaPlayer
apple_id: DTS40009203
resource_type: Sample Code
platform: macOS
topic: null
technology: QTKit
published: '2011-09-12'
source_url: https://developer.apple.com/library/archive/samplecode/MyMediaPlayer/Listings/MyDocument_m.html
archived_at: '2026-07-18T03:16:39.026701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MyMediaPlayer](MyMediaPlayer.md)


[Next](Document%20Revision%20History.md)[Previous](MyDocument.h.md)

# MyDocument.m

```objc
/*

File: MyDocument.m

Abstract: A NSDocument subclass that implements a fullscreen movie player.

Version: 2.0

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

Copyright (C) 2009 Apple Inc. All Rights Reserved.

*/

#import "MyDocument.h"
#import "FullScreenWindow.h"
#import "FullScreenOverlayWindowController.h"

#import <QTKit/QTKit.h>

@interface MyDocument ()
- (void)handleLoadStateChanged;
- (void)updateMovieRate;
@property(getter=isFullscreen) BOOL fullscreen;
- (void)repositionOverlayWindow;
@end

@implementation MyDocument

- (void)dealloc 
{
    // Note that we must not be in fullscreen mode when entering this method, for a variety of reasons
    // We take care of that in -close below
    NSNotificationCenter *nc = [NSNotificationCenter defaultCenter];
    [nc removeObserver:self name:QTMovieLoadStateDidChangeNotification object:mMovie];
    [nc removeObserver:self name:QTMovieRateDidChangeNotification object:mMovie];

    [mMovie release];
    [mFullscreenWindowController release];
    [mFullscreenOverlayWindowController release];
    [mFullscreenScreen release];

    [super dealloc];
}

#pragma mark NSDocument overrides

- (void)close
{
    [self setFullscreen:NO];

    [super close];
}

// Initially, we have only one window.  This may change if we enter fullscreen.
- (NSString *)windowNibName 
{
    return @"MyDocument";
}

- (void)windowControllerDidLoadNib:(NSWindowController *)windowController
{
    // set the play button to not change its title when it's highlighted
    NSButtonCell *playPauseButtonCell = (NSButtonCell *)[playPauseButton cell];
    if ([playPauseButtonCell isKindOfClass:[NSButtonCell class]])
        [playPauseButtonCell setHighlightsBy:([playPauseButtonCell highlightsBy] & ~NSContentsCellMask)];
}

- (BOOL)readFromURL:(NSURL *)absoluteURL ofType:(NSString *)typeName error:(NSError **)outError 
{
    NSDictionary *attrs = [NSDictionary dictionaryWithObjectsAndKeys: 
                           absoluteURL, QTMovieURLAttribute, 
                           /* Set the QTMovieOpenForPlaybackAttribute attribute to indicate that you intend to use movie playback methods (such as -play or -stop, 
                            or corresponding movie view methods such as -play: or -pause:) to control the movie, but do not intend to use other methods that edit,
                            export, or in any way modify the movie. Knowing that you need playback services only may allow QTMovie to use more efficient code paths
                            for some media files. */
                           [NSNumber numberWithBool:YES], QTMovieOpenForPlaybackAttribute ,
                           /* Set the QTMovieOpenAsyncRequiredAttribute attribute to indicate that all operations necessary to open the movie file (or other container)
                            and create a valid QTMovie object must occur asynchronously. That is to say, the methods +movieWithAttributes:error: and -initWithAttributes:error: 
                            must return almost immediately, performing any lengthy operations on another thread. Your application can monitor the movie load state to 
                            determine the progress of those operations.*/
                           [NSNumber numberWithBool:YES], QTMovieOpenAsyncRequiredAttribute,
                           nil]; 

    [self willChangeValueForKey:@"movie"];
    mMovie = [[QTMovie alloc] initWithAttributes:attrs error:outError];
    [self didChangeValueForKey:@"movie"];

    if (mMovie) {       
        // Register to receive movie load state and rate change notifications
        NSNotificationCenter *nc = [NSNotificationCenter defaultCenter];
        [nc addObserver:self
               selector:@selector(movieLoadStateChanged:) 
                   name:QTMovieLoadStateDidChangeNotification 
                 object:mMovie];
        [nc addObserver:self
               selector:@selector(movieRateChanged:) 
                   name:QTMovieRateDidChangeNotification 
                 object:mMovie];

        // Check movie load state immediately in case the movie is available already
        [self handleLoadStateChanged];
    }

    return (mMovie != nil);
}

- (NSWindow *)windowForSheet
{
    return [self isFullscreen] ? [mFullscreenWindowController window] : [super windowForSheet];
}

#pragma mark Movie

@synthesize movie = mMovie;

- (void)movieLoadStateChanged:(NSNotification *)notification 
{
    [self handleLoadStateChanged];
}

- (void)movieRateChanged:(NSNotification *)notification
{
    [self updateMovieRate];
}

- (void)handleLoadStateChanged
{
    QTMovie *movie = [self movie];
    QTMovieLoadState loadState = [[movie attributeForKey:QTMovieLoadStateAttribute] integerValue];

    /*
     The QuickTime movie load states are defined as follows (see QTMovie.h):

     QTMovieLoadStateError              = -1L,          // an error occurred while loading the movie
     QTMovieLoadStateLoading            = 1000,         // the movie is loading
     QTMovieLoadStateLoaded             = 2000,         // the movie atom has loaded; it's safe to query movie properties
     QTMovieLoadStatePlayable           = 10000,        // the movie has loaded enough media data to begin playing
     QTMovieLoadStatePlaythroughOK      = 20000,        // the movie has loaded enough media data to play through to the end
     QTMovieLoadStateComplete           = 100000L       // the movie has loaded completely

     */

    if (loadState == QTMovieLoadStateError) {
        // What goes here is app-specific:
        // You can query QTMovieLoadStateErrorAttribute to get the error code, if it matters
        // If the movie failed to open because it was instantiated with QTMovieOpenAsyncRequiredAttribute and it cannot be opened asynchronously, you can try again without that attribute if you require a movie object.
        // You might also need to undo some operations done in the other state handlers

        // In this case, we just put up an error dialog and close ourselves (in -loadStateErrorSheetDidEnd:)
        NSError *err = [movie attributeForKey:QTMovieLoadStateErrorAttribute];
        [self presentError:err modalForWindow:[self windowForSheet] delegate:self didPresentSelector:@selector(loadStateErrorSheetDidEnd:returnCode:contextInfo:) contextInfo:NULL];
    }

    if (loadState >= QTMovieLoadStateLoaded) {
        // Can query properties here
        // For instance, if you need to size a QTMovieView based on the movie's natural size, you can do so now

        QTTime duration = [movie duration];
        [durationTextField setStringValue:QTStringFromTime(duration)];
    }

    if (loadState >= QTMovieLoadStatePlayable) {
        // Can start movie playing here, if appropriate

        [movie setRate:mMovieRate];
    }
}

- (void)loadStateErrorSheetDidEnd:(NSAlert *)alert returnCode:(NSInteger)returnCode contextInfo:(void *)contextInfo
{
    [self close];
}

@dynamic movieIsPlaying;
- (BOOL)movieIsPlaying
{
    return (mMovieRate != 0.f);
}

- (void)setMovieIsPlaying:(BOOL)movieIsPlaying
{
    QTMovie *movie = [self movie];

    // Cache the desired rate in case the movie is not yet playable
    // If that is the case, we update the movie's rate in -handleLoadStateChanged
    mMovieRate = movieIsPlaying ? 1.f : 0.f;

    QTMovieLoadState loadState = [[movie attributeForKey:QTMovieLoadStateAttribute] integerValue];
    if (loadState >= QTMovieLoadStatePlayable)
        [movie setRate:mMovieRate];
}

+ (BOOL)automaticallyNotifiesObserversForMovieIsPlaying
{
    // setMovieIsPlaying: does not need to automatically notify key value observers because
    // the value returned by movieIsPlaying is actually updated in updateMovieRate
    return NO;
}

- (void)updateMovieRate
{
    QTMovie *movie = [self movie];

    [self willChangeValueForKey:@"movieIsPlaying"];
    mMovieRate = [movie rate];
    [self didChangeValueForKey:@"movieIsPlaying"];  
}

#pragma mark Fullscreen

@synthesize fullscreen = mFullscreen;

- (void)setFullscreen:(BOOL)isFullscreen
{
    NSNotificationCenter *nc = [NSNotificationCenter defaultCenter];

    if (isFullscreen == mFullscreen)
        return;

    mFullscreen = isFullscreen;

    if (mFullscreen) {
        // Since we want to ensure that in fullscreen mode we always cover exactly the area of a single screen, register for screen config notifications
        [nc addObserver:self selector:@selector(screenParametersDidChange:) name:NSApplicationDidChangeScreenParametersNotification object:NSApp];

        mFullscreenScreen = [[movieWindow screen] retain];
        NSRect screenRect = [mFullscreenScreen frame];

        // Create a window to cover the screen
        FullScreenWindow *fullscreenWindow = [[[FullScreenWindow alloc] initWithContentRect:screenRect
                                                                                  styleMask:NSBorderlessWindowMask
                                                                                    backing:NSBackingStoreBuffered
                                                                                      defer:NO]
                                              autorelease];
        [fullscreenWindow setBackgroundColor:[NSColor blackColor]];

        // Create window controllers for the fullscreen window and control overlay window
        mFullscreenWindowController = [[NSWindowController alloc] initWithWindow:fullscreenWindow];
        [self addWindowController:mFullscreenWindowController];
        mFullscreenOverlayWindowController = [[FullScreenOverlayWindowController alloc] init];
        [self addWindowController:mFullscreenOverlayWindowController];

        [fullscreenWindow addChildWindow:[mFullscreenOverlayWindowController window] ordered:NSWindowAbove];

        [self repositionOverlayWindow];

        // Move the movie view into fullscreen
        [[movieView retain] autorelease];  // in case the superview has the only retain
        [movieView removeFromSuperviewWithoutNeedingDisplay];
        [[fullscreenWindow contentView] addSubview:movieView];
        mSavedMovieViewRect = [movieView frame]; // remember the current rect/size
        [movieView setFrame:[[fullscreenWindow contentView] bounds]];

        // Bring the fullscreen and overlay windows to the front
        [movieWindow orderOut:self];
        [mFullscreenOverlayWindowController showWindow:self];
        [mFullscreenWindowController showWindow:self];

        // Hide the dock and menu bar, saving previous presentation options
        mSavedPresentationOptions = [NSApp presentationOptions];
        [NSApp setPresentationOptions:(NSApplicationPresentationAutoHideDock | NSApplicationPresentationAutoHideMenuBar)];
    } else {
        [nc removeObserver:self name:NSApplicationDidChangeScreenParametersNotification object:NSApp];
        [mFullscreenScreen release];
        mFullscreenScreen = nil;

        // Move movie view back to the main document window
        [[movieView retain] autorelease];  // in case the superview has the only retain
        [movieView removeFromSuperviewWithoutNeedingDisplay];
        [movieView setFrame:mSavedMovieViewRect];
        [[movieWindow contentView] addSubview:movieView];

        // Get rid of the fullscreen windows
        [mFullscreenWindowController close];
        [mFullscreenWindowController release];
        mFullscreenWindowController = nil;

        [mFullscreenOverlayWindowController close];
        [mFullscreenOverlayWindowController release];
        mFullscreenOverlayWindowController = nil;

        // Bring the main movie window back to the front
        [movieWindow makeKeyAndOrderFront:self];

        // Restore previous presentation options
        [NSApp setPresentationOptions:mSavedPresentationOptions];
    }   
}

- (IBAction)toggleFullscreen:(id)sender 
{
    [self setFullscreen:![self isFullscreen]];
}

- (void)screenParametersDidChange:(NSNotification *)notification
{
    if ([[NSScreen screens] containsObject:mFullscreenScreen]) {
        // The screen is still there, but may have changed resolution

        NSWindow *fullscreenWindow = [mFullscreenWindowController window];
        NSRect screenRect = [mFullscreenScreen frame];
        if (!NSEqualRects([fullscreenWindow frame], screenRect)) {
            [fullscreenWindow setFrame:screenRect display:YES];
            [self repositionOverlayWindow];
        }
    } else {
        // That other screen is gone now.  Our best bet is just to break out of fullscreen mode.
        [self setFullscreen:NO];
    }
}

- (void)repositionOverlayWindow
{
    NSRect fullscreenRect = [[mFullscreenWindowController window] frame];
    NSWindow *overlayWindow = [mFullscreenOverlayWindowController window];
    NSRect overlayRect = [overlayWindow frame];
    [overlayWindow setFrameOrigin:NSMakePoint(NSMinX(fullscreenRect) + ((0.5f * NSWidth(fullscreenRect)) - (0.5f * NSWidth(overlayRect))), 0.15f * NSHeight(fullscreenRect))];  
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](MyDocument.h.md)


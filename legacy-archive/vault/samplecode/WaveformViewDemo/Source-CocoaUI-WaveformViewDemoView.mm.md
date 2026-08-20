---
title: WaveformViewDemo
apple_id: DTS40008653
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/WaveformViewDemo/Listings/Source_CocoaUI_WaveformViewDemoView_mm.html
archived_at: '2026-07-18T03:28:09.294716Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WaveformViewDemo](WaveformViewDemo.md)


[Next](Source-CocoaUI-WaveformViewDemoViewFactory.h.md)[Previous](Source-CocoaUI-WaveformViewDemoView.h.md)

# Source/CocoaUI/WaveformViewDemoView.mm

```objc
/*  Copyright © 2007 Apple Inc. All Rights Reserved.

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
*/
#import "WaveformViewDemoView.h"
#import "WaveformViewDemo.h"


#pragma mark ____ LISTENER CALLBACK DISPATCHER ____



// This listener responds to parameter changes, gestures, and property notifications
void EventListenerDispatcher (void *inRefCon, void *inObject, const AudioUnitEvent *inEvent, UInt64 inHostTime, Float32 inValue)
{
    WaveformViewDemoView *SELF = (WaveformViewDemoView *)inRefCon;
    [SELF priv_eventListener:inObject event: inEvent value: inValue];
}

@implementation WaveformViewDemoView
#pragma mark ____ (INIT /) DEALLOC ____
- (void)dealloc {

    [self priv_removeListeners];

    if (mData) {
        free(mData);
        mData = NULL;
    }

    mAU = NULL;

    [super dealloc];
}

- (void) removeFromSuperview
{
    [mFetchTimer invalidate];
    //[[NSNotificationCenter defaultCenter] removeObserver: self];

    [super removeFromSuperview];
}

#pragma mark ____ PRIVATE FUNCTIONS ____


- (void) priv_initBuffers
{
    mData =(WaveformOverview*) malloc(sizeof(WaveformOverview) + (kMaxWaveformSamples-1)*sizeof(Float32));

    memset (&mData->mFetchStamp, 0, sizeof(AudioTimeStamp));
    mData->mFetchStamp.mFlags = kAudioTimeStampSampleTimeValid;

}


- (void)priv_addListeners 
{
    if (mAU) {
        verify_noerr( AUEventListenerCreate(EventListenerDispatcher, self,
                                            CFRunLoopGetCurrent(), kCFRunLoopDefaultMode, 0.05, 0.05, 
                                            &mAUEventListener));
    }
}

- (void)priv_removeListeners 
{
    if (mAUEventListener) verify_noerr (AUListenerDispose(mAUEventListener));
    mAUEventListener = NULL;
    mAU = NULL;
}


- (void)priv_synchronizeUIWithParameterValues {

}

#pragma mark ___OnTimer___
- (NSTimer *) timer {
    return [[mFetchTimer retain] autorelease];
}

- (void) setTimer: (NSTimer *) value {
    if ( mFetchTimer != value ) {
        [mFetchTimer release];
        mFetchTimer = [value retain];
    }
}

#pragma mark ____ PUBLIC FUNCTIONS ____

- (void) updateCurve:(NSTimer*) t
{   
    mData->mChannel = 0;

    Float64 tStamp;
    UInt32 size = sizeof(Float64);
    ComponentResult result = AudioUnitGetProperty(  mAU,
                                                    kAudioUnitProperty_SampleTimeStamp,
                                                    kAudioUnitScope_Global,
                                                    0,
                                                    &tStamp,
                                                    &size);
#pragma mark HOW MUCH TO DISPLAY

    SInt64 numToGet = (SInt64)(tStamp - mData->mFetchStamp.mSampleTime);

    if (numToGet == 0) return;

    if (numToGet > kMaxWaveformSamples)
        numToGet = kMaxWaveformSamples;

    mData->mNumDataPoints = numToGet;


    size = sizeof(WaveformOverview);
    result = AudioUnitGetProperty(                  mAU,
                                                    kAudioUnitProperty_WaveformOverview,
                                                    kAudioUnitScope_Global,
                                                    0,
                                                    mData,
                                                    &size);
    if (result == noErr && tStamp != 0){
        [uiWaveformView plotNum: numToGet dataPoints: mData->mOverview];    
    }
}


- (void)setAU:(AudioUnit)inAU {
    // remove previous listeners
    [self priv_initBuffers];

    if (mAU) [self priv_removeListeners];

    mAU = inAU;

    // add new listeners
    [self priv_addListeners];   
    // initial setup
    [self priv_synchronizeUIWithParameterValues];

    // register for resize notification and data changes
//  [[NSNotificationCenter defaultCenter]
//   addObserver: self selector: @selector(handleWaveformSizeChanged:) name: NSViewFrameDidChangeNotification  object: uiWaveformView];

    [self setTimer: [NSTimer scheduledTimerWithTimeInterval: (1.0/140.0)
                                             target: self
                                             selector: @selector(updateCurve:)
                                             userInfo: nil
                                            repeats: YES]]; 


}


#pragma mark ____ INTERFACE ACTIONS ____

- (void) handleWaveformSizeChanged:(NSNotification *) aNotification {
    [self updateCurve:nil];
}


#pragma mark ____ LISTENER CALLBACK DISPATCHEE ____
- (void)priv_parameterListener:(void *)inObject parameter:(const AudioUnitParameter *)inParameter value:(Float32)inValue {
    //inObject ignored in this case.

    switch (inParameter->mParameterID) {

    }
}

// Handle kAudioUnitProperty_PresentPreset event
- (void)priv_eventListener:(void *) inObject event:(const AudioUnitEvent *)inEvent value:(Float32)inValue {
    switch (inEvent->mEventType) {

    }
}

@end
```

[Next](Source-CocoaUI-WaveformViewDemoViewFactory.h.md)[Previous](Source-CocoaUI-WaveformViewDemoView.h.md)


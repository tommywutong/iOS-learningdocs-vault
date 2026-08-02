---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Meters_Mediator_NBodyMeters_mm.html
archived_at: '2026-07-18T03:17:41.802760Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.mm.md)[Previous](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.h.md)

# Sources/Model/NBody/UI/Meters/Mediator/NBodyMeters.mm

```objc
/*
 <codex>
 <import>NBodyMeters.h</import>
 </codex>
 */

#pragma mark -

#import <OpenGL/gl.h>

#import "GLMConstants.h"
#import "GLMTransforms.h"

#import "NBodyMeter.h"
#import "NBodyMeters.h"

@implementation NBodyMeters
{
@private
    size_t           _index;
    size_t           _count;
    NSMutableArray*  mpMeters;
    NBodyMeter*      mpMeter;
}

- (instancetype) initWithCount:(size_t)count
{
    self = [super init];

    if(self)
    {
        _index = 0;
        _count = count;

        mpMeters = [[NSMutableArray alloc] initWithCapacity:_count];

        if(mpMeters)
        {
            size_t i;

            for(i = 0; i < _count; ++i)
            {
                mpMeters[i] = [NBodyMeter meter];
            } // for

            mpMeter = mpMeters[_index];
        } // if
    } // if

    return self;
} // init

- (void) dealloc
{
    if(mpMeters)
    {
        [mpMeters release];

        mpMeters = nil;
    } // if

    [super dealloc];
} // dealloc

- (void) reset
{
    for(NBodyMeter* pMeter in mpMeters)
    {
        pMeter.value = 0.0;

        [pMeter reset];
    } // for
} // reset

- (void) resize:(NSSize)size
{
    for(NBodyMeter* pMeter in mpMeters)
    {
        pMeter.frame = size;
    } // for
} // resize

- (void) show:(BOOL)doShow;
{
    for(NBodyMeter* pMeter in mpMeters)
    {
        pMeter.isVisible = doShow;
    } // for
} // show

- (BOOL) acquire
{
    return [mpMeter acquire];
} // acquire

- (void) toggle
{
    [mpMeter toggle];
} // toggle

- (void) update
{
    [mpMeter update];
} // update

- (void) draw
{
    [mpMeter draw];
} // draw

- (void) draw:(NSArray *)positions
{
    if(positions)
    {
        size_t i = 0;

       for(NSValue* position in positions)
       {
           NBodyMeter* pMeter = mpMeters[i];

           pMeter.point = position.pointValue;

           [pMeter update];
           [pMeter draw];

           i++;
       } // for
    } // if
} // draw

- (GLsizei) bound
{
    return mpMeter.bound;
} // bound

- (CGSize) frame
{
    return mpMeter.frame;
} // frame

- (BOOL) useTimer
{
    return mpMeter.useTimer;
} // useTimer

- (BOOL) useHostInfo
{
    return mpMeter.useHostInfo;
} // useHostInfo

- (BOOL) isVisible
{
    return mpMeter.isVisible;
} // isVisible

- (std::string) label
{
    return mpMeter.label;
} // label

- (size_t) max
{
    return mpMeter.max;
} // max

- (CGPoint) point
{
    return mpMeter.point;
} // point

- (GLfloat) speed
{
    return mpMeter.speed;
}// speed

- (GLfloat) value
{
    return mpMeter.value;
} // value

- (void) setBound:(GLsizei)bound
{
    mpMeter.bound = bound;
} // setBound

- (void) setFrame:(CGSize)frame
{
    mpMeter.frame = frame;
} // setFrame

- (void) setUseTimer:(BOOL)useTimer
{
    mpMeter.useTimer = useTimer;
} // setUseTimer

- (void) setUseHostInfo:(BOOL)useHostInfo
{
    mpMeter.useHostInfo = useHostInfo;
} // setUseHostInfo

- (void) setIndex:(size_t)index
{
    _index = (index < _count) ? index : 0;

    mpMeter = mpMeters[_index];
} // setIndex

- (void) setIsVisible:(BOOL)isVisible
{
    mpMeter.isVisible = isVisible;
} // setIsVisible

- (void) setLabel:(std::string)label
{
    mpMeter.label = label;
} // setLabel

- (void) setMax:(size_t)max
{
    mpMeter.max = max;
} // setMax

- (void) setPoint:(CGPoint)point
{
    mpMeter.point = point;
} // setPoint

- (void) setSpeed:(GLfloat)speed
{
    mpMeter.speed = speed;
} // setSpeed

- (void) setValue:(GLfloat)value
{
    mpMeter.value = value;
} // setValue

@end
```

[Next](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.mm.md)[Previous](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.h.md)


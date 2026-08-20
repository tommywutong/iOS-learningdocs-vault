---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Buttons_Mediator_NBodyButtons_mm.html
archived_at: '2026-07-18T03:17:41.541425Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-OpenGL-Math-Transforms-GLMTransforms.mm.md)[Previous](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.h.md)

# Sources/Model/NBody/UI/Buttons/Mediator/NBodyButtons.mm

```objc
/*
 <codex>
 <import>NBodyButtons.h</import>
 </codex>
 */

#import "NBodyButton.h"
#import "NBodyButtons.h"

@implementation NBodyButtons
{
@private
    size_t          _index;
    size_t          _count;
    NSMutableArray* mpButtons;
    NBodyButton*    mpButton;
}

- (instancetype) initWithCount:(size_t)count
{
    self = [super init];

    if(self)
    {
        _index = 0;
        _count = count;

        mpButtons = [[NSMutableArray alloc] initWithCapacity:_count];

        if(mpButtons)
        {
            size_t i;

            for(i = 0; i < _count; ++i)
            {
                mpButtons[i] = [NBodyButton button];
            } // for

            mpButton = mpButtons[_index];
        } // if
    } // if

    return self;
} // init

- (void) dealloc
{
    if(mpButtons)
    {
        [mpButtons release];

        mpButtons = nil;
    } // if

    [super dealloc];
} // dealloc

- (void) setIndex:(size_t)index
{
    _index = (index < _count) ? index : 0;

    mpButton = mpButtons[_index];
} // setIndex

- (BOOL) isItalic
{
    return mpButton.isItalic;
} // isItalic

- (BOOL) isSelected
{
    return mpButton.isSelected;
} // isSelected

- (BOOL) isVisible
{
    return mpButton.isVisible;
} // isVisible

- (std::string) label
{
    return mpButton.label;
} // label

- (CGFloat) fontSize
{
    return mpButton.fontSize;
} // fontSize

- (GLfloat) speed
{
    return mpButton.speed;
} // speed

- (CGRect) bounds
{
    return mpButton.bounds;
} // bounds

- (CGPoint) origin
{
    return mpButton.origin;
} // origin

- (CGPoint) position
{
    return mpButton.position;
} // position

- (CGSize) size
{
    return mpButton.size;
} // size

- (void) setLabel:(std::string)label
{
    mpButton.label = label;
} // setLabel

- (void) setIsItalic:(BOOL)isItalic
{
    mpButton.isItalic = isItalic;
} // setIsItalic

- (void) setIsSelected:(BOOL)isSelected
{
    mpButton.isSelected = isSelected;
} // setIsSelected

- (void) setIsVisible:(BOOL)isVisible
{
    mpButton.isVisible = isVisible;
} // setIsVisible

- (void) setFontSize:(CGFloat)fontSize
{
    mpButton.fontSize = fontSize;
} // fontSize

- (void) setSpeed:(GLfloat)speed
{
    mpButton.speed = speed;
} // setSpeed

- (void) setOrigin:(CGPoint)origin
{
    mpButton.origin = origin;
} // setOrigin

- (void) setSize:(CGSize)size
{
    mpButton.size = size;
} // setSize

- (BOOL) acquire
{
    return [mpButton acquire];
} // acquire

- (void) toggle
{
    [mpButton toggle];
} // toggle

- (void) draw
{
    [mpButton draw];
} // draw

@end
```

[Next](Sources-Model-OpenGL-Math-Transforms-GLMTransforms.mm.md)[Previous](Sources-Model-NBody-UI-Buttons-Mediator-NBodyButtons.h.md)


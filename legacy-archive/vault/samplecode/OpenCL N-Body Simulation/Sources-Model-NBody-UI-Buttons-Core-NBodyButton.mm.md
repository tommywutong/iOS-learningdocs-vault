---
title: OpenCL N-Body Simulation
apple_id: TP40016610
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_NBody_Simulation/Listings/Sources_Model_NBody_UI_Buttons_Core_NBodyButton_mm.html
archived_at: '2026-07-18T03:17:41.448163Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL N-Body Simulation](OpenCL%20N-Body%20Simulation.md)


[Next](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.h.md)[Previous](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.mm.md)

# Sources/Model/NBody/UI/Buttons/Core/NBodyButton.mm

```objc
/*
 <codex>
 <import>NBodyButton.h</import>
 </codex>
 */

#pragma mark -
#pragma mark Private - Headers

#import "GLMConstants.h"
#import "HUDButton.h"
#import "NBodyConstants.h"
#import "NBodyButton.h"

@implementation NBodyButton
{
@private
    BOOL         _isVisible;
    BOOL         _isSelected;
    BOOL         _isItalic;
    CGFloat      _fontSize;
    GLfloat      _speed;
    CGRect       _bounds;
    CGPoint      _position;
    CGPoint      _origin;
    CGSize       _size;
    std::string  _label;

    HUD::Button::Image* mpButton;
}

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        mpButton    = nullptr;
        _label      = "";
        _isVisible  = YES;
        _isSelected = NO;
        _isItalic   = NO;
        _fontSize   = 24.0f;
        _bounds     = NSMakeRect(0.0f, 0.0f, 0.0f, 0.0f);
        _size       = NSMakeSize(0.0f, 0.0f);
        _position   = NSMakePoint(0.0f, 0.0f);
        _origin     = CGPointMake(0.0f, (_isVisible ? GLM::kHalfPi_f : 0.0f));
        _speed      = NBody::Defaults::kSpeed;
    } // if

    return self;
} // init

+ (instancetype) button
{
    return [[[NBodyButton allocWithZone:[self zone]] init] autorelease];
} // button

- (void) dealloc
{
    if(!_label.empty())
    {
        _label.clear();
    } // if

    if(mpButton != nullptr)
    {
        delete mpButton;

        mpButton = nullptr;
    } // if

    [super dealloc];
} // dealloc

- (void) setIsVisible:(BOOL)isVisible
{
    _isVisible = isVisible;
    _origin.y  = _isVisible ? GLM::kHalfPi_f : 0.0f;
} // setIsVisible

- (void) setLabel:(std::string)label
{
    if(!label.empty())
    {
        _label = label;
    } // if
} // setLabel

- (void) setSize:(CGSize)size
{
    _size   = size;
    _bounds = CGRectMake(0.75f * _size.width - 0.5f * NBody::Button::kWidth,
                         NBody::Button::kSpacing,
                         NBody::Button::kWidth,
                         NBody::Button::kHeight);
} // setSize

- (BOOL) acquire
{
    if(mpButton == nullptr)
    {
        mpButton = new (std::nothrow) HUD::Button::Image(_bounds,
                                                         _fontSize,
                                                         _isItalic,
                                                         _label);
    } // if

    return mpButton != nullptr;
} // acquire

- (void) toggle
{
    _isVisible = !_isVisible;
} // toggle

- (void) draw
{
    if(mpButton != nullptr)
    {
        if(_isVisible)
        {
            if(_origin.y <= (GLM::kHalfPi_f - _speed))
            {
                _origin.y += _speed;
            } // if
        } // if
        else if(_origin.y > 0.0f)
        {
            _origin.y -= _speed;
        } // else if

        GLfloat x = -NBody::Button::kWidth * std::sin(_origin.x);
        GLfloat y = 100.0f * (std::sin(_origin.y) - 1.0f);

        _position = CGPointMake(x, y);

        mpButton->draw(_isSelected, _position, _bounds);
    } // if
} // draw

@end
```

[Next](Sources-Model-NBody-UI-Buttons-Core-NBodyButton.h.md)[Previous](Sources-Model-NBody-UI-Meters-Mediator-NBodyMeters.mm.md)


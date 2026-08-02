---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_UI_AAPLSlider_m.html
archived_at: '2026-07-26T19:54:16.865014Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-UI-AAPLButton.m.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLSlider.h.md)

# Objective-C/fox2 Shared/UI/AAPLSlider.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom `SKNode` based slider.
 */

#import "AAPLSlider.h"

@interface AAPLSlider ()

@property (strong, nonatomic) SKLabelNode *label;
@property (strong, nonatomic) SKShapeNode *slider;
@property (strong, nonatomic) SKSpriteNode *background;
@property (nonatomic, readonly) SEL actionClicked;
@property (nonatomic, readonly, weak) id targetClicked;

@end

@implementation AAPLSlider

@synthesize value = _value;

+ (AAPLSlider*)sliderWithWidth:(int)width height:(int)height text:(NSString*)txt
{
    AAPLSlider *s = [[AAPLSlider alloc] initWithWidth:width height:height text:txt];

    return s;
}

- (id)initWithWidth:(int)width height:(int)height text:(NSString*)txt
{
    if (self = [super init])
    {
        // create a label
        NSString *fontName = @"Optima-ExtraBlack";
        _label = [SKLabelNode labelNodeWithFontNamed:fontName];
        _label.text = txt;
        _label.fontSize = 18;
        _label.fontColor = [SKColor whiteColor];
        _label.position = CGPointMake(0., -8.);

        // create background & slider
        _background = [SKSpriteNode spriteNodeWithColor:[SKColor whiteColor] size:CGSizeMake(width, 2) ];
        _slider = [SKShapeNode shapeNodeWithCircleOfRadius:height];
        _slider.fillColor = [SKColor whiteColor];
        _background.anchorPoint = CGPointMake(0.f, 0.5f);

        _slider.position = CGPointMake(_label.frame.size.width/2 + 15, 0.);
        _background.position = CGPointMake(_label.frame.size.width/2 + 15, 0.);

        // add to the root node
        [self addChild:_label];
        [self addChild:_background];
        [self addChild:_slider];

        // track mouse event
        self.userInteractionEnabled = YES;

        _value = 0.f;
    }

    return self;
}

- (CGFloat) width
{
    return _background.frame.size.width;
}
- (CGFloat) height
{
    return _slider.frame.size.height;
}

- (void)setValue:(CGFloat)value
{
    _value = value;
    _slider.position = CGPointMake( self.background.position.x + _value*self.width, 0.);

}
- (CGFloat) value
{
    return _value;
}

- (void)setBackgroundColor:(SKColor*)col
{
    [_background setColor:col];
}

- (void)setClickedTarget:(id)target action:(SEL)action
{
    assert( target != nil && action != nil );

    _targetClicked = target;
    _actionClicked = action;

    IMP imp = [_targetClicked methodForSelector:action];
    assert( imp != nil );

    _action = (void *)imp;
}

#if TARGET_OS_OSX

- (void)mouseDown:(NSEvent *)event
{
    [self mouseDragged:event];
}
- (void)mouseUp:(NSEvent *)event
{
    [self setBackgroundColor:[SKColor whiteColor]];
}
- (void)mouseDragged:(NSEvent *)event
{
    [self setBackgroundColor:[SKColor grayColor]];

    CGPoint posInView = [self.scene convertPoint:self.position fromNode:self.parent];

    float x = [event locationInWindow].x - posInView.x - self.background.position.x;
    float pos = fmaxf( fminf( x, self.width), 0.f);
    _slider.position = CGPointMake( self.background.position.x + pos, 0.);

    self.value = pos / self.width;
    _action( _targetClicked, _actionClicked );
}

#endif

#if TARGET_OS_IPHONE
- (void)touchesMoved:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event
{
    [self setBackgroundColor:[SKColor grayColor]];

    float x = [[touches anyObject] locationInNode:self].x - self.background.position.x;
    float pos = fmaxf( fminf( x, self.width), 0.f);
    _slider.position = CGPointMake( self.background.position.x + pos, 0.);

    self.value = pos / self.width;

    _action( _targetClicked, _actionClicked );
}
#endif

@end
```

[Next](Objective-C-fox2%20Shared-UI-AAPLButton.m.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLSlider.h.md)


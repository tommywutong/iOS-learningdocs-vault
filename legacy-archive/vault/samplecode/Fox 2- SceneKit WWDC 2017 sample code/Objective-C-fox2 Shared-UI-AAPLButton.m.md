---
title: 'Fox 2: SceneKit WWDC 2017 sample code'
apple_id: TP40017656
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: SceneKit
published: '2018-04-05'
source_url: https://developer.apple.com/library/archive/samplecode/scenekit-2017/Listings/Objective_C_fox2_Shared_UI_AAPLButton_m.html
archived_at: '2026-07-26T19:54:16.876047Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Fox 2: SceneKit WWDC 2017 sample code](Fox%202-%20SceneKit%20WWDC%202017%20sample%20code.md)


[Next](Objective-C-fox2%20Shared-UI-AAPLButton.h.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLSlider.m.md)

# Objective-C/fox2 Shared/UI/AAPLButton.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Custom `SKNode` based button.
 */

#import "AAPLButton.h"

@interface AAPLButton ()

@property (strong, nonatomic) SKLabelNode *label;
@property (strong, nonatomic) SKSpriteNode *background;

@property (nonatomic, readonly) SEL actionClicked;
@property (nonatomic, readonly, weak) id targetClicked;

@property (nonatomic) CGSize size;

@end

@implementation AAPLButton

+ (AAPLButton*)buttonWithText:(NSString*)txt
{
    AAPLButton *button = [[AAPLButton alloc] initWithText:txt];
    return button;
}

+ (AAPLButton*)buttonWithSKNode:(SKNode*)node
{
    AAPLButton *button = [[AAPLButton alloc] initWithSKNode:node];
    return button;
}

- (id)initWithText:(NSString*)txt
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

        // create the background
        _size = CGSizeMake(_label.frame.size.width + 10., 30.);
        _background = [SKSpriteNode spriteNodeWithColor:[SKColor colorWithRed:0 green:0 blue:0 alpha:0.75] size:_size ];

        // add to the root node
        [self addChild:_background];
        [self addChild:_label];

        // Track mouse event
        self.userInteractionEnabled = YES;
    }

    return self;
}

- (id)initWithSKNode:(SKNode *)node
{
    if (self = [super init])
    {
        // Track mouse event
        self.userInteractionEnabled = YES;

        _size = node.frame.size;
        [self addChild:node];
    }

    return self;
}

- (CGFloat) width
{
    return _size.width;
}
- (CGFloat) height
{
    return _size.height;
}

- (void)setText:(NSString*)txt
{
    _label.text = txt;
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
    [self setBackgroundColor:[SKColor colorWithRed:0 green:0 blue:0 alpha:1.0]];
}

- (void)mouseUp:(NSEvent *)event
{
    [self setBackgroundColor:[SKColor colorWithRed:0 green:0 blue:0 alpha:0.75]];
    CGPoint pos = [self.scene convertPoint:self.position fromNode:self.parent];

    CGPoint p = [event locationInWindow];
    if( fabs(p.x-pos.x) < self.width/2*self.xScale && fabs(p.y-pos.y) < self.height/2*self.yScale )
        _action( _targetClicked, _actionClicked );
}

#endif

#if TARGET_OS_IPHONE

- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(nullable UIEvent *)event
{
    _action( _targetClicked, _actionClicked );
}

#endif

@end
```

[Next](Objective-C-fox2%20Shared-UI-AAPLButton.h.md)[Previous](Objective-C-fox2%20Shared-UI-AAPLSlider.m.md)


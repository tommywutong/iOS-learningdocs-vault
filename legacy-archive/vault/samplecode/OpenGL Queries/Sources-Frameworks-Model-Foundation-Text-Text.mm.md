---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Foundation_Text_Text_mm.html
archived_at: '2026-07-18T03:18:13.224528Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Query-QueryDataSource.mm.md)[Previous](Sources-Frameworks-Model-Foundation-Text-Text.h.md)

# Sources/Frameworks/Model/Foundation/Text/Text.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utility class for generating a mutable attributed string from a c-string and the associated properties.
 */

#import "Text.h"

@implementation Text
{
@private
    BOOL                        mbFontUpdate;
    BOOL                        mbParagraphStyleUpdate;
    BOOL                        mbColorUpdate;
    NSRange                     _range;
    NSRange                     _colorRange;
    NSColor*                    _color;
    CGFloat                     _fontSize;
    NSString*                   _fontName;
    NSMutableAttributedString*  _text;
    NSUInteger                  mnLength;
    NSFont*                     mpFont;
    NSMutableParagraphStyle*    mpParagraphStyle;
}

- (void) _newTextWithString:(NSString *)string
{
    if(string)
    {
        NSUInteger length = string.length;

        if(length)
        {
            _text = [[NSMutableAttributedString alloc] initWithString:string];

            if(_text)
            {
                _fontName    = @"Helvetica";
                _fontSize    = 12.0f;
                mpFont       = nil;
                mbFontUpdate = YES;

                mnLength = length;
                _range   = NSMakeRange(0, mnLength);

                _colorRange   = _range;
                _color        = [[[NSColor blackColor] colorUsingColorSpace:[NSColorSpace deviceRGBColorSpace]] retain];
                mbColorUpdate = (_color) ? YES : NO;

                mpParagraphStyle       = [NSMutableParagraphStyle new];
                mbParagraphStyleUpdate = (mpParagraphStyle) ? YES : NO;

                if(mbParagraphStyleUpdate)
                {
                    mpParagraphStyle.alignment        = NSLeftTextAlignment;
                    mpParagraphStyle.lineSpacing      = 1.0f;
                    mpParagraphStyle.paragraphSpacing = 1.0f;
                    mpParagraphStyle.lineBreakMode    = NSLineBreakByWordWrapping;
                } // if
            } // if
        } // if
    } // if
} // _newTextWithString

- (void) _newTextWithCString:(const char *)string
{
    if(string != nullptr)
    {
        [self _newTextWithString:[NSString stringWithCString:string
                                                    encoding:NSASCIIStringEncoding]];
    } // if
} // _newTextWithCString

- (instancetype) initWithString:(NSString *)string
{
    self = [super init];

    if(self)
    {
        [self _newTextWithString:string];
    } // if

    return self;
} // initWithString

- (instancetype) initWithCString:(const char *)string
{
    self = [super init];

    if(self)
    {
        [self _newTextWithCString:string];
    } // if

    return self;
} // initWithCString

+ (instancetype) textWithString:(NSString *)string
{
    return [[[Text allocWithZone:[self zone]] initWithString:string] autorelease];
} // textWithString

+ (instancetype) textWithCString:(const char *)string
{
    return [[[Text allocWithZone:[self zone]] initWithCString:string] autorelease];
} // textWithCString

- (void) dealloc
{
    if(mpParagraphStyle)
    {
        [mpParagraphStyle release];

        mpParagraphStyle = nil;
    } // if

    if(_color)
    {
        [_color release];

        _color = nil;
    } // if

    if(mpFont)
    {
        [mpFont release];

        mpFont = nil;
    } // if

    if(_fontName)
    {
        [_fontName release];

        _fontName = nil;
    } // if

    if(_text)
    {
        [_text release];

        _text = nil;
    } // if

    [super dealloc];
} // dealloc

- (void) setAlignment:(NSTextAlignment)alignment
{
    if(mpParagraphStyle)
    {
        mbParagraphStyleUpdate = (mbParagraphStyleUpdate) || (mpParagraphStyle.alignment != alignment);

        mpParagraphStyle.alignment = alignment;
    } // if
} // setAlignment

- (void) setLineSpacing:(CGFloat)lineSpacing
{
    if(mpParagraphStyle)
    {
        mbParagraphStyleUpdate = (mbParagraphStyleUpdate) || (mpParagraphStyle.lineSpacing != lineSpacing);

        mpParagraphStyle.lineSpacing = (lineSpacing >= 0.5f) ? lineSpacing : 1.0f;
    } // if
} // setLineSpacing

- (void) setParagraphSpacing:(CGFloat)paragraphSpacing
{
    if(mpParagraphStyle)
    {
        mbParagraphStyleUpdate = (mbParagraphStyleUpdate) || (mpParagraphStyle.paragraphSpacing != paragraphSpacing);

        mpParagraphStyle.paragraphSpacing = (paragraphSpacing >= 0.5f) ? paragraphSpacing : 1.0f;
    } // if
} // setParagraphSpacing

- (void) setLineBreakMode:(NSLineBreakMode)lineBreakMode
{
    if(mpParagraphStyle)
    {
        mbParagraphStyleUpdate = (mbParagraphStyleUpdate) || (mpParagraphStyle.lineBreakMode != lineBreakMode);

        mpParagraphStyle.lineBreakMode = lineBreakMode;
    } // if
} // setLineBreakMode

- (void) setColor:(NSColor *)color
{
    if(_color && color)
    {
        NSColor* dstColor = [color colorUsingColorSpace:[NSColorSpace deviceRGBColorSpace]];

        if(dstColor)
        {
            BOOL bRed   = _color.redComponent   != dstColor.redComponent;
            BOOL bGreen = _color.greenComponent != dstColor.greenComponent;
            BOOL bBlue  = _color.blueComponent  != dstColor.blueComponent;

            mbColorUpdate = mbColorUpdate || (bRed || bGreen || bBlue);

            if(mbColorUpdate)
            {
                [_color release];

                _color = [dstColor retain];
            } // if
        } // if
    } // if
} // setColor

- (void) setColorRange:(NSRange)colorRange
{
    if(colorRange.length)
    {
        mbColorUpdate =     mbColorUpdate
                        ||  (colorRange.length   != _colorRange.length)
                        ||  (colorRange.location != _colorRange.location);

        _colorRange = colorRange;
    } // if
} // setColorRange

- (void) setRange:(NSRange)range
{
    if(range.length)
    {
        _range = range;
    } // if
} // setRange

- (void) setFontSize:(CGFloat)fontSize
{
    mbFontUpdate = mbFontUpdate || (_fontSize != fontSize);

    _fontSize = (_fontSize >= 1.0f) ? fontSize : 12.0f;
} // setPointSize

- (void) setFontName:(NSString *)fontName
{
    if(fontName && _fontName)
    {
        NSComparisonResult nResult = [_fontName compare:fontName];

        mbFontUpdate = mbFontUpdate || (nResult != NSOrderedSame);

        if(mbFontUpdate)
        {
            [_fontName release];

            _fontName = [fontName retain];
        } // if
    } // if
} // setFontName

- (NSUInteger) length
{
    return mnLength;
} // length

- (NSString *) string
{
    return _text.string;
} // string

- (NSTextAlignment) alignment
{
    return mpParagraphStyle.alignment;
} // alignment

- (CGFloat) lineSpacing
{
    return mpParagraphStyle.lineSpacing;
} // lineSpacing

- (CGFloat) paragraphSpacing
{
    return mpParagraphStyle.paragraphSpacing;
} // paragraphSpacing

- (NSLineBreakMode) lineBreakMode
{
    return mpParagraphStyle.lineBreakMode;
} // lineBreakMode

- (void) _updateFont
{
    if(mbFontUpdate)
    {
        NSFont* pFont = [[NSFont fontWithName:_fontName
                                         size:_fontSize] retain];

        if(pFont)
        {
            if(mpFont)
            {
                [mpFont release];
            } // if

            mpFont = pFont;

            [_text addAttribute:NSFontAttributeName
                          value:mpFont
                          range:_range];

            mbFontUpdate = NO;
        } // if
    } // if
} // _updateFont

- (void) _updateParagraphStyle
{
    if(mbParagraphStyleUpdate)
    {
        [_text addAttribute:NSParagraphStyleAttributeName
                      value:mpParagraphStyle
                      range:_range];

        mbParagraphStyleUpdate = NO;
    } // if
} // _updateParagraphStyle

- (void) _updateColor
{
    if(mbColorUpdate)
    {
        [_text addAttribute:NSForegroundColorAttributeName
                      value:_color
                      range:_colorRange];

        mbColorUpdate = NO;
    } // if
} // _updateColor

- (NSMutableAttributedString *) text
{
    [self _updateFont];
    [self _updateParagraphStyle];
    [self _updateColor];

    return _text;
} // text

@end
```

[Next](Sources-Frameworks-Model-Query-QueryDataSource.mm.md)[Previous](Sources-Frameworks-Model-Foundation-Text-Text.h.md)


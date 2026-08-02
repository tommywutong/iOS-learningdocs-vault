---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Graphics_Displays_Data_CGDisplaysDataSource_mm.html
archived_at: '2026-07-18T03:18:13.372679Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.h.md)

# Sources/Frameworks/Model/Graphics/Displays/Data/CGDisplaysDataSource.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for the outline view.
 */

#import <iomanip>
#import <iostream>
#import <sstream>

#import "Text.h"

#import "CGDisplaysDataSource.h"

@implementation CGDisplaysDataSource
{
@private
    NSMutableDictionary*  _dictionary;
    NSMutableSet*         _parent;
    NSMutableSet*         _childern;
    CG::Display::List*    mpList;
}

- (Text *) _acquireParent:(const std::string&)key
                    value:(const GLuint&)value
{
    NSRange  hexRange = NSMakeRange(0,0);

    std::ostringstream stream;

    if(!key.empty())
    {
        if(value)
        {
            std::ostringstream vstream;

            vstream << "0x" << std::hex << value;

            std::string  hexStr = vstream.str();
            size_t       hexLen = hexStr.length();

            hexRange = NSMakeRange(1,hexLen);

            stream << "[" << hexStr << "] " << key;
        } // if
        else
        {
            stream << key;
        } // else
    } // if
    else
    {
        stream << "parent";
    } // else

    Text* pText = nil;

    std::string string = stream.str();

    NSString* pString = [NSString stringWithCString:string.c_str()
                                           encoding:NSASCIIStringEncoding];

    if(pString)
    {
        [_parent addObject:pString];

        pText = [Text textWithString:pString];

        if(pText)
        {
            pText.fontSize   = 14.0f;
            pText.fontName   = @"Helvetica";
            pText.color      = [NSColor blueColor];
            pText.colorRange = hexRange;
        } // if
    } // if

    return pText;
} // _acquireParent

- (Text *) _acquireBounds:(const CG::Display::Mode&)mode
{
    Text* pText = nil;

    std::ostringstream stream;

    CG::Display::Size pixels = mode.pixels();

    stream << std::setw(4) << pixels.width << " x " << std::setw(4) << pixels.height;

    std::string string = stream.str();

    NSString* pString = [NSString stringWithCString:string.c_str()
                                           encoding:NSASCIIStringEncoding];

    if(pString)
    {
        [_childern addObject:pString];

        pText = [Text textWithString:pString];

        if(pText)
        {
            pText.fontSize   = 14.0f;
            pText.fontName   = @"Courier";
            pText.alignment  = NSJustifiedTextAlignment;
            pText.color      = [NSColor blueColor];
        } // if
    } // if

    return pText;
} // _acquireBounds

- (NSArray *) _modesArray:(const CG::Display::Modes&)displayModes
{
    NSArray *pSortedModes = nil;

    NSMutableArray* pModes = [NSMutableArray arrayWithCapacity:displayModes.count()];

    if(pModes)
    {
        size_t idx = 0;

        CG::Display::ModeTable modes = displayModes.table();

        for(auto& mode:modes)
        {
            Text *pBounds = [self _acquireBounds:mode.second];

            if(pBounds)
            {
                pModes[idx] = pBounds.text;
            } // if

            idx++;
        } // for

        pSortedModes = [pModes sortedArrayUsingComparator:
                        ^(NSAttributedString* pAttrStrA, NSAttributedString* pAttrStrB)
                        {
                            NSString *pStrA = pAttrStrA.string;
                            NSString *pStrB = pAttrStrB.string;

                            return [pStrA localizedCompare:pStrB];
                        }];
    } // if

    return pSortedModes;
} // _modesArray

- (NSMutableDictionary *) _displayDictionary:(const uint32_t&)displayID
                                       modes:(const CG::Display::Modes&)displayModes
{
    NSMutableDictionary  *pDictionary = [NSMutableDictionary dictionary];

    if(pDictionary)
    {
        Text* pDisplayID = [self _acquireParent:"Resolutions"
                                          value:displayID];

        if(pDisplayID)
        {
            pDictionary[@"parent"] = pDisplayID.text;
        } // if

        NSArray* pModes = [self _modesArray:displayModes];

        if(pModes)
        {
            pDictionary[@"children"] = pModes;
        } // if
    } // if

    return pDictionary;
} // _displayDictionary

- (NSMutableArray *) _displayArray:(const CG::Display::DisplayTable&)displays
{
    NSMutableArray* pDisplays = [NSMutableArray arrayWithCapacity:displays.size()];

    if(pDisplays)
    {
        size_t idx = 0;

        for(auto& display:displays)
        {
            NSMutableDictionary* pDisplay = [self _displayDictionary:display.first
                                                               modes:display.second];

            if(pDisplay)
            {
                pDisplays[idx] = pDisplay;
            } // if

            idx++;
        } // for
    } // if

    return pDisplays;
} // _displayArray

- (void) _addDisplays
{
    const CG::Display::DisplayTable displays = mpList->table();

    if(!displays.empty())
    {
        _dictionary = [NSMutableDictionary new];

        if(_dictionary)
        {
            Text* pLabel = [Text textWithString:@"Displays"];

            if(pLabel)
            {
                pLabel.fontSize  = 14.0f;
                pLabel.fontName  = @"Helvetica";

                [_parent addObject:@"Displays"];

                _dictionary[@"parent"] = pLabel.text;
            } // if

            NSMutableArray* pArray = [self _displayArray:displays];

            if(pArray)
            {
                _dictionary[@"children"] = pArray;
            } // if
        } // if
    } // if
} // _addDisplays

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        mpList = CG::Display::List::create();

        if(mpList != nullptr)
        {
            _parent   = [NSMutableSet new];
            _childern = [NSMutableSet new];

            [self _addDisplays];
        } // if
    } // if

    return self;
} // init

+ (instancetype) query
{
    return [[[CGDisplaysDataSource allocWithZone:[self zone]] init] autorelease];
} // query

- (void) dealloc
{
    if(_parent)
    {
        [_parent release];

        _parent = nil;
    } // if

    if(_childern)
    {
        [_childern release];

        _childern = nil;
    } // if

    if(_dictionary)
    {
        [_dictionary release];

        _dictionary = nil;
    } // if

    if(mpList)
    {
        delete mpList;

        mpList = nullptr;
    } // if

    [super dealloc];
} // dealloc

- (BOOL) isChild:(NSString *)string
{
    BOOL bSuccess = string != nil;

    if(bSuccess)
    {
        bSuccess = [_childern containsObject:string];
    } // if

    return bSuccess;
} // isChild

- (BOOL) isParent:(NSString *)string
{
    BOOL bSuccess = string != nil;

    if(bSuccess)
    {
        bSuccess = [_parent containsObject:string];
    } // if

    return bSuccess;
} // isParent

@end
```

[Next](Sources-Frameworks-Model-Graphics-Displays-Data-CGDisplaysDataSource.h.md)[Previous](Sources-Frameworks-Model-Graphics-Displays-Mode-CGDisplayMode.h.md)


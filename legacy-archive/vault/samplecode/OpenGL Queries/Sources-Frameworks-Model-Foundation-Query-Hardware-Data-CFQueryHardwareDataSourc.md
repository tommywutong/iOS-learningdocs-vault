---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_Foundation_Query_Hardware_Data_CFQueryHardwareDataSource_mm.html
archived_at: '2026-07-18T03:18:13.083941Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc-2.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.h.md)

# Sources/Frameworks/Model/Foundation/Query/Hardware/Data/CFQueryHardwareDataSource.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for hardware property queries.
 */

#import <string>
#import <iostream>
#import <sstream>
#import <string>

#import "Text.h"

#import "CFQueryHardwareDataSource.h"

@implementation CFQueryHardwareDataSource
{
@private
    NSMutableDictionary*  _dictionary;
    NSMutableSet*         _parent;
    NSMutableSet*         _childern;
    CF::Query::Hardware*  mpHardware;
}

- (Text *) _acquireText:(const std::string&)string
{
    Text* pText = [Text textWithCString:string.c_str()];

    if(pText)
    {
        pText.fontName  = @"Courier";
        pText.fontSize  = 14.0f;
        pText.alignment = NSJustifiedTextAlignment;
        pText.color     = [NSColor blueColor];
    } // if

    return pText;
} // _acquireText

- (Text *) _acquireHardware
{
    [_parent addObject:@"Hardware"];

    Text* pText = [Text textWithString:@"Hardware"];

    if(pText)
    {
        pText.fontSize  = 14.0f;
        pText.alignment = NSJustifiedTextAlignment;
    } // if

    return pText;
} // _acquireHardware

- (void) _addCores:(NSMutableArray *)pArray
{
    std::ostringstream stream;

    stream << "Number of Cores:\t\t" << mpHardware->cores();

    Text* pCores = [self _acquireText:stream.str()];

    if(pCores)
    {
        [_childern addObject:pCores.string];

        pArray[0] = pCores.text;
    } // if
} // _addCores

- (void) _addMemory:(NSMutableArray *)pArray
{
    std::ostringstream stream;

    stream << "Memory Size:\t\t\t" << mpHardware->memory() << " GB";

    Text* pMemory = [self _acquireText:stream.str()];

    if(pMemory)
    {
        [_childern addObject:pMemory.string];

        pArray[1] = pMemory.text;
    } // if
} // _addMemory

- (void) _addCPU:(NSMutableArray *)pArray
{
    std::ostringstream stream;

    stream << "Processor Speed:\t\t" << mpHardware->cpu() << " GHz";

    Text* pCPU = [self _acquireText:stream.str()];

    if(pCPU)
    {
        [_childern addObject:pCPU.string];

        pArray[2] = pCPU.text;
    } // if
} // _addCPU

- (void) _addModel:(NSMutableArray *)pArray
{
    std::ostringstream stream;

    stream << "Model:\t\t\t\t\t" << "\"" << mpHardware->model() << "\"";

    Text* pModel = [self _acquireText:stream.str()];

    if(pModel)
    {        
        [_childern addObject:pModel.string];

        pArray[3] = pModel.text;
    } // if
} // _addModel

- (void) _addHardware
{
    mpHardware = new (std::nothrow) CF::Query::Hardware;

    if(mpHardware != nullptr)
    {
        _dictionary = [NSMutableDictionary new];

        if(_dictionary)
        {
            Text* pLabel = [self _acquireHardware];

            if(pLabel)
            {
                _dictionary[@"parent"] = pLabel.text;
            } // if

            NSMutableArray* pArray = [NSMutableArray arrayWithCapacity:4];

            if(pArray)
            {
                [self _addCores:pArray];
                [self _addMemory:pArray];
                [self _addCPU:pArray];
                [self _addModel:pArray];

                _dictionary[@"children"] = pArray;
            } // if
        } // if
    } // if
    else
    {
        NSLog(@">> ERROR: Failed allocating memory for hardware query object!");
    } // else
} // _addHardware

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        _parent   = [NSMutableSet new];
        _childern = [NSMutableSet new];

        [self _addHardware];
    } // if

    return self;
} // init

+ (instancetype) query
{
    return [[[CFQueryHardwareDataSource allocWithZone:[self zone]] init] autorelease];
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

    if(mpHardware)
    {
        delete mpHardware;

        mpHardware = nullptr;
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

[Next](Sources-Frameworks-Model-Foundation-Query-Hardware-Data-CFQueryHardwareDataSourc-2.md)[Previous](Sources-Frameworks-Model-Foundation-Query-Hardware-Core-CFQueryHardware.h.md)


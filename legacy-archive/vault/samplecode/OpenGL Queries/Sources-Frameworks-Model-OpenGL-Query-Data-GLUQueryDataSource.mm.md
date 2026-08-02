---
title: OpenGL Queries
apple_id: TP40016611
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2015-12-10'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Queries/Listings/Sources_Frameworks_Model_OpenGL_Query_Data_GLUQueryDataSource_mm.html
archived_at: '2026-07-18T03:18:13.935793Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenGL Queries](OpenGL%20Queries.md)


[Next](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.mm.md)

# Sources/Frameworks/Model/OpenGL/Query/Data/GLUQueryDataSource.mm

```objc
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Query data source for OpenGL renderer and device quaries.
 */

#import <iomanip>
#import <iostream>
#import <sstream>

#import "Text.h"

#import "GLUQueryRendererPropertyNames.h"
#import "GLUQueryRendererProperty.h"
#import "GLUQueryDataSource.h"

@implementation GLUQueryDataSource
{
@private
    NSMutableDictionary*    _dictionary;
    NSMutableSet*           _parent;
    NSMutableSet*           _childern;
    GLU::Query::Devices*    mpDevices;
    GLU::Query::Renderers*  mpRenderers;
}

- (Text *) _acquireText:(const GLstring&)string
{
    Text* pText = [Text textWithCString:string.c_str()];

    if(pText)
    {
        pText.fontSize = 14.0f;
        pText.fontName = @"Courier";
        pText.color    = [NSColor blueColor];
    } // if

    return pText;
} // _acquireText

- (Text *) _acquireParent:(const GLstring&)key
                    color:(NSColor *)color
                    value:(const GLuint&)value
{
    NSRange  hexRange = NSMakeRange(0,0);

    GLosstringstream stream;

    if(!key.empty())
    {
        if(value)
        {
            GLosstringstream vstream;

            vstream << "0x" << std::hex << value;

            GLstring  hexStr = vstream.str();
            size_t    hexLen = hexStr.length();

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

    GLstring string = stream.str();

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
            pText.color      = color;
            pText.colorRange = hexRange;
        } // if
    } // if

    return pText;
} // _acquireParent

- (Text *) _acquireDescription:(const GLuint&)value
{
    return [self _acquireParent:"Description"
                          color:[NSColor blueColor]
                          value:value];
} // _acquireDescription

- (Text *) _acquireFeatures:(const GLuint&)value
{
    return [self _acquireParent:"Features"
                          color:[NSColor blueColor]
                          value:value];
} // _acquireFeatures

- (Text *) _acquireProperties:(const GLuint&)value
{
    return [self _acquireParent:"Properties"
                          color:[NSColor blueColor]
                          value:value];
} // _acquireProperties

- (Text *) _acquireRenderer:(const GLuint&)value
{
    return [self _acquireParent:"Renderer"
                          color:[NSColor blueColor]
                          value:value];
} // _acquireRenderer

- (Text *) _acquireRenderers
{
    return [self _acquireParent:"Renderers"
                          color:[NSColor blackColor]
                          value:0];
} // _acquireRenderers

- (Text *) _acquireProperty:(const GLstring&)key
                      value:(const GLuint&)value
                     length:(const size_t&)length
{
    GLint width = GLint(length - key.length());

    GLosstringstream stream;

    stream << key << std::setw(width);

    switch(value)
    {
        case 0:
            stream << "NO";
            break;

        case 1:
            stream << "YES";
            break;

        default:
            stream << value;
            break;
    } // switch

    Text* pText = nil;

    GLstring string = stream.str();

    NSString* pString = [NSString stringWithCString:string.c_str()
                                           encoding:NSASCIIStringEncoding];

    if(pString)
    {
        [_childern addObject:pString];

        pText = [Text textWithString:pString];

        if(pText)
        {
            pText.fontSize  = 14.0f;
            pText.fontName  = @"Courier";
            pText.alignment = NSJustifiedTextAlignment;
            pText.color     = [NSColor blueColor];
        } // if
    } // if

    return pText;
} // _acquireProperty

- (NSMutableArray *) _propertiesArray:(const GLproperties&)properties
{
    NSMutableArray*  pProperties = [NSMutableArray arrayWithCapacity:properties.size()];

    if(pProperties)
    {
        GLU::Query::RendererProperty* pRendererProps = new (std::nothrow) GLU::Query::RendererProperty;

        if(pRendererProps != nullptr)
        {
            size_t idx    = 0;
            size_t length = pRendererProps->length();

            for(auto& property:properties)
            {
                GLuint   value = property.second;
                GLstring key   = pRendererProps->find(property.first);

                Text* pProperty = [self _acquireProperty:key
                                                   value:value
                                                  length:length];

                if(pProperty)
                {
                    pProperties[idx] = pProperty.text;
                } // if

                idx++;
            } // for

            delete pRendererProps;
        } // if
        else
        {
            NSLog(@">> ERROR: Failed allocating memory for renderer property query object!");
        } // else
    } // if

    return pProperties;
} // _propertiesArray

- (NSMutableDictionary *) _propertiesDictionary:(const GLint&)nRendererID
                                     properties:(const GLproperties&)properties
{
    NSMutableDictionary* pDictionary = [NSMutableDictionary dictionary];

    if(pDictionary)
    {
        Text* pPropertiesID = [self _acquireProperties:nRendererID];

        if(pPropertiesID)
        {
            pDictionary[@"parent"] = pPropertiesID.text;
        } // if

        NSMutableArray* pProperties = [self _propertiesArray:properties];

        if(pProperties)
        {
            pDictionary[@"children"] = pProperties;
        } // if
    } // if

    return pDictionary;
} // _propertiesDictionary

- (NSArray *) _featuresArray:(const GLint&)nRendererID
{
    NSArray* pSortedFeatures = nil;

    GLfeatures       features  = mpDevices->features(nRendererID);
    NSMutableArray*  pFeatures = [NSMutableArray arrayWithCapacity:features.size()];

    if(pFeatures)
    {
        size_t idx = 0;

        for(auto& feature:features)
        {
            GLstring key = feature.first;

            Text* pFeature = [self _acquireText:key];

            if(pFeature)
            {
                pFeatures[idx] = pFeature.text;
            } // if

            idx++;
        } // for

        pSortedFeatures = [pFeatures sortedArrayUsingComparator:
                           ^(NSAttributedString* pAttrStrA, NSAttributedString* pAttrStrB)
                           {
                               NSString *pStrA = [pAttrStrA string];
                               NSString *pStrB = [pAttrStrB string];

                               return [pStrA localizedCompare:pStrB];
                           }];
    } // if

    return pSortedFeatures;
} // _featuresArray

- (NSMutableDictionary *) _featuresDictionary:(const GLint&)nRendererID
{
    NSMutableDictionary* pDictionary = [NSMutableDictionary dictionary];

    if(pDictionary)
    {
        Text* pFeaturesID = [self _acquireFeatures:nRendererID];

        if(pFeaturesID)
        {
            pDictionary[@"parent"] = pFeaturesID.text;
        } // if

        NSArray* pFeatures = [self _featuresArray:nRendererID];

        if(pFeatures)
        {
            pDictionary[@"children"] = pFeatures;
        } // if
    } // if

    return pDictionary;
} // _featuresDictionary

- (NSMutableDictionary *) _descriptionDictionary:(const GLint&)nRendererID
{
    NSMutableDictionary* pDescription = [NSMutableDictionary dictionary];

    if(pDescription)
    {
        Text* pDescriptionID = [self _acquireDescription:nRendererID];

        if(pDescriptionID)
        {
            pDescription[@"parent"] = pDescriptionID.text;
        } // if

        NSMutableArray* pArray = [NSMutableArray arrayWithCapacity:3];

        if(pArray)
        {
            Text* pRenderer = [self _acquireText:mpDevices->renderer(nRendererID)];

            if(pRenderer)
            {
                pArray[0] = pRenderer.text;
            } // if

            Text* pVendor = [self _acquireText:mpDevices->vendor(nRendererID)];

            if(pVendor)
            {
                pArray[1] = pVendor.text;
            } // if

            Text* pVersion = [self _acquireText:mpDevices->version(nRendererID)];

            if(pVersion)
            {
                pArray[2] = pVersion.text;
            } // if

            pDescription[@"children"] = pArray;
        } // if
    } // if

    return pDescription;
} // _descriptionDictionary

- (NSMutableDictionary *) _rendererDictionary:(const GLuint&)nRendererID
                                   properties:(const GLproperties&)properties
{
    NSMutableDictionary* pRenderer = [NSMutableDictionary dictionary];

    if(pRenderer)
    {
        Text* pRendererID = [self _acquireRenderer:nRendererID];

        if(pRendererID)
        {
            pRenderer[@"parent"] = pRendererID.text;
        } // if

        NSMutableArray* pArray = [NSMutableArray arrayWithCapacity:3];

        if(pArray)
        {
            NSMutableDictionary* pDescription = [self _descriptionDictionary:nRendererID];

            if(pDescription)
            {
                pArray[0] = pDescription;
            } // if

            NSMutableDictionary* pFeatures = [self _featuresDictionary:nRendererID];

            if(pFeatures)
            {
                pArray[1] = pFeatures;
            } // if

            NSMutableDictionary* pProperties = [self _propertiesDictionary:nRendererID
                                                                properties:properties];

            if(pProperties)
            {
                pArray[2] = pProperties;
            } // if

            pRenderer[@"children"] = pArray;
        } // if
    } // if

    return pRenderer;
} // _rendererDictionary

- (NSArray *) _renderersArray:(const GLrenderers&)renderers
{
    NSArray* pSortedRenderers = nil;

    NSMutableArray* pRenderers = [NSMutableArray arrayWithCapacity:renderers.size()];

    if(pRenderers)
    {
        size_t idx = 0;

        for(auto& renderer:renderers)
        {
            NSMutableDictionary* pRenderer = [self _rendererDictionary:renderer.first
                                                            properties:renderer.second];

            if(pRenderer)
            {
                pRenderers[idx] = pRenderer;
            } // if

            idx++;
        } // for

        pSortedRenderers = [pRenderers sortedArrayUsingComparator:
                            ^(NSMutableDictionary* pDictA, NSMutableDictionary* pDictB)
                            {
                                NSString *pStrA = [pDictA[@"parent"] string];
                                NSString *pStrB = [pDictB[@"parent"] string];

                                return [pStrA localizedCompare:pStrB];
                            }];
    } // if

    return pSortedRenderers;
} // _renderersArray

- (void) _addRenderers
{
    const GLrenderers renderers = mpRenderers->renderers();

    if(!renderers.empty())
    {
        _dictionary = [NSMutableDictionary new];

        if(_dictionary)
        {
            Text* pLabel = [self _acquireRenderers];

            if(pLabel)
            {
                _dictionary[@"parent"] = pLabel.text;
            } // if

            NSArray* pArray = [self _renderersArray:renderers];

            if(pArray)
            {
                _dictionary[@"children"] = pArray;
            } // if
        } // if
    } // if
} // _addRenderers

- (instancetype) init
{
    self = [super init];

    if(self)
    {
        mpRenderers = GLU::Query::Renderers::create();

        if(mpRenderers != nullptr)
        {
            mpDevices = GLU::Query::Devices::create();

            if(mpDevices != nullptr)
            {
                _parent   = [NSMutableSet new];
                _childern = [NSMutableSet new];

                [self _addRenderers];
            } // if
        } // if
    } // if

    return self;
} // init

+ (instancetype) query
{
    return [[[GLUQueryDataSource allocWithZone:[self zone]] init] autorelease];
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

    if(mpDevices)
    {
        delete mpDevices;

        mpDevices = nullptr;
    } // if

    if(mpRenderers)
    {
        delete mpRenderers;

        mpRenderers = nullptr;
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

[Next](Sources-Frameworks-Model-OpenGL-Query-Data-GLUQueryDataSource.h.md)[Previous](Sources-Frameworks-Model-OpenGL-Query-Renderers-GLUQueryRenderers.mm.md)


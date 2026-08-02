---
title: Final Cut Pro X Workflows Developer Guide
apple_id: TP40013781
resource_type: Guide
platform: macOS
topic: Apple Applications
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/FinalCutProX/Conceptual/FinalCutProXWorkflowsGuide/ScriptingSupportCategories/ScriptingSupportCategories.html
archived_at: '2026-07-15T07:32:30.125988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Final Cut Pro X Workflows Developer Guide](About%20Final%20Cut%20Pro%20X%20Workflows.md)


[Next](Document%20Revision%20History.md)[Previous](Appendix%20C-%20Share%20Metadata.md)

# Appendix D: Scripting Support Categories

This appendix lists a sample implementation of the categories discussed in [Scripting Support Class Extensions](Exporting.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztoobrfvbuqmznknltg). For more information on the `NSAppleEventDescriptor` class, consult _[NSAppleEventDescriptor Class Reference](https://developer.apple.com/documentation/foundation/nsappleeventdescriptor)_.

```objc
/*
 File: ScriptingSupportCategories.m
 Abstract: Cocoa Scripting Support Categories implementations
 Version: 1.6

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

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

 Copyright (C) 2016 Apple Inc. All Rights Reserved.

 */

#import "ScriptingSupportCategories.h"

#import <Carbon/Carbon.h>


@implementation NSDictionary (UserDefinedRecord)

+(NSDictionary*)scriptingUserDefinedRecordWithDescriptor:(NSAppleEventDescriptor*)desc
{
    NSMutableDictionary* dict = [NSMutableDictionary dictionaryWithCapacity:0];
    NSAppleEventDescriptor* userFieldItems = [desc descriptorForKeyword:keyASUserRecordFields];
    NSInteger numItems = [userFieldItems numberOfItems];

    for ( NSInteger itemIndex = 1; itemIndex <= numItems - 1; itemIndex += 2 ) {
        NSAppleEventDescriptor* keyDesc = [userFieldItems descriptorAtIndex:itemIndex];
        NSAppleEventDescriptor* valueDesc = [userFieldItems descriptorAtIndex:itemIndex + 1];
        NSString* keyString = [keyDesc stringValue];
        id value = [valueDesc objectValue];

        if ( keyString != nil && value != nil )
            [dict setObject:value forKey:keyString];
    }

    return [NSDictionary dictionaryWithDictionary:dict];
}

-(NSAppleEventDescriptor*)scriptingUserDefinedRecordDescriptor
{
    NSAppleEventDescriptor* recordDesc = [NSAppleEventDescriptor recordDescriptor];
    NSAppleEventDescriptor* userFieldDesc = [NSAppleEventDescriptor listDescriptor];
    NSInteger userFieldIndex = 1;

    for ( id key in self ) {
        if ( [key isKindOfClass:[NSString class]] ) {
            NSString* valueString = nil;
            id value = [self objectForKey:key];

            if ( ! [value isKindOfClass:[NSString class]] )
                valueString = [NSString stringWithFormat:@"%@", value];
            else
                valueString = value;

            NSAppleEventDescriptor* valueDesc = [NSAppleEventDescriptor descriptorWithString:valueString];
            NSAppleEventDescriptor* keyDesc = [NSAppleEventDescriptor descriptorWithString:key];

            if ( valueDesc != nil && keyDesc != nil ) {
                [userFieldDesc insertDescriptor:keyDesc atIndex:userFieldIndex++];
                [userFieldDesc insertDescriptor:valueDesc atIndex:userFieldIndex++];
            }
        }
    }

    [recordDesc setDescriptor:userFieldDesc forKeyword:keyASUserRecordFields];

    return recordDesc;
}


@end

@implementation NSArray (UserList)

+(NSArray*)scriptingUserListWithDescriptor:(NSAppleEventDescriptor*)desc
{
    NSMutableArray* array = [NSMutableArray arrayWithCapacity:0];
    NSInteger numItems = [desc numberOfItems];

    for ( NSInteger itemIndex = 1; itemIndex <= numItems; itemIndex++ ) {
        NSAppleEventDescriptor* itemDesc = [desc descriptorAtIndex:itemIndex];

        [array addObject:[itemDesc objectValue]];
    }

    return [NSArray arrayWithArray:array];
}

-(NSAppleEventDescriptor*)scriptingUserListDescriptor
{
    NSAppleEventDescriptor* listDesc = [NSAppleEventDescriptor listDescriptor];
    NSInteger itemIndex = 1;

    for ( id item in self ) {
        NSAppleEventDescriptor* itemDesc = [NSAppleEventDescriptor descriptorWithObject:item];

        [listDesc insertDescriptor:itemDesc atIndex:itemIndex++];
    }

    return listDesc;
}

@end


@implementation NSAppleEventDescriptor (GenericObject)

+(NSAppleEventDescriptor*)descriptorWithObject:(id)object
{
    NSAppleEventDescriptor* desc = nil;

    if ( [object isKindOfClass:[NSArray class]] ) {
        NSArray*    array = (NSArray*)object;

        desc = [array scriptingUserListDescriptor];
    }
    else if ( [object isKindOfClass:[NSDictionary class]] ) {
        NSDictionary*   dict = (NSDictionary*)object;

        desc = [dict scriptingUserDefinedRecordDescriptor];
    }
    else if ( [object isKindOfClass:[NSString class]] ) {
        desc = [NSAppleEventDescriptor descriptorWithString:(NSString*)object];
    }
    else if ( [object isKindOfClass:[NSURL class]] ) {
        desc = [NSAppleEventDescriptor descriptorWithURL:(NSURL*)object];
    }
    else {
        NSString* valueString = [NSString stringWithFormat:@"%@", object];

        desc = [NSAppleEventDescriptor descriptorWithString:valueString];
    }

    return desc;
}

-(id)objectValue
{
    DescType    descType = [self descriptorType];
    DescType    bigEndianDescType = 0;
    id          object = nil;


    switch ( descType ) {
        case typeUnicodeText:
        case typeUTF8Text:
            object = [self stringValue];
            break;
        case typeFileURL:
            object = [self fileURLValue];
            break;
        case typeAEList:
            object = [NSArray scriptingUserListWithDescriptor:self];
            break;
        case typeAERecord:
            object = [NSDictionary scriptingUserDefinedRecordWithDescriptor:self];
            break;
        case typeSInt16:
        case typeUInt16:
        case typeSInt32:
        case typeUInt32:
        case typeSInt64:
        case typeUInt64:
            object = [NSNumber numberWithInteger:(NSInteger)[self int32Value]];
            break;
        default:
            bigEndianDescType = EndianU32_NtoB(descType);
            NSLog(@"Creating NSData for AE desc type %.4s.", (char*)&bigEndianDescType);
            object = [self data];
            break;
    }

    return object;
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Appendix%20C-%20Share%20Metadata.md)


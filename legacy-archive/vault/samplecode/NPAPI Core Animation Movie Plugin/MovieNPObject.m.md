---
title: NPAPI Core Animation Movie Plugin
apple_id: DTS40011209
resource_type: Sample Code
platform: Safari|macOS
topic: General
technology: null
published: '2011-09-06'
source_url: https://developer.apple.com/library/archive/samplecode/NPAPI_Core_Animation_Movie_Plugin/Listings/MovieNPObject_m.html
archived_at: '2026-07-18T03:16:44.827422Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NPAPI Core Animation Movie Plugin](NPAPI%20Core%20Animation%20Movie%20Plugin.md)


[Next](test.html.md)[Previous](MovieNPObject.h.md)

# MovieNPObject.m

```objc
/*
 File: MovieNPObject.m
 Version: 1.0

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

 Copyright (C) 2011 Apple Inc. All Rights Reserved.

 */

#import "MovieNPObject.h"

#import <QTKit/QTKit.h>
#import <WebKit/npfunctions.h>

extern NPNetscapeFuncs* browser;


typedef struct {
    // Put the NPObject first so that casting from an NPObject to a 
    // MovieNPObject works as expected.
    NPObject npObject;

    QTMovie *movie;
} MovieNPObject;

enum {
    ID_PLAY,
    ID_PAUSE,
    NUM_METHOD_IDENTIFIERS
};

static NPIdentifier methodIdentifiers[NUM_METHOD_IDENTIFIERS];
static const NPUTF8 *methodIdentifierNames[NUM_METHOD_IDENTIFIERS] = {
    "play",
    "pause",
};

static void initializeIdentifiers(void)
{
    static bool identifiersInitialized;
    if (identifiersInitialized)
        return;

    // Take all method identifier names and convert them to NPIdentifiers.
    browser->getstringidentifiers(methodIdentifierNames, NUM_METHOD_IDENTIFIERS, methodIdentifiers);
    identifiersInitialized = true;
}

static NPObject *movieNPObjectAllocate(NPP npp, NPClass* theClass)
{
    initializeIdentifiers();

    MovieNPObject *movieNPObject = malloc(sizeof(MovieNPObject));
    movieNPObject->movie = 0;

    return (NPObject *)movieNPObject;
}

static void movieNPObjectDeallocate(NPObject *npObject)
{
    MovieNPObject *movieNPObject = (MovieNPObject *)npObject;

    // Release the QTMovie object that this NPObject wraps.
    [movieNPObject->movie release];

    // Free the NPObject memory.
    free(movieNPObject);
}

static bool movieNPObjectHasMethod(NPObject *obj, NPIdentifier name)
{
    // Loop over all the method NPIdentifiers and see if we expose the given method.
    for (int i = 0; i < NUM_METHOD_IDENTIFIERS; i++) {
        if (name == methodIdentifiers[i])
            return true;
    }

    return false;
}

static bool movieNPObjectInvoke(NPObject *npObject, NPIdentifier name, const NPVariant* args, uint32_t argCount, NPVariant* result)
{
    MovieNPObject *movieNPObject = (MovieNPObject *)npObject;

    if (name == methodIdentifiers[ID_PLAY]) {
        [movieNPObject->movie play];
        return true;
    }

    if (name == methodIdentifiers[ID_PAUSE]) {
        [movieNPObject->movie stop];
        return true;
    }

    return false;
}

static NPClass movieNPClass = {
    NP_CLASS_STRUCT_VERSION,
    movieNPObjectAllocate, // NP_Allocate
    movieNPObjectDeallocate, // NP_Deallocate
    0, // NP_Invalidate
    movieNPObjectHasMethod, // NP_HasMethod
    movieNPObjectInvoke, // NP_Invoke
    0, // NP_InvokeDefault
    0, // NP_HasProperty
    0, // NP_GetProperty
    0, // NP_SetProperty
    0, // NP_RemoveProperty
    0, // NP_Enumerate
    0, // NP_Construct
};

NPObject *createMovieNPObject(NPP npp, QTMovie *movie)
{
    MovieNPObject *movieNPObject = (MovieNPObject *)browser->createobject(npp, &movieNPClass);

    movieNPObject->movie = [movie retain];

    return (NPObject *)movieNPObject;
}
```

[Next](test.html.md)[Previous](MovieNPObject.h.md)


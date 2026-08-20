---
title: Plug-in Programming Topics
apple_id: 10000128i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2005-03-03'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPlugIns/Tasks/GeneratingUUID.html
archived_at: '2026-07-15T07:22:40.660555Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Plug-in Programming Topics](Introduction%20to%20Plug-ins.md)


[Next](Document%20Revision%20History.md)[Previous](Loading%20and%20Using%20a%20Plug-in.md)

# Generating a UUID Programmatically

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3dmljrgm3dqmbqfvbecsseizfeera) shows you how to generate a UUID programmatically using CFUUID functions. Plug-ins use UUIDs to uniquely identify types, interfaces, and factories.

__Listing 1__  Generating a UUID programmatically

```
CFUUIDRef     myUUID;
CFStringRef   myUUIDString;
char          strBuffer[100];

myUUID = CFUUIDCreate(kCFAllocatorDefault);
myUUIDString = CFUUIDCreateString(kCFAllocatorDefault, myUUID);

// This is the safest way to obtain a C string from a CFString.
CFStringGetCString(myUUIDString, strBuffer, 100, kCFStringEncodingASCII);

CFStringRef outputString =
    CFStringCreateWithFormat(kCFAllocatorDefault,
                             NULL,
                             CFSTR("My UUID is: %s!\n"),
                             strBuffer);
CFShow(outputString);
```

[Next](Document%20Revision%20History.md)[Previous](Loading%20and%20Using%20a%20Plug-in.md)


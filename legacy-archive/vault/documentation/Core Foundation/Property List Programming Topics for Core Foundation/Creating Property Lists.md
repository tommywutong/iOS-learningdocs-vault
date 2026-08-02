---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Creating.html
archived_at: '2026-07-15T07:22:45.565758Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Property List Programming Topics for Core Foundation](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Saving%20and%20Restoring%20Property%20Lists.md)[Previous](Property%20List%20Structure%20and%20Contents.md)

# Creating Property Lists

The examples in this section demonstrate how to create and work with property lists. The error checking code has been removed for clarity. In practice, it is _vital_ that you check for errors because passing bad parameters into Core Foundation routines can cause your application to crash.

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tiljrgaydsobqfvbegskgijbecqq) shows you how to create a very simple property list—an array of CFString objects.

__Listing 1__  Creating a simple property list from an array

```c
#include <CoreFoundation/CoreFoundation.h>
#define kNumNames 6

void main () {

    CFStringRef names[kNumNames];
    names[0] = CFSTR("Steve");
    names[1] = CFSTR("Susan");
    names[2] = CFSTR("Sally");
    names[3] = CFSTR("Patrick");
    names[4] = CFSTR("Jeff");
    names[5] = CFSTR("Jane");

    // Create a property list using the string array of names
    CFArrayRef array = CFArrayCreate(kCFAllocatorDefault, (const void **)names,
                kNumNames, &kCFTypeArrayCallBacks);

    // Convert the plist into XML data
    CFErrorRef myError;
    CFDataRef xmlData = CFPropertyListCreateData(kCFAllocatorDefault, array, kCFPropertyListXMLFormat_v1_0, 0, &myError);

    // Check for errors, do things with the data

    // Clean up CF objects.
    CFRelease(array);
    CFRelease(xmlData);
    CFRelease(myError);
}
```

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tiljrgaytknrsfvbegskeiveuuri) shows how the contents of `xmlData`, created in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tiljrgaydsobqfvbegskgijbecqq), would look if printed to the screen.

__Listing 2__  XML created by the sample program

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <string>Steve</string>
    <string>Susan</string>
    <string>Sally</string>
    <string>Patrick</string>
    <string>Jeff</string>
    <string>Jane</string>
</array>
</plist>
```

[Next](Saving%20and%20Restoring%20Property%20Lists.md)[Previous](Property%20List%20Structure%20and%20Contents.md)


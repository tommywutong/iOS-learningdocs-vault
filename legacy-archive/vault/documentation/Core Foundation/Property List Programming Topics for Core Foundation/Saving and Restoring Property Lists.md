---
title: Property List Programming Topics for Core Foundation
apple_id: 10000130i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreFoundation
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/Articles/Saving.html
archived_at: '2026-07-15T07:22:46.609618Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Property List Programming Topics for Core Foundation](Introduction%20to%20Property%20List%20Programming%20Topics%20for%20Core%20Foundation.md)


[Next](Using%20Numbers%20in%20Property%20Lists.md)[Previous](Creating%20Property%20Lists.md)

# Saving and Restoring Property Lists

[Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tkljrgeydcnbvfvbegskei5bussa) shows you how to create a property list, convert it to XML, write it to disk, and then re-create the original data structure using the saved XML. For more information about using CFDictionary objects see _[Collections Programming Topics for Core Foundation](../Collections%20Programming%20Topics%20for%20Core%20Foundation/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdi2i)_.

__Listing 1__  Saving and restoring property list data

```c
#include <CoreFoundation/CoreFoundation.h>

#define kNumKids 2
#define kNumBytesInPic 10

CFDictionaryRef CreateMyDictionary(void);
CFPropertyListRef CreateMyPropertyListFromFile(CFURLRef fileURL);
void WriteMyPropertyListToFile(CFPropertyListRef propertyList, CFURLRef fileURL);

int main () {

    // Construct a complex dictionary object;
    CFPropertyListRef propertyList = CreateMyDictionary();

    // Create a URL specifying the file to hold the XML data.
    CFURLRef fileURL = CFURLCreateWithFileSystemPath(kCFAllocatorDefault,
                           CFSTR("test.txt"),      // file path name
                           kCFURLPOSIXPathStyle,   // interpret as POSIX path
                           false);                 // is it a directory?

    // Write the property list to the file.
    WriteMyPropertyListToFile(propertyList, fileURL);
    CFRelease(propertyList);

    // Recreate the property list from the file.
    propertyList = CreateMyPropertyListFromFile(fileURL);

    // Release objects we created.
    CFRelease(propertyList);
    CFRelease(fileURL);
    return 0;
}

CFDictionaryRef CreateMyDictionary(void) {

    // Create a dictionary that will hold the data.
    CFMutableDictionaryRef dict = CFDictionaryCreateMutable(kCFAllocatorDefault, 0,
                                       &kCFTypeDictionaryKeyCallBacks,
                                       &kCFTypeDictionaryValueCallBacks);

    /*
     Put various items into the dictionary.
     Values are retained as they are placed into the dictionary, so any values
     that are created can be released after being added to the dictionary.
    */

    CFDictionarySetValue(dict, CFSTR("Name"), CFSTR("John Doe"));

    CFDictionarySetValue(dict, CFSTR("City of Birth"), CFSTR("Springfield"));

    int yearOfBirth = 1965;
    CFNumberRef num = CFNumberCreate(kCFAllocatorDefault, kCFNumberIntType, &yearOfBirth);
    CFDictionarySetValue(dict, CFSTR("Year Of Birth"), num);
    CFRelease(num);

    CFStringRef kidsNames[kNumKids];
    // Define some data.
    kidsNames[0] = CFSTR("John");
    kidsNames[1] = CFSTR("Kyra");
    CFArrayRef array = CFArrayCreate(kCFAllocatorDefault,
                           (const void **)kidsNames,
                           kNumKids,
                           &kCFTypeArrayCallBacks);
    CFDictionarySetValue(dict, CFSTR("Kids Names"), array);
    CFRelease(array);

    array = CFArrayCreate(kCFAllocatorDefault, NULL, 0, &kCFTypeArrayCallBacks);
    CFDictionarySetValue(dict, CFSTR("Pets Names"), array);
    CFRelease(array);

    // Fake data to stand in for a picture of John Doe.
    const unsigned char pic[kNumBytesInPic] = {0x3c, 0x42, 0x81,
             0xa5, 0x81, 0xa5, 0x99, 0x81, 0x42, 0x3c};
    CFDataRef data = CFDataCreate(kCFAllocatorDefault, pic, kNumBytesInPic);
    CFDictionarySetValue(dict, CFSTR("Picture"), data);
    CFRelease(data);

    return dict;
}

void WriteMyPropertyListToFile(CFPropertyListRef propertyList, CFURLRef fileURL) {

    // Convert the property list into XML data
    CFErrorRef myError;
    CFDataRef xmlData = CFPropertyListCreateData(
                 kCFAllocatorDefault, propertyList, kCFPropertyListXMLFormat_v1_0, 0, &myError);
    // Handle any errors

    // Write the XML data to the file.
    SInt32 errorCode;
    Boolean status = CFURLWriteDataAndPropertiesToResource(
                        fileURL, xmlData, NULL, &errorCode);

    if (!status) {
        // Handle the error.
    }
    CFRelease(xmlData);
    CFRelease(myError);
}

CFPropertyListRef CreateMyPropertyListFromFile(CFURLRef fileURL) {

    // Read the XML file
    CFDataRef resourceData;
    SInt32 errorCode;
    Boolean status = CFURLCreateDataAndPropertiesFromResource(
               kCFAllocatorDefault, fileURL, &resourceData,
               NULL, NULL, &errorCode);

    if (!status) {
        // Handle the error
    }
    // Reconstitute the dictionary using the XML data
    CFErrorRef myError;
    CFPropertyListRef propertyList = CFPropertyListCreateWithData(
                          kCFAllocatorDefault, resourceData, kCFPropertyListImmutable, NULL, &myError);

    // Handle any errors

    CFRelease(resourceData);
    CFRelease(myError);
    return propertyList;
}
```

[Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tkljrgaytknrwfvbegskcinceqqq) shows how the contents of `xmlData`, created in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrge3tkljrgeydcnbvfvbegskei5bussa), would look if printed to the screen.

__Listing 2__  XML file contents created by the sample program

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
        "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Year Of Birth</key>
    <integer>1965</integer>
    <key>Pets Names</key>
    <array/>
    <key>Picture</key>
    <data>
        PEKBpYGlmYFCPA==
    </data>
    <key>City of Birth</key>
    <string>Springfield</string>
    <key>Name</key>
    <string>John Doe</string>
    <key>Kids Names</key>
    <array>
        <string>John</string>
        <string>Kyra</string>
    </array>
</dict>
</plist>
```

[Next](Using%20Numbers%20in%20Property%20Lists.md)[Previous](Creating%20Property%20Lists.md)


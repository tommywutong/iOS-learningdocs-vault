---
title: Adding Unicode characters to Text Media in a Text Track
apple_id: DTS10003772
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-19'
source_url: https://developer.apple.com/library/archive/qa/qa1400/_index.html
archived_at: '2026-07-18T02:30:31.555661Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1400

# Adding Unicode characters to Text Media in a Text Track

## Q:  I am able to add English language text samples to text media in a text track using `TextMediaAddTESample`. But when I try to pass Unicode Japanese text my movie shows the text as unreadable characters. Is it possible to add text samples other than English to text media in a text track using `TextMediaAddTESample`? Also, can I pass my text as a `CFString` to `TextMediaAddTESample` and others?

A: You can't pass Unicode characters to `TextMediaAddTESample` -- instead, use `TextMediaAddTextSample`. You can pass `TextMediaAddTextSample` UTF-16 characters prepended with a byte order marker (BOM) to indicate endianess.

You can't pass your text as a `CFString` to `TextMediaAddTextSample`; you must pass a buffer with the raw array of Unicode characters (and if you are passing UTF-16 these must include a BOM).

Also, before adding your text you need to tell the Text Media Handler the added sample is encoded in Unicode with a BOM. You do this with the `TextMediaSetTextSampleData` API as follows:


```
 // tell the text media handler the upcoming text sample is
    // encoded in Unicode with a byte order mark (BOM)

    SInt32 dataPtr = kTextEncodingUnicodeDefault;
    ComponentResult myErr =
        TextMediaSetTextSampleData (inTextMediaHandler,
                                    (void *)&dataPtr,
                                    kTXNTextEncodingAttribute);
```

Lastly, you should specify a media's localized language or region code using the `SetMediaLanguage` API. This will avoid unexpected errors in any text encoding conversion (if a conversion is necessary). Also, it will help QuickTime select an alternate language track if one is provided.


```
 // Set the language of the text track media to the desired value
    SetMediaLanguage (inMedia, langJapanese /* your language here */);
```

Here's a code snippet which shows how to add UTF-16 characters with a prepended BOM to a text media:

__Listing 1__  Adding UTF-16 characters with a prepended BOM to a text media.

```
//
// DoAddUTF16ToTextMedia
//
// Create some UTF-16 characters and add them to a given text media
//
//    inMedia - text media for your text track sample data
//

ComponentResult DoAddUTF16ToTextMedia(Media inMedia)
{
    // Set the language of the text track media to the desired value
    SetMediaLanguage (inMedia, langJapanese /* your language here */);
    ComponentResult myErr = GetMoviesError ();
    require(myErr == noErr, SETMEDIALANG);

    // Make a buffer of UTF16 characters, preceded by
    // a BOM (byte order marker)
    CFDataRef charData = MakeUTF16Characters();
    require(nil != charData, MAKECHARS);

    Rect myTextBounds = {0,0,200,100}; // text box within which the text
                                       // is to be displayed

    // Add the UTF16 characters to our text media
    myErr = TextMedia_AddUTF16Text( GetMediaHandler(inMedia),
                                      &myTextBounds,
                                      GetMediaTimeScale(inMedia),
                                      (char *)CFDataGetBytePtr (charData),
                                      CFDataGetLength (charData)
                                    );
    CFRelease(charData);

SETMEDIALANG:
MAKECHARS:

    return myErr;
}


//
// TextMedia_AddUTF16Text
//
// Adds UTF16 styled text to an existing media.
//

ComponentResult TextMedia_AddUTF16Text( MediaHandler    inTextMediaHandler,
                                          Rect            *inTextBox,
                                          TimeValue       inDuration,
                                          Ptr             inChars,
                                          SInt32          inCharLen)
{
    // tell the text media handler the upcoming text sample is
    // encoded in Unicode with a byte order mark (BOM)
    SInt32 dataPtr = kTextEncodingUnicodeDefault;
    FourCharCode txtEncodingAttribute = 'encd';
    ComponentResult myErr = TextMediaSetTextSampleData (inTextMediaHandler,
                                                        (void *)&dataPtr,
                                                        txtEncodingAttribute);
    require(myErr == noErr, SETTEXTDATA);

    // specify the desired font name here!
    ATSFontFamilyRef fontRef = ATSFontFamilyFindFromQuickDrawName("Osaka");

    // write out the new text sample data to the media
    myErr = TextMediaAddTextSample( inTextMediaHandler,
                                    inChars,
                                    inCharLen,
                                    fontRef,        // font number
                                    12,             // font size
                                    normal,         // text face
                                    NULL,
                                    NULL,
                                    teCenter,
                                    inTextBox,
                                    dfClipToTextBox,
                                    0,
                                    0,
                                    0,
                                    NULL,
                                    inDuration,
                                    NULL);

SETTEXTDATA:

    return myErr;
}


//
// MakeUTF16Characters
//
// Returns a CFData object filled with some
// UTF16 characters preceded by a BOM (byte
// order marker)
//

CFDataRef MakeUTF16Characters()
{
    // Make a CFString of some Japanese characters to add to our text track
    UniChar uniBuf[] = { 0x30A1, 0x30A2, 0x30A3, 0x30A4, 0x30A5, 0x30A6 };
    CFStringRef stringRef =
            CFStringCreateWithCharacters(NULL,
                                        uniBuf,
                                        sizeof(uniBuf) / sizeof(UniChar));
    require(stringRef != nil, CREATESTRING);

    // Make a CFData object that stores the characters of the CFString as an
    // "external representation.". If the encoding of the characters in the
    // data object is Unicode, the function inserts a BOM (byte order marker)
    // to indicate endianness.

    // Note:
    //
    // kCFStringEncodingUTF16 here means to use native endian (big endian
    // on PPC, little endian on Intel)
    //
    // Use kCFStringEncodingUTF16BE if you want big endian
    //
    CFDataRef data =
        CFStringCreateExternalRepresentation
                                    (NULL,
                                     stringRef,
                                     kCFStringEncodingUTF16, // native endian
                                     0);
    require(data != nil, CREATEEXTERNALREP);

    CFRelease(stringRef);

    return data;

CREATESTRING:
CREATEEXTERNALREP:

    return nil;

}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-19 | Editorial |
| 2005-09-01 | New document that describes how to add Unicode characters to text media in a text track |


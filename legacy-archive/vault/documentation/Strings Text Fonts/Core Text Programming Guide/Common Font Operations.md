---
title: Core Text Programming Guide
apple_id: TP40005533
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: CoreText
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/CoreText_Programming/FontOperations/FontOperations.html
archived_at: '2026-07-18T02:06:51.637148Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Core Text Programming Guide](About%20Core%20Text.md)


[Next](Document%20Revision%20History.md)[Previous](Common%20Text%20Layout%20Operations.md)

# Common Font Operations

This chapter describes some common font-handling operations and shows how to code them using Core Text. These operations are the same on iOS and OS X. The following operations with code listings are included in this chapter:

- [Creating Font Descriptors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltcny)
- [Creating a Font from a Font Descriptor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltq)
- [Creating Related Fonts](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltemi)
- [Serializing a Font](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknlteni)
- [Creating a Font from Serialized Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltenq)
- [Changing Kerning](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknlteny)
- [Getting Glyphs for Characters](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltcmq)

The example function in Listing 3-1 creates a font descriptor from parameter values specifying a PostScript font name and the point size.

__Listing 3-1__  Creating a font descriptor from a name and point size

```
CTFontDescriptorRef CreateFontDescriptorFromName(CFStringRef postScriptName,
                                                  CGFloat size)
{
    return CTFontDescriptorCreateWithNameAndSize(postScriptName, size);
}
```

The example function in Listing 3-2 creates a font descriptor from a font family name and font traits.

__Listing 3-2__  Creating a font descriptor from a family and traits

```
NSString* familyName = @"Papyrus";
CTFontSymbolicTraits symbolicTraits = kCTFontTraitCondensed;
CGFloat size = 24.0;

NSMutableDictionary* attributes = [NSMutableDictionary dictionary];
[attributes setObject:familyName forKey:(id)kCTFontFamilyNameAttribute];

// The attributes dictionary contains another dictionary, the traits dictionary,
// which in this example specifies only the symbolic traits.
NSMutableDictionary* traits = [NSMutableDictionary dictionary];
[traits setObject:[NSNumber numberWithUnsignedInt:symbolicTraits]
                                           forKey:(id)kCTFontSymbolicTrait];

[attributes setObject:traits forKey:(id)kCTFontTraitsAttribute];
[attributes setObject:[NSNumber numberWithFloat:size]
                                         forKey:(id)kCTFontSizeAttribute];

CTFontDescriptorRef descriptor =
             CTFontDescriptorCreateWithAttributes((CFDictionaryRef)attributes);
CFRelease(descriptor);
```


[Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknlto) shows how to create a font descriptor and use it to create a font. When you call [CTFontCreateWithFontDescriptor](https://developer.apple.com/documentation/coretext/1509056-ctfontcreatewithfontdescriptor), you usually pass `NULL` for the matrix parameter to specify the default (identity) matrix. The size and matrix (second and third) parameters of [CTFontCreateWithFontDescriptor](https://developer.apple.com/documentation/coretext/1509056-ctfontcreatewithfontdescriptor) override any specified in the font descriptor unless they are unspecified (`0.0` for size and `NULL` for matrix).

__Listing 3-3__  Creating a font from a font descriptor

```
NSDictionary *fontAttributes =
                  [NSDictionary dictionaryWithObjectsAndKeys:
                          @"Courier", (NSString *)kCTFontFamilyNameAttribute,
                          @"Bold", (NSString *)kCTFontStyleNameAttribute,
                          [NSNumber numberWithFloat:16.0],
                          (NSString *)kCTFontSizeAttribute,
                          nil];
// Create a descriptor.
CTFontDescriptorRef descriptor =
          CTFontDescriptorCreateWithAttributes((CFDictionaryRef)fontAttributes);

// Create a font using the descriptor.
CTFontRef font = CTFontCreateWithFontDescriptor(descriptor, 0.0, NULL);
CFRelease(descriptor);
```


It is often useful to convert an existing font to a related or similar font. The example function in [Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltcna) shows how to make a font bold or unbold based on the value of the Boolean parameter passed with the function call. If the current font family does not have the requested style, the function returns `NULL`.

__Listing 3-4__  Changing traits of a font

```
CTFontRef CreateBoldFont(CTFontRef font, Boolean makeBold)
{
    CTFontSymbolicTraits desiredTrait = 0;
    CTFontSymbolicTraits traitMask;

    // If requesting that the font be bold, set the desired trait
    // to be bold.
    if (makeBold) desiredTrait = kCTFontBoldTrait;

    // Mask off the bold trait to indicate that it is the only trait
    // to be modified. As CTFontSymbolicTraits is a bit field,
    // could change multiple traits if desired.
    traitMask = kCTFontBoldTrait;

    // Create a copy of the original font with the masked trait set to the
    // desired value. If the font family does not have the appropriate style,
    // returns NULL.

    return CTFontCreateCopyWithSymbolicTraits(font, 0.0, NULL, desiredTrait, traitMask);
}
```

The example function in Listing 3-8 converts a given font to a similar font in another font family, preserving traits if possible. It may return `NULL`. Passing in `0.0` for the size parameter and `NULL` for the matrix parameter preserves the size from the original font.

__Listing 3-5__  Converting a font to another family

```
CTFontRef CreateFontConvertedToFamily(CTFontRef font, CFStringRef family)
{
    // Create a copy of the original font with the new family. This call
    // attempts to preserve traits, and may return NULL if that is not possible.
    // Pass in 0.0 and NULL for size and matrix to preserve the values from
    // the original font.

    return CTFontCreateCopyWithFamily(font, 0.0, NULL, family);
}
```


The example function in Listing 3-6 shows how to create XML data to serialize a font that can be embedded in a document. Alternatively, and preferably, `NSArchiver` could be used. This is just one way to accomplish this task, but it preserves all data from the font needed to recreate the exact font at a later time.

__Listing 3-6__  Serializing a font

```
CFDataRef CreateFlattenedFontData(CTFontRef font)
{
    CFDataRef           result = NULL;
    CTFontDescriptorRef descriptor;
    CFDictionaryRef     attributes;

    // Get the font descriptor for the font.
    descriptor = CTFontCopyFontDescriptor(font);

    if (descriptor != NULL) {
        // Get the font attributes from the descriptor. This should be enough
        // information to recreate the descriptor and the font later.
        attributes = CTFontDescriptorCopyAttributes(descriptor);

        if (attributes != NULL) {
            // If attributes are a valid property list, directly flatten
            // the property list. Otherwise we may need to analyze the attributes
            // and remove or manually convert them to serializable forms.
            // This is left as an exercise for the reader.
           if (CFPropertyListIsValid(attributes, kCFPropertyListXMLFormat_v1_0)) {
                result = CFPropertyListCreateXMLData(kCFAllocatorDefault, attributes);
            }
        }
    }
    return result;
}
```


The example function in Listing 3-7 shows how to create a font reference from flattened XML data. It shows how to unflatten font attributes and create a font with those attributes.

__Listing 3-7__  Creating a font from serialized data

```
CTFontRef CreateFontFromFlattenedFontData(CFDataRef iData)
{
    CTFontRef           font = NULL;
    CFDictionaryRef     attributes;
    CTFontDescriptorRef descriptor;

    // Create our font attributes from the property list.
    // For simplicity, this example creates an immutable object.
    // If you needed to massage or convert certain attributes
    // from their serializable form to the Core Text usable form,
    // do it here.
    attributes =
          (CFDictionaryRef)CFPropertyListCreateFromXMLData(
                               kCFAllocatorDefault,
                               iData, kCFPropertyListImmutable, NULL);
    if (attributes != NULL) {
        // Create the font descriptor from the attributes.
        descriptor = CTFontDescriptorCreateWithAttributes(attributes);
        if (descriptor != NULL) {
            // Create the font from the font descriptor. This sample uses
            // 0.0 and NULL for the size and matrix parameters. This
            // causes the font to be created with the size and/or matrix
            // that exist in the descriptor, if present. Otherwise default
            // values are used.
            font = CTFontCreateWithFontDescriptor(descriptor, 0.0, NULL);
        }
    }
    return font;
}
```


Ligatures and kerning are enabled by default. To disable, set the `kCTKernAttributeName` attribute to `0`. [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tkmztfvbuqnbnknltcni) sets the kern size to a large number for the first few characters drawn.

__Listing 3-8__  Setting kerning

```
 // Set the color of the first 13 characters to red
 // using a previously defined red CGColor object.
 CFAttributedStringSetAttribute(attrString, CFRangeMake(0, 13),
                                      kCTForegroundColorAttributeName, red);

 // Set kerning between the first 18 chars to be 20
 CGFloat otherNum = 20;
 CFNumberRef otherCFNum = CFNumberCreate(NULL, kCFNumberCGFloatType, &otherNum);
 CFAttributedStringSetAttribute(attrString, CFRangeMake(0,18),
                                           kCTKernAttributeName, otherCFNum);
```


Listing 3-9 shows how to get glyphs for the characters in a string with a single font. Most of the time you should just use a CTLine object to get this information because one font may not encode the entire string. In addition, simple character-to-glyph mapping will not get the correct appearance for complex scripts. This simple glyph mapping may be appropriate if you are trying to display specific Unicode characters for a font.

__Listing 3-9__  Getting glyphs for characters

```
void GetGlyphsForCharacters(CTFontRef font, CFStringRef string)
{
    // Get the string length.
    CFIndex count = CFStringGetLength(string);

    // Allocate our buffers for characters and glyphs.
    UniChar *characters = (UniChar *)malloc(sizeof(UniChar) * count);
    CGGlyph *glyphs = (CGGlyph *)malloc(sizeof(CGGlyph) * count);

    // Get the characters from the string.
    CFStringGetCharacters(string, CFRangeMake(0, count), characters);

    // Get the glyphs for the characters.
    CTFontGetGlyphsForCharacters(font, characters, glyphs, count);

    // Do something with the glyphs here. Characters not mapped by this font will be zero.
    // ...

    // Free the buffers
    free(characters);
    free(glyphs);
}
```

[Next](Document%20Revision%20History.md)[Previous](Common%20Text%20Layout%20Operations.md)


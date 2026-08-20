---
title: ATSUI Programming Guide
apple_id: TP30000984
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-09-30'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/ATSUI_Concepts/atsui_chap6/atsui_adv_tasks.html
archived_at: '2026-07-15T05:22:22.124828Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [ATSUI Programming Guide](Introduction%20to%20ATSUI%20Programming%20Guide.md)


[Next](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md)[Previous](Interactive%20Tasks-%20Supporting%20Carets%20and%20Highlighting%20Text.md)

# Advanced Tasks: Substituting Fonts and Modifying Layouts

The tasks described in this chapter provide examples of some of the more sophisticated ways you can use ATSUI to control how Unicode text is rendered. Before you read this chapter you should be familiar with the tasks outlined in Chapter 4, [Basic Tasks: Working With Objects and Drawing Text](Basic%20Tasks-%20Working%20With%20Objects%20and%20Drawing%20Text.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzqfvkfami).

This chapter provides information on advanced tasks in the following sections:

- [Using Font Fallback Objects](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcmzy) shows how to create and use a font fallback object to specify how ATSUI should search for a substitute font when a glyph is unavailable.
- [Setting a Baseline](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnbr) describes how to draw a line of text whose glyphs use different baselines. In particular, you’ll see how to draw drop capitals.
- [Kerning Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnbw) explains how to adjust the overlap between glyphs, including how to suppress the kerning specified by the font designer.
- [Adjusting Interglyph Positions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnby) shows how to change the normal tracking setting for a font.
- [Retrieving Glyph Metrics](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcmzx) explains how to obtain resolution-independent and resolution-dependent metrics for a glyph.

If you want to use ATSUI to manipulate glyph data directly, you should read [Direct-Access Tasks: Working With Glyph Data](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamztfvkfami), [Direct-Access Tasks: Working With Glyph Data](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamztfvkfami).

This chapter provides a number of code samples to illustrate how to substitute fonts and modify text layout. You can obtain the sample applications from which this code is taken, as well as additional code samples, from the developer sample code website:

[http://developer.apple.com/samplecode/](https://developer.apple.com/samplecode/)

There may be situations in which ATSUI cannot draw a glyph with the assigned font because the font does not have the glyph in its repertoire. In these cases, you can turn on automatic font substitution by calling the function `ATSUSetTransientFontMatching`. This function is applied to a text layout object; you need to call it for each text layout object that needs automatic font substitution. You can also use this function to turn off automatic font substitution.

You can use the function `ATSUSetTransientFontMatching` to set up ATSUI to scan all valid fonts on the user’s system until it finds a suitable substitute font. The substitute font is the first valid font ATSUI finds. If ATSUI doesn’t find any suitable replacements for a font, it uses a glyph from the Last Resort font to represent unavailable characters.

If you want ATSUI to identify a substitute font, but you do not want ATSUI to automatically perform the font substitution, you can call the function `ATSUMatchFontsToText`.

When you use transient font matching, you can specify one of the following search methods for finding a font match:

- `kATSUDefaultFontFallbacks` specifies to use ATSUI’s default font search method. ATSUI searches through all available fonts on the system for one that matches any text that cannot be drawn with the font specified in the current ATSU style object (`ATSUStyle`). ATSUI first searches in the standard application fonts for various languages. If that fails, it searches through the remaining fonts on the system in whatever order the Font Manager returns them. After ATSUI has searched all the fonts in the system, any unmatched text is drawn with the last-resort font.
- `kATSULastResortOnlyFontFallbacks` specifies that ATSUI should use the Last Resort font if the assigned font does not contain the needed glyphs.
- `kATSUSequentialFallbacksPreferred` specifies that ATSUI should first search sequentially through the list of supplied fonts before it searching through all available fonts on the system.
- `kATSUSequentialFallbacksExclusive` specifies that ATSUI should search exclusively through the list of supplied fonts. ATSUI use the Last Resort font if it does not find a match in the list of supplied fonts.

If you want to specify a search order, then you must create a font fallback object and call the function `ATSUSetObjFontFallbacks` to associate a font fallback method with the font fallback object. This function takes the following parameters:

- `iFontFallbacks` ,a font fallback object created by calling the function `ATSUCreateFontFallbacks`.
- `iFontFallbacksCount`, a value that specifies the number of fonts ATSUI is to search. Typically this is the number of font IDs in the `iFonts` array.
- `iFonts`, a pointer to the first `ATSUFontID` value in an array of the font IDs that you want ATSUI to search.
- `iFontFallbackMethod`, a constant that specifies a font fallback method that identifies the order in which ATSUI is to search.

After you’ve associated a font fallback search method with a font fallback object, you can call the function `ATSUSetLayoutControls` to associate the font fallback object with a text layout object.

The code in listing Listing 5-1 shows how to create a font fallback object, associate a font fallback method with it, and then associate the font fallback object with a text layout object. A detailed explanation for each numbered line of code follows the listing.

__Listing 5-1__  Code that creates and sets up a font fallback object for a text layout object

```
ATSUFontFallbacks       myFontFallbacks;// 1
ATSUAttributeTag        theTags[2];// 2
ByteCount               theSizes[2];
ATSUAttributeValuePtr   theValues

ATSUCreateFontFallbacks (&myFontFallbacks);// 3
ATSUSetObjFontFallbacks (myFontFallbacks,
                        myNumFontIDs,
                        &myFontIDArray,
                        kATSUSequentialFallbacksPreferred);// 4
theTags[0]      = kATSULineFontFallbacksTag;// 5
theSizes[0]     = sizeof (ATSUFontFallbacks);
theValues[0]    = &myFontFallbacks;

ATSUSetLayoutControls (myLayout, 1, theTags, theSizes, theValues);// 6
ATSUSetTransientFontMatching (myLayout, true);// 7
```

Here’s what the code does:

1. Declares storage for the font fallback object.
2. Declares variables for a triple (attribute tag, size, value).
3. Calls the function `ATSUCreateFontFallbacks` to create an opaque font fallback object.
4. Calls the function `ATSUSetObjFontFallbacks` to assign a font-search method (`kATSUSequentialFallbacksPreferred`) to the font fallback object. The number of fonts in the font list is `myNumFontIDs`, and the font list is `myFontIDArray`. This means ATSUI first searches sequentially through the list of fonts specified in the array `myFontIDArray`. If a font is not found, then ATSUI searches in other fonts available in the user’s system.
5. Sets up a triple (tag, size, value) to specify the font fallback object you want to associate with the text layout object.
6. Calls the function `ATSUSetLayoutControls` to associate the triple with the text layout object whose font-search method you want to specify.
7. Calls the function `ATSUSetTransientFontMatching` to turn on transient font matching for this text layout object. Associating the font fallback object with the text layout object doesn’t have an effect unless transient font matching is turned on.

ATSUI lets you modify the baseline in two ways:

- You can set a baseline other than that specified by the font.
- You can specify baseline delta values to use when ATSUI draws text.

You set a baseline by specifying a baseline class value for the baseline class attribute tag (`kATSUBaselineClassTag`). The most common baseline classes are listed in Table 5-1. Baseline classes are specified by a font designer and are not available unless the font designer has chosen to specify them.

Baseline delta values specify how much (in points) to deviate from the current baseline. Positive delta values specify a location above the current baseline and negative values specify a location below the current baseline. You set the baseline delta values by specifying an array of delta values for the baseline values attribute tag (`kATSULineBaselineValuesTag`).

__Table 5-1__  Common baseline classes

| Baseline class | Specifies |
| `kBSLNRomanBaseline` | A baseline on which glyphs sit. |
| `kBSLNIdeographicCenterBaseline` | A font-defined baseline on which to center ideographs. |
| `kBSLNIdesographicLowBaseline` | A font-defined baseline on which ideographs are drawn. |
| `kBSLNHangingBaseline` | A font-defined baseline from which glyphs hang. |
| `kBSLNMathBaseline` | A font-defined baseline on which to position mathematical symbols. |
| `kBSLNLastBaseline` | The last baseline. |
| `kBSLNNumBaselineClasses` | The number of baseline classes. You can use this value if you need to iterate through baseline classes. |
| `kBSLNNoBaselineOverride` | The standard baseline setting from the current font. |

To set a baseline, you need to perform these tasks:

1. Set up a style object for the baseline class you want to use.

   You can reuse this style as needed. [Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnrw) shows a function that sets up a style object for a baseline class. The function sets up a triple (tag, size, value) for the baseline class style attribute. A detailed explanation for each numbered line of code appears following the listing.
2. Apply the style object to the appropriate runs of text in your text layout object.
3. Calculate baseline delta values for the text associated with your text layout object.

   You call the function `ATSUCalculateBaselineDeltas`, passing the style object for which you want to calculate baseline delta values, the baseline class to use, and an array (`BslnBaselineRcord`) of `Fixed` values. On output, the array contains baseline offsets that specify distances in points from the default baseline to each of the other baseline types in the style object.
4. Associate the baseline delta values with your text layout object.

   [Listing 5-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvbeeq2kineeqsq) shows a function that sets up baseline delta values for a text layout object. The function sets up a triple (tag, size, value) for the baseline value layout attribute. A detailed explanation for each numbered line of code appears following the listing.
5. Draw the text.

__Listing 5-2__  A function that sets the baseline class for a style object

```
OSStatus MySetBaselineClass (ATSUStyle myStyle,
                                BslnBaselineClass myBaselineClass)
{
    OSStatus                status = noErr;
    ATSUAttributeTag        theTag;
    ByteCount               theSize;
    ATSUAttributeValuePtr   theValue;

    theTag = kATSUBaselineClassTag;// 1
    theSize = (ByteCount) sizeof (BslnBaselineClass);
    theValue = (ATSUAttributeValuePtr) &baselineClass;

    status = ATSUSetAttributes (myStyle, 1,
                                &theTag, &theSize, &theValue);// 2
    return status;
}
```

Here’s what the code does:

1. Sets up a triple (tag, size, value) for the baseline class attribute.
2. Associates the baseline class attribute with a style object.

__Listing 5-3__  A function that sets baseline values for a text layout object


```
status MySetBaselineValues (ATSUTextLayout myTextLayout,
                             BslnBaselineRecord myBaselineRec)
{
    OSStatus                status = noErr;
    ATSUAttributeTag        theTag;
    ByteCount               theSize;
    ATSUAttributeValuePtr   theValue;

    theTag = kATSULineBaselineValuesTag;// 1
    theValueSize = (ByteCount) sizeof (BslnBaselineRecord);
    theValue = (ATSUAttributeValuePtr) baselineRec;

    status = ATSUSetLayoutControls (myTextLayout, 1,
                        &theTag, &theSize, &theValue);// 2
    return status;

}
```

Here’s what the code does:

1. Sets up a triple (tag, size, value) for the baseline values attribute.
2. Associates the baseline values attribute with a text layout object.

You can set baselines to achieve special effects. Figure 5-1 shows a line of text drawn normally followed by a line of text that uses drop capitals. A drop capital is a special effect created by altering both the baseline and the size of uppercase glyphs in a line of text. The first line of text in Figure 5-1 is drawn using a Roman baseline. The uppercase glyphs in the second line of text are drawn using a hanging baseline and the size of these glyphs is also larger than those in the first line. The lowercase glyphs in the second line are drawn using a Roman baseline.

__Figure 5-1__  Text drawn using a Roman baseline and a hanging baseline for capitals

![Text drawn using a Roman baseline and a hanging baseline for capitals](attachments/art/dropcaps.gif)

You can perform the following tasks to achieve a drop capitals effect:

1. Set up a drop-capitals style object that has two attributes: one to specify a hanging baseline as the baseline class and another to specify the point size.

   The drop-capitals effect usually draws uppercase glyphs in a point size larger than that used for lowercase glyphs. You can keep this style object around and use it whenever drop capitals are needed.

   See [Listing 5-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnrw) for information on setting the baseline class for a style object.
2. Apply the drop-capitals style object to the appropriate runs of text in your text layout object.

   You should apply this style only to the uppercase glyphs. In the example, the drop-capitals style object is applied to “D” and “C”.
3. Use the function `ATSUCalculateBaselineDeltas` to calculate baseline delta values for the text associated with your text layout object.
4. Associate the baseline delta values with your text layout object.

   See [Listing 5-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvbeeq2kineeqsq) for information on associating baseline values with a text layout object.
5. Draw the text.

   The lowercase glyphs are drawn using the default Roman baseline and no baseline delta values, while the uppercase glyphs are drawn using the hanging baseline and the appropriate baseline delta values.

Kerning increases the overlap between glyphs that fit together naturally. As such, it does not apply evenly to all glyphs in a style run. ATSUI uses information supplied by the font to determine how much to increase or decrease the space between glyphs. In the general case, this amount can depend on more than just the two adjacent glyphs. The amount of kerning can also depend on the preceding or following glyphs, or even on glyphs in other parts of the line.

You can control how much kerning is applied to text, or you can specify that no kerning should occur. Kerning is controlled by the style attribute `kATSUKerningInhibitFactorTag`. As its name implies, when you associate a value with the `kATSUKerningInhibitFactorTag` you specify to what degree to inhibit the kerning set by the font designer.

If you set the value associated with this tag to `1`, kerning is inhibited completely. If you set the value to `0`, kerning is used to the full amount specified by the font designer. If you specify a value between `0` and `1`, kerning is reduced. The specific amount of reduction is based on the values specified by the font designer. If glyphs aren’t usually kerned, then kerning inhibition has no effect. If glyphs are usually kerned, then ATSUI uses the value you provide to calculate a percentage of what’s specified by the font designer.

Listing 5-4 shows a function that sets a kerning inhibition value for a style object. A detailed explanation for each numbered line of code follows the listing.

__Listing 5-4__  A function that sets kerning inhibition for a style object

```
status MySetKerningInhibitFactor (ATSUStyle myStyleObject,
                                Fract kerningInhibitFactor)// 1
{
    OSStatus                status = noErr;
    ATSUAttributeTag        theTag;
    ByteCount               theSize;
    ATSUAttributeValuePtr   theValue;

    theTag = kATSUKerningInhibitFactorTag;// 2
    theSize = (ByteCount) sizeof(Fract);
    theValue = (ATSUAttributeValuePtr) &kerningInhibitFactor;

    status = ATSUSetAttributes (myStyleObject, 1,
                        &theTag, &theSize, &theValue);// 3
    return status;
}
```

Here’s what the code does:

1. The `MySetKerningInhibitFactor` function takes two parameters, a previously created style object and a kerning inhibition value. Values can be from `0` to `1.0`, with `0` having no effect on kerning and `1.0` specifying not to use kerning.
2. Sets up a triple (tag, size, value) for the kerning inhibition attribute.
3. Associates the kerning inhibition attribute with a style object.

After you have associated a kerning inhibition value with a style object, you must then call the function `ATSUSetRunStyle` to associate the style object with the run of text whose kerning you want to inhibit. If you want to affect kerning for an entire text object, you can supply this style object when you create the text layout object.

You can expand or contract the spacings of all glyphs in a style run by applying a tracking setting to that style run. The tracking setting controls the relative proportion of font-defined adjustments to apply to interglyph positions. (See [ATSUI Style and Text Layout Objects](ATSUI%20Style%20and%20Text%20Layout%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamrzfvkfami) for more information on the tracking setting style attribute.)

You can set and retrieve the tracking setting using the `kATSUTrackingTag` style attribute tag. Specifying a tracking setting of `0` means to space “normally” according to the specifications set by the font designer. That does not necessarily mean that no adjustment to spacing occurs. The font designer may decide that normal spacing includes some spacing adjustment in certain point size ranges. A positive tracking setting increases interglyph position while a negative one decreases the interglyph position.

Listing 5-5 shows a function that sets a tracking value for a style object. A detailed explanation for each numbered line of code appears following the listing.

__Listing 5-5__  A function that sets a tracking value

```
OSStatus MySetTracking (ATSUStyle theStyle, Fixed myTrackingValue)// 1
{
    OSStatus                status = noERR;
    ATSUAttributeTag        theTag;
    ByteCount               theSize;
    ATSUAttributeValuePtr   theValue;

    theTag = kATSUTrackingTag;// 2
    theSize = (ByteCount) sizeof(Fixed);
    theValue = (ATSUAttributeValuePtr) &myTrackingValue;

    status = ATSUSetAttributes (theStyle,
                            1,
                            &theTag,
                            &theValueSize,
                            &theValue);// 3
    return status;

}
```

Here’s what the code does:

1. The `MySetTracking` function takes a style object and the tracking value you want to associate with the style object. The value must be a `Fixed` value; positive for loose tracking and negative for tight tracking.
2. Sets up a triple (tag, size, value) for the tracking attribute.
3. Calls the function `ATSUSetAttributes` to associate the tracking value with the style object.

Whenever you want to apply a tracking setting to a line of text, you can include code similar to that shown in Listing 5-6. A detailed explanation for each numbered line of code appears following the listing.

__Listing 5-6__  Code that applies a tracking setting to a line of text

```
    myTrackingValue =  Long2Fix (-4);// 1
    status = MySetTracking (myStyle, myTrackingValue);// 2
    require_noerr (status, TrackSettingFailed);
    status = ATSUSetRunStyle (myTextLayout, myStyle,
                            theOffset, theUniLen);// 3
    status = ATSUDrawText (myTextLayout, theOffset,
                    theUniLen, penX, penY);// 4
```

Here’s what the code does:

1. Assigns a `Fixed` value as the tracking value. In this case, the negative value indicates a reduction in interglyph positions—tight tracking.
2. Calls the function `MySetTracking` (see [Listing 5-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydamzsfvkfawcsivddcnru)) to associate the tracking value with the style object.
3. Calls the function `ATSUSetRunStyle` to associate the style object with the run of text whose tracking you want to modify.
4. Calls the function `ATSUDrawText` to render the text onscreen. This line of code assumes you have already determined values for the text offset and length of text to be drawn, as well as the pen location. You must make sure you supply the appropriate parameter values when you call `ATSUDrawText`. 

ATSUI lets you retrieve the ideal (resolution-independent) glyph metrics by calling the function `ATSUGlyphGetIdealMetrics` and the screen (resolution-dependent) metrics by calling the function `ATSUGlyphGetScreenMetrics`.

You can use the function `ATSUGlyphGetIdealMetrics` to obtain

- the advance of the glyph—the amount by which the pen is advanced after drawing the glyph
- the origin-side bearing of the glyph—the offset from the glyph origin to the beginning of the glyph image
- the end-side bearing of the glyph—the offset from the end of the glyph image to the end of the glyph advance

You can use the function `ATSUGlyphGetScreenMetrics` to obtain

- the device advance—the number of pixels of the advance for the glyph as actually drawn on the screen
- the top-left point of the glyph in device coordinates
- the height and width of the glyph in pixels; the glyph specified by these values may overlap with other glyphs when drawn
- the origin-side bearing and trailing-side bearing in pixels

[Next](Direct-Access%20Tasks-%20Working%20With%20Glyph%20Data.md)[Previous](Interactive%20Tasks-%20Supporting%20Carets%20and%20Highlighting%20Text.md)


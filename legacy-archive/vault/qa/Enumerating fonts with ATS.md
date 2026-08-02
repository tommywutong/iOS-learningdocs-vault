---
title: Enumerating fonts with ATS
apple_id: DTS10003916
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2006-04-14'
source_url: https://developer.apple.com/library/archive/qa/qa1471/_index.html
archived_at: '2026-07-18T02:30:57.172888Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1471

# Enumerating fonts with ATS

## Q:  ATS provides several different methods for enumerating the fonts and font families available in Mac OS X. Which method should I use for my application?

A: ATS provides several different methods for enumerating the fonts and font families available in Mac OS X. Which method should I use for my application?

First you'll want to validate that your situation requires you to enumerate the font list. If your goal is to gather information about all fonts installed in the system, you should enumerate once and then cache the results. Enumerating the entire system can be time-consuming and degrade system performance, especially on systems with many fonts installed. ATS includes notification mechanisms to inform you of font system changes thus eliminating the need to poll the system. See [Setting Up Notifications](https://developer.apple.com/documentation/Carbon/Conceptual/ATS_Concepts/atsfonts_tasks/chapter_3_section_5.html) in the 'Managing Fonts: ATS' guide.

If your goal is to provide a font selection menu to the user, you should implement the fonts window instead. This ensures that your application user interface remains consistent with the rest of Mac OS X. For more information on how to display and manage a fonts window see [Fonts Window Services Reference.](https://developer.apple.com/documentation/Carbon/Reference/FontsWindow/)

The following code listings demonstrate using ATS to iterate the system font database within a local context with an unrestricted scope. While similar, Listing 1 creates an iterator to enumerate all the fonts and Listing 2 creates an iterator to enumerate all the font families.

It's important to note here that your application should gracefully handle the kATSIterationScopeModified error that could be returned by ATSFontIteratorNext. This is not a fatal error, it simply indicates that one or more changes occurred in the font database since you started the iteration. In most cases, you should reset the iterator and start again. However, you should take preventive measures to not get stuck in a reset loop should the user make sudden, drastic changes to the font database, for example, adding many fonts at once.

__Listing 1__  ATS Font Iterator

```
CFArrayRef CreateCarbonSystemFontList(void) {     ATSFontIterator theFontIterator = NULL;     CFMutableArrayRef outArray = NULL;     ATSFontRef theATSFontRef = 0;     OSStatus status = noErr;      // Create array to store font names     outArray = CFArrayCreateMutable(kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);     if(!outArray)         return NULL;      // Create the iterator     status = ATSFontIteratorCreate(kATSFontContextLocal, nil,nil,                                     kATSOptionFlagsUnRestrictedScope,                                     &theFontIterator );     while (status == noErr)     {         // Get the next font in the iteration.         status = ATSFontIteratorNext( theFontIterator, &theATSFontRef );         if(status == noErr)         {             CFStringRef theName = NULL;              // Add your code here to do something with font information.             // This example gets font name and stores it in our array             ATSFontGetName(theATSFontRef, kATSOptionFlagsDefault, &theName);             CFArrayAppendValue(outArray, theName);             CFRelease(theName);         }         else if (status == kATSIterationScopeModified) // Make sure the font database hasn’t changed.         {             // reset the iterator             status = ATSFontIteratorReset (kATSFontContextLocal, nil, nil,                                             kATSOptionFlagsUnRestrictedScope,                                             &theFontIterator);             CFArrayRemoveAllValues(outArray);         }     }      ATSFontIteratorRelease(&theFontIterator);      return outArray; }
```


__Listing 2__  ATS Font Family Iterator

```
 ATSFontFamilyIterator theFontFamilyIterator = NULL;     CFMutableArrayRef outArray = NULL;     ATSFontFamilyRef theATSFontFamilyRef = 0;     OSStatus status = noErr;      // Create array to store font names     outArray = CFArrayCreateMutable(kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);     if(!outArray)         return NULL;      // Create the iterator     status = ATSFontFamilyIteratorCreate(kATSFontContextLocal, nil,nil,                                             kATSOptionFlagsUnRestrictedScope,                                             &theFontFamilyIterator );     while (status == noErr)     {         // Get the next font family in the iteration.         status = ATSFontFamilyIteratorNext( theFontFamilyIterator, &theATSFontFamilyRef );         if(status == noErr)         {             CFStringRef theName = NULL;              // Add your code here to do something with font information.             // This example gets font name and stores it in our array             ATSFontFamilyGetName(theATSFontFamilyRef, kATSOptionFlagsDefault, &theName);             CFArrayAppendValue(outArray, theName);             CFRelease(theName);         }         else if (status == kATSIterationScopeModified) // Make sure the font database hasn’t changed.         {             // reset the iterator             status = ATSFontFamilyIteratorReset (kATSFontContextLocal, nil, nil,                                                     kATSOptionFlagsUnRestrictedScope,                                                     &theFontFamilyIterator);             CFArrayRemoveAllValues(outArray);         }     }      ATSFontFamilyIteratorRelease(&theFontFamilyIterator);      return outArray; }
```


- [Managing Fonts: ATS](https://developer.apple.com/documentation/Carbon/Conceptual/ATS_Concepts/index.html)
- [Fonts Window Services Reference](https://developer.apple.com/documentation/Carbon/Reference/FontsWindow/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-04-14 | New document that describes the different ATS font enumeration methods |


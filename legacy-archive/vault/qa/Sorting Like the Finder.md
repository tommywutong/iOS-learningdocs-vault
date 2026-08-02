---
title: Sorting Like the Finder
apple_id: DTS10003422
resource_type: QA
platform: macOS
topic: Data Management
technology: Foundation
published: '2010-01-04'
source_url: https://developer.apple.com/library/archive/qa/qa1159/_index.html
archived_at: '2026-07-18T02:29:59.635254Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1159

# Sorting Like the Finder

## Q:  My application displays a list of files to the user. How can I sort this list like the Finder?

A: My application displays a list of files to the user. How can I sort this list like the Finder?

Starting with Mac OS X 10.6 you can sort like the Finder using the `-[NSString localizedStandardCompare:]` method. If you're sorting a user-visible list of strings, you should use this method if it's available.

On earlier systems there is no specific system routine to sort a list of strings as the Finder does. However, the Finder uses a standard system routine, `UCCompareTextDefault`, to compare file names, and you can use this routine to sort your own list. Listing 1 shows how to sort an array of strings like the Finder by combining `CFArraySortValues` with a comparison function that uses `UCCompareTextDefault`.

__Listing 1__  Comparison function to sort like the Finder

```c
#include <CoreServices/CoreServices.h> #include <sys/param.h>  static CFComparisonResult CompareLikeTheFinder(     const void *    val1,      const void *    val2,      void *          context ) {     #pragma unused(context)     SInt32          compareResult;     CFStringRef     lhsStr;     CFStringRef     rhsStr;     CFIndex         lhsLen;     CFIndex         rhsLen;     UniChar         lhsBuf[MAXPATHLEN];     UniChar         rhsBuf[MAXPATHLEN];      // val1 is the left-hand side CFString.      lhsStr = (CFStringRef) val1;     lhsLen = CFStringGetLength(lhsStr);      // val2 is the right-hand side CFString.      rhsStr = (CFStringRef) val2;     rhsLen = CFStringGetLength(rhsStr);      // Get the actual Unicode characters (UTF-16) for each string.      CFStringGetCharacters( lhsStr, CFRangeMake(0, lhsLen), lhsBuf);     CFStringGetCharacters( rhsStr, CFRangeMake(0, rhsLen), rhsBuf);      // Do the comparison.      (void) UCCompareTextDefault(            kUCCollateComposeInsensitiveMask         | kUCCollateWidthInsensitiveMask         | kUCCollateCaseInsensitiveMask         | kUCCollateDigitsOverrideMask         | kUCCollateDigitsAsNumberMask         | kUCCollatePunctuationSignificantMask,         lhsBuf,          lhsLen,         rhsBuf,          rhsLen,         NULL,         &compareResult     );      // Return the result. Conveniently, UCCompareTextDefault      // returns -1, 0, or +1, which matches the values for      // CFComparisonResult exactly.      return (CFComparisonResult) compareResult; }  static void SortCFMutableArrayOfCFStringsLikeTheFinder(     CFMutableArrayRef strArray ) {     CFArraySortValues(         strArray,          CFRangeMake(0, CFArrayGetCount(strArray)),          CompareLikeTheFinder,          NULL     ); }
```

- You could reduce string conversion overhead by storing the strings as UTF-16, or by converting all of the strings before starting the sort.
- You could speed up the string comparison by using collation keys (see the documentation for `UCGetCollationKey` and `UCCompareCollationKeys`).

I could, and in production quality code I would, get the length of the string and allocate an appropriately sized buffer. However, that would be overkill for a sample whose focus is on how to sort file names. Moreover, in production code I would prefer to preconvert all of the strings to UTF-16 rather than converting them for each string comparison.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-01-04 | Updated for Mac OS X 10.6, which added a specific method for Finder-like string comparison. |
| 2004-10-27 | New document that shows how to sort strings like the Finder's list view. |


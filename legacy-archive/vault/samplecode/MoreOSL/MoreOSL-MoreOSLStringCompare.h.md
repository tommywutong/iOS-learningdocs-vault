---
title: MoreOSL
apple_id: DTS10000670
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ApplicationServices
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreOSL/Listings/MoreOSL_MoreOSLStringCompare_h.html
archived_at: '2026-07-18T03:15:52.279043Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreOSL](MoreOSL.md)


[Next](MoreOSL-MoreOSLTokens.c.md)[Previous](MoreOSL-MoreOSLStringCompare.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html%23//apple_ref/doc/uid/TP40002164](https://developer.apple.com/library/mac/#documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

# MoreOSL/MoreOSLStringCompare.h

```c
/*
    File:       MoreOSLStringCompare.h

    Contains:   String comparison utilities for MoreOSL.

    Written by: Quinn

    Copyright:  Copyright © 2000 by Apple Computer, Inc., all rights reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):

         <3>     27/3/00    Quinn   Change "Pre-Carbon" -> "Non-Carbon" to be consisent with rest of
                                    MOSL.
         <2>     20/3/00    Quinn   Lots of comments.
         <1>      9/3/00    Quinn   First checked in.
*/

#pragma once

/////////////////////////////////////////////////////////////////

// MoreIsBetter Setup

#include "MoreSetup.h"

// Mac OS Interfaces

#include <AEDataModel.h>

#if TARGET_API_MAC_CARBON
    #include <CFString.h>
#endif

// MIB Prototypes

/////////////////////////////////////////////////////////////////

#ifdef __cplusplus
extern "C" {
#endif

/////////////////////////////////////////////////////////////////

// String Comparison and AppleScript
// ---------------------------------
// Implementing support for AppleScriptÕs string comparison operators is
// easy to do badly, but very hard to do right.  The challenges include:
//
//   1. The system provides no international friendly way of implementing 
//      the "contains" operator that works 100% correctly.  The CFString
//      mechanism works pretty well, but it does have itÕs problems (see below).
//
//   2. Any mechanism provided by the system still wouldnÕt be the same as
//      AppleScriptÕs built-in string operators because AppleScript carries
//      around its own string canonicalisation tables.
//
//   3. There is no documented way of getting at the scriptÕs current
//      "considering" and "ignoring" state.  This is a known limitation,
//      documented in the AppleScript Language Guide, but itÕs still lame.
//
// Some of these difficulties are evident even in the Roman script system.
// For example, assuming document 1 is called "Þnd" (the first character
// is the fi ligature (option-shift-5)), the script:
//
//      tell application "X"
//          name of document 1 = "find"
//      end tell
//
// might produce different results from:
//
//      tell application "X"
//          get name of document 1
//          result = "find"
//      end tell
//
// because the application implements string comparison in terms of IdenticalText
// or CFStringCompare, which break down the ligature, but AppleScriptÕs built-in
// string tables doesn't (even if you turn on expansion).
//
// Moreover, while testing this against CFString I discovered a bug [2442526] that
// causes it to break the identity:
//
//      (a equals b) implies ((a contains b) and (b contains a))
//
// While this probably wonÕt be a huge problem in practice, it is annoying.
//
// While casting around for a solution (especially for the "contains" operator)
// I looked at how some other applications did this.  That was a depressing
// exercise.  The FinderÕs implementation of "contains", for example, does not
// even attempt to be two-byte friendly, nor does it address the possibility
// that IdenticalText may return true for text of different length (for example,
// "Þnd" vs "find").
//
// Despite these obstacles, an application /must/ implement string comparison
// in order to support the simplest AppleScript constructs (such as formName).
// So I had to come up with a solution.  I chose two different paths depending
// on the target environment.
//
//   1. Carbon -- For Carbon applications, CFString was the obvious solution,
//      despite the niggling bug described above.
//
//   2. Non-Carbon -- For non-Carbon applications, there is no obvious, clean
//      solution.  Eventually I resorted to loading an AppleScript (using OSA)
//      and forcing it to do the comparison (using OSADoEvent).  Sleasy, but
//      functionaly.
//
// After this much pain, I thought it was important to file a bug [2444555] asking
// for a better solution.

extern pascal OSStatus MOSLStringCompare(DescType oper, const AEDesc *data1, const AEDesc *data2, Boolean *result);
    // This routine is the core string compare functionality provided
    // by MOSL.  It is called by both MOSL itself, and is available for your
    // general use.  It implements the following operators:
    //
    //      kAEEquals
    //      kAEGreaterThanEquals
    //      kAEGreaterThan
    //      kAELessThan
    //      kAELessThanEquals
    //      kAEBeginsWith
    //      kAEEndsWith
    //      kAEContains
    //
    // For Carbon code, comparison is done using CFString with the following
    // options:  kCFCompareCaseInsensitive, kCFCompareNonliteral, kCFCompareLocalized.
    //
    // For non-Carbon code, comparison is done using an embedded AppleScript,
    // using the default AppleScript comparison options.
    //
    // IMPORTANT:
    // Non-Carbon implementations must have the 'scpt' ID=5300 resource from
    // "MoreOSLStringCompare.rsrc" available in CurResFile before calling 
    // this routine.

// The following routines are provided for use by your "accessByName"
// object primitive.

extern pascal OSStatus MOSLStringEqualsPStringDesc(ConstStr255Param myObjectName, const AEDesc *comparisonName, Boolean *result);
    // This routine is a helper wrapper function that allows you to
    // test a Pascal string for equality with an AEDesc.

extern pascal OSStatus MOSLStringEqualsCStringDesc(const char *myObjectName, const AEDesc *comparisonName, Boolean *result);
    // This routine is a helper wrapper function that allows you to
    // test a C string for equality with an AEDesc.

extern pascal OSStatus MOSLStringEqualsIntlTextDesc(ScriptCode script, LangCode lang, const void *textBuf, Size textBufLen, const AEDesc *comparisonName, Boolean *result);
    // This routine is a helper wrapper function that allows you to
    // test the guts of an typeIntlText AEDesc for equality with an AEDesc.

#if TARGET_API_MAC_CARBON

    extern pascal OSStatus MOSLStringEqualsCFStringDesc(CFStringRef myObjectName, const AEDesc *comparisonName, Boolean *result);
        // This routine is a helper wrapper function that allows you to
        // test a CFString for equality with an AEDesc.

#endif

/////////////////////////////////////////////////////////////////

#ifdef __cplusplus
};
#endif
```

[Next](MoreOSL-MoreOSLTokens.c.md)[Previous](MoreOSL-MoreOSLStringCompare.c.md)


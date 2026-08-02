---
title: Private HITheme APIs in Mac OS X 10.2 should not be called
apple_id: DTS10003440
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-10-27'
source_url: https://developer.apple.com/library/archive/qa/qa1377/_index.html
archived_at: '2026-07-18T02:30:27.848471Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1377

# Private HITheme APIs in Mac OS X 10.2 should not be called

## Q:  My application crashes in `HIThemexxx` on Mac OS X 10.2 (Jaguar). Why?

A: My application crashes in `HIThemexxx` on Mac OS X 10.2 (Jaguar). Why?

Because most of the `HITheme` APIs (see list below), introduced and publicly available in Mac OS X 10.3, were private on Mac OS X 10.2 and their argument list were different.

Since the `HITheme` APIs are not available on all versions of Mac OS X, developers should weak-link with and, at runtime, test for their availability prior to calling and there lies the problem: the test mechanism most commonly used is to simply check a particular API name against NULL (see Listing 1):

__Listing 1__  Weak-linked API common runtime check.

```
if ( HIThemeGetTextDimensions != NULL )     HIThemeGetTextDimensions( ... ); else     GetThemeTextDimensions( ... );
```

But, on Mac OS X 10.2, since most of the `HITheme` APIs were present, although private, the test above will execute the `HITheme` API. Unfortunately, the list of arguments that those APIs were expecting on Mac OS X 10.2 is different than the list of arguments that was eventually published when they were introduced in Mac OS X 10.3. Any attempt to call a `HITheme` API on Mac OS X 10.2 with an argument list such as expected by Mac OS X 10.3 (and later) will provoke a crash on Mac OS X 10.2.

The exhaustive list of private `HITheme` APIs present on Mac OS X 10.2:

- HIThemeApplyBackground
- HIThemeDrawButton
- HIThemeDrawChasingArrows
- HIThemeDrawFocusRect
- HIThemeDrawGenericWell
- HIThemeDrawGrabber
- HIThemeDrawMenuBackground
- HIThemeDrawMenuBarBackground
- HIThemeDrawMenuItem
- HIThemeDrawMenuSeparator
- HIThemeDrawMenuTitle
- HIThemeDrawPaneSplitter
- HIThemeDrawPlacard
- HIThemeDrawPopupArrow
- HIThemeDrawScrollBarDelimiters
- HIThemeDrawSeparator
- HIThemeDrawTab
- HIThemeDrawTabPane
- HIThemeDrawTextBox
- HIThemeDrawTickMark
- HIThemeDrawTitleBarWidget
- HIThemeDrawTrack
- HIThemeDrawTrackTickMarks
- HIThemeDrawWindowFrame
- HIThemeGetButtonBackgroundBounds
- HIThemeGetButtonContentBounds
- HIThemeGetScrollBarTrackRect
- HIThemeGetTextDimensions
- HIThemeGetTrackBounds
- HIThemeGetTrackDragRect
- HIThemeGetTrackLiveValue
- HIThemeGetTrackPartBounds
- HIThemeGetTrackParts
- HIThemeGetTrackThumbPositionFromOffset
- HIThemeGetWindowRegionHit
- HIThemeHitTestScrollBarArrows
- HIThemeHitTestTrack

Thus, in this situation, the correct solution is to check against a particular version of the HIToolbox before calling a `HITheme` API (see Listing 2) using the `GetHIToolboxVersion` function given in Listing 3:

__Listing 2__  HIToolbox version check.

```
if ( GetHIToolboxVersion() >= 0x130)     HIThemeGetTextDimensions( ... ); else     GetThemeTextDimensions( ... );
```


__Listing 3__  `GetHIToolboxVersion`.

```
UInt32 GetHIToolboxVersion()     {     CFBundleRef bundle;     CFStringRef versStr = NULL;     static UInt32 version = 0;      // let's do the heavy following code only once...     if (version != 0) return version;      bundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.HIToolbox"));     if ( bundle != NULL )         versStr = (CFStringRef)CFBundleGetValueForInfoDictionaryKey(bundle,                                     CFSTR("CFBundleShortVersionString"));      if ( versStr != NULL &&         CFGetTypeID(versStr) == CFStringGetTypeID())         {         int major = 0, minor = 0, bugfix = 0;         char sz[20];          CFStringGetCString(versStr, sz, sizeof(sz), kCFStringEncodingUTF8);         sscanf(sz, "%d.%d.%d", &major, &minor, &bugfix);         version = ( major << 8 ) + ( minor << 4 ) + bugfix;         }      return version;     }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-27 | New document that explains why weak-linked API common runtime check is not good enough for the HITheme APIs. |


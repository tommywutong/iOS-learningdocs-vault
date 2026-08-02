---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/ApplicationServices.html
archived_at: '2026-07-18T02:52:54.556101Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# ApplicationServices Changes for Objective-C

### ApplicationServices

#### ATSUnicodeDirectAccess.h

Removed ATSUDirectAddStyleSettingRef()Removed ATSUDirectGetLayoutDataArrayPtrFromLineRef()Removed ATSUDirectGetLayoutDataArrayPtrFromTextLayout()Removed ATSUDirectReleaseLayoutDataArrayPtr()

#### ATSUnicodeDrawing.h

Removed ATSUBatchBreakLines()Removed ATSUBreakLine()Removed ATSUClearSoftLineBreaks()Removed ATSUDrawText()Removed ATSUGetGlyphBounds()Removed ATSUGetSoftLineBreaks()Removed ATSUGetTextHighlight()Removed ATSUGetUnjustifiedBounds()Removed ATSUHighlightInactiveText()Removed ATSUHighlightText()Removed ATSULeftwardCursorPosition()Removed ATSUMeasureText()Removed ATSUMeasureTextImage()Removed ATSUNextCursorPosition()Removed ATSUOffsetToCursorPosition()Removed ATSUOffsetToPosition()Removed ATSUPositionToCursorOffset()Removed ATSUPositionToOffset()Removed ATSUPreviousCursorPosition()Removed ATSURightwardCursorPosition()Removed ATSUSetHighlightingMethod()Removed ATSUSetSoftLineBreak()Removed ATSUUnhighlightText()

#### ATSUnicodeFlattening.h

Removed ATSUCopyToHandle()Removed ATSUFlattenStyleRunsToStream()Removed ATSUPasteFromHandle()Removed ATSUUnflattenStyleRunsFromStream()

#### ATSUnicodeFonts.h

Removed ATSUClearFontFeatures()Removed ATSUClearFontVariations()Removed ATSUCountFontFeatureSelectors()Removed ATSUCountFontFeatureTypes()Removed ATSUCountFontInstances()Removed ATSUCountFontNames()Removed ATSUCountFontTracking()Removed ATSUCountFontVariations()Removed ATSUFindFontFromName()Removed ATSUFindFontName()Removed ATSUFONDtoFontID()Removed ATSUFontCount()Removed ATSUFontIDtoFOND()Removed ATSUGetAllFontFeatures()Removed ATSUGetAllFontVariations()Removed ATSUGetFontFeature()Removed ATSUGetFontFeatureNameCode()Removed ATSUGetFontFeatureSelectors()Removed ATSUGetFontFeatureTypes()Removed ATSUGetFontIDs()Removed ATSUGetFontInstance()Removed ATSUGetFontInstanceNameCode()Removed ATSUGetFontVariationNameCode()Removed ATSUGetFontVariationValue()Removed ATSUGetIndFontName()Removed ATSUGetIndFontTracking()Removed ATSUGetIndFontVariation()Removed ATSUSetFontFeatures()Removed ATSUSetVariations()

#### ATSUnicodeGlyphs.h

Removed ATSUDrawGlyphInfo()Removed ATSUGetGlyphInfo()Removed ATSUGetNativeCurveType()Removed ATSUGlyphGetCubicPaths()Removed ATSUGlyphGetCurvePaths()Removed ATSUGlyphGetIdealMetrics()Removed ATSUGlyphGetQuadraticPaths()Removed ATSUGlyphGetScreenMetrics()Removed DisposeATSCubicClosePathUPP()Removed #def DisposeATSCubicClosePathUPPRemoved DisposeATSCubicCurveToUPP()Removed #def DisposeATSCubicCurveToUPPRemoved DisposeATSCubicLineToUPP()Removed #def DisposeATSCubicLineToUPPRemoved DisposeATSCubicMoveToUPP()Removed #def DisposeATSCubicMoveToUPPRemoved DisposeATSQuadraticClosePathUPP()Removed #def DisposeATSQuadraticClosePathUPPRemoved DisposeATSQuadraticCurveUPP()Removed #def DisposeATSQuadraticCurveUPPRemoved DisposeATSQuadraticLineUPP()Removed #def DisposeATSQuadraticLineUPPRemoved DisposeATSQuadraticNewPathUPP()Removed #def DisposeATSQuadraticNewPathUPPRemoved InvokeATSCubicClosePathUPP()Removed #def InvokeATSCubicClosePathUPPRemoved InvokeATSCubicCurveToUPP()Removed #def InvokeATSCubicCurveToUPPRemoved InvokeATSCubicLineToUPP()Removed #def InvokeATSCubicLineToUPPRemoved InvokeATSCubicMoveToUPP()Removed #def InvokeATSCubicMoveToUPPRemoved InvokeATSQuadraticClosePathUPP()Removed #def InvokeATSQuadraticClosePathUPPRemoved InvokeATSQuadraticCurveUPP()Removed #def InvokeATSQuadraticCurveUPPRemoved InvokeATSQuadraticLineUPP()Removed #def InvokeATSQuadraticLineUPPRemoved InvokeATSQuadraticNewPathUPP()Removed #def InvokeATSQuadraticNewPathUPPRemoved NewATSCubicClosePathUPP()Removed #def NewATSCubicClosePathUPPRemoved NewATSCubicCurveToUPP()Removed #def NewATSCubicCurveToUPPRemoved NewATSCubicLineToUPP()Removed #def NewATSCubicLineToUPPRemoved NewATSCubicMoveToUPP()Removed #def NewATSCubicMoveToUPPRemoved NewATSQuadraticClosePathUPP()Removed #def NewATSQuadraticClosePathUPPRemoved NewATSQuadraticCurveUPP()Removed #def NewATSQuadraticCurveUPPRemoved NewATSQuadraticLineUPP()Removed #def NewATSQuadraticLineUPPRemoved NewATSQuadraticNewPathUPP()Removed #def NewATSQuadraticNewPathUPP

#### ATSUnicodeObjects.h

Removed ATSUCalculateBaselineDeltas()Removed ATSUClearAttributes()Removed ATSUClearLayoutCache()Removed ATSUClearLayoutControls()Removed ATSUClearLineControls()Removed ATSUClearStyle()Removed ATSUCompareStyles()Removed ATSUCopyAttributes()Removed ATSUCopyLayoutControls()Removed ATSUCopyLineControls()Removed ATSUCreateAndCopyStyle()Removed ATSUCreateAndCopyTextLayout()Removed ATSUCreateFontFallbacks()Removed ATSUCreateStyle()Removed ATSUCreateTextLayout()Removed ATSUCreateTextLayoutWithTextHandle()Removed ATSUCreateTextLayoutWithTextPtr()Removed ATSUDisposeFontFallbacks()Removed ATSUDisposeStyle()Removed ATSUDisposeTextLayout()Removed ATSUGetAllAttributes()Removed ATSUGetAllLayoutControls()Removed ATSUGetAllLineControls()Removed ATSUGetAttribute()Removed ATSUGetContinuousAttributes()Removed ATSUGetFontFallbacks()Removed ATSUGetLayoutControl()Removed ATSUGetLineControl()Removed ATSUGetObjFontFallbacks()Removed ATSUGetRunStyle()Removed ATSUGetStyleRefCon()Removed ATSUGetTabArray()Removed ATSUGetTextLayoutRefCon()Removed ATSUGetTextLocation()Removed ATSUGetTransientFontMatching()Removed ATSUIdle()Removed ATSUMatchFontsToText()Removed ATSUOverwriteAttributes()Removed ATSUSetAttributes()Removed ATSUSetFontFallbacks()Removed ATSUSetLayoutControls()Removed ATSUSetLineControls()Removed ATSUSetObjFontFallbacks()Removed ATSUSetRunStyle()Removed ATSUSetStyleRefCon()Removed ATSUSetTabArray()Removed ATSUSetTextHandleLocation()Removed ATSUSetTextLayoutRefCon()Removed ATSUSetTextPointerLocation()Removed ATSUSetTransientFontMatching()Removed ATSUStyleIsEmpty()Removed ATSUTextDeleted()Removed ATSUTextInserted()Removed ATSUTextMoved()Removed ATSUUnderwriteAttributes()

#### ATSUnicodeTypes.h

Removed DisposeRedrawBackgroundUPP()Removed #def DisposeRedrawBackgroundUPPRemoved InvokeRedrawBackgroundUPP()Removed #def InvokeRedrawBackgroundUPPRemoved NewRedrawBackgroundUPP()Removed #def NewRedrawBackgroundUPP

#### AXTextAttributedString.h

Added [kAXListItemIndexTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemindextextattribute)Added [kAXListItemLevelTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemleveltextattribute)Added [kAXListItemPrefixTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxlistitemprefixtextattribute)

#### AXUIElement.h

Modified [AXIsProcessTrustedWithOptions()](https://developer.apple.com/documentation/applicationservices/1459186-axisprocesstrustedwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` Boolean AXIsProcessTrustedWithOptions (     CFDictionaryRef options ); ``` |
| To | ``` Boolean AXIsProcessTrustedWithOptions (     CFDictionaryRef _Nullable options ); ``` |

Modified [AXMakeProcessTrusted()](https://developer.apple.com/documentation/applicationservices/1462083-axmakeprocesstrusted)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXMakeProcessTrusted (     CFStringRef executablePath ); ``` |
| To | ``` AXError AXMakeProcessTrusted (     CFStringRef _Nonnull executablePath ); ``` |

Modified [AXObserverAddNotification()](https://developer.apple.com/documentation/applicationservices/1462089-axobserveraddnotification)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXObserverAddNotification (     AXObserverRef observer,     AXUIElementRef element,     CFStringRef notification,     void *refcon ); ``` |
| To | ``` AXError AXObserverAddNotification (     AXObserverRef _Nonnull observer,     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull notification,     void * _Nullable refcon ); ``` |

Modified [AXObserverCreate()](https://developer.apple.com/documentation/applicationservices/1460133-axobservercreate)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXObserverCreate (     pid_t application,     AXObserverCallback callback,     AXObserverRef *outObserver ); ``` |
| To | ``` AXError AXObserverCreate (     pid_t application,     AXObserverCallback _Nonnull callback,     AXObserverRef  _Nullable * _Nonnull outObserver ); ``` |

Modified [AXObserverCreateWithInfoCallback()](https://developer.apple.com/documentation/applicationservices/1460610-axobservercreatewithinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXObserverCreateWithInfoCallback (     pid_t application,     AXObserverCallbackWithInfo callback,     AXObserverRef *outObserver ); ``` |
| To | ``` AXError AXObserverCreateWithInfoCallback (     pid_t application,     AXObserverCallbackWithInfo _Nonnull callback,     AXObserverRef  _Nullable * _Nonnull outObserver ); ``` |

Modified [AXObserverGetRunLoopSource()](https://developer.apple.com/documentation/applicationservices/1459139-axobservergetrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef AXObserverGetRunLoopSource (     AXObserverRef observer ); ``` |
| To | ``` CFRunLoopSourceRef _Nonnull AXObserverGetRunLoopSource (     AXObserverRef _Nonnull observer ); ``` |

Modified [AXObserverRemoveNotification()](https://developer.apple.com/documentation/applicationservices/1462066-axobserverremovenotification)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXObserverRemoveNotification (     AXObserverRef observer,     AXUIElementRef element,     CFStringRef notification ); ``` |
| To | ``` AXError AXObserverRemoveNotification (     AXObserverRef _Nonnull observer,     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull notification ); ``` |

Modified [AXUIElementCopyActionDescription()](https://developer.apple.com/documentation/applicationservices/1462075-axuielementcopyactiondescription)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyActionDescription (     AXUIElementRef element,     CFStringRef action,     CFStringRef *description ); ``` |
| To | ``` AXError AXUIElementCopyActionDescription (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull action,     CFStringRef  _Nullable * _Nonnull description ); ``` |

Modified [AXUIElementCopyActionNames()](https://developer.apple.com/documentation/applicationservices/1462053-axuielementcopyactionnames)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyActionNames (     AXUIElementRef element,     CFArrayRef *names ); ``` |
| To | ``` AXError AXUIElementCopyActionNames (     AXUIElementRef _Nonnull element,     CFArrayRef  _Nullable * _Nonnull names ); ``` |

Modified [AXUIElementCopyAttributeNames()](https://developer.apple.com/documentation/applicationservices/1459475-axuielementcopyattributenames)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyAttributeNames (     AXUIElementRef element,     CFArrayRef *names ); ``` |
| To | ``` AXError AXUIElementCopyAttributeNames (     AXUIElementRef _Nonnull element,     CFArrayRef  _Nullable * _Nonnull names ); ``` |

Modified [AXUIElementCopyAttributeValue()](https://developer.apple.com/documentation/applicationservices/1462085-axuielementcopyattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyAttributeValue (     AXUIElementRef element,     CFStringRef attribute,     CFTypeRef *value ); ``` |
| To | ``` AXError AXUIElementCopyAttributeValue (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull attribute,     CFTypeRef  _Nullable * _Nonnull value ); ``` |

Modified [AXUIElementCopyAttributeValues()](https://developer.apple.com/documentation/applicationservices/1462060-axuielementcopyattributevalues)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyAttributeValues (     AXUIElementRef element,     CFStringRef attribute,     CFIndex index,     CFIndex maxValues,     CFArrayRef *values ); ``` |
| To | ``` AXError AXUIElementCopyAttributeValues (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull attribute,     CFIndex index,     CFIndex maxValues,     CFArrayRef  _Nullable * _Nonnull values ); ``` |

Modified [AXUIElementCopyElementAtPosition()](https://developer.apple.com/documentation/applicationservices/1462077-axuielementcopyelementatposition)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyElementAtPosition (     AXUIElementRef application,     float x,     float y,     AXUIElementRef *element ); ``` |
| To | ``` AXError AXUIElementCopyElementAtPosition (     AXUIElementRef _Nonnull application,     float x,     float y,     AXUIElementRef  _Nullable * _Nonnull element ); ``` |

Modified [AXUIElementCopyMultipleAttributeValues()](https://developer.apple.com/documentation/applicationservices/1462051-axuielementcopymultipleattribute)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyMultipleAttributeValues (     AXUIElementRef element,     CFArrayRef attributes,     AXCopyMultipleAttributeOptions options,     CFArrayRef *values ); ``` |
| To | ``` AXError AXUIElementCopyMultipleAttributeValues (     AXUIElementRef _Nonnull element,     CFArrayRef _Nonnull attributes,     AXCopyMultipleAttributeOptions options,     CFArrayRef  _Nullable * _Nonnull values ); ``` |

Modified [AXUIElementCopyParameterizedAttributeNames()](https://developer.apple.com/documentation/applicationservices/1458783-axuielementcopyparameterizedattr)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyParameterizedAttributeNames (     AXUIElementRef element,     CFArrayRef *names ); ``` |
| To | ``` AXError AXUIElementCopyParameterizedAttributeNames (     AXUIElementRef _Nonnull element,     CFArrayRef  _Nullable * _Nonnull names ); ``` |

Modified [AXUIElementCopyParameterizedAttributeValue()](https://developer.apple.com/documentation/applicationservices/1461203-axuielementcopyparameterizedattr)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementCopyParameterizedAttributeValue (     AXUIElementRef element,     CFStringRef parameterizedAttribute,     CFTypeRef parameter,     CFTypeRef *result ); ``` |
| To | ``` AXError AXUIElementCopyParameterizedAttributeValue (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull parameterizedAttribute,     CFTypeRef _Nonnull parameter,     CFTypeRef  _Nullable * _Nonnull result ); ``` |

Modified [AXUIElementCreateApplication()](https://developer.apple.com/documentation/applicationservices/1459374-axuielementcreateapplication)

|  | Declaration |
| --- | --- |
| From | ``` AXUIElementRef AXUIElementCreateApplication (     pid_t pid ); ``` |
| To | ``` AXUIElementRef _Nonnull AXUIElementCreateApplication (     pid_t pid ); ``` |

Modified [AXUIElementCreateSystemWide()](https://developer.apple.com/documentation/applicationservices/1462095-axuielementcreatesystemwide)

|  | Declaration |
| --- | --- |
| From | ``` AXUIElementRef AXUIElementCreateSystemWide (     void ); ``` |
| To | ``` AXUIElementRef _Nonnull AXUIElementCreateSystemWide (     void ); ``` |

Modified [AXUIElementGetAttributeValueCount()](https://developer.apple.com/documentation/applicationservices/1459066-axuielementgetattributevaluecoun)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementGetAttributeValueCount (     AXUIElementRef element,     CFStringRef attribute,     CFIndex *count ); ``` |
| To | ``` AXError AXUIElementGetAttributeValueCount (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull attribute,     CFIndex * _Nonnull count ); ``` |

Modified [AXUIElementGetPid()](https://developer.apple.com/documentation/applicationservices/1460337-axuielementgetpid)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementGetPid (     AXUIElementRef element,     pid_t *pid ); ``` |
| To | ``` AXError AXUIElementGetPid (     AXUIElementRef _Nonnull element,     pid_t * _Nonnull pid ); ``` |

Modified [AXUIElementIsAttributeSettable()](https://developer.apple.com/documentation/applicationservices/1459972-axuielementisattributesettable)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementIsAttributeSettable (     AXUIElementRef element,     CFStringRef attribute,     Boolean *settable ); ``` |
| To | ``` AXError AXUIElementIsAttributeSettable (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull attribute,     Boolean * _Nonnull settable ); ``` |

Modified [AXUIElementPerformAction()](https://developer.apple.com/documentation/applicationservices/1462091-axuielementperformaction)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementPerformAction (     AXUIElementRef element,     CFStringRef action ); ``` |
| To | ``` AXError AXUIElementPerformAction (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull action ); ``` |

Modified [AXUIElementPostKeyboardEvent()](https://developer.apple.com/documentation/applicationservices/1462057-axuielementpostkeyboardevent)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementPostKeyboardEvent (     AXUIElementRef application,     CGCharCode keyChar,     CGKeyCode virtualKey,     Boolean keyDown ); ``` |
| To | ``` AXError AXUIElementPostKeyboardEvent (     AXUIElementRef _Nonnull application,     CGCharCode keyChar,     CGKeyCode virtualKey,     Boolean keyDown ); ``` |

Modified [AXUIElementSetAttributeValue()](https://developer.apple.com/documentation/applicationservices/1460434-axuielementsetattributevalue)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementSetAttributeValue (     AXUIElementRef element,     CFStringRef attribute,     CFTypeRef value ); ``` |
| To | ``` AXError AXUIElementSetAttributeValue (     AXUIElementRef _Nonnull element,     CFStringRef _Nonnull attribute,     CFTypeRef _Nonnull value ); ``` |

Modified [AXUIElementSetMessagingTimeout()](https://developer.apple.com/documentation/applicationservices/1459345-axuielementsetmessagingtimeout)

|  | Declaration |
| --- | --- |
| From | ``` AXError AXUIElementSetMessagingTimeout (     AXUIElementRef element,     float timeoutInSeconds ); ``` |
| To | ``` AXError AXUIElementSetMessagingTimeout (     AXUIElementRef _Nonnull element,     float timeoutInSeconds ); ``` |

#### AXValue.h

Removed [kAXValueAXErrorType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvalueaxerrortype)Removed [kAXValueCFRangeType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluecfrangetype)Removed [kAXValueCGPointType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluecgpointtype)Removed [kAXValueCGRectType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluecgrecttype)Removed [kAXValueCGSizeType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluecgsizetype)Removed [kAXValueIllegalType](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvalueillegaltype)Added [kAXValueAXErrorType](https://developer.apple.com/documentation/applicationservices/kaxvalueaxerrortype)Added [kAXValueCFRangeType](https://developer.apple.com/documentation/applicationservices/kaxvaluecfrangetype)Added [kAXValueCGPointType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgpointtype)Added [kAXValueCGRectType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgrecttype)Added [kAXValueCGSizeType](https://developer.apple.com/documentation/applicationservices/kaxvaluecgsizetype)Added [kAXValueIllegalType](https://developer.apple.com/documentation/applicationservices/kaxvalueillegaltype)Added [kAXValueTypeAXError](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluetypeaxerror)Added [kAXValueTypeCFRange](https://developer.apple.com/documentation/applicationservices/axvaluetype/cfrange)Added [kAXValueTypeCGPoint](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgpoint)Added [kAXValueTypeCGRect](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgrect)Added [kAXValueTypeCGSize](https://developer.apple.com/documentation/applicationservices/axvaluetype/cgsize)Added [kAXValueTypeIllegal](https://developer.apple.com/documentation/applicationservices/axvaluetype/kaxvaluetypeillegal)Modified [AXValueCreate()](https://developer.apple.com/documentation/applicationservices/1459351-axvaluecreate)

|  | Declaration |
| --- | --- |
| From | ``` AXValueRef AXValueCreate (     AXValueType theType,     const void *valuePtr ); ``` |
| To | ``` AXValueRef _Nullable AXValueCreate (     AXValueType theType,     const void * _Nonnull valuePtr ); ``` |

Modified [AXValueGetType()](https://developer.apple.com/documentation/applicationservices/1460911-axvaluegettype)

|  | Declaration |
| --- | --- |
| From | ``` AXValueType AXValueGetType (     AXValueRef value ); ``` |
| To | ``` AXValueType AXValueGetType (     AXValueRef _Nonnull value ); ``` |

Modified [AXValueGetValue()](https://developer.apple.com/documentation/applicationservices/1462933-axvaluegetvalue)

|  | Declaration |
| --- | --- |
| From | ``` Boolean AXValueGetValue (     AXValueRef value,     AXValueType theType,     void *valuePtr ); ``` |
| To | ``` Boolean AXValueGetValue (     AXValueRef _Nonnull value,     AXValueType theType,     void * _Nonnull valuePtr ); ``` |

#### ColorSyncDeprecated.h

Removed [CMCloneProfileRef()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804891-cmcloneprofileref)Removed [CMCloseProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804861-cmcloseprofile)Removed [CMConvertFixedXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805174-cmconvertfixedxyztoxyz)Removed [CMConvertHLSToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805152-cmconverthlstorgb)Removed [CMConvertHSVToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805160-cmconverthsvtorgb)Removed [CMConvertLabToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805134-cmconvertlabtoxyz)Removed [CMConvertLuvToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805140-cmconvertluvtoxyz)Removed CMConvertRGBFloatBitmap()Removed [CMConvertRGBToGray()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805164-cmconvertrgbtogray)Removed [CMConvertRGBToHLS()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805149-cmconvertrgbtohls)Removed [CMConvertRGBToHSV()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805155-cmconvertrgbtohsv)Removed CMConvertXYZFloatBitmap()Removed [CMConvertXYZToFixedXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805169-cmconvertxyztofixedxyz)Removed [CMConvertXYZToLab()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805133-cmconvertxyztolab)Removed [CMConvertXYZToLuv()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805137-cmconvertxyztoluv)Removed [CMConvertXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805177-cmconvertxyztoxyz)Removed [CMConvertXYZToYxy()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805142-cmconvertxyztoyxy)Removed [CMConvertYxyToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805146-cmconvertyxytoxyz)Removed [CMCopyProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804870-cmcopyprofile)Removed [CMCopyProfileDescriptionString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805012-cmcopyprofiledescriptionstring)Removed [CMCopyProfileLocalizedString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805016-cmcopyprofilelocalizedstring)Removed [CMCopyProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805020-cmcopyprofilelocalizedstringdict)Removed [CMCountImageProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805281-cmcountimageprofiles)Removed [CMCountProfileElements()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804963-cmcountprofileelements)Removed [CMCreateProfileIdentifier()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805369-cmcreateprofileidentifier)Removed [CMDisposeProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805358-cmdisposeprofilesearch)Removed [CMEmbedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805269-cmembedimage)Removed [CMFlattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804897-cmflattenprofile)Removed CMFloatBitmapMakeChunky()Removed [CMGetColorSyncFolderSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804907-cmgetcolorsyncfolderspec)Removed [CMGetColorSyncVersion()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805293-cmgetcolorsyncversion)Removed [CMGetCWInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo)Removed [CMGetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805235-cmgetdefaultdevice)Removed [CMGetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804940-cmgetdefaultprofilebyspace)Removed [CMGetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804948-cmgetdefaultprofilebyuse)Removed [CMGetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805249-cmgetdevicedefaultprofileid)Removed [CMGetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805240-cmgetdevicefactoryprofiles)Removed [CMGetDeviceInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805260-cmgetdeviceinfo)Removed [CMGetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805256-cmgetdeviceprofile)Removed [CMGetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805245-cmgetdeviceprofiles)Removed [CMGetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805257-cmgetdevicestate)Removed [CMGetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805289-cmgetgammabyavid)Removed [CMGetImageSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805267-cmgetimagespace)Removed [CMGetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805284-cmgetindimageprofile)Removed [CMGetIndNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805059-cmgetindnamedcolorvalue)Removed [CMGetIndProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805002-cmgetindprofileelement)Removed [CMGetIndProfileElementInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804996-cmgetindprofileelementinfo)Removed [CMGetNamedColorIndex()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805065-cmgetnamedcolorindex)Removed [CMGetNamedColorInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805047-cmgetnamedcolorinfo)Removed [CMGetNamedColorName()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805072-cmgetnamedcolorname)Removed [CMGetNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805053-cmgetnamedcolorvalue)Removed [CMGetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804984-cmgetpartialprofileelement)Removed [CMGetPreferredCMM()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805182-cmgetpreferredcmm)Removed [CMGetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804955-cmgetprofilebyavid)Removed [CMGetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805034-cmgetprofiledescriptions)Removed [CMGetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804973-cmgetprofileelement)Removed [CMGetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804879-cmgetprofileheader)Removed [CMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804885-cmgetprofilelocation)Removed [CMGetProfileMD5()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804876-cmgetprofilemd5)Removed [CMGetProfileRefCount()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804894-cmgetprofilerefcount)Removed [CMGetPS2ColorRendering()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805202-cmgetps2colorrendering)Removed [CMGetPS2ColorRenderingIntent()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805196-cmgetps2colorrenderingintent)Removed [CMGetPS2ColorRenderingVMSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805206-cmgetps2colorrenderingvmsize)Removed [CMGetPS2ColorSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805191-cmgetps2colorspace)Removed [CMGetScriptProfileDescription()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805029-cmgetscriptprofiledescription)Removed [CMGetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804926-cmgetsystemprofile)Removed [CMIterateCMMInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805185-cmiteratecmminfo)Removed [CMIterateColorDevices()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805262-cmiteratecolordevices)Removed [CMIterateColorSyncFolder()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder)Removed [CMIterateDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805263-cmiteratedeviceprofiles)Removed [CMLaunchControlPanel()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805294-cmlaunchcontrolpanel)Removed [CMLinkImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805278-cmlinkimage)Removed CMM_CheckBitmap()Removed CMM_CheckColors()Removed CMM_ConcatColorWorld()Removed CMM_CreateLinkProfile()Removed CMM_GetProperty()Removed CMM_MatchBitmap()Removed CMM_MatchColors()Removed CMM_MatchFloatBitmap()Removed CMM_ValidateProfile()Removed [CMMakeProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804920-cmmakeprofile)Removed CMMatchFloatBitmap()Removed [CMMatchImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805273-cmmatchimage)Removed [CMNewProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804911-cmnewprofile)Removed [CMNewProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805344-cmnewprofilesearch)Removed [CMOpenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804853-cmopenprofile)Removed CMProfileCopyICCData()Removed [CMProfileElementExists()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804967-cmprofileelementexists)Removed [CMProfileIdentifierFolderSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805374-cmprofileidentifierfoldersearch)Removed [CMProfileIdentifierListSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805376-cmprofileidentifierlistsearch)Removed [CMProfileModified()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804872-cmprofilemodified)Removed [CMProofImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805276-cmproofimage)Removed [CMRegisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805231-cmregistercolordevice)Removed [CMRemoveProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805008-cmremoveprofileelement)Removed [CMSearchGetIndProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805362-cmsearchgetindprofile)Removed [CMSearchGetIndProfileFileSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805365-cmsearchgetindprofilefilespec)Removed [CMSetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805238-cmsetdefaultdevice)Removed [CMSetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804944-cmsetdefaultprofilebyspace)Removed [CMSetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804951-cmsetdefaultprofilebyuse)Removed [CMSetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805251-cmsetdevicedefaultprofileid)Removed [CMSetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805241-cmsetdevicefactoryprofiles)Removed [CMSetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805253-cmsetdeviceprofile)Removed [CMSetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805247-cmsetdeviceprofiles)Removed [CMSetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805258-cmsetdevicestate)Removed [CMSetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805291-cmsetgammabyavid)Removed [CMSetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805286-cmsetindimageprofile)Removed [CMSetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804989-cmsetpartialprofileelement)Removed CMSetPreferredCMM()Removed [CMSetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804959-cmsetprofilebyavid)Removed [CMSetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805039-cmsetprofiledescriptions)Removed [CMSetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804977-cmsetprofileelement)Removed [CMSetProfileElementReference()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805005-cmsetprofileelementreference)Removed [CMSetProfileElementSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804980-cmsetprofileelementsize)Removed [CMSetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804882-cmsetprofileheader)Removed [CMSetProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805025-cmsetprofilelocalizedstringdicti)Removed [CMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804932-cmsetsystemprofile)Removed cmTextureRGBtoRGBX16Removed cmTextureRGBtoRGBX8Removed cmTextureRGBtoRGBXFloat32Removed [CMUnembedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805271-cmunembedimage)Removed [CMUnregisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805234-cmunregistercolordevice)Removed [CMUpdateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804864-cmupdateprofile)Removed [CMUpdateProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805356-cmupdateprofilesearch)Removed [CMValidateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804856-cmvalidateprofile)Removed [CMValidImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805264-cmvalidimage)Removed [CWCheckBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805121-cwcheckbitmap)Removed [CWCheckColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805111-cwcheckcolors)Removed CWColorWorldGetProperty()Removed CWColorWorldSetProperty()Removed [CWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805087-cwconcatcolorworld)Removed [CWDisposeColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805102-cwdisposecolorworld)Removed [CWFillLookupTexture()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805126-cwfilllookuptexture)Removed CWGetCMMSignature()Removed [CWMatchBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805116-cwmatchbitmap)Removed [CWMatchColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805108-cwmatchcolors)Removed [CWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804915-cwnewlinkprofile)Removed [DisposeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805300-disposecmbitmapcallbackupp)Removed [DisposeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805310-disposecmconcatcallbackupp)Removed [DisposeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805318-disposecmflattenupp)Removed [DisposeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805323-disposecmmiterateupp)Removed [DisposeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805329-disposecmprofileaccessupp)Removed [DisposeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805337-disposecmprofilefilterupp)Removed [DisposeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805341-disposecmprofileiterateupp)Removed [InvokeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805303-invokecmbitmapcallbackupp)Removed [InvokeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805312-invokecmconcatcallbackupp)Removed [InvokeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805320-invokecmflattenupp)Removed [InvokeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)Removed [InvokeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805333-invokecmprofileaccessupp)Removed [InvokeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805338-invokecmprofilefilterupp)Removed [InvokeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805343-invokecmprofileiterateupp)Removed kCMIlluminantD50Removed kCMIlluminantD65Removed [NCMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804889-ncmgetprofilelocation)Removed [NCMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804936-ncmsetsystemprofile)Removed [NCMUnflattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804901-ncmunflattenprofile)Removed [NCWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805091-ncwconcatcolorworld)Removed [NCWNewColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805079-ncwnewcolorworld)Removed [NCWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804918-ncwnewlinkprofile)Removed [NewCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805297-newcmbitmapcallbackupp)Removed [NewCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805306-newcmconcatcallbackupp)Removed [NewCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805315-newcmflattenupp)Removed [NewCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805322-newcmmiterateupp)Removed [NewCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805327-newcmprofileaccessupp)Removed [NewCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805336-newcmprofilefilterupp)Removed [NewCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805339-newcmprofileiterateupp)

#### ColorSyncProfile.h

Added [#def COLORSYNC_PROFILE_INSTALL_ENTITLEMENT](https://developer.apple.com/documentation/colorsync/colorsync_profile_install_entitlement)Added [ColorSyncProfileInstall()](https://developer.apple.com/documentation/colorsync/1463116-colorsyncprofileinstall)Added [ColorSyncProfileUninstall()](https://developer.apple.com/documentation/colorsync/1458805-colorsyncprofileuninstall)Added [kColorSyncACESCGLinearProfile](https://developer.apple.com/documentation/colorsync/kcolorsyncacescglinearprofile)Added [kColorSyncITUR2020Profile](https://developer.apple.com/documentation/colorsync/kcolorsyncitur2020profile)Added [kColorSyncITUR709Profile](https://developer.apple.com/documentation/colorsync/kcolorsyncitur709profile)Added [kColorSyncProfileComputerDomain](https://developer.apple.com/documentation/colorsync/kcolorsyncprofilecomputerdomain)Added [kColorSyncProfileUserDomain](https://developer.apple.com/documentation/colorsync/kcolorsyncprofileuserdomain)Added [kColorSyncROMMRGBProfile](https://developer.apple.com/documentation/colorsync/kcolorsyncrommrgbprofile)

#### ColorSyncTransform.h

Added [kColorSync10BitInteger](https://developer.apple.com/documentation/colorsync/colorsyncdatadepth/kcolorsync10bitinteger)Added [kColorSyncTransformCodeFragmentType](https://developer.apple.com/documentation/colorsync/kcolorsynctransformcodefragmenttype)

#### PDEPluginInterface.h

Removed -[NSObject panelViewDidResize]Modified [-[NSObject initWithBundle:]](https://developer.apple.com/documentation/objectivec/nsobject/1494220-initwithbundle)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)initWithBundle:(NSBundle *)theBundle ``` |
| To | ``` - (BOOL)initWithBundle:(NSBundle * _Nonnull)theBundle ``` |

Modified [-[NSObject pageFormat]](https://developer.apple.com/documentation/objectivec/nsobject/1494209-pageformat)

|  | Declaration |
| --- | --- |
| From | ``` - (PMPageFormat)pageFormat ``` |
| To | ``` - (PMPageFormat _Nullable)pageFormat ``` |

Modified [-[NSObject panelKind]](https://developer.apple.com/documentation/objectivec/nsobject/1494208-panelkind)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)panelKind ``` |
| To | ``` - (NSString * _Nonnull)panelKind ``` |

Modified [-[NSObject panelName]](https://developer.apple.com/documentation/objectivec/nsobject/1494224-panelname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)panelName ``` |
| To | ``` - (NSString * _Nonnull)panelName ``` |

Modified [-[NSObject panelView]](https://developer.apple.com/documentation/objectivec/nsobject/1494214-panelview)

|  | Declaration |
| --- | --- |
| From | ``` - (NSView *)panelView ``` |
| To | ``` - (NSView * _Nonnull)panelView ``` |

Modified [-[NSObject PDEPanelsForType:withHostInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1494234-pdepanelsfortype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)PDEPanelsForType:(NSString *)pdeType withHostInfo:(id)host ``` |
| To | ``` - (NSArray * _Nullable)PDEPanelsForType:(NSString * _Nonnull)pdeType withHostInfo:(id _Nonnull)host ``` |

Modified [-[NSObject PMPrinter]](https://developer.apple.com/documentation/objectivec/nsobject/1494230-pmprinter)

|  | Declaration |
| --- | --- |
| From | ``` - (PMPrinter)PMPrinter ``` |
| To | ``` - (PMPrinter _Nonnull)PMPrinter ``` |

Modified [-[NSObject ppdFile]](https://developer.apple.com/documentation/objectivec/nsobject/1494226-ppdfile)

|  | Declaration |
| --- | --- |
| From | ``` - (ppd_file_t *)ppdFile ``` |
| To | ``` - (ppd_file_t * _Nullable)ppdFile ``` |

Modified [-[NSObject PPDOptionKeyValueDidChange:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494202-ppdoptionkeyvaluedidchange)

|  | Declaration |
| --- | --- |
| From | ``` - (void)PPDOptionKeyValueDidChange:(NSString *)option ppdChoice:(NSString *)choice ``` |
| To | ``` - (void)PPDOptionKeyValueDidChange:(NSString * _Nonnull)option ppdChoice:(NSString * _Nonnull)choice ``` |

Modified [-[NSObject printSession]](https://developer.apple.com/documentation/objectivec/nsobject/1494218-printsession)

|  | Declaration |
| --- | --- |
| From | ``` - (PMPrintSession)printSession ``` |
| To | ``` - (PMPrintSession _Nonnull)printSession ``` |

Modified [-[NSObject printSettings]](https://developer.apple.com/documentation/objectivec/nsobject/1494206-printsettings)

|  | Declaration |
| --- | --- |
| From | ``` - (PMPrintSettings)printSettings ``` |
| To | ``` - (PMPrintSettings _Nullable)printSettings ``` |

Modified [-[NSObject restoreValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494216-restorevaluesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)restoreValuesAndReturnError:(NSError **)error ``` |
| To | ``` - (BOOL)restoreValuesAndReturnError:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSObject saveValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494222-savevaluesandreturnerror)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)saveValuesAndReturnError:(NSError **)error ``` |
| To | ``` - (BOOL)saveValuesAndReturnError:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[NSObject summaryInfo]](https://developer.apple.com/documentation/objectivec/nsobject/1494212-summaryinfo)

|  | Declaration |
| --- | --- |
| From | ``` - (NSDictionary *)summaryInfo ``` |
| To | ``` - (NSDictionary * _Nonnull)summaryInfo ``` |

Modified [-[NSObject supportedPPDOptionKeys]](https://developer.apple.com/documentation/objectivec/nsobject/1494232-supportedppdoptionkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)supportedPPDOptionKeys ``` |
| To | ``` - (NSArray * _Nullable)supportedPPDOptionKeys ``` |

Modified [-[NSObject willChangePPDOptionKeyValue:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494235-willchangeppdoptionkeyvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)willChangePPDOptionKeyValue:(NSString *)option ppdChoice:(NSString *)choice ``` |
| To | ``` - (BOOL)willChangePPDOptionKeyValue:(NSString * _Nonnull)option ppdChoice:(NSString * _Nonnull)choice ``` |

#### PMCore.h

Modified [PMCGImageCreateWithEPSDataProvider()](https://developer.apple.com/documentation/applicationservices/1462361-pmcgimagecreatewithepsdataprovid)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef PMCGImageCreateWithEPSDataProvider (     CGDataProviderRef epsDataProvider,     CGImageRef epsPreview ); ``` |
| To | ``` CGImageRef _Nullable PMCGImageCreateWithEPSDataProvider (     CGDataProviderRef _Nullable epsDataProvider,     CGImageRef _Nonnull epsPreview ); ``` |

Modified [PMCopyAvailablePPDs()](https://developer.apple.com/documentation/applicationservices/1464170-pmcopyavailableppds)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCopyAvailablePPDs (     PMPPDDomain domain,     CFArrayRef *ppds ); ``` |
| To | ``` OSStatus PMCopyAvailablePPDs (     PMPPDDomain domain,     CFArrayRef  _Nullable * _Nonnull ppds ); ``` |

Modified [PMCopyLocalizedPPD()](https://developer.apple.com/documentation/applicationservices/1459690-pmcopylocalizedppd)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCopyLocalizedPPD (     CFURLRef ppd,     CFURLRef *localizedPPD ); ``` |
| To | ``` OSStatus PMCopyLocalizedPPD (     CFURLRef _Nonnull ppd,     CFURLRef  _Nullable * _Nonnull localizedPPD ); ``` |

Modified [PMCopyPageFormat()](https://developer.apple.com/documentation/applicationservices/1464669-pmcopypageformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCopyPageFormat (     PMPageFormat formatSrc,     PMPageFormat formatDest ); ``` |
| To | ``` OSStatus PMCopyPageFormat (     PMPageFormat _Nonnull formatSrc,     PMPageFormat _Nonnull formatDest ); ``` |

Modified [PMCopyPPDData()](https://developer.apple.com/documentation/applicationservices/1460345-pmcopyppddata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCopyPPDData (     CFURLRef ppd,     CFDataRef *data ); ``` |
| To | ``` OSStatus PMCopyPPDData (     CFURLRef _Nonnull ppd,     CFDataRef  _Nullable * _Nonnull data ); ``` |

Modified [PMCopyPrintSettings()](https://developer.apple.com/documentation/applicationservices/1462491-pmcopyprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCopyPrintSettings (     PMPrintSettings settingSrc,     PMPrintSettings settingDest ); ``` |
| To | ``` OSStatus PMCopyPrintSettings (     PMPrintSettings _Nonnull settingSrc,     PMPrintSettings _Nonnull settingDest ); ``` |

Modified [PMCreateGenericPrinter()](https://developer.apple.com/documentation/applicationservices/1461960-pmcreategenericprinter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCreateGenericPrinter (     PMPrinter *printer ); ``` |
| To | ``` OSStatus PMCreateGenericPrinter (     PMPrinter  _Nonnull * _Nonnull printer ); ``` |

Modified [PMCreatePageFormat()](https://developer.apple.com/documentation/applicationservices/1459485-pmcreatepageformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCreatePageFormat (     PMPageFormat *pageFormat ); ``` |
| To | ``` OSStatus PMCreatePageFormat (     PMPageFormat  _Nonnull * _Nonnull pageFormat ); ``` |

Modified [PMCreatePageFormatWithPMPaper()](https://developer.apple.com/documentation/applicationservices/1459274-pmcreatepageformatwithpmpaper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCreatePageFormatWithPMPaper (     PMPageFormat *pageFormat,     PMPaper paper ); ``` |
| To | ``` OSStatus PMCreatePageFormatWithPMPaper (     PMPageFormat  _Nonnull * _Nonnull pageFormat,     PMPaper _Nonnull paper ); ``` |

Modified [PMCreatePrintSettings()](https://developer.apple.com/documentation/applicationservices/1463239-pmcreateprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCreatePrintSettings (     PMPrintSettings *printSettings ); ``` |
| To | ``` OSStatus PMCreatePrintSettings (     PMPrintSettings  _Nonnull * _Nonnull printSettings ); ``` |

Modified [PMCreateSession()](https://developer.apple.com/documentation/applicationservices/1463247-pmcreatesession)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMCreateSession (     PMPrintSession *printSession ); ``` |
| To | ``` OSStatus PMCreateSession (     PMPrintSession  _Nonnull * _Nonnull printSession ); ``` |

Modified [PMGetAdjustedPageRect()](https://developer.apple.com/documentation/applicationservices/1461543-pmgetadjustedpagerect)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetAdjustedPageRect (     PMPageFormat pageFormat,     PMRect *pageRect ); ``` |
| To | ``` OSStatus PMGetAdjustedPageRect (     PMPageFormat _Nonnull pageFormat,     PMRect * _Nonnull pageRect ); ``` |

Modified [PMGetAdjustedPaperRect()](https://developer.apple.com/documentation/applicationservices/1459167-pmgetadjustedpaperrect)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetAdjustedPaperRect (     PMPageFormat pageFormat,     PMRect *paperRect ); ``` |
| To | ``` OSStatus PMGetAdjustedPaperRect (     PMPageFormat _Nonnull pageFormat,     PMRect * _Nonnull paperRect ); ``` |

Modified [PMGetCollate()](https://developer.apple.com/documentation/applicationservices/1464492-pmgetcollate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetCollate (     PMPrintSettings printSettings,     Boolean *collate ); ``` |
| To | ``` OSStatus PMGetCollate (     PMPrintSettings _Nonnull printSettings,     Boolean * _Nonnull collate ); ``` |

Modified [PMGetCopies()](https://developer.apple.com/documentation/applicationservices/1464480-pmgetcopies)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetCopies (     PMPrintSettings printSettings,     UInt32 *copies ); ``` |
| To | ``` OSStatus PMGetCopies (     PMPrintSettings _Nonnull printSettings,     UInt32 * _Nonnull copies ); ``` |

Modified [PMGetDuplex()](https://developer.apple.com/documentation/applicationservices/1458921-pmgetduplex)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetDuplex (     PMPrintSettings printSettings,     PMDuplexMode *duplexSetting ); ``` |
| To | ``` OSStatus PMGetDuplex (     PMPrintSettings _Nonnull printSettings,     PMDuplexMode * _Nonnull duplexSetting ); ``` |

Modified [PMGetFirstPage()](https://developer.apple.com/documentation/applicationservices/1460271-pmgetfirstpage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetFirstPage (     PMPrintSettings printSettings,     UInt32 *first ); ``` |
| To | ``` OSStatus PMGetFirstPage (     PMPrintSettings _Nonnull printSettings,     UInt32 * _Nonnull first ); ``` |

Modified [PMGetLastPage()](https://developer.apple.com/documentation/applicationservices/1462747-pmgetlastpage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetLastPage (     PMPrintSettings printSettings,     UInt32 *last ); ``` |
| To | ``` OSStatus PMGetLastPage (     PMPrintSettings _Nonnull printSettings,     UInt32 * _Nonnull last ); ``` |

Modified [PMGetOrientation()](https://developer.apple.com/documentation/applicationservices/1459144-pmgetorientation)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetOrientation (     PMPageFormat pageFormat,     PMOrientation *orientation ); ``` |
| To | ``` OSStatus PMGetOrientation (     PMPageFormat _Nonnull pageFormat,     PMOrientation * _Nonnull orientation ); ``` |

Modified [PMGetPageFormatExtendedData()](https://developer.apple.com/documentation/applicationservices/1464455-pmgetpageformatextendeddata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetPageFormatExtendedData (     PMPageFormat pageFormat,     OSType dataID,     UInt32 *size,     void *extendedData ); ``` |
| To | ``` OSStatus PMGetPageFormatExtendedData (     PMPageFormat _Nonnull pageFormat,     OSType dataID,     UInt32 * _Nullable size,     void * _Nullable extendedData ); ``` |

Modified [PMGetPageFormatPaper()](https://developer.apple.com/documentation/applicationservices/1461319-pmgetpageformatpaper)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetPageFormatPaper (     PMPageFormat format,     PMPaper *paper ); ``` |
| To | ``` OSStatus PMGetPageFormatPaper (     PMPageFormat _Nonnull format,     PMPaper  _Nonnull * _Nonnull paper ); ``` |

Modified [PMGetPageRange()](https://developer.apple.com/documentation/applicationservices/1459324-pmgetpagerange)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetPageRange (     PMPrintSettings printSettings,     UInt32 *minPage,     UInt32 *maxPage ); ``` |
| To | ``` OSStatus PMGetPageRange (     PMPrintSettings _Nonnull printSettings,     UInt32 * _Nonnull minPage,     UInt32 * _Nonnull maxPage ); ``` |

Modified [PMGetScale()](https://developer.apple.com/documentation/applicationservices/1458796-pmgetscale)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetScale (     PMPageFormat pageFormat,     double *scale ); ``` |
| To | ``` OSStatus PMGetScale (     PMPageFormat _Nonnull pageFormat,     double * _Nonnull scale ); ``` |

Modified [PMGetUnadjustedPageRect()](https://developer.apple.com/documentation/applicationservices/1462944-pmgetunadjustedpagerect)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetUnadjustedPageRect (     PMPageFormat pageFormat,     PMRect *pageRect ); ``` |
| To | ``` OSStatus PMGetUnadjustedPageRect (     PMPageFormat _Nonnull pageFormat,     PMRect * _Nonnull pageRect ); ``` |

Modified [PMGetUnadjustedPaperRect()](https://developer.apple.com/documentation/applicationservices/1462939-pmgetunadjustedpaperrect)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMGetUnadjustedPaperRect (     PMPageFormat pageFormat,     PMRect *paperRect ); ``` |
| To | ``` OSStatus PMGetUnadjustedPaperRect (     PMPageFormat _Nonnull pageFormat,     PMRect * _Nonnull paperRect ); ``` |

Modified [PMPageFormatCreateDataRepresentation()](https://developer.apple.com/documentation/applicationservices/1464227-pmpageformatcreatedatarepresenta)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPageFormatCreateDataRepresentation (     PMPageFormat pageFormat,     CFDataRef *data,     PMDataFormat format ); ``` |
| To | ``` OSStatus PMPageFormatCreateDataRepresentation (     PMPageFormat _Nonnull pageFormat,     CFDataRef  _Nonnull * _Nonnull data,     PMDataFormat format ); ``` |

Modified [PMPageFormatCreateWithDataRepresentation()](https://developer.apple.com/documentation/applicationservices/1462876-pmpageformatcreatewithdatarepres)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPageFormatCreateWithDataRepresentation (     CFDataRef data,     PMPageFormat *pageFormat ); ``` |
| To | ``` OSStatus PMPageFormatCreateWithDataRepresentation (     CFDataRef _Nonnull data,     PMPageFormat  _Nonnull * _Nonnull pageFormat ); ``` |

Modified [PMPageFormatGetPrinterID()](https://developer.apple.com/documentation/applicationservices/1462961-pmpageformatgetprinterid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPageFormatGetPrinterID (     PMPageFormat pageFormat,     CFStringRef *printerID ); ``` |
| To | ``` OSStatus PMPageFormatGetPrinterID (     PMPageFormat _Nonnull pageFormat,     CFStringRef  _Nullable * _Nonnull printerID ); ``` |

Modified [PMPaperCreateCustom()](https://developer.apple.com/documentation/applicationservices/1459322-pmpapercreatecustom)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperCreateCustom (     PMPrinter printer,     CFStringRef id,     CFStringRef name,     double width,     double height,     const PMPaperMargins *margins,     PMPaper *paperP ); ``` |
| To | ``` OSStatus PMPaperCreateCustom (     PMPrinter _Nullable printer,     CFStringRef _Nullable id,     CFStringRef _Nullable name,     double width,     double height,     const PMPaperMargins * _Nonnull margins,     PMPaper  _Nullable * _Nonnull paperP ); ``` |

Modified [PMPaperCreateLocalizedName()](https://developer.apple.com/documentation/applicationservices/1460981-pmpapercreatelocalizedname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperCreateLocalizedName (     PMPaper paper,     PMPrinter printer,     CFStringRef *paperName ); ``` |
| To | ``` OSStatus PMPaperCreateLocalizedName (     PMPaper _Nonnull paper,     PMPrinter _Nonnull printer,     CFStringRef  _Nullable * _Nonnull paperName ); ``` |

Modified [PMPaperGetHeight()](https://developer.apple.com/documentation/applicationservices/1460389-pmpapergetheight)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetHeight (     PMPaper paper,     double *paperHeight ); ``` |
| To | ``` OSStatus PMPaperGetHeight (     PMPaper _Nonnull paper,     double * _Nonnull paperHeight ); ``` |

Modified [PMPaperGetID()](https://developer.apple.com/documentation/applicationservices/1462910-pmpapergetid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetID (     PMPaper paper,     CFStringRef *paperID ); ``` |
| To | ``` OSStatus PMPaperGetID (     PMPaper _Nonnull paper,     CFStringRef  _Nonnull * _Nonnull paperID ); ``` |

Modified [PMPaperGetMargins()](https://developer.apple.com/documentation/applicationservices/1461994-pmpapergetmargins)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetMargins (     PMPaper paper,     PMPaperMargins *paperMargins ); ``` |
| To | ``` OSStatus PMPaperGetMargins (     PMPaper _Nonnull paper,     PMPaperMargins * _Nonnull paperMargins ); ``` |

Modified [PMPaperGetPPDPaperName()](https://developer.apple.com/documentation/applicationservices/1461039-pmpapergetppdpapername)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetPPDPaperName (     PMPaper paper,     CFStringRef *paperName ); ``` |
| To | ``` OSStatus PMPaperGetPPDPaperName (     PMPaper _Nonnull paper,     CFStringRef  _Nullable * _Nonnull paperName ); ``` |

Modified [PMPaperGetPrinterID()](https://developer.apple.com/documentation/applicationservices/1461737-pmpapergetprinterid)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetPrinterID (     PMPaper paper,     CFStringRef *printerID ); ``` |
| To | ``` OSStatus PMPaperGetPrinterID (     PMPaper _Nonnull paper,     CFStringRef  _Nullable * _Nonnull printerID ); ``` |

Modified [PMPaperGetWidth()](https://developer.apple.com/documentation/applicationservices/1459209-pmpapergetwidth)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPaperGetWidth (     PMPaper paper,     double *paperWidth ); ``` |
| To | ``` OSStatus PMPaperGetWidth (     PMPaper _Nonnull paper,     double * _Nonnull paperWidth ); ``` |

Modified [PMPaperIsCustom()](https://developer.apple.com/documentation/applicationservices/1459526-pmpaperiscustom)

|  | Declaration |
| --- | --- |
| From | ``` Boolean PMPaperIsCustom (     PMPaper paper ); ``` |
| To | ``` Boolean PMPaperIsCustom (     PMPaper _Nonnull paper ); ``` |

Modified [PMPresetCopyName()](https://developer.apple.com/documentation/applicationservices/1460343-pmpresetcopyname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPresetCopyName (     PMPreset preset,     CFStringRef *name ); ``` |
| To | ``` OSStatus PMPresetCopyName (     PMPreset _Nonnull preset,     CFStringRef  _Nullable * _Nonnull name ); ``` |

Modified [PMPresetCreatePrintSettings()](https://developer.apple.com/documentation/applicationservices/1463414-pmpresetcreateprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPresetCreatePrintSettings (     PMPreset preset,     PMPrintSession session,     PMPrintSettings *printSettings ); ``` |
| To | ``` OSStatus PMPresetCreatePrintSettings (     PMPreset _Nonnull preset,     PMPrintSession _Nonnull session,     PMPrintSettings  _Nonnull * _Nonnull printSettings ); ``` |

Modified [PMPresetGetAttributes()](https://developer.apple.com/documentation/applicationservices/1459042-pmpresetgetattributes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPresetGetAttributes (     PMPreset preset,     CFDictionaryRef *attributes ); ``` |
| To | ``` OSStatus PMPresetGetAttributes (     PMPreset _Nonnull preset,     CFDictionaryRef  _Nullable * _Nonnull attributes ); ``` |

Modified [PMPrinterCopyDescriptionURL()](https://developer.apple.com/documentation/applicationservices/1459187-pmprintercopydescriptionurl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterCopyDescriptionURL (     PMPrinter printer,     CFStringRef descriptionType,     CFURLRef *fileURL ); ``` |
| To | ``` OSStatus PMPrinterCopyDescriptionURL (     PMPrinter _Nonnull printer,     CFStringRef _Nonnull descriptionType,     CFURLRef  _Nullable * _Nonnull fileURL ); ``` |

Modified [PMPrinterCopyDeviceURI()](https://developer.apple.com/documentation/applicationservices/1460543-pmprintercopydeviceuri)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterCopyDeviceURI (     PMPrinter printer,     CFURLRef *deviceURI ); ``` |
| To | ``` OSStatus PMPrinterCopyDeviceURI (     PMPrinter _Nonnull printer,     CFURLRef  _Nullable * _Nonnull deviceURI ); ``` |

Modified [PMPrinterCopyHostName()](https://developer.apple.com/documentation/applicationservices/1462076-pmprintercopyhostname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterCopyHostName (     PMPrinter printer,     CFStringRef *hostNameP ); ``` |
| To | ``` OSStatus PMPrinterCopyHostName (     PMPrinter _Nonnull printer,     CFStringRef  _Nonnull * _Nonnull hostNameP ); ``` |

Modified [PMPrinterCopyPresets()](https://developer.apple.com/documentation/applicationservices/1459117-pmprintercopypresets)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterCopyPresets (     PMPrinter printer,     CFArrayRef *presetList ); ``` |
| To | ``` OSStatus PMPrinterCopyPresets (     PMPrinter _Nonnull printer,     CFArrayRef  _Nullable * _Nonnull presetList ); ``` |

Modified [PMPrinterCopyState()](https://developer.apple.com/documentation/applicationservices/1460381-pmprintercopystate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterCopyState (     PMPrinter printer,     CFDictionaryRef *stateDict ); ``` |
| To | ``` OSStatus PMPrinterCopyState (     PMPrinter _Nonnull printer,     CFDictionaryRef  _Nonnull * _Nonnull stateDict ); ``` |

Modified [PMPrinterCreateFromPrinterID()](https://developer.apple.com/documentation/applicationservices/1461363-pmprintercreatefromprinterid)

|  | Declaration |
| --- | --- |
| From | ``` PMPrinter PMPrinterCreateFromPrinterID (     CFStringRef printerID ); ``` |
| To | ``` PMPrinter _Nullable PMPrinterCreateFromPrinterID (     CFStringRef _Nonnull printerID ); ``` |

Modified [PMPrinterGetCommInfo()](https://developer.apple.com/documentation/applicationservices/1461069-pmprintergetcomminfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetCommInfo (     PMPrinter printer,     Boolean *supportsControlCharRangeP,     Boolean *supportsEightBitP ); ``` |
| To | ``` OSStatus PMPrinterGetCommInfo (     PMPrinter _Nonnull printer,     Boolean * _Nullable supportsControlCharRangeP,     Boolean * _Nullable supportsEightBitP ); ``` |

Modified [PMPrinterGetDriverCreator()](https://developer.apple.com/documentation/applicationservices/1459107-pmprintergetdrivercreator)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetDriverCreator (     PMPrinter printer,     OSType *creator ); ``` |
| To | ``` OSStatus PMPrinterGetDriverCreator (     PMPrinter _Nonnull printer,     OSType * _Nonnull creator ); ``` |

Modified [PMPrinterGetDriverReleaseInfo()](https://developer.apple.com/documentation/applicationservices/1464149-pmprintergetdriverreleaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetDriverReleaseInfo (     PMPrinter printer,     VersRec *release ); ``` |
| To | ``` OSStatus PMPrinterGetDriverReleaseInfo (     PMPrinter _Nonnull printer,     VersRec * _Nonnull release ); ``` |

Modified [PMPrinterGetID()](https://developer.apple.com/documentation/applicationservices/1459606-pmprintergetid)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef PMPrinterGetID (     PMPrinter printer ); ``` |
| To | ``` CFStringRef _Nullable PMPrinterGetID (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterGetIndexedPrinterResolution()](https://developer.apple.com/documentation/applicationservices/1464490-pmprintergetindexedprinterresolu)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetIndexedPrinterResolution (     PMPrinter printer,     UInt32 index,     PMResolution *resolutionP ); ``` |
| To | ``` OSStatus PMPrinterGetIndexedPrinterResolution (     PMPrinter _Nonnull printer,     UInt32 index,     PMResolution * _Nonnull resolutionP ); ``` |

Modified [PMPrinterGetLanguageInfo()](https://developer.apple.com/documentation/applicationservices/1458956-pmprintergetlanguageinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetLanguageInfo (     PMPrinter printer,     PMLanguageInfo *info ); ``` |
| To | ``` OSStatus PMPrinterGetLanguageInfo (     PMPrinter _Nonnull printer,     PMLanguageInfo * _Nonnull info ); ``` |

Modified [PMPrinterGetLocation()](https://developer.apple.com/documentation/applicationservices/1461467-pmprintergetlocation)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef PMPrinterGetLocation (     PMPrinter printer ); ``` |
| To | ``` CFStringRef _Nullable PMPrinterGetLocation (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterGetMakeAndModelName()](https://developer.apple.com/documentation/applicationservices/1463347-pmprintergetmakeandmodelname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetMakeAndModelName (     PMPrinter printer,     CFStringRef *makeAndModel ); ``` |
| To | ``` OSStatus PMPrinterGetMakeAndModelName (     PMPrinter _Nonnull printer,     CFStringRef  _Nullable * _Nonnull makeAndModel ); ``` |

Modified [PMPrinterGetMimeTypes()](https://developer.apple.com/documentation/applicationservices/1460125-pmprintergetmimetypes)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetMimeTypes (     PMPrinter printer,     PMPrintSettings settings,     CFArrayRef *mimeTypes ); ``` |
| To | ``` OSStatus PMPrinterGetMimeTypes (     PMPrinter _Nonnull printer,     PMPrintSettings _Nullable settings,     CFArrayRef  _Nullable * _Nonnull mimeTypes ); ``` |

Modified [PMPrinterGetName()](https://developer.apple.com/documentation/applicationservices/1459018-pmprintergetname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef PMPrinterGetName (     PMPrinter printer ); ``` |
| To | ``` CFStringRef _Nullable PMPrinterGetName (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterGetOutputResolution()](https://developer.apple.com/documentation/applicationservices/1459076-pmprintergetoutputresolution)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetOutputResolution (     PMPrinter printer,     PMPrintSettings printSettings,     PMResolution *resolutionP ); ``` |
| To | ``` OSStatus PMPrinterGetOutputResolution (     PMPrinter _Nonnull printer,     PMPrintSettings _Nonnull printSettings,     PMResolution * _Nonnull resolutionP ); ``` |

Modified [PMPrinterGetPaperList()](https://developer.apple.com/documentation/applicationservices/1460088-pmprintergetpaperlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetPaperList (     PMPrinter printer,     CFArrayRef *paperList ); ``` |
| To | ``` OSStatus PMPrinterGetPaperList (     PMPrinter _Nonnull printer,     CFArrayRef  _Nullable * _Nonnull paperList ); ``` |

Modified [PMPrinterGetPrinterResolutionCount()](https://developer.apple.com/documentation/applicationservices/1462004-pmprintergetprinterresolutioncou)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetPrinterResolutionCount (     PMPrinter printer,     UInt32 *countP ); ``` |
| To | ``` OSStatus PMPrinterGetPrinterResolutionCount (     PMPrinter _Nonnull printer,     UInt32 * _Nonnull countP ); ``` |

Modified [PMPrinterGetState()](https://developer.apple.com/documentation/applicationservices/1462954-pmprintergetstate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterGetState (     PMPrinter printer,     PMPrinterState *state ); ``` |
| To | ``` OSStatus PMPrinterGetState (     PMPrinter _Nonnull printer,     PMPrinterState * _Nonnull state ); ``` |

Modified [PMPrinterIsDefault()](https://developer.apple.com/documentation/applicationservices/1459030-pmprinterisdefault)

|  | Declaration |
| --- | --- |
| From | ``` Boolean PMPrinterIsDefault (     PMPrinter printer ); ``` |
| To | ``` Boolean PMPrinterIsDefault (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterIsFavorite()](https://developer.apple.com/documentation/applicationservices/1462074-pmprinterisfavorite)

|  | Declaration |
| --- | --- |
| From | ``` Boolean PMPrinterIsFavorite (     PMPrinter printer ); ``` |
| To | ``` Boolean PMPrinterIsFavorite (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterIsPostScriptCapable()](https://developer.apple.com/documentation/applicationservices/1464168-pmprinterispostscriptcapable)

|  | Declaration |
| --- | --- |
| From | ``` Boolean PMPrinterIsPostScriptCapable (     PMPrinter printer ); ``` |
| To | ``` Boolean PMPrinterIsPostScriptCapable (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterIsPostScriptPrinter()](https://developer.apple.com/documentation/applicationservices/1462257-pmprinterispostscriptprinter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterIsPostScriptPrinter (     PMPrinter printer,     Boolean *isPSPrinter ); ``` |
| To | ``` OSStatus PMPrinterIsPostScriptPrinter (     PMPrinter _Nonnull printer,     Boolean * _Nonnull isPSPrinter ); ``` |

Modified [PMPrinterIsRemote()](https://developer.apple.com/documentation/applicationservices/1461377-pmprinterisremote)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterIsRemote (     PMPrinter printer,     Boolean *isRemoteP ); ``` |
| To | ``` OSStatus PMPrinterIsRemote (     PMPrinter _Nonnull printer,     Boolean * _Nonnull isRemoteP ); ``` |

Modified [PMPrinterPrintWithFile()](https://developer.apple.com/documentation/applicationservices/1464600-pmprinterprintwithfile)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterPrintWithFile (     PMPrinter printer,     PMPrintSettings settings,     PMPageFormat format,     CFStringRef mimeType,     CFURLRef fileURL ); ``` |
| To | ``` OSStatus PMPrinterPrintWithFile (     PMPrinter _Nonnull printer,     PMPrintSettings _Nonnull settings,     PMPageFormat _Nullable format,     CFStringRef _Nullable mimeType,     CFURLRef _Nonnull fileURL ); ``` |

Modified [PMPrinterPrintWithProvider()](https://developer.apple.com/documentation/applicationservices/1461110-pmprinterprintwithprovider)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterPrintWithProvider (     PMPrinter printer,     PMPrintSettings settings,     PMPageFormat format,     CFStringRef mimeType,     CGDataProviderRef provider ); ``` |
| To | ``` OSStatus PMPrinterPrintWithProvider (     PMPrinter _Nonnull printer,     PMPrintSettings _Nonnull settings,     PMPageFormat _Nullable format,     CFStringRef _Nonnull mimeType,     CGDataProviderRef _Nonnull provider ); ``` |

Modified [PMPrinterSendCommand()](https://developer.apple.com/documentation/applicationservices/1463872-pmprintersendcommand)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterSendCommand (     PMPrinter printer,     CFStringRef commandString,     CFStringRef jobTitle,     CFDictionaryRef options ); ``` |
| To | ``` OSStatus PMPrinterSendCommand (     PMPrinter _Nonnull printer,     CFStringRef _Nonnull commandString,     CFStringRef _Nullable jobTitle,     CFDictionaryRef _Nullable options ); ``` |

Modified [PMPrinterSetDefault()](https://developer.apple.com/documentation/applicationservices/1461118-pmprintersetdefault)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterSetDefault (     PMPrinter printer ); ``` |
| To | ``` OSStatus PMPrinterSetDefault (     PMPrinter _Nonnull printer ); ``` |

Modified [PMPrinterSetOutputResolution()](https://developer.apple.com/documentation/applicationservices/1459931-pmprintersetoutputresolution)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterSetOutputResolution (     PMPrinter printer,     PMPrintSettings printSettings,     const PMResolution *resolutionP ); ``` |
| To | ``` OSStatus PMPrinterSetOutputResolution (     PMPrinter _Nonnull printer,     PMPrintSettings _Nonnull printSettings,     const PMResolution * _Nonnull resolutionP ); ``` |

Modified [PMPrinterWritePostScriptToURL()](https://developer.apple.com/documentation/applicationservices/1459729-pmprinterwritepostscripttourl)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrinterWritePostScriptToURL (     PMPrinter printer,     PMPrintSettings settings,     PMPageFormat format,     CFStringRef mimeType,     CFURLRef sourceFileURL,     CFURLRef destinationFileURL ); ``` |
| To | ``` OSStatus PMPrinterWritePostScriptToURL (     PMPrinter _Nonnull printer,     PMPrintSettings _Nonnull settings,     PMPageFormat _Nullable format,     CFStringRef _Nullable mimeType,     CFURLRef _Nonnull sourceFileURL,     CFURLRef _Nonnull destinationFileURL ); ``` |

Modified [PMPrintSettingsCopyAsDictionary()](https://developer.apple.com/documentation/applicationservices/1459088-pmprintsettingscopyasdictionary)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsCopyAsDictionary (     PMPrintSettings printSettings,     CFDictionaryRef *settingsDictionary ); ``` |
| To | ``` OSStatus PMPrintSettingsCopyAsDictionary (     PMPrintSettings _Nonnull printSettings,     CFDictionaryRef  _Nullable * _Nonnull settingsDictionary ); ``` |

Modified [PMPrintSettingsCopyKeys()](https://developer.apple.com/documentation/applicationservices/1462730-pmprintsettingscopykeys)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsCopyKeys (     PMPrintSettings printSettings,     CFArrayRef *settingsKeys ); ``` |
| To | ``` OSStatus PMPrintSettingsCopyKeys (     PMPrintSettings _Nonnull printSettings,     CFArrayRef  _Nullable * _Nonnull settingsKeys ); ``` |

Modified [PMPrintSettingsCreateDataRepresentation()](https://developer.apple.com/documentation/applicationservices/1464570-pmprintsettingscreatedatareprese)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsCreateDataRepresentation (     PMPrintSettings printSettings,     CFDataRef *data,     PMDataFormat format ); ``` |
| To | ``` OSStatus PMPrintSettingsCreateDataRepresentation (     PMPrintSettings _Nonnull printSettings,     CFDataRef  _Nonnull * _Nonnull data,     PMDataFormat format ); ``` |

Modified [PMPrintSettingsCreateWithDataRepresentation()](https://developer.apple.com/documentation/applicationservices/1462203-pmprintsettingscreatewithdatarep)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsCreateWithDataRepresentation (     CFDataRef data,     PMPrintSettings *printSettings ); ``` |
| To | ``` OSStatus PMPrintSettingsCreateWithDataRepresentation (     CFDataRef _Nonnull data,     PMPrintSettings  _Nonnull * _Nonnull printSettings ); ``` |

Modified [PMPrintSettingsGetJobName()](https://developer.apple.com/documentation/applicationservices/1459233-pmprintsettingsgetjobname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsGetJobName (     PMPrintSettings printSettings,     CFStringRef *name ); ``` |
| To | ``` OSStatus PMPrintSettingsGetJobName (     PMPrintSettings _Nonnull printSettings,     CFStringRef  _Nullable * _Nonnull name ); ``` |

Modified [PMPrintSettingsGetValue()](https://developer.apple.com/documentation/applicationservices/1460602-pmprintsettingsgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsGetValue (     PMPrintSettings printSettings,     CFStringRef key,     CFTypeRef *value ); ``` |
| To | ``` OSStatus PMPrintSettingsGetValue (     PMPrintSettings _Nonnull printSettings,     CFStringRef _Nonnull key,     CFTypeRef  _Nullable * _Nonnull value ); ``` |

Modified [PMPrintSettingsSetJobName()](https://developer.apple.com/documentation/applicationservices/1460149-pmprintsettingssetjobname)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsSetJobName (     PMPrintSettings printSettings,     CFStringRef name ); ``` |
| To | ``` OSStatus PMPrintSettingsSetJobName (     PMPrintSettings _Nonnull printSettings,     CFStringRef _Nonnull name ); ``` |

Modified [PMPrintSettingsSetValue()](https://developer.apple.com/documentation/applicationservices/1461697-pmprintsettingssetvalue)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsSetValue (     PMPrintSettings printSettings,     CFStringRef key,     CFTypeRef value,     Boolean locked ); ``` |
| To | ``` OSStatus PMPrintSettingsSetValue (     PMPrintSettings _Nonnull printSettings,     CFStringRef _Nonnull key,     CFTypeRef _Nullable value,     Boolean locked ); ``` |

Modified [PMPrintSettingsToOptions()](https://developer.apple.com/documentation/applicationservices/1459069-pmprintsettingstooptions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsToOptions (     PMPrintSettings settings,     char **options ); ``` |
| To | ``` OSStatus PMPrintSettingsToOptions (     PMPrintSettings _Nonnull settings,     char * _Nullable * _Nonnull options ); ``` |

Modified [PMPrintSettingsToOptionsWithPrinterAndPageFormat()](https://developer.apple.com/documentation/applicationservices/1459435-pmprintsettingstooptionswithprin)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMPrintSettingsToOptionsWithPrinterAndPageFormat (     PMPrintSettings settings,     PMPrinter printer,     PMPageFormat pageFormat,     char **options ); ``` |
| To | ``` OSStatus PMPrintSettingsToOptionsWithPrinterAndPageFormat (     PMPrintSettings _Nonnull settings,     PMPrinter _Nonnull printer,     PMPageFormat _Nullable pageFormat,     char * _Nullable * _Nonnull options ); ``` |

Modified [PMRelease()](https://developer.apple.com/documentation/applicationservices/1461402-pmrelease)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMRelease (     PMObject object ); ``` |
| To | ``` OSStatus PMRelease (     PMObject _Nullable object ); ``` |

Modified [PMRetain()](https://developer.apple.com/documentation/applicationservices/1460190-pmretain)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMRetain (     PMObject object ); ``` |
| To | ``` OSStatus PMRetain (     PMObject _Nullable object ); ``` |

Modified [PMServerCreatePrinterList()](https://developer.apple.com/documentation/applicationservices/1459953-pmservercreateprinterlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMServerCreatePrinterList (     PMServer server,     CFArrayRef *printerList ); ``` |
| To | ``` OSStatus PMServerCreatePrinterList (     PMServer _Nullable server,     CFArrayRef  _Nullable * _Nonnull printerList ); ``` |

Modified [PMServerLaunchPrinterBrowser()](https://developer.apple.com/documentation/applicationservices/1460175-pmserverlaunchprinterbrowser)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMServerLaunchPrinterBrowser (     PMServer server,     CFDictionaryRef options ); ``` |
| To | ``` OSStatus PMServerLaunchPrinterBrowser (     PMServer _Nullable server,     CFDictionaryRef _Nullable options ); ``` |

Modified [PMSessionBeginCGDocumentNoDialog()](https://developer.apple.com/documentation/applicationservices/1460101-pmsessionbegincgdocumentnodialog)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionBeginCGDocumentNoDialog (     PMPrintSession printSession,     PMPrintSettings printSettings,     PMPageFormat pageFormat ); ``` |
| To | ``` OSStatus PMSessionBeginCGDocumentNoDialog (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     PMPageFormat _Nonnull pageFormat ); ``` |

Modified [PMSessionBeginPageNoDialog()](https://developer.apple.com/documentation/applicationservices/1463416-pmsessionbeginpagenodialog)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionBeginPageNoDialog (     PMPrintSession printSession,     PMPageFormat pageFormat,     const PMRect *pageFrame ); ``` |
| To | ``` OSStatus PMSessionBeginPageNoDialog (     PMPrintSession _Nonnull printSession,     PMPageFormat _Nullable pageFormat,     const PMRect * _Nullable pageFrame ); ``` |

Modified [PMSessionCopyDestinationFormat()](https://developer.apple.com/documentation/applicationservices/1464266-pmsessioncopydestinationformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionCopyDestinationFormat (     PMPrintSession printSession,     PMPrintSettings printSettings,     CFStringRef *destFormatP ); ``` |
| To | ``` OSStatus PMSessionCopyDestinationFormat (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     CFStringRef  _Nullable * _Nonnull destFormatP ); ``` |

Modified [PMSessionCopyDestinationLocation()](https://developer.apple.com/documentation/applicationservices/1462967-pmsessioncopydestinationlocation)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionCopyDestinationLocation (     PMPrintSession printSession,     PMPrintSettings printSettings,     CFURLRef *destLocationP ); ``` |
| To | ``` OSStatus PMSessionCopyDestinationLocation (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     CFURLRef  _Nullable * _Nonnull destLocationP ); ``` |

Modified [PMSessionCopyOutputFormatList()](https://developer.apple.com/documentation/applicationservices/1461332-pmsessioncopyoutputformatlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionCopyOutputFormatList (     PMPrintSession printSession,     PMDestinationType destType,     CFArrayRef *documentFormatP ); ``` |
| To | ``` OSStatus PMSessionCopyOutputFormatList (     PMPrintSession _Nonnull printSession,     PMDestinationType destType,     CFArrayRef  _Nullable * _Nonnull documentFormatP ); ``` |

Modified [PMSessionCreatePageFormatList()](https://developer.apple.com/documentation/applicationservices/1463985-pmsessioncreatepageformatlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionCreatePageFormatList (     PMPrintSession printSession,     PMPrinter printer,     CFArrayRef *pageFormatList ); ``` |
| To | ``` OSStatus PMSessionCreatePageFormatList (     PMPrintSession _Nonnull printSession,     PMPrinter _Nullable printer,     CFArrayRef  _Nullable * _Nonnull pageFormatList ); ``` |

Modified [PMSessionCreatePrinterList()](https://developer.apple.com/documentation/applicationservices/1460119-pmsessioncreateprinterlist)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionCreatePrinterList (     PMPrintSession printSession,     CFArrayRef *printerList,     CFIndex *currentIndex,     PMPrinter *currentPrinter ); ``` |
| To | ``` OSStatus PMSessionCreatePrinterList (     PMPrintSession _Nonnull printSession,     CFArrayRef  _Nonnull * _Nonnull printerList,     CFIndex * _Nullable currentIndex,     PMPrinter  _Nonnull * _Nullable currentPrinter ); ``` |

Modified [PMSessionDefaultPageFormat()](https://developer.apple.com/documentation/applicationservices/1462217-pmsessiondefaultpageformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionDefaultPageFormat (     PMPrintSession printSession,     PMPageFormat pageFormat ); ``` |
| To | ``` OSStatus PMSessionDefaultPageFormat (     PMPrintSession _Nonnull printSession,     PMPageFormat _Nonnull pageFormat ); ``` |

Modified [PMSessionDefaultPrintSettings()](https://developer.apple.com/documentation/applicationservices/1460138-pmsessiondefaultprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionDefaultPrintSettings (     PMPrintSession printSession,     PMPrintSettings printSettings ); ``` |
| To | ``` OSStatus PMSessionDefaultPrintSettings (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings ); ``` |

Modified [PMSessionEndDocumentNoDialog()](https://developer.apple.com/documentation/applicationservices/1464527-pmsessionenddocumentnodialog)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionEndDocumentNoDialog (     PMPrintSession printSession ); ``` |
| To | ``` OSStatus PMSessionEndDocumentNoDialog (     PMPrintSession _Nonnull printSession ); ``` |

Modified [PMSessionEndPageNoDialog()](https://developer.apple.com/documentation/applicationservices/1462014-pmsessionendpagenodialog)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionEndPageNoDialog (     PMPrintSession printSession ); ``` |
| To | ``` OSStatus PMSessionEndPageNoDialog (     PMPrintSession _Nonnull printSession ); ``` |

Modified [PMSessionError()](https://developer.apple.com/documentation/applicationservices/1460003-pmsessionerror)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionError (     PMPrintSession printSession ); ``` |
| To | ``` OSStatus PMSessionError (     PMPrintSession _Nonnull printSession ); ``` |

Modified [PMSessionGetCGGraphicsContext()](https://developer.apple.com/documentation/applicationservices/1461952-pmsessiongetcggraphicscontext)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionGetCGGraphicsContext (     PMPrintSession printSession,     CGContextRef *context ); ``` |
| To | ``` OSStatus PMSessionGetCGGraphicsContext (     PMPrintSession _Nonnull printSession,     CGContextRef  _Nullable * _Nonnull context ); ``` |

Modified [PMSessionGetCurrentPrinter()](https://developer.apple.com/documentation/applicationservices/1458998-pmsessiongetcurrentprinter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionGetCurrentPrinter (     PMPrintSession printSession,     PMPrinter *currentPrinter ); ``` |
| To | ``` OSStatus PMSessionGetCurrentPrinter (     PMPrintSession _Nonnull printSession,     PMPrinter  _Nonnull * _Nonnull currentPrinter ); ``` |

Modified [PMSessionGetDataFromSession()](https://developer.apple.com/documentation/applicationservices/1462964-pmsessiongetdatafromsession)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionGetDataFromSession (     PMPrintSession printSession,     CFStringRef key,     CFTypeRef *data ); ``` |
| To | ``` OSStatus PMSessionGetDataFromSession (     PMPrintSession _Nonnull printSession,     CFStringRef _Nonnull key,     CFTypeRef  _Nullable * _Nonnull data ); ``` |

Modified [PMSessionGetDestinationType()](https://developer.apple.com/documentation/applicationservices/1461071-pmsessiongetdestinationtype)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionGetDestinationType (     PMPrintSession printSession,     PMPrintSettings printSettings,     PMDestinationType *destTypeP ); ``` |
| To | ``` OSStatus PMSessionGetDestinationType (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     PMDestinationType * _Nonnull destTypeP ); ``` |

Modified [PMSessionSetCurrentPMPrinter()](https://developer.apple.com/documentation/applicationservices/1461096-pmsessionsetcurrentpmprinter)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionSetCurrentPMPrinter (     PMPrintSession session,     PMPrinter printer ); ``` |
| To | ``` OSStatus PMSessionSetCurrentPMPrinter (     PMPrintSession _Nonnull session,     PMPrinter _Nonnull printer ); ``` |

Modified [PMSessionSetDataInSession()](https://developer.apple.com/documentation/applicationservices/1461902-pmsessionsetdatainsession)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionSetDataInSession (     PMPrintSession printSession,     CFStringRef key,     CFTypeRef data ); ``` |
| To | ``` OSStatus PMSessionSetDataInSession (     PMPrintSession _Nonnull printSession,     CFStringRef _Nonnull key,     CFTypeRef _Nonnull data ); ``` |

Modified [PMSessionSetDestination()](https://developer.apple.com/documentation/applicationservices/1459855-pmsessionsetdestination)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionSetDestination (     PMPrintSession printSession,     PMPrintSettings printSettings,     PMDestinationType destType,     CFStringRef destFormat,     CFURLRef destLocation ); ``` |
| To | ``` OSStatus PMSessionSetDestination (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     PMDestinationType destType,     CFStringRef _Nullable destFormat,     CFURLRef _Nullable destLocation ); ``` |

Modified [PMSessionSetError()](https://developer.apple.com/documentation/applicationservices/1460216-pmsessionseterror)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionSetError (     PMPrintSession printSession,     OSStatus printError ); ``` |
| To | ``` OSStatus PMSessionSetError (     PMPrintSession _Nonnull printSession,     OSStatus printError ); ``` |

Modified [PMSessionValidatePageFormat()](https://developer.apple.com/documentation/applicationservices/1459090-pmsessionvalidatepageformat)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionValidatePageFormat (     PMPrintSession printSession,     PMPageFormat pageFormat,     Boolean *result ); ``` |
| To | ``` OSStatus PMSessionValidatePageFormat (     PMPrintSession _Nonnull printSession,     PMPageFormat _Nonnull pageFormat,     Boolean * _Nullable changed ); ``` |

Modified [PMSessionValidatePrintSettings()](https://developer.apple.com/documentation/applicationservices/1458994-pmsessionvalidateprintsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSessionValidatePrintSettings (     PMPrintSession printSession,     PMPrintSettings printSettings,     Boolean *result ); ``` |
| To | ``` OSStatus PMSessionValidatePrintSettings (     PMPrintSession _Nonnull printSession,     PMPrintSettings _Nonnull printSettings,     Boolean * _Nullable changed ); ``` |

Modified [PMSetCollate()](https://developer.apple.com/documentation/applicationservices/1463223-pmsetcollate)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetCollate (     PMPrintSettings printSettings,     Boolean collate ); ``` |
| To | ``` OSStatus PMSetCollate (     PMPrintSettings _Nonnull printSettings,     Boolean collate ); ``` |

Modified [PMSetCopies()](https://developer.apple.com/documentation/applicationservices/1463804-pmsetcopies)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetCopies (     PMPrintSettings printSettings,     UInt32 copies,     Boolean lock ); ``` |
| To | ``` OSStatus PMSetCopies (     PMPrintSettings _Nonnull printSettings,     UInt32 copies,     Boolean lock ); ``` |

Modified [PMSetDuplex()](https://developer.apple.com/documentation/applicationservices/1462000-pmsetduplex)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetDuplex (     PMPrintSettings printSettings,     PMDuplexMode duplexSetting ); ``` |
| To | ``` OSStatus PMSetDuplex (     PMPrintSettings _Nonnull printSettings,     PMDuplexMode duplexSetting ); ``` |

Modified [PMSetFirstPage()](https://developer.apple.com/documentation/applicationservices/1461519-pmsetfirstpage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetFirstPage (     PMPrintSettings printSettings,     UInt32 first,     Boolean lock ); ``` |
| To | ``` OSStatus PMSetFirstPage (     PMPrintSettings _Nonnull printSettings,     UInt32 first,     Boolean lock ); ``` |

Modified [PMSetLastPage()](https://developer.apple.com/documentation/applicationservices/1463595-pmsetlastpage)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetLastPage (     PMPrintSettings printSettings,     UInt32 last,     Boolean lock ); ``` |
| To | ``` OSStatus PMSetLastPage (     PMPrintSettings _Nonnull printSettings,     UInt32 last,     Boolean lock ); ``` |

Modified [PMSetOrientation()](https://developer.apple.com/documentation/applicationservices/1459016-pmsetorientation)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetOrientation (     PMPageFormat pageFormat,     PMOrientation orientation,     Boolean lock ); ``` |
| To | ``` OSStatus PMSetOrientation (     PMPageFormat _Nonnull pageFormat,     PMOrientation orientation,     Boolean lock ); ``` |

Modified [PMSetPageFormatExtendedData()](https://developer.apple.com/documentation/applicationservices/1463464-pmsetpageformatextendeddata)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetPageFormatExtendedData (     PMPageFormat pageFormat,     OSType dataID,     UInt32 size,     void *extendedData ); ``` |
| To | ``` OSStatus PMSetPageFormatExtendedData (     PMPageFormat _Nonnull pageFormat,     OSType dataID,     UInt32 size,     void * _Nonnull extendedData ); ``` |

Modified [PMSetPageRange()](https://developer.apple.com/documentation/applicationservices/1462294-pmsetpagerange)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetPageRange (     PMPrintSettings printSettings,     UInt32 minPage,     UInt32 maxPage ); ``` |
| To | ``` OSStatus PMSetPageRange (     PMPrintSettings _Nonnull printSettings,     UInt32 minPage,     UInt32 maxPage ); ``` |

Modified [PMSetScale()](https://developer.apple.com/documentation/applicationservices/1463343-pmsetscale)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMSetScale (     PMPageFormat pageFormat,     double scale ); ``` |
| To | ``` OSStatus PMSetScale (     PMPageFormat _Nonnull pageFormat,     double scale ); ``` |

Modified [PMWorkflowCopyItems()](https://developer.apple.com/documentation/applicationservices/1459914-pmworkflowcopyitems)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMWorkflowCopyItems (     CFArrayRef *workflowItems ); ``` |
| To | ``` OSStatus PMWorkflowCopyItems (     CFArrayRef  _Nullable * _Nonnull workflowItems ); ``` |

Modified [PMWorkflowSubmitPDFWithOptions()](https://developer.apple.com/documentation/applicationservices/1463747-pmworkflowsubmitpdfwithoptions)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMWorkflowSubmitPDFWithOptions (     CFURLRef workflowItem,     CFStringRef title,     const char *options,     CFURLRef pdfFile ); ``` |
| To | ``` OSStatus PMWorkflowSubmitPDFWithOptions (     CFURLRef _Nonnull workflowItem,     CFStringRef _Nullable title,     const char * _Nullable options,     CFURLRef _Nonnull pdfFile ); ``` |

Modified [PMWorkflowSubmitPDFWithSettings()](https://developer.apple.com/documentation/applicationservices/1458874-pmworkflowsubmitpdfwithsettings)

|  | Declaration |
| --- | --- |
| From | ``` OSStatus PMWorkflowSubmitPDFWithSettings (     CFURLRef workflowItem,     PMPrintSettings settings,     CFURLRef pdfFile ); ``` |
| To | ``` OSStatus PMWorkflowSubmitPDFWithSettings (     CFURLRef _Nonnull workflowItem,     PMPrintSettings _Nonnull settings,     CFURLRef _Nonnull pdfFile ); ``` |

#### Quickdraw.h

Removed DisposeColorComplementUPP()Removed #def DisposeColorComplementUPPRemoved DisposeColorSearchUPP()Removed #def DisposeColorSearchUPPRemoved DisposeDragGrayRgnUPP()Removed #def DisposeDragGrayRgnUPPRemoved DisposeQDArcUPP()Removed #def DisposeQDArcUPPRemoved DisposeQDBitsUPP()Removed #def DisposeQDBitsUPPRemoved DisposeQDCommentUPP()Removed #def DisposeQDCommentUPPRemoved DisposeQDGetPicUPP()Removed #def DisposeQDGetPicUPPRemoved DisposeQDJShieldCursorUPP()Removed #def DisposeQDJShieldCursorUPPRemoved DisposeQDLineUPP()Removed #def DisposeQDLineUPPRemoved DisposeQDOpcodeUPP()Removed #def DisposeQDOpcodeUPPRemoved DisposeQDOvalUPP()Removed #def DisposeQDOvalUPPRemoved DisposeQDPolyUPP()Removed #def DisposeQDPolyUPPRemoved DisposeQDPrinterStatusUPP()Removed #def DisposeQDPrinterStatusUPPRemoved DisposeQDPutPicUPP()Removed #def DisposeQDPutPicUPPRemoved DisposeQDRectUPP()Removed #def DisposeQDRectUPPRemoved DisposeQDRgnUPP()Removed #def DisposeQDRgnUPPRemoved DisposeQDRRectUPP()Removed #def DisposeQDRRectUPPRemoved DisposeQDStdGlyphsUPP()Removed #def DisposeQDStdGlyphsUPPRemoved DisposeQDTextUPP()Removed #def DisposeQDTextUPPRemoved DisposeQDTxMeasUPP()Removed #def DisposeQDTxMeasUPPRemoved DisposeRegionToRectsUPP()Removed #def DisposeRegionToRectsUPPRemoved InvokeColorComplementUPP()Removed #def InvokeColorComplementUPPRemoved InvokeColorSearchUPP()Removed #def InvokeColorSearchUPPRemoved InvokeDragGrayRgnUPP()Removed #def InvokeDragGrayRgnUPPRemoved InvokeQDArcUPP()Removed #def InvokeQDArcUPPRemoved InvokeQDBitsUPP()Removed #def InvokeQDBitsUPPRemoved InvokeQDCommentUPP()Removed #def InvokeQDCommentUPPRemoved InvokeQDGetPicUPP()Removed #def InvokeQDGetPicUPPRemoved InvokeQDJShieldCursorUPP()Removed #def InvokeQDJShieldCursorUPPRemoved InvokeQDLineUPP()Removed #def InvokeQDLineUPPRemoved InvokeQDOpcodeUPP()Removed #def InvokeQDOpcodeUPPRemoved InvokeQDOvalUPP()Removed #def InvokeQDOvalUPPRemoved InvokeQDPolyUPP()Removed #def InvokeQDPolyUPPRemoved InvokeQDPrinterStatusUPP()Removed #def InvokeQDPrinterStatusUPPRemoved InvokeQDPutPicUPP()Removed #def InvokeQDPutPicUPPRemoved InvokeQDRectUPP()Removed #def InvokeQDRectUPPRemoved InvokeQDRgnUPP()Removed #def InvokeQDRgnUPPRemoved InvokeQDRRectUPP()Removed #def InvokeQDRRectUPPRemoved InvokeQDStdGlyphsUPP()Removed #def InvokeQDStdGlyphsUPPRemoved InvokeQDTextUPP()Removed #def InvokeQDTextUPPRemoved InvokeQDTxMeasUPP()Removed #def InvokeQDTxMeasUPPRemoved InvokeRegionToRectsUPP()Removed #def InvokeRegionToRectsUPPRemoved NewColorComplementUPP()Removed #def NewColorComplementUPPRemoved NewColorSearchUPP()Removed #def NewColorSearchUPPRemoved NewDragGrayRgnUPP()Removed #def NewDragGrayRgnUPPRemoved NewQDArcUPP()Removed #def NewQDArcUPPRemoved NewQDBitsUPP()Removed #def NewQDBitsUPPRemoved NewQDCommentUPP()Removed #def NewQDCommentUPPRemoved NewQDGetPicUPP()Removed #def NewQDGetPicUPPRemoved NewQDJShieldCursorUPP()Removed #def NewQDJShieldCursorUPPRemoved NewQDLineUPP()Removed #def NewQDLineUPPRemoved NewQDOpcodeUPP()Removed #def NewQDOpcodeUPPRemoved NewQDOvalUPP()Removed #def NewQDOvalUPPRemoved NewQDPolyUPP()Removed #def NewQDPolyUPPRemoved NewQDPrinterStatusUPP()Removed #def NewQDPrinterStatusUPPRemoved NewQDPutPicUPP()Removed #def NewQDPutPicUPPRemoved NewQDRectUPP()Removed #def NewQDRectUPPRemoved NewQDRgnUPP()Removed #def NewQDRgnUPPRemoved NewQDRRectUPP()Removed #def NewQDRRectUPPRemoved NewQDStdGlyphsUPP()Removed #def NewQDStdGlyphsUPPRemoved NewQDTextUPP()Removed #def NewQDTextUPPRemoved NewQDTxMeasUPP()Removed #def NewQDTxMeasUPPRemoved NewRegionToRectsUPP()Removed #def NewRegionToRectsUPPRemoved QDBeginCGContext()Removed QDEndCGContext()

#### SpeechSynthesis.h

Modified [ContinueSpeech()](https://developer.apple.com/documentation/applicationservices/1462728-continuespeech)

|  | Declaration |
| --- | --- |
| From | ``` OSErr ContinueSpeech (     SpeechChannel chan ); ``` |
| To | ``` OSErr ContinueSpeech (     SpeechChannel _Nonnull chan ); ``` |

Modified [CopyPhonemesFromText()](https://developer.apple.com/documentation/applicationservices/1460918-copyphonemesfromtext)

|  | Declaration |
| --- | --- |
| From | ``` OSErr CopyPhonemesFromText (     SpeechChannel chan,     CFStringRef text,     CFStringRef *phonemes ); ``` |
| To | ``` OSErr CopyPhonemesFromText (     SpeechChannel _Nonnull chan,     CFStringRef _Nonnull text,     CFStringRef  _Nullable * _Nonnull phonemes ); ``` |

Modified [CopySpeechProperty()](https://developer.apple.com/documentation/applicationservices/1459075-copyspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSErr CopySpeechProperty (     SpeechChannel chan,     CFStringRef property,     CFTypeRef *object ); ``` |
| To | ``` OSErr CopySpeechProperty (     SpeechChannel _Nonnull chan,     CFStringRef _Nonnull property,     CFTypeRef  _Nullable * _Nonnull object ); ``` |

Modified [CountVoices()](https://developer.apple.com/documentation/applicationservices/1459947-countvoices)

|  | Declaration |
| --- | --- |
| From | ``` OSErr CountVoices (     SInt16 *numVoices ); ``` |
| To | ``` OSErr CountVoices (     SInt16 * _Nonnull numVoices ); ``` |

Modified [DisposeSpeechChannel()](https://developer.apple.com/documentation/applicationservices/1462081-disposespeechchannel)

|  | Declaration |
| --- | --- |
| From | ``` OSErr DisposeSpeechChannel (     SpeechChannel chan ); ``` |
| To | ``` OSErr DisposeSpeechChannel (     SpeechChannel _Nonnull chan ); ``` |

Modified [DisposeSpeechDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552237-disposespeechdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechDoneUPP (     SpeechDoneUPP userUPP ); ``` |
| To | ``` void DisposeSpeechDoneUPP (     SpeechDoneUPP _Nonnull userUPP ); ``` |

Modified [DisposeSpeechErrorUPP()](https://developer.apple.com/documentation/applicationservices/1552245-disposespeecherrorupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechErrorUPP (     SpeechErrorUPP userUPP ); ``` |
| To | ``` void DisposeSpeechErrorUPP (     SpeechErrorUPP _Nonnull userUPP ); ``` |

Modified [DisposeSpeechPhonemeUPP()](https://developer.apple.com/documentation/applicationservices/1552226-disposespeechphonemeupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechPhonemeUPP (     SpeechPhonemeUPP userUPP ); ``` |
| To | ``` void DisposeSpeechPhonemeUPP (     SpeechPhonemeUPP _Nonnull userUPP ); ``` |

Modified [DisposeSpeechSyncUPP()](https://developer.apple.com/documentation/applicationservices/1552219-disposespeechsyncupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechSyncUPP (     SpeechSyncUPP userUPP ); ``` |
| To | ``` void DisposeSpeechSyncUPP (     SpeechSyncUPP _Nonnull userUPP ); ``` |

Modified [DisposeSpeechTextDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552229-disposespeechtextdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechTextDoneUPP (     SpeechTextDoneUPP userUPP ); ``` |
| To | ``` void DisposeSpeechTextDoneUPP (     SpeechTextDoneUPP _Nonnull userUPP ); ``` |

Modified [DisposeSpeechWordUPP()](https://developer.apple.com/documentation/applicationservices/1552222-disposespeechwordupp)

|  | Declaration |
| --- | --- |
| From | ``` void DisposeSpeechWordUPP (     SpeechWordUPP userUPP ); ``` |
| To | ``` void DisposeSpeechWordUPP (     SpeechWordUPP _Nonnull userUPP ); ``` |

Modified [GetIndVoice()](https://developer.apple.com/documentation/applicationservices/1464595-getindvoice)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetIndVoice (     SInt16 index,     VoiceSpec *voice ); ``` |
| To | ``` OSErr GetIndVoice (     SInt16 index,     VoiceSpec * _Nonnull voice ); ``` |

Modified [GetSpeechInfo()](https://developer.apple.com/documentation/applicationservices/1552220-getspeechinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetSpeechInfo (     SpeechChannel chan,     OSType selector,     void *speechInfo ); ``` |
| To | ``` OSErr GetSpeechInfo (     SpeechChannel _Nonnull chan,     OSType selector,     void * _Nonnull speechInfo ); ``` |

Modified [GetSpeechPitch()](https://developer.apple.com/documentation/applicationservices/1464774-getspeechpitch)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetSpeechPitch (     SpeechChannel chan,     Fixed *pitch ); ``` |
| To | ``` OSErr GetSpeechPitch (     SpeechChannel _Nonnull chan,     Fixed * _Nonnull pitch ); ``` |

Modified [GetSpeechRate()](https://developer.apple.com/documentation/applicationservices/1460797-getspeechrate)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetSpeechRate (     SpeechChannel chan,     Fixed *rate ); ``` |
| To | ``` OSErr GetSpeechRate (     SpeechChannel _Nonnull chan,     Fixed * _Nonnull rate ); ``` |

Modified [GetVoiceDescription()](https://developer.apple.com/documentation/applicationservices/1463940-getvoicedescription)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetVoiceDescription (     const VoiceSpec *voice,     VoiceDescription *info,     long infoLength ); ``` |
| To | ``` OSErr GetVoiceDescription (     const VoiceSpec * _Nullable voice,     VoiceDescription * _Nullable info,     long infoLength ); ``` |

Modified [GetVoiceInfo()](https://developer.apple.com/documentation/applicationservices/1461410-getvoiceinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSErr GetVoiceInfo (     const VoiceSpec *voice,     OSType selector,     void *voiceInfo ); ``` |
| To | ``` OSErr GetVoiceInfo (     const VoiceSpec * _Nullable voice,     OSType selector,     void * _Nonnull voiceInfo ); ``` |

Modified [InvokeSpeechDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552215-invokespeechdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechDoneUPP (     SpeechChannel chan,     SRefCon refCon,     SpeechDoneUPP userUPP ); ``` |
| To | ``` void InvokeSpeechDoneUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     SpeechDoneUPP _Nonnull userUPP ); ``` |

Modified [InvokeSpeechErrorUPP()](https://developer.apple.com/documentation/applicationservices/1552214-invokespeecherrorupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechErrorUPP (     SpeechChannel chan,     SRefCon refCon,     OSErr theError,     long bytePos,     SpeechErrorUPP userUPP ); ``` |
| To | ``` void InvokeSpeechErrorUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     OSErr theError,     long bytePos,     SpeechErrorUPP _Nonnull userUPP ); ``` |

Modified [InvokeSpeechPhonemeUPP()](https://developer.apple.com/documentation/applicationservices/1552234-invokespeechphonemeupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechPhonemeUPP (     SpeechChannel chan,     SRefCon refCon,     SInt16 phonemeOpcode,     SpeechPhonemeUPP userUPP ); ``` |
| To | ``` void InvokeSpeechPhonemeUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     SInt16 phonemeOpcode,     SpeechPhonemeUPP _Nonnull userUPP ); ``` |

Modified [InvokeSpeechSyncUPP()](https://developer.apple.com/documentation/applicationservices/1552243-invokespeechsyncupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechSyncUPP (     SpeechChannel chan,     SRefCon refCon,     OSType syncMessage,     SpeechSyncUPP userUPP ); ``` |
| To | ``` void InvokeSpeechSyncUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     OSType syncMessage,     SpeechSyncUPP _Nonnull userUPP ); ``` |

Modified [InvokeSpeechTextDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552249-invokespeechtextdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechTextDoneUPP (     SpeechChannel chan,     SRefCon refCon,     const void **nextBuf,     unsigned long *byteLen,     SInt32 *controlFlags,     SpeechTextDoneUPP userUPP ); ``` |
| To | ``` void InvokeSpeechTextDoneUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     const void * _Nullable * _Nullable nextBuf,     unsigned long * _Nonnull byteLen,     SInt32 * _Nonnull controlFlags,     SpeechTextDoneUPP _Nonnull userUPP ); ``` |

Modified [InvokeSpeechWordUPP()](https://developer.apple.com/documentation/applicationservices/1552227-invokespeechwordupp)

|  | Declaration |
| --- | --- |
| From | ``` void InvokeSpeechWordUPP (     SpeechChannel chan,     SRefCon refCon,     unsigned long wordPos,     UInt16 wordLen,     SpeechWordUPP userUPP ); ``` |
| To | ``` void InvokeSpeechWordUPP (     SpeechChannel _Nonnull chan,     SRefCon refCon,     unsigned long wordPos,     UInt16 wordLen,     SpeechWordUPP _Nonnull userUPP ); ``` |

Modified [MakeVoiceSpec()](https://developer.apple.com/documentation/applicationservices/1461446-makevoicespec)

|  | Declaration |
| --- | --- |
| From | ``` OSErr MakeVoiceSpec (     OSType creator,     OSType id,     VoiceSpec *voice ); ``` |
| To | ``` OSErr MakeVoiceSpec (     OSType creator,     OSType id,     VoiceSpec * _Nonnull voice ); ``` |

Modified [NewSpeechChannel()](https://developer.apple.com/documentation/applicationservices/1461367-newspeechchannel)

|  | Declaration |
| --- | --- |
| From | ``` OSErr NewSpeechChannel (     VoiceSpec *voice,     SpeechChannel *chan ); ``` |
| To | ``` OSErr NewSpeechChannel (     VoiceSpec * _Nullable voice,     SpeechChannel  _Nullable * _Nonnull chan ); ``` |

Modified [NewSpeechDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552218-newspeechdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechDoneUPP NewSpeechDoneUPP (     SpeechDoneProcPtr userRoutine ); ``` |
| To | ``` SpeechDoneUPP _Nonnull NewSpeechDoneUPP (     SpeechDoneProcPtr _Nonnull userRoutine ); ``` |

Modified [NewSpeechErrorUPP()](https://developer.apple.com/documentation/applicationservices/1552224-newspeecherrorupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechErrorUPP NewSpeechErrorUPP (     SpeechErrorProcPtr userRoutine ); ``` |
| To | ``` SpeechErrorUPP _Nonnull NewSpeechErrorUPP (     SpeechErrorProcPtr _Nonnull userRoutine ); ``` |

Modified [NewSpeechPhonemeUPP()](https://developer.apple.com/documentation/applicationservices/1552225-newspeechphonemeupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechPhonemeUPP NewSpeechPhonemeUPP (     SpeechPhonemeProcPtr userRoutine ); ``` |
| To | ``` SpeechPhonemeUPP _Nonnull NewSpeechPhonemeUPP (     SpeechPhonemeProcPtr _Nonnull userRoutine ); ``` |

Modified [NewSpeechSyncUPP()](https://developer.apple.com/documentation/applicationservices/1552244-newspeechsyncupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechSyncUPP NewSpeechSyncUPP (     SpeechSyncProcPtr userRoutine ); ``` |
| To | ``` SpeechSyncUPP _Nonnull NewSpeechSyncUPP (     SpeechSyncProcPtr _Nonnull userRoutine ); ``` |

Modified [NewSpeechTextDoneUPP()](https://developer.apple.com/documentation/applicationservices/1552247-newspeechtextdoneupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechTextDoneUPP NewSpeechTextDoneUPP (     SpeechTextDoneProcPtr userRoutine ); ``` |
| To | ``` SpeechTextDoneUPP _Nonnull NewSpeechTextDoneUPP (     SpeechTextDoneProcPtr _Nonnull userRoutine ); ``` |

Modified [NewSpeechWordUPP()](https://developer.apple.com/documentation/applicationservices/1552230-newspeechwordupp)

|  | Declaration |
| --- | --- |
| From | ``` SpeechWordUPP NewSpeechWordUPP (     SpeechWordProcPtr userRoutine ); ``` |
| To | ``` SpeechWordUPP _Nonnull NewSpeechWordUPP (     SpeechWordProcPtr _Nonnull userRoutine ); ``` |

Modified [PauseSpeechAt()](https://developer.apple.com/documentation/applicationservices/1461174-pausespeechat)

|  | Declaration |
| --- | --- |
| From | ``` OSErr PauseSpeechAt (     SpeechChannel chan,     SInt32 whereToPause ); ``` |
| To | ``` OSErr PauseSpeechAt (     SpeechChannel _Nonnull chan,     SInt32 whereToPause ); ``` |

Modified [SetSpeechInfo()](https://developer.apple.com/documentation/applicationservices/1552223-setspeechinfo)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SetSpeechInfo (     SpeechChannel chan,     OSType selector,     const void *speechInfo ); ``` |
| To | ``` OSErr SetSpeechInfo (     SpeechChannel _Nonnull chan,     OSType selector,     const void * _Nullable speechInfo ); ``` |

Modified [SetSpeechPitch()](https://developer.apple.com/documentation/applicationservices/1462674-setspeechpitch)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SetSpeechPitch (     SpeechChannel chan,     Fixed pitch ); ``` |
| To | ``` OSErr SetSpeechPitch (     SpeechChannel _Nonnull chan,     Fixed pitch ); ``` |

Modified [SetSpeechProperty()](https://developer.apple.com/documentation/applicationservices/1459256-setspeechproperty)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SetSpeechProperty (     SpeechChannel chan,     CFStringRef property,     CFTypeRef object ); ``` |
| To | ``` OSErr SetSpeechProperty (     SpeechChannel _Nonnull chan,     CFStringRef _Nonnull property,     CFTypeRef _Nullable object ); ``` |

Modified [SetSpeechRate()](https://developer.apple.com/documentation/applicationservices/1459896-setspeechrate)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SetSpeechRate (     SpeechChannel chan,     Fixed rate ); ``` |
| To | ``` OSErr SetSpeechRate (     SpeechChannel _Nonnull chan,     Fixed rate ); ``` |

Modified [SpeakBuffer()](https://developer.apple.com/documentation/applicationservices/1552252-speakbuffer)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeakBuffer (     SpeechChannel chan,     const void *textBuf,     unsigned long textBytes,     SInt32 controlFlags ); ``` |
| To | ``` OSErr SpeakBuffer (     SpeechChannel _Nonnull chan,     const void * _Nonnull textBuf,     unsigned long textBytes,     SInt32 controlFlags ); ``` |

Modified [SpeakCFString()](https://developer.apple.com/documentation/applicationservices/1461621-speakcfstring)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeakCFString (     SpeechChannel chan,     CFStringRef aString,     CFDictionaryRef options ); ``` |
| To | ``` OSErr SpeakCFString (     SpeechChannel _Nonnull chan,     CFStringRef _Nonnull aString,     CFDictionaryRef _Nullable options ); ``` |

Modified [SpeakString()](https://developer.apple.com/documentation/applicationservices/1552250-speakstring)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeakString (     ConstStr255Param textToBeSpoken ); ``` |
| To | ``` OSErr SpeakString (     ConstStr255Param _Nonnull textToBeSpoken ); ``` |

Modified [SpeakText()](https://developer.apple.com/documentation/applicationservices/1552236-speaktext)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeakText (     SpeechChannel chan,     const void *textBuf,     unsigned long textBytes ); ``` |
| To | ``` OSErr SpeakText (     SpeechChannel _Nonnull chan,     const void * _Nonnull textBuf,     unsigned long textBytes ); ``` |

Modified [SpeechSynthesisRegisterModuleURL()](https://developer.apple.com/documentation/applicationservices/1459624-speechsynthesisregistermoduleurl)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeechSynthesisRegisterModuleURL (     CFURLRef url ); ``` |
| To | ``` OSErr SpeechSynthesisRegisterModuleURL (     CFURLRef _Nonnull url ); ``` |

Modified [SpeechSynthesisUnregisterModuleURL()](https://developer.apple.com/documentation/applicationservices/1462511-speechsynthesisunregistermoduleu)

|  | Declaration |
| --- | --- |
| From | ``` OSErr SpeechSynthesisUnregisterModuleURL (     CFURLRef url ); ``` |
| To | ``` OSErr SpeechSynthesisUnregisterModuleURL (     CFURLRef _Nonnull url ); ``` |

Modified [StopSpeech()](https://developer.apple.com/documentation/applicationservices/1462745-stopspeech)

|  | Declaration |
| --- | --- |
| From | ``` OSErr StopSpeech (     SpeechChannel chan ); ``` |
| To | ``` OSErr StopSpeech (     SpeechChannel _Nonnull chan ); ``` |

Modified [StopSpeechAt()](https://developer.apple.com/documentation/applicationservices/1459780-stopspeechat)

|  | Declaration |
| --- | --- |
| From | ``` OSErr StopSpeechAt (     SpeechChannel chan,     SInt32 whereToStop ); ``` |
| To | ``` OSErr StopSpeechAt (     SpeechChannel _Nonnull chan,     SInt32 whereToStop ); ``` |

Modified [TextToPhonemes()](https://developer.apple.com/documentation/applicationservices/1552235-texttophonemes)

|  | Declaration |
| --- | --- |
| From | ``` OSErr TextToPhonemes (     SpeechChannel chan,     const void *textBuf,     unsigned long textBytes,     Handle phonemeBuf,     long *phonemeBytes ); ``` |
| To | ``` OSErr TextToPhonemes (     SpeechChannel _Nonnull chan,     const void * _Nonnull textBuf,     unsigned long textBytes,     Handle _Nonnull phonemeBuf,     long * _Nonnull phonemeBytes ); ``` |

Modified [UseDictionary()](https://developer.apple.com/documentation/applicationservices/1552255-usedictionary)

|  | Declaration |
| --- | --- |
| From | ``` OSErr UseDictionary (     SpeechChannel chan,     Handle dictionary ); ``` |
| To | ``` OSErr UseDictionary (     SpeechChannel _Nonnull chan,     Handle _Nonnull dictionary ); ``` |

Modified [UseSpeechDictionary()](https://developer.apple.com/documentation/applicationservices/1463688-usespeechdictionary)

|  | Declaration |
| --- | --- |
| From | ``` OSErr UseSpeechDictionary (     SpeechChannel chan,     CFDictionaryRef speechDictionary ); ``` |
| To | ``` OSErr UseSpeechDictionary (     SpeechChannel _Nonnull chan,     CFDictionaryRef _Nonnull speechDictionary ); ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

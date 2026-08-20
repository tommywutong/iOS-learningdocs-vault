---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/ApplicationServices.html
archived_at: '2026-07-18T02:54:24.933260Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# ApplicationServices Changes

## ApplicationServices

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

ATSFont.hModified refCon

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

ATSLayoutTypes.hModified DisposeATSUDirectLayoutOperationOverrideUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified NewATSUDirectLayoutOperationOverrideUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified InvokeATSUDirectLayoutOperationOverrideUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

ATSTypes.hModified NewFMFontFamilyCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified DisposeFMFontFamilyCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified InvokeFMFontFamilyCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified NewFMFontCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified DisposeFMFontCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified InvokeFMFontCallbackFilterUPP()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

AXAttributeConstants.hAdded [#def kAXFullScreenButtonAttribute](https://developer.apple.com/documentation/applicationservices/kaxfullscreenbuttonattribute)Added [#def kAXIdentifierAttribute](https://developer.apple.com/documentation/applicationservices/kaxidentifierattribute)AXRoleConstants.hAdded [#def kAXFullScreenButtonSubrole](https://developer.apple.com/documentation/applicationservices/kaxfullscreenbuttonsubrole)Added [#def kAXPopoverRole](https://developer.apple.com/documentation/applicationservices/kaxpopoverrole)Added [#def kAXSeparatorDockItemSubrole](https://developer.apple.com/documentation/applicationservices/kaxseparatordockitemsubrole)AXTextAttributedString.hAdded [kAXAutocorrectedTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxautocorrectedtextattribute)CGColorSpace.hModified [CGColorSpaceCreateWithPlatformColorSpace()](https://developer.apple.com/documentation/coregraphics/1408850-cgcolorspacecreatewithplatformco)

|  | Declaration |
| --- | --- |
| From | CGColorSpaceRef CGColorSpaceCreateWithPlatformColorSpace ( void \*ref); |
| To | CGColorSpaceRef CGColorSpaceCreateWithPlatformColorSpace ( const void \*ref); |

CGDirectDisplay.hRemoved [CGDisplayAddressForPosition()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807904-cgdisplayaddressforposition)Removed [CGDisplayBaseAddress()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807908-cgdisplaybaseaddress)Removed [CGDisplayBitsPerPixel()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807972-cgdisplaybitsperpixel)Removed [CGDisplayBitsPerSample()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807973-cgdisplaybitspersample)Removed [CGDisplayBytesPerRow()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807976-cgdisplaybytesperrow)Removed [CGDisplaySamplesPerPixel()](https://developer.apple.com/documentation/coregraphics/quartz_display_services/1807975-cgdisplaysamplesperpixel)Modified CGDisplayWaitForBeamPositionOutsideLines()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGDisplaySetPalette()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGDisplayCanSetPalette()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGDisplayBeamPosition()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CGDirectPalette.hModified CGPaletteGetNumberOfSamples()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateWithSamples()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateCopy()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteRelease()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteGetIndexForColor()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateWithDisplay()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteSetColorAtIndex()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateWithByteSamples()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteGetColorAtIndex()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteIsEqualToPalette()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateFromPaletteBlendedWithColor()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateDefaultColorPalette()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified CGPaletteCreateWithCapacity()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

CGEventTypes.hAdded [kCGMouseEventWindowUnderMousePointer](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventwindowundermousepointer)Added [kCGMouseEventWindowUnderMousePointerThatCanHandleThisEvent](https://developer.apple.com/documentation/coregraphics/cgeventfield/kcgmouseeventwindowundermousepointerthatcanhandlethisevent)Added [kCGScrollWheelEventScrollPhase](https://developer.apple.com/documentation/coregraphics/cgeventfield/scrollwheeleventscrollphase)CGImageProperties.hAdded [kCGImagePropertyExifBodySerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifbodyserialnumber)Added [kCGImagePropertyExifCameraOwnerName](https://developer.apple.com/documentation/imageio/kcgimagepropertyexifcameraownername)Added [kCGImagePropertyExifLensMake](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmake)Added [kCGImagePropertyExifLensModel](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensmodel)Added [kCGImagePropertyExifLensSerialNumber](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensserialnumber)Added [kCGImagePropertyExifLensSpecification](https://developer.apple.com/documentation/imageio/kcgimagepropertyexiflensspecification)Added [kCGImagePropertyGIFUnclampedDelayTime](https://developer.apple.com/documentation/imageio/kcgimagepropertygifunclampeddelaytime)Added [kCGImagePropertyPNGAuthor](https://developer.apple.com/documentation/imageio/kcgimagepropertypngauthor)Added [kCGImagePropertyPNGCopyright](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcopyright)Added [kCGImagePropertyPNGCreationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngcreationtime)Added [kCGImagePropertyPNGDescription](https://developer.apple.com/documentation/imageio/kcgimagepropertypngdescription)Added [kCGImagePropertyPNGModificationTime](https://developer.apple.com/documentation/imageio/kcgimagepropertypngmodificationtime)Added [kCGImagePropertyPNGSoftware](https://developer.apple.com/documentation/imageio/kcgimagepropertypngsoftware)Added [kCGImagePropertyPNGTitle](https://developer.apple.com/documentation/imageio/kcgimagepropertypngtitle)CGPDFContext.hAdded [CGPDFContextAddDocumentMetadata()](https://developer.apple.com/documentation/coregraphics/1456026-cgpdfcontextadddocumentmetadata)CGPath.hAdded [CGPathAddRelativeArc()](https://developer.apple.com/documentation/coregraphics/1411136-cgpathaddrelativearc)Added [CGPathCreateCopyByDashingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411134-init)Added [CGPathCreateCopyByStrokingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411128-init)Added [CGPathCreateCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411161-copy)Added [CGPathCreateMutableCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/1411150-cgpathcreatemutablecopybytransfo)Added [CGPathCreateWithEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1411177-cgpathcreatewithellipseinrect)Added [CGPathCreateWithRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411155-init)Modified [kCGLineJoinMiter](https://developer.apple.com/documentation/coregraphics/cglinejoin/kcglinejoinmiter)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [CGLineCap](https://developer.apple.com/documentation/coregraphics/cglinecap)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineJoinBevel](https://developer.apple.com/documentation/coregraphics/cglinejoin/bevel)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineJoinRound](https://developer.apple.com/documentation/coregraphics/cglinejoin/kcglinejoinround)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapRound](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapround)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapSquare](https://developer.apple.com/documentation/coregraphics/cglinecap/square)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [CGLineJoin](https://developer.apple.com/documentation/coregraphics/cglinejoin)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

Modified [kCGLineCapButt](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapbutt)

|  | Header |
| --- | --- |
| From | CGContext.h |
| To | CGPath.h |

CGWindow.hAdded [kCGWindowImageBestResolution](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/kcgwindowimagebestresolution)Added [kCGWindowImageNominalResolution](https://developer.apple.com/documentation/coregraphics/cgwindowimageoption/1455597-nominalresolution)CTDefines.hAdded #def CT_AVAILABLE_BUT_DEPRECATEDAdded #def CT_AVAILABLE_STARTINGCTFont.hAdded [CTFontDrawGlyphs()](https://developer.apple.com/documentation/coretext/1509850-ctfontdrawglyphs)Added [CTFontGetLigatureCaretPositions()](https://developer.apple.com/documentation/coretext/1508820-ctfontgetligaturecaretpositions)Added [kCTFontTableKerx](https://developer.apple.com/documentation/coretext/1524658-anonymous/kctfonttablekerx)Added [kCTFontTableSbit](https://developer.apple.com/documentation/coretext/1524658-anonymous/kctfonttablesbit)Added [kCTFontTableSbix](https://developer.apple.com/documentation/coretext/kctfonttablesbix)CTFontCollection.hAdded [CTFontCollectionCopyExclusionDescriptors()](https://developer.apple.com/documentation/coretext/1510000-ctfontcollectioncopyexclusiondes)Added [CTFontCollectionCopyFontAttribute()](https://developer.apple.com/documentation/coretext/1509577-ctfontcollectioncopyfontattribut)Added [CTFontCollectionCopyFontAttributes()](https://developer.apple.com/documentation/coretext/1511083-ctfontcollectioncopyfontattribut)Added [CTFontCollectionCopyOptions](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions)Added [CTFontCollectionCopyQueryDescriptors()](https://developer.apple.com/documentation/coretext/1510010-ctfontcollectioncopyquerydescrip)Added [CTFontCollectionCreateMatchingFontDescriptorsForFamily()](https://developer.apple.com/documentation/coretext/1508637-ctfontcollectioncreatematchingfo)Added [CTFontCollectionCreateMatchingFontDescriptorsWithOptions()](https://developer.apple.com/documentation/coretext/1509397-ctfontcollectioncreatematchingfo)Added [CTFontCollectionCreateMutableCopy()](https://developer.apple.com/documentation/coretext/1509247-ctfontcollectioncreatemutablecop)Added [CTFontCollectionSetExclusionDescriptors()](https://developer.apple.com/documentation/coretext/1509406-ctfontcollectionsetexclusiondesc)Added [CTFontCollectionSetQueryDescriptors()](https://developer.apple.com/documentation/coretext/1509060-ctfontcollectionsetquerydescript)Added [CTMutableFontCollectionRef](https://developer.apple.com/documentation/coretext/ctmutablefontcollectionref)Added [kCTFontCollectionCopyDefaultOptions](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopydefaultoptions)Added [kCTFontCollectionCopyStandardSort](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/1509424-standardsort)Added [kCTFontCollectionCopyUnique](https://developer.apple.com/documentation/coretext/ctfontcollectioncopyoptions/kctfontcollectioncopyunique)Added [kCTFontCollectionDisallowAutoActivationOption](https://developer.apple.com/documentation/coretext/kctfontcollectiondisallowautoactivationoption)Added [kCTFontCollectionIncludeDisabledFontsOption](https://developer.apple.com/documentation/coretext/kctfontcollectionincludedisabledfontsoption)Modified [CTFontCollectionCreateCopyWithFontDescriptors()](https://developer.apple.com/documentation/coretext/1510692-ctfontcollectioncreatecopywithfo)

|  | Declaration |
| --- | --- |
| From | CTFontCollectionRef CTFontCollectionCreateCopyWithFontDescriptors ( CTFontCollectionRef original, CFArrayRef descriptors, CFDictionaryRef options); |
| To | CTFontCollectionRef CTFontCollectionCreateCopyWithFontDescriptors ( CTFontCollectionRef original, CFArrayRef queryDescriptors, CFDictionaryRef options); |

Modified [CTFontCollectionCreateWithFontDescriptors()](https://developer.apple.com/documentation/coretext/1509202-ctfontcollectioncreatewithfontde)

|  | Declaration |
| --- | --- |
| From | CTFontCollectionRef CTFontCollectionCreateWithFontDescriptors ( CFArrayRef descriptors, CFDictionaryRef options); |
| To | CTFontCollectionRef CTFontCollectionCreateWithFontDescriptors ( CFArrayRef queryDescriptors, CFDictionaryRef options); |

CTFontTraits.hAdded [kCTFontColorGlyphsTrait](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/1508808-colorglyphstrait)CTFrame.hAdded [CTFramePathFillRule](https://developer.apple.com/documentation/coretext/ctframepathfillrule)Added [kCTFrameClippingPathsAttributeName](https://developer.apple.com/documentation/coretext/kctframeclippingpathsattributename)Added [kCTFramePathClippingPathAttributeName](https://developer.apple.com/documentation/coretext/kctframepathclippingpathattributename)Added [kCTFramePathFillEvenOdd](https://developer.apple.com/documentation/coretext/ctframepathfillrule/evenodd)Added [kCTFramePathFillRuleAttributeName](https://developer.apple.com/documentation/coretext/kctframepathfillruleattributename)Added [kCTFramePathFillWindingNumber](https://developer.apple.com/documentation/coretext/ctframepathfillrule/windingnumber)Added [kCTFramePathWidthAttributeName](https://developer.apple.com/documentation/coretext/kctframepathwidthattributename)CTParagraphStyle.hAdded [kCTParagraphStyleSpecifierLineSpacingAdjustment](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/linespacingadjustment)Added [kCTParagraphStyleSpecifierMaximumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/maximumlinespacing)Added [kCTParagraphStyleSpecifierMinimumLineSpacing](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier/kctparagraphstylespecifierminimumlinespacing)CTStringAttributes.hAdded [kCTRunDelegateAttributeName](https://developer.apple.com/documentation/coretext/kctrundelegateattributename)CTTypesetter.hAdded [CTTypesetterCreateLineWithOffset()](https://developer.apple.com/documentation/coretext/1510023-cttypesettercreatelinewithoffset)Added [CTTypesetterSuggestClusterBreakWithOffset()](https://developer.apple.com/documentation/coretext/1511119-cttypesettersuggestclusterbreakw)Added [CTTypesetterSuggestLineBreakWithOffset()](https://developer.apple.com/documentation/coretext/1508862-cttypesettersuggestlinebreakwith)ColorSyncDeprecated.hAdded #def DEPRECATED_IN_MAC_OS_X_VERSION_10_6_AND_LATERModified [CMCountProfileElements()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804963-cmcountprofileelements)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMError](https://developer.apple.com/documentation/coremotion/cmerror)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805253-cmsetdeviceprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileAccessUPP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetImageSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805267-cmgetimagespace)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804932-cmsetsystemprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMDeviceProfileArrayPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilearrayptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMM_GetProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805247-cmsetdeviceprofiles)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CMMatchOption

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCopyProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805020-cmcopyprofilelocalizedstringdict)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetProfileElementSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804980-cmsetprofileelementsize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMValidateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804856-cmvalidateprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMConvertRGBFloatBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWFillLookupTexture()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805126-cwfilllookuptexture)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [NCMUnflattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804901-ncmunflattenprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetPS2ColorRenderingIntent()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805196-cmgetps2colorrenderingintent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified kCMIlluminantD65

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMProfileMD5Ptr](https://developer.apple.com/documentation/applicationservices/cmprofilemd5ptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805289-cmgetgammabyavid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMDeviceInfoPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceinfoptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [NCWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805091-ncwconcatcolorworld)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileSearchRecordHandle

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertXYZToYxy()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805142-cmconvertxyztoyxy)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMBitmapColorSpace](https://developer.apple.com/documentation/applicationservices/cmbitmapcolorspace)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileHandle

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805177-cmconvertxyztoxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CMM_MatchFloatBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMSetPreferredCMM()

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMUnregisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805234-cmunregistercolordevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMUnembedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805271-cmunembedimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CMM_MatchBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMUpdateProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805356-cmupdateprofilesearch)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetCWInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804984-cmgetpartialprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804955-cmgetprofilebyavid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMProfileModified()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804872-cmprofilemodified)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMIterateCMMInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805185-cmiteratecmminfo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWMatchBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805116-cwmatchbitmap)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805087-cwconcatcolorworld)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetIndProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805002-cmgetindprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805235-cmgetdefaultdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMIterateColorDevices()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805262-cmiteratecolordevices)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMIterateDeviceInfoProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceinfoprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMLaunchControlPanel()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805294-cmlaunchcontrolpanel)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMWorldRef](https://developer.apple.com/documentation/applicationservices/cmworldref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [NCMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804889-ncmgetprofilelocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetIndNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805059-cmgetindnamedcolorvalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMUpdateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804864-cmupdateprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertXYZToFixedXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805169-cmconvertxyztofixedxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMSetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805238-cmsetdefaultdevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileSearchRef

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMNewProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804911-cmnewprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCloneProfileRef()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804891-cmcloneprofileref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804879-cmgetprofileheader)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMProfileIdentifierFolderSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805374-cmprofileidentifierfoldersearch)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetScriptProfileDescription()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805029-cmgetscriptprofiledescription)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CWColorWorldSetProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805251-cmsetdevicedefaultprofileid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805257-cmgetdevicestate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805258-cmsetdevicestate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWMatchColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805108-cwmatchcolors)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetNamedColorName()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805072-cmgetnamedcolorname)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805284-cmgetindimageprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804940-cmgetdefaultprofilebyspace)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertRGBToHLS()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805149-cmconvertrgbtohls)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProfileElementExists()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804967-cmprofileelementexists)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMBitmapCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMM_CheckColors()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMIterateColorSyncFolder()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805039-cmsetprofiledescriptions)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMM_ConcatColorWorld()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertHSVToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805160-cmconverthsvtorgb)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified kCMIlluminantD50

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804926-cmgetsystemprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804948-cmgetdefaultprofilebyuse)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805034-cmgetprofiledescriptions)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMConvertXYZFloatBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804944-cmsetdefaultprofilebyspace)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMSetProfileElementReference()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805005-cmsetprofileelementreference)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804973-cmgetprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCopyProfileDescriptionString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805012-cmcopyprofiledescriptionstring)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetColorSyncFolderSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804907-cmgetcolorsyncfolderspec)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMSetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804959-cmsetprofilebyavid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMMIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmmiterateprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertRGBToHSV()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805155-cmconvertrgbtohsv)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProfileIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmprofileiterateprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetPS2ColorRendering()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805202-cmgetps2colorrendering)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertLuvToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805140-cmconvertluvtoxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [NCWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804918-ncwnewlinkprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMRegisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805231-cmregistercolordevice)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805286-cmsetindimageprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CMM_CreateLinkProfile()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMDeviceID](https://developer.apple.com/documentation/applicationservices/cmdeviceid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMIterateDeviceProfileProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceprofileprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805256-cmgetdeviceprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805240-cmgetdevicefactoryprofiles)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMMatchFlag

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWCheckColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805111-cwcheckcolors)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileFilterUPP

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805025-cmsetprofilelocalizedstringdicti)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMM_CheckBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMNewProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805344-cmnewprofilesearch)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetPreferredCMM()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805182-cmgetpreferredcmm)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetNamedColorInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805047-cmgetnamedcolorinfo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804977-cmsetprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSearchGetIndProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805362-cmsearchgetindprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMDisposeProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805358-cmdisposeprofilesearch)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMMatchImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805273-cmmatchimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CM2ProfileHandle](https://developer.apple.com/documentation/applicationservices/cm2profilehandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804989-cmsetpartialprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CWGetCMMSignature()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConcatCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileIdentifierPtr

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804885-cmgetprofilelocation)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetPS2ColorSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805191-cmgetps2colorspace)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805241-cmsetdevicefactoryprofiles)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSearchGetIndProfileFileSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805365-cmsearchgetindprofilefilespec)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProfileMD5](https://developer.apple.com/documentation/applicationservices/cmprofilemd5)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMValidImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805264-cmvalidimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMDeviceProfileID](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMFloatBitmapMakeChunky()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/cmchromaticadaptation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805249-cmgetdevicedefaultprofileid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMLinkImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805278-cmlinkimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMMIterateUPP](https://developer.apple.com/documentation/applicationservices/cmmiterateupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertLabToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805134-cmconvertlabtoxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMAppleProfileHeader](https://developer.apple.com/documentation/applicationservices/1560290-cmappleprofileheader)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileAccessProcPtr

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMBitmapCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [NCMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804936-ncmsetsystemprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProfileIterateUPP](https://developer.apple.com/documentation/applicationservices/cmprofileiterateupp)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMDisplayIDType](https://developer.apple.com/documentation/applicationservices/cmdisplayidtype)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMProfileRef](https://developer.apple.com/documentation/applicationservices/cmprofileref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileFilterProcPtr

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMOpenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804853-cmopenprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCreateProfileIdentifier()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805369-cmcreateprofileidentifier)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMConvertFixedXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805174-cmconvertfixedxyztoxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProfileIdentifierListSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805376-cmprofileidentifierlistsearch)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified CMM_ValidateProfile()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetIndProfileElementInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804996-cmgetindprofileelementinfo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileMD5()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804876-cmgetprofilemd5)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertXYZToLuv()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805137-cmconvertxyztoluv)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMLabToLabProcPtr](https://developer.apple.com/documentation/applicationservices/cmlabtolabprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMM_MatchColors()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMDeviceState](https://developer.apple.com/documentation/applicationservices/cmdevicestate)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804951-cmsetdefaultprofilebyuse)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMProofImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805276-cmproofimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMIterateDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805263-cmiteratedeviceprofiles)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMProfileCopyICCData()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertHLSToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805152-cmconverthlstorgb)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMFlattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804897-cmflattenprofile)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetNamedColorIndex()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805065-cmgetnamedcolorindex)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CWColorWorldGetProperty()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertYxyToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805146-cmconvertyxytoxyz)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetColorSyncVersion()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805293-cmgetcolorsyncversion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCopyProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804870-cmcopyprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWCheckBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805121-cwcheckbitmap)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertRGBToGray()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805164-cmconvertrgbtogray)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMCloseProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804861-cmcloseprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMMatchRef

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMRemoveProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805008-cmremoveprofileelement)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMConvertXYZToLab()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805133-cmconvertxyztolab)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMSetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805291-cmsetgammabyavid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetPS2ColorRenderingVMSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805206-cmgetps2colorrenderingvmsize)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetProfileRefCount()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804894-cmgetprofilerefcount)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMSetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804882-cmsetprofileheader)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified CMMatchFloatBitmap()

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMEmbedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805269-cmembedimage)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMCopyProfileLocalizedString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805016-cmcopyprofilelocalizedstring)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMCountImageProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805281-cmcountimageprofiles)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMGetDeviceInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805260-cmgetdeviceinfo)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805245-cmgetdeviceprofiles)

|  | Deprecation |
| --- | --- |
| From | OS X v10.5 |
| To | OS X v10.6 |

Modified [CMConcatCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackprocptr)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMGetNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805053-cmgetnamedcolorvalue)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CMMakeProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804920-cmmakeprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [NCWNewColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805079-ncwnewcolorworld)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified [CWDisposeColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805102-cwdisposecolorworld)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

Modified refcon

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.6 |

CoreText.hAdded [#def kCTVersionNumber10_7](https://developer.apple.com/documentation/coretext/kctversionnumber10_7)Displays.hRemoved AVLocationPtrRemoved AVLocationRecRemoved AVPowerStatePtrRemoved AVPowerStateRecRemoved DMAddDisplay()Removed DMBeginConfigureDisplays()Removed DMBlockMirroring()Removed DMCanMirrorNow()Removed DMCheckDisplayMode()Removed DMComponentListEntryPtrRemoved DMComponentListEntryRecRemoved DMComponentListIteratorProcPtrRemoved DMComponentListIteratorUPPRemoved DMConfirmConfiguration()Removed DMDepthInfoBlockPtrRemoved DMDepthInfoBlockRecRemoved DMDepthInfoPtrRemoved DMDepthInfoRecRemoved DMDisableDisplay()Removed DMDisplayListIteratorProcPtrRemoved DMDisplayListIteratorUPPRemoved DMDisplayModeListEntryPtrRemoved DMDisplayModeListEntryRecRemoved DMDisplayModeListIteratorProcPtrRemoved DMDisplayModeListIteratorUPPRemoved DMDisplayTimingInfoPtrRemoved DMDisplayTimingInfoRecRemoved DMDisposeAVComponent()Removed DMDisposeDisplay()Removed DMDisposeList()Removed DMDrawDesktopRect()Removed DMDrawDesktopRegion()Removed DMEnableDisplay()Removed DMEndConfigureDisplays()Removed DMExtendedNotificationProcPtrRemoved DMExtendedNotificationUPPRemoved DMFidelityTypeRemoved DMGetAVPowerState()Removed DMGetDeskRegion()Removed DMGetDeviceAVIDByPortAVID()Removed DMGetDeviceComponentByAVID()Removed DMGetDisplayComponent()Removed DMGetDisplayIDByGDevice()Removed DMGetDisplayMode()Removed DMGetEnableByAVID()Removed DMGetFirstScreenDevice()Removed DMGetGDeviceByDisplayID()Removed DMGetGraphicInfoByAVID()Removed DMGetIndexedComponentFromList()Removed DMGetIndexedDisplayModeFromList()Removed DMGetNameByAVID()Removed DMGetNextMirroredDevice()Removed DMGetNextScreenDevice()Removed DMGetPortComponentByAVID()Removed DMIsMirroringOn()Removed DMListIndexTypeRemoved DMListTypeRemoved DMMakeAndModelPtrRemoved DMMakeAndModelRecRemoved DMMirrorDevices()Removed DMModalFilterUPPRemoved DMMoveDisplay()Removed DMNewAVDeviceList()Removed DMNewAVEngineList()Removed DMNewAVIDByDeviceComponent()Removed DMNewAVIDByPortComponent()Removed DMNewAVPanelList()Removed DMNewAVPortListByDeviceAVID()Removed DMNewAVPortListByPortType()Removed DMNewDisplay()Removed DMNewDisplayModeList()Removed DMNotificationProcPtrRemoved DMNotificationUPPRemoved DMProcessInfoPtrRemoved DMProfileListEntryPtrRemoved DMProfileListEntryRecRemoved DMProfileListIteratorProcPtrRemoved DMProfileListIteratorUPPRemoved DMQDIsMirroringCapable()Removed DMRegisterExtendedNotifyProc()Removed DMRegisterNotifyProc()Removed DMRemoveDisplay()Removed DMRemoveExtendedNotifyProc()Removed DMRemoveNotifyProc()Removed DMResolveDisplayComponents()Removed DMSaveScreenPrefs()Removed DMSendDependentNotification()Removed DMSetAVPowerState()Removed DMSetDisplayComponent()Removed DMSetDisplayMode()Removed DMSetEnableByAVID()Removed DMSetMainDisplay()Removed DMUnblockMirroring()Removed DMUnmirrorDevice()Removed DependentNotifyPtrRemoved DependentNotifyRecRemoved DisplayListEntryPtrRemoved DisplayListEntryRecRemoved DisposeDMComponentListIteratorUPP()Removed DisposeDMDisplayListIteratorUPP()Removed DisposeDMDisplayModeListIteratorUPP()Removed DisposeDMExtendedNotificationUPP()Removed DisposeDMNotificationUPP()Removed DisposeDMProfileListIteratorUPP()Removed InvokeDMComponentListIteratorUPP()Removed InvokeDMDisplayListIteratorUPP()Removed InvokeDMDisplayModeListIteratorUPP()Removed InvokeDMExtendedNotificationUPP()Removed InvokeDMNotificationUPP()Removed InvokeDMProfileListIteratorUPP()Removed NewDMComponentListIteratorUPP()Removed NewDMDisplayListIteratorUPP()Removed NewDMDisplayModeListIteratorUPP()Removed NewDMExtendedNotificationUPP()Removed NewDMNotificationUPP()Removed NewDMProfileListIteratorUPP()Removed dmAllDisplaysRemoved dmOnlyActiveDisplaysRemoved kAEDisplayNoticeRemoved kAEDisplaySummaryRemoved kAESystemConfigNoticeRemoved kAddDisplayBitRemoved kAllowDuplicatesBitRemoved kAnyDeviceTypeRemoved kAnyEngineTypeRemoved kAnyPanelTypeRemoved kAnyPortTypeRemoved kBeginEndConfigureBitRemoved kComponentListNotPreferredBitRemoved kComponentListNotPreferredMaskRemoved kDMForceNumbersMaskRemoved kDMModeListExcludeCustomModesMaskRemoved kDMModeListExcludeDisplayModesMaskRemoved kDMModeListExcludeDriverModesMaskRemoved kDMModeListIncludeAllModesMaskRemoved kDMModeListIncludeOfflineModesMaskRemoved kDMModeListPreferSafeModesMaskRemoved kDMModeListPreferStretchedModesMaskRemoved kDMNotifyDependentsRemoved kDMNotifyDisplayDidWakeRemoved kDMNotifyDisplayWillSleepRemoved kDMNotifyEventRemoved kDMNotifyExtendEventRemoved kDMNotifyInstalledRemoved kDMNotifyPrepRemoved kDMNotifyRemovedRemoved kDMNotifyRequestConnectionProbeRemoved kDMNotifyRequestDisplayProbeRemoved kDMNotifyResumeConfigureRemoved kDMNotifySuspendConfigureRemoved kDMSupressNameMaskRemoved kDMSupressNumbersMaskRemoved kDefaultFidelityRemoved kDefaultManufacturerFidelityRemoved kDependentNotifyClassDisplayMgrOverrideRemoved kDependentNotifyClassDriverOverrideRemoved kDependentNotifyClassProfileChangedRemoved kDependentNotifyClassShowCursorRemoved kDepthNotAvailableBitRemoved kDisabledDisplayBitRemoved kDisplayGestaltBrightnessAffectsGammaMaskRemoved kDisplayGestaltCalibratorAttrRemoved kDisplayGestaltDisplayCommunicationAttrRemoved kDisplayGestaltForbidI2CMaskRemoved kDisplayGestaltUseI2CPowerMaskRemoved kDisplayGestaltViewAngleAffectsGammaMaskRemoved kDisplayModeEntryVersionOneRemoved kDisplayModeEntryVersionZeroRemoved kDisplayModeListNotPreferredBitRemoved kDisplayModeListNotPreferredMaskRemoved kDisplayTimingInfoReservedCountVersionZeroRemoved kDisplayTimingInfoVersionZeroRemoved kDisposeDisplayBitRemoved kDummyDeviceIDRemoved kEnabledDisplayBitRemoved kExtendedNotificationProcRemoved kFirstDisplayIDRemoved kForceConfirmBitRemoved kForceConfirmMaskRemoved kForceNumberBitRemoved kForceNumberMaskRemoved kFullDependencyNotifyRemoved kFullNotifyRemoved kIncludeHardwareMirroredDisplaysMaskRemoved kIncludeOfflineDisplaysMaskRemoved kIncludeOfflineDummyDisplaysMaskRemoved kIncludeOnlineActiveDisplaysMaskRemoved kIncludeOnlineDisabledDisplaysMaskRemoved kInvalidDisplayIDRemoved kMakeAndModelReservedCountRemoved kMinimumFidelityRemoved kMirrorDisplayBitRemoved kModeNotResizeBitRemoved kMovedDisplayBitRemoved kNeverShowModeBitRemoved kNewDisplayBitRemoved kNoFidelityRemoved kNoSwitchConfirmBitRemoved kPLIncludeOfflineDevicesBitRemoved kRemoveDisplayBitRemoved kSetDisplayModeBitRemoved kSetMainDisplayBitRemoved kShowModeBitRemoved kSuppressNameBitRemoved kSuppressNameMaskRemoved kSuppressNumberBitRemoved kSuppressNumberMaskRemoved kUnMirrorDisplayBitRemoved keyDMConfigFlagsRemoved keyDMConfigReservedRemoved keyDMConfigVersionRemoved keyDeviceDepthModeRemoved keyDeviceFlagsRemoved keyDeviceRectRemoved keyDisplayComponentRemoved keyDisplayDeviceRemoved keyDisplayFlagsRemoved keyDisplayIDRemoved keyDisplayMirroredIdRemoved keyDisplayModeRemoved keyDisplayModeReservedRemoved keyDisplayNewConfigRemoved keyDisplayOldConfigRemoved keyDisplayReservedRemoved keyPixMapAlignmentRemoved keyPixMapCmpCountRemoved keyPixMapCmpSizeRemoved keyPixMapColorTableSeedRemoved keyPixMapHResolutionRemoved keyPixMapPixelSizeRemoved keyPixMapPixelTypeRemoved keyPixMapRectRemoved keyPixMapResReservedRemoved keyPixMapReservedRemoved keyPixMapVResolutionRemoved keySummaryChangesRemoved keySummaryMenubarFontSync.hRemoved FNSEnabled()Removed FNSFeatureFlagsRemoved FNSFontProfileRemoved FNSFontReferenceRemoved FNSMatchDefaultsGet()Removed FNSMatchOptionsRemoved FNSObjectVersionRemoved FNSProfileAddReference()Removed FNSProfileClear()Removed FNSProfileClose()Removed FNSProfileCompact()Removed FNSProfileCountReferences()Removed FNSProfileCreate()Removed FNSProfileCreateWithFSRef()Removed FNSProfileGetIndReference()Removed FNSProfileGetVersion()Removed FNSProfileMatchReference()Removed FNSProfileOpen()Removed FNSProfileOpenWithFSRef()Removed FNSProfileRemoveIndReference()Removed FNSProfileRemoveReference()Removed FNSReferenceCountNames()Removed FNSReferenceCreate()Removed FNSReferenceCreateFromFamily()Removed FNSReferenceDispose()Removed FNSReferenceFindName()Removed FNSReferenceFlatten()Removed FNSReferenceFlattenedSize()Removed FNSReferenceGetFamilyInfo()Removed FNSReferenceGetIndName()Removed FNSReferenceGetVersion()Removed FNSReferenceMatch()Removed FNSReferenceMatchFamilies()Removed FNSReferenceMatchFonts()Removed FNSReferenceUnflatten()Removed FNSSysInfoRemoved FNSSysInfoGet()Removed kFNSCreatorDefaultRemoved kFNSCurSysInfoVersionRemoved kFNSMatchAATLayoutRemoved kFNSMatchATSUMetricsRemoved kFNSMatchAllRemoved kFNSMatchDefaultsRemoved kFNSMatchEncodingsRemoved kFNSMatchGlyphsRemoved kFNSMatchKerningRemoved kFNSMatchNamesRemoved kFNSMatchPrintEncodingRemoved kFNSMatchQDMetricsRemoved kFNSMatchTechnologyRemoved kFNSMatchWSLayoutRemoved kFNSMissingDataNoMatchRemoved kFNSProfileFileTypeRemoved kFNSVersionDontCareFonts.hRemoved FMActivateFonts()Removed FMCreateFontFamilyInstanceIterator()Removed FMCreateFontFamilyIterator()Removed FMCreateFontIterator()Removed FMDeactivateFonts()Removed FMDisposeFontFamilyInstanceIterator()Removed FMDisposeFontFamilyIterator()Removed FMDisposeFontIterator()Removed FMFontGetCGFontRefFromFontFamilyInstance()Removed FMGetATSFontFamilyRefFromFontFamily()Removed FMGetATSFontRefFromFont()Removed FMGetFontContainer()Removed FMGetFontContainerFromFontFamilyInstance()Removed FMGetFontFamilyFromATSFontFamilyRef()Removed FMGetFontFamilyFromName()Removed FMGetFontFamilyGeneration()Removed FMGetFontFamilyInstanceFromFont()Removed FMGetFontFamilyName()Removed FMGetFontFamilyResource()Removed FMGetFontFamilyTextEncoding()Removed FMGetFontFormat()Removed FMGetFontFromATSFontRef()Removed FMGetFontFromFontFamilyInstance()Removed FMGetFontGeneration()Removed FMGetFontTable()Removed FMGetFontTableDirectory()Removed FMGetGeneration()Removed FMGetNextFont()Removed FMGetNextFontFamily()Removed FMGetNextFontFamilyInstance()Removed FMOutPtrRemoved FMOutputRemoved FMOutputPtrRemoved FMResetFontFamilyInstanceIterator()Removed FMResetFontFamilyIterator()Removed FMResetFontIterator()Removed FMSwapFont()Removed FMetricRecRemoved FMetricRecHandleRemoved FMetricRecPtrRemoved FetchFontInfo()Removed FontFamilyIDRemoved FontMetrics()Removed FontPointSizeRemoved GetAppFont()Removed GetDefFontSize()Removed GetFNum()Removed GetFontName()Removed GetOutlinePreferred()Removed GetPreserveGlyph()Removed GetSysFont()Removed IsAntiAliasedTextEnabled()Removed IsOutline()Removed OutlineMetrics()Removed QDTextBounds()Removed RealFont()Removed SetAntiAliasedTextEnabled()Removed SetFScaleDisable()Removed SetFractEnable()Removed SetOutlinePreferred()Removed SetPreserveGlyph()Removed WidEntryRemoved WidTableRemoved WidthTableRemoved WidthTableHdlRemoved WidthTablePtrRemoved applFontRemoved appleMarkRemoved athens (no architecture available)Removed cairo (no architecture available)Removed checkMarkRemoved commandMarkRemoved courier (no architecture available)Removed diamondMarkRemoved fixedFontRemoved fontWidRemoved fxdFntHRemoved fxdFntHWRemoved fxdFntWRemoved geneva (no architecture available)Removed helvetica (no architecture available)Removed kFMDefaultActivationContextRemoved kFMDefaultIterationScopeRemoved kFMDefaultOptionsRemoved kFMGlobalActivationContextRemoved kFMGlobalIterationScopeRemoved kFMLocalActivationContextRemoved kFMLocalIterationScopeRemoved kFMUseGlobalScopeOptionRemoved kFontIDAthensRemoved kFontIDCairoRemoved kFontIDCourierRemoved kFontIDGenevaRemoved kFontIDHelveticaRemoved kFontIDLondonRemoved kFontIDLosAngelesRemoved kFontIDMobileRemoved kFontIDMonacoRemoved kFontIDNewYorkRemoved kFontIDSanFranciscoRemoved kFontIDSymbolRemoved kFontIDTimesRemoved kFontIDTorontoRemoved kFontIDVeniceRemoved kPlatformDefaultGuiFontIDRemoved london (no architecture available)Removed losAngeles (no architecture available)Removed mobile (no architecture available)Removed monaco (no architecture available)Removed newYork (no architecture available)Removed propFontRemoved prpFntHRemoved prpFntHWRemoved prpFntWRemoved sanFran (no architecture available)Removed symbol (no architecture available)Removed systemFontRemoved times (no architecture available)Removed toronto (no architecture available)Removed venice (no architecture available)ImageIOBase.hAdded #def IMAGEIO_AVAILABLE_BUT_DEPRECATEDAdded #def IMAGEIO_AVAILABLE_STARTINGAdded #def IMAGEIO_EXTERNAdded #def IMAGEIO_EXTERN_C_BEGINAdded #def IMAGEIO_EXTERN_C_ENDInternetConfig.hModified [ICGetIndPref()](https://developer.apple.com/documentation/applicationservices/1578503-icgetindpref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICMapFilename()](https://developer.apple.com/documentation/applicationservices/1578490-icmapfilename)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICMapEntriesFilename()](https://developer.apple.com/documentation/applicationservices/1578539-icmapentriesfilename)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICAddMapEntry()](https://developer.apple.com/documentation/applicationservices/1578495-icaddmapentry)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICCreateGURLEvent()](https://developer.apple.com/documentation/applicationservices/1578532-iccreategurlevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICStop()](https://developer.apple.com/documentation/applicationservices/1578518-icstop)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetPref()](https://developer.apple.com/documentation/applicationservices/1578522-icgetpref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICDeleteProfile()](https://developer.apple.com/documentation/applicationservices/1578483-icdeleteprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSetMapEntry()](https://developer.apple.com/documentation/applicationservices/1578540-icsetmapentry)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetSeed()](https://developer.apple.com/documentation/applicationservices/1578514-icgetseed)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICEditPreferences()](https://developer.apple.com/documentation/applicationservices/1578512-iceditpreferences)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetVersion()](https://developer.apple.com/documentation/applicationservices/1578536-icgetversion)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICEnd()](https://developer.apple.com/documentation/applicationservices/1578544-icend)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICAddProfile()](https://developer.apple.com/documentation/applicationservices/1578498-icaddprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetIndProfile()](https://developer.apple.com/documentation/applicationservices/1578519-icgetindprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICMapEntriesTypeCreator()](https://developer.apple.com/documentation/applicationservices/1578486-icmapentriestypecreator)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICBegin()](https://developer.apple.com/documentation/applicationservices/1578517-icbegin)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetCurrentProfile()](https://developer.apple.com/documentation/applicationservices/1578505-icgetcurrentprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetPrefHandle()](https://developer.apple.com/documentation/applicationservices/1578489-icgetprefhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICDeletePref()](https://developer.apple.com/documentation/applicationservices/1578534-icdeletepref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSendGURLEvent()](https://developer.apple.com/documentation/applicationservices/1578487-icsendgurlevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSetPref()](https://developer.apple.com/documentation/applicationservices/1578533-icsetpref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICDeleteMapEntry()](https://developer.apple.com/documentation/applicationservices/1578488-icdeletemapentry)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetDefaultPref()](https://developer.apple.com/documentation/applicationservices/1578528-icgetdefaultpref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetIndMapEntry()](https://developer.apple.com/documentation/applicationservices/1578493-icgetindmapentry)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICCountPref()](https://developer.apple.com/documentation/applicationservices/1578542-iccountpref)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICParseURL()](https://developer.apple.com/documentation/applicationservices/1578515-icparseurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICCountProfiles()](https://developer.apple.com/documentation/applicationservices/1578494-iccountprofiles)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICStart()](https://developer.apple.com/documentation/applicationservices/1578513-icstart)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetConfigName()](https://developer.apple.com/documentation/applicationservices/1578511-icgetconfigname)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetMapEntry()](https://developer.apple.com/documentation/applicationservices/1578510-icgetmapentry)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetProfileName()](https://developer.apple.com/documentation/applicationservices/1578523-icgetprofilename)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICFindPrefHandle()](https://developer.apple.com/documentation/applicationservices/1578526-icfindprefhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSetProfileName()](https://developer.apple.com/documentation/applicationservices/1578501-icsetprofilename)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICCountMapEntries()](https://developer.apple.com/documentation/applicationservices/1578509-iccountmapentries)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICGetPerm()](https://developer.apple.com/documentation/applicationservices/1578492-icgetperm)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICMapTypeCreator()](https://developer.apple.com/documentation/applicationservices/1578520-icmaptypecreator)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSetCurrentProfile()](https://developer.apple.com/documentation/applicationservices/1578485-icsetcurrentprofile)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICLaunchURL()](https://developer.apple.com/documentation/applicationservices/1578504-iclaunchurl)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

Modified [ICSetPrefHandle()](https://developer.apple.com/documentation/applicationservices/1578545-icsetprefhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X v10.7 |

PMCoreDeprecated.hAdded PMPrinterCreatePaperInfoListForMenu()Modified [PMPaperGetName()](https://developer.apple.com/documentation/applicationservices/core_printing/1805534-pmpapergetname)

|  | Header | Deprecation |
| --- | --- | --- |
| From | PMCore.h | _none_ |
| To | PMCoreDeprecated.h | OS X v10.7 |

PMDefinitions.hAdded [#def kPMPrintSelectionTitleKey](https://developer.apple.com/documentation/applicationservices/kpmprintselectiontitlekey)PMPrintAETypes.hAdded #def kPMPDFWorkFlowAEKeyAdded [#def kPMPDFWorkFlowAEProp](https://developer.apple.com/documentation/applicationservices/kpmpdfworkflowaeprop)Added #def kPMPDFWorkFlowAETypeAdded #def kPMPresetAEKeyAdded [#def kPMPresetAEProp](https://developer.apple.com/documentation/applicationservices/kpmpresetaeprop)Added #def kPMPresetAETypeAdded #def kPMSaveAsPDFAEKeyAdded [#def kPMSaveAsPDFAEProp](https://developer.apple.com/documentation/applicationservices/kpmsaveaspdfaeprop)Added #def kPMSaveAsPDFAETypeAdded #def kPMSaveAsPSAEKeyAdded [#def kPMSaveAsPSAEProp](https://developer.apple.com/documentation/applicationservices/kpmsaveaspsaeprop)Added #def kPMSaveAsPSAETypePMPrintSettingsKeys.hAdded #def kPMFitToPageKeyAdded [#def kPMFitToPageStr](https://developer.apple.com/documentation/applicationservices/kpmfittopagestr)PMPrintingDialogExtensions.hRemoved #def kPMQualityMediaPDEKindIDAdded #def kPMFaxAddressesPDEKindIDAdded #def kPMMediaQualityPDEKindIDAdded #def kPMSandboxCompatiblePDEsAdded #def kPMUniPrinterPDEKindIDAdded #def kPMUnsupportedPDEKindIDPalettes.hRemoved ActivatePalette()Removed AnimateEntry()Removed AnimatePalette()Removed CTab2Palette()Removed ColorInfoRemoved ColorInfoHandleRemoved ColorInfoPtrRemoved CopyPalette()Removed DisposePalette()Removed Entry2Index()Removed GetEntryColor()Removed GetEntryUsage()Removed GetGray()Removed GetNewPalette()Removed GetPalette()Removed GetPaletteUpdates()Removed HasDepth()Removed InitPalettes()Removed #def MacAnimatePaletteRemoved MacAnimatePalette() (no architecture available)Removed MacResizePalette() (no architecture available)Removed #def MacResizePaletteRemoved NSetPalette()Removed NewPalette()Removed PMgrVersion()Removed PaletteRemoved Palette2CTab()Removed PaletteHandleRemoved PalettePtrRemoved PmBackColor()Removed PmForeColor()Removed ResizePalette()Removed RestoreBack()Removed RestoreDeviceClut()Removed RestoreFore()Removed SaveBack()Removed SaveFore()Removed SetDepth()Removed SetEntryColor()Removed SetEntryUsage()Removed SetPalette()Removed SetPaletteUpdates()Removed pmAllUpdatesRemoved pmAnimatedRemoved pmBkUpdatesRemoved pmBlackRemoved pmCourteousRemoved pmDitheredRemoved pmExplicitRemoved pmFgUpdatesRemoved pmInhibitC2Removed pmInhibitC4Removed pmInhibitC8Removed pmInhibitG2Removed pmInhibitG4Removed pmInhibitG8Removed pmNoUpdatesRemoved pmTolerantRemoved pmWhitePictUtils.hRemoved CalcColorTableProcPtrRemoved CalcColorTableUPPRemoved ColorBankIs555Removed ColorBankIsCustomRemoved ColorBankIsExactAnd555Removed CommentSpecRemoved CommentSpecHandleRemoved CommentSpecPtrRemoved DisposeCalcColorTableUPP()Removed DisposeColorPickMethodProcPtrRemoved DisposeColorPickMethodUPPRemoved DisposeDisposeColorPickMethodUPP()Removed DisposeInitPickMethodUPP()Removed DisposePictInfo()Removed DisposeRecordColorsUPP()Removed FontSpecRemoved FontSpecHandleRemoved FontSpecPtrRemoved GetPictInfo()Removed GetPixMapInfo()Removed InitPickMethodProcPtrRemoved InitPickMethodUPPRemoved InvokeCalcColorTableUPP()Removed InvokeDisposeColorPickMethodUPP()Removed InvokeInitPickMethodUPP()Removed InvokeRecordColorsUPP()Removed NewCalcColorTableUPP()Removed NewDisposeColorPickMethodUPP()Removed NewInitPickMethodUPP()Removed NewPictInfo()Removed NewRecordColorsUPP()Removed PictInfoRemoved PictInfoHandleRemoved PictInfoIDRemoved PictInfoPtrRemoved RecordColorsProcPtrRemoved RecordColorsUPPRemoved RecordPictInfo()Removed RecordPixMapInfo()Removed RetrievePictInfo()Removed medianMethodRemoved popularMethodRemoved recordCommentsRemoved recordFontInfoRemoved returnColorTableRemoved returnPaletteRemoved suppressBlackAndWhiteRemoved systemMethodProcesses.hAdded [kProcessTransformToBackgroundApplication](https://developer.apple.com/documentation/applicationservices/1501117-anonymous/kprocesstransformtobackgroundapplication)Added [kProcessTransformToUIElementApplication](https://developer.apple.com/documentation/applicationservices/1501117-anonymous/kprocesstransformtouielementapplication)QDOffscreen.hRemoved AllowPurgePixels()Removed CTabChanged()Removed DisposeGWorld()Removed DisposeScreenBuffer()Removed GDeviceChanged()Removed GetGWorld()Removed GetGWorldDevice()Removed GetGWorldPixMap()Removed GetPixBaseAddr()Removed GetPixRowBytes()Removed GetPixelsState()Removed LockPixels()Removed NewGWorld()Removed NewGWorldFromPtr()Removed NewScreenBuffer()Removed NewTempScreenBuffer()Removed NoPurgePixels()Removed OffscreenVersion()Removed PixMap32Bit()Removed PixPatChanged()Removed PortChanged()Removed QDDone()Removed SetGWorld()Removed SetPixelsState()Removed UnlockPixels()Removed UpdateGWorld()Removed alignPixRemoved alignPixBitRemoved clipPixRemoved clipPixBitRemoved deviceIsAScreenRemoved deviceIsDCISurfaceRemoved deviceIsDDSurfaceRemoved deviceIsExternalBufferRemoved deviceIsGDISurfaceRemoved deviceIsIndirectRemoved deviceIsOverlaySurfaceRemoved deviceIsStaticRemoved deviceNeedsLockRemoved ditherPixRemoved ditherPixBitRemoved gwFlagErrRemoved gwFlagErrBitRemoved kAllocDirectDrawSurfaceRemoved kNativeEndianPixMapRemoved keepLocalRemoved keepLocalBitRemoved mapPixRemoved mapPixBitRemoved nativeEndianPixMapBitRemoved newDepthRemoved newDepthBitRemoved newRowBytesRemoved newRowBytesBitRemoved noNewDeviceRemoved noNewDeviceBitRemoved pixPurgeRemoved pixPurgeBitRemoved pixelsLockedRemoved pixelsLockedBitRemoved pixelsPurgeableRemoved pixelsPurgeableBitRemoved reallocPixRemoved reallocPixBitRemoved stretchPixRemoved stretchPixBitRemoved useDistantHdwrMemRemoved useDistantHdwrMemBitRemoved useLocalHdwrMemRemoved useLocalHdwrMemBitRemoved useTempMemRemoved useTempMemBitQDPictToCGContext.hRemoved QDPictCreateWithProvider()Removed QDPictCreateWithURL()Removed QDPictDrawToCGContext()Removed QDPictGetBounds()Removed QDPictGetResolution()Removed QDPictRefRemoved QDPictRelease()Removed QDPictRetain()Quickdraw.hAdded DisposeQDPrinterStatusUPP()Added InvokeQDPrinterStatusUPP()Added NewQDPrinterStatusUPP()Added [#def QD_HEADERS_ARE_PRIVATE](https://developer.apple.com/documentation/applicationservices/qd_headers_are_private)Modified NewQDGetPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DialogPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified RgnHandle

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PixPatHandle](https://developer.apple.com/documentation/applicationservices/pixpathandle)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDTextUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDTxMeasUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDPutPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdputpicprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDOvalUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified GWorldFlags

|  | Header |
| --- | --- |
| From | QDOffscreen.h |
| To | Quickdraw.h |

Modified DisposeColorComplementUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k2IndexedPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k2indexedpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrrectprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k32ABGRPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k32abgrpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDBitsUPP](https://developer.apple.com/documentation/applicationservices/qdbitsupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k32BGRAPixelFormat](https://developer.apple.com/documentation/applicationservices/k32bgrapixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k4IndexedGrayPixelFormat](https://developer.apple.com/documentation/applicationservices/k4indexedgraypixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDJShieldCursorUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kYUV411PixelFormat](https://developer.apple.com/documentation/applicationservices/kyuv411pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRegionParseDirection](https://developer.apple.com/documentation/applicationservices/qdregionparsedirection)

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [DragConstraint](https://developer.apple.com/documentation/applicationservices/dragconstraint)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDStdGlyphsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [CGrafPort](https://developer.apple.com/documentation/applicationservices/cgrafport)

|  | Header | 32/64-bit | Architectures |
| --- | --- | --- | --- |
| From | QuickdrawTypes.h | _Unknown_ | Unknown |
| To | Quickdraw.h | Both | i386,x86_64 |

Modified [GDevice](https://developer.apple.com/documentation/applicationservices/gdevice)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDArcUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [FontInfo](https://developer.apple.com/documentation/applicationservices/fontinfo)

|  | Header |
| --- | --- |
| From | QuickdrawText.h |
| To | Quickdraw.h |

Modified [k2IndexedGrayPixelFormat](https://developer.apple.com/documentation/applicationservices/k2indexedgraypixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PixPat](https://developer.apple.com/documentation/applicationservices/pixpat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDBitsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeRegionToRectsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [BitMapHandle](https://developer.apple.com/documentation/applicationservices/bitmaphandle)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorSpec](https://developer.apple.com/documentation/kernel/colorspec)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDBitsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDCommentUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [CQDProcs](https://developer.apple.com/documentation/applicationservices/cqdprocs)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeDragGrayRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [Pattern](https://developer.apple.com/documentation/applicationservices/pattern)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDPrinterStatusProcPtr](https://developer.apple.com/documentation/applicationservices/qdprinterstatusprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewRegionToRectsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [QDPolyProcPtr](https://developer.apple.com/documentation/applicationservices/qdpolyprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDOpcodeProcPtr](https://developer.apple.com/documentation/applicationservices/qdopcodeprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDOpcodeUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeColorSearchUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k16LE555PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k16le555pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kYUV211PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/kyuv211pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDGetPicUPP](https://developer.apple.com/documentation/applicationservices/qdgetpicupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kYUVSPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/kyuvspixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDPrinterStatusUPP](https://developer.apple.com/documentation/applicationservices/qdprinterstatusupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewColorSearchUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k4IndexedPixelFormat](https://developer.apple.com/documentation/applicationservices/k4indexedpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [MacPolygon](https://developer.apple.com/documentation/applicationservices/macpolygon)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [RegionToRectsProcPtr](https://developer.apple.com/documentation/applicationservices/regiontorectsprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [CSpecArray](https://developer.apple.com/documentation/applicationservices/cspecarray)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [GrafVerb](https://developer.apple.com/documentation/applicationservices/grafverb)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDTxMeasUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDGetPicProcPtr](https://developer.apple.com/documentation/applicationservices/qdgetpicprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorSearchUPP](https://developer.apple.com/documentation/applicationservices/colorsearchupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kNoConstraint](https://developer.apple.com/documentation/applicationservices/knoconstraint)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDOpcodeUPP](https://developer.apple.com/documentation/applicationservices/qdopcodeupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PatPtr](https://developer.apple.com/documentation/applicationservices/patptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDTextUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDArcUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDGetPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorTable](https://developer.apple.com/documentation/applicationservices/colortable)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified PixMapPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDRRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDJShieldCursorUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDPolyUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [CQDProcsPtr](https://developer.apple.com/documentation/applicationservices/cqdprocsptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDGetPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDPolyUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kYVYU422PixelFormat](https://developer.apple.com/documentation/applicationservices/kyvyu422pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified size

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified PicHandle

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorSearchProcPtr](https://developer.apple.com/documentation/applicationservices/colorsearchprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified QDEndCGContext()

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [kYVU9PixelFormat](https://developer.apple.com/documentation/applicationservices/kyvu9pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [BitMapPtr](https://developer.apple.com/documentation/applicationservices/bitmapptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDTextUPP](https://developer.apple.com/documentation/applicationservices/qdtextupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified CTabHandle

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDPolyUPP](https://developer.apple.com/documentation/applicationservices/qdpolyupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [GrafPort](https://developer.apple.com/documentation/applicationservices/grafport)

|  | Header | 32/64-bit | Architectures |
| --- | --- | --- | --- |
| From | QuickdrawTypes.h | _Unknown_ | Unknown |
| To | Quickdraw.h | Both | i386,x86_64 |

Modified [QDRectProcPtr](https://developer.apple.com/documentation/applicationservices/qdrectprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kHorizontalConstraint](https://developer.apple.com/documentation/applicationservices/khorizontalconstraint)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PolyPtr](https://developer.apple.com/documentation/applicationservices/polyptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [RGBColor](https://developer.apple.com/documentation/kernel/rgbcolor)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDLineUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDOvalUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorComplementProcPtr](https://developer.apple.com/documentation/applicationservices/colorcomplementprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k8IndexedPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k8indexedpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDOpcodeUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDTextProcPtr](https://developer.apple.com/documentation/applicationservices/qdtextprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [Picture](https://developer.apple.com/documentation/applicationservices/picture)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k16LE565PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k16le565pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDCommentProcPtr](https://developer.apple.com/documentation/applicationservices/qdcommentprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDBitsProcPtr](https://developer.apple.com/documentation/applicationservices/qdbitsprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified printerStatus

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDLineUPP](https://developer.apple.com/documentation/applicationservices/qdlineupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDRRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified rgn

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [k32ARGBPixelFormat](https://developer.apple.com/documentation/applicationservices/k32argbpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k8IndexedGrayPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k8indexedgraypixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified rect

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [QDStdGlyphsUPP](https://developer.apple.com/documentation/applicationservices/qdstdglyphsupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDLineUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [kYUVUPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/kyuvupixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDTxMeasUPP](https://developer.apple.com/documentation/applicationservices/qdtxmeasupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified CGrafPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDOpcodeUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified GDPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified WindowRef

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRectUPP](https://developer.apple.com/documentation/applicationservices/qdrectupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k24RGBPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k24rgbpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDLineUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDPutPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorComplementUPP](https://developer.apple.com/documentation/applicationservices/colorcomplementupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PrinterStatusOpcode](https://developer.apple.com/documentation/applicationservices/printerstatusopcode)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDCommentUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [VDGammaRecord](https://developer.apple.com/documentation/kernel/vdgammarecord)

|  | Header |
| --- | --- |
| From | Video.h |
| To | Quickdraw.h |

Modified NewColorComplementUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeDragGrayRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRRectUPP](https://developer.apple.com/documentation/applicationservices/qdrrectupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified GDHandle

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified WindowPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDPutPicUPP](https://developer.apple.com/documentation/applicationservices/qdputpicupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified GWorldPtr

|  | Header |
| --- | --- |
| From | QDOffscreen.h |
| To | Quickdraw.h |

Modified #def GETPIXMAPPIXELFORMAT

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDErr](https://developer.apple.com/documentation/applicationservices/qderr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDOvalUPP](https://developer.apple.com/documentation/applicationservices/qdovalupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [DragGrayRgnUPP](https://developer.apple.com/documentation/applicationservices/draggrayrgnupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDJShieldCursorUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDTxMeasUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [Polygon](https://developer.apple.com/documentation/applicationservices/polygon)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewDragGrayRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDOvalProcPtr](https://developer.apple.com/documentation/applicationservices/qdovalprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k2vuyPixelFormat](https://developer.apple.com/documentation/applicationservices/k2vuypixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeRegionToRectsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [kVerticalConstraint](https://developer.apple.com/documentation/applicationservices/1535370-anonymous/kverticalconstraint)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeColorComplementUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [ColorSpecPtr](https://developer.apple.com/documentation/applicationservices/colorspecptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDRgnUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDBitsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k1IndexedGrayPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k1indexedgraypixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PixMap](https://developer.apple.com/documentation/applicationservices/pixmap)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDJShieldCursorProcPtr](https://developer.apple.com/documentation/applicationservices/qdjshieldcursorprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [DragGrayRgnProcPtr](https://developer.apple.com/documentation/applicationservices/draggrayrgnprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeColorSearchUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PixPatPtr](https://developer.apple.com/documentation/applicationservices/pixpatptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDStdGlyphsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified QDBeginCGContext()

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

Modified [kUYVY422PixelFormat](https://developer.apple.com/documentation/applicationservices/kuyvy422pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified PixMapHandle

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k1MonochromePixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k1monochromepixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified currentPort

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k16BE565PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k16be565pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [BitMap](https://developer.apple.com/documentation/applicationservices/bitmap)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDCommentUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRgnProcPtr](https://developer.apple.com/documentation/applicationservices/qdrgnprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDTxMeasProcPtr](https://developer.apple.com/documentation/applicationservices/qdtxmeasprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PatHandle](https://developer.apple.com/documentation/applicationservices/pathandle)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [TruncCode](https://developer.apple.com/documentation/applicationservices/trunccode)

|  | Header |
| --- | --- |
| From | QuickdrawText.h |
| To | Quickdraw.h |

Modified [k16BE555PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k16be555pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified CTabPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k16LE5551PixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k16le5551pixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDArcUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDTextUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDPolyUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [PolyHandle](https://developer.apple.com/documentation/applicationservices/polyhandle)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDCommentUPP](https://developer.apple.com/documentation/applicationservices/qdcommentupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified InvokeQDPutPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k24BGRPixelFormat](https://developer.apple.com/documentation/applicationservices/k24bgrpixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [k32RGBAPixelFormat](https://developer.apple.com/documentation/applicationservices/1535445-anonymous/k32rgbapixelformat)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified PicPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDLineProcPtr](https://developer.apple.com/documentation/applicationservices/qdlineprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified srcCopy

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [VDGamRecPtr](https://developer.apple.com/documentation/iokit/vdgamrecptr)

|  | Header |
| --- | --- |
| From | Video.h |
| To | Quickdraw.h |

Modified InvokeQDOvalUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified GrafPtr

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDArcUPP](https://developer.apple.com/documentation/applicationservices/qdarcupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDArcProcPtr](https://developer.apple.com/documentation/applicationservices/qdarcprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDStdGlyphsProcPtr](https://developer.apple.com/documentation/applicationservices/qdstdglyphsprocptr)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDRRectUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified NewQDStdGlyphsUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified DisposeQDPutPicUPP()

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDRgnUPP](https://developer.apple.com/documentation/applicationservices/qdrgnupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [OpenCPicParams](https://developer.apple.com/documentation/applicationservices/opencpicparams)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [QDJShieldCursorUPP](https://developer.apple.com/documentation/applicationservices/qdjshieldcursorupp)

|  | Header |
| --- | --- |
| From | QuickdrawTypes.h |
| To | Quickdraw.h |

Modified [RegionToRectsUPP](https://developer.apple.com/documentation/applicationservices/regiontorectsupp)

|  | Header |
| --- | --- |
| From | QuickdrawAPI.h |
| To | Quickdraw.h |

QuickdrawAPI.hRemoved AddComp()Removed AddPt()Removed AddSearch()Removed AllocCursor()Removed AngleFromSlope()Removed BackColor()Removed BackPat()Removed BackPixPat()Removed BitMapToRegion()Removed [CMEnableMatchingComment()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805227-cmenablematchingcomment)Removed [CMEndMatching()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805220-cmendmatching)Removed [CWCheckPixMap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805214-cwcheckpixmap)Removed [CWMatchPixMap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805211-cwmatchpixmap)Removed CalcCMask()Removed CalcMask()Removed ClipCGContextToRegion()Removed ClipRect()Removed CloseCursorComponent()Removed ClosePicture()Removed ClosePoly()Removed CloseRgn()Removed Color2Index()Removed ColorBit()Removed CopyBits()Removed CopyDeepMask()Removed CopyMask()Removed CopyPixMap()Removed CopyPixPat()Removed CopyRgn()Removed CreateCGContextForPort()Removed CreateNewPort()Removed CreateNewPortForCGDisplayID()Removed CursorComponentChanged()Removed CursorComponentSetData()Removed CursorInfoRemoved CustomXFerProcPtrRemoved CustomXFerRecRemoved CustomXFerRecPtrRemoved DelComp()Removed DelSearch()Removed DeltaPoint()Removed DeviceLoop()Removed DiffRgn()Removed DisposeCCursor()Removed DisposeCTable()Removed DisposeGDevice()Removed DisposePixMap()Removed DisposePixPat()Removed DisposePort()Removed DisposeRgn()Removed DrawPicture()Removed EmptyRect()Removed EmptyRgn()Removed EqualPt()Removed EqualRect()Removed EqualRgn()Removed EraseArc()Removed EraseOval()Removed ErasePoly()Removed EraseRect()Removed EraseRgn()Removed EraseRoundRect()Removed FillArc()Removed FillCArc()Removed FillCOval()Removed FillCPoly()Removed FillCRect()Removed FillCRgn()Removed FillCRoundRect()Removed FillOval()Removed FillPoly()Removed FillRect()Removed FillRgn()Removed FillRoundRect()Removed ForeColor()Removed FrameArc()Removed FrameOval()Removed FramePoly()Removed FrameRect()Removed FrameRgn()Removed FrameRoundRect()Removed GetBackColor()Removed GetCCursor()Removed GetCPixel()Removed GetCTSeed()Removed GetCTable()Removed GetClip()Removed GetCursor()Removed GetDeviceList()Removed GetForeColor()Removed GetGDevice()Removed GetIndPattern()Removed GetMainDevice()Removed GetMaskTable()Removed GetMaxDevice()Removed GetNextDevice()Removed GetPattern()Removed GetPen()Removed GetPenState()Removed GetPicture()Removed GetPixBounds()Removed GetPixDepth()Removed GetPixPat()Removed GetPixel()Removed GetPort()Removed GetPortBackColor()Removed GetPortBackPixPat()Removed GetPortBitMapForCopyBits()Removed GetPortBounds()Removed GetPortChExtra()Removed GetPortClipRegion()Removed GetPortCustomXFerProc()Removed GetPortFillPixPat()Removed GetPortForeColor()Removed GetPortFracHPenLocation()Removed GetPortGrafProcs()Removed GetPortHiliteColor()Removed GetPortOpColor()Removed GetPortPenLocation()Removed GetPortPenMode()Removed GetPortPenPixPat()Removed GetPortPenSize()Removed GetPortPenVisibility()Removed GetPortPixMap()Removed GetPortSpExtra()Removed GetPortTextFace()Removed GetPortTextFont()Removed GetPortTextMode()Removed GetPortTextSize()Removed GetPortVisibleRegion()Removed GetQDGlobalsArrow()Removed GetQDGlobalsBlack()Removed GetQDGlobalsDarkGray()Removed GetQDGlobalsGray()Removed GetQDGlobalsLightGray()Removed GetQDGlobalsRandomSeed()Removed GetQDGlobalsScreenBits()Removed GetQDGlobalsThePort()Removed GetQDGlobalsWhite()Removed GetRegionBounds()Removed GetSubTable()Removed GlobalToLocal()Removed GrafDevice()Removed HandleToRgn()Removed HideCursor()Removed HidePen()Removed HiliteColor()Removed Index2Color()Removed InitCursor()Removed InitGDevice()Removed InsetRect()Removed InsetRgn()Removed InvertArc()Removed InvertColor()Removed InvertOval()Removed InvertPoly()Removed InvertRect()Removed InvertRgn()Removed InvertRoundRect()Removed IsPortClipRegionEmpty()Removed IsPortColor()Removed IsPortOffscreen()Removed IsPortPictureBeingDefined()Removed IsPortPolyBeingDefined()Removed IsPortRegionBeingDefined()Removed IsPortVisibleRegionEmpty()Removed IsRegionRectangular()Removed IsValidPort()Removed IsValidRgnHandle()Removed KillPicture()Removed KillPoly()Removed LMGetCursorNew()Removed LMGetDeviceList()Removed LMGetFractEnable()Removed LMGetHiliteMode()Removed LMGetHiliteRGB()Removed LMGetLastFOND()Removed LMGetLastSPExtra()Removed LMGetMainDevice()Removed LMGetQDColors()Removed LMGetScrHRes()Removed LMGetScrVRes()Removed LMGetTheGDevice()Removed LMGetWidthListHand()Removed LMGetWidthPtr()Removed LMGetWidthTabHandle()Removed LMSetCursorNew()Removed LMSetDeviceList()Removed LMSetFractEnable()Removed LMSetHiliteMode()Removed LMSetHiliteRGB()Removed LMSetLastFOND()Removed LMSetLastSPExtra()Removed LMSetMainDevice()Removed LMSetQDColors()Removed LMSetScrHRes()Removed LMSetScrVRes()Removed LMSetTheGDevice()Removed LMSetWidthListHand()Removed LMSetWidthPtr()Removed LMSetWidthTabHandle()Removed Line()Removed LineTo()Removed LocalToGlobal()Removed LockPortBits()Removed #def MacCopyRgnRemoved MacCopyRgn() (no architecture available)Removed #def MacEqualRectRemoved MacEqualRect() (no architecture available)Removed MacEqualRgn() (no architecture available)Removed #def MacEqualRgnRemoved #def MacFillRectRemoved MacFillRect() (no architecture available)Removed #def MacFillRgnRemoved MacFillRgn() (no architecture available)Removed MacFrameRect() (no architecture available)Removed #def MacFrameRectRemoved MacFrameRgn() (no architecture available)Removed #def MacFrameRgnRemoved MacGetCursor() (no architecture available)Removed #def MacGetCursorRemoved #def MacGetPixelRemoved MacGetPixel() (no architecture available)Removed #def MacInsetRectRemoved MacInsetRect() (no architecture available)Removed #def MacInvertRectRemoved MacInvertRect() (no architecture available)Removed #def MacInvertRgnRemoved MacInvertRgn() (no architecture available)Removed #def MacLineToRemoved MacLineTo() (no architecture available)Removed MacOffsetRect() (no architecture available)Removed #def MacOffsetRectRemoved #def MacOffsetRgnRemoved MacOffsetRgn() (no architecture available)Removed #def MacPaintRgnRemoved MacPaintRgn() (no architecture available)Removed MacPtInRect() (no architecture available)Removed #def MacPtInRectRemoved #def MacSetCursorRemoved MacSetCursor() (no architecture available)Removed #def MacSetPortRemoved MacSetPort() (no architecture available)Removed #def MacSetRectRemoved MacSetRect() (no architecture available)Removed #def MacSetRectRgnRemoved MacSetRectRgn() (no architecture available)Removed MacShowCursor() (no architecture available)Removed #def MacShowCursorRemoved MacUnionRect() (no architecture available)Removed #def MacUnionRectRemoved MacUnionRgn() (no architecture available)Removed #def MacUnionRgnRemoved MacXorRgn() (no architecture available)Removed #def MacXorRgnRemoved MakeITable()Removed MakeRGBPat()Removed MapPoly()Removed MapPt()Removed MapRect()Removed MapRgn()Removed Move()Removed MovePortTo()Removed MoveTo()Removed [NCMBeginMatching()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805216-ncmbeginmatching)Removed [NCMDrawMatchedPicture()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805223-ncmdrawmatchedpicture)Removed [NCMUseProfileComment()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805229-ncmuseprofilecomment)Removed NewGDevice()Removed NewPixMap()Removed NewPixPat()Removed NewRgn()Removed ObscureCursor()Removed OffsetPoly()Removed OffsetRect()Removed OffsetRgn()Removed OpColor()Removed OpenCPicture()Removed OpenCursorComponent()Removed OpenPicture()Removed OpenPoly()Removed OpenRgn()Removed PackBits()Removed PaintArc()Removed PaintOval()Removed PaintPoly()Removed PaintRect()Removed PaintRgn()Removed PaintRoundRect()Removed PenMode()Removed PenNormal()Removed PenPat()Removed PenPixPat()Removed PenSize()Removed PicComment()Removed PortSize()Removed ProtectEntry()Removed Pt2Rect()Removed PtInRect()Removed PtInRgn()Removed PtToAngle()Removed QDAddRectToDirtyRegion()Removed QDAddRegionToDirtyRegion()Removed QDDisplayWaitCursor()Removed QDDisposeRegionBits()Removed QDError()Removed QDFlushPortBuffer()Removed QDGetCGDirectDisplayID()Removed QDGetCursorData()Removed QDGetCursorNameForSystemCursor()Removed QDGetCursorScale()Removed QDGetDirtyRegion()Removed QDGetPatternOrigin()Removed QDGetPictureBounds()Removed QDGlobalToLocalPoint()Removed QDGlobalToLocalRect()Removed QDGlobalToLocalRegion()Removed QDIsNamedPixMapCursorRegistered()Removed QDIsPortBufferDirty()Removed QDIsPortBuffered()Removed QDLocalToGlobalPoint()Removed QDLocalToGlobalRect()Removed QDLocalToGlobalRegion()Removed QDRegionBitsRefRemoved QDRegionToRects()Removed QDRegisterNamedPixMapCursor()Removed QDRestoreRegionBits()Removed QDSaveRegionBits()Removed QDSetCursorScale()Removed QDSetDirtyRegion()Removed QDSetNamedPixMapCursor()Removed QDSetPatternOrigin()Removed QDSwapPort()Removed QDSwapPortTextFlags()Removed QDSwapTextFlags()Removed QDUnregisterNamedPixMapCursor()Removed QDUnregisterNamedPixMapCursur()Removed QDXSystemCursorIDRemoved RGBBackColor()Removed RGBForeColor()Removed Random()Removed RealColor()Removed RectInRgn()Removed RectRgn()Removed ReserveEntry()Removed RestoreEntries()Removed RgnToHandle()Removed SaveEntries()Removed ScalePt()Removed ScreenRes()Removed ScrollRect()Removed SectRect()Removed SectRegionWithPortClipRegion()Removed SectRegionWithPortVisibleRegion()Removed SectRgn()Removed SeedCFill()Removed SeedFill()Removed SetCCursor()Removed SetCPixel()Removed SetClientID()Removed SetClip()Removed SetCursor()Removed SetCursorComponent()Removed SetDeviceAttribute()Removed SetEmptyRgn()Removed SetEntries()Removed SetGDevice()Removed SetOrigin()Removed SetPenState()Removed SetPort()Removed SetPortBackPixPat()Removed SetPortBits()Removed SetPortBounds()Removed SetPortClipRegion()Removed SetPortCustomXFerProc()Removed SetPortFillPixPat()Removed SetPortFracHPenLocation()Removed SetPortGrafProcs()Removed SetPortOpColor()Removed SetPortPenMode()Removed SetPortPenPixPat()Removed SetPortPenSize()Removed SetPortPix()Removed SetPortTextFace()Removed SetPortTextFont()Removed SetPortTextMode()Removed SetPortTextSize()Removed SetPortVisibleRegion()Removed SetPt()Removed SetQDError()Removed SetQDGlobalsArrow()Removed SetQDGlobalsRandomSeed()Removed SetRect()Removed SetRectRgn()Removed SetStdCProcs()Removed SetStdProcs()Removed ShieldCursor()Removed ShowCursor()Removed ShowPen()Removed SlopeFromAngle()Removed StdArc()Removed StdBits()Removed StdComment()Removed StdGetPic()Removed StdLine()Removed StdOpcode()Removed StdOval()Removed StdPoly()Removed StdPutPic()Removed StdRRect()Removed StdRect()Removed StdRgn()Removed StuffHex()Removed SubPt()Removed SwapPortPicSaveHandle()Removed SwapPortPolySaveHandle()Removed SwapPortRegionSaveHandle()Removed SyncCGContextOriginWithPort()Removed TestDeviceAttribute()Removed UnionRect()Removed UnionRgn()Removed UnlockPortBits()Removed UnpackBits()Removed XorRgn()Removed colorXorXFerRemoved cursorDoesAnimateRemoved cursorDoesHardwareRemoved cursorDoesUnreadableScreenBitsRemoved customXFerRemoved deltapoint()Removed kCursorComponentAnimateRemoved kCursorComponentDrawRemoved kCursorComponentEraseRemoved kCursorComponentGetInfoRemoved kCursorComponentInitRemoved kCursorComponentLastReservedRemoved kCursorComponentMoveRemoved kCursorComponentReconfigureRemoved kCursorComponentSetDataRemoved kCursorComponentSetOutputModeRemoved kCursorComponentTypeRemoved kCursorComponentsVersionRemoved kQDDontChangeFlagsRemoved kQDParseRegionFromBottomRemoved kQDParseRegionFromBottomRightRemoved kQDParseRegionFromLeftRemoved kQDParseRegionFromRightRemoved kQDParseRegionFromTopRemoved kQDParseRegionFromTopLeftRemoved kQDRegionToRectsMsgInitRemoved kQDRegionToRectsMsgParseRemoved kQDRegionToRectsMsgTerminateRemoved kQDSupportedFlagsRemoved kQDUseCGTextMetricsRemoved kQDUseCGTextRenderingRemoved kQDUseDefaultTextRenderingRemoved kQDUseTrueTypeScalerGlyphsRemoved kQDXAliasCursorRemoved kQDXArrowCursorRemoved kQDXCopyCursorRemoved kQDXIBeamCursorRemoved kQDXIBeamXORCursorRemoved kQDXMoveCursorRemoved kQDXNumberOfSystemCursorsRemoved kRenderCursorInHardwareRemoved kRenderCursorInSoftwareRemoved kXFer1PixelAtATimeRemoved kXFerConvertPixelToRGB32Removed noiseXFerQuickdrawText.hRemoved CharExtra()Removed CharToPixel()Removed CharWidth()Removed DisposeStyleRunDirectionUPP()Removed DrawChar()Removed DrawJustified()Removed DrawString()Removed DrawText()Removed FormatOrderRemoved FormatOrderPtrRemoved GetFontInfo()Removed GetFormatOrder()Removed HiliteText()Removed InvokeStyleRunDirectionUPP()Removed JustStyleCodeRemoved MacDrawText() (no architecture available)Removed #def MacDrawTextRemoved MeasureJustified()Removed MeasureText()Removed NewStyleRunDirectionUPP()Removed PixelToChar()Removed PortionLine()Removed SpaceExtra()Removed StandardGlyphs()Removed StdText()Removed StdTxMeas()Removed StringWidth()Removed StyleRunDirectionProcPtrRemoved StyleRunDirectionUPPRemoved StyledLineBreak()Removed StyledLineBreakCodeRemoved SwapQDTextFlags()Removed TextFace()Removed TextFont()Removed TextMode()Removed TextSize()Removed TextWidth()Removed TruncString()Removed TruncText()Removed VisibleLength()Removed kHiliteRemoved leftCaretRemoved leftStyleRunRemoved middleStyleRunRemoved notTruncatedRemoved onlyStyleRunRemoved rightCaretRemoved rightStyleRunRemoved smBreakCharRemoved smBreakOverflowRemoved smBreakWordRemoved smHiliteRemoved smLeftCaretRemoved smLeftStyleRunRemoved smMiddleStyleRunRemoved smNotTruncatedRemoved smOnlyStyleRunRemoved smRightCaretRemoved smRightStyleRunRemoved smTruncEndRemoved smTruncErrRemoved smTruncMiddleRemoved smTruncatedRemoved stdtext()Removed tfAntiAliasRemoved tfUnicodeRemoved truncEndRemoved truncErrRemoved truncMiddleRemoved truncatedQuickdrawTypes.hRemoved Bits16Removed CCrsrRemoved CCrsrHandleRemoved CCrsrPtrRemoved CProcHndlRemoved CProcPtrRemoved CProcRecRemoved CWindowPtrRemoved ConstPatternParamRemoved CursHandleRemoved CursPtrRemoved CursorRemoved DeviceLoopDrawingProcPtrRemoved DeviceLoopDrawingUPPRemoved DeviceLoopFlagsRemoved DisposeDeviceLoopDrawingUPP()Removed GVarHandleRemoved GVarPtrRemoved [GammaTbl](https://developer.apple.com/documentation/iokit/gammatbl)Removed GammaTblHandleRemoved [GammaTblPtr](https://developer.apple.com/documentation/kernel/gammatblptr)Removed GrafVarsRemoved ITabRemoved ITabHandleRemoved ITabPtrRemoved InvokeDeviceLoopDrawingUPP()Removed MacRegion (no architecture available)Removed MatchRecRemoved #def NON_MAC_PIXEL_FORMATSRemoved NewDeviceLoopDrawingUPP()Removed #def OLDGDEVICESTRUCTRemoved #def OLDPIXMAPSTRUCTRemoved PenStateRemoved PixelTypeRemoved PrinterFontStatusRemoved PrinterScalingStatusRemoved QDByteRemoved QDGlobals (no architecture available)Removed QDGlobalsHdl (no architecture available)Removed QDGlobalsPtr (no architecture available)Removed QDHandleRemoved QDProcsRemoved QDProcsPtrRemoved QDPtrRemoved [RGBColorHdl](https://developer.apple.com/documentation/iokit/rgbcolorhdl)Removed [RGBColorPtr](https://developer.apple.com/documentation/iokit/rgbcolorptr)Removed [RGBDirect](https://developer.apple.com/documentation/kernel/1645171-anonymous/rgbdirect)Removed Region (no architecture available)Removed ReqListRecRemoved RgnPtr (no architecture available)Removed SProcHndlRemoved SProcPtrRemoved SProcRecRemoved adMaxRemoved adMinRemoved addMaxRemoved addOverRemoved addPinRemoved allDevicesRemoved allDevicesBitRemoved allInitRemoved baseAddr32Removed blackBitRemoved blackColorRemoved blendRemoved blueBitRemoved blueColorRemoved burstDeviceRemoved chunkyRemoved chunkyPlanarRemoved [clutType](https://developer.apple.com/documentation/kernel/1645171-anonymous/cluttype)Removed condenseBitRemoved crossCursorRemoved cyanBitRemoved cyanColorRemoved defQDColorsRemoved [directType](https://developer.apple.com/documentation/kernel/1645171-anonymous/directtype)Removed ditherCopyRemoved dontMatchSeedsRemoved dontMatchSeedsBitRemoved erase (no architecture available)Removed ext32DeviceRemoved extendBitRemoved fill (no architecture available)Removed [fixedType](https://developer.apple.com/documentation/kernel/1645171-anonymous/fixedtype)Removed [frame](https://developer.apple.com/documentation/fxplug/fxrenderinfo/time) (no architecture available)Removed gdDevTypeRemoved grayishTextOrRemoved greenBitRemoved greenColorRemoved hasAuxMenuBarRemoved hiliteRemoved hiliteBitRemoved hilitetransfermodeRemoved hwMirroredDeviceRemoved iBeamCursorRemoved interlacedDeviceRemoved invalColReqRemoved inverseBitRemoved invert (no architecture available)Removed italicBitRemoved kPrinterFontStatusRemoved kPrinterScalingStatusRemoved kQDGrafVerbEraseRemoved kQDGrafVerbFillRemoved kQDGrafVerbFrameRemoved kQDGrafVerbInvertRemoved kQDGrafVerbPaintRemoved magentaBitRemoved magentaColorRemoved mainScreenRemoved noDriverRemoved normalBitRemoved notPatBicRemoved notPatCopyRemoved notPatOrRemoved notPatXorRemoved notSrcBicRemoved notSrcCopyRemoved notSrcOrRemoved notSrcXorRemoved outlineBitRemoved pHiliteBitRemoved paint (no architecture available)Removed patBicRemoved patCopyRemoved patOrRemoved patXorRemoved picLParenRemoved picRParenRemoved planarRemoved plusCursorRemoved ramInitRemoved redBitRemoved redColorRemoved roundedDeviceRemoved screenActiveRemoved screenDeviceRemoved shadowBitRemoved singleDevicesRemoved singleDevicesBitRemoved srcBicRemoved srcOrRemoved srcXorRemoved subOverRemoved subPinRemoved sysPatListIDRemoved transparentRemoved ulineBitRemoved watchCursorRemoved whiteColorRemoved xCSpecArrayRemoved xColorSpecRemoved xColorSpecPtrRemoved yellowBitRemoved yellowColorSFNTLayoutTypes.hAdded KerxArrayOffsetAdded KerxControlPointActionAdded KerxControlPointEntryAdded KerxControlPointHeaderAdded KerxCoordinateActionAdded KerxFormatSpecificHeaderAdded KerxIndexArrayHeaderAdded KerxKerningPairAdded KerxOffsetTableAdded KerxOffsetTablePtrAdded KerxOrderedListEntryAdded KerxOrderedListEntryPtrAdded KerxOrderedListHeaderAdded KerxSimpleArrayHeaderAdded KerxStateEntryAdded KerxStateHeaderAdded KerxSubtableCoverageAdded KerxSubtableHeaderAdded KerxSubtableHeaderPtrAdded KerxTableHeaderAdded KerxTableHeaderHandleAdded KerxTableHeaderPtrAdded kKERXActionOffsetMaskAdded kKERXControlPointAdded kKERXCrossStreamAdded kKERXCrossStreamResetNoteAdded kKERXCurrentVersionAdded kKERXFormatMaskAdded kKERXIndexArrayAdded kKERXLineEndKerningAdded kKERXLineStartAdded kKERXNoCrossKerningAdded kKERXNoStakeNoteAdded kKERXNotAppliedAdded kKERXNotesRequestedAdded kKERXOrderedListAdded kKERXResetCrossStreamAdded kKERXSimpleArrayAdded kKERXStateTableAdded kKERXTagAdded kKERXUnusedBitsAdded kKERXUsesCoordinatesAdded kKERXVariationAdded kKERXVerticalSpeechSynthesis.hRemoved SpeechBoundaryRemoved kSpeechImmediateBoundaryRemoved kSpeechSentenceBoundaryRemoved kSpeechWordBoundaryAdded [kSpeechAudioGraphProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiographproperty)Added [kSpeechAudioUnitProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiounitproperty)Added [kSpeechModeTune](https://developer.apple.com/documentation/applicationservices/kspeechmodetune)Added [modeTune](https://developer.apple.com/documentation/applicationservices/modetune)Video.hRemoved [AVIDType](https://developer.apple.com/documentation/kernel/avidtype)Removed [DepthMode](https://developer.apple.com/documentation/iokit/depthmode)Removed [DisplayIDType](https://developer.apple.com/documentation/iokit/displayidtype)Removed [DisplayModeID](https://developer.apple.com/documentation/iokit/displaymodeid)Removed [ExtendedSenseCode](https://developer.apple.com/documentation/iokit/extendedsensecode)Removed [GammaTableID](https://developer.apple.com/documentation/kernel/gammatableid)Removed [RawSenseCode](https://developer.apple.com/documentation/kernel/rawsensecode)Removed VDBaseAddressInfoPtrRemoved VDBaseAddressInfoRecRemoved [VDClutBehavior](https://developer.apple.com/documentation/iokit/vdclutbehavior)Removed [VDClutBehaviorPtr](https://developer.apple.com/documentation/kernel/vdclutbehaviorptr)Removed [VDCommunicationInfoPtr](https://developer.apple.com/documentation/iokit/vdcommunicationinfoptr)Removed [VDCommunicationInfoRec](https://developer.apple.com/documentation/kernel/vdcommunicationinforec)Removed [VDCommunicationPtr](https://developer.apple.com/documentation/kernel/vdcommunicationptr)Removed [VDCommunicationRec](https://developer.apple.com/documentation/iokit/vdcommunicationrec)Removed [VDConvolutionInfoPtr](https://developer.apple.com/documentation/iokit/vdconvolutioninfoptr)Removed [VDConvolutionInfoRec](https://developer.apple.com/documentation/kernel/vdconvolutioninforec)Removed [VDDDCBlockPtr](https://developer.apple.com/documentation/kernel/vdddcblockptr)Removed [VDDDCBlockRec](https://developer.apple.com/documentation/iokit/vdddcblockrec)Removed [VDDefMode](https://developer.apple.com/documentation/iokit/vddefmode)Removed [VDDefModePtr](https://developer.apple.com/documentation/kernel/vddefmodeptr)Removed [VDDetailedTimingPtr](https://developer.apple.com/documentation/iokit/vddetailedtimingptr)Removed [VDDetailedTimingRec](https://developer.apple.com/documentation/kernel/vddetailedtimingrec)Removed [VDDisplayConnectInfoPtr](https://developer.apple.com/documentation/kernel/vddisplayconnectinfoptr)Removed [VDDisplayConnectInfoRec](https://developer.apple.com/documentation/kernel/vddisplayconnectinforec)Removed [VDDisplayTimingRangePtr](https://developer.apple.com/documentation/iokit/vddisplaytimingrangeptr)Removed [VDDisplayTimingRangeRec](https://developer.apple.com/documentation/kernel/vddisplaytimingrangerec)Removed [VDDrawHardwareCursorPtr](https://developer.apple.com/documentation/iokit/vddrawhardwarecursorptr)Removed [VDDrawHardwareCursorRec](https://developer.apple.com/documentation/kernel/vddrawhardwarecursorrec)Removed [VDEntRecPtr](https://developer.apple.com/documentation/kernel/vdentrecptr)Removed [VDEntryRecord](https://developer.apple.com/documentation/iokit/vdentryrecord)Removed [VDFlagRecPtr](https://developer.apple.com/documentation/iokit/vdflagrecptr)Removed [VDFlagRecord](https://developer.apple.com/documentation/iokit/vdflagrecord)Removed [VDGammaInfoPtr](https://developer.apple.com/documentation/kernel/vdgammainfoptr)Removed [VDGammaInfoRec](https://developer.apple.com/documentation/iokit/vdgammainforec)Removed [VDGetGammaListPtr](https://developer.apple.com/documentation/iokit/vdgetgammalistptr)Removed [VDGetGammaListRec](https://developer.apple.com/documentation/kernel/vdgetgammalistrec)Removed [VDGrayPtr](https://developer.apple.com/documentation/kernel/vdgrayptr)Removed [VDGrayRecord](https://developer.apple.com/documentation/iokit/vdgrayrecord)Removed [VDHardwareCursorDrawStatePtr](https://developer.apple.com/documentation/iokit/vdhardwarecursordrawstateptr)Removed [VDHardwareCursorDrawStateRec](https://developer.apple.com/documentation/kernel/vdhardwarecursordrawstaterec)Removed [VDMultiConnectInfoPtr](https://developer.apple.com/documentation/iokit/vdmulticonnectinfoptr)Removed [VDMultiConnectInfoRec](https://developer.apple.com/documentation/kernel/vdmulticonnectinforec)Removed [VDPageInfo](https://developer.apple.com/documentation/kernel/vdpageinfo)Removed [VDPgInfoPtr](https://developer.apple.com/documentation/kernel/vdpginfoptr)Removed [VDPowerStatePtr](https://developer.apple.com/documentation/kernel/vdpowerstateptr)Removed [VDPowerStateRec](https://developer.apple.com/documentation/kernel/vdpowerstaterec)Removed [VDPrivateSelectorDataRec](https://developer.apple.com/documentation/kernel/vdprivateselectordatarec)Removed [VDPrivateSelectorRec](https://developer.apple.com/documentation/iokit/vdprivateselectorrec)Removed [VDResolutionInfoPtr](https://developer.apple.com/documentation/kernel/vdresolutioninfoptr)Removed [VDResolutionInfoRec](https://developer.apple.com/documentation/iokit/vdresolutioninforec)Removed [VDRetrieveGammaPtr](https://developer.apple.com/documentation/kernel/vdretrievegammaptr)Removed [VDRetrieveGammaRec](https://developer.apple.com/documentation/iokit/vdretrievegammarec)Removed [VDSetEntryPtr](https://developer.apple.com/documentation/iokit/vdsetentryptr)Removed [VDSetEntryRecord](https://developer.apple.com/documentation/iokit/vdsetentryrecord)Removed [VDSetHardwareCursorPtr](https://developer.apple.com/documentation/iokit/vdsethardwarecursorptr)Removed [VDSetHardwareCursorRec](https://developer.apple.com/documentation/kernel/vdsethardwarecursorrec)Removed [VDSettings](https://developer.apple.com/documentation/kernel/vdsettings)Removed [VDSettingsPtr](https://developer.apple.com/documentation/kernel/vdsettingsptr)Removed [VDSizeInfo](https://developer.apple.com/documentation/kernel/vdsizeinfo)Removed [VDSupportsHardwareCursorPtr](https://developer.apple.com/documentation/kernel/vdsupportshardwarecursorptr)Removed [VDSupportsHardwareCursorRec](https://developer.apple.com/documentation/iokit/vdsupportshardwarecursorrec)Removed [VDSwitchInfoPtr](https://developer.apple.com/documentation/kernel/vdswitchinfoptr)Removed [VDSwitchInfoRec](https://developer.apple.com/documentation/kernel/vdswitchinforec)Removed [VDSyncInfoPtr](https://developer.apple.com/documentation/iokit/vdsyncinfoptr)Removed [VDSyncInfoRec](https://developer.apple.com/documentation/kernel/vdsyncinforec)Removed [VDSzInfoPtr](https://developer.apple.com/documentation/iokit/vdszinfoptr)Removed [VDTimingInfoPtr](https://developer.apple.com/documentation/kernel/vdtiminginfoptr)Removed [VDTimingInfoRec](https://developer.apple.com/documentation/kernel/vdtiminginforec)Removed [VDVideoParametersInfoPtr](https://developer.apple.com/documentation/iokit/vdvideoparametersinfoptr)Removed [VDVideoParametersInfoRec](https://developer.apple.com/documentation/iokit/vdvideoparametersinforec)Removed [VPBlock](https://developer.apple.com/documentation/kernel/vpblock)Removed [VPBlockPtr](https://developer.apple.com/documentation/kernel/vpblockptr)Removed [VideoDeviceType](https://developer.apple.com/documentation/iokit/videodevicetype)Removed [cscDirectSetEntries](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscdirectsetentries)Removed [cscDoCommunication](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscdocommunication)Removed [cscDrawHardwareCursor](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscdrawhardwarecursor)Removed [cscGetBaseAddr](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetbaseaddr)Removed [cscGetClutBehavior](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetclutbehavior)Removed [cscGetCommunicationInfo](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetcommunicationinfo)Removed [cscGetConnection](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetconnection)Removed [cscGetConvolution](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetconvolution)Removed [cscGetCurMode](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetcurmode)Removed [cscGetDDCBlock](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetddcblock)Removed [cscGetDefaultMode](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetdefaultmode)Removed [cscGetDetailedTiming](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetdetailedtiming)Removed [cscGetEntries](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetentries)Removed [cscGetGamma](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetgamma)Removed [cscGetGammaInfoList](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetgammainfolist)Removed [cscGetGray](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetgray)Removed [cscGetHardwareCursorDrawState](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgethardwarecursordrawstate)Removed [cscGetInterrupt](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetinterrupt)Removed [cscGetMode](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetmode)Removed [cscGetModeBaseAddress](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetmodebaseaddress)Removed [cscGetModeTiming](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetmodetiming)Removed [cscGetMultiConnect](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetmulticonnect)Removed [cscGetNextResolution](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetnextresolution)Removed [cscGetPageBase](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetpagebase)Removed [cscGetPageCnt](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetpagecnt)Removed [cscGetPages](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetpages)Removed [cscGetPowerState](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetpowerstate)Removed [cscGetPreferredConfiguration](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetpreferredconfiguration)Removed [cscGetScanProc](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscgetscanproc)Removed [cscGetSync](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetsync)Removed [cscGetTimingRanges](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgettimingranges)Removed [cscGetVideoParameters](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscgetvideoparameters)Removed [cscGrayPage](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscgraypage)Removed [cscGrayScreen](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscgrayscreen)Removed [cscKillIO](https://developer.apple.com/documentation/iokit/1568097-anonymous/csckillio)Removed [cscPrivateControlCall](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscprivatecontrolcall)Removed [cscPrivateStatusCall](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscprivatestatuscall)Removed [cscProbeConnection](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscprobeconnection)Removed [cscReset](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscreset)Removed [cscRetrieveGammaTable](https://developer.apple.com/documentation/kernel/1644537-anonymous/cscretrievegammatable)Removed [cscSavePreferredConfiguration](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscsavepreferredconfiguration)Removed [cscSetClutBehavior](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetclutbehavior)Removed [cscSetConvolution](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetconvolution)Removed [cscSetDefaultMode](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscsetdefaultmode)Removed [cscSetDetailedTiming](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetdetailedtiming)Removed [cscSetEntries](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetentries)Removed [cscSetGamma](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscsetgamma)Removed [cscSetGray](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetgray)Removed [cscSetHardwareCursor](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsethardwarecursor)Removed [cscSetInterrupt](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetinterrupt)Removed [cscSetMode](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetmode)Removed [cscSetMultiConnect](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetmulticonnect)Removed [cscSetPowerState](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetpowerstate)Removed [cscSetSync](https://developer.apple.com/documentation/kernel/1644563-anonymous/cscsetsync)Removed [cscSupportsHardwareCursor](https://developer.apple.com/documentation/iokit/1568085-anonymous/cscsupportshardwarecursor)Removed [cscSwitchMode](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscswitchmode)Removed [cscUnusedCall](https://developer.apple.com/documentation/iokit/1568097-anonymous/cscunusedcall)Removed [eightBitMode](https://developer.apple.com/documentation/kernel/1644560-anonymous/eightbitmode)Removed [fifthVidMode](https://developer.apple.com/documentation/iokit/1567898-anonymous/fifthvidmode)Removed [firstVidMode](https://developer.apple.com/documentation/iokit/1567898-anonymous/firstvidmode)Removed [fourBitMode](https://developer.apple.com/documentation/kernel/1644560-anonymous/fourbitmode)Removed [fourthVidMode](https://developer.apple.com/documentation/kernel/1644540-anonymous/fourthvidmode)Removed [kAVPowerOff](https://developer.apple.com/documentation/kernel/1644557-anonymous/kavpoweroff)Removed [kAVPowerOn](https://developer.apple.com/documentation/kernel/1644557-anonymous/kavpoweron)Removed [kAVPowerStandby](https://developer.apple.com/documentation/iokit/1567488-anonymous/kavpowerstandby)Removed [kAVPowerSuspend](https://developer.apple.com/documentation/iokit/1567488-anonymous/kavpowersuspend)Removed [kActivateConnection](https://developer.apple.com/documentation/kernel/1644581-anonymous/kactivateconnection)Removed [kAllModesSafe](https://developer.apple.com/documentation/kernel/1644573-anonymous/kallmodessafe)Removed [kAllModesValid](https://developer.apple.com/documentation/kernel/1644573-anonymous/kallmodesvalid)Removed [kAnalogSetupExpectedBit](https://developer.apple.com/documentation/kernel/1644564-anonymous/kanalogsetupexpectedbit)Removed [kAnalogSetupExpectedMask](https://developer.apple.com/documentation/kernel/1644564-anonymous/kanalogsetupexpectedmask)Removed [kAnalogSignalLevel_0700_0000](https://developer.apple.com/documentation/iokit/1567512-anonymous/kanalogsignallevel_0700_0000)Removed [kAnalogSignalLevel_0700_0300](https://developer.apple.com/documentation/kernel/1644559-anonymous/kanalogsignallevel_0700_0300)Removed [kAnalogSignalLevel_0714_0286](https://developer.apple.com/documentation/kernel/1644559-anonymous/kanalogsignallevel_0714_0286)Removed [kAnalogSignalLevel_1000_0400](https://developer.apple.com/documentation/iokit/1567512-anonymous/kanalogsignallevel_1000_0400)Removed [kBuiltInConnection](https://developer.apple.com/documentation/iokit/1567936-anonymous/kbuiltinconnection)Removed [kColor16Connect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kcolor16connect)Removed [kColor19Connect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kcolor19connect)Removed [kColorTwoPageConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kcolortwopageconnect)Removed [kCompositeSyncMask](https://developer.apple.com/documentation/kernel/1644576-anonymous/kcompositesyncmask)Removed [kConnectionInactive](https://developer.apple.com/documentation/iokit/1567936-anonymous/kconnectioninactive)Removed [kConvolved](https://developer.apple.com/documentation/kernel/1644549-anonymous/kconvolved)Removed [kConvolvedMask](https://developer.apple.com/documentation/kernel/1644549-anonymous/kconvolvedmask)Removed [kDDCBlockSize](https://developer.apple.com/documentation/kernel/1644556-anonymous/kddcblocksize)Removed [kDDCBlockTypeEDID](https://developer.apple.com/documentation/iokit/1567252-anonymous/kddcblocktypeedid)Removed [kDDCConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kddcconnect)Removed [kDDCForceReadBit](https://developer.apple.com/documentation/iokit/1567708-anonymous/kddcforcereadbit)Removed [kDDCForceReadMask](https://developer.apple.com/documentation/iokit/1567708-anonymous/kddcforcereadmask)Removed [kDMSModeFree](https://developer.apple.com/documentation/kernel/1644542-anonymous/kdmsmodefree)Removed [kDMSModeNotReady](https://developer.apple.com/documentation/kernel/1644542-anonymous/kdmsmodenotready)Removed [kDMSModeReady](https://developer.apple.com/documentation/kernel/1644542-anonymous/kdmsmodeready)Removed [kDPMSSyncMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/kdpmssyncmask)Removed [kDPMSSyncOff](https://developer.apple.com/documentation/iokit/1567596-anonymous/kdpmssyncoff)Removed [kDPMSSyncOn](https://developer.apple.com/documentation/kernel/1644545-anonymous/kdpmssyncon)Removed [kDPMSSyncStandby](https://developer.apple.com/documentation/iokit/1567596-anonymous/kdpmssyncstandby)Removed [kDPMSSyncSuspend](https://developer.apple.com/documentation/iokit/1567596-anonymous/kdpmssyncsuspend)Removed [kDeactivateConnection](https://developer.apple.com/documentation/kernel/1644581-anonymous/kdeactivateconnection)Removed [kDeclROMtables](https://developer.apple.com/documentation/iokit/1568080-anonymous/kdeclromtables)Removed [kDependentConnection](https://developer.apple.com/documentation/iokit/1567936-anonymous/kdependentconnection)Removed [kDepthDependent](https://developer.apple.com/documentation/iokit/1567225-anonymous/kdepthdependent)Removed [kDepthMode1](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode1)Removed [kDepthMode2](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode2)Removed [kDepthMode3](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode3)Removed [kDepthMode4](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode4)Removed [kDepthMode5](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode5)Removed [kDepthMode6](https://developer.apple.com/documentation/kernel/1644574-anonymous/kdepthmode6)Removed [kDetailedTimingFormat](https://developer.apple.com/documentation/kernel/1644577-anonymous/kdetailedtimingformat)Removed [kDigitalSignalBit](https://developer.apple.com/documentation/kernel/1644564-anonymous/kdigitalsignalbit)Removed [kDigitalSignalMask](https://developer.apple.com/documentation/iokit/1567687-anonymous/kdigitalsignalmask)Removed [kDisableCompositeSyncBit](https://developer.apple.com/documentation/iokit/1567952-anonymous/kdisablecompositesyncbit)Removed [kDisableHorizontalSyncBit](https://developer.apple.com/documentation/iokit/1567952-anonymous/kdisablehorizontalsyncbit)Removed [kDisableVerticalSyncBit](https://developer.apple.com/documentation/kernel/1644576-anonymous/kdisableverticalsyncbit)Removed [kDisplayModeIDBootProgrammable](https://developer.apple.com/documentation/kernel/1644568-anonymous/kdisplaymodeidbootprogrammable)Removed [kDisplayModeIDCurrent](https://developer.apple.com/documentation/kernel/1644568-anonymous/kdisplaymodeidcurrent)Removed [kDisplayModeIDFindFirstProgrammable](https://developer.apple.com/documentation/kernel/1644568-anonymous/kdisplaymodeidfindfirstprogrammable)Removed [kDisplayModeIDFindFirstResolution](https://developer.apple.com/documentation/iokit/1567926-anonymous/kdisplaymodeidfindfirstresolution)Removed [kDisplayModeIDInvalid](https://developer.apple.com/documentation/kernel/1644568-anonymous/kdisplaymodeidinvalid)Removed [kDisplayModeIDNoMoreResolutions](https://developer.apple.com/documentation/kernel/1644568-anonymous/kdisplaymodeidnomoreresolutions)Removed [kDisplayModeIDReservedBase](https://developer.apple.com/documentation/iokit/1567926-anonymous/kdisplaymodeidreservedbase)Removed [kESCFivePortrait](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescfiveportrait)Removed [kESCFourNTSC](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescfourntsc)Removed [kESCOnePortraitMono](https://developer.apple.com/documentation/iokit/1567836-anonymous/kesconeportraitmono)Removed [kESCSeven16Inch](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescseven16inch)Removed [kESCSeven19Inch](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescseven19inch)Removed [kESCSevenDDC](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescsevenddc)Removed [kESCSevenNTSC](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsevenntsc)Removed [kESCSevenNoDisplay](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescsevennodisplay)Removed [kESCSevenPAL](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsevenpal)Removed [kESCSevenPALAlternate](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsevenpalalternate)Removed [kESCSevenVGA](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescsevenvga)Removed [kESCSixMSB1](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsixmsb1)Removed [kESCSixMSB2](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsixmsb2)Removed [kESCSixMSB3](https://developer.apple.com/documentation/iokit/1567836-anonymous/kescsixmsb3)Removed [kESCSixStandard](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescsixstandard)Removed [kESCThree21InchMono](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescthree21inchmono)Removed [kESCThree21InchMonoRadius](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescthree21inchmonoradius)Removed [kESCThree21InchRadius](https://developer.apple.com/documentation/kernel/1644551-anonymous/kescthree21inchradius)Removed [kESCTwo12Inch](https://developer.apple.com/documentation/kernel/1644551-anonymous/kesctwo12inch)Removed [kESCZero21Inch](https://developer.apple.com/documentation/kernel/1644551-anonymous/kesczero21inch)Removed [kEnableSyncOnBlue](https://developer.apple.com/documentation/kernel/1644576-anonymous/kenablesynconblue)Removed [kEnableSyncOnGreen](https://developer.apple.com/documentation/iokit/1567952-anonymous/kenablesyncongreen)Removed [kEnableSyncOnRed](https://developer.apple.com/documentation/kernel/1644576-anonymous/kenablesynconred)Removed [kFastCheckForDDC](https://developer.apple.com/documentation/iokit/1567936-anonymous/kfastcheckforddc)Removed [kFifthDepthMode](https://developer.apple.com/documentation/kernel/1644532-anonymous/kfifthdepthmode)Removed [kFirstDepthMode](https://developer.apple.com/documentation/kernel/1644532-anonymous/kfirstdepthmode)Removed [kFixedModeCRTConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kfixedmodecrtconnect)Removed [kFourthDepthMode](https://developer.apple.com/documentation/kernel/1644532-anonymous/kfourthdepthmode)Removed [kFullPageConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kfullpageconnect)Removed [kGammaTableIDFindFirst](https://developer.apple.com/documentation/kernel/1644541-anonymous/kgammatableidfindfirst)Removed [kGammaTableIDNoMoreTables](https://developer.apple.com/documentation/kernel/1644541-anonymous/kgammatableidnomoretables)Removed [kGammaTableIDSpecific](https://developer.apple.com/documentation/iokit/1567918-anonymous/kgammatableidspecific)Removed [kGenericCRT](https://developer.apple.com/documentation/iokit/1568011-anonymous/kgenericcrt)Removed [kGenericLCD](https://developer.apple.com/documentation/iokit/1568011-anonymous/kgenericlcd)Removed [kGetConnectionCount](https://developer.apple.com/documentation/iokit/1567585-anonymous/kgetconnectioncount)Removed [kHRConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/khrconnect)Removed [kHardwareSleep](https://developer.apple.com/documentation/kernel/1644557-anonymous/khardwaresleep)Removed [kHardwareWake](https://developer.apple.com/documentation/iokit/1567488-anonymous/khardwarewake)Removed [kHardwareWakeFromSuspend](https://developer.apple.com/documentation/iokit/1567488-anonymous/khardwarewakefromsuspend)Removed [kHardwareWakeToDoze](https://developer.apple.com/documentation/iokit/1567488-anonymous/khardwarewaketodoze)Removed [kHardwareWakeToDozeFromSuspend](https://developer.apple.com/documentation/kernel/1644557-anonymous/khardwarewaketodozefromsuspend)Removed [kHasDDCConnection](https://developer.apple.com/documentation/kernel/1644573-anonymous/khasddcconnection)Removed [kHasDirectConnection](https://developer.apple.com/documentation/kernel/1644573-anonymous/khasdirectconnection)Removed [kHorizontalSyncMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/khorizontalsyncmask)Removed [kIsMonoDev](https://developer.apple.com/documentation/iokit/1567936-anonymous/kismonodev)Removed [kLiveVideoPassThru](https://developer.apple.com/documentation/kernel/1644549-anonymous/klivevideopassthru)Removed [kLiveVideoPassThruMask](https://developer.apple.com/documentation/iokit/1568057-anonymous/klivevideopassthrumask)Removed [kModeBuiltIn](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodebuiltin)Removed [kModeDefault](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodedefault)Removed [kModeInterlaced](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodeinterlaced)Removed [kModeNotPreset](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodenotpreset)Removed [kModeNotResize](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodenotresize)Removed [kModeRequiresPan](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmoderequirespan)Removed [kModeSafe](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodesafe)Removed [kModeShowNever](https://developer.apple.com/documentation/kernel/1644539-anonymous/kmodeshownever)Removed [kModeShowNow](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodeshownow)Removed [kModeSimulscan](https://developer.apple.com/documentation/kernel/1644539-anonymous/kmodesimulscan)Removed [kModeStretched](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodestretched)Removed [kModeValid](https://developer.apple.com/documentation/iokit/1567315-anonymous/kmodevalid)Removed [kModelessConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kmodelessconnect)Removed [kMonoTwoPageConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kmonotwopageconnect)Removed [kMultiModeCRT1Connect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kmultimodecrt1connect)Removed [kMultiModeCRT2Connect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kmultimodecrt2connect)Removed [kMultiModeCRT3Connect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kmultimodecrt3connect)Removed [kMultiModeCRT4Connect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kmultimodecrt4connect)Removed [kNTSCConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kntscconnect)Removed [kNoConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/knoconnect)Removed [kNoSeparateSyncControlBit](https://developer.apple.com/documentation/iokit/1567952-anonymous/knoseparatesynccontrolbit)Removed [kOverrideConnection](https://developer.apple.com/documentation/iokit/1567936-anonymous/koverrideconnection)Removed [kPALConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kpalconnect)Removed [kPanelConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kpanelconnect)Removed [kPanelFSTNConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kpanelfstnconnect)Removed [kPanelTFTConnect](https://developer.apple.com/documentation/kernel/1644536-anonymous/kpaneltftconnect)Removed [kPowerStateNeedsRefresh](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstateneedsrefresh)Removed [kPowerStateNeedsRefreshMask](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstateneedsrefreshmask)Removed [kPowerStateSleepAwareBit](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepawarebit)Removed [kPowerStateSleepAwareMask](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepawaremask)Removed [kPowerStateSleepCanPowerOffBit](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepcanpoweroffbit)Removed [kPowerStateSleepCanPowerOffMask](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepcanpoweroffmask)Removed [kPowerStateSleepForbiddenBit](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepforbiddenbit)Removed [kPowerStateSleepForbiddenMask](https://developer.apple.com/documentation/kernel/1644575-anonymous/kpowerstatesleepforbiddenmask)Removed [kPowerStateSleepNoDPMSBit](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepnodpmsbit)Removed [kPowerStateSleepNoDPMSMask](https://developer.apple.com/documentation/iokit/1567457-anonymous/kpowerstatesleepnodpmsmask)Removed [kPowerStateSleepWaketoDozeBit](https://developer.apple.com/documentation/kernel/1644575-anonymous/kpowerstatesleepwaketodozebit)Removed [kPowerStateSleepWaketoDozeMask](https://developer.apple.com/documentation/kernel/1644575-anonymous/kpowerstatesleepwaketodozemask)Removed [kRSCFive](https://developer.apple.com/documentation/iokit/1567872-anonymous/krscfive)Removed [kRSCFour](https://developer.apple.com/documentation/kernel/1644565-anonymous/krscfour)Removed [kRSCOne](https://developer.apple.com/documentation/kernel/1644565-anonymous/krscone)Removed [kRSCSeven](https://developer.apple.com/documentation/kernel/1644565-anonymous/krscseven)Removed [kRSCSix](https://developer.apple.com/documentation/kernel/1644565-anonymous/krscsix)Removed [kRSCThree](https://developer.apple.com/documentation/kernel/1644565-anonymous/krscthree)Removed [kRSCTwo](https://developer.apple.com/documentation/iokit/1567872-anonymous/krsctwo)Removed [kRSCZero](https://developer.apple.com/documentation/iokit/1567872-anonymous/krsczero)Removed [kRangeSupportsCompositeSyncBit](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportscompositesyncbit)Removed [kRangeSupportsCompositeSyncMask](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportscompositesyncmask)Removed [kRangeSupportsSeperateSyncsBit](https://developer.apple.com/documentation/kernel/1644567-anonymous/krangesupportsseperatesyncsbit)Removed [kRangeSupportsSeperateSyncsMask](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportsseperatesyncsmask)Removed [kRangeSupportsSignal_0700_0000_Bit](https://developer.apple.com/documentation/kernel/1644582-anonymous/krangesupportssignal_0700_0000_bit)Removed [kRangeSupportsSignal_0700_0000_Mask](https://developer.apple.com/documentation/iokit/1568064-anonymous/krangesupportssignal_0700_0000_mask)Removed [kRangeSupportsSignal_0700_0300_Bit](https://developer.apple.com/documentation/kernel/1644582-anonymous/krangesupportssignal_0700_0300_bit)Removed [kRangeSupportsSignal_0700_0300_Mask](https://developer.apple.com/documentation/kernel/1644582-anonymous/krangesupportssignal_0700_0300_mask)Removed [kRangeSupportsSignal_0714_0286_Bit](https://developer.apple.com/documentation/kernel/1644582-anonymous/krangesupportssignal_0714_0286_bit)Removed [kRangeSupportsSignal_0714_0286_Mask](https://developer.apple.com/documentation/iokit/1568064-anonymous/krangesupportssignal_0714_0286_mask)Removed [kRangeSupportsSignal_1000_0400_Bit](https://developer.apple.com/documentation/iokit/1568064-anonymous/krangesupportssignal_1000_0400_bit)Removed [kRangeSupportsSignal_1000_0400_Mask](https://developer.apple.com/documentation/iokit/1568064-anonymous/krangesupportssignal_1000_0400_mask)Removed [kRangeSupportsSyncOnGreenBit](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportssyncongreenbit)Removed [kRangeSupportsSyncOnGreenMask](https://developer.apple.com/documentation/kernel/1644567-anonymous/krangesupportssyncongreenmask)Removed [kRangeSupportsVSyncSerrationBit](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportsvsyncserrationbit)Removed [kRangeSupportsVSyncSerrationMask](https://developer.apple.com/documentation/iokit/1567343-anonymous/krangesupportsvsyncserrationmask)Removed [kReportsDDCConnection](https://developer.apple.com/documentation/kernel/1644573-anonymous/kreportsddcconnection)Removed [kReportsHotPlugging](https://developer.apple.com/documentation/iokit/1567936-anonymous/kreportshotplugging)Removed [kReportsTagging](https://developer.apple.com/documentation/kernel/1644573-anonymous/kreportstagging)Removed [kResolutionHasMultipleDepthSizes](https://developer.apple.com/documentation/kernel/1644569-anonymous/kresolutionhasmultipledepthsizes)Removed [kSecondDepthMode](https://developer.apple.com/documentation/kernel/1644532-anonymous/kseconddepthmode)Removed [kSetClutAtSetEntries](https://developer.apple.com/documentation/iokit/1567506-anonymous/ksetclutatsetentries)Removed [kSetClutAtVBL](https://developer.apple.com/documentation/iokit/1567506-anonymous/ksetclutatvbl)Removed [kSixthDepthMode](https://developer.apple.com/documentation/kernel/1644532-anonymous/ksixthdepthmode)Removed [kSyncAnalogBipolarMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogbipolarmask)Removed [kSyncAnalogBipolarSRGBSyncMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogbipolarsrgbsyncmask)Removed [kSyncAnalogBipolarSerrateMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogbipolarserratemask)Removed [kSyncAnalogCompositeMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogcompositemask)Removed [kSyncAnalogCompositeRGBSyncMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogcompositergbsyncmask)Removed [kSyncAnalogCompositeSerrateMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncanalogcompositeserratemask)Removed [kSyncDigitalCompositeMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncdigitalcompositemask)Removed [kSyncDigitalCompositeMatchHSyncMask](https://developer.apple.com/documentation/iokit/1567939-anonymous/ksyncdigitalcompositematchhsyncmask)Removed [kSyncDigitalCompositeSerrateMask](https://developer.apple.com/documentation/iokit/1567939-anonymous/ksyncdigitalcompositeserratemask)Removed [kSyncDigitalHSyncPositiveMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncdigitalhsyncpositivemask)Removed [kSyncDigitalSeperateMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncdigitalseperatemask)Removed [kSyncDigitalVSyncPositiveMask](https://developer.apple.com/documentation/iokit/1567939-anonymous/ksyncdigitalvsyncpositivemask)Removed [kSyncInterlaceMask](https://developer.apple.com/documentation/kernel/1644531-anonymous/ksyncinterlacemask)Removed [kSyncOnBlueMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/ksynconbluemask)Removed [kSyncOnGreenMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/ksyncongreenmask)Removed [kSyncOnMask](https://developer.apple.com/documentation/kernel/1644576-anonymous/ksynconmask)Removed [kSyncOnRedMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/ksynconredmask)Removed [kSyncPositivePolarityBit](https://developer.apple.com/documentation/iokit/1568016-anonymous/ksyncpositivepolaritybit)Removed [kSyncPositivePolarityMask](https://developer.apple.com/documentation/iokit/1568016-anonymous/ksyncpositivepolaritymask)Removed [kTaggingInfoNonStandard](https://developer.apple.com/documentation/kernel/1644573-anonymous/ktagginginfononstandard)Removed [kThirdDepthMode](https://developer.apple.com/documentation/iokit/1567646-anonymous/kthirddepthmode)Removed [kTimingChangeRestrictedErr](https://developer.apple.com/documentation/iokit/1567789-anonymous/ktimingchangerestrictederr)Removed [kTriStateSyncBit](https://developer.apple.com/documentation/iokit/1567952-anonymous/ktristatesyncbit)Removed [kTriStateSyncMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/ktristatesyncmask)Removed [kUncertainConnection](https://developer.apple.com/documentation/iokit/1567936-anonymous/kuncertainconnection)Removed [kUnknownConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kunknownconnect)Removed [kVGAConnect](https://developer.apple.com/documentation/iokit/1568011-anonymous/kvgaconnect)Removed [kVerticalSyncMask](https://developer.apple.com/documentation/iokit/1567952-anonymous/kverticalsyncmask)Removed [kVideoBufferSizeErr](https://developer.apple.com/documentation/kernel/1644554-anonymous/kvideobuffersizeerr)Removed [kVideoBusTypeI2C](https://developer.apple.com/documentation/kernel/1644552-anonymous/kvideobustypei2c)Removed [kVideoBusTypeInvalid](https://developer.apple.com/documentation/kernel/1644552-anonymous/kvideobustypeinvalid)Removed [kVideoDDCciReplyType](https://developer.apple.com/documentation/iokit/1567416-anonymous/kvideoddccireplytype)Removed [kVideoDefaultBus](https://developer.apple.com/documentation/iokit/1568079-anonymous/kvideodefaultbus)Removed [kVideoI2CBusyErr](https://developer.apple.com/documentation/kernel/1644554-anonymous/kvideoi2cbusyerr)Removed [kVideoI2CReplyPendingErr](https://developer.apple.com/documentation/iokit/1567789-anonymous/kvideoi2creplypendingerr)Removed [kVideoI2CTransactionErr](https://developer.apple.com/documentation/kernel/1644554-anonymous/kvideoi2ctransactionerr)Removed [kVideoI2CTransactionTypeErr](https://developer.apple.com/documentation/iokit/1567789-anonymous/kvideoi2ctransactiontypeerr)Removed [kVideoNoTransactionType](https://developer.apple.com/documentation/kernel/1644547-anonymous/kvideonotransactiontype)Removed [kVideoReplyMicroSecDelayMask](https://developer.apple.com/documentation/kernel/1644546-anonymous/kvideoreplymicrosecdelaymask)Removed [kVideoSimpleI2CType](https://developer.apple.com/documentation/kernel/1644547-anonymous/kvideosimplei2ctype)Removed [mBaseOffset](https://developer.apple.com/documentation/kernel/1644560-anonymous/mbaseoffset)Removed [mBounds](https://developer.apple.com/documentation/iokit/1567390-anonymous/mbounds)Removed [mCmpCount](https://developer.apple.com/documentation/kernel/1644560-anonymous/mcmpcount)Removed [mCmpSize](https://developer.apple.com/documentation/kernel/1644560-anonymous/mcmpsize)Removed [mDevType](https://developer.apple.com/documentation/kernel/1644560-anonymous/mdevtype)Removed [mHRes](https://developer.apple.com/documentation/kernel/1644560-anonymous/mhres)Removed [mPageCnt](https://developer.apple.com/documentation/iokit/1567390-anonymous/mpagecnt)Removed [mPixelSize](https://developer.apple.com/documentation/kernel/1644560-anonymous/mpixelsize)Removed [mPixelType](https://developer.apple.com/documentation/iokit/1567390-anonymous/mpixeltype)Removed [mPlaneBytes](https://developer.apple.com/documentation/iokit/1567390-anonymous/mplanebytes)Removed [mRowBytes](https://developer.apple.com/documentation/iokit/1567390-anonymous/mrowbytes)Removed [mTable](https://developer.apple.com/documentation/iokit/1567390-anonymous/mtable)Removed [mVRes](https://developer.apple.com/documentation/kernel/1644560-anonymous/mvres)Removed [mVersion](https://developer.apple.com/documentation/kernel/1644560-anonymous/mversion)Removed [mVertRefRate](https://developer.apple.com/documentation/iokit/1567390-anonymous/mvertrefrate)Removed [mVidParams](https://developer.apple.com/documentation/iokit/1567390-anonymous/mvidparams)Removed [oneBitMode](https://developer.apple.com/documentation/iokit/1567390-anonymous/onebitmode)Removed [secondVidMode](https://developer.apple.com/documentation/kernel/1644540-anonymous/secondvidmode)Removed [sixteenBitMode](https://developer.apple.com/documentation/kernel/1644540-anonymous/sixteenbitmode)Removed [sixthVidMode](https://developer.apple.com/documentation/iokit/1567898-anonymous/sixthvidmode)Removed [spGammaDir](https://developer.apple.com/documentation/kernel/1644540-anonymous/spgammadir)Removed [spVidNamesDir](https://developer.apple.com/documentation/iokit/1567898-anonymous/spvidnamesdir)Removed [thirdVidMode](https://developer.apple.com/documentation/iokit/1567898-anonymous/thirdvidmode)Removed [thirtyTwoBitMode](https://developer.apple.com/documentation/kernel/1644540-anonymous/thirtytwobitmode)Removed [timingApple12](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapple12)Removed [timingApple12x](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple12x)Removed [timingApple13](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapple13)Removed [timingApple13x](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapple13x)Removed [timingApple15](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple15)Removed [timingApple15x](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple15x)Removed [timingApple16](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple16)Removed [timingApple19](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapple19)Removed [timingApple1Ka](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple1ka)Removed [timingApple1Kb](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapple1kb)Removed [timingApple21](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapple21)Removed [timingAppleNTSC_FF](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapplentsc_ff)Removed [timingAppleNTSC_FFconv](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapplentsc_ffconv)Removed [timingAppleNTSC_ST](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapplentsc_st)Removed [timingAppleNTSC_STconv](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapplentsc_stconv)Removed [timingApplePAL_FF](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapplepal_ff)Removed [timingApplePAL_FFconv](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapplepal_ffconv)Removed [timingApplePAL_ST](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapplepal_st)Removed [timingApplePAL_STconv](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapplepal_stconv)Removed [timingAppleSVGA](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingapplesvga)Removed [timingAppleVGA](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingapplevga)Removed [timingApple_0x0_0hz_Offline](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_0x0_0hz_offline)Removed [timingApple_1024x768_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_1024x768_75hz)Removed [timingApple_1152x870_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapple_1152x870_75hz)Removed [timingApple_512x384_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapple_512x384_60hz)Removed [timingApple_560x384_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapple_560x384_60hz)Removed [timingApple_640x400_67hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapple_640x400_67hz)Removed [timingApple_640x480_67hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingapple_640x480_67hz)Removed [timingApple_640x818_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_640x818_75hz)Removed [timingApple_640x870_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_640x870_75hz)Removed [timingApple_832x624_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_832x624_75hz)Removed [timingApple_FixedRateLCD](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingapple_fixedratelcd)Removed [timingFilmRate_48hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingfilmrate_48hz)Removed [timingGTF_640x480_120hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timinggtf_640x480_120hz)Removed [timingInvalid](https://developer.apple.com/documentation/iokit/1567577-anonymous/timinginvalid)Removed [timingInvalid_SM_T24](https://developer.apple.com/documentation/iokit/1567577-anonymous/timinginvalid_sm_t24)Removed [timingSMPTE240M_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingsmpte240m_60hz)Removed [timingSony_1600x1024_76hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingsony_1600x1024_76hz)Removed [timingSony_1900x1200_74hz](https://developer.apple.com/documentation/iokit/1567324-anonymous/timingsony_1900x1200_74hz)Removed [timingSony_1900x1200_76hz](https://developer.apple.com/documentation/kernel/1644580-anonymous/timingsony_1900x1200_76hz)Removed [timingSony_1920x1080_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingsony_1920x1080_60hz)Removed [timingSony_1920x1080_72hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingsony_1920x1080_72hz)Removed [timingSony_1920x1200_76hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingsony_1920x1200_76hz)Removed [timingVESA_1024x768_60hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1024x768_60hz)Removed [timingVESA_1024x768_70hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1024x768_70hz)Removed [timingVESA_1024x768_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1024x768_75hz)Removed [timingVESA_1024x768_85hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1024x768_85hz)Removed [timingVESA_1280x1024_60hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x1024_60hz)Removed [timingVESA_1280x1024_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x1024_75hz)Removed [timingVESA_1280x1024_85hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x1024_85hz)Removed [timingVESA_1280x960_60hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x960_60hz)Removed [timingVESA_1280x960_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x960_75hz)Removed [timingVESA_1280x960_85hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1280x960_85hz)Removed [timingVESA_1600x1200_60hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1600x1200_60hz)Removed [timingVESA_1600x1200_65hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1600x1200_65hz)Removed [timingVESA_1600x1200_70hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1600x1200_70hz)Removed [timingVESA_1600x1200_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1600x1200_75hz)Removed [timingVESA_1600x1200_80hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1600x1200_80hz)Removed [timingVESA_1600x1200_85hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_1600x1200_85hz)Removed [timingVESA_1792x1344_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1792x1344_60hz)Removed [timingVESA_1792x1344_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1792x1344_75hz)Removed [timingVESA_1856x1392_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1856x1392_60hz)Removed [timingVESA_1856x1392_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1856x1392_75hz)Removed [timingVESA_1920x1440_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1920x1440_60hz)Removed [timingVESA_1920x1440_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_1920x1440_75hz)Removed [timingVESA_640x480_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_640x480_60hz)Removed [timingVESA_640x480_72hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_640x480_72hz)Removed [timingVESA_640x480_75hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_640x480_75hz)Removed [timingVESA_640x480_85hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_640x480_85hz)Removed [timingVESA_800x600_56hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_800x600_56hz)Removed [timingVESA_800x600_60hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_800x600_60hz)Removed [timingVESA_800x600_72hz](https://developer.apple.com/documentation/kernel/1644550-anonymous/timingvesa_800x600_72hz)Removed [timingVESA_800x600_75hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_800x600_75hz)Removed [timingVESA_800x600_85hz](https://developer.apple.com/documentation/iokit/1567577-anonymous/timingvesa_800x600_85hz)Removed [twoBitMode](https://developer.apple.com/documentation/kernel/1644560-anonymous/twobitmode)

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

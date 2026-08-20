---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/ApplicationServices.html
archived_at: '2026-07-18T02:58:41.563513Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# ApplicationServices Changes

## ApplicationServices

AXAttributeConstants.hAdded [#def kAXCriticalValueAttribute](https://developer.apple.com/documentation/applicationservices/kaxcriticalvalueattribute)Added [#def kAXPlaceholderValueAttribute](https://developer.apple.com/documentation/applicationservices/kaxplaceholdervalueattribute)Added [#def kAXWarningValueAttribute](https://developer.apple.com/documentation/applicationservices/kaxwarningvalueattribute)AXRoleConstants.hAdded [#def kAXLevelIndicatorRole](https://developer.apple.com/documentation/applicationservices/kaxlevelindicatorrole)Added [#def kAXRatingIndicatorSubrole](https://developer.apple.com/documentation/applicationservices/kaxratingindicatorsubrole)CGBase.hAdded #def CG_AVAILABLE_BUT_DEPRECATEDAdded #def CG_AVAILABLE_STARTINGCGColorSpace.hRemoved #def kCGColorSpaceUserCMYKRemoved #def kCGColorSpaceUserGrayRemoved #def kCGColorSpaceUserRGBModified [CGColorSpaceGetColorTable()](https://developer.apple.com/documentation/coregraphics/1408853-cgcolorspacegetcolortable)

|  | Declaration |
| --- | --- |
| Old | void CGColorSpaceGetColorTable ( CGColorSpaceRef space, unsigned char \*table); |
| New | void CGColorSpaceGetColorTable ( CGColorSpaceRef space, uint8_t \*table); |

CGContext.hModified [CGContextSetPatternPhase()](https://developer.apple.com/documentation/coregraphics/1455334-cgcontextsetpatternphase)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetPatternPhase ( CGContextRef c, CGSize phase); |
| New | void CGContextSetPatternPhase ( CGContextRef context, CGSize phase); |

Modified [CGContextSetCharacterSpacing()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454786-setcharacterspacing)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetCharacterSpacing ( CGContextRef c, CGFloat spacing); |
| New | void CGContextSetCharacterSpacing ( CGContextRef context, CGFloat spacing); |

Modified [CGContextSetGrayStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455209-cgcontextsetgraystrokecolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetGrayStrokeColor ( CGContextRef c, CGFloat gray, CGFloat alpha); |
| New | void CGContextSetGrayStrokeColor ( CGContextRef context, CGFloat gray, CGFloat alpha); |

Modified [CGContextSetStrokeColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454396-setstrokecolorspace)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetStrokeColorSpace ( CGContextRef c, CGColorSpaceRef colorspace); |
| New | void CGContextSetStrokeColorSpace ( CGContextRef context, CGColorSpaceRef space); |

Modified [CGContextSetCMYKFillColor()](https://developer.apple.com/documentation/coregraphics/1454214-cgcontextsetcmykfillcolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetCMYKFillColor ( CGContextRef c, CGFloat cyan, CGFloat magenta, CGFloat yellow, CGFloat black, CGFloat alpha); |
| New | void CGContextSetCMYKFillColor ( CGContextRef context, CGFloat cyan, CGFloat magenta, CGFloat yellow, CGFloat black, CGFloat alpha); |

Modified [CGContextSetFillColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455151-setfillcolorspace)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetFillColorSpace ( CGContextRef c, CGColorSpaceRef colorspace); |
| New | void CGContextSetFillColorSpace ( CGContextRef context, CGColorSpaceRef space); |

Modified [CGContextSetRenderingIntent()](https://developer.apple.com/documentation/coregraphics/1455544-cgcontextsetrenderingintent)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetRenderingIntent ( CGContextRef c, CGColorRenderingIntent intent); |
| New | void CGContextSetRenderingIntent ( CGContextRef context, CGColorRenderingIntent intent); |

Modified [CGContextConvertSizeToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)

|  | Declaration |
| --- | --- |
| Old | CGSize CGContextConvertSizeToDeviceSpace ( CGContextRef c, CGSize size); |
| New | CGSize CGContextConvertSizeToDeviceSpace ( CGContextRef context, CGSize size); |

Modified [CGContextSetStrokeColor()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456283-setstrokecolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetStrokeColor ( CGContextRef c, const CGFloat components[]); |
| New | void CGContextSetStrokeColor ( CGContextRef context, const CGFloat components[]); |

Modified [CGContextSetRGBStrokeColor()](https://developer.apple.com/documentation/coregraphics/1456378-cgcontextsetrgbstrokecolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetRGBStrokeColor ( CGContextRef c, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha); |
| New | void CGContextSetRGBStrokeColor ( CGContextRef context, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha); |

Modified [CGContextConvertRectToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac)

|  | Declaration |
| --- | --- |
| Old | CGRect CGContextConvertRectToDeviceSpace ( CGContextRef c, CGRect rect); |
| New | CGRect CGContextConvertRectToDeviceSpace ( CGContextRef context, CGRect rect); |

Modified [CGContextConvertPointToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455916-converttodevicespace)

|  | Declaration |
| --- | --- |
| Old | CGPoint CGContextConvertPointToDeviceSpace ( CGContextRef c, CGPoint point); |
| New | CGPoint CGContextConvertPointToDeviceSpace ( CGContextRef context, CGPoint point); |

Modified [CGContextGetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1454940-cgcontextgetinterpolationquality)

|  | Declaration |
| --- | --- |
| Old | CGInterpolationQuality CGContextGetInterpolationQuality ( CGContextRef c); |
| New | CGInterpolationQuality CGContextGetInterpolationQuality ( CGContextRef context); |

Modified [CGContextShowGlyphsAtPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint)

|  | Declaration |
| --- | --- |
| Old | void CGContextShowGlyphsAtPoint ( CGContextRef c, CGFloat x, CGFloat y, const CGGlyph glyphs[], size_t count); |
| New | void CGContextShowGlyphsAtPoint ( CGContextRef context, CGFloat x, CGFloat y, const CGGlyph glyphs[], size_t count); |

Modified [CGContextSetStrokePattern()](https://developer.apple.com/documentation/coregraphics/1454796-cgcontextsetstrokepattern)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetStrokePattern ( CGContextRef c, CGPatternRef pattern, const CGFloat components[]); |
| New | void CGContextSetStrokePattern ( CGContextRef context, CGPatternRef pattern, const CGFloat components[]); |

Modified [CGContextSetCMYKStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455358-cgcontextsetcmykstrokecolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetCMYKStrokeColor ( CGContextRef c, CGFloat cyan, CGFloat magenta, CGFloat yellow, CGFloat black, CGFloat alpha); |
| New | void CGContextSetCMYKStrokeColor ( CGContextRef context, CGFloat cyan, CGFloat magenta, CGFloat yellow, CGFloat black, CGFloat alpha); |

Modified [CGContextConvertRectToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454165-converttouserspace)

|  | Declaration |
| --- | --- |
| Old | CGRect CGContextConvertRectToUserSpace ( CGContextRef c, CGRect rect); |
| New | CGRect CGContextConvertRectToUserSpace ( CGContextRef context, CGRect rect); |

Modified [CGContextConvertPointToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456451-converttouserspace)

|  | Declaration |
| --- | --- |
| Old | CGPoint CGContextConvertPointToUserSpace ( CGContextRef c, CGPoint point); |
| New | CGPoint CGContextConvertPointToUserSpace ( CGContextRef context, CGPoint point); |

Modified [CGContextSetRGBFillColor()](https://developer.apple.com/documentation/coregraphics/1455624-cgcontextsetrgbfillcolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetRGBFillColor ( CGContextRef c, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha); |
| New | void CGContextSetRGBFillColor ( CGContextRef context, CGFloat red, CGFloat green, CGFloat blue, CGFloat alpha); |

Modified [CGContextSetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetInterpolationQuality ( CGContextRef c, CGInterpolationQuality quality); |
| New | void CGContextSetInterpolationQuality ( CGContextRef context, CGInterpolationQuality quality); |

Modified [CGContextGetTextPosition()](https://developer.apple.com/documentation/coregraphics/1454687-cgcontextgettextposition)

|  | Declaration |
| --- | --- |
| Old | CGPoint CGContextGetTextPosition ( CGContextRef c); |
| New | CGPoint CGContextGetTextPosition ( CGContextRef context); |

Modified [CGContextSetGrayFillColor()](https://developer.apple.com/documentation/coregraphics/1454255-cgcontextsetgrayfillcolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetGrayFillColor ( CGContextRef c, CGFloat gray, CGFloat alpha); |
| New | void CGContextSetGrayFillColor ( CGContextRef context, CGFloat gray, CGFloat alpha); |

Modified [CGContextConvertSizeToUserSpace()](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)

|  | Declaration |
| --- | --- |
| Old | CGSize CGContextConvertSizeToUserSpace ( CGContextRef c, CGSize size); |
| New | CGSize CGContextConvertSizeToUserSpace ( CGContextRef context, CGSize size); |

Modified [CGContextGetUserSpaceToDeviceSpaceTransform()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455677-userspacetodevicespacetransform)

|  | Declaration |
| --- | --- |
| Old | CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform ( CGContextRef c); |
| New | CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform ( CGContextRef context); |

Modified [CGContextSetFillColor()](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetFillColor ( CGContextRef c, const CGFloat components[]); |
| New | void CGContextSetFillColor ( CGContextRef context, const CGFloat components[]); |

Modified [CGContextSetFillPattern()](https://developer.apple.com/documentation/coregraphics/1456334-cgcontextsetfillpattern)

|  | Declaration |
| --- | --- |
| Old | void CGContextSetFillPattern ( CGContextRef c, CGPatternRef pattern, const CGFloat components[]); |
| New | void CGContextSetFillPattern ( CGContextRef context, CGPatternRef pattern, const CGFloat components[]); |

CGDataConsumer.hRemoved CGDataConsumerPutBytesCallback (no architecture available)CGDataProvider.hRemoved CGDataProviderGetBytesCallback (no architecture available)Modified [CGDataProviderCreateDirectAccess()](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1805228-cgdataprovidercreatedirectaccess)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGDataProviderCreate()](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1805224-cgdataprovidercreate)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

CGDirectDisplay.hRemoved CGDirectDisplayID (no architecture available)CGDirectPalette.hRemoved CGPaletteBlendFraction (no architecture available)CGDisplayFade.hRemoved CGDisplayFadeReservationToken (no architecture available)CGGeometry.hAdded [#def CGPointEqualToPoint](https://developer.apple.com/documentation/coregraphics/cgpointequaltopoint)Added [#def CGSizeEqualToSize](https://developer.apple.com/documentation/coregraphics/cgsizeequaltosize)CGImage.hModified [CGImageCreateCopyWithColorSpace()](https://developer.apple.com/documentation/coregraphics/cgimage/1455355-copy)

|  | Declaration |
| --- | --- |
| Old | CGImageRef CGImageCreateCopyWithColorSpace ( CGImageRef image, CGColorSpaceRef colorspace); |
| New | CGImageRef CGImageCreateCopyWithColorSpace ( CGImageRef image, CGColorSpaceRef space); |

Modified [CGImageCreate()](https://developer.apple.com/documentation/coregraphics/cgimage/1455149-init)

|  | Declaration |
| --- | --- |
| Old | CGImageRef CGImageCreate ( size_t width, size_t height, size_t bitsPerComponent, size_t bitsPerPixel, size_t bytesPerRow, CGColorSpaceRef colorspace, CGBitmapInfo bitmapInfo, CGDataProviderRef provider, const CGFloat decode[], bool shouldInterpolate, CGColorRenderingIntent intent); |
| New | CGImageRef CGImageCreate ( size_t width, size_t height, size_t bitsPerComponent, size_t bitsPerPixel, size_t bytesPerRow, CGColorSpaceRef space, CGBitmapInfo bitmapInfo, CGDataProviderRef provider, const CGFloat decode[], bool shouldInterpolate, CGColorRenderingIntent intent); |

CGPDFDocument.hModified [CGPDFDocumentGetArtBox()](https://developer.apple.com/documentation/coregraphics/1402601-cgpdfdocumentgetartbox)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGPDFDocumentGetBleedBox()](https://developer.apple.com/documentation/coregraphics/1402596-cgpdfdocumentgetbleedbox)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGPDFDocumentGetTrimBox()](https://developer.apple.com/documentation/coregraphics/1402590-cgpdfdocumentgettrimbox)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGPDFDocumentGetMediaBox()](https://developer.apple.com/documentation/coregraphics/1402592-cgpdfdocumentgetmediabox)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGPDFDocumentGetCropBox()](https://developer.apple.com/documentation/coregraphics/1402598-cgpdfdocumentgetcropbox)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

Modified [CGPDFDocumentGetRotationAngle()](https://developer.apple.com/documentation/coregraphics/1402602-cgpdfdocumentgetrotationangle)

|  | Deprecation |
| --- | --- |
| Old | 10.5 |
| New |  |

CGPattern.hRemoved CGPatternDrawPatternCallback (no architecture available)CGRemoteOperation.hRemoved CGEventErr (no architecture available)CGShading.hModified [CGShadingCreateAxial()](https://developer.apple.com/documentation/coregraphics/1455224-cgshadingcreateaxial)

|  | Declaration |
| --- | --- |
| Old | CGShadingRef CGShadingCreateAxial ( CGColorSpaceRef colorspace, CGPoint start, CGPoint end, CGFunctionRef function, bool extendStart, bool extendEnd); |
| New | CGShadingRef CGShadingCreateAxial ( CGColorSpaceRef space, CGPoint start, CGPoint end, CGFunctionRef function, bool extendStart, bool extendEnd); |

Modified [CGShadingCreateRadial()](https://developer.apple.com/documentation/coregraphics/1456399-cgshadingcreateradial)

|  | Declaration |
| --- | --- |
| Old | CGShadingRef CGShadingCreateRadial ( CGColorSpaceRef colorspace, CGPoint start, CGFloat startRadius, CGPoint end, CGFloat endRadius, CGFunctionRef function, bool extendStart, bool extendEnd); |
| New | CGShadingRef CGShadingCreateRadial ( CGColorSpaceRef space, CGPoint start, CGFloat startRadius, CGPoint end, CGFloat endRadius, CGFunctionRef function, bool extendStart, bool extendEnd); |

CGWindowLevel.hRemoved CGWindowLevel (no architecture available)CMDeviceIntegration.hAdded [cmPrefsSynchError](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmprefssyncherror)CTFontDescriptor.hAdded [CTFontFormat](https://developer.apple.com/documentation/coretext/ctfontformat)Added [CTFontPriority](https://developer.apple.com/documentation/coretext/ctfontpriority)Added [kCTFontEnabledAttribute](https://developer.apple.com/documentation/coretext/kctfontenabledattribute)Added [kCTFontFormatAttribute](https://developer.apple.com/documentation/coretext/kctfontformatattribute)Added [kCTFontFormatBitmap](https://developer.apple.com/documentation/coretext/ctfontformat/bitmap)Added kCTFontFormatOpenTypeAdded [kCTFontFormatPostScript](https://developer.apple.com/documentation/coretext/ctfontformat/postscript)Added [kCTFontFormatTrueType](https://developer.apple.com/documentation/coretext/ctfontformat/truetype)Added [kCTFontFormatUnrecognized](https://developer.apple.com/documentation/coretext/ctfontformat/kctfontformatunrecognized)Added [kCTFontPriorityAttribute](https://developer.apple.com/documentation/coretext/kctfontpriorityattribute)Added [kCTFontPriorityComputer](https://developer.apple.com/documentation/coretext/1543856-anonymous/kctfontprioritycomputer)Added [kCTFontPriorityDynamic](https://developer.apple.com/documentation/coretext/kctfontprioritydynamic)Added [kCTFontPriorityNetwork](https://developer.apple.com/documentation/coretext/kctfontprioritynetwork)Added [kCTFontPriorityProcess](https://developer.apple.com/documentation/coretext/1543856-anonymous/kctfontpriorityprocess)Added [kCTFontPrioritySystem](https://developer.apple.com/documentation/coretext/1543856-anonymous/kctfontprioritysystem)Added [kCTFontPriorityUser](https://developer.apple.com/documentation/coretext/1543856-anonymous/kctfontpriorityuser)Added [kCTFontRegistrationScopeAttribute](https://developer.apple.com/documentation/coretext/kctfontregistrationscopeattribute)Added [kCTFontURLAttribute](https://developer.apple.com/documentation/coretext/kctfonturlattribute)CTFontManager.hAdded [CTFontManagerAutoActivationSetting](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting)Added [CTFontManagerCompareFontFamilyNames()](https://developer.apple.com/documentation/coretext/1499513-ctfontmanagercomparefontfamilyna)Added [CTFontManagerCopyAvailableFontFamilyNames()](https://developer.apple.com/documentation/coretext/1499494-ctfontmanagercopyavailablefontfa)Added [CTFontManagerCopyAvailableFontURLs()](https://developer.apple.com/documentation/coretext/1499478-ctfontmanagercopyavailablefontur)Added [CTFontManagerCopyAvailablePostScriptNames()](https://developer.apple.com/documentation/coretext/1499516-ctfontmanagercopyavailablepostsc)Added [CTFontManagerCreateFontDescriptorsFromURL()](https://developer.apple.com/documentation/coretext/1499500-ctfontmanagercreatefontdescripto)Added [CTFontManagerCreateFontRequestRunLoopSource()](https://developer.apple.com/documentation/coretext/1499507-ctfontmanagercreatefontrequestru) (no architecture available)Added [CTFontManagerEnableFontDescriptors()](https://developer.apple.com/documentation/coretext/1499515-ctfontmanagerenablefontdescripto)Added [CTFontManagerGetAutoActivationSetting()](https://developer.apple.com/documentation/coretext/1499473-ctfontmanagergetautoactivationse)Added [CTFontManagerGetScopeForURL()](https://developer.apple.com/documentation/coretext/1499506-ctfontmanagergetscopeforurl)Added [CTFontManagerIsSupportedFont()](https://developer.apple.com/documentation/coretext/1499491-ctfontmanagerissupportedfont)Added [CTFontManagerRegisterFontsForURL()](https://developer.apple.com/documentation/coretext/1499468-ctfontmanagerregisterfontsforurl)Added [CTFontManagerRegisterFontsForURLs()](https://developer.apple.com/documentation/coretext/1499470-ctfontmanagerregisterfontsforurl)Added [CTFontManagerScope](https://developer.apple.com/documentation/coretext/ctfontmanagerscope)Added [CTFontManagerSetAutoActivationSetting()](https://developer.apple.com/documentation/coretext/1499481-ctfontmanagersetautoactivationse)Added [CTFontManagerUnregisterFontsForURL()](https://developer.apple.com/documentation/coretext/1499496-ctfontmanagerunregisterfontsforu)Added [CTFontManagerUnregisterFontsForURLs()](https://developer.apple.com/documentation/coretext/1499477-ctfontmanagerunregisterfontsforu)Added [kCTFontManagerAutoActivationDefault](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/kctfontmanagerautoactivationdefault)Added [kCTFontManagerAutoActivationDisabled](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/kctfontmanagerautoactivationdisabled)Added [kCTFontManagerAutoActivationEnabled](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/kctfontmanagerautoactivationenabled)Added [kCTFontManagerAutoActivationPromptUser](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting/promptuser)Added [kCTFontManagerBundleIdentifier](https://developer.apple.com/documentation/coretext/kctfontmanagerbundleidentifier)Added [kCTFontManagerRegisteredFontsChangedNotification](https://developer.apple.com/documentation/coretext/kctfontmanagerregisteredfontschangednotification)Added [kCTFontManagerScopeNone](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/none)Added [kCTFontManagerScopeProcess](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/process)Added [kCTFontManagerScopeSession](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/kctfontmanagerscopesession)Added [kCTFontManagerScopeUser](https://developer.apple.com/documentation/coretext/ctfontmanagerscope/user)CTFontManagerErrors.hAdded [CTFontManagerError](https://developer.apple.com/documentation/coretext/ctfontmanagererror)Added [kCTFontManagerErrorAlreadyRegistered](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererroralreadyregistered)Added [kCTFontManagerErrorDomain](https://developer.apple.com/documentation/coretext/kctfontmanagererrordomain)Added [kCTFontManagerErrorFileNotFound](https://developer.apple.com/documentation/coretext/ctfontmanagererror/filenotfound)Added [kCTFontManagerErrorFontURLsKey](https://developer.apple.com/documentation/coretext/kctfontmanagererrorfonturlskey)Added [kCTFontManagerErrorInUse](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorinuse)Added [kCTFontManagerErrorInsufficientPermissions](https://developer.apple.com/documentation/coretext/ctfontmanagererror/insufficientpermissions)Added [kCTFontManagerErrorInvalidFontData](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorinvalidfontdata)Added [kCTFontManagerErrorNotRegistered](https://developer.apple.com/documentation/coretext/ctfontmanagererror/notregistered)Added [kCTFontManagerErrorSystemRequired](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorsystemrequired)Added [kCTFontManagerErrorUnrecognizedFormat](https://developer.apple.com/documentation/coretext/ctfontmanagererror/kctfontmanagererrorunrecognizedformat)CoreText.hAdded [#def kCTVersionNumber10_5_2](https://developer.apple.com/documentation/coretext/kctversionnumber10_5_2)Added [#def kCTVersionNumber10_5_3](https://developer.apple.com/documentation/coretext/kctversionnumber10_5_3)Added [#def kCTVersionNumber10_6](https://developer.apple.com/documentation/coretext/kctversionnumber10_6)Dictionary.hRemoved DictionaryAttributeTableRemoved DictionaryAttributeTablePtrRemoved DictionaryDataInsertModeRemoved DictionaryEntryAttributeRemoved DictionaryInformationRemoved kAdjectiveRemoved kAdverbRemoved kInsertRemoved kInsertOrReplaceRemoved kIsCaseSensitiveRemoved kIsNotDiacriticalSensitiveRemoved kNounRemoved kReplaceRemoved kVerbFontSync.hModified FNSProfileRemoveIndReference()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceGetFamilyInfo()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceDispose()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileAddReference()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileCreate()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceGetIndName()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileCreateWithFSRef()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSSysInfoGet()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceCreate()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileOpen()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSMatchDefaultsGet()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileGetIndReference()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceCreateFromFamily()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileOpenWithFSRef()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceFlatten()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceMatch()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceFindName()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceUnflatten()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileClear()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceMatchFamilies()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceGetVersion()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceCountNames()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileRemoveReference()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileCountReferences()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileClose()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileMatchReference()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceFlattenedSize()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSReferenceMatchFonts()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSProfileGetVersion()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

Modified FNSEnabled()

|  | Deprecation |
| --- | --- |
| Old |  |
| New | 10.5 |

PDEPluginInterface.hAdded [-[NSObject PDEPanelsForType:withHostInfo:]](https://developer.apple.com/documentation/objectivec/nsobject/1494234-pdepanelsfortype)Added [-[NSObject PMPrinter]](https://developer.apple.com/documentation/objectivec/nsobject/1494230-pmprinter)Added [-[NSObject PPDOptionKeyValueDidChange:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494202-ppdoptionkeyvaluedidchange)Added [-[NSObject initWithBundle:]](https://developer.apple.com/documentation/objectivec/nsobject/1494220-initwithbundle)Added [-[NSObject pageFormat]](https://developer.apple.com/documentation/objectivec/nsobject/1494209-pageformat)Added [-[NSObject panelKind]](https://developer.apple.com/documentation/objectivec/nsobject/1494208-panelkind)Added [-[NSObject panelName]](https://developer.apple.com/documentation/objectivec/nsobject/1494224-panelname)Added [-[NSObject panelView]](https://developer.apple.com/documentation/objectivec/nsobject/1494214-panelview)Added -[NSObject panelViewDidResize]Added [-[NSObject ppdFile]](https://developer.apple.com/documentation/objectivec/nsobject/1494226-ppdfile)Added [-[NSObject printSession]](https://developer.apple.com/documentation/objectivec/nsobject/1494218-printsession)Added [-[NSObject printSettings]](https://developer.apple.com/documentation/objectivec/nsobject/1494206-printsettings)Added [-[NSObject restoreValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494216-restorevaluesandreturnerror)Added [-[NSObject saveValuesAndReturnError:]](https://developer.apple.com/documentation/objectivec/nsobject/1494222-savevaluesandreturnerror)Added [-[NSObject shouldHide]](https://developer.apple.com/documentation/objectivec/nsobject/1494210-shouldhide)Added [-[NSObject summaryInfo]](https://developer.apple.com/documentation/objectivec/nsobject/1494212-summaryinfo)Added [-[NSObject supportedPPDOptionKeys]](https://developer.apple.com/documentation/objectivec/nsobject/1494232-supportedppdoptionkeys)Added [-[NSObject willChangePPDOptionKeyValue:ppdChoice:]](https://developer.apple.com/documentation/objectivec/nsobject/1494235-willchangeppdoptionkeyvalue)Added [-[NSObject willShow]](https://developer.apple.com/documentation/objectivec/nsobject/1494204-willshow)Added NSObject(PDEPanel)Added NSObject(PDEPlugIn)Added NSObject(PDEPlugInCallbackProtocol)PMCoreDeprecated.hModified [PMSetPrintSettingsExtendedData()](https://developer.apple.com/documentation/applicationservices/core_printing/1805491-pmsetprintsettingsextendeddata)

|  | Header | Deprecation |
| --- | --- | --- |
| Old | PMCore.h |  |
| New | PMCoreDeprecated.h | 10.6 |

Modified [PMGetPrintSettingsExtendedData()](https://developer.apple.com/documentation/applicationservices/core_printing/1805488-pmgetprintsettingsextendeddata)

|  | Header | Deprecation |
| --- | --- | --- |
| Old | PMCore.h |  |
| New | PMCoreDeprecated.h | 10.6 |

PMDefinitions.hAdded [#def kPMPresetGraphicsTypeAll](https://developer.apple.com/documentation/applicationservices/kpmpresetgraphicstypeall)Added [#def kPMPresetGraphicsTypeGeneral](https://developer.apple.com/documentation/applicationservices/kpmpresetgraphicstypegeneral)Added [#def kPMPresetGraphicsTypeKey](https://developer.apple.com/documentation/applicationservices/kpmpresetgraphicstypekey)Added [#def kPMPresetGraphicsTypeNone](https://developer.apple.com/documentation/applicationservices/kpmpresetgraphicstypenone)Added [#def kPMPresetGraphicsTypePhoto](https://developer.apple.com/documentation/applicationservices/kpmpresetgraphicstypephoto)PMIOModule.hRemoved IOMProcs::CALLBACK_API_C() (no architecture available)Removed IOMContextRemoved IOMInterfaceRemoved IOMInterfaceRefRemoved IOMProcsRemoved #def kIOMBaseVersionMajorRemoved #def kIOMBaseVersionMinorRemoved #def kIOMBuildVersionMajorRemoved #def kIOMBuildVersionMinorRemoved #def kIOModuleIntfIDStrRemoved #def kIOModuleTypeIDStrRemoved #def kPM8BitChannelAttrRemoved #def kPMAppleTalkConnectionRemoved #def kPMBiDiAttrRemoved #def kPMBluetoothConnectionRemoved #def kPMDNSSDConnectionRemoved #def kPMDirServicesConnectionRemoved #def kPMJobIDAttrRemoved #def kPMLPRConnectionRemoved #def kPMLastErrorStrAttrRemoved #def kPMPrinterURIRemoved #def kPMTStatusAttrRemoved #def kPMTimeoutAttrRemoved #def kPMTransparentByteRangeRemoved #def kPMUSBConnectionPMPluginHeader.hRemoved PMPlugInHeader::CALLBACK_API_C() (no architecture available)Removed PMPlugInAPIVersionRemoved PMPlugInHeaderRemoved PMPlugInHeaderInterfacePMPrintSettingsKeys.hAdded #def kPMCustomProfilePathKeyAdded [#def kPMCustomProfilePathStr](https://developer.apple.com/documentation/applicationservices/kpmcustomprofilepathstr)Modified #def kPMLayoutTileOrientationKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMLayoutNUpKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxSubjectKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPrintSelectionOnlyStr](https://developer.apple.com/documentation/applicationservices/kpmprintselectiononlystr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPrimaryPaperFeedKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPageToPaperMappingAllowScalingUpStr](https://developer.apple.com/documentation/applicationservices/kpmpagetopapermappingallowscalingupstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMSecondaryPaperFeedStr](https://developer.apple.com/documentation/applicationservices/kpmsecondarypaperfeedstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMColorMatchingModeStr](https://developer.apple.com/documentation/applicationservices/kpmcolormatchingmodestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMLayoutDirectionStr](https://developer.apple.com/documentation/applicationservices/kpmlayoutdirectionstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPrimaryPaperFeedStr](https://developer.apple.com/documentation/applicationservices/kpmprimarypaperfeedstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMJobHoldUntilTimeKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMCoverPageStr](https://developer.apple.com/documentation/applicationservices/kpmcoverpagestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxUseSoundStr](https://developer.apple.com/documentation/applicationservices/kpmfaxusesoundstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMColorMatchingModeKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMVendorColorMatching

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMLayoutRowsKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMLayoutNUpStr](https://developer.apple.com/documentation/applicationservices/kpmlayoutnupstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxToneDialingKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxWaitForDialToneKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxFromLabelStr](https://developer.apple.com/documentation/applicationservices/kpmfaxfromlabelstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxCoverSheetMessageKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxFromLabelKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMLayoutColumnsKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [kPMCoverPageAfter](https://developer.apple.com/documentation/applicationservices/1418010-anonymous/kpmcoverpageafter)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMLayoutColumnsStr](https://developer.apple.com/documentation/applicationservices/kpmlayoutcolumnsstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMCoverPageDefault

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMApplicationColorMatchingStr](https://developer.apple.com/documentation/applicationservices/kpmapplicationcolormatchingstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxSubjectLabelKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPSErrorHandlerKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxCoverSheetMessageStr](https://developer.apple.com/documentation/applicationservices/kpmfaxcoversheetmessagestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMTotalBeginPagesStr](https://developer.apple.com/documentation/applicationservices/kpmtotalbeginpagesstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [PMPageToPaperMappingType](https://developer.apple.com/documentation/applicationservices/pmpagetopapermappingtype)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMCopiesKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxDateLabelKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMBorderTypeKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMColorSyncProfileIDKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxPrefixKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMOutputOrderStr](https://developer.apple.com/documentation/applicationservices/kpmoutputorderstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMBorderKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMBorderTypeStr](https://developer.apple.com/documentation/applicationservices/kpmbordertypestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPSErrorHandlerStr](https://developer.apple.com/documentation/applicationservices/kpmpserrorhandlerstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMTotalSidesImagedKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPageToPaperMediaNameStr](https://developer.apple.com/documentation/applicationservices/kpmpagetopapermedianamestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMOutputFilenameKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPageToPaperMappingTypeKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxToStr](https://developer.apple.com/documentation/applicationservices/kpmfaxtostr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPageToPaperMediaNameKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMColorSyncProfileIDStr](https://developer.apple.com/documentation/applicationservices/kpmcolorsyncprofileidstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMCopiesStr](https://developer.apple.com/documentation/applicationservices/kpmcopiesstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxToneDialingStr](https://developer.apple.com/documentation/applicationservices/kpmfaxtonedialingstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMJobPriorityKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMSecondaryPaperFeedKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxDateLabelStr](https://developer.apple.com/documentation/applicationservices/kpmfaxdatelabelstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [kPMCoverPageNone](https://developer.apple.com/documentation/applicationservices/kpmcoverpagenone)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMCopyCollateKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMOutputOrderKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxSubjectStr](https://developer.apple.com/documentation/applicationservices/kpmfaxsubjectstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxNumberKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxSheetsLabelKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxPrefixStr](https://developer.apple.com/documentation/applicationservices/kpmfaxprefixstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxNumberStr](https://developer.apple.com/documentation/applicationservices/kpmfaxnumberstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMJobPriorityStr](https://developer.apple.com/documentation/applicationservices/kpmjobprioritystr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxToKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxToLabelStr](https://developer.apple.com/documentation/applicationservices/kpmfaxtolabelstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMCoverPageSourceStr](https://developer.apple.com/documentation/applicationservices/kpmcoverpagesourcestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMJobStateStr](https://developer.apple.com/documentation/applicationservices/kpmjobstatestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMJobStateKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPageToPaperMappingAllowScalingUpKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMTotalBeginPagesKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMOutputFilenameStr](https://developer.apple.com/documentation/applicationservices/kpmoutputfilenamestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxSubjectLabelStr](https://developer.apple.com/documentation/applicationservices/kpmfaxsubjectlabelstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPrintSelectionOnlyKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMDuplexingStr](https://developer.apple.com/documentation/applicationservices/kpmduplexingstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMLayoutRowsStr](https://developer.apple.com/documentation/applicationservices/kpmlayoutrowsstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMVendorColorMatchingStr](https://developer.apple.com/documentation/applicationservices/kpmvendorcolormatchingstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxCoverSheetKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMApplicationColorMatching

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMBorderStr](https://developer.apple.com/documentation/applicationservices/kpmborderstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxSheetsLabelStr](https://developer.apple.com/documentation/applicationservices/kpmfaxsheetslabelstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPageSetStr](https://developer.apple.com/documentation/applicationservices/kpmpagesetstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMCoverPageKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPSTraySwitchStr](https://developer.apple.com/documentation/applicationservices/kpmpstrayswitchstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMJobHoldUntilTimeStr](https://developer.apple.com/documentation/applicationservices/kpmjobholduntiltimestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMTotalSidesImagedStr](https://developer.apple.com/documentation/applicationservices/kpmtotalsidesimagedstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMPageToPaperMappingTypeStr](https://developer.apple.com/documentation/applicationservices/kpmpagetopapermappingtypestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMDestinationPrinterIDKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPSTraySwitchKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [kPMPageToPaperMappingNone](https://developer.apple.com/documentation/applicationservices/kpmpagetopapermappingnone)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMDestinationTypeKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMCoverPageSourceKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxUseSoundKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxWaitForDialToneStr](https://developer.apple.com/documentation/applicationservices/kpmfaxwaitfordialtonestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMFaxCoverSheetStr](https://developer.apple.com/documentation/applicationservices/kpmfaxcoversheetstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMDuplexingKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMLayoutDirectionKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMFaxToLabelKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMDestinationPrinterIDStr](https://developer.apple.com/documentation/applicationservices/kpmdestinationprinteridstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [kPMPageToPaperMappingScaleToFit](https://developer.apple.com/documentation/applicationservices/kpmpagetopapermappingscaletofit)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMCopyCollateStr](https://developer.apple.com/documentation/applicationservices/kpmcopycollatestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [kPMCoverPageBefore](https://developer.apple.com/documentation/applicationservices/kpmcoverpagebefore)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMDestinationTypeStr](https://developer.apple.com/documentation/applicationservices/kpmdestinationtypestr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified #def kPMPageSetKey

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

Modified [#def kPMLayoutTileOrientationStr](https://developer.apple.com/documentation/applicationservices/kpmlayouttileorientationstr)

|  | Header |
| --- | --- |
| Old | PMTicket.h |
| New | PMPrintSettingsKeys.h |

PMPrinterModule.hRemoved #def A0Removed #def A1Removed #def A2Removed #def A3Removed #def A4Removed #def A5Removed #def A6Removed #def A7Removed #def A8Removed #def A9Removed #def ASizeRemoved #def B0Removed #def B1Removed #def B10Removed #def B2Removed #def B3Removed #def B4Removed #def B5Removed #def B6Removed #def B7Removed #def B8Removed #def B9Removed #def BSizeRemoved #def CSizeRemoved #def DSizeRemoved #def DefaultPaperRemoved #def ESizeRemoved #def Envelope10Removed #def Envelope10x13Removed #def Envelope10x14Removed #def Envelope10x15Removed #def Envelope6x9Removed #def Envelope7x9Removed #def Envelope9Removed #def Envelope9x11Removed #def Envelope9x12Removed #def EnvelopeB4Removed #def EnvelopeB5Removed #def EnvelopeC3Removed #def EnvelopeC4Removed #def EnvelopeC5Removed #def EnvelopeC6Removed #def EnvelopeLongRemoved #def EnvelopeMonarchRemoved #def FolioRemoved #def InvoiceRemoved #def JISB0Removed #def JISB1Removed #def JISB10Removed #def JISB2Removed #def JISB3Removed #def JISB4Removed #def JISB5Removed #def JISB7Removed #def JISB8Removed #def JISB9Removed #def LedgerRemoved #def QuartoRemoved #def TabloidRemoved #def USExecutiveEnvelopeRemoved #def USLegalRemoved #def USLetterRemoved #def iso10PMPrinterModuleDeprecated.hRemoved PMProcs::CALLBACK_API_C() (no architecture available)Removed GetConnInfoProcPtrRemoved PMContextRemoved PMDrawingCtxRemoved PMIOCloseProcPtrRemoved PMIOGetAttributeProcPtrRemoved PMIOOpenProcPtrRemoved PMIOProcsRemoved PMIOReadProcPtrRemoved PMIOSetAttributeProcPtrRemoved PMIOStatusProcPtrRemoved PMIOWriteProcPtrRemoved PMImageRefRemoved PMInterfaceRemoved PMInterfaceRefRemoved PMJobStreamGetNextBandProcPtrRemoved PMJobStreamGetPosProcPtrRemoved PMJobStreamOpenProcPtrRemoved PMJobStreamProcsRemoved PMJobStreamReadWriteProcPtrRemoved PMJobStreamSetPosProcPtrRemoved PMNotificationProcPtrRemoved PMProcsRemoved attribute (no architecture available)Removed buffPtr (no architecture available)Removed buffer (no architecture available)Removed connectionType (no architecture available)Removed eoj (no architecture available)Removed #def kPMBaseVersionMajorRemoved #def kPMBaseVersionMinorRemoved #def kPMBrowserInfoNumValuesRemoved #def kPMBuildVersionMajorRemoved #def kPMBuildVersionMinorRemoved #def kPMErrorCodeKeyRemoved #def kPMErrorExplanationKeyRemoved #def kPMErrorTextKeyRemoved #def kPMEventCodeKeyRemoved #def kPMEventContextKeyRemoved #def kPMEventErrorOccurredRemoved #def kPMEventPrinterStatusRemoved #def kPMEventRecoverableErrorClearedRemoved #def kPMEventRecoverableErrorOccurredRemoved #def kPMPrinterBrowserDeviceIDKeyRemoved #def kPMPrinterBrowserIconsKeyRemoved #def kPMPrinterBrowserInfoKeyRemoved #def kPMPrinterBrowserKindKeyRemoved #def kPModuleIntfIDStrRemoved #def kPModuleTypeIDStrRemoved markerPos (no architecture available)Removed notificationDict (no architecture available)Removed notificationReplyDict (no architecture available)Removed pbmPath (no architecture available)Removed pmRasterBand (no architecture available)Removed posMode (no architecture available)Removed result (no architecture available)Removed status (no architecture available)PMPrintingDialogExtensions.hAdded #def SUMMARY_DISPLAY_ORDERAdded #def kAppPageSetupDialogTypeIDStrAdded #def kAppPrintDialogTypeIDStrAdded #def kAppPrintThumbnailTypeIDStrAdded #def kDialogExtensionIntfIDStrAdded #def kGeneralPageSetupDialogTypeIDStrAdded #def kGeneralPrintDialogTypeIDStrAdded #def kPMColorMatchingPDEKindIDAdded #def kPMColorPDEKindIDAdded #def kPMCopiesAndPagesPDEKindIDAdded #def kPMCoverPagePDEKindIDAdded #def kPMCustomPaperSizePDEKindIDAdded #def kPMDuplexPDEKindIDAdded #def kPMErrorHandlingPDEKindIDAdded #def kPMFaxCoverPagePDEKindIDAdded #def kPMFaxModemPDEKindIDAdded #def kPMImagingOptionsPDEKindIDAdded #def kPMInkPDEKindIDAdded #def kPMLayoutPDEKindIDAdded #def kPMOutputOptionsPDEKindIDAdded #def kPMPageAttributesKindIDAdded #def kPMPaperFeedPDEKindIDAdded #def kPMPaperHandlingPDEKindIDAdded #def kPMPaperSourcePDEKindIDAdded #def kPMPrinterFeaturesPDEKindIDAdded #def kPMPriorityPDEKindIDAdded #def kPMQualityMediaPDEKindIDAdded #def kPMRotationScalingPDEKindIDAdded #def kPMSchedulerPDEKindIDAdded #def kPMSummaryPanelKindIDAdded #def kPrinterModuleTypeIDStrPMRaster.hRemoved PMBandOrderRemoved PMPixelFormatRemoved PMPixelLayoutRemoved PMRasterBandRemoved kPMCMYK_32Removed kPMDataChunkyRemoved #def kPMDataFormatRasterRemoved kPMDataPlanarRemoved kPMDataUnusedRemoved kPMFirstBandRemoved kPMGray_1Removed kPMGray_8Removed kPMLastBandRemoved kPMLoneBandRemoved kPMMiddleBandRemoved kPMRGBX_32Removed kPMRGBX_32_Sep_Gray_8Removed kPMRGB_16Removed kPMRGB_24Removed kPMUnusedRemoved kPMXRGB_32PMTemplate.hRemoved PMConstraintTypeRemoved PMTemplateCreate()Removed PMTemplateCreateXML()Removed PMTemplateDelete()Removed PMTemplateGetBooleanDefaultValue()Removed PMTemplateGetCFArrayConstraintValue()Removed PMTemplateGetCFDataDefaultValue()Removed PMTemplateGetCFDefaultValue()Removed PMTemplateGetCFRangeConstraintValue()Removed PMTemplateGetConstraintType()Removed PMTemplateGetDoubleDefaultValue()Removed PMTemplateGetDoubleListConstraintValue()Removed PMTemplateGetDoubleRangeConstraintValue()Removed PMTemplateGetDoubleRangeDefaultValue()Removed PMTemplateGetDoubleRangesConstraintValue()Removed PMTemplateGetListTicketConstraintValue()Removed PMTemplateGetPMRectDefaultValue()Removed PMTemplateGetPMRectListConstraintValue()Removed PMTemplateGetPMTicketDefaultValue()Removed PMTemplateGetSInt32DefaultValue()Removed PMTemplateGetSInt32ListConstraintValue()Removed PMTemplateGetSInt32RangeConstraintValue()Removed PMTemplateGetSInt32RangeDefaultValue()Removed PMTemplateGetSInt32RangesConstraintValue()Removed PMTemplateGetValueType()Removed PMTemplateIsLocked()Removed PMTemplateLoadFromXML()Removed PMTemplateMakeEntry()Removed PMTemplateMakeFullEntry()Removed PMTemplateMergeTemplates()Removed PMTemplateRemoveEntry()Removed PMTemplateSetBooleanDefaultValue()Removed PMTemplateSetCFArrayConstraintValue()Removed PMTemplateSetCFDataDefaultValue()Removed PMTemplateSetCFDefaultValue()Removed PMTemplateSetCFRangeConstraint()Removed PMTemplateSetDoubleDefaultValue()Removed PMTemplateSetDoubleListConstraint()Removed PMTemplateSetDoubleRangeConstraint()Removed PMTemplateSetDoubleRangeDefaultValue()Removed PMTemplateSetDoubleRangesConstraint()Removed PMTemplateSetPMRectDefaultValue()Removed PMTemplateSetPMRectListConstraint()Removed PMTemplateSetPMTicketDefaultValue()Removed PMTemplateSetPMTicketListConstraint()Removed PMTemplateSetSInt32DefaultValue()Removed PMTemplateSetSInt32ListConstraint()Removed PMTemplateSetSInt32RangeConstraint()Removed PMTemplateSetSInt32RangeDefaultValue()Removed PMTemplateSetSInt32RangesConstraint()Removed PMTemplateValidateItem()Removed PMTemplateWriteXML()Removed PMValueTypeRemoved kPMConstraintListRemoved kPMConstraintPrivateRemoved kPMConstraintRangeRemoved kPMConstraintUndefinedRemoved #def kPMCustomPageHeightKeyRemoved #def kPMCustomPageHeightStrRemoved #def kPMCustomPageMarginsKeyRemoved #def kPMCustomPageMarginsStrRemoved #def kPMCustomPageWidthKeyRemoved #def kPMCustomPageWidthStrRemoved #def kPMDefaultReverseOutputOrderKeyRemoved #def kPMDefaultReverseOutputOrderStrRemoved #def kPMPaperInfoListRemoved #def kPMPaperInfoListStrRemoved #def kPMTemplatePreludeRemoved kPMValueArrayRemoved kPMValueBooleanRemoved kPMValueDataRemoved kPMValueDateRemoved kPMValueDictRemoved kPMValueDoubleRemoved kPMValueDoubleRangeRemoved kPMValuePMRectRemoved kPMValueSInt32Removed kPMValueSInt32RangeRemoved kPMValueStringRemoved kPMValueTicketRemoved kPMValueUInt32Removed kPMValueUInt32RangeRemoved kPMValueUndefinedPMTicket.hRemoved CStrListRemoved ConstCStrListRemoved ConstPMRectListRemoved ConstSInt32ListRemoved EXTERN_API_C() (no architecture available)Removed PMRectListRemoved PMTemplateRefRemoved PMTicketConfirmTicket()Removed PMTicketContainsItem()Removed PMTicketContainsTicket()Removed PMTicketCopy()Removed PMTicketCopyItem()Removed PMTicketCopyKeys()Removed PMTicketCreate()Removed PMTicketCreateDict()Removed PMTicketCreateTemplate()Removed PMTicketDeleteItem()Removed PMTicketErrorsRemoved PMTicketFillFromArray()Removed PMTicketGetAPIVersion()Removed PMTicketGetAllocator()Removed PMTicketGetBoolean()Removed PMTicketGetBytes()Removed PMTicketGetCFArray()Removed PMTicketGetCFBoolean()Removed PMTicketGetCFData()Removed PMTicketGetCFDate()Removed PMTicketGetCFDictionary()Removed PMTicketGetCFNumber()Removed PMTicketGetCFString()Removed PMTicketGetCString()Removed PMTicketGetDouble()Removed PMTicketGetEnumType()Removed PMTicketGetIndexPMResolution()Removed PMTicketGetItem()Removed PMTicketGetPMRect()Removed PMTicketGetPMResolution()Removed PMTicketGetPString()Removed PMTicketGetRetainCount()Removed PMTicketGetSInt32()Removed PMTicketGetTicket()Removed PMTicketGetType()Removed PMTicketGetUInt32()Removed PMTicketItemStructRemoved PMTicketItemTypeRemoved PMTicketReadXMLFromFile()Removed PMTicketRefRemoved PMTicketRelease()Removed PMTicketReleaseAndClear()Removed PMTicketReleaseItem()Removed PMTicketRemoveTicket()Removed PMTicketRetain()Removed PMTicketSetBoolean()Removed PMTicketSetBytes()Removed PMTicketSetCFArray()Removed PMTicketSetCFBoolean()Removed PMTicketSetCFData()Removed PMTicketSetCFDate()Removed PMTicketSetCFDictionary()Removed PMTicketSetCFNumber()Removed PMTicketSetCFString()Removed PMTicketSetCString()Removed PMTicketSetCStringArray()Removed PMTicketSetDouble()Removed PMTicketSetDoubleArray()Removed PMTicketSetItem()Removed PMTicketSetPMRect()Removed PMTicketSetPMRectArray()Removed PMTicketSetPMResolution()Removed PMTicketSetPMResolutionArray()Removed PMTicketSetPString()Removed PMTicketSetSInt32()Removed PMTicketSetSInt32Array()Removed PMTicketSetTemplate()Removed PMTicketSetTicket()Removed PMTicketSetUInt32()Removed PMTicketSetUInt32Array()Removed PMTicketToXML()Removed PMTicketTypeRemoved PMTicketValidate()Removed PMTicketWriteXML()Removed PMTicketWriteXMLToFile()Removed PMXMLToTicket()Removed PMXMLURLToTicket()Removed SInt32ListRemoved #def kPM8BitCommKeyRemoved #def kPM8BitCommStrRemoved #def kPMAdjustedPageRectKeyRemoved #def kPMAdjustedPageRectStrRemoved #def kPMAdjustedPaperRectKeyRemoved #def kPMAdjustedPaperRectStrRemoved #def kPMAdobeRGBCustomColorMatchingProfileKeyRemoved #def kPMAdobeRGBCustomColorMatchingProfileStrRemoved #def kPMApplicationNameKeyRemoved #def kPMApplicationNameStrRemoved #def kPMColorDeviceIDKeyRemoved #def kPMColorDeviceIDStrRemoved #def kPMColorSpaceModelKeyRemoved #def kPMColorSpaceModelStrRemoved #def kPMColorSyncProfilesKeyRemoved #def kPMColorSyncProfilesStrRemoved #def kPMCompiledPPDKeyRemoved #def kPMCompiledPPDStrRemoved #def kPMConstrainedPaperKeyRemoved #def kPMConstrainedPaperStrRemoved #def kPMConverterSetupTicketRemoved kPMConverterSetupTicketTypeRemoved #def kPMCopyCollateDefaultRemoved #def kPMCustomColorMatchingProfileKeyRemoved #def kPMCustomColorMatchingProfileStrRemoved #def kPMCustomPaperKeyRemoved #def kPMCustomPaperStrRemoved #def kPMDescriptionFileKeyRemoved #def kPMDescriptionFileStrRemoved #def kPMDestinationTicketRemoved kPMDestinationTicketTypeRemoved #def kPMDocumentTicketRemoved #def kPMDocumentTicketPreludeRemoved kPMDocumentTicketTypeRemoved #def kPMDoesCopiesKeyRemoved #def kPMDoesCopiesStrRemoved #def kPMDoesCopyCollateKeyRemoved #def kPMDoesCopyCollateStrRemoved #def kPMDoesReverseOrderKeyRemoved #def kPMDoesReverseOrderStrRemoved #def kPMDontFetchItemRemoved #def kPMDrawingResHorizontalKeyRemoved #def kPMDrawingResHorizontalStrRemoved #def kPMDrawingResVerticalKeyRemoved #def kPMDrawingResVerticalStrRemoved #def kPMDriverCreatorKeyRemoved #def kPMDriverCreatorStrRemoved #def kPMDuplexingRequiresFlippedMarginAdjustKeyRemoved #def kPMDuplexingRequiresFlippedMarginAdjustStrRemoved #def kPMFirstPageKeyRemoved #def kPMFirstPageStrRemoved #def kPMFormattingPrinterKeyRemoved #def kPMFormattingPrinterStrRemoved #def kPMHasCustomDuplexPDEKeyRemoved #def kPMHasCustomDuplexPDEStrRemoved #def kPMInputFileTypeListKeyRemoved #def kPMInputFileTypeListStrRemoved #def kPMInstallableOptionKeyRemoved #def kPMInstallableOptionStrRemoved #def kPMIsBinaryOKKeyRemoved #def kPMIsBinaryOKStrRemoved kPMItemBooleanTypeRemoved kPMItemCStrListTypeRemoved kPMItemCStringTypeRemoved kPMItemInvalidTypeRemoved kPMItemPMRectListTypeRemoved kPMItemPMRectTypeRemoved kPMItemSInt32ListTypeRemoved kPMItemSInt32TypeRemoved #def kPMJobNameKeyRemoved #def kPMJobNameStrRemoved #def kPMJobOwnerKeyRemoved #def kPMJobOwnerStrRemoved #def kPMJobTagsKeyRemoved #def kPMJobTagsStrRemoved #def kPMJobTemplateKeyRemoved #def kPMJobTemplateStrRemoved #def kPMJobTicketRemoved #def kPMJobTicketPreludeRemoved kPMJobTicketTypeRemoved #def kPMLastPageKeyRemoved #def kPMLastPageStrRemoved #def kPMMakeAndModelNameKeyRemoved #def kPMMakeAndModelNameStrRemoved #def kPMMatchPaperKeyRemoved #def kPMMatchPaperStrRemoved #def kPMModuleInfoTicketRemoved kPMModuleInfoTicketTypeRemoved #def kPMOutputTypeKeyRemoved #def kPMOutputTypeListKeyRemoved #def kPMOutputTypeListStrRemoved #def kPMOutputTypeStrRemoved #def kPMPPDNameKeyRemoved #def kPMPPDNameStrRemoved #def kPMPPDPaperCodeNameKeyRemoved #def kPMPPDPaperCodeNameStrRemoved #def kPMPPDPaperNameKeyRemoved #def kPMPPDPaperNameStrRemoved kPMPSTTRasterizerAccept68KRemoved kPMPSTTRasterizerNoneRemoved kPMPSTTRasterizerType42Removed kPMPSTTRasterizerUnknownRemoved kPMPSTargetLanguageLevel1Removed kPMPSTargetLanguageLevel1and2Removed kPMPSTargetLanguageLevel2Removed kPMPSTargetLanguageLevel2and3Removed kPMPSTargetLanguageLevel3Removed kPMPSTargetLanguageLevelDefaultRemoved kPMPSTargetLanguageLevelUnknownRemoved #def kPMPageFormatPreludeRemoved #def kPMPageFormatTicketRemoved kPMPageFormatTicketTypeRemoved #def kPMPageOrientationKeyRemoved #def kPMPageOrientationStrRemoved #def kPMPageRangeKeyRemoved #def kPMPageRangeStrRemoved #def kPMPageScalingHorizontalKeyRemoved #def kPMPageScalingHorizontalStrRemoved #def kPMPageScalingVerticalKeyRemoved #def kPMPageScalingVerticalStrRemoved #def kPMPageTicketRemoved #def kPMPageTicketPreludeRemoved kPMPageTicketTypeRemoved #def kPMPaperInfoPreludeRemoved #def kPMPaperInfoTicketRemoved kPMPaperInfoTicketTypeRemoved #def kPMPaperNameKeyRemoved #def kPMPaperNameStrRemoved #def kPMPostScriptLevelKeyRemoved #def kPMPostScriptLevelStrRemoved #def kPMPostScriptRevisionKeyRemoved #def kPMPostScriptRevisionStrRemoved #def kPMPostScriptTrueTypeFontRasterizerKeyRemoved #def kPMPostScriptTrueTypeFontRasterizerStrRemoved #def kPMPostScriptVersionKeyRemoved #def kPMPostScriptVersionStrRemoved #def kPMPreviewKeyRemoved #def kPMPreviewStrRemoved #def kPMPrintSettingsPreludeRemoved #def kPMPrintSettingsTicketRemoved kPMPrintSettingsTicketTypeRemoved #def kPMPrinterAddressKeyRemoved #def kPMPrinterAddressStrRemoved #def kPMPrinterFontKeyRemoved #def kPMPrinterFontStrRemoved #def kPMPrinterInfoPreludeRemoved #def kPMPrinterInfoTicketRemoved kPMPrinterInfoTicketTypeRemoved #def kPMPrinterIsPostScriptDriverKeyRemoved #def kPMPrinterIsPostScriptDriverStrRemoved #def kPMPrinterLongNameKeyRemoved #def kPMPrinterLongNameStrRemoved #def kPMPrinterMaxResKeyRemoved #def kPMPrinterMaxResStrRemoved #def kPMPrinterMinResKeyRemoved #def kPMPrinterMinResStrRemoved #def kPMPrinterModuleFormatKeyRemoved #def kPMPrinterModuleFormatStrRemoved #def kPMPrinterShortNameKeyRemoved #def kPMPrinterShortNameStrRemoved #def kPMPrinterSuggestedResKeyRemoved #def kPMPrinterSuggestedResStrRemoved #def kPMSpoolFormatKeyRemoved #def kPMSpoolFormatStrRemoved #def kPMSupportsColorKeyRemoved #def kPMSupportsColorStrRemoved #def kPMSupportsVendorMatchingModeKeyRemoved #def kPMSupportsVendorMatchingModeStrRemoved #def kPMTicketListRemoved #def kPMTicketListPreludeRemoved kPMTicketListTypeRemoved kPMTicketTypeUnknownRemoved #def kPMTopLevelRemoved #def kPMTotalMemAvailableKeyRemoved #def kPMTotalMemAvailableStrRemoved #def kPMTotalMemInstalledKeyRemoved #def kPMTotalMemInstalledStrRemoved #def kPMTransparentCommKeyRemoved #def kPMTransparentCommStrRemoved #def kPMUnadjustedPageRectKeyRemoved #def kPMUnadjustedPageRectStrRemoved #def kPMUnadjustedPaperRectKeyRemoved #def kPMUnadjustedPaperRectStrRemoved #def kPMUserLanguageKeyRemoved #def kPMUserLanguageStrRemoved #def kPMsRGBCustomColorMatchingProfileKeyRemoved #def kPMsRGBCustomColorMatchingProfileStrRemoved kPSErrorHandlerRemoved kPSNoErrorHandlerPMTicketDeprecated.hRemoved PMSessionGetTemplateFromSession()Removed PMSessionGetTicketFromSession()Removed PMTicketGetLockedState()Removed PMTicketGetMetaItem()Removed PMTicketGetPPDDict()Removed PMTicketIsItemLocked()Removed PMTicketLockItem()Removed PMTicketSetMetaItem()Removed PMTicketUnlockItem()Removed #def kPMBandingRequestedKeyRemoved #def kPMBandingRequestedStrRemoved #def kPMCVColorSyncProfileIDKeyRemoved #def kPMCVColorSyncProfileIDStrRemoved #def kPMColorModeKeyRemoved #def kPMColorModeStrRemoved #def kPMColorSyncMatchingRemoved #def kPMColorSyncMatchingStrRemoved #def kPMConverterResHorizontalKeyRemoved #def kPMConverterResHorizontalStrRemoved #def kPMConverterResVerticalKeyRemoved #def kPMConverterResVerticalStrRemoved #def kPMConverterSetupPreludeRemoved #def kPMDepthSwitchingEnabledKeyRemoved #def kPMDepthSwitchingEnabledStrRemoved #def kPMPSErrorOnScreenKeyRemoved #def kPMPSErrorOnScreenStrRemoved #def kPMPageCustomDialogHdlKeyRemoved #def kPMPageCustomDialogHdlStrRemoved #def kPMPaperSourceKeyRemoved #def kPMPaperSourceStrRemoved #def kPMPaperTypeKeyRemoved #def kPMPaperTypeStrRemoved #def kPMPrintBackupRecordDataKeyRemoved #def kPMPrintBackupRecordDataStrRemoved #def kPMPrintBackupRecordHdlKeyRemoved #def kPMPrintBackupRecordHdlStrRemoved #def kPMPrintCustomDialogHdlKeyRemoved #def kPMPrintCustomDialogHdlStrRemoved #def kPMPrintOrientationKeyRemoved #def kPMPrintOrientationStrRemoved #def kPMPrintScalingAlignmentKeyRemoved #def kPMPrintScalingAlignmentStrRemoved #def kPMPrintScalingHorizontalKeyRemoved #def kPMPrintScalingHorizontalStrRemoved #def kPMPrintScalingVerticalKeyRemoved #def kPMPrintScalingVerticalStrRemoved #def kPMQualityKeyRemoved #def kPMQualityStrRemoved #def kPMRequestedPixelFormatKeyRemoved #def kPMRequestedPixelFormatStrRemoved #def kPMRequestedPixelLayoutKeyRemoved #def kPMRequestedPixelLayoutStrRemoved #def kPMRequiredBandHeightKeyRemoved #def kPMRequiredBandHeightStrRemoved #def kPMWhiteSkippingEnabledKeyRemoved #def kPMWhiteSkippingEnabledStrPPDLib.hRemoved InfoButtonProcPtrRemoved InvocationLocatorRemoved LAxisRemoved LPaperRemoved MindexRemoved OindexRemoved PPDAddFeatureEntries()Removed PPDAddFeatureEntriesFromPPDContext()Removed PPDContextRemoved PPDEventFilterRemoved PPDFileSpecRemoved PPDGetGenericPPDNameProcRemoved PPDMatchRemoved PPDMatchHandleRemoved PPDMatchPtrRemoved PPDParseErrRemoved PPDPrinterDescRemoved PindexRemoved StrListRemoved StrListHdlRemoved StrListPtrRemoved TindexRemoved UIConstraintRemoved UIConstraintListRemoved UIConstraintListHRemoved UIConstraintListPRemoved UIConstraintPRemoved WebSearchDlgFilterRemoved WebSearchProgressProcRemoved getUIConstraintListH()Removed #def kDoManualRemoved #def kPPDInvalidIndexRemoved #def kUIHeaderVersionRemoved #def kUIOptionVersionRemoved ppdApplyConstraints()Removed ppdCheckConstraints()Removed ppdCheckDates()Removed ppdClearOptions()Removed ppdCloseCompiledPPDFromTicket()Removed ppdCloseContext()Removed ppdCountUIHeaders()Removed ppdCountUIOptions()Removed ppdCreateInstallableOptionsData()Removed ppdErrForbiddenRemoved ppdErrNotFoundRemoved ppdFindFile()Removed ppdGetAllOptions()Removed ppdGetCompiledPPDData()Removed ppdGetFolder()Removed ppdGetGenericPPDName()Removed ppdGetGroupAlias()Removed ppdGetIndUIHeader()Removed ppdGetIndUIOption()Removed ppdGetInvocation()Removed ppdGetInvocationFile()Removed ppdGetInvocationLocator()Removed ppdGetInvocationString()Removed ppdGetInvocationStruct()Removed ppdGetMainAlias()Removed ppdGetMainIndex()Removed ppdGetMainString()Removed ppdGetMessageTranslateList()Removed ppdGetOptionAlias()Removed ppdGetOptionIndex()Removed ppdGetOptionString()Removed ppdGetParseFolder()Removed ppdGetUIHeader()Removed ppdGetUIKeyType()Removed ppdGetUIOption()Removed ppdMatchPrinter()Removed ppdOpenAndParsePPDAutoSetup()Removed ppdOpenCompiledPPDFromTicket()Removed ppdOpenContext()Removed ppdParseFile()Removed ppdParseHandle()Removed ppdSetDefaultOptions()Removed ppdSetSelection()Removed recordOptionPairProcRemoved setInstallableOptions()Removed xUIHeaderRemoved xUIHeaderPRemoved xUIOptionRemoved xUIOptionPQuickdrawTypes.hModified size

|  | Header |
| --- | --- |
| Old | PMPrinterModuleDeprecated.h |
| New | QuickdrawTypes.h |

SFNTTypes.hAdded kFontUnicodeV2_0BMPOnlySemanticsAdded kFontUnicodeV2_0FullCoverageSemanticsAdded kFontUnicodeV4_0VariationSequenceSemantics

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

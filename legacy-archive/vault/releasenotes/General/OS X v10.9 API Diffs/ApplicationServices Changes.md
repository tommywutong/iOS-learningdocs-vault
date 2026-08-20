---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/ApplicationServices.html
archived_at: '2026-07-18T02:54:08.721953Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# ApplicationServices Changes

## ApplicationServices

AXActionConstants.hAdded [#def kAXShowAlternateUIAction](https://developer.apple.com/documentation/applicationservices/kaxshowalternateuiaction)Added [#def kAXShowDefaultUIAction](https://developer.apple.com/documentation/applicationservices/kaxshowdefaultuiaction)AXAttributeConstants.hAdded [AXMenuItemModifiers](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers)Added [kAXMenuItemModifierControl](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/1464333-control)Added [kAXMenuItemModifierNoCommand](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/1464506-nocommand)Added [kAXMenuItemModifierNone](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifiernone)Added [kAXMenuItemModifierOption](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/kaxmenuitemmodifieroption)Added [kAXMenuItemModifierShift](https://developer.apple.com/documentation/applicationservices/axmenuitemmodifiers/1461092-shift)AXNotificationConstants.hAdded [AXPriority](https://developer.apple.com/documentation/applicationservices/axpriority)Added [#def kAXAnnouncementKey](https://developer.apple.com/documentation/applicationservices/kaxannouncementkey)Added [#def kAXAnnouncementRequestedNotification](https://developer.apple.com/documentation/applicationservices/kaxannouncementrequestednotification)Added [#def kAXLayoutChangedNotification](https://developer.apple.com/documentation/applicationservices/kaxlayoutchangednotification)Added [kAXPriorityHigh](https://developer.apple.com/documentation/applicationservices/axpriority/high)Added [#def kAXPriorityKey](https://developer.apple.com/documentation/applicationservices/kaxprioritykey)Added [kAXPriorityLow](https://developer.apple.com/documentation/applicationservices/axpriority/low)Added [kAXPriorityMedium](https://developer.apple.com/documentation/applicationservices/axpriority/kaxprioritymedium)Added [#def kAXUIElementsKey](https://developer.apple.com/documentation/applicationservices/kaxuielementskey)AXRoleConstants.hAdded [#def kAXDescriptionListSubrole](https://developer.apple.com/documentation/applicationservices/kaxdescriptionlistsubrole)Added [#def kAXSwitchSubrole](https://developer.apple.com/documentation/applicationservices/kaxswitchsubrole)Added [#def kAXToggleSubrole](https://developer.apple.com/documentation/applicationservices/kaxtogglesubrole)AXTextAttributedString.hAdded [kAXMarkedMisspelledTextAttribute](https://developer.apple.com/documentation/applicationservices/kaxmarkedmisspelledtextattribute)AXUIElement.hAdded [AXIsProcessTrustedWithOptions()](https://developer.apple.com/documentation/applicationservices/1459186-axisprocesstrustedwithoptions)Added [AXObserverCallbackWithInfo](https://developer.apple.com/documentation/applicationservices/axobservercallbackwithinfo)Added [AXObserverCreateWithInfoCallback()](https://developer.apple.com/documentation/applicationservices/1460610-axobservercreatewithinfocallback)Added [kAXTrustedCheckOptionPrompt](https://developer.apple.com/documentation/applicationservices/kaxtrustedcheckoptionprompt)Modified [AXAPIEnabled()](https://developer.apple.com/documentation/applicationservices/1462072-axapienabled)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [AXMakeProcessTrusted()](https://developer.apple.com/documentation/applicationservices/1462083-axmakeprocesstrusted)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [AXUIElementPostKeyboardEvent()](https://developer.apple.com/documentation/applicationservices/1462057-axuielementpostkeyboardevent)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Accessibility.hAdded #def AX_ALLOW_OLD_SECURITY_METHODCGAffineTransform.hCGBase.hCGBitmapContext.hCGColor.hCGColorSpace.hCGContext.hCGDataConsumer.hCGDataProvider.hCGDirectDisplay.hCGDirectPalette.hCGDisplayConfiguration.hCGDisplayFade.hCGDisplayStream.hCGError.hCGEvent.hCGEventSource.hCGEventTypes.hCGFont.hCGFunction.hCGGLContext.hCGGeometry.hCGGradient.hCGImage.hCGLayer.hCGPDFArray.hCGPDFContentStream.hCGPDFContext.hCGPDFDictionary.hCGPDFDocument.hCGPDFObject.hCGPDFOperatorTable.hCGPDFPage.hCGPDFScanner.hCGPDFStream.hCGPDFString.hCGPSConverter.hCGPath.hCGPattern.hCGRemoteOperation.hCGSession.hCGShading.hCGWindow.hCGWindowLevel.hColorSyncBase.hModified #def CSEXPORT

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | ColorSync/ColorSyncBase.h |

Modified #def CSEXTERN

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | ColorSync/ColorSyncBase.h |

ColorSyncDeprecated.hModified [CM2Header](https://developer.apple.com/documentation/applicationservices/cm2header)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2Profile](https://developer.apple.com/documentation/applicationservices/cm2profile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2ProfileHandle](https://developer.apple.com/documentation/applicationservices/cm2profilehandle)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2ProfilePtr](https://developer.apple.com/documentation/applicationservices/cm2profileptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM4Header](https://developer.apple.com/documentation/applicationservices/cm4header)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMAdaptationMatrixType](https://developer.apple.com/documentation/applicationservices/cmadaptationmatrixtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMAppleProfileHeader](https://developer.apple.com/documentation/applicationservices/1560290-cmappleprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def CMBITMAPCALLBACKPROCPTR_DEFINED](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr_defined)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmap](https://developer.apple.com/documentation/applicationservices/cmbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapColorSpace](https://developer.apple.com/documentation/applicationservices/cmbitmapcolorspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBufferLocation](https://developer.apple.com/documentation/applicationservices/cmbufferlocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCMYColor](https://developer.apple.com/documentation/applicationservices/cmcmycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCMYKColor](https://developer.apple.com/documentation/applicationservices/cmcmykcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMCWInfoRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/cmchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCloneProfileRef()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804891-cmcloneprofileref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCloseProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804861-cmcloseprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMColor](https://developer.apple.com/documentation/applicationservices/1560453-cmcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatProfileSet](https://developer.apple.com/documentation/applicationservices/cmconcatprofileset)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertFixedXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805174-cmconvertfixedxyztoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertHLSToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805152-cmconverthlstorgb)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertHSVToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805160-cmconverthsvtorgb)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertLabToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805134-cmconvertlabtoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertLuvToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805140-cmconvertluvtoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMConvertRGBFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToGray()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805164-cmconvertrgbtogray)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToHLS()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805149-cmconvertrgbtohls)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToHSV()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805155-cmconvertrgbtohsv)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMConvertXYZFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToFixedXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805169-cmconvertxyztofixedxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToLab()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805133-cmconvertxyztolab)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToLuv()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805137-cmconvertxyztoluv)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805177-cmconvertxyztoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToYxy()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805142-cmconvertxyztoyxy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertYxyToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805146-cmconvertyxytoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804870-cmcopyprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileDescriptionString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805012-cmcopyprofiledescriptionstring)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileLocalizedString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805016-cmcopyprofilelocalizedstring)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805020-cmcopyprofilelocalizedstringdict)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCountImageProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805281-cmcountimageprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCountProfileElements()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804963-cmcountprofileelements)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCreateProfileIdentifier()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805369-cmcreateprofileidentifier)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCurveType](https://developer.apple.com/documentation/applicationservices/cmcurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDataType](https://developer.apple.com/documentation/applicationservices/cmdatatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDateTime](https://developer.apple.com/documentation/applicationservices/cmdatetime)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDateTimeType](https://developer.apple.com/documentation/applicationservices/cmdatetimetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceClass](https://developer.apple.com/documentation/applicationservices/cmdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceID](https://developer.apple.com/documentation/applicationservices/cmdeviceid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceInfo](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceInfoPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceinfoptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileArray](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilearray)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileArrayPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilearrayptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileID](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileInfo](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileScope](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilescope)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceScope](https://developer.apple.com/documentation/applicationservices/cmdevicescope)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceState](https://developer.apple.com/documentation/applicationservices/cmdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDisplayIDType](https://developer.apple.com/documentation/applicationservices/cmdisplayidtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDisposeProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805358-cmdisposeprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMEmbedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805269-cmembedimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMError](https://developer.apple.com/documentation/coremotion/cmerror)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMFileLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFixedXYColor](https://developer.apple.com/documentation/applicationservices/cmfixedxycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFixedXYZColor](https://developer.apple.com/documentation/applicationservices/cmfixedxyzcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenProcPtr](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804897-cmflattenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenUPP](https://developer.apple.com/documentation/applicationservices/cmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFloatBitmap](https://developer.apple.com/documentation/applicationservices/cmfloatbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFloatBitmapFlags](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMFloatBitmapMakeChunky()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetCWInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetColorSyncFolderSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804907-cmgetcolorsyncfolderspec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetColorSyncVersion()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805293-cmgetcolorsyncversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805235-cmgetdefaultdevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804940-cmgetdefaultprofilebyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804948-cmgetdefaultprofilebyuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805249-cmgetdevicedefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805240-cmgetdevicefactoryprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805260-cmgetdeviceinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805256-cmgetdeviceprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805245-cmgetdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805257-cmgetdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805289-cmgetgammabyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetImageSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805267-cmgetimagespace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805284-cmgetindimageprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805059-cmgetindnamedcolorvalue)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805002-cmgetindprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndProfileElementInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804996-cmgetindprofileelementinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorIndex()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805065-cmgetnamedcolorindex)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805047-cmgetnamedcolorinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorName()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805072-cmgetnamedcolorname)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805053-cmgetnamedcolorvalue)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRendering()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805202-cmgetps2colorrendering)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRenderingIntent()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805196-cmgetps2colorrenderingintent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRenderingVMSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805206-cmgetps2colorrenderingvmsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805191-cmgetps2colorspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804984-cmgetpartialprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPreferredCMM()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805182-cmgetpreferredcmm)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804955-cmgetprofilebyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805034-cmgetprofiledescriptions)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804973-cmgetprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804879-cmgetprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804885-cmgetprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileMD5()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804876-cmgetprofilemd5)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileRefCount()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804894-cmgetprofilerefcount)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetScriptProfileDescription()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805029-cmgetscriptprofiledescription)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804926-cmgetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGrayColor](https://developer.apple.com/documentation/applicationservices/cmgraycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHLSColor](https://developer.apple.com/documentation/applicationservices/cmhlscolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHSVColor](https://developer.apple.com/documentation/applicationservices/cmhsvcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHandleLocation](https://developer.apple.com/documentation/applicationservices/cmhandlelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMHeader

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMIString

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIntentCRDVMSize](https://developer.apple.com/documentation/applicationservices/cmintentcrdvmsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateCMMInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805185-cmiteratecmminfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateColorDevices()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805262-cmiteratecolordevices)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateColorSyncFolder()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceInfoProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceinfoprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceProfileProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceprofileprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805263-cmiteratedeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLabColor](https://developer.apple.com/documentation/applicationservices/cmlabcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLabToLabProcPtr](https://developer.apple.com/documentation/applicationservices/cmlabtolabprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLaunchControlPanel()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805294-cmlaunchcontrolpanel)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLinkImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805278-cmlinkimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLut16Type](https://developer.apple.com/documentation/applicationservices/cmlut16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLut8Type](https://developer.apple.com/documentation/applicationservices/cmlut8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLuvColor](https://developer.apple.com/documentation/applicationservices/cmluvcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMInfo](https://developer.apple.com/documentation/applicationservices/cmminfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMInfoRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmmiterateprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMIterateUPP](https://developer.apple.com/documentation/applicationservices/cmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CheckBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CheckColors()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_ConcatColorWorld()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CreateLinkProfile()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_GetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchColors()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_ValidateProfile()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeAndModel](https://developer.apple.com/documentation/applicationservices/cmmakeandmodel)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeAndModelType](https://developer.apple.com/documentation/applicationservices/cmmakeandmodeltype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804920-cmmakeprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchFlag

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMatchImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805273-cmmatchimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchOption

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchRef

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMeasurementType](https://developer.apple.com/documentation/applicationservices/cmmeasurementtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctCLUTType](https://developer.apple.com/documentation/applicationservices/cmmultifunctcluttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutA2BType](https://developer.apple.com/documentation/applicationservices/cmmultifunctluta2btype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutB2AType](https://developer.apple.com/documentation/applicationservices/cmmultifunctlutb2atype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutType](https://developer.apple.com/documentation/applicationservices/cmmultifunctluttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiLocalizedUniCodeEntryRec](https://developer.apple.com/documentation/applicationservices/cmmultilocalizedunicodeentryrec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiLocalizedUniCodeType](https://developer.apple.com/documentation/applicationservices/cmmultilocalizedunicodetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel5Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel5color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel6Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel6color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel7Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel7color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel8Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel8color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor](https://developer.apple.com/documentation/applicationservices/cmnamedcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor2EntryType](https://developer.apple.com/documentation/applicationservices/cmnamedcolor2entrytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor2Type](https://developer.apple.com/documentation/applicationservices/cmnamedcolor2type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColorType](https://developer.apple.com/documentation/applicationservices/cmnamedcolortype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNativeDisplayInfo](https://developer.apple.com/documentation/applicationservices/cmnativedisplayinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNativeDisplayInfoType](https://developer.apple.com/documentation/applicationservices/cmnativedisplayinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNewProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804911-cmnewprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNewProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805344-cmnewprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMOpenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804853-cmopenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMPS2CRDVMSizeType](https://developer.apple.com/documentation/applicationservices/cmps2crdvmsizetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMParametricCurveType](https://developer.apple.com/documentation/applicationservices/cmparametriccurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMPathLocation](https://developer.apple.com/documentation/applicationservices/cmpathlocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProcedureLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfLoc](https://developer.apple.com/documentation/applicationservices/1560460-cmprofloc)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileAccessProcPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileAccessUPP

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileChromaticities

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileCopyICCData()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileElementExists()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804967-cmprofileelementexists)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileFilterProcPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileFilterUPP

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileHandle

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileIdentifier

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIdentifierFolderSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805374-cmprofileidentifierfoldersearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIdentifierListSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805376-cmprofileidentifierlistsearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileIdentifierPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateData](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmprofileiterateprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateUPP](https://developer.apple.com/documentation/applicationservices/cmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileLocation](https://developer.apple.com/documentation/applicationservices/cmprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileMD5](https://developer.apple.com/documentation/applicationservices/cmprofilemd5)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileMD5AreEqual()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileMD5Ptr](https://developer.apple.com/documentation/applicationservices/cmprofilemd5ptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileModified()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804872-cmprofilemodified)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfilePtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileRef](https://developer.apple.com/documentation/applicationservices/cmprofileref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecordHandle

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecordPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRef

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileSequenceDescType](https://developer.apple.com/documentation/applicationservices/cmprofilesequencedesctype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProofImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805276-cmproofimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMPtrLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRGBColor](https://developer.apple.com/documentation/applicationservices/cmrgbcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRegisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805231-cmregistercolordevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRemoveProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805008-cmremoveprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMS15Fixed16ArrayType](https://developer.apple.com/documentation/applicationservices/cms15fixed16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMScreeningChannelRec](https://developer.apple.com/documentation/applicationservices/cmscreeningchannelrec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMScreeningType](https://developer.apple.com/documentation/applicationservices/cmscreeningtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSearchGetIndProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805362-cmsearchgetindprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSearchGetIndProfileFileSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805365-cmsearchgetindprofilefilespec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMSearchRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805238-cmsetdefaultdevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804944-cmsetdefaultprofilebyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804951-cmsetdefaultprofilebyuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805251-cmsetdevicedefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805241-cmsetdevicefactoryprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805253-cmsetdeviceprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805247-cmsetdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805258-cmsetdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805291-cmsetgammabyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805286-cmsetindimageprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804989-cmsetpartialprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMSetPreferredCMM()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804959-cmsetprofilebyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805039-cmsetprofiledescriptions)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804977-cmsetprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElementReference()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805005-cmsetprofileelementreference)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElementSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804980-cmsetprofileelementsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804882-cmsetprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805025-cmsetprofilelocalizedstringdicti)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804932-cmsetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSignatureType](https://developer.apple.com/documentation/applicationservices/cmsignaturetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTagElemTable](https://developer.apple.com/documentation/applicationservices/cmtagelemtable)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTagRecord](https://developer.apple.com/documentation/applicationservices/cmtagrecord)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTextDescriptionType](https://developer.apple.com/documentation/applicationservices/cmtextdescriptiontype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTextType](https://developer.apple.com/documentation/applicationservices/cmtexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMU16Fixed16ArrayType](https://developer.apple.com/documentation/applicationservices/cmu16fixed16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt16ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt32ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint32arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt64ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint64arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt8ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint8arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUcrBgType](https://developer.apple.com/documentation/applicationservices/cmucrbgtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnembedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805271-cmunembedimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnicodeTextType](https://developer.apple.com/documentation/applicationservices/cmunicodetexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnregisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805234-cmunregistercolordevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUpdateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804864-cmupdateprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUpdateProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805356-cmupdateprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMValidImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805264-cmvalidimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMValidateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804856-cmvalidateprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGamma](https://developer.apple.com/documentation/applicationservices/cmvideocardgamma)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaFormula](https://developer.apple.com/documentation/applicationservices/cmvideocardgammaformula)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaTable](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatable)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaType](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMViewingConditionsType](https://developer.apple.com/documentation/applicationservices/cmviewingconditionstype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMWorldRef](https://developer.apple.com/documentation/applicationservices/cmworldref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZColor](https://developer.apple.com/documentation/applicationservices/cmxyzcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZComponent](https://developer.apple.com/documentation/applicationservices/cmxyzcomponent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZType](https://developer.apple.com/documentation/applicationservices/cmxyztype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMYxyColor](https://developer.apple.com/documentation/applicationservices/cmyxycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified #def CSEXPORT

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | ColorSync/ColorSyncBase.h |

Modified #def CSEXTERN

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | ColorSync/ColorSyncBase.h |

Modified [CS_MAX_PATH](https://developer.apple.com/documentation/applicationservices/cs_max_path)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWCheckBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805121-cwcheckbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWCheckColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805111-cwcheckcolors)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWColorWorldGetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWColorWorldSetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805087-cwconcatcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWDisposeColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805102-cwdisposecolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWFillLookupTexture()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805126-cwfilllookuptexture)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWGetCMMSignature()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWMatchBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805116-cwmatchbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWMatchColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805108-cwmatchcolors)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804915-cwnewlinkprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805300-disposecmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805310-disposecmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805318-disposecmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805323-disposecmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805329-disposecmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805337-disposecmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805341-disposecmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805303-invokecmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805312-invokecmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805320-invokecmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805333-invokecmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805338-invokecmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805343-invokecmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMConcatProfileSet](https://developer.apple.com/documentation/applicationservices/ncmconcatprofileset)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMConcatProfileSpec](https://developer.apple.com/documentation/applicationservices/ncmconcatprofilespec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMDeviceProfileInfo](https://developer.apple.com/documentation/applicationservices/ncmdeviceprofileinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804889-ncmgetprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804936-ncmsetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMUnflattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804901-ncmunflattenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805091-ncwconcatcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWNewColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805079-ncwnewcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804918-ncwnewlinkprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805297-newcmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805306-newcmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805315-newcmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805322-newcmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805327-newcmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805336-newcmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805339-newcmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm10CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm10clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm11CLRData](https://developer.apple.com/documentation/applicationservices/cm11clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm12CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm12clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm13CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm13clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm14CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm14clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm15CLRData](https://developer.apple.com/documentation/applicationservices/cm15clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm16_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm16_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm24_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm24_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_16ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm32_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_32ColorPacking](https://developer.apple.com/documentation/applicationservices/cm32_32colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm32_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm3CLRData](https://developer.apple.com/documentation/applicationservices/cm3clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm40_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm40_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm48_16ColorPacking](https://developer.apple.com/documentation/applicationservices/cm48_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm48_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm48_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm4CLRData](https://developer.apple.com/documentation/applicationservices/cm4clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm56_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm56_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm5CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm5clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm64_16ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm64_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm64_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm64_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm6CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm6clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm7CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm7clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm8CLRData](https://developer.apple.com/documentation/applicationservices/cm8clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm8_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm8_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm9CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm9clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64LPmulSpace](https://developer.apple.com/documentation/applicationservices/cmargb64lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64PmulSpace](https://developer.apple.com/documentation/applicationservices/cmargb64pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64Space](https://developer.apple.com/documentation/applicationservices/cmargb64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB0Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmatob0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmatob1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB2Tag](https://developer.apple.com/documentation/applicationservices/cmatob2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbortWriteAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmabortwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbsoluteColorimetric](https://developer.apple.com/documentation/applicationservices/cmabsolutecolorimetric)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbstractClass](https://developer.apple.com/documentation/applicationservices/cmabstractclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaFirstPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmalphafirstpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaLastPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmalphalastpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmalphapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmalphaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAsciiData](https://developer.apple.com/documentation/applicationservices/1560593-data_type_element_values/cmasciidata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA0Tag](https://developer.apple.com/documentation/applicationservices/cmbtoa0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmbtoa1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA2Tag](https://developer.apple.com/documentation/applicationservices/cmbtoa2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBeginAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmbeginaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBeginProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBeginProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBestMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmbestmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBgResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBinaryData](https://developer.apple.com/documentation/applicationservices/cmbinarydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlackPointCompensation](https://developer.apple.com/documentation/applicationservices/cmblackpointcompensation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlackPointCompensationMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmblackpointcompensationmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlueColorantTag](https://developer.apple.com/documentation/applicationservices/cmbluecoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBlueResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlueTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmbluetrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBradfordChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/cmbradfordchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBufferBasedProfile](https://developer.apple.com/documentation/applicationservices/cmbufferbasedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMSReservedFlagsMask](https://developer.apple.com/documentation/applicationservices/cmcmsreservedflagsmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYData](https://developer.apple.com/documentation/applicationservices/cmcmydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK64Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYKData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmcmykdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYKSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmcmykspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1ChromTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1chromtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1CustTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1custtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1NameTag](https://developer.apple.com/documentation/applicationservices/cmcs1nametag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1ProfileVersion](https://developer.apple.com/documentation/applicationservices/cmcs1profileversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1TRCTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1trctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS2ProfileVersion](https://developer.apple.com/documentation/applicationservices/cmcs2profileversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCalibrationDateTimeTag](https://developer.apple.com/documentation/applicationservices/cmcalibrationdatetimetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCameraDeviceClass](https://developer.apple.com/documentation/applicationservices/cmcameradeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCharTargetTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmchartargettag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmChromaticAdaptationTag](https://developer.apple.com/documentation/applicationservices/cmchromaticadaptationtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCloseAccess](https://developer.apple.com/documentation/applicationservices/cmcloseaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCloseSpool](https://developer.apple.com/documentation/applicationservices/cmclosespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacealphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceClass](https://developer.apple.com/documentation/applicationservices/cmcolorspaceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceEncodingMask](https://developer.apple.com/documentation/applicationservices/cmcolorspaceencodingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpacePackingMask](https://developer.apple.com/documentation/applicationservices/cmcolorspacepackingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpacePremulAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacepremulalphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceReservedMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacereservedmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceSpaceAndAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacespaceandalphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceSpaceMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacespacemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmColorimetricMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmComment

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmContinueProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCopyrightTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmcopyrighttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCreateNewAccess](https://developer.apple.com/documentation/applicationservices/cmcreatenewaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentDeviceInfoVersion](https://developer.apple.com/documentation/applicationservices/1560146-current_info_versions/cmcurrentdeviceinfoversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileInfoVersion](https://developer.apple.com/documentation/applicationservices/1560146-current_info_versions/cmcurrentprofileinfoversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileLocationSize](https://developer.apple.com/documentation/applicationservices/cmcurrentprofilelocationsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileMajorVersion](https://developer.apple.com/documentation/applicationservices/1560659-current_major_version_mask/cmcurrentprofilemajorversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmCyanResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDefaultDeviceID](https://developer.apple.com/documentation/applicationservices/cmdefaultdeviceid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDefaultProfileID](https://developer.apple.com/documentation/applicationservices/1560386-default_ids/cmdefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceAlreadyRegistered](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmdevicealreadyregistered)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceDBNotFoundErr](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmdevicedbnotfounderr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceInfoVersion1](https://developer.apple.com/documentation/applicationservices/cmdeviceinfoversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceMfgDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmdevicemfgdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceModelDescTag](https://developer.apple.com/documentation/applicationservices/cmdevicemodeldesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceNotRegistered](https://developer.apple.com/documentation/applicationservices/cmdevicenotregistered)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfileInfoVersion1](https://developer.apple.com/documentation/applicationservices/1560472-current_device_versions/cmdeviceprofileinfoversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfileInfoVersion2](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileinfoversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfilesNotFound](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilesnotfound)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateAppleRsvdBits](https://developer.apple.com/documentation/applicationservices/cmdevicestateapplersvdbits)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateBusy](https://developer.apple.com/documentation/applicationservices/cmdevicestatebusy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateDefault](https://developer.apple.com/documentation/applicationservices/cmdevicestatedefault)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateDeviceRsvdBits](https://developer.apple.com/documentation/applicationservices/cmdevicestatedevicersvdbits)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateForceNotify](https://developer.apple.com/documentation/applicationservices/cmdevicestateforcenotify)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateOffline](https://developer.apple.com/documentation/applicationservices/cmdevicestateoffline)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmDisableMatching

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayClass](https://developer.apple.com/documentation/applicationservices/cmdisplayclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayDeviceClass](https://developer.apple.com/documentation/applicationservices/cmdisplaydeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayUse](https://developer.apple.com/documentation/applicationservices/cmdisplayuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDraftMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmdraftmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEmbedProfileIdentifier

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEmbedWholeProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmembeddedmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedProfile](https://developer.apple.com/documentation/applicationservices/cmembeddedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedUse](https://developer.apple.com/documentation/applicationservices/cmembeddeduse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedUseMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmembeddedusemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEnableMatching

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEndAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmendaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEndProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEndProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmFileBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmFlare0](https://developer.apple.com/documentation/applicationservices/1560283-measurement_flares/cmflare0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmFlare100](https://developer.apple.com/documentation/applicationservices/1560283-measurement_flares/cmflare100)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutCheckingMask](https://developer.apple.com/documentation/applicationservices/cmgamutcheckingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutResult1Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgamutresult1space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutResultSpace](https://developer.apple.com/documentation/applicationservices/cmgamutresultspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgamuttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometry045or450](https://developer.apple.com/documentation/applicationservices/cmgeometry045or450)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometry0dord0](https://developer.apple.com/documentation/applicationservices/1560539-measurement_geometries/cmgeometry0dord0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometryUnknown](https://developer.apple.com/documentation/applicationservices/1560539-measurement_geometries/cmgeometryunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGlossy](https://developer.apple.com/documentation/applicationservices/1560327-device_and_media_attributes/cmglossy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGlossyMatteMask](https://developer.apple.com/documentation/applicationservices/1560447-x_profiles/cmglossymattemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray16LSpace](https://developer.apple.com/documentation/applicationservices/cmgray16lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgray16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray8Space](https://developer.apple.com/documentation/applicationservices/cmgray8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA16PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya16pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32LPmulSpace](https://developer.apple.com/documentation/applicationservices/cmgraya32lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya32lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32Space](https://developer.apple.com/documentation/applicationservices/cmgraya32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayAPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmgrayapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayASpace](https://developer.apple.com/documentation/applicationservices/cmgrayaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmgraydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmGrayResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGraySpace](https://developer.apple.com/documentation/applicationservices/cmgrayspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayTRCTag](https://developer.apple.com/documentation/applicationservices/cmgraytrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGreenColorantTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgreencoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmGreenResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGreenTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgreentrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLS32Space](https://developer.apple.com/documentation/applicationservices/cmhls32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLSData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmhlsdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLSSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmhlsspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSV32Space](https://developer.apple.com/documentation/applicationservices/cmhsv32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSVData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmhsvdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSVSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmhsvspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmHandleBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion2](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion21](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion21)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion4](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCReservedFlagsMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmiccreservedflagsmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantA](https://developer.apple.com/documentation/applicationservices/cmilluminanta)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD50](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd50)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD55](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd55)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD65](https://developer.apple.com/documentation/applicationservices/cmilluminantd65)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD93](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd93)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantEquiPower](https://developer.apple.com/documentation/applicationservices/cmilluminantequipower)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantF2](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantf2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantF8](https://developer.apple.com/documentation/applicationservices/cmilluminantf8)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantUnknown](https://developer.apple.com/documentation/applicationservices/cmilluminantunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInputClass](https://developer.apple.com/documentation/applicationservices/cminputclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInputUse](https://developer.apple.com/documentation/applicationservices/cminputuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInternalCFErr](https://developer.apple.com/documentation/applicationservices/cminternalcferr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInterpolationMask](https://developer.apple.com/documentation/applicationservices/cminterpolationmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateAllDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratealldeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateCurrentDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecurrentdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateCustomDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecustomdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateDeviceProfilesMask](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceprofilesmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateFactoryDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratefactorydeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB48LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB48Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLABSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmlabspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLUV32Space](https://developer.apple.com/documentation/applicationservices/cmluv32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLUVSpace](https://developer.apple.com/documentation/applicationservices/cmluvspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLabData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmlabdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinearChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmlinearchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinesPer](https://developer.apple.com/documentation/applicationservices/1560247-screen_encoding_tags/cmlinesper)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinkClass](https://developer.apple.com/documentation/applicationservices/cmlinkclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLittleEndianPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmlittleendianpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLong10ColorPacking](https://developer.apple.com/documentation/applicationservices/cmlong10colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLong8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmlong8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLuminanceTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmluminancetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLuvData](https://developer.apple.com/documentation/applicationservices/cmluvdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCEight8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmceight8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCEightSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmceightspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCFive8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmcfive8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCFiveSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcfivespace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH5Data](https://developer.apple.com/documentation/applicationservices/cmmch5data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH6Data](https://developer.apple.com/documentation/applicationservices/cmmch6data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH7Data](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmmch7data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH8Data](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmmch8data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSeven8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmcseven8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSevenSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcsevenspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSix8Space](https://developer.apple.com/documentation/applicationservices/cmmcsix8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSixSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcsixspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMacintosh](https://developer.apple.com/documentation/applicationservices/cmmacintosh)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMagentaResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMagicNumber](https://developer.apple.com/documentation/applicationservices/1560690-magic_cookie_number/cmmagicnumber)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMakeAndModelTag](https://developer.apple.com/documentation/applicationservices/cmmakeandmodeltag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchAnyProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchApplProfileVersion

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchAttributes

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchBlack

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchCMMType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDataColorSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDataType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceAttributes

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceManufacturer

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceModel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchFlags

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchManufacturer

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchModel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchOptions

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileCMMType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileClass

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileConnectionSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileFlags

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchWhite

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMeasurementTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmmeasurementtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMediaBlackPointTag](https://developer.apple.com/documentation/applicationservices/cmmediablackpointtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMediaWhitePointTag](https://developer.apple.com/documentation/applicationservices/cmmediawhitepointtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMicrosoft](https://developer.apple.com/documentation/applicationservices/cmmicrosoft)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMonitorDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColor2Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmnamedcolor2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColorClass](https://developer.apple.com/documentation/applicationservices/1560630-profile_classes/cmnamedcolorclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColorTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmnamedcolortag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmnameddata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexed32LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmnamedindexed32lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexed32Space](https://developer.apple.com/documentation/applicationservices/cmnamedindexed32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexedSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmnamedindexedspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNativeDisplayInfoTag](https://developer.apple.com/documentation/applicationservices/1560164-video_card_gamma_tags/cmnativedisplayinfotag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmNativeMatchingPreferred

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmnocolorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoProfileBase](https://developer.apple.com/documentation/applicationservices/1560599-profile_location_type/cmnoprofilebase)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoSpace](https://developer.apple.com/documentation/applicationservices/cmnospace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNormalMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmnormalmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNumHeaderElements](https://developer.apple.com/documentation/applicationservices/1560086-tag_type_information/cmnumheaderelements)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOneBitDirectPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmonebitdirectpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmOnePlusLastResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenReadAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmopenreadaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenReadSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmopenreadspool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenWriteAccess](https://developer.apple.com/documentation/applicationservices/cmopenwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenWriteSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmopenwritespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOriginalProfileLocationSize](https://developer.apple.com/documentation/applicationservices/1560369-profile_location_sizes/cmoriginalprofilelocationsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOutputClass](https://developer.apple.com/documentation/applicationservices/1560630-profile_classes/cmoutputclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOutputUse](https://developer.apple.com/documentation/applicationservices/1560730-use_types/cmoutputuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD0Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmps2crd0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD1Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD2Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD3Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd3tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRDVMSizeTag](https://developer.apple.com/documentation/applicationservices/cmps2crdvmsizetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CSATag](https://developer.apple.com/documentation/applicationservices/cmps2csatag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2RenderingIntentTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmps2renderingintenttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS7bit](https://developer.apple.com/documentation/applicationservices/1560551-postscript_data_formats/cmps7bit)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS8bit](https://developer.apple.com/documentation/applicationservices/1560551-postscript_data_formats/cmps8bit)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType0](https://developer.apple.com/documentation/applicationservices/cmparametrictype0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType1](https://developer.apple.com/documentation/applicationservices/cmparametrictype1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType2](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType3](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype3)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType4](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPathBasedProfile](https://developer.apple.com/documentation/applicationservices/cmpathbasedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPerceptual](https://developer.apple.com/documentation/applicationservices/1560278-x_profiles/cmperceptual)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPerceptualMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrefsSynchError](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmprefssyncherror)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview0Tag](https://developer.apple.com/documentation/applicationservices/cmpreview0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmpreview1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview2Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmpreview2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPrinterDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrinterDeviceClass](https://developer.apple.com/documentation/applicationservices/cmprinterdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmProcedureBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileDescriptionMLTag](https://developer.apple.com/documentation/applicationservices/cmprofiledescriptionmltag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileDescriptionTag](https://developer.apple.com/documentation/applicationservices/cmprofiledescriptiontag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmProfileIdentifierSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion1](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedataversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion2](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedataversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion3](https://developer.apple.com/documentation/applicationservices/1560189-profile_iteration_constants/cmprofileiteratedataversion3)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion4](https://developer.apple.com/documentation/applicationservices/1560189-profile_iteration_constants/cmprofileiteratedataversion4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileMajorVersionMask](https://developer.apple.com/documentation/applicationservices/cmprofilemajorversionmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileSequenceDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmprofilesequencedesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProofDeviceClass](https://developer.apple.com/documentation/applicationservices/cmproofdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProofUse](https://developer.apple.com/documentation/applicationservices/1560730-use_types/cmproofuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrtrDefaultScreens](https://developer.apple.com/documentation/applicationservices/1560247-screen_encoding_tags/cmprtrdefaultscreens)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPtrBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmQualityMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmqualitymask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB16LSpace](https://developer.apple.com/documentation/applicationservices/cmrgb16lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB32Space](https://developer.apple.com/documentation/applicationservices/cmrgb32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB48LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB48Space](https://developer.apple.com/documentation/applicationservices/cmrgb48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB565LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb565lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB565Space](https://developer.apple.com/documentation/applicationservices/cmrgb565space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64LPmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64PmulSpace](https://developer.apple.com/documentation/applicationservices/cmrgba64pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBAPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBASpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmrgbdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReadAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmreadaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReadSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmreadspool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRedColorantTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmredcoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmRedResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRedTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmredtrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReflective](https://developer.apple.com/documentation/applicationservices/1560327-device_and_media_attributes/cmreflective)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReflectiveTransparentMask](https://developer.apple.com/documentation/applicationservices/1560447-x_profiles/cmreflectivetransparentmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRelativeColorimetric](https://developer.apple.com/documentation/applicationservices/1560278-x_profiles/cmrelativecolorimetric)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReservedSpace1](https://developer.apple.com/documentation/applicationservices/cmreservedspace1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReservedSpace2](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmreservedspace2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReverseChannelPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmreversechannelpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSRGB16ChannelEncoding](https://developer.apple.com/documentation/applicationservices/cmsrgb16channelencoding)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSRGBData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmsrgbdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSaturation](https://developer.apple.com/documentation/applicationservices/cmsaturation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmSaturationMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmScannerDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScannerDeviceClass](https://developer.apple.com/documentation/applicationservices/cmscannerdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScreeningDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmscreeningdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScreeningTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmscreeningtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigCrdInfoType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigcrdinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigCurveType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigcurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigDataType](https://developer.apple.com/documentation/applicationservices/cmsigdatatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigDateTimeType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigdatetimetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigLut16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiglut16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigLut8Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiglut8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMakeAndModelType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigmakeandmodeltype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMeasurementType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigmeasurementtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiFunctA2BType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigmultifuncta2btype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiFunctB2AType](https://developer.apple.com/documentation/applicationservices/cmsigmultifunctb2atype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiLocalizedUniCodeType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigmultilocalizedunicodetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNamedColor2Type](https://developer.apple.com/documentation/applicationservices/cmsignamedcolor2type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNamedColorType](https://developer.apple.com/documentation/applicationservices/cmsignamedcolortype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNativeDisplayInfoType](https://developer.apple.com/documentation/applicationservices/cmsignativedisplayinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigPS2CRDVMSizeType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigps2crdvmsizetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigParametricCurveType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigparametriccurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigProfileDescriptionType](https://developer.apple.com/documentation/applicationservices/cmsigprofiledescriptiontype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigProfileSequenceDescType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigprofilesequencedesctype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigS15Fixed16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigs15fixed16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigScreeningType](https://developer.apple.com/documentation/applicationservices/cmsigscreeningtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigSignatureType](https://developer.apple.com/documentation/applicationservices/cmsigsignaturetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigTextType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigtexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigU16Fixed16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigu16fixed16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigU1Fixed15Type](https://developer.apple.com/documentation/applicationservices/cmsigu1fixed15type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt16Type](https://developer.apple.com/documentation/applicationservices/cmsiguint16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt32Type](https://developer.apple.com/documentation/applicationservices/cmsiguint32type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt64Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiguint64type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt8Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiguint8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUcrBgType](https://developer.apple.com/documentation/applicationservices/cmsigucrbgtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUnicodeTextType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigunicodetexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigVideoCardGammaType](https://developer.apple.com/documentation/applicationservices/cmsigvideocardgammatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigViewingConditionsType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigviewingconditionstype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigXYZType](https://developer.apple.com/documentation/applicationservices/cmsigxyztype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSiliconGraphics](https://developer.apple.com/documentation/applicationservices/cmsilicongraphics)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSolaris](https://developer.apple.com/documentation/applicationservices/1560191-platform_enumeration_values/cmsolaris)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionCross](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctioncross)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionDefault](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctiondefault)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionDiamond](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctiondiamond)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionEllipse](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionellipse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionLine](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionline)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionRound](https://developer.apple.com/documentation/applicationservices/cmspotfunctionround)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionSquare](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionsquare)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionUnknown](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobs1931TwoDegrees](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobs1931twodegrees)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobs1964TenDegrees](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobs1964tendegrees)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobsUnknown](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobsunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTaligent](https://developer.apple.com/documentation/applicationservices/1560191-platform_enumeration_values/cmtaligent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyAMDisplay](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyamdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyCRTDisplay](https://developer.apple.com/documentation/applicationservices/cmtechnologycrtdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyDigitalCamera](https://developer.apple.com/documentation/applicationservices/cmtechnologydigitalcamera)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyDyeSublimationPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologydyesublimationprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyElectrophotographicPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyelectrophotographicprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyElectrostaticPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyelectrostaticprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFilmScanner](https://developer.apple.com/documentation/applicationservices/cmtechnologyfilmscanner)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFilmWriter](https://developer.apple.com/documentation/applicationservices/cmtechnologyfilmwriter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFlexography](https://developer.apple.com/documentation/applicationservices/cmtechnologyflexography)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyGravure](https://developer.apple.com/documentation/applicationservices/cmtechnologygravure)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyInkJetPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyinkjetprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyOffsetLithography](https://developer.apple.com/documentation/applicationservices/cmtechnologyoffsetlithography)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPMDisplay](https://developer.apple.com/documentation/applicationservices/cmtechnologypmdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotoCD](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyphotocd)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotoImageSetter](https://developer.apple.com/documentation/applicationservices/cmtechnologyphotoimagesetter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotographicPaperPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyphotographicpaperprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyProjectionTelevision](https://developer.apple.com/documentation/applicationservices/cmtechnologyprojectiontelevision)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyReflectiveScanner](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyreflectivescanner)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologySilkscreen](https://developer.apple.com/documentation/applicationservices/cmtechnologysilkscreen)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmtechnologytag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyThermalWaxPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologythermalwaxprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyVideoCamera](https://developer.apple.com/documentation/applicationservices/cmtechnologyvideocamera)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyVideoMonitor](https://developer.apple.com/documentation/applicationservices/cmtechnologyvideomonitor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBX16

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBX8

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBXFloat32

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTurnOffCache

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmUcrBgTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmucrbgtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmUcrResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmUseDefaultChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmusedefaultchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaFormulaType](https://developer.apple.com/documentation/applicationservices/1560344-video_card_gamma_storage_types/cmvideocardgammaformulatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaTableType](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatabletype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaTag](https://developer.apple.com/documentation/applicationservices/1560164-video_card_gamma_tags/cmvideocardgammatag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmViewingConditionsDescTag](https://developer.apple.com/documentation/applicationservices/cmviewingconditionsdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmViewingConditionsTag](https://developer.apple.com/documentation/applicationservices/cmviewingconditionstag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVonKriesChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmvonkrieschromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWord565ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmword565colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWord5ColorPacking](https://developer.apple.com/documentation/applicationservices/cmword5colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWriteAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWriteSpool](https://developer.apple.com/documentation/applicationservices/cmwritespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ48LSpace](https://developer.apple.com/documentation/applicationservices/cmxyz48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ48Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmxyzdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmxyzspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYCbCrData](https://developer.apple.com/documentation/applicationservices/cmycbcrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYXY32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmyxy32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYXYSpace](https://developer.apple.com/documentation/applicationservices/cmyxyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmYellowResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYxyData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmyxydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspFavorEmbeddedMask

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidImageFile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidImageSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileDest

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileEmbed

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileLink

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileProof

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileSource

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDefaultDeviceNotification](https://developer.apple.com/documentation/applicationservices/kcmdefaultdevicenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDefaultDeviceProfileNotification](https://developer.apple.com/documentation/applicationservices/kcmdefaultdeviceprofilenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceOfflineNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceofflinenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceOnlineNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceonlinenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceProfilesNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceprofilesnotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceRegisteredNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceregisterednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceStateNotification](https://developer.apple.com/documentation/applicationservices/kcmdevicestatenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceUnregisteredNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceunregisterednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDisplayDeviceProfilesNotification](https://developer.apple.com/documentation/applicationservices/kcmdisplaydeviceprofilesnotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsAlpha](https://developer.apple.com/documentation/applicationservices/kcmfloatbitmapflagsalpha)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsAlphaPremul](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags/kcmfloatbitmapflagsalphapremul)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsNone](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags/kcmfloatbitmapflagsnone)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsRangeClipped](https://developer.apple.com/documentation/applicationservices/kcmfloatbitmapflagsrangeclipped)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified kCMIlluminantD50

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified kCMIlluminantD65

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMPrefsChangedNotification](https://developer.apple.com/documentation/applicationservices/kcmprefschangednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kDefaultCMMSignature](https://developer.apple.com/documentation/applicationservices/kdefaultcmmsignature)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kDeviceToPCS](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kdevicetopcs)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kNoTransform](https://developer.apple.com/documentation/applicationservices/knotransform)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kPCSToDevice](https://developer.apple.com/documentation/applicationservices/kpcstodevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kPCSToPCS](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kpcstopcs)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseAtoB](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kuseatob)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseBtoA](https://developer.apple.com/documentation/applicationservices/kusebtoa)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseBtoB](https://developer.apple.com/documentation/applicationservices/kusebtob)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseProfileIntent](https://developer.apple.com/documentation/applicationservices/kuseprofileintent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

ColorSyncDeprecated.hModified [CM2Header](https://developer.apple.com/documentation/applicationservices/cm2header)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2Profile](https://developer.apple.com/documentation/applicationservices/cm2profile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2ProfileHandle](https://developer.apple.com/documentation/applicationservices/cm2profilehandle)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM2ProfilePtr](https://developer.apple.com/documentation/applicationservices/cm2profileptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CM4Header](https://developer.apple.com/documentation/applicationservices/cm4header)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMAdaptationMatrixType](https://developer.apple.com/documentation/applicationservices/cmadaptationmatrixtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMAppleProfileHeader](https://developer.apple.com/documentation/applicationservices/1560290-cmappleprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def CMBITMAPCALLBACKPROCPTR_DEFINED](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr_defined)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmap](https://developer.apple.com/documentation/applicationservices/cmbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBitmapColorSpace](https://developer.apple.com/documentation/applicationservices/cmbitmapcolorspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMBufferLocation](https://developer.apple.com/documentation/applicationservices/cmbufferlocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCMYColor](https://developer.apple.com/documentation/applicationservices/cmcmycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCMYKColor](https://developer.apple.com/documentation/applicationservices/cmcmykcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMCWInfoRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/cmchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCloneProfileRef()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804891-cmcloneprofileref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCloseProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804861-cmcloseprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMColor](https://developer.apple.com/documentation/applicationservices/1560453-cmcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatCallBackProcPtr](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatCallBackUPP](https://developer.apple.com/documentation/applicationservices/cmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConcatProfileSet](https://developer.apple.com/documentation/applicationservices/cmconcatprofileset)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertFixedXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805174-cmconvertfixedxyztoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertHLSToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805152-cmconverthlstorgb)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertHSVToRGB()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805160-cmconverthsvtorgb)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertLabToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805134-cmconvertlabtoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertLuvToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805140-cmconvertluvtoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMConvertRGBFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToGray()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805164-cmconvertrgbtogray)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToHLS()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805149-cmconvertrgbtohls)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertRGBToHSV()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805155-cmconvertrgbtohsv)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMConvertXYZFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToFixedXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805169-cmconvertxyztofixedxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToLab()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805133-cmconvertxyztolab)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToLuv()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805137-cmconvertxyztoluv)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805177-cmconvertxyztoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertXYZToYxy()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805142-cmconvertxyztoyxy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMConvertYxyToXYZ()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805146-cmconvertyxytoxyz)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804870-cmcopyprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileDescriptionString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805012-cmcopyprofiledescriptionstring)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileLocalizedString()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805016-cmcopyprofilelocalizedstring)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCopyProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805020-cmcopyprofilelocalizedstringdict)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCountImageProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805281-cmcountimageprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCountProfileElements()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804963-cmcountprofileelements)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCreateProfileIdentifier()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805369-cmcreateprofileidentifier)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMCurveType](https://developer.apple.com/documentation/applicationservices/cmcurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDataType](https://developer.apple.com/documentation/applicationservices/cmdatatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDateTime](https://developer.apple.com/documentation/applicationservices/cmdatetime)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDateTimeType](https://developer.apple.com/documentation/applicationservices/cmdatetimetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceClass](https://developer.apple.com/documentation/applicationservices/cmdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceID](https://developer.apple.com/documentation/applicationservices/cmdeviceid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceInfo](https://developer.apple.com/documentation/applicationservices/cmdeviceinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceInfoPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceinfoptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileArray](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilearray)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileArrayPtr](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilearrayptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileID](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileInfo](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceProfileScope](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilescope)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceScope](https://developer.apple.com/documentation/applicationservices/cmdevicescope)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDeviceState](https://developer.apple.com/documentation/applicationservices/cmdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDisplayIDType](https://developer.apple.com/documentation/applicationservices/cmdisplayidtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMDisposeProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805358-cmdisposeprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMEmbedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805269-cmembedimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMError](https://developer.apple.com/documentation/coremotion/cmerror)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMFileLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFixedXYColor](https://developer.apple.com/documentation/applicationservices/cmfixedxycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFixedXYZColor](https://developer.apple.com/documentation/applicationservices/cmfixedxyzcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenProcPtr](https://developer.apple.com/documentation/applicationservices/cmflattenprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804897-cmflattenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFlattenUPP](https://developer.apple.com/documentation/applicationservices/cmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFloatBitmap](https://developer.apple.com/documentation/applicationservices/cmfloatbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMFloatBitmapFlags](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMFloatBitmapMakeChunky()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetCWInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805097-cmgetcwinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetColorSyncFolderSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804907-cmgetcolorsyncfolderspec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetColorSyncVersion()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805293-cmgetcolorsyncversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805235-cmgetdefaultdevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804940-cmgetdefaultprofilebyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804948-cmgetdefaultprofilebyuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805249-cmgetdevicedefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805240-cmgetdevicefactoryprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805260-cmgetdeviceinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805256-cmgetdeviceprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805245-cmgetdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805257-cmgetdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805289-cmgetgammabyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetImageSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805267-cmgetimagespace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805284-cmgetindimageprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805059-cmgetindnamedcolorvalue)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805002-cmgetindprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetIndProfileElementInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804996-cmgetindprofileelementinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorIndex()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805065-cmgetnamedcolorindex)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805047-cmgetnamedcolorinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorName()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805072-cmgetnamedcolorname)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetNamedColorValue()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805053-cmgetnamedcolorvalue)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRendering()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805202-cmgetps2colorrendering)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRenderingIntent()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805196-cmgetps2colorrenderingintent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorRenderingVMSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805206-cmgetps2colorrenderingvmsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPS2ColorSpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805191-cmgetps2colorspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804984-cmgetpartialprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetPreferredCMM()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805182-cmgetpreferredcmm)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804955-cmgetprofilebyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805034-cmgetprofiledescriptions)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804973-cmgetprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804879-cmgetprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804885-cmgetprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileMD5()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804876-cmgetprofilemd5)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetProfileRefCount()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804894-cmgetprofilerefcount)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetScriptProfileDescription()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805029-cmgetscriptprofiledescription)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804926-cmgetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMGrayColor](https://developer.apple.com/documentation/applicationservices/cmgraycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHLSColor](https://developer.apple.com/documentation/applicationservices/cmhlscolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHSVColor](https://developer.apple.com/documentation/applicationservices/cmhsvcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMHandleLocation](https://developer.apple.com/documentation/applicationservices/cmhandlelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMHeader

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMIString

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIntentCRDVMSize](https://developer.apple.com/documentation/applicationservices/cmintentcrdvmsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateCMMInfo()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805185-cmiteratecmminfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateColorDevices()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805262-cmiteratecolordevices)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateColorSyncFolder()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804904-cmiteratecolorsyncfolder)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceInfoProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceinfoprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceProfileProcPtr](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceprofileprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMIterateDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805263-cmiteratedeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLabColor](https://developer.apple.com/documentation/applicationservices/cmlabcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLabToLabProcPtr](https://developer.apple.com/documentation/applicationservices/cmlabtolabprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLaunchControlPanel()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805294-cmlaunchcontrolpanel)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLinkImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805278-cmlinkimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLut16Type](https://developer.apple.com/documentation/applicationservices/cmlut16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLut8Type](https://developer.apple.com/documentation/applicationservices/cmlut8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMLuvColor](https://developer.apple.com/documentation/applicationservices/cmluvcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMInfo](https://developer.apple.com/documentation/applicationservices/cmminfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMInfoRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmmiterateprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMIterateUPP](https://developer.apple.com/documentation/applicationservices/cmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CheckBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CheckColors()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_ConcatColorWorld()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_CreateLinkProfile()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_GetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchColors()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_MatchFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMM_ValidateProfile()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeAndModel](https://developer.apple.com/documentation/applicationservices/cmmakeandmodel)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeAndModelType](https://developer.apple.com/documentation/applicationservices/cmmakeandmodeltype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMakeProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804920-cmmakeprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchFlag

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchFloatBitmap()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMatchImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805273-cmmatchimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchOption

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMMatchRef

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMeasurementType](https://developer.apple.com/documentation/applicationservices/cmmeasurementtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctCLUTType](https://developer.apple.com/documentation/applicationservices/cmmultifunctcluttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutA2BType](https://developer.apple.com/documentation/applicationservices/cmmultifunctluta2btype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutB2AType](https://developer.apple.com/documentation/applicationservices/cmmultifunctlutb2atype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiFunctLutType](https://developer.apple.com/documentation/applicationservices/cmmultifunctluttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiLocalizedUniCodeEntryRec](https://developer.apple.com/documentation/applicationservices/cmmultilocalizedunicodeentryrec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultiLocalizedUniCodeType](https://developer.apple.com/documentation/applicationservices/cmmultilocalizedunicodetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel5Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel5color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel6Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel6color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel7Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel7color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMMultichannel8Color](https://developer.apple.com/documentation/applicationservices/cmmultichannel8color)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor](https://developer.apple.com/documentation/applicationservices/cmnamedcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor2EntryType](https://developer.apple.com/documentation/applicationservices/cmnamedcolor2entrytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColor2Type](https://developer.apple.com/documentation/applicationservices/cmnamedcolor2type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNamedColorType](https://developer.apple.com/documentation/applicationservices/cmnamedcolortype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNativeDisplayInfo](https://developer.apple.com/documentation/applicationservices/cmnativedisplayinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNativeDisplayInfoType](https://developer.apple.com/documentation/applicationservices/cmnativedisplayinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNewProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804911-cmnewprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMNewProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805344-cmnewprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMOpenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804853-cmopenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMPS2CRDVMSizeType](https://developer.apple.com/documentation/applicationservices/cmps2crdvmsizetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMParametricCurveType](https://developer.apple.com/documentation/applicationservices/cmparametriccurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMPathLocation](https://developer.apple.com/documentation/applicationservices/cmpathlocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProcedureLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfLoc](https://developer.apple.com/documentation/applicationservices/1560460-cmprofloc)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileAccessProcPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileAccessUPP

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileChromaticities

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileCopyICCData()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileElementExists()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804967-cmprofileelementexists)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileFilterProcPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileFilterUPP

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileHandle

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileIdentifier

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIdentifierFolderSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805374-cmprofileidentifierfoldersearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIdentifierListSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805376-cmprofileidentifierlistsearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileIdentifierPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateData](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateProcPtr](https://developer.apple.com/documentation/applicationservices/cmprofileiterateprocptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileIterateUPP](https://developer.apple.com/documentation/applicationservices/cmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileLocation](https://developer.apple.com/documentation/applicationservices/cmprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileMD5](https://developer.apple.com/documentation/applicationservices/cmprofilemd5)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileMD5AreEqual()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileMD5Ptr](https://developer.apple.com/documentation/applicationservices/cmprofilemd5ptr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileModified()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804872-cmprofilemodified)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfilePtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileRef](https://developer.apple.com/documentation/applicationservices/cmprofileref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecordHandle

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRecordPtr

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMProfileSearchRef

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProfileSequenceDescType](https://developer.apple.com/documentation/applicationservices/cmprofilesequencedesctype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMProofImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805276-cmproofimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMPtrLocation

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRGBColor](https://developer.apple.com/documentation/applicationservices/cmrgbcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRegisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805231-cmregistercolordevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMRemoveProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805008-cmremoveprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMS15Fixed16ArrayType](https://developer.apple.com/documentation/applicationservices/cms15fixed16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMScreeningChannelRec](https://developer.apple.com/documentation/applicationservices/cmscreeningchannelrec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMScreeningType](https://developer.apple.com/documentation/applicationservices/cmscreeningtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSearchGetIndProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805362-cmsearchgetindprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSearchGetIndProfileFileSpec()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805365-cmsearchgetindprofilefilespec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMSearchRecord

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805238-cmsetdefaultdevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultProfileBySpace()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804944-cmsetdefaultprofilebyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDefaultProfileByUse()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804951-cmsetdefaultprofilebyuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceDefaultProfileID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805251-cmsetdevicedefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceFactoryProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805241-cmsetdevicefactoryprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805253-cmsetdeviceprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceProfiles()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805247-cmsetdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetDeviceState()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805258-cmsetdevicestate)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetGammaByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805291-cmsetgammabyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetIndImageProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805286-cmsetindimageprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetPartialProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804989-cmsetpartialprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CMSetPreferredCMM()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileByAVID()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804959-cmsetprofilebyavid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileDescriptions()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805039-cmsetprofiledescriptions)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElement()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804977-cmsetprofileelement)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElementReference()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805005-cmsetprofileelementreference)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileElementSize()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804980-cmsetprofileelementsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileHeader()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804882-cmsetprofileheader)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetProfileLocalizedStringDictionary()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805025-cmsetprofilelocalizedstringdicti)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804932-cmsetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMSignatureType](https://developer.apple.com/documentation/applicationservices/cmsignaturetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTagElemTable](https://developer.apple.com/documentation/applicationservices/cmtagelemtable)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTagRecord](https://developer.apple.com/documentation/applicationservices/cmtagrecord)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTextDescriptionType](https://developer.apple.com/documentation/applicationservices/cmtextdescriptiontype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMTextType](https://developer.apple.com/documentation/applicationservices/cmtexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMU16Fixed16ArrayType](https://developer.apple.com/documentation/applicationservices/cmu16fixed16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt16ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint16arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt32ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint32arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt64ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint64arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUInt8ArrayType](https://developer.apple.com/documentation/applicationservices/cmuint8arraytype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUcrBgType](https://developer.apple.com/documentation/applicationservices/cmucrbgtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnembedImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805271-cmunembedimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnicodeTextType](https://developer.apple.com/documentation/applicationservices/cmunicodetexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUnregisterColorDevice()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805234-cmunregistercolordevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUpdateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804864-cmupdateprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMUpdateProfileSearch()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805356-cmupdateprofilesearch)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMValidImage()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805264-cmvalidimage)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMValidateProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804856-cmvalidateprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGamma](https://developer.apple.com/documentation/applicationservices/cmvideocardgamma)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaFormula](https://developer.apple.com/documentation/applicationservices/cmvideocardgammaformula)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaTable](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatable)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMVideoCardGammaType](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMViewingConditionsType](https://developer.apple.com/documentation/applicationservices/cmviewingconditionstype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMWorldRef](https://developer.apple.com/documentation/applicationservices/cmworldref)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZColor](https://developer.apple.com/documentation/applicationservices/cmxyzcolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZComponent](https://developer.apple.com/documentation/applicationservices/cmxyzcomponent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMXYZType](https://developer.apple.com/documentation/applicationservices/cmxyztype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CMYxyColor](https://developer.apple.com/documentation/applicationservices/cmyxycolor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CS_MAX_PATH](https://developer.apple.com/documentation/applicationservices/cs_max_path)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWCheckBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805121-cwcheckbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWCheckColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805111-cwcheckcolors)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWColorWorldGetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWColorWorldSetProperty()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805087-cwconcatcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWDisposeColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805102-cwdisposecolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWFillLookupTexture()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805126-cwfilllookuptexture)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified CWGetCMMSignature()

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWMatchBitmap()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805116-cwmatchbitmap)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWMatchColors()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805108-cwmatchcolors)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [CWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804915-cwnewlinkprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805300-disposecmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805310-disposecmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805318-disposecmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805323-disposecmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805329-disposecmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805337-disposecmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [DisposeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805341-disposecmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805303-invokecmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805312-invokecmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805320-invokecmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805325-invokecmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805333-invokecmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805338-invokecmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [InvokeCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805343-invokecmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMConcatProfileSet](https://developer.apple.com/documentation/applicationservices/ncmconcatprofileset)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMConcatProfileSpec](https://developer.apple.com/documentation/applicationservices/ncmconcatprofilespec)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMDeviceProfileInfo](https://developer.apple.com/documentation/applicationservices/ncmdeviceprofileinfo)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMGetProfileLocation()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804889-ncmgetprofilelocation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMSetSystemProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804936-ncmsetsystemprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCMUnflattenProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804901-ncmunflattenprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWConcatColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805091-ncwconcatcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWNewColorWorld()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805079-ncwnewcolorworld)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NCWNewLinkProfile()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1804918-ncwnewlinkprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMBitmapCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805297-newcmbitmapcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMConcatCallBackUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805306-newcmconcatcallbackupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMFlattenUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805315-newcmflattenupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMMIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805322-newcmmiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileAccessUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805327-newcmprofileaccessupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileFilterUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805336-newcmprofilefilterupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [NewCMProfileIterateUPP()](https://developer.apple.com/documentation/applicationservices/colorsync_manager/1805339-newcmprofileiterateupp)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm10CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm10clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm11CLRData](https://developer.apple.com/documentation/applicationservices/cm11clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm12CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm12clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm13CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm13clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm14CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm14clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm15CLRData](https://developer.apple.com/documentation/applicationservices/cm15clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm16_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm16_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm24_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm24_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_16ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm32_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_32ColorPacking](https://developer.apple.com/documentation/applicationservices/cm32_32colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm32_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm32_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm3CLRData](https://developer.apple.com/documentation/applicationservices/cm3clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm40_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm40_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm48_16ColorPacking](https://developer.apple.com/documentation/applicationservices/cm48_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm48_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm48_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm4CLRData](https://developer.apple.com/documentation/applicationservices/cm4clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm56_8ColorPacking](https://developer.apple.com/documentation/applicationservices/cm56_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm5CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm5clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm64_16ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm64_16colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm64_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm64_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm6CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm6clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm7CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm7clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm8CLRData](https://developer.apple.com/documentation/applicationservices/cm8clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm8_8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cm8_8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cm9CLRData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cm9clrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64LPmulSpace](https://developer.apple.com/documentation/applicationservices/cmargb64lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmargb64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64PmulSpace](https://developer.apple.com/documentation/applicationservices/cmargb64pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmARGB64Space](https://developer.apple.com/documentation/applicationservices/cmargb64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB0Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmatob0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmatob1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAToB2Tag](https://developer.apple.com/documentation/applicationservices/cmatob2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbortWriteAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmabortwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbsoluteColorimetric](https://developer.apple.com/documentation/applicationservices/cmabsolutecolorimetric)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAbstractClass](https://developer.apple.com/documentation/applicationservices/cmabstractclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaFirstPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmalphafirstpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaLastPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmalphalastpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmalphapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAlphaSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmalphaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmAsciiData](https://developer.apple.com/documentation/applicationservices/1560593-data_type_element_values/cmasciidata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA0Tag](https://developer.apple.com/documentation/applicationservices/cmbtoa0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmbtoa1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBToA2Tag](https://developer.apple.com/documentation/applicationservices/cmbtoa2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBeginAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmbeginaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBeginProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBeginProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBestMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmbestmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBgResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBinaryData](https://developer.apple.com/documentation/applicationservices/cmbinarydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlackPointCompensation](https://developer.apple.com/documentation/applicationservices/cmblackpointcompensation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlackPointCompensationMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmblackpointcompensationmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlueColorantTag](https://developer.apple.com/documentation/applicationservices/cmbluecoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmBlueResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBlueTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmbluetrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBradfordChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/cmbradfordchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmBufferBasedProfile](https://developer.apple.com/documentation/applicationservices/cmbufferbasedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMSReservedFlagsMask](https://developer.apple.com/documentation/applicationservices/cmcmsreservedflagsmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYData](https://developer.apple.com/documentation/applicationservices/cmcmydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYK64Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmcmyk64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYKData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmcmykdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCMYKSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmcmykspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1ChromTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1chromtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1CustTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1custtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1NameTag](https://developer.apple.com/documentation/applicationservices/cmcs1nametag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1ProfileVersion](https://developer.apple.com/documentation/applicationservices/cmcs1profileversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS1TRCTag](https://developer.apple.com/documentation/applicationservices/1560273-0_profiles/cmcs1trctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCS2ProfileVersion](https://developer.apple.com/documentation/applicationservices/cmcs2profileversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCalibrationDateTimeTag](https://developer.apple.com/documentation/applicationservices/cmcalibrationdatetimetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCameraDeviceClass](https://developer.apple.com/documentation/applicationservices/cmcameradeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCharTargetTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmchartargettag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmChromaticAdaptationTag](https://developer.apple.com/documentation/applicationservices/cmchromaticadaptationtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCloseAccess](https://developer.apple.com/documentation/applicationservices/cmcloseaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCloseSpool](https://developer.apple.com/documentation/applicationservices/cmclosespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacealphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceClass](https://developer.apple.com/documentation/applicationservices/cmcolorspaceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceEncodingMask](https://developer.apple.com/documentation/applicationservices/cmcolorspaceencodingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpacePackingMask](https://developer.apple.com/documentation/applicationservices/cmcolorspacepackingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpacePremulAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacepremulalphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceReservedMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacereservedmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceSpaceAndAlphaMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacespaceandalphamask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmColorSpaceSpaceMask](https://developer.apple.com/documentation/applicationservices/1560521-color_space_masks/cmcolorspacespacemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmColorimetricMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmComment

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmContinueProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCopyrightTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmcopyrighttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCreateNewAccess](https://developer.apple.com/documentation/applicationservices/cmcreatenewaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentDeviceInfoVersion](https://developer.apple.com/documentation/applicationservices/1560146-current_info_versions/cmcurrentdeviceinfoversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileInfoVersion](https://developer.apple.com/documentation/applicationservices/1560146-current_info_versions/cmcurrentprofileinfoversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileLocationSize](https://developer.apple.com/documentation/applicationservices/cmcurrentprofilelocationsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmCurrentProfileMajorVersion](https://developer.apple.com/documentation/applicationservices/1560659-current_major_version_mask/cmcurrentprofilemajorversion)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmCyanResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDefaultDeviceID](https://developer.apple.com/documentation/applicationservices/cmdefaultdeviceid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDefaultProfileID](https://developer.apple.com/documentation/applicationservices/1560386-default_ids/cmdefaultprofileid)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceAlreadyRegistered](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmdevicealreadyregistered)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceDBNotFoundErr](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmdevicedbnotfounderr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceInfoVersion1](https://developer.apple.com/documentation/applicationservices/cmdeviceinfoversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceMfgDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmdevicemfgdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceModelDescTag](https://developer.apple.com/documentation/applicationservices/cmdevicemodeldesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceNotRegistered](https://developer.apple.com/documentation/applicationservices/cmdevicenotregistered)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfileInfoVersion1](https://developer.apple.com/documentation/applicationservices/1560472-current_device_versions/cmdeviceprofileinfoversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfileInfoVersion2](https://developer.apple.com/documentation/applicationservices/cmdeviceprofileinfoversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceProfilesNotFound](https://developer.apple.com/documentation/applicationservices/cmdeviceprofilesnotfound)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateAppleRsvdBits](https://developer.apple.com/documentation/applicationservices/cmdevicestateapplersvdbits)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateBusy](https://developer.apple.com/documentation/applicationservices/cmdevicestatebusy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateDefault](https://developer.apple.com/documentation/applicationservices/cmdevicestatedefault)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateDeviceRsvdBits](https://developer.apple.com/documentation/applicationservices/cmdevicestatedevicersvdbits)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateForceNotify](https://developer.apple.com/documentation/applicationservices/cmdevicestateforcenotify)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDeviceStateOffline](https://developer.apple.com/documentation/applicationservices/cmdevicestateoffline)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmDisableMatching

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayClass](https://developer.apple.com/documentation/applicationservices/cmdisplayclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayDeviceClass](https://developer.apple.com/documentation/applicationservices/cmdisplaydeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDisplayUse](https://developer.apple.com/documentation/applicationservices/cmdisplayuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmDraftMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmdraftmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEmbedProfileIdentifier

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEmbedWholeProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmembeddedmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedProfile](https://developer.apple.com/documentation/applicationservices/cmembeddedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedUse](https://developer.apple.com/documentation/applicationservices/cmembeddeduse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEmbeddedUseMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmembeddedusemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEnableMatching

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmEndAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmendaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEndProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmEndProfileSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmFileBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmFlare0](https://developer.apple.com/documentation/applicationservices/1560283-measurement_flares/cmflare0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmFlare100](https://developer.apple.com/documentation/applicationservices/1560283-measurement_flares/cmflare100)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutCheckingMask](https://developer.apple.com/documentation/applicationservices/cmgamutcheckingmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutResult1Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgamutresult1space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutResultSpace](https://developer.apple.com/documentation/applicationservices/cmgamutresultspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGamutTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgamuttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometry045or450](https://developer.apple.com/documentation/applicationservices/cmgeometry045or450)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometry0dord0](https://developer.apple.com/documentation/applicationservices/1560539-measurement_geometries/cmgeometry0dord0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGeometryUnknown](https://developer.apple.com/documentation/applicationservices/1560539-measurement_geometries/cmgeometryunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGlossy](https://developer.apple.com/documentation/applicationservices/1560327-device_and_media_attributes/cmglossy)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGlossyMatteMask](https://developer.apple.com/documentation/applicationservices/1560447-x_profiles/cmglossymattemask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray16LSpace](https://developer.apple.com/documentation/applicationservices/cmgray16lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgray16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGray8Space](https://developer.apple.com/documentation/applicationservices/cmgray8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA16PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya16pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32LPmulSpace](https://developer.apple.com/documentation/applicationservices/cmgraya32lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya32lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmgraya32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayA32Space](https://developer.apple.com/documentation/applicationservices/cmgraya32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayAPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmgrayapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayASpace](https://developer.apple.com/documentation/applicationservices/cmgrayaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmgraydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmGrayResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGraySpace](https://developer.apple.com/documentation/applicationservices/cmgrayspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGrayTRCTag](https://developer.apple.com/documentation/applicationservices/cmgraytrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGreenColorantTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgreencoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmGreenResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmGreenTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmgreentrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLS32Space](https://developer.apple.com/documentation/applicationservices/cmhls32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLSData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmhlsdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHLSSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmhlsspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSV32Space](https://developer.apple.com/documentation/applicationservices/cmhsv32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSVData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmhsvdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmHSVSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmhsvspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmHandleBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion2](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion21](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion21)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCProfileVersion4](https://developer.apple.com/documentation/applicationservices/1560658-icc_profile_versions/cmiccprofileversion4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmICCReservedFlagsMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmiccreservedflagsmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantA](https://developer.apple.com/documentation/applicationservices/cmilluminanta)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD50](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd50)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD55](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd55)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD65](https://developer.apple.com/documentation/applicationservices/cmilluminantd65)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantD93](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantd93)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantEquiPower](https://developer.apple.com/documentation/applicationservices/cmilluminantequipower)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantF2](https://developer.apple.com/documentation/applicationservices/1560108-illuminant_measurement_endocings/cmilluminantf2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantF8](https://developer.apple.com/documentation/applicationservices/cmilluminantf8)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIlluminantUnknown](https://developer.apple.com/documentation/applicationservices/cmilluminantunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInputClass](https://developer.apple.com/documentation/applicationservices/cminputclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInputUse](https://developer.apple.com/documentation/applicationservices/cminputuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInternalCFErr](https://developer.apple.com/documentation/applicationservices/cminternalcferr)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmInterpolationMask](https://developer.apple.com/documentation/applicationservices/cminterpolationmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateAllDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratealldeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateCurrentDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecurrentdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateCustomDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratecustomdeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateDeviceProfilesMask](https://developer.apple.com/documentation/applicationservices/cmiteratedeviceprofilesmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmIterateFactoryDeviceProfiles](https://developer.apple.com/documentation/applicationservices/1560091-profile_iteration_values/cmiteratefactorydeviceprofiles)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB48LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLAB48Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmlab48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLABSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmlabspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLUV32Space](https://developer.apple.com/documentation/applicationservices/cmluv32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLUVSpace](https://developer.apple.com/documentation/applicationservices/cmluvspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLabData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmlabdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinearChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmlinearchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinesPer](https://developer.apple.com/documentation/applicationservices/1560247-screen_encoding_tags/cmlinesper)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLinkClass](https://developer.apple.com/documentation/applicationservices/cmlinkclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLittleEndianPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmlittleendianpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLong10ColorPacking](https://developer.apple.com/documentation/applicationservices/cmlong10colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLong8ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmlong8colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLuminanceTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmluminancetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmLuvData](https://developer.apple.com/documentation/applicationservices/cmluvdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCEight8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmceight8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCEightSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmceightspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCFive8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmcfive8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCFiveSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcfivespace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH5Data](https://developer.apple.com/documentation/applicationservices/cmmch5data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH6Data](https://developer.apple.com/documentation/applicationservices/cmmch6data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH7Data](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmmch7data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCH8Data](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmmch8data)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSeven8Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmmcseven8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSevenSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcsevenspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSix8Space](https://developer.apple.com/documentation/applicationservices/cmmcsix8space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMCSixSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmmcsixspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMacintosh](https://developer.apple.com/documentation/applicationservices/cmmacintosh)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMagentaResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMagicNumber](https://developer.apple.com/documentation/applicationservices/1560690-magic_cookie_number/cmmagicnumber)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMakeAndModelTag](https://developer.apple.com/documentation/applicationservices/cmmakeandmodeltag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchAnyProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchApplProfileVersion

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchAttributes

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchBlack

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchCMMType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDataColorSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDataType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceAttributes

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceManufacturer

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceModel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchDeviceType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchFlags

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchManufacturer

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchModel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchOptions

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileCMMType

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileClass

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileConnectionSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchProfileFlags

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMatchWhite

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMeasurementTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmmeasurementtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMediaBlackPointTag](https://developer.apple.com/documentation/applicationservices/cmmediablackpointtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMediaWhitePointTag](https://developer.apple.com/documentation/applicationservices/cmmediawhitepointtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmMicrosoft](https://developer.apple.com/documentation/applicationservices/cmmicrosoft)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmMonitorDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColor2Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmnamedcolor2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColorClass](https://developer.apple.com/documentation/applicationservices/1560630-profile_classes/cmnamedcolorclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedColorTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmnamedcolortag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmnameddata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexed32LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmnamedindexed32lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexed32Space](https://developer.apple.com/documentation/applicationservices/cmnamedindexed32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNamedIndexedSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmnamedindexedspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNativeDisplayInfoTag](https://developer.apple.com/documentation/applicationservices/1560164-video_card_gamma_tags/cmnativedisplayinfotag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmNativeMatchingPreferred

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmnocolorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoProfileBase](https://developer.apple.com/documentation/applicationservices/1560599-profile_location_type/cmnoprofilebase)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNoSpace](https://developer.apple.com/documentation/applicationservices/cmnospace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNormalMode](https://developer.apple.com/documentation/applicationservices/1560115-x_profiles/cmnormalmode)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmNumHeaderElements](https://developer.apple.com/documentation/applicationservices/1560086-tag_type_information/cmnumheaderelements)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOneBitDirectPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmonebitdirectpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmOnePlusLastResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenReadAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmopenreadaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenReadSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmopenreadspool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenWriteAccess](https://developer.apple.com/documentation/applicationservices/cmopenwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOpenWriteSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmopenwritespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOriginalProfileLocationSize](https://developer.apple.com/documentation/applicationservices/1560369-profile_location_sizes/cmoriginalprofilelocationsize)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOutputClass](https://developer.apple.com/documentation/applicationservices/1560630-profile_classes/cmoutputclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmOutputUse](https://developer.apple.com/documentation/applicationservices/1560730-use_types/cmoutputuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD0Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmps2crd0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD1Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD2Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRD3Tag](https://developer.apple.com/documentation/applicationservices/cmps2crd3tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CRDVMSizeTag](https://developer.apple.com/documentation/applicationservices/cmps2crdvmsizetag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2CSATag](https://developer.apple.com/documentation/applicationservices/cmps2csatag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS2RenderingIntentTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmps2renderingintenttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS7bit](https://developer.apple.com/documentation/applicationservices/1560551-postscript_data_formats/cmps7bit)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPS8bit](https://developer.apple.com/documentation/applicationservices/1560551-postscript_data_formats/cmps8bit)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType0](https://developer.apple.com/documentation/applicationservices/cmparametrictype0)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType1](https://developer.apple.com/documentation/applicationservices/cmparametrictype1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType2](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType3](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype3)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmParametricType4](https://developer.apple.com/documentation/applicationservices/1560541-parametric_types/cmparametrictype4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPathBasedProfile](https://developer.apple.com/documentation/applicationservices/cmpathbasedprofile)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPerceptual](https://developer.apple.com/documentation/applicationservices/1560278-x_profiles/cmperceptual)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPerceptualMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrefsSynchError](https://developer.apple.com/documentation/applicationservices/1560507-anonymous/cmprefssyncherror)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview0Tag](https://developer.apple.com/documentation/applicationservices/cmpreview0tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview1Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmpreview1tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPreview2Tag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmpreview2tag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPrinterDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrinterDeviceClass](https://developer.apple.com/documentation/applicationservices/cmprinterdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmProcedureBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileDescriptionMLTag](https://developer.apple.com/documentation/applicationservices/cmprofiledescriptionmltag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileDescriptionTag](https://developer.apple.com/documentation/applicationservices/cmprofiledescriptiontag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmProfileIdentifierSel

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion1](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedataversion1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion2](https://developer.apple.com/documentation/applicationservices/cmprofileiteratedataversion2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion3](https://developer.apple.com/documentation/applicationservices/1560189-profile_iteration_constants/cmprofileiteratedataversion3)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileIterateDataVersion4](https://developer.apple.com/documentation/applicationservices/1560189-profile_iteration_constants/cmprofileiteratedataversion4)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileMajorVersionMask](https://developer.apple.com/documentation/applicationservices/cmprofilemajorversionmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProfileSequenceDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmprofilesequencedesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProofDeviceClass](https://developer.apple.com/documentation/applicationservices/cmproofdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmProofUse](https://developer.apple.com/documentation/applicationservices/1560730-use_types/cmproofuse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmPrtrDefaultScreens](https://developer.apple.com/documentation/applicationservices/1560247-screen_encoding_tags/cmprtrdefaultscreens)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmPtrBasedProfile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmQualityMask](https://developer.apple.com/documentation/applicationservices/1560699-x_profiles/cmqualitymask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB16LSpace](https://developer.apple.com/documentation/applicationservices/cmrgb16lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB16Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb16space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB32Space](https://developer.apple.com/documentation/applicationservices/cmrgb32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB48LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB48Space](https://developer.apple.com/documentation/applicationservices/cmrgb48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB565LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgb565lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGB565Space](https://developer.apple.com/documentation/applicationservices/cmrgb565space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA32PmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba32pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64LPmulSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64lpmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64LSpace](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64PmulSpace](https://developer.apple.com/documentation/applicationservices/cmrgba64pmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBA64Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmrgba64space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBAPmulSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbapmulspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBASpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbaspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmrgbdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRGBSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmrgbspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReadAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmreadaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReadSpool](https://developer.apple.com/documentation/applicationservices/1560166-data_transfer_commands/cmreadspool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRedColorantTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmredcoloranttag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmRedResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRedTRCTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmredtrctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReflective](https://developer.apple.com/documentation/applicationservices/1560327-device_and_media_attributes/cmreflective)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReflectiveTransparentMask](https://developer.apple.com/documentation/applicationservices/1560447-x_profiles/cmreflectivetransparentmask)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmRelativeColorimetric](https://developer.apple.com/documentation/applicationservices/1560278-x_profiles/cmrelativecolorimetric)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReservedSpace1](https://developer.apple.com/documentation/applicationservices/cmreservedspace1)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReservedSpace2](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmreservedspace2)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmReverseChannelPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmreversechannelpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSRGB16ChannelEncoding](https://developer.apple.com/documentation/applicationservices/cmsrgb16channelencoding)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSRGBData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmsrgbdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSaturation](https://developer.apple.com/documentation/applicationservices/cmsaturation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmSaturationMatch

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmScannerDevice

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScannerDeviceClass](https://developer.apple.com/documentation/applicationservices/cmscannerdeviceclass)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScreeningDescTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmscreeningdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmScreeningTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmscreeningtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigCrdInfoType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigcrdinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigCurveType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigcurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigDataType](https://developer.apple.com/documentation/applicationservices/cmsigdatatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigDateTimeType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigdatetimetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigLut16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiglut16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigLut8Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiglut8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMakeAndModelType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigmakeandmodeltype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMeasurementType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigmeasurementtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiFunctA2BType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigmultifuncta2btype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiFunctB2AType](https://developer.apple.com/documentation/applicationservices/cmsigmultifunctb2atype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigMultiLocalizedUniCodeType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigmultilocalizedunicodetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNamedColor2Type](https://developer.apple.com/documentation/applicationservices/cmsignamedcolor2type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNamedColorType](https://developer.apple.com/documentation/applicationservices/cmsignamedcolortype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigNativeDisplayInfoType](https://developer.apple.com/documentation/applicationservices/cmsignativedisplayinfotype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigPS2CRDVMSizeType](https://developer.apple.com/documentation/applicationservices/1560275-video_card_gamma_signatures/cmsigps2crdvmsizetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigParametricCurveType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigparametriccurvetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigProfileDescriptionType](https://developer.apple.com/documentation/applicationservices/cmsigprofiledescriptiontype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigProfileSequenceDescType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigprofilesequencedesctype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigS15Fixed16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigs15fixed16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigScreeningType](https://developer.apple.com/documentation/applicationservices/cmsigscreeningtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigSignatureType](https://developer.apple.com/documentation/applicationservices/cmsigsignaturetype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigTextType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigtexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigU16Fixed16Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigu16fixed16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigU1Fixed15Type](https://developer.apple.com/documentation/applicationservices/cmsigu1fixed15type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt16Type](https://developer.apple.com/documentation/applicationservices/cmsiguint16type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt32Type](https://developer.apple.com/documentation/applicationservices/cmsiguint32type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt64Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiguint64type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUInt8Type](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsiguint8type)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUcrBgType](https://developer.apple.com/documentation/applicationservices/cmsigucrbgtype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigUnicodeTextType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigunicodetexttype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigVideoCardGammaType](https://developer.apple.com/documentation/applicationservices/cmsigvideocardgammatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigViewingConditionsType](https://developer.apple.com/documentation/applicationservices/1560346-public_type_signatures/cmsigviewingconditionstype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSigXYZType](https://developer.apple.com/documentation/applicationservices/cmsigxyztype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSiliconGraphics](https://developer.apple.com/documentation/applicationservices/cmsilicongraphics)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSolaris](https://developer.apple.com/documentation/applicationservices/1560191-platform_enumeration_values/cmsolaris)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionCross](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctioncross)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionDefault](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctiondefault)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionDiamond](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctiondiamond)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionEllipse](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionellipse)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionLine](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionline)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionRound](https://developer.apple.com/documentation/applicationservices/cmspotfunctionround)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionSquare](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionsquare)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmSpotFunctionUnknown](https://developer.apple.com/documentation/applicationservices/1560411-spot_function_values/cmspotfunctionunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobs1931TwoDegrees](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobs1931twodegrees)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobs1964TenDegrees](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobs1964tendegrees)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmStdobsUnknown](https://developer.apple.com/documentation/applicationservices/1560388-standard_observer/cmstdobsunknown)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTaligent](https://developer.apple.com/documentation/applicationservices/1560191-platform_enumeration_values/cmtaligent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyAMDisplay](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyamdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyCRTDisplay](https://developer.apple.com/documentation/applicationservices/cmtechnologycrtdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyDigitalCamera](https://developer.apple.com/documentation/applicationservices/cmtechnologydigitalcamera)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyDyeSublimationPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologydyesublimationprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyElectrophotographicPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyelectrophotographicprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyElectrostaticPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyelectrostaticprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFilmScanner](https://developer.apple.com/documentation/applicationservices/cmtechnologyfilmscanner)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFilmWriter](https://developer.apple.com/documentation/applicationservices/cmtechnologyfilmwriter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyFlexography](https://developer.apple.com/documentation/applicationservices/cmtechnologyflexography)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyGravure](https://developer.apple.com/documentation/applicationservices/cmtechnologygravure)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyInkJetPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyinkjetprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyOffsetLithography](https://developer.apple.com/documentation/applicationservices/cmtechnologyoffsetlithography)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPMDisplay](https://developer.apple.com/documentation/applicationservices/cmtechnologypmdisplay)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotoCD](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyphotocd)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotoImageSetter](https://developer.apple.com/documentation/applicationservices/cmtechnologyphotoimagesetter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyPhotographicPaperPrinter](https://developer.apple.com/documentation/applicationservices/cmtechnologyphotographicpaperprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyProjectionTelevision](https://developer.apple.com/documentation/applicationservices/cmtechnologyprojectiontelevision)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyReflectiveScanner](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologyreflectivescanner)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologySilkscreen](https://developer.apple.com/documentation/applicationservices/cmtechnologysilkscreen)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmtechnologytag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyThermalWaxPrinter](https://developer.apple.com/documentation/applicationservices/1560433-technology_tag_descriptions/cmtechnologythermalwaxprinter)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyVideoCamera](https://developer.apple.com/documentation/applicationservices/cmtechnologyvideocamera)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmTechnologyVideoMonitor](https://developer.apple.com/documentation/applicationservices/cmtechnologyvideomonitor)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBX16

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBX8

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTextureRGBtoRGBXFloat32

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmTurnOffCache

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmUcrBgTag](https://developer.apple.com/documentation/applicationservices/1560717-public_tags/cmucrbgtag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmUcrResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmUseDefaultChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmusedefaultchromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaFormulaType](https://developer.apple.com/documentation/applicationservices/1560344-video_card_gamma_storage_types/cmvideocardgammaformulatype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaTableType](https://developer.apple.com/documentation/applicationservices/cmvideocardgammatabletype)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVideoCardGammaTag](https://developer.apple.com/documentation/applicationservices/1560164-video_card_gamma_tags/cmvideocardgammatag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmViewingConditionsDescTag](https://developer.apple.com/documentation/applicationservices/cmviewingconditionsdesctag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmViewingConditionsTag](https://developer.apple.com/documentation/applicationservices/cmviewingconditionstag)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmVonKriesChromaticAdaptation](https://developer.apple.com/documentation/applicationservices/1560580-anonymous/cmvonkrieschromaticadaptation)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWord565ColorPacking](https://developer.apple.com/documentation/applicationservices/1560270-color_packing_for_color_spaces/cmword565colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWord5ColorPacking](https://developer.apple.com/documentation/applicationservices/cmword5colorpacking)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWriteAccess](https://developer.apple.com/documentation/applicationservices/1560733-profile_access_procedures/cmwriteaccess)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmWriteSpool](https://developer.apple.com/documentation/applicationservices/cmwritespool)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ24Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz24space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ48LSpace](https://developer.apple.com/documentation/applicationservices/cmxyz48lspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZ48Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmxyz48space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmxyzdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmXYZSpace](https://developer.apple.com/documentation/applicationservices/1560701-abstract_color_space_constants/cmxyzspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYCbCrData](https://developer.apple.com/documentation/applicationservices/cmycbcrdata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYXY32Space](https://developer.apple.com/documentation/applicationservices/1560256-anonymous/cmyxy32space)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYXYSpace](https://developer.apple.com/documentation/applicationservices/cmyxyspace)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmYellowResponse

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [cmYxyData](https://developer.apple.com/documentation/applicationservices/1560276-color_space_signatures/cmyxydata)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspFavorEmbeddedMask

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidImageFile

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidImageSpace

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileDest

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileEmbed

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileLink

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileProof

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified cmspInvalidProfileSource

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDefaultDeviceNotification](https://developer.apple.com/documentation/applicationservices/kcmdefaultdevicenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDefaultDeviceProfileNotification](https://developer.apple.com/documentation/applicationservices/kcmdefaultdeviceprofilenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceOfflineNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceofflinenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceOnlineNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceonlinenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceProfilesNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceprofilesnotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceRegisteredNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceregisterednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceStateNotification](https://developer.apple.com/documentation/applicationservices/kcmdevicestatenotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDeviceUnregisteredNotification](https://developer.apple.com/documentation/applicationservices/kcmdeviceunregisterednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMDisplayDeviceProfilesNotification](https://developer.apple.com/documentation/applicationservices/kcmdisplaydeviceprofilesnotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsAlpha](https://developer.apple.com/documentation/applicationservices/kcmfloatbitmapflagsalpha)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsAlphaPremul](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags/kcmfloatbitmapflagsalphapremul)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsNone](https://developer.apple.com/documentation/applicationservices/cmfloatbitmapflags/kcmfloatbitmapflagsnone)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kCMFloatBitmapFlagsRangeClipped](https://developer.apple.com/documentation/applicationservices/kcmfloatbitmapflagsrangeclipped)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified kCMIlluminantD50

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified kCMIlluminantD65

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [#def kCMPrefsChangedNotification](https://developer.apple.com/documentation/applicationservices/kcmprefschangednotification)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kDefaultCMMSignature](https://developer.apple.com/documentation/applicationservices/kdefaultcmmsignature)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kDeviceToPCS](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kdevicetopcs)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kNoTransform](https://developer.apple.com/documentation/applicationservices/knotransform)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kPCSToDevice](https://developer.apple.com/documentation/applicationservices/kpcstodevice)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kPCSToPCS](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kpcstopcs)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseAtoB](https://developer.apple.com/documentation/applicationservices/1560373-profile_concatenation_values/kuseatob)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseBtoA](https://developer.apple.com/documentation/applicationservices/kusebtoa)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseBtoB](https://developer.apple.com/documentation/applicationservices/kusebtob)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

Modified [kUseProfileIntent](https://developer.apple.com/documentation/applicationservices/kuseprofileintent)

|  | Header |
| --- | --- |
| From | ColorSync/ColorSyncDeprecated.h |
| To | QD/ColorSyncDeprecated.h |

ColorSyncProfile.hAdded [kColorSyncSigAToB0Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigatob0tag)Added [kColorSyncSigAToB1Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigatob1tag)Added [kColorSyncSigAToB2Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigatob2tag)Added [kColorSyncSigAbstractClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsigabstractclass)Added [kColorSyncSigBToA0Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigbtoa0tag)Added [kColorSyncSigBToA1Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigbtoa1tag)Added [kColorSyncSigBToA2Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigbtoa2tag)Added [kColorSyncSigBlueColorantTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigbluecoloranttag)Added [kColorSyncSigBlueTRCTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigbluetrctag)Added [kColorSyncSigCmykData](https://developer.apple.com/documentation/colorsync/kcolorsyncsigcmykdata)Added [kColorSyncSigColorSpaceClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsigcolorspaceclass)Added [kColorSyncSigCopyrightTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigcopyrighttag)Added [kColorSyncSigDeviceMfgDescTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigdevicemfgdesctag)Added [kColorSyncSigDeviceModelDescTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigdevicemodeldesctag)Added [kColorSyncSigDisplayClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsigdisplayclass)Added [kColorSyncSigGamutTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsiggamuttag)Added [kColorSyncSigGrayData](https://developer.apple.com/documentation/colorsync/kcolorsyncsiggraydata)Added [kColorSyncSigGrayTRCTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsiggraytrctag)Added [kColorSyncSigGreenColorantTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsiggreencoloranttag)Added [kColorSyncSigGreenTRCTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsiggreentrctag)Added [kColorSyncSigInputClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsiginputclass)Added [kColorSyncSigLabData](https://developer.apple.com/documentation/colorsync/kcolorsyncsiglabdata)Added [kColorSyncSigLinkClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsiglinkclass)Added [kColorSyncSigMediaBlackPointTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigmediablackpointtag)Added [kColorSyncSigMediaWhitePointTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigmediawhitepointtag)Added [kColorSyncSigNamedColor2Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsignamedcolor2tag)Added [kColorSyncSigNamedColorClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsignamedcolorclass)Added [kColorSyncSigOutputClass](https://developer.apple.com/documentation/colorsync/kcolorsyncsigoutputclass)Added [kColorSyncSigPreview0Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigpreview0tag)Added [kColorSyncSigPreview1Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigpreview1tag)Added [kColorSyncSigPreview2Tag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigpreview2tag)Added [kColorSyncSigProfileDescriptionTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigprofiledescriptiontag)Added [kColorSyncSigProfileSequenceDescTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigprofilesequencedesctag)Added [kColorSyncSigRedColorantTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigredcoloranttag)Added [kColorSyncSigRedTRCTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigredtrctag)Added [kColorSyncSigRgbData](https://developer.apple.com/documentation/colorsync/kcolorsyncsigrgbdata)Added [kColorSyncSigTechnologyTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigtechnologytag)Added [kColorSyncSigViewingCondDescTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigviewingconddesctag)Added [kColorSyncSigViewingConditionsTag](https://developer.apple.com/documentation/colorsync/kcolorsyncsigviewingconditionstag)Added [kColorSyncSigXYZData](https://developer.apple.com/documentation/colorsync/kcolorsyncsigxyzdata)ColorSyncTransform.hAdded [kColorSyncConversionNDLut](https://developer.apple.com/documentation/colorsync/kcolorsyncconversionndlut)Added [kColorSyncFixedPointRange](https://developer.apple.com/documentation/colorsync/kcolorsyncfixedpointrange)CoreGraphics.hPMPrintSettingsKeys.hAdded #def kPMUseOptionalPINKeyAdded [#def kPMUseOptionalPINStr](https://developer.apple.com/documentation/applicationservices/kpmuseoptionalpinstr)PMPrintingDialogExtensions.hAdded #def kPMJobPINPDEKindIDProcesses.hModified [CopyProcessName()](https://developer.apple.com/documentation/applicationservices/1501067-copyprocessname)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [ExitToShell()](https://developer.apple.com/documentation/applicationservices/1500985-exittoshell)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetCurrentProcess()](https://developer.apple.com/documentation/applicationservices/1501115-getcurrentprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetFrontProcess()](https://developer.apple.com/documentation/applicationservices/1501050-getfrontprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetNextProcess()](https://developer.apple.com/documentation/applicationservices/1501061-getnextprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetProcessBundleLocation()](https://developer.apple.com/documentation/applicationservices/1501092-getprocessbundlelocation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetProcessForPID()](https://developer.apple.com/documentation/applicationservices/1501069-getprocessforpid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetProcessInformation()](https://developer.apple.com/documentation/applicationservices/1501011-getprocessinformation)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GetProcessPID()](https://developer.apple.com/documentation/applicationservices/1500992-getprocesspid)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [IsProcessVisible()](https://developer.apple.com/documentation/applicationservices/1501035-isprocessvisible)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [KillProcess()](https://developer.apple.com/documentation/applicationservices/1501110-killprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [LaunchApplication()](https://developer.apple.com/documentation/applicationservices/1501089-launchapplication)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [ProcessInformationCopyDictionary()](https://developer.apple.com/documentation/applicationservices/1501104-processinformationcopydictionary)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SameProcess()](https://developer.apple.com/documentation/applicationservices/1501087-sameprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SetFrontProcess()](https://developer.apple.com/documentation/applicationservices/1501042-setfrontprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [SetFrontProcessWithOptions()](https://developer.apple.com/documentation/applicationservices/1501003-setfrontprocesswithoptions)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [ShowHideProcess()](https://developer.apple.com/documentation/applicationservices/1501053-showhideprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [WakeUpProcess()](https://developer.apple.com/documentation/applicationservices/1501091-wakeupprocess)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

SpeechSynthesis.hAdded [kSpeechAudioOutputFormatProperty](https://developer.apple.com/documentation/applicationservices/kspeechaudiooutputformatproperty)Added [kSpeechOutputChannelMapProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputchannelmapproperty)Added [kSpeechOutputToFileDescriptorProperty](https://developer.apple.com/documentation/applicationservices/kspeechoutputtofiledescriptorproperty)Added [kSpeechSynthExtensionProperty](https://developer.apple.com/documentation/applicationservices/kspeechsynthextensionproperty)

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

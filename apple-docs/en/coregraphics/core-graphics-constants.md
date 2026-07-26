---
title: Core Graphics Constants
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/core-graphics-constants
source_url: 'https://developer.apple.com/documentation/coregraphics/core-graphics-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/core-graphics-constants.json'
content_hash: 'sha256:70652e7c001bf419'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# Core Graphics Constants

<sub>API Collection</sub>

## Topics

### Constants

- [kCGColorConversionBlackPointCompensation](cgcolor/conversionblackpointcompensation.md) — An option for whether to apply black point compensation when converting between color profiles.
- [kCGDisplayBitsPerPixel](kcgdisplaybitsperpixel.md) — Specifies a CFNumber integer value that represents the number of bits in a pixel.
- [kCGDisplayBitsPerSample](kcgdisplaybitspersample.md) — Specifies a CFNumber integer value that represents the number of bits in an individual sample (for example, a color value in an RGB pixel).
- [kCGDisplayBlendNormal](kcgdisplayblendnormal.md) — The blend color is not applied at the start or end of a fade operation.
- [kCGDisplayBlendSolidColor](kcgdisplayblendsolidcolor.md) — The user sees only the blend color at the start or end of a fade operation.
- [kCGDisplayBytesPerRow](kcgdisplaybytesperrow.md) — Specifies a CFNumber integer value that represents the number of bytes in a row on the display.
- [kCGDisplayFadeReservationInvalidToken](kcgdisplayfadereservationinvalidtoken.md)
- [kCGDisplayHeight](kcgdisplayheight.md) — Specifies a CFNumber integer value that represents the height of the display in pixels.
- [kCGDisplayIOFlags](kcgdisplayioflags.md) — Specifies a CFNumber integer value that contains the I/O Kit display mode flags. For more information, see the header file `IOKit/IOGraphicsTypes.h`.
- [kCGDisplayMode](kcgdisplaymode.md) — Specifies a `CFNumber` integer value that represents the I/O Kit display mode number.
- [kCGDisplayModeIsInterlaced](kcgdisplaymodeisinterlaced.md) — Specifies a CFBoolean value indicating that the I/O Kit interlace mode flag is set.
- [kCGDisplayModeIsSafeForHardware](kcgdisplaymodeissafeforhardware.md) — Specifies a CFBoolean value indicating that the display mode doesn’t need a confirmation dialog to be set. _(deprecated)_
- [kCGDisplayModeIsStretched](kcgdisplaymodeisstretched.md) — Specifies a CFBoolean value indicating that the I/O Kit stretched mode flag is set.
- [kCGDisplayModeIsTelevisionOutput](kcgdisplaymodeistelevisionoutput.md) — Specifies a CFBoolean value indicating that the I/O Kit television output mode flag is set.
- [kCGDisplayModeUsableForDesktopGUI](kcgdisplaymodeusablefordesktopgui.md) — Specifies a CFBoolean value that indicates whether the display is suitable for use with the macOS graphical user interface. The criteria include factors such as sufficient width and height and adequate pixel depth.
- [kCGDisplayRefreshRate](kcgdisplayrefreshrate.md) — Specifies a `CFNumber` double-precision floating point value that represents the refresh rate of a CRT display.
- [kCGDisplaySamplesPerPixel](kcgdisplaysamplesperpixel.md) — Specifies a CFNumber integer value that represents the number of samples in a pixel.
- [kCGDisplayShowDuplicateLowResolutionModes](kcgdisplayshowduplicatelowresolutionmodes.md)
- [kCGDisplayStreamYCbCrMatrix_ITU_R_601_4](cgdisplaystream/ycbcrmatrix_itu_r_601_4.md) — Specifies the YCbCr to RGB conversion matrix for standard digital television (ITU R 601) images.
- [kCGDisplayStreamYCbCrMatrix_ITU_R_709_2](cgdisplaystream/ycbcrmatrix_itu_r_709_2.md) — Specifies the YCbCr to RGB conversion matrix for HDTV digital television (ITU R 709) images.
- [kCGDisplayStreamYCbCrMatrix_SMPTE_240M_1995](cgdisplaystream/ycbcrmatrix_smpte_240m_1995.md) — Specifies the YCbCR to RGB conversion matrix for 1920 x 1135 HDTV (SMPTE 240M 1995).
- [kCGDisplayWidth](kcgdisplaywidth.md) — Specifies a CFNumber integer value that represents the width of the display in pixels. _(deprecated)_
- [kCGFontIndexInvalid](kcgfontindexinvalid.md) — An invalid font index (a value which never represents a valid glyph).
- [kCGFontIndexMax](kcgfontindexmax.md) — The maximum allowed value of a [CGFontIndex](cgfontindex.md).
- [kCGGlyphMax](kcgglyphmax.md) — The maximum allowed value of a [CGGlyph](cgglyph.md).
- [kCGIODisplayModeID](kcgiodisplaymodeid.md)
- [kCGMouseDownEventMaskingDeadSwitchTimeout](kcgmousedowneventmaskingdeadswitchtimeout.md)
- [kCGNotifyEventTapAdded](kcgnotifyeventtapadded.md)
- [kCGNotifyEventTapRemoved](kcgnotifyeventtapremoved.md)
- [kCGNotifyGUIConsoleSessionChanged](kcgnotifyguiconsolesessionchanged.md)
- [kCGNotifyGUISessionUserChanged](kcgnotifyguisessionuserchanged.md)
- [kCGNumReservedWindowLevels](kcgnumreservedwindowlevels.md)
- [kCGSessionConsoleSetKey](kcgsessionconsolesetkey.md) — A `CFNumber` 32-bit unsigned integer value that represents a set of hardware composing a console.
- [kCGSessionLoginDoneKey](kcgsessionlogindonekey.md) — A `CFBoolean` value indicating whether the login operation has been done.
- [kCGSessionOnConsoleKey](kcgsessiononconsolekey.md) — A `CFBoolean` value indicating whether the session is on a console.
- [kCGSessionUserIDKey](kcgsessionuseridkey.md) — A `CFNumber` 32-bit unsigned integer value that encodes a user ID for the session’s current user.
- [kCGSessionUserNameKey](kcgsessionusernamekey.md) — A `CFString` value that encodes the session’s short user name as set by the login operation.
- [kCGWindowAlpha](kcgwindowalpha.md)
- [kCGWindowBackingLocationVideoMemory](kcgwindowbackinglocationvideomemory.md)
- [kCGWindowBounds](kcgwindowbounds.md)
- [kCGWindowIsOnscreen](kcgwindowisonscreen.md)
- [kCGWindowLayer](kcgwindowlayer.md)
- [kCGWindowMemoryUsage](kcgwindowmemoryusage.md)
- [kCGWindowName](kcgwindowname.md)
- [kCGWindowNumber](kcgwindownumber.md)
- [kCGWindowOwnerName](kcgwindowownername.md)
- [kCGWindowOwnerPID](kcgwindowownerpid.md)
- [kCGWindowSharingState](kcgwindowsharingstate.md)
- [kCGWindowStoreType](kcgwindowstoretype.md)
- [CGPointZero](cgpointzero.md) — A point constant with location `(0,0)`. The zero point is equivalent to `CGPointMake(0,0)`.
- [CGRectZero](cgrectzero.md) — A rectangle constant with location `(0,0)`, and width and height of 0. The zero rectangle is equivalent to `CGRectMake(0,0,0,0)`.
- [CGSizeZero](cgsizezero.md) — A size constant with width and height of `0`. The zero size is equivalent to `CGSizeMake(0,0)`.
- [kCGWindowWorkspace](kcgwindowworkspace.md) _(deprecated)_
- [CG_HDR_BT_2100](cg_hdr_bt_2100.md)
- [kCGBitmapByteOrder16Host](kcgbitmapbyteorder16host.md) — 16-bit, host endian format. _(deprecated)_
- [kCGBitmapByteOrder32Host](kcgbitmapbyteorder32host.md) — 32-bit, host endian format. _(deprecated)_
- [kCGColorSpaceExtendedRange](kcgcolorspaceextendedrange.md)
- [kCGDefaultHDRImageContentHeadroom](kcgdefaulthdrimagecontentheadroom.md)
- [kCGEXRToneMappingGammaDefog](kcgexrtonemappinggammadefog.md)
- [kCGEXRToneMappingGammaExposure](kcgexrtonemappinggammaexposure.md)
- [kCGEXRToneMappingGammaKneeHigh](kcgexrtonemappinggammakneehigh.md)
- [kCGEXRToneMappingGammaKneeLow](kcgexrtonemappinggammakneelow.md)
- [kCGNullDirectDisplay](kcgnulldirectdisplay.md) — A value that will never correspond to actual hardware.
- [kCGNullWindowID](kcgnullwindowid.md)
- [kCGNumReservedBaseWindowLevels](kcgnumreservedbasewindowlevels.md)
- [kCGPDFContextAccessPermissions](kcgpdfcontextaccesspermissions.md)
- [kCGPDFContextCreateLinearizedPDF](kcgpdfcontextcreatelinearizedpdf.md)
- [kCGPDFContextCreatePDFA](kcgpdfcontextcreatepdfa.md)
- [kCGPDFOutlineChildren](kcgpdfoutlinechildren.md)
- [kCGPDFOutlineDestination](kcgpdfoutlinedestination.md)
- [kCGPDFOutlineDestinationRect](kcgpdfoutlinedestinationrect.md)
- [kCGPDFOutlineTitle](kcgpdfoutlinetitle.md)
- [kCGSkipBoostToHDR](kcgskipboosttohdr.md)
- [kCGUse100nitsHLGOOTF](kcguse100nitshlgootf.md)
- [kCGUseBT1886ForCoreVideoGamma](kcgusebt1886forcorevideogamma.md)
- [kCGUseLegacyHDREcosystem](kcguselegacyhdrecosystem.md)
- [kCGAssistiveTechHighWindowLevel](kcgassistivetechhighwindowlevel.md)
- [kCGBackstopMenuLevel](kcgbackstopmenulevel.md)
- [kCGDockWindowLevel](kcgdockwindowlevel.md)
- [kCGDraggingWindowLevel](kcgdraggingwindowlevel.md)
- [kCGFloatingWindowLevel](kcgfloatingwindowlevel.md)
- [kCGHelpWindowLevel](kcghelpwindowlevel.md)
- [kCGMainMenuWindowLevel](kcgmainmenuwindowlevel.md)
- [kCGModalPanelWindowLevel](kcgmodalpanelwindowlevel.md)
- [kCGNormalWindowLevel](kcgnormalwindowlevel.md)
- [kCGOverlayWindowLevel](kcgoverlaywindowlevel.md)
- [kCGPopUpMenuWindowLevel](kcgpopupmenuwindowlevel.md)
- [kCGScreenSaverWindowLevel](kcgscreensaverwindowlevel.md)
- [kCGStatusWindowLevel](kcgstatuswindowlevel.md)
- [kCGTornOffMenuWindowLevel](kcgtornoffmenuwindowlevel.md)
- [kCGUtilityWindowLevel](kcgutilitywindowlevel.md)

## See Also

### Reference

- [Core Graphics Structures](core-graphics-structures.md)
- [Core Graphics Enumerations](core-graphics-enumerations.md)
- [Core Graphics Functions](core-graphics-functions.md)
- [Core Graphics Data Types](core-graphics-data-types.md)

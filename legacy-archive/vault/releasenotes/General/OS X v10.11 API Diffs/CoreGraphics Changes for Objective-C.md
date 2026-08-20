---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/CoreGraphics.html
archived_at: '2026-07-18T02:52:58.292306Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# CoreGraphics Changes for Objective-C

### CoreGraphics

#### CGBitmapContext.h

Modified [CGBitmapContextCreate()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGBitmapContextCreate (     void *data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo ); ``` |
| To | ``` CGContextRef _Nullable CGBitmapContextCreate (     void * _Nullable data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     uint32_t bitmapInfo ); ``` |

Modified [CGBitmapContextCreateImage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454225-makeimage)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGBitmapContextCreateImage (     CGContextRef context ); ``` |
| To | ``` CGImageRef _Nullable CGBitmapContextCreateImage (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextCreateWithData()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454984-init)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGBitmapContextCreateWithData (     void *data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo,     CGBitmapContextReleaseDataCallback releaseCallback,     void *releaseInfo ); ``` |
| To | ``` CGContextRef _Nullable CGBitmapContextCreateWithData (     void * _Nullable data,     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     uint32_t bitmapInfo,     CGBitmapContextReleaseDataCallback _Nullable releaseCallback,     void * _Nullable releaseInfo ); ``` |

Modified [CGBitmapContextGetAlphaInfo()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454960-alphainfo)

|  | Declaration |
| --- | --- |
| From | ``` CGImageAlphaInfo CGBitmapContextGetAlphaInfo (     CGContextRef context ); ``` |
| To | ``` CGImageAlphaInfo CGBitmapContextGetAlphaInfo (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetBitmapInfo()](https://developer.apple.com/documentation/coregraphics/1455839-cgbitmapcontextgetbitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` CGBitmapInfo CGBitmapContextGetBitmapInfo (     CGContextRef context ); ``` |
| To | ``` CGBitmapInfo CGBitmapContextGetBitmapInfo (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetBitsPerComponent()](https://developer.apple.com/documentation/coregraphics/1455383-cgbitmapcontextgetbitspercompone)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGBitmapContextGetBitsPerComponent (     CGContextRef context ); ``` |
| To | ``` size_t CGBitmapContextGetBitsPerComponent (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetBitsPerPixel()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455946-bitsperpixel)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGBitmapContextGetBitsPerPixel (     CGContextRef context ); ``` |
| To | ``` size_t CGBitmapContextGetBitsPerPixel (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetBytesPerRow()](https://developer.apple.com/documentation/coregraphics/1456129-cgbitmapcontextgetbytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGBitmapContextGetBytesPerRow (     CGContextRef context ); ``` |
| To | ``` size_t CGBitmapContextGetBytesPerRow (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetColorSpace()](https://developer.apple.com/documentation/coregraphics/1454058-cgbitmapcontextgetcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGBitmapContextGetColorSpace (     CGContextRef context ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGBitmapContextGetColorSpace (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetData()](https://developer.apple.com/documentation/coregraphics/1455517-cgbitmapcontextgetdata)

|  | Declaration |
| --- | --- |
| From | ``` void * CGBitmapContextGetData (     CGContextRef context ); ``` |
| To | ``` void * _Nullable CGBitmapContextGetData (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetHeight()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454681-height)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGBitmapContextGetHeight (     CGContextRef context ); ``` |
| To | ``` size_t CGBitmapContextGetHeight (     CGContextRef _Nullable context ); ``` |

Modified [CGBitmapContextGetWidth()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455607-width)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGBitmapContextGetWidth (     CGContextRef context ); ``` |
| To | ``` size_t CGBitmapContextGetWidth (     CGContextRef _Nullable context ); ``` |

#### CGColor.h

Added [CGColorCreateCopyByMatchingToColorSpace()](https://developer.apple.com/documentation/coregraphics/1455493-cgcolorcreatecopybymatchingtocol)Modified [CGColorCreate()](https://developer.apple.com/documentation/coregraphics/1455927-cgcolorcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreate (     CGColorSpaceRef space,     const CGFloat components[] ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreate (     CGColorSpaceRef _Nullable space,     const CGFloat * _Nullable components ); ``` |

Modified [CGColorCreateCopy()](https://developer.apple.com/documentation/coregraphics/cgcolor/1456134-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateCopy (     CGColorRef color ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreateCopy (     CGColorRef _Nullable color ); ``` |

Modified [CGColorCreateCopyWithAlpha()](https://developer.apple.com/documentation/coregraphics/cgcolor/1455986-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateCopyWithAlpha (     CGColorRef color,     CGFloat alpha ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreateCopyWithAlpha (     CGColorRef _Nullable color,     CGFloat alpha ); ``` |

Modified [CGColorCreateGenericCMYK()](https://developer.apple.com/documentation/coregraphics/cgcolor/1454222-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateGenericCMYK (     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |
| To | ``` CGColorRef _Nonnull CGColorCreateGenericCMYK (     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |

Modified [CGColorCreateGenericGray()](https://developer.apple.com/documentation/coregraphics/cgcolor/1456453-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateGenericGray (     CGFloat gray,     CGFloat alpha ); ``` |
| To | ``` CGColorRef _Nonnull CGColorCreateGenericGray (     CGFloat gray,     CGFloat alpha ); ``` |

Modified [CGColorCreateGenericRGB()](https://developer.apple.com/documentation/coregraphics/1455631-cgcolorcreategenericrgb)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateGenericRGB (     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |
| To | ``` CGColorRef _Nonnull CGColorCreateGenericRGB (     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |

Modified [CGColorCreateWithPattern()](https://developer.apple.com/documentation/coregraphics/cgcolor/1455687-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorCreateWithPattern (     CGColorSpaceRef space,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` CGColorRef _Nullable CGColorCreateWithPattern (     CGColorSpaceRef _Nullable space,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

Modified [CGColorEqualToColor()](https://developer.apple.com/documentation/coregraphics/1455217-cgcolorequaltocolor)

|  | Declaration |
| --- | --- |
| From | ``` bool CGColorEqualToColor (     CGColorRef color1,     CGColorRef color2 ); ``` |
| To | ``` bool CGColorEqualToColor (     CGColorRef _Nullable color1,     CGColorRef _Nullable color2 ); ``` |

Modified [CGColorGetAlpha()](https://developer.apple.com/documentation/coregraphics/cgcolor/1456637-alpha)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CGColorGetAlpha (     CGColorRef color ); ``` |
| To | ``` CGFloat CGColorGetAlpha (     CGColorRef _Nullable color ); ``` |

Modified [CGColorGetColorSpace()](https://developer.apple.com/documentation/coregraphics/1455744-cgcolorgetcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorGetColorSpace (     CGColorRef color ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorGetColorSpace (     CGColorRef _Nullable color ); ``` |

Modified [CGColorGetComponents()](https://developer.apple.com/documentation/coregraphics/1455930-cgcolorgetcomponents)

|  | Declaration |
| --- | --- |
| From | ``` const CGFloat * CGColorGetComponents (     CGColorRef color ); ``` |
| To | ``` const CGFloat * _Nullable CGColorGetComponents (     CGColorRef _Nullable color ); ``` |

Modified [CGColorGetConstantColor()](https://developer.apple.com/documentation/coregraphics/1454283-cgcolorgetconstantcolor)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorGetConstantColor (     CFStringRef colorName ); ``` |
| To | ``` CGColorRef _Nullable CGColorGetConstantColor (     CFStringRef _Nullable colorName ); ``` |

Modified [CGColorGetNumberOfComponents()](https://developer.apple.com/documentation/coregraphics/cgcolor/1454130-numberofcomponents)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGColorGetNumberOfComponents (     CGColorRef color ); ``` |
| To | ``` size_t CGColorGetNumberOfComponents (     CGColorRef _Nullable color ); ``` |

Modified [CGColorGetPattern()](https://developer.apple.com/documentation/coregraphics/1455937-cgcolorgetpattern)

|  | Declaration |
| --- | --- |
| From | ``` CGPatternRef CGColorGetPattern (     CGColorRef color ); ``` |
| To | ``` CGPatternRef _Nullable CGColorGetPattern (     CGColorRef _Nullable color ); ``` |

Modified [CGColorRelease()](https://developer.apple.com/documentation/coregraphics/1586340-cgcolorrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGColorRelease (     CGColorRef color ); ``` |
| To | ``` void CGColorRelease (     CGColorRef _Nullable color ); ``` |

Modified [CGColorRetain()](https://developer.apple.com/documentation/coregraphics/1586339-cgcolorretain)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRef CGColorRetain (     CGColorRef color ); ``` |
| To | ``` CGColorRef _Nullable CGColorRetain (     CGColorRef _Nullable color ); ``` |

#### CGColorSpace.h

Added [kCGColorSpaceACESCGLinear](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408841-acescglinear)Added [kCGColorSpaceGenericXYZ](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408844-genericxyz)Added [kCGColorSpaceITUR_2020](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408901-itur_2020)Added [kCGColorSpaceITUR_709](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408906-itur_709)Added [kCGColorSpaceROMMRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacerommrgb)Modified [CGColorSpaceCopyICCProfile()](https://developer.apple.com/documentation/coregraphics/1408889-cgcolorspacecopyiccprofile)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGColorSpaceCopyICCProfile (     CGColorSpaceRef space ); ``` |
| To | ``` CFDataRef _Nullable CGColorSpaceCopyICCProfile (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceCopyName()](https://developer.apple.com/documentation/coregraphics/1408903-cgcolorspacecopyname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGColorSpaceCopyName (     CGColorSpaceRef space ); ``` |
| To | ``` CFStringRef _Nullable CGColorSpaceCopyName (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceCreateCalibratedGray()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408887-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateCalibratedGray (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     CGFloat gamma ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateCalibratedGray (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     CGFloat gamma ); ``` |

Modified [CGColorSpaceCreateCalibratedRGB()](https://developer.apple.com/documentation/coregraphics/1408861-cgcolorspacecreatecalibratedrgb)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateCalibratedRGB (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     const CGFloat gamma[3],     const CGFloat matrix[9] ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateCalibratedRGB (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     const CGFloat gamma[3],     const CGFloat matrix[9] ); ``` |

Modified [CGColorSpaceCreateDeviceCMYK()](https://developer.apple.com/documentation/coregraphics/1408897-cgcolorspacecreatedevicecmyk)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateDeviceCMYK (     void ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateDeviceCMYK (     void ); ``` |

Modified [CGColorSpaceCreateDeviceGray()](https://developer.apple.com/documentation/coregraphics/1408908-cgcolorspacecreatedevicegray)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateDeviceGray (     void ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateDeviceGray (     void ); ``` |

Modified [CGColorSpaceCreateDeviceRGB()](https://developer.apple.com/documentation/coregraphics/1408837-cgcolorspacecreatedevicergb)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateDeviceRGB (     void ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateDeviceRGB (     void ); ``` |

Modified [CGColorSpaceCreateICCBased()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408881-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateICCBased (     size_t nComponents,     const CGFloat *range,     CGDataProviderRef profile,     CGColorSpaceRef alternate ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateICCBased (     size_t nComponents,     const CGFloat * _Nullable range,     CGDataProviderRef _Nullable profile,     CGColorSpaceRef _Nullable alternate ); ``` |

Modified [CGColorSpaceCreateIndexed()](https://developer.apple.com/documentation/coregraphics/1408899-cgcolorspacecreateindexed)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateIndexed (     CGColorSpaceRef baseSpace,     size_t lastIndex,     const unsigned char *colorTable ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateIndexed (     CGColorSpaceRef _Nullable baseSpace,     size_t lastIndex,     const unsigned char * _Nullable colorTable ); ``` |

Modified [CGColorSpaceCreateLab()](https://developer.apple.com/documentation/coregraphics/1408879-cgcolorspacecreatelab)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateLab (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     const CGFloat range[4] ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateLab (     const CGFloat whitePoint[3],     const CGFloat blackPoint[3],     const CGFloat range[4] ); ``` |

Modified [CGColorSpaceCreatePattern()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408869-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreatePattern (     CGColorSpaceRef baseSpace ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreatePattern (     CGColorSpaceRef _Nullable baseSpace ); ``` |

Modified [CGColorSpaceCreateWithICCProfile()](https://developer.apple.com/documentation/coregraphics/1408895-cgcolorspacecreatewithiccprofile)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateWithICCProfile (     CFDataRef data ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateWithICCProfile (     CFDataRef _Nullable data ); ``` |

Modified [CGColorSpaceCreateWithName()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408921-init)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateWithName (     CFStringRef name ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateWithName (     CFStringRef _Nullable name ); ``` |

Modified [CGColorSpaceCreateWithPlatformColorSpace()](https://developer.apple.com/documentation/coregraphics/1408850-cgcolorspacecreatewithplatformco)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceCreateWithPlatformColorSpace (     const void *ref ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceCreateWithPlatformColorSpace (     const void * _Nullable ref ); ``` |

Modified [CGColorSpaceGetBaseColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408839-basecolorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceGetBaseColorSpace (     CGColorSpaceRef space ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceGetBaseColorSpace (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceGetColorTable()](https://developer.apple.com/documentation/coregraphics/1408853-cgcolorspacegetcolortable)

|  | Declaration |
| --- | --- |
| From | ``` void CGColorSpaceGetColorTable (     CGColorSpaceRef space,     uint8_t *table ); ``` |
| To | ``` void CGColorSpaceGetColorTable (     CGColorSpaceRef _Nullable space,     uint8_t * _Nullable table ); ``` |

Modified [CGColorSpaceGetColorTableCount()](https://developer.apple.com/documentation/coregraphics/1408883-cgcolorspacegetcolortablecount)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGColorSpaceGetColorTableCount (     CGColorSpaceRef space ); ``` |
| To | ``` size_t CGColorSpaceGetColorTableCount (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceGetModel()](https://developer.apple.com/documentation/coregraphics/1408854-cgcolorspacegetmodel)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceModel CGColorSpaceGetModel (     CGColorSpaceRef space ); ``` |
| To | ``` CGColorSpaceModel CGColorSpaceGetModel (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceGetNumberOfComponents()](https://developer.apple.com/documentation/coregraphics/1408848-cgcolorspacegetnumberofcomponent)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGColorSpaceGetNumberOfComponents (     CGColorSpaceRef space ); ``` |
| To | ``` size_t CGColorSpaceGetNumberOfComponents (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceRelease()](https://developer.apple.com/documentation/coregraphics/1408855-cgcolorspacerelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGColorSpaceRelease (     CGColorSpaceRef space ); ``` |
| To | ``` void CGColorSpaceRelease (     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGColorSpaceRetain()](https://developer.apple.com/documentation/coregraphics/1408885-cgcolorspaceretain)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGColorSpaceRetain (     CGColorSpaceRef space ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGColorSpaceRetain (     CGColorSpaceRef _Nullable space ); ``` |

#### CGContext.h

Modified [CGContextAddArc()](https://developer.apple.com/documentation/coregraphics/1455756-cgcontextaddarc)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddArc (     CGContextRef c,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat endAngle,     int clockwise ); ``` |
| To | ``` void CGContextAddArc (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat endAngle,     int clockwise ); ``` |

Modified [CGContextAddArcToPoint()](https://developer.apple.com/documentation/coregraphics/1456238-cgcontextaddarctopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddArcToPoint (     CGContextRef c,     CGFloat x1,     CGFloat y1,     CGFloat x2,     CGFloat y2,     CGFloat radius ); ``` |
| To | ``` void CGContextAddArcToPoint (     CGContextRef _Nullable c,     CGFloat x1,     CGFloat y1,     CGFloat x2,     CGFloat y2,     CGFloat radius ); ``` |

Modified [CGContextAddCurveToPoint()](https://developer.apple.com/documentation/coregraphics/1456393-cgcontextaddcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddCurveToPoint (     CGContextRef c,     CGFloat cp1x,     CGFloat cp1y,     CGFloat cp2x,     CGFloat cp2y,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGContextAddCurveToPoint (     CGContextRef _Nullable c,     CGFloat cp1x,     CGFloat cp1y,     CGFloat cp2x,     CGFloat cp2y,     CGFloat x,     CGFloat y ); ``` |

Modified [CGContextAddEllipseInRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456420-addellipse)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextAddEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextAddLines()](https://developer.apple.com/documentation/coregraphics/1455461-cgcontextaddlines)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddLines (     CGContextRef c,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGContextAddLines (     CGContextRef _Nullable c,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGContextAddLineToPoint()](https://developer.apple.com/documentation/coregraphics/1455213-cgcontextaddlinetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddLineToPoint (     CGContextRef c,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGContextAddLineToPoint (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y ); ``` |

Modified [CGContextAddPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456628-addpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddPath (     CGContextRef context,     CGPathRef path ); ``` |
| To | ``` void CGContextAddPath (     CGContextRef _Nullable c,     CGPathRef _Nullable path ); ``` |

Modified [CGContextAddQuadCurveToPoint()](https://developer.apple.com/documentation/coregraphics/1454268-cgcontextaddquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddQuadCurveToPoint (     CGContextRef c,     CGFloat cpx,     CGFloat cpy,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGContextAddQuadCurveToPoint (     CGContextRef _Nullable c,     CGFloat cpx,     CGFloat cpy,     CGFloat x,     CGFloat y ); ``` |

Modified [CGContextAddRect()](https://developer.apple.com/documentation/coregraphics/1456617-cgcontextaddrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddRect (     CGContextRef c,     CGRect rect ); ``` |
| To | ``` void CGContextAddRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextAddRects()](https://developer.apple.com/documentation/coregraphics/1454734-cgcontextaddrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextAddRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextAddRects (     CGContextRef _Nullable c,     const CGRect * _Nullable rects,     size_t count ); ``` |

Modified [CGContextBeginPage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454794-beginpage)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginPage (     CGContextRef c,     const CGRect *mediaBox ); ``` |
| To | ``` void CGContextBeginPage (     CGContextRef _Nullable c,     const CGRect * _Nullable mediaBox ); ``` |

Modified [CGContextBeginPath()](https://developer.apple.com/documentation/coregraphics/1456635-cgcontextbeginpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginPath (     CGContextRef c ); ``` |
| To | ``` void CGContextBeginPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextBeginTransparencyLayer()](https://developer.apple.com/documentation/coregraphics/1456011-cgcontextbegintransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginTransparencyLayer (     CGContextRef context,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` void CGContextBeginTransparencyLayer (     CGContextRef _Nullable c,     CFDictionaryRef _Nullable auxiliaryInfo ); ``` |

Modified [CGContextBeginTransparencyLayerWithRect()](https://developer.apple.com/documentation/coregraphics/1454368-cgcontextbegintransparencylayerw)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextBeginTransparencyLayerWithRect (     CGContextRef context,     CGRect rect,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` void CGContextBeginTransparencyLayerWithRect (     CGContextRef _Nullable c,     CGRect rect,     CFDictionaryRef _Nullable auxInfo ); ``` |

Modified [CGContextClearRect()](https://developer.apple.com/documentation/coregraphics/1456457-cgcontextclearrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClearRect (     CGContextRef c,     CGRect rect ); ``` |
| To | ``` void CGContextClearRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextClip()](https://developer.apple.com/documentation/coregraphics/1455262-cgcontextclip)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClip (     CGContextRef c ); ``` |
| To | ``` void CGContextClip (     CGContextRef _Nullable c ); ``` |

Modified [CGContextClipToMask()](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClipToMask (     CGContextRef c,     CGRect rect,     CGImageRef mask ); ``` |
| To | ``` void CGContextClipToMask (     CGContextRef _Nullable c,     CGRect rect,     CGImageRef _Nullable mask ); ``` |

Modified [CGContextClipToRect()](https://developer.apple.com/documentation/coregraphics/1454716-cgcontextcliptorect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClipToRect (     CGContextRef c,     CGRect rect ); ``` |
| To | ``` void CGContextClipToRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextClipToRects()](https://developer.apple.com/documentation/coregraphics/1454626-cgcontextcliptorects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClipToRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextClipToRects (     CGContextRef _Nullable c,     const CGRect * _Nonnull rects,     size_t count ); ``` |

Modified [CGContextClosePath()](https://developer.apple.com/documentation/coregraphics/1454508-cgcontextclosepath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextClosePath (     CGContextRef c ); ``` |
| To | ``` void CGContextClosePath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextConcatCTM()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454897-concatenate)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextConcatCTM (     CGContextRef c,     CGAffineTransform transform ); ``` |
| To | ``` void CGContextConcatCTM (     CGContextRef _Nullable c,     CGAffineTransform transform ); ``` |

Modified [CGContextConvertPointToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455916-converttodevicespace)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextConvertPointToDeviceSpace (     CGContextRef context,     CGPoint point ); ``` |
| To | ``` CGPoint CGContextConvertPointToDeviceSpace (     CGContextRef _Nullable c,     CGPoint point ); ``` |

Modified [CGContextConvertPointToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456451-converttouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextConvertPointToUserSpace (     CGContextRef context,     CGPoint point ); ``` |
| To | ``` CGPoint CGContextConvertPointToUserSpace (     CGContextRef _Nullable c,     CGPoint point ); ``` |

Modified [CGContextConvertRectToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextConvertRectToDeviceSpace (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` CGRect CGContextConvertRectToDeviceSpace (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextConvertRectToUserSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454165-converttouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextConvertRectToUserSpace (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` CGRect CGContextConvertRectToUserSpace (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextConvertSizeToDeviceSpace()](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CGContextConvertSizeToDeviceSpace (     CGContextRef context,     CGSize size ); ``` |
| To | ``` CGSize CGContextConvertSizeToDeviceSpace (     CGContextRef _Nullable c,     CGSize size ); ``` |

Modified [CGContextConvertSizeToUserSpace()](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CGContextConvertSizeToUserSpace (     CGContextRef context,     CGSize size ); ``` |
| To | ``` CGSize CGContextConvertSizeToUserSpace (     CGContextRef _Nullable c,     CGSize size ); ``` |

Modified [CGContextCopyPath()](https://developer.apple.com/documentation/coregraphics/1455397-cgcontextcopypath)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGContextCopyPath (     CGContextRef context ); ``` |
| To | ``` CGPathRef _Nullable CGContextCopyPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextDrawImage()](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawImage (     CGContextRef c,     CGRect rect,     CGImageRef image ); ``` |
| To | ``` void CGContextDrawImage (     CGContextRef _Nullable c,     CGRect rect,     CGImageRef _Nullable image ); ``` |

Modified [CGContextDrawLinearGradient()](https://developer.apple.com/documentation/coregraphics/1454782-cgcontextdrawlineargradient)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawLinearGradient (     CGContextRef context,     CGGradientRef gradient,     CGPoint startPoint,     CGPoint endPoint,     CGGradientDrawingOptions options ); ``` |
| To | ``` void CGContextDrawLinearGradient (     CGContextRef _Nullable c,     CGGradientRef _Nullable gradient,     CGPoint startPoint,     CGPoint endPoint,     CGGradientDrawingOptions options ); ``` |

Modified [CGContextDrawPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455195-drawpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawPath (     CGContextRef c,     CGPathDrawingMode mode ); ``` |
| To | ``` void CGContextDrawPath (     CGContextRef _Nullable c,     CGPathDrawingMode mode ); ``` |

Modified [CGContextDrawPDFDocument()](https://developer.apple.com/documentation/coregraphics/1586508-cgcontextdrawpdfdocument)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawPDFDocument (     CGContextRef c,     CGRect rect,     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` void CGContextDrawPDFDocument (     CGContextRef _Nullable c,     CGRect rect,     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGContextDrawPDFPage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456255-drawpdfpage)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawPDFPage (     CGContextRef c,     CGPDFPageRef page ); ``` |
| To | ``` void CGContextDrawPDFPage (     CGContextRef _Nullable c,     CGPDFPageRef _Nullable page ); ``` |

Modified [CGContextDrawRadialGradient()](https://developer.apple.com/documentation/coregraphics/1455923-cgcontextdrawradialgradient)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawRadialGradient (     CGContextRef context,     CGGradientRef gradient,     CGPoint startCenter,     CGFloat startRadius,     CGPoint endCenter,     CGFloat endRadius,     CGGradientDrawingOptions options ); ``` |
| To | ``` void CGContextDrawRadialGradient (     CGContextRef _Nullable c,     CGGradientRef _Nullable gradient,     CGPoint startCenter,     CGFloat startRadius,     CGPoint endCenter,     CGFloat endRadius,     CGGradientDrawingOptions options ); ``` |

Modified [CGContextDrawShading()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456643-drawshading)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawShading (     CGContextRef context,     CGShadingRef shading ); ``` |
| To | ``` void CGContextDrawShading (     CGContextRef _Nullable c,     CGShadingRef _Nullable shading ); ``` |

Modified [CGContextDrawTiledImage()](https://developer.apple.com/documentation/coregraphics/1456240-cgcontextdrawtiledimage)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawTiledImage (     CGContextRef c,     CGRect rect,     CGImageRef image ); ``` |
| To | ``` void CGContextDrawTiledImage (     CGContextRef _Nullable c,     CGRect rect,     CGImageRef _Nullable image ); ``` |

Modified [CGContextEndPage()](https://developer.apple.com/documentation/coregraphics/1455027-cgcontextendpage)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextEndPage (     CGContextRef c ); ``` |
| To | ``` void CGContextEndPage (     CGContextRef _Nullable c ); ``` |

Modified [CGContextEndTransparencyLayer()](https://developer.apple.com/documentation/coregraphics/1456554-cgcontextendtransparencylayer)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextEndTransparencyLayer (     CGContextRef context ); ``` |
| To | ``` void CGContextEndTransparencyLayer (     CGContextRef _Nullable c ); ``` |

Modified [CGContextEOClip()](https://developer.apple.com/documentation/coregraphics/1455944-cgcontexteoclip)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextEOClip (     CGContextRef c ); ``` |
| To | ``` void CGContextEOClip (     CGContextRef _Nullable c ); ``` |

Modified [CGContextEOFillPath()](https://developer.apple.com/documentation/coregraphics/1454865-cgcontexteofillpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextEOFillPath (     CGContextRef c ); ``` |
| To | ``` void CGContextEOFillPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextFillEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1454371-cgcontextfillellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextFillEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextFillPath()](https://developer.apple.com/documentation/coregraphics/1456306-cgcontextfillpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillPath (     CGContextRef c ); ``` |
| To | ``` void CGContextFillPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextFillRect()](https://developer.apple.com/documentation/coregraphics/1454700-cgcontextfillrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillRect (     CGContextRef c,     CGRect rect ); ``` |
| To | ``` void CGContextFillRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextFillRects()](https://developer.apple.com/documentation/coregraphics/1454132-cgcontextfillrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFillRects (     CGContextRef c,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGContextFillRects (     CGContextRef _Nullable c,     const CGRect * _Nullable rects,     size_t count ); ``` |

Modified [CGContextFlush()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454895-flush)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextFlush (     CGContextRef c ); ``` |
| To | ``` void CGContextFlush (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetClipBoundingBox()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455387-boundingboxofclippath)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextGetClipBoundingBox (     CGContextRef c ); ``` |
| To | ``` CGRect CGContextGetClipBoundingBox (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetCTM()](https://developer.apple.com/documentation/coregraphics/1454691-cgcontextgetctm)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CGContextGetCTM (     CGContextRef c ); ``` |
| To | ``` CGAffineTransform CGContextGetCTM (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1454940-cgcontextgetinterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` CGInterpolationQuality CGContextGetInterpolationQuality (     CGContextRef context ); ``` |
| To | ``` CGInterpolationQuality CGContextGetInterpolationQuality (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetPathBoundingBox()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454577-boundingboxofpath)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGContextGetPathBoundingBox (     CGContextRef context ); ``` |
| To | ``` CGRect CGContextGetPathBoundingBox (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetPathCurrentPoint()](https://developer.apple.com/documentation/coregraphics/1454788-cgcontextgetpathcurrentpoint)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextGetPathCurrentPoint (     CGContextRef context ); ``` |
| To | ``` CGPoint CGContextGetPathCurrentPoint (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetTextMatrix()](https://developer.apple.com/documentation/coregraphics/1456154-cgcontextgettextmatrix)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CGContextGetTextMatrix (     CGContextRef c ); ``` |
| To | ``` CGAffineTransform CGContextGetTextMatrix (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetTextPosition()](https://developer.apple.com/documentation/coregraphics/1454687-cgcontextgettextposition)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGContextGetTextPosition (     CGContextRef context ); ``` |
| To | ``` CGPoint CGContextGetTextPosition (     CGContextRef _Nullable c ); ``` |

Modified [CGContextGetUserSpaceToDeviceSpaceTransform()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455677-userspacetodevicespacetransform)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform (     CGContextRef context ); ``` |
| To | ``` CGAffineTransform CGContextGetUserSpaceToDeviceSpaceTransform (     CGContextRef _Nullable c ); ``` |

Modified [CGContextIsPathEmpty()](https://developer.apple.com/documentation/coregraphics/1455772-cgcontextispathempty)

|  | Declaration |
| --- | --- |
| From | ``` bool CGContextIsPathEmpty (     CGContextRef context ); ``` |
| To | ``` bool CGContextIsPathEmpty (     CGContextRef _Nullable c ); ``` |

Modified [CGContextMoveToPoint()](https://developer.apple.com/documentation/coregraphics/1454738-cgcontextmovetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextMoveToPoint (     CGContextRef c,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGContextMoveToPoint (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y ); ``` |

Modified [CGContextPathContainsPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454778-pathcontains)

|  | Declaration |
| --- | --- |
| From | ``` bool CGContextPathContainsPoint (     CGContextRef context,     CGPoint point,     CGPathDrawingMode mode ); ``` |
| To | ``` bool CGContextPathContainsPoint (     CGContextRef _Nullable c,     CGPoint point,     CGPathDrawingMode mode ); ``` |

Modified [CGContextRelease()](https://developer.apple.com/documentation/coregraphics/1586509-cgcontextrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextRelease (     CGContextRef c ); ``` |
| To | ``` void CGContextRelease (     CGContextRef _Nullable c ); ``` |

Modified [CGContextReplacePathWithStrokedPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454517-replacepathwithstrokedpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextReplacePathWithStrokedPath (     CGContextRef c ); ``` |
| To | ``` void CGContextReplacePathWithStrokedPath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextRestoreGState()](https://developer.apple.com/documentation/coregraphics/1455391-cgcontextrestoregstate)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextRestoreGState (     CGContextRef c ); ``` |
| To | ``` void CGContextRestoreGState (     CGContextRef _Nullable c ); ``` |

Modified [CGContextRetain()](https://developer.apple.com/documentation/coregraphics/1586506-cgcontextretain)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGContextRetain (     CGContextRef c ); ``` |
| To | ``` CGContextRef _Nullable CGContextRetain (     CGContextRef _Nullable c ); ``` |

Modified [CGContextRotateCTM()](https://developer.apple.com/documentation/coregraphics/1456228-cgcontextrotatectm)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextRotateCTM (     CGContextRef c,     CGFloat angle ); ``` |
| To | ``` void CGContextRotateCTM (     CGContextRef _Nullable c,     CGFloat angle ); ``` |

Modified [CGContextSaveGState()](https://developer.apple.com/documentation/coregraphics/1456156-cgcontextsavegstate)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSaveGState (     CGContextRef c ); ``` |
| To | ``` void CGContextSaveGState (     CGContextRef _Nullable c ); ``` |

Modified [CGContextScaleCTM()](https://developer.apple.com/documentation/coregraphics/1454659-cgcontextscalectm)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextScaleCTM (     CGContextRef c,     CGFloat sx,     CGFloat sy ); ``` |
| To | ``` void CGContextScaleCTM (     CGContextRef _Nullable c,     CGFloat sx,     CGFloat sy ); ``` |

Modified [CGContextSelectFont()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586511-selectfont)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSelectFont (     CGContextRef c,     const char *name,     CGFloat size,     CGTextEncoding textEncoding ); ``` |
| To | ``` void CGContextSelectFont (     CGContextRef _Nullable c,     const char * _Nullable name,     CGFloat size,     CGTextEncoding textEncoding ); ``` |

Modified [CGContextSetAllowsAntialiasing()](https://developer.apple.com/documentation/coregraphics/1456310-cgcontextsetallowsantialiasing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsAntialiasing (     CGContextRef context,     bool allowsAntialiasing ); ``` |
| To | ``` void CGContextSetAllowsAntialiasing (     CGContextRef _Nullable c,     bool allowsAntialiasing ); ``` |

Modified [CGContextSetAllowsFontSmoothing()](https://developer.apple.com/documentation/coregraphics/1454767-cgcontextsetallowsfontsmoothing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSmoothing (     CGContextRef context,     bool allowsFontSmoothing ); ``` |
| To | ``` void CGContextSetAllowsFontSmoothing (     CGContextRef _Nullable c,     bool allowsFontSmoothing ); ``` |

Modified [CGContextSetAllowsFontSubpixelPositioning()](https://developer.apple.com/documentation/coregraphics/1454942-cgcontextsetallowsfontsubpixelpo)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSubpixelPositioning (     CGContextRef context,     bool allowsFontSubpixelPositioning ); ``` |
| To | ``` void CGContextSetAllowsFontSubpixelPositioning (     CGContextRef _Nullable c,     bool allowsFontSubpixelPositioning ); ``` |

Modified [CGContextSetAllowsFontSubpixelQuantization()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456263-setallowsfontsubpixelquantizatio)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAllowsFontSubpixelQuantization (     CGContextRef context,     bool allowsFontSubpixelQuantization ); ``` |
| To | ``` void CGContextSetAllowsFontSubpixelQuantization (     CGContextRef _Nullable c,     bool allowsFontSubpixelQuantization ); ``` |

Modified [CGContextSetAlpha()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456404-setalpha)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetAlpha (     CGContextRef c,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetAlpha (     CGContextRef _Nullable c,     CGFloat alpha ); ``` |

Modified [CGContextSetBlendMode()](https://developer.apple.com/documentation/coregraphics/1455994-cgcontextsetblendmode)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetBlendMode (     CGContextRef context,     CGBlendMode mode ); ``` |
| To | ``` void CGContextSetBlendMode (     CGContextRef _Nullable c,     CGBlendMode mode ); ``` |

Modified [CGContextSetCharacterSpacing()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454786-setcharacterspacing)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCharacterSpacing (     CGContextRef context,     CGFloat spacing ); ``` |
| To | ``` void CGContextSetCharacterSpacing (     CGContextRef _Nullable c,     CGFloat spacing ); ``` |

Modified [CGContextSetCMYKFillColor()](https://developer.apple.com/documentation/coregraphics/1454214-cgcontextsetcmykfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCMYKFillColor (     CGContextRef context,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetCMYKFillColor (     CGContextRef _Nullable c,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |

Modified [CGContextSetCMYKStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455358-cgcontextsetcmykstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetCMYKStrokeColor (     CGContextRef context,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetCMYKStrokeColor (     CGContextRef _Nullable c,     CGFloat cyan,     CGFloat magenta,     CGFloat yellow,     CGFloat black,     CGFloat alpha ); ``` |

Modified [CGContextSetFillColor()](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillColor (     CGContextRef context,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetFillColor (     CGContextRef _Nullable c,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetFillColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455151-setfillcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillColorSpace (     CGContextRef context,     CGColorSpaceRef space ); ``` |
| To | ``` void CGContextSetFillColorSpace (     CGContextRef _Nullable c,     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGContextSetFillColorWithColor()](https://developer.apple.com/documentation/coregraphics/1454079-cgcontextsetfillcolorwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillColorWithColor (     CGContextRef c,     CGColorRef color ); ``` |
| To | ``` void CGContextSetFillColorWithColor (     CGContextRef _Nullable c,     CGColorRef _Nullable color ); ``` |

Modified [CGContextSetFillPattern()](https://developer.apple.com/documentation/coregraphics/1456334-cgcontextsetfillpattern)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFillPattern (     CGContextRef context,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetFillPattern (     CGContextRef _Nullable c,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetFlatness()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455798-setflatness)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFlatness (     CGContextRef c,     CGFloat flatness ); ``` |
| To | ``` void CGContextSetFlatness (     CGContextRef _Nullable c,     CGFloat flatness ); ``` |

Modified [CGContextSetFont()](https://developer.apple.com/documentation/coregraphics/1454950-cgcontextsetfont)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFont (     CGContextRef c,     CGFontRef font ); ``` |
| To | ``` void CGContextSetFont (     CGContextRef _Nullable c,     CGFontRef _Nullable font ); ``` |

Modified [CGContextSetFontSize()](https://developer.apple.com/documentation/coregraphics/1456426-cgcontextsetfontsize)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetFontSize (     CGContextRef c,     CGFloat size ); ``` |
| To | ``` void CGContextSetFontSize (     CGContextRef _Nullable c,     CGFloat size ); ``` |

Modified [CGContextSetGrayFillColor()](https://developer.apple.com/documentation/coregraphics/1454255-cgcontextsetgrayfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetGrayFillColor (     CGContextRef context,     CGFloat gray,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetGrayFillColor (     CGContextRef _Nullable c,     CGFloat gray,     CGFloat alpha ); ``` |

Modified [CGContextSetGrayStrokeColor()](https://developer.apple.com/documentation/coregraphics/1455209-cgcontextsetgraystrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetGrayStrokeColor (     CGContextRef context,     CGFloat gray,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetGrayStrokeColor (     CGContextRef _Nullable c,     CGFloat gray,     CGFloat alpha ); ``` |

Modified [CGContextSetInterpolationQuality()](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetInterpolationQuality (     CGContextRef context,     CGInterpolationQuality quality ); ``` |
| To | ``` void CGContextSetInterpolationQuality (     CGContextRef _Nullable c,     CGInterpolationQuality quality ); ``` |

Modified [CGContextSetLineCap()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454326-setlinecap)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetLineCap (     CGContextRef c,     CGLineCap cap ); ``` |
| To | ``` void CGContextSetLineCap (     CGContextRef _Nullable c,     CGLineCap cap ); ``` |

Modified [CGContextSetLineDash()](https://developer.apple.com/documentation/coregraphics/1455911-cgcontextsetlinedash)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetLineDash (     CGContextRef c,     CGFloat phase,     const CGFloat lengths[],     size_t count ); ``` |
| To | ``` void CGContextSetLineDash (     CGContextRef _Nullable c,     CGFloat phase,     const CGFloat * _Nullable lengths,     size_t count ); ``` |

Modified [CGContextSetLineJoin()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455973-setlinejoin)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetLineJoin (     CGContextRef c,     CGLineJoin join ); ``` |
| To | ``` void CGContextSetLineJoin (     CGContextRef _Nullable c,     CGLineJoin join ); ``` |

Modified [CGContextSetLineWidth()](https://developer.apple.com/documentation/coregraphics/1455270-cgcontextsetlinewidth)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetLineWidth (     CGContextRef c,     CGFloat width ); ``` |
| To | ``` void CGContextSetLineWidth (     CGContextRef _Nullable c,     CGFloat width ); ``` |

Modified [CGContextSetMiterLimit()](https://developer.apple.com/documentation/coregraphics/1456499-cgcontextsetmiterlimit)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetMiterLimit (     CGContextRef c,     CGFloat limit ); ``` |
| To | ``` void CGContextSetMiterLimit (     CGContextRef _Nullable c,     CGFloat limit ); ``` |

Modified [CGContextSetPatternPhase()](https://developer.apple.com/documentation/coregraphics/1455334-cgcontextsetpatternphase)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetPatternPhase (     CGContextRef context,     CGSize phase ); ``` |
| To | ``` void CGContextSetPatternPhase (     CGContextRef _Nullable c,     CGSize phase ); ``` |

Modified [CGContextSetRenderingIntent()](https://developer.apple.com/documentation/coregraphics/1455544-cgcontextsetrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRenderingIntent (     CGContextRef context,     CGColorRenderingIntent intent ); ``` |
| To | ``` void CGContextSetRenderingIntent (     CGContextRef _Nullable c,     CGColorRenderingIntent intent ); ``` |

Modified [CGContextSetRGBFillColor()](https://developer.apple.com/documentation/coregraphics/1455624-cgcontextsetrgbfillcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRGBFillColor (     CGContextRef context,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetRGBFillColor (     CGContextRef _Nullable c,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |

Modified [CGContextSetRGBStrokeColor()](https://developer.apple.com/documentation/coregraphics/1456378-cgcontextsetrgbstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetRGBStrokeColor (     CGContextRef context,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |
| To | ``` void CGContextSetRGBStrokeColor (     CGContextRef _Nullable c,     CGFloat red,     CGFloat green,     CGFloat blue,     CGFloat alpha ); ``` |

Modified [CGContextSetShadow()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456082-setshadow)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShadow (     CGContextRef context,     CGSize offset,     CGFloat blur ); ``` |
| To | ``` void CGContextSetShadow (     CGContextRef _Nullable c,     CGSize offset,     CGFloat blur ); ``` |

Modified [CGContextSetShadowWithColor()](https://developer.apple.com/documentation/coregraphics/1455205-cgcontextsetshadowwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShadowWithColor (     CGContextRef context,     CGSize offset,     CGFloat blur,     CGColorRef color ); ``` |
| To | ``` void CGContextSetShadowWithColor (     CGContextRef _Nullable c,     CGSize offset,     CGFloat blur,     CGColorRef _Nullable color ); ``` |

Modified [CGContextSetShouldAntialias()](https://developer.apple.com/documentation/coregraphics/1455178-cgcontextsetshouldantialias)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldAntialias (     CGContextRef context,     bool shouldAntialias ); ``` |
| To | ``` void CGContextSetShouldAntialias (     CGContextRef _Nullable c,     bool shouldAntialias ); ``` |

Modified [CGContextSetShouldSmoothFonts()](https://developer.apple.com/documentation/coregraphics/1455816-cgcontextsetshouldsmoothfonts)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSmoothFonts (     CGContextRef context,     bool shouldSmoothFonts ); ``` |
| To | ``` void CGContextSetShouldSmoothFonts (     CGContextRef _Nullable c,     bool shouldSmoothFonts ); ``` |

Modified [CGContextSetShouldSubpixelPositionFonts()](https://developer.apple.com/documentation/coregraphics/1455671-cgcontextsetshouldsubpixelpositi)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSubpixelPositionFonts (     CGContextRef context,     bool shouldSubpixelPositionFonts ); ``` |
| To | ``` void CGContextSetShouldSubpixelPositionFonts (     CGContextRef _Nullable c,     bool shouldSubpixelPositionFonts ); ``` |

Modified [CGContextSetShouldSubpixelQuantizeFonts()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455766-setshouldsubpixelquantizefonts)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetShouldSubpixelQuantizeFonts (     CGContextRef context,     bool shouldSubpixelQuantizeFonts ); ``` |
| To | ``` void CGContextSetShouldSubpixelQuantizeFonts (     CGContextRef _Nullable c,     bool shouldSubpixelQuantizeFonts ); ``` |

Modified [CGContextSetStrokeColor()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456283-setstrokecolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokeColor (     CGContextRef context,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetStrokeColor (     CGContextRef _Nullable c,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetStrokeColorSpace()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454396-setstrokecolorspace)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokeColorSpace (     CGContextRef context,     CGColorSpaceRef space ); ``` |
| To | ``` void CGContextSetStrokeColorSpace (     CGContextRef _Nullable c,     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGContextSetStrokeColorWithColor()](https://developer.apple.com/documentation/coregraphics/1456196-cgcontextsetstrokecolorwithcolor)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokeColorWithColor (     CGContextRef c,     CGColorRef color ); ``` |
| To | ``` void CGContextSetStrokeColorWithColor (     CGContextRef _Nullable c,     CGColorRef _Nullable color ); ``` |

Modified [CGContextSetStrokePattern()](https://developer.apple.com/documentation/coregraphics/1454796-cgcontextsetstrokepattern)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetStrokePattern (     CGContextRef context,     CGPatternRef pattern,     const CGFloat components[] ); ``` |
| To | ``` void CGContextSetStrokePattern (     CGContextRef _Nullable c,     CGPatternRef _Nullable pattern,     const CGFloat * _Nullable components ); ``` |

Modified [CGContextSetTextDrawingMode()](https://developer.apple.com/documentation/coregraphics/1454253-cgcontextsettextdrawingmode)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetTextDrawingMode (     CGContextRef c,     CGTextDrawingMode mode ); ``` |
| To | ``` void CGContextSetTextDrawingMode (     CGContextRef _Nullable c,     CGTextDrawingMode mode ); ``` |

Modified [CGContextSetTextMatrix()](https://developer.apple.com/documentation/coregraphics/1455611-cgcontextsettextmatrix)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetTextMatrix (     CGContextRef c,     CGAffineTransform t ); ``` |
| To | ``` void CGContextSetTextMatrix (     CGContextRef _Nullable c,     CGAffineTransform t ); ``` |

Modified [CGContextSetTextPosition()](https://developer.apple.com/documentation/coregraphics/1456069-cgcontextsettextposition)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSetTextPosition (     CGContextRef c,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGContextSetTextPosition (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y ); ``` |

Modified [CGContextShowGlyphs()](https://developer.apple.com/documentation/coregraphics/1586500-cgcontextshowglyphs)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphs (     CGContextRef c,     const CGGlyph g[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphs (     CGContextRef _Nullable c,     const CGGlyph * _Nullable g,     size_t count ); ``` |

Modified [CGContextShowGlyphsAtPoint()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586502-showglyphsatpoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsAtPoint (     CGContextRef context,     CGFloat x,     CGFloat y,     const CGGlyph glyphs[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsAtPoint (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y,     const CGGlyph * _Nullable glyphs,     size_t count ); ``` |

Modified [CGContextShowGlyphsAtPositions()](https://developer.apple.com/documentation/coregraphics/1456200-cgcontextshowglyphsatpositions)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsAtPositions (     CGContextRef context,     const CGGlyph glyphs[],     const CGPoint positions[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsAtPositions (     CGContextRef _Nullable c,     const CGGlyph * _Nullable glyphs,     const CGPoint * _Nullable Lpositions,     size_t count ); ``` |

Modified [CGContextShowGlyphsWithAdvances()](https://developer.apple.com/documentation/coregraphics/1586503-cgcontextshowglyphswithadvances)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowGlyphsWithAdvances (     CGContextRef context,     const CGGlyph glyphs[],     const CGSize advances[],     size_t count ); ``` |
| To | ``` void CGContextShowGlyphsWithAdvances (     CGContextRef _Nullable c,     const CGGlyph * _Nullable glyphs,     const CGSize * _Nullable advances,     size_t count ); ``` |

Modified [CGContextShowText()](https://developer.apple.com/documentation/coregraphics/cgcontext/1586507-showtext)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowText (     CGContextRef c,     const char *string,     size_t length ); ``` |
| To | ``` void CGContextShowText (     CGContextRef _Nullable c,     const char * _Nullable string,     size_t length ); ``` |

Modified [CGContextShowTextAtPoint()](https://developer.apple.com/documentation/coregraphics/1586505-cgcontextshowtextatpoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextShowTextAtPoint (     CGContextRef c,     CGFloat x,     CGFloat y,     const char *string,     size_t length ); ``` |
| To | ``` void CGContextShowTextAtPoint (     CGContextRef _Nullable c,     CGFloat x,     CGFloat y,     const char * _Nullable string,     size_t length ); ``` |

Modified [CGContextStrokeEllipseInRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455774-strokeellipse)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeEllipseInRect (     CGContextRef context,     CGRect rect ); ``` |
| To | ``` void CGContextStrokeEllipseInRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextStrokeLineSegments()](https://developer.apple.com/documentation/coregraphics/1454389-cgcontextstrokelinesegments)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeLineSegments (     CGContextRef c,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGContextStrokeLineSegments (     CGContextRef _Nullable c,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGContextStrokePath()](https://developer.apple.com/documentation/coregraphics/1454490-cgcontextstrokepath)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokePath (     CGContextRef c ); ``` |
| To | ``` void CGContextStrokePath (     CGContextRef _Nullable c ); ``` |

Modified [CGContextStrokeRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454675-stroke)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeRect (     CGContextRef c,     CGRect rect ); ``` |
| To | ``` void CGContextStrokeRect (     CGContextRef _Nullable c,     CGRect rect ); ``` |

Modified [CGContextStrokeRectWithWidth()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454679-stroke)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextStrokeRectWithWidth (     CGContextRef c,     CGRect rect,     CGFloat width ); ``` |
| To | ``` void CGContextStrokeRectWithWidth (     CGContextRef _Nullable c,     CGRect rect,     CGFloat width ); ``` |

Modified [CGContextSynchronize()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455450-synchronize)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextSynchronize (     CGContextRef c ); ``` |
| To | ``` void CGContextSynchronize (     CGContextRef _Nullable c ); ``` |

Modified [CGContextTranslateCTM()](https://developer.apple.com/documentation/coregraphics/1455286-cgcontexttranslatectm)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextTranslateCTM (     CGContextRef c,     CGFloat tx,     CGFloat ty ); ``` |
| To | ``` void CGContextTranslateCTM (     CGContextRef _Nullable c,     CGFloat tx,     CGFloat ty ); ``` |

Modified [CGTextEncoding](https://developer.apple.com/documentation/coregraphics/cgtextencoding)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | -- |

Modified [kCGEncodingFontSpecific](https://developer.apple.com/documentation/coregraphics/cgtextencoding/encodingfontspecific)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

Modified [kCGEncodingMacRoman](https://developer.apple.com/documentation/coregraphics/cgtextencoding/encodingmacroman)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.9 |

#### CGDataConsumer.h

Modified [CGDataConsumerCreate()](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/1456428-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDataConsumerRef CGDataConsumerCreate (     void *info,     const CGDataConsumerCallbacks *callbacks ); ``` |
| To | ``` CGDataConsumerRef _Nullable CGDataConsumerCreate (     void * _Nullable info,     const CGDataConsumerCallbacks * _Nullable cbks ); ``` |

Modified [CGDataConsumerCreateWithCFData()](https://developer.apple.com/documentation/coregraphics/1456292-cgdataconsumercreatewithcfdata)

|  | Declaration |
| --- | --- |
| From | ``` CGDataConsumerRef CGDataConsumerCreateWithCFData (     CFMutableDataRef data ); ``` |
| To | ``` CGDataConsumerRef _Nullable CGDataConsumerCreateWithCFData (     CFMutableDataRef _Nullable data ); ``` |

Modified [CGDataConsumerCreateWithURL()](https://developer.apple.com/documentation/coregraphics/1454474-cgdataconsumercreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` CGDataConsumerRef CGDataConsumerCreateWithURL (     CFURLRef url ); ``` |
| To | ``` CGDataConsumerRef _Nullable CGDataConsumerCreateWithURL (     CFURLRef _Nullable url ); ``` |

Modified [CGDataConsumerRelease()](https://developer.apple.com/documentation/coregraphics/1508424-cgdataconsumerrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGDataConsumerRelease (     CGDataConsumerRef consumer ); ``` |
| To | ``` void CGDataConsumerRelease (     CGDataConsumerRef _Nullable consumer ); ``` |

Modified [CGDataConsumerRetain()](https://developer.apple.com/documentation/coregraphics/1508422-cgdataconsumerretain)

|  | Declaration |
| --- | --- |
| From | ``` CGDataConsumerRef CGDataConsumerRetain (     CGDataConsumerRef consumer ); ``` |
| To | ``` CGDataConsumerRef _Nullable CGDataConsumerRetain (     CGDataConsumerRef _Nullable consumer ); ``` |

#### CGDataProvider.h

Modified [CGDataProviderCopyData()](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408309-data)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGDataProviderCopyData (     CGDataProviderRef provider ); ``` |
| To | ``` CFDataRef _Nullable CGDataProviderCopyData (     CGDataProviderRef _Nullable provider ); ``` |

Modified [CGDataProviderCreateDirect()](https://developer.apple.com/documentation/coregraphics/1408282-cgdataprovidercreatedirect)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateDirect (     void *info,     off_t size,     const CGDataProviderDirectCallbacks *callbacks ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateDirect (     void * _Nullable info,     off_t size,     const CGDataProviderDirectCallbacks * _Nullable callbacks ); ``` |

Modified [CGDataProviderCreateSequential()](https://developer.apple.com/documentation/coregraphics/1408291-cgdataprovidercreatesequential)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateSequential (     void *info,     const CGDataProviderSequentialCallbacks *callbacks ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateSequential (     void * _Nullable info,     const CGDataProviderSequentialCallbacks * _Nullable callbacks ); ``` |

Modified [CGDataProviderCreateWithCFData()](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408284-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateWithCFData (     CFDataRef data ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateWithCFData (     CFDataRef _Nullable data ); ``` |

Modified [CGDataProviderCreateWithData()](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408288-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateWithData (     void *info,     const void *data,     size_t size,     CGDataProviderReleaseDataCallback releaseData ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateWithData (     void * _Nullable info,     const void * _Nullable data,     size_t size,     CGDataProviderReleaseDataCallback _Nullable releaseData ); ``` |

Modified [CGDataProviderCreateWithFilename()](https://developer.apple.com/documentation/coregraphics/1408294-cgdataprovidercreatewithfilename)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateWithFilename (     const char *filename ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateWithFilename (     const char * _Nullable filename ); ``` |

Modified [CGDataProviderCreateWithURL()](https://developer.apple.com/documentation/coregraphics/1408327-cgdataprovidercreatewithurl)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderCreateWithURL (     CFURLRef url ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderCreateWithURL (     CFURLRef _Nullable url ); ``` |

Modified [CGDataProviderRelease()](https://developer.apple.com/documentation/coregraphics/1408304-cgdataproviderrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGDataProviderRelease (     CGDataProviderRef provider ); ``` |
| To | ``` void CGDataProviderRelease (     CGDataProviderRef _Nullable provider ); ``` |

Modified [CGDataProviderRetain()](https://developer.apple.com/documentation/coregraphics/1408276-cgdataproviderretain)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGDataProviderRetain (     CGDataProviderRef provider ); ``` |
| To | ``` CGDataProviderRef _Nullable CGDataProviderRetain (     CGDataProviderRef _Nullable provider ); ``` |

#### CGDirectDisplay.h

Modified [CGDisplayAvailableModes()](https://developer.apple.com/documentation/coregraphics/1562068-cgdisplayavailablemodes)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGDisplayAvailableModes (     CGDirectDisplayID display ); ``` |
| To | ``` CFArrayRef _Nullable CGDisplayAvailableModes (     CGDirectDisplayID dsp ); ``` |

Modified [CGDisplayBestModeForParameters()](https://developer.apple.com/documentation/coregraphics/1562060-cgdisplaybestmodeforparameters)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGDisplayBestModeForParameters (     CGDirectDisplayID display,     size_t bitsPerPixel,     size_t width,     size_t height,     boolean_t *exactMatch ); ``` |
| To | ``` CFDictionaryRef _Nullable CGDisplayBestModeForParameters (     CGDirectDisplayID display,     size_t bitsPerPixel,     size_t width,     size_t height,     boolean_t * _Nullable exactMatch ); ``` |

Modified [CGDisplayBestModeForParametersAndRefreshRate()](https://developer.apple.com/documentation/coregraphics/1562066-cgdisplaybestmodeforparametersan)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGDisplayBestModeForParametersAndRefreshRate (     CGDirectDisplayID display,     size_t bitsPerPixel,     size_t width,     size_t height,     CGRefreshRate refreshRate,     boolean_t *exactMatch ); ``` |
| To | ``` CFDictionaryRef _Nullable CGDisplayBestModeForParametersAndRefreshRate (     CGDirectDisplayID display,     size_t bitsPerPixel,     size_t width,     size_t height,     CGRefreshRate refreshRate,     boolean_t * _Nullable exactMatch ); ``` |

Modified [CGDisplayCopyAllDisplayModes()](https://developer.apple.com/documentation/coregraphics/1455537-cgdisplaycopyalldisplaymodes)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGDisplayCopyAllDisplayModes (     CGDirectDisplayID display,     CFDictionaryRef options ); ``` |
| To | ``` CFArrayRef _Nullable CGDisplayCopyAllDisplayModes (     CGDirectDisplayID display,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGDisplayCopyDisplayMode()](https://developer.apple.com/documentation/coregraphics/1454099-cgdisplaycopydisplaymode)

|  | Declaration |
| --- | --- |
| From | ``` CGDisplayModeRef CGDisplayCopyDisplayMode (     CGDirectDisplayID display ); ``` |
| To | ``` CGDisplayModeRef _Nullable CGDisplayCopyDisplayMode (     CGDirectDisplayID display ); ``` |

Modified [CGDisplayCreateImage()](https://developer.apple.com/documentation/coregraphics/1455691-cgdisplaycreateimage)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGDisplayCreateImage (     CGDirectDisplayID displayID ); ``` |
| To | ``` CGImageRef _Nullable CGDisplayCreateImage (     CGDirectDisplayID displayID ); ``` |

Modified [CGDisplayCreateImageForRect()](https://developer.apple.com/documentation/coregraphics/1454595-cgdisplaycreateimage)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGDisplayCreateImageForRect (     CGDirectDisplayID display,     CGRect rect ); ``` |
| To | ``` CGImageRef _Nullable CGDisplayCreateImageForRect (     CGDirectDisplayID display,     CGRect rect ); ``` |

Modified [CGDisplayCurrentMode()](https://developer.apple.com/documentation/coregraphics/1562062-cgdisplaycurrentmode)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGDisplayCurrentMode (     CGDirectDisplayID display ); ``` |
| To | ``` CFDictionaryRef _Nullable CGDisplayCurrentMode (     CGDirectDisplayID display ); ``` |

Modified [CGDisplayGetDrawingContext()](https://developer.apple.com/documentation/coregraphics/1456576-cgdisplaygetdrawingcontext)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGDisplayGetDrawingContext (     CGDirectDisplayID display ); ``` |
| To | ``` CGContextRef _Nullable CGDisplayGetDrawingContext (     CGDirectDisplayID display ); ``` |

Modified [CGDisplayModeCopyPixelEncoding()](https://developer.apple.com/documentation/coregraphics/1455067-cgdisplaymodecopypixelencoding)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` CFStringRef CGDisplayModeCopyPixelEncoding (     CGDisplayModeRef mode ); ``` | -- |
| To | ``` CFStringRef _Nullable CGDisplayModeCopyPixelEncoding (     CGDisplayModeRef _Nullable mode ); ``` | OS X 10.11 |

Modified [CGDisplayModeGetHeight()](https://developer.apple.com/documentation/coregraphics/1455380-cgdisplaymodegetheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGDisplayModeGetHeight (     CGDisplayModeRef mode ); ``` |
| To | ``` size_t CGDisplayModeGetHeight (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetIODisplayModeID()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454728-iodisplaymodeid)

|  | Declaration |
| --- | --- |
| From | ``` int32_t CGDisplayModeGetIODisplayModeID (     CGDisplayModeRef mode ); ``` |
| To | ``` int32_t CGDisplayModeGetIODisplayModeID (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetIOFlags()](https://developer.apple.com/documentation/coregraphics/1454092-cgdisplaymodegetioflags)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t CGDisplayModeGetIOFlags (     CGDisplayModeRef mode ); ``` |
| To | ``` uint32_t CGDisplayModeGetIOFlags (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetPixelHeight()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1456406-pixelheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGDisplayModeGetPixelHeight (     CGDisplayModeRef mode ); ``` |
| To | ``` size_t CGDisplayModeGetPixelHeight (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetPixelWidth()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454756-pixelwidth)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGDisplayModeGetPixelWidth (     CGDisplayModeRef mode ); ``` |
| To | ``` size_t CGDisplayModeGetPixelWidth (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetRefreshRate()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454661-refreshrate)

|  | Declaration |
| --- | --- |
| From | ``` double CGDisplayModeGetRefreshRate (     CGDisplayModeRef mode ); ``` |
| To | ``` double CGDisplayModeGetRefreshRate (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeGetWidth()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454442-width)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGDisplayModeGetWidth (     CGDisplayModeRef mode ); ``` |
| To | ``` size_t CGDisplayModeGetWidth (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeIsUsableForDesktopGUI()](https://developer.apple.com/documentation/coregraphics/cgdisplaymode/1454928-isusablefordesktopgui)

|  | Declaration |
| --- | --- |
| From | ``` bool CGDisplayModeIsUsableForDesktopGUI (     CGDisplayModeRef mode ); ``` |
| To | ``` bool CGDisplayModeIsUsableForDesktopGUI (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeRelease()](https://developer.apple.com/documentation/coregraphics/1562069-cgdisplaymoderelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGDisplayModeRelease (     CGDisplayModeRef mode ); ``` |
| To | ``` void CGDisplayModeRelease (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplayModeRetain()](https://developer.apple.com/documentation/coregraphics/1562059-cgdisplaymoderetain)

|  | Declaration |
| --- | --- |
| From | ``` CGDisplayModeRef CGDisplayModeRetain (     CGDisplayModeRef mode ); ``` |
| To | ``` CGDisplayModeRef _Nullable CGDisplayModeRetain (     CGDisplayModeRef _Nullable mode ); ``` |

Modified [CGDisplaySetDisplayMode()](https://developer.apple.com/documentation/coregraphics/1454760-cgdisplaysetdisplaymode)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplaySetDisplayMode (     CGDirectDisplayID display,     CGDisplayModeRef mode,     CFDictionaryRef options ); ``` |
| To | ``` CGError CGDisplaySetDisplayMode (     CGDirectDisplayID display,     CGDisplayModeRef _Nullable mode,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGDisplaySwitchToMode()](https://developer.apple.com/documentation/coregraphics/1562065-cgdisplayswitchtomode)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplaySwitchToMode (     CGDirectDisplayID display,     CFDictionaryRef mode ); ``` |
| To | ``` CGError CGDisplaySwitchToMode (     CGDirectDisplayID display,     CFDictionaryRef _Nullable mode ); ``` |

Modified [CGGetActiveDisplayList()](https://developer.apple.com/documentation/coregraphics/1454603-cggetactivedisplaylist)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetActiveDisplayList (     uint32_t maxDisplays,     CGDirectDisplayID *activeDisplays,     uint32_t *displayCount ); ``` |
| To | ``` CGError CGGetActiveDisplayList (     uint32_t maxDisplays,     CGDirectDisplayID * _Nullable activeDisplays,     uint32_t * _Nullable displayCount ); ``` |

Modified [CGGetDisplaysWithOpenGLDisplayMask()](https://developer.apple.com/documentation/coregraphics/1454234-cggetdisplayswithopengldisplayma)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetDisplaysWithOpenGLDisplayMask (     CGOpenGLDisplayMask mask,     uint32_t maxDisplays,     CGDirectDisplayID *displays,     uint32_t *matchingDisplayCount ); ``` |
| To | ``` CGError CGGetDisplaysWithOpenGLDisplayMask (     CGOpenGLDisplayMask mask,     uint32_t maxDisplays,     CGDirectDisplayID * _Nullable displays,     uint32_t * _Nullable matchingDisplayCount ); ``` |

Modified [CGGetDisplaysWithPoint()](https://developer.apple.com/documentation/coregraphics/1454385-cggetdisplayswithpoint)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetDisplaysWithPoint (     CGPoint point,     uint32_t maxDisplays,     CGDirectDisplayID *displays,     uint32_t *matchingDisplayCount ); ``` |
| To | ``` CGError CGGetDisplaysWithPoint (     CGPoint point,     uint32_t maxDisplays,     CGDirectDisplayID * _Nullable displays,     uint32_t * _Nullable matchingDisplayCount ); ``` |

Modified [CGGetDisplaysWithRect()](https://developer.apple.com/documentation/coregraphics/1456071-cggetdisplayswithrect)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetDisplaysWithRect (     CGRect rect,     uint32_t maxDisplays,     CGDirectDisplayID *displays,     uint32_t *matchingDisplayCount ); ``` |
| To | ``` CGError CGGetDisplaysWithRect (     CGRect rect,     uint32_t maxDisplays,     CGDirectDisplayID * _Nullable displays,     uint32_t * _Nullable matchingDisplayCount ); ``` |

Modified [CGGetDisplayTransferByFormula()](https://developer.apple.com/documentation/coregraphics/1456330-cggetdisplaytransferbyformula)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetDisplayTransferByFormula (     CGDirectDisplayID display,     CGGammaValue *redMin,     CGGammaValue *redMax,     CGGammaValue *redGamma,     CGGammaValue *greenMin,     CGGammaValue *greenMax,     CGGammaValue *greenGamma,     CGGammaValue *blueMin,     CGGammaValue *blueMax,     CGGammaValue *blueGamma ); ``` |
| To | ``` CGError CGGetDisplayTransferByFormula (     CGDirectDisplayID display,     CGGammaValue * _Nullable redMin,     CGGammaValue * _Nullable redMax,     CGGammaValue * _Nullable redGamma,     CGGammaValue * _Nullable greenMin,     CGGammaValue * _Nullable greenMax,     CGGammaValue * _Nullable greenGamma,     CGGammaValue * _Nullable blueMin,     CGGammaValue * _Nullable blueMax,     CGGammaValue * _Nullable blueGamma ); ``` |

Modified [CGGetDisplayTransferByTable()](https://developer.apple.com/documentation/coregraphics/1454974-cggetdisplaytransferbytable)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetDisplayTransferByTable (     CGDirectDisplayID display,     uint32_t capacity,     CGGammaValue *redTable,     CGGammaValue *greenTable,     CGGammaValue *blueTable,     uint32_t *sampleCount ); ``` |
| To | ``` CGError CGGetDisplayTransferByTable (     CGDirectDisplayID display,     uint32_t capacity,     CGGammaValue * _Nullable redTable,     CGGammaValue * _Nullable greenTable,     CGGammaValue * _Nullable blueTable,     uint32_t * _Nullable sampleCount ); ``` |

Modified [CGGetLastMouseDelta()](https://developer.apple.com/documentation/coregraphics/1456484-cggetlastmousedelta)

|  | Declaration |
| --- | --- |
| From | ``` void CGGetLastMouseDelta (     int32_t *deltaX,     int32_t *deltaY ); ``` |
| To | ``` void CGGetLastMouseDelta (     int32_t * _Nullable deltaX,     int32_t * _Nullable deltaY ); ``` |

Modified [CGGetOnlineDisplayList()](https://developer.apple.com/documentation/coregraphics/1454964-cggetonlinedisplaylist)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetOnlineDisplayList (     uint32_t maxDisplays,     CGDirectDisplayID *onlineDisplays,     uint32_t *displayCount ); ``` |
| To | ``` CGError CGGetOnlineDisplayList (     uint32_t maxDisplays,     CGDirectDisplayID * _Nullable onlineDisplays,     uint32_t * _Nullable displayCount ); ``` |

Modified [CGSetDisplayTransferByByteTable()](https://developer.apple.com/documentation/coregraphics/1455896-cgsetdisplaytransferbybytetable)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGSetDisplayTransferByByteTable (     CGDirectDisplayID display,     uint32_t tableSize,     const uint8_t *redTable,     const uint8_t *greenTable,     const uint8_t *blueTable ); ``` |
| To | ``` CGError CGSetDisplayTransferByByteTable (     CGDirectDisplayID display,     uint32_t tableSize,     const uint8_t * _Nonnull redTable,     const uint8_t * _Nonnull greenTable,     const uint8_t * _Nonnull blueTable ); ``` |

Modified [CGSetDisplayTransferByTable()](https://developer.apple.com/documentation/coregraphics/1456604-cgsetdisplaytransferbytable)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGSetDisplayTransferByTable (     CGDirectDisplayID display,     uint32_t tableSize,     const CGGammaValue *redTable,     const CGGammaValue *greenTable,     const CGGammaValue *blueTable ); ``` |
| To | ``` CGError CGSetDisplayTransferByTable (     CGDirectDisplayID display,     uint32_t tableSize,     const CGGammaValue * _Nullable redTable,     const CGGammaValue * _Nullable greenTable,     const CGGammaValue * _Nullable blueTable ); ``` |

#### CGDirectDisplayMetal.h (Added)

Added [CGDirectDisplayCopyCurrentMetalDevice()](https://developer.apple.com/documentation/coregraphics/1493900-cgdirectdisplaycopycurrentmetald)

#### CGDisplayConfiguration.h

Modified [CGBeginDisplayConfiguration()](https://developer.apple.com/documentation/coregraphics/1455235-cgbegindisplayconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGBeginDisplayConfiguration (     CGDisplayConfigRef *config ); ``` |
| To | ``` CGError CGBeginDisplayConfiguration (     CGDisplayConfigRef  _Nullable * _Nullable config ); ``` |

Modified [CGCancelDisplayConfiguration()](https://developer.apple.com/documentation/coregraphics/1455522-cgcanceldisplayconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGCancelDisplayConfiguration (     CGDisplayConfigRef config ); ``` |
| To | ``` CGError CGCancelDisplayConfiguration (     CGDisplayConfigRef _Nullable config ); ``` |

Modified [CGCompleteDisplayConfiguration()](https://developer.apple.com/documentation/coregraphics/1454488-cgcompletedisplayconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGCompleteDisplayConfiguration (     CGDisplayConfigRef config,     CGConfigureOption option ); ``` |
| To | ``` CGError CGCompleteDisplayConfiguration (     CGDisplayConfigRef _Nullable config,     CGConfigureOption option ); ``` |

Modified [CGConfigureDisplayMirrorOfDisplay()](https://developer.apple.com/documentation/coregraphics/1454531-cgconfiguredisplaymirrorofdispla)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayMirrorOfDisplay (     CGDisplayConfigRef config,     CGDirectDisplayID display,     CGDirectDisplayID master ); ``` |
| To | ``` CGError CGConfigureDisplayMirrorOfDisplay (     CGDisplayConfigRef _Nullable config,     CGDirectDisplayID display,     CGDirectDisplayID master ); ``` |

Modified [CGConfigureDisplayMode()](https://developer.apple.com/documentation/coregraphics/1543535-cgconfiguredisplaymode)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayMode (     CGDisplayConfigRef config,     CGDirectDisplayID display,     CFDictionaryRef mode ); ``` |
| To | ``` CGError CGConfigureDisplayMode (     CGDisplayConfigRef _Nullable config,     CGDirectDisplayID display,     CFDictionaryRef _Nullable mode ); ``` |

Modified [CGConfigureDisplayOrigin()](https://developer.apple.com/documentation/coregraphics/1454090-cgconfiguredisplayorigin)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayOrigin (     CGDisplayConfigRef config,     CGDirectDisplayID display,     int32_t x,     int32_t y ); ``` |
| To | ``` CGError CGConfigureDisplayOrigin (     CGDisplayConfigRef _Nullable config,     CGDirectDisplayID display,     int32_t x,     int32_t y ); ``` |

Modified [CGConfigureDisplayStereoOperation()](https://developer.apple.com/documentation/coregraphics/1456308-cgconfiguredisplaystereooperatio)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayStereoOperation (     CGDisplayConfigRef config,     CGDirectDisplayID display,     boolean_t stereo,     boolean_t forceBlueLine ); ``` |
| To | ``` CGError CGConfigureDisplayStereoOperation (     CGDisplayConfigRef _Nullable config,     CGDirectDisplayID display,     boolean_t stereo,     boolean_t forceBlueLine ); ``` |

Modified [CGConfigureDisplayWithDisplayMode()](https://developer.apple.com/documentation/coregraphics/1454273-cgconfiguredisplaywithdisplaymod)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayWithDisplayMode (     CGDisplayConfigRef config,     CGDirectDisplayID display,     CGDisplayModeRef mode,     CFDictionaryRef options ); ``` |
| To | ``` CGError CGConfigureDisplayWithDisplayMode (     CGDisplayConfigRef _Nullable config,     CGDirectDisplayID display,     CGDisplayModeRef _Nullable mode,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGDisplayCopyColorSpace()](https://developer.apple.com/documentation/coregraphics/1454190-cgdisplaycopycolorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGDisplayCopyColorSpace (     CGDirectDisplayID display ); ``` |
| To | ``` CGColorSpaceRef _Nonnull CGDisplayCopyColorSpace (     CGDirectDisplayID display ); ``` |

Modified [CGDisplayRegisterReconfigurationCallback()](https://developer.apple.com/documentation/coregraphics/1455336-cgdisplayregisterreconfiguration)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplayRegisterReconfigurationCallback (     CGDisplayReconfigurationCallBack callback,     void *userInfo ); ``` |
| To | ``` CGError CGDisplayRegisterReconfigurationCallback (     CGDisplayReconfigurationCallBack _Nullable callback,     void * _Nullable userInfo ); ``` |

Modified [CGDisplayRemoveReconfigurationCallback()](https://developer.apple.com/documentation/coregraphics/1455407-cgdisplayremovereconfigurationca)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplayRemoveReconfigurationCallback (     CGDisplayReconfigurationCallBack callback,     void *userInfo ); ``` |
| To | ``` CGError CGDisplayRemoveReconfigurationCallback (     CGDisplayReconfigurationCallBack _Nullable callback,     void * _Nullable userInfo ); ``` |

#### CGDisplayFade.h

Modified [CGAcquireDisplayFadeReservation()](https://developer.apple.com/documentation/coregraphics/1456391-cgacquiredisplayfadereservation)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGAcquireDisplayFadeReservation (     CGDisplayReservationInterval seconds,     CGDisplayFadeReservationToken *token ); ``` |
| To | ``` CGError CGAcquireDisplayFadeReservation (     CGDisplayReservationInterval seconds,     CGDisplayFadeReservationToken * _Nullable token ); ``` |

Modified [CGConfigureDisplayFadeEffect()](https://developer.apple.com/documentation/coregraphics/1454103-cgconfiguredisplayfadeeffect)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGConfigureDisplayFadeEffect (     CGDisplayConfigRef config,     CGDisplayFadeInterval fadeOutSeconds,     CGDisplayFadeInterval fadeInSeconds,     float fadeRed,     float fadeGreen,     float fadeBlue ); ``` |
| To | ``` CGError CGConfigureDisplayFadeEffect (     CGDisplayConfigRef _Nullable config,     CGDisplayFadeInterval fadeOutSeconds,     CGDisplayFadeInterval fadeInSeconds,     float fadeRed,     float fadeGreen,     float fadeBlue ); ``` |

#### CGDisplayStream.h

Modified [CGDisplayStreamCreate()](https://developer.apple.com/documentation/coregraphics/1455170-cgdisplaystreamcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGDisplayStreamRef CGDisplayStreamCreate (     CGDirectDisplayID display,     size_t outputWidth,     size_t outputHeight,     int32_t pixelFormat,     CFDictionaryRef properties,     CGDisplayStreamFrameAvailableHandler handler ); ``` |
| To | ``` CGDisplayStreamRef _Nullable CGDisplayStreamCreate (     CGDirectDisplayID display,     size_t outputWidth,     size_t outputHeight,     int32_t pixelFormat,     CFDictionaryRef _Nullable properties,     CGDisplayStreamFrameAvailableHandler _Nullable handler ); ``` |

Modified [CGDisplayStreamCreateWithDispatchQueue()](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454968-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDisplayStreamRef CGDisplayStreamCreateWithDispatchQueue (     CGDirectDisplayID display,     size_t outputWidth,     size_t outputHeight,     int32_t pixelFormat,     CFDictionaryRef properties,     dispatch_queue_t queue,     CGDisplayStreamFrameAvailableHandler handler ); ``` |
| To | ``` CGDisplayStreamRef _Nullable CGDisplayStreamCreateWithDispatchQueue (     CGDirectDisplayID display,     size_t outputWidth,     size_t outputHeight,     int32_t pixelFormat,     CFDictionaryRef _Nullable properties,     dispatch_queue_t _Nonnull queue,     CGDisplayStreamFrameAvailableHandler _Nullable handler ); ``` |

Modified [CGDisplayStreamGetRunLoopSource()](https://developer.apple.com/documentation/coregraphics/1455403-cgdisplaystreamgetrunloopsource)

|  | Declaration |
| --- | --- |
| From | ``` CFRunLoopSourceRef CGDisplayStreamGetRunLoopSource (     CGDisplayStreamRef displayStream ); ``` |
| To | ``` CFRunLoopSourceRef _Nullable CGDisplayStreamGetRunLoopSource (     CGDisplayStreamRef _Nullable displayStream ); ``` |

Modified [CGDisplayStreamStart()](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1454870-start)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplayStreamStart (     CGDisplayStreamRef displayStream ); ``` |
| To | ``` CGError CGDisplayStreamStart (     CGDisplayStreamRef _Nullable displayStream ); ``` |

Modified [CGDisplayStreamStop()](https://developer.apple.com/documentation/coregraphics/cgdisplaystream/1455658-stop)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGDisplayStreamStop (     CGDisplayStreamRef displayStream ); ``` |
| To | ``` CGError CGDisplayStreamStop (     CGDisplayStreamRef _Nullable displayStream ); ``` |

Modified [CGDisplayStreamUpdateCreateMergedUpdate()](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdate/1454341-init)

|  | Declaration |
| --- | --- |
| From | ``` CGDisplayStreamUpdateRef CGDisplayStreamUpdateCreateMergedUpdate (     CGDisplayStreamUpdateRef firstUpdate,     CGDisplayStreamUpdateRef secondUpdate ); ``` |
| To | ``` CGDisplayStreamUpdateRef _Nullable CGDisplayStreamUpdateCreateMergedUpdate (     CGDisplayStreamUpdateRef _Nullable firstUpdate,     CGDisplayStreamUpdateRef _Nullable secondUpdate ); ``` |

Modified [CGDisplayStreamUpdateGetDropCount()](https://developer.apple.com/documentation/coregraphics/1456212-cgdisplaystreamupdategetdropcoun)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGDisplayStreamUpdateGetDropCount (     CGDisplayStreamUpdateRef updateRef ); ``` |
| To | ``` size_t CGDisplayStreamUpdateGetDropCount (     CGDisplayStreamUpdateRef _Nullable updateRef ); ``` |

Modified [CGDisplayStreamUpdateGetMovedRectsDelta()](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdate/1455469-getmovedrectsdelta)

|  | Declaration |
| --- | --- |
| From | ``` void CGDisplayStreamUpdateGetMovedRectsDelta (     CGDisplayStreamUpdateRef updateRef,     CGFloat *dx,     CGFloat *dy ); ``` |
| To | ``` void CGDisplayStreamUpdateGetMovedRectsDelta (     CGDisplayStreamUpdateRef _Nullable updateRef,     CGFloat * _Nonnull dx,     CGFloat * _Nonnull dy ); ``` |

Modified [CGDisplayStreamUpdateGetRects()](https://developer.apple.com/documentation/coregraphics/cgdisplaystreamupdate/1455530-getrects)

|  | Declaration |
| --- | --- |
| From | ``` const CGRect * CGDisplayStreamUpdateGetRects (     CGDisplayStreamUpdateRef updateRef,     CGDisplayStreamUpdateRectType rectType,     size_t *rectCount ); ``` |
| To | ``` const CGRect * _Nullable CGDisplayStreamUpdateGetRects (     CGDisplayStreamUpdateRef _Nullable updateRef,     CGDisplayStreamUpdateRectType rectType,     size_t * _Nonnull rectCount ); ``` |

#### CGEvent.h

Added [CGEventPostToPid()](https://developer.apple.com/documentation/coregraphics/1454804-cgeventposttopid)Added [CGEventTapCreateForPid()](https://developer.apple.com/documentation/coregraphics/1456048-cgeventtapcreateforpid)Modified [CGEventCreate()](https://developer.apple.com/documentation/coregraphics/cgevent/1454913-init)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreate (     CGEventSourceRef source ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreate (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventCreateCopy()](https://developer.apple.com/documentation/coregraphics/1454071-cgeventcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreateCopy (     CGEventRef event ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreateCopy (     CGEventRef _Nullable event ); ``` |

Modified [CGEventCreateData()](https://developer.apple.com/documentation/coregraphics/1454381-cgeventcreatedata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGEventCreateData (     CFAllocatorRef allocator,     CGEventRef event ); ``` |
| To | ``` CFDataRef _Nullable CGEventCreateData (     CFAllocatorRef _Nullable allocator,     CGEventRef _Nullable event ); ``` |

Modified [CGEventCreateFromData()](https://developer.apple.com/documentation/coregraphics/cgevent/1454249-init)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreateFromData (     CFAllocatorRef allocator,     CFDataRef data ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreateFromData (     CFAllocatorRef _Nullable allocator,     CFDataRef _Nullable data ); ``` |

Modified [CGEventCreateKeyboardEvent()](https://developer.apple.com/documentation/coregraphics/1456564-cgeventcreatekeyboardevent)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreateKeyboardEvent (     CGEventSourceRef source,     CGKeyCode virtualKey,     bool keyDown ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreateKeyboardEvent (     CGEventSourceRef _Nullable source,     CGKeyCode virtualKey,     bool keyDown ); ``` |

Modified [CGEventCreateMouseEvent()](https://developer.apple.com/documentation/coregraphics/1454356-cgeventcreatemouseevent)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreateMouseEvent (     CGEventSourceRef source,     CGEventType mouseType,     CGPoint mouseCursorPosition,     CGMouseButton mouseButton ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreateMouseEvent (     CGEventSourceRef _Nullable source,     CGEventType mouseType,     CGPoint mouseCursorPosition,     CGMouseButton mouseButton ); ``` |

Modified [CGEventCreateScrollWheelEvent()](https://developer.apple.com/documentation/coregraphics/1541327-cgeventcreatescrollwheelevent)

|  | Declaration |
| --- | --- |
| From | ``` CGEventRef CGEventCreateScrollWheelEvent (     CGEventSourceRef source,     CGScrollEventUnit units,     uint32_t wheelCount,     int32_t wheel1,     ... ); ``` |
| To | ``` CGEventRef _Nullable CGEventCreateScrollWheelEvent (     CGEventSourceRef _Nullable source,     CGScrollEventUnit units,     uint32_t wheelCount,     int32_t wheel1,     ... ); ``` |

Modified [CGEventCreateSourceFromEvent()](https://developer.apple.com/documentation/coregraphics/1455393-cgeventcreatesourcefromevent)

|  | Declaration |
| --- | --- |
| From | ``` CGEventSourceRef CGEventCreateSourceFromEvent (     CGEventRef event ); ``` |
| To | ``` CGEventSourceRef _Nullable CGEventCreateSourceFromEvent (     CGEventRef _Nullable event ); ``` |

Modified [CGEventGetDoubleValueField()](https://developer.apple.com/documentation/coregraphics/1455506-cgeventgetdoublevaluefield)

|  | Declaration |
| --- | --- |
| From | ``` double CGEventGetDoubleValueField (     CGEventRef event,     CGEventField field ); ``` |
| To | ``` double CGEventGetDoubleValueField (     CGEventRef _Nullable event,     CGEventField field ); ``` |

Modified [CGEventGetFlags()](https://developer.apple.com/documentation/coregraphics/cgevent/1455642-flags)

|  | Declaration |
| --- | --- |
| From | ``` CGEventFlags CGEventGetFlags (     CGEventRef event ); ``` |
| To | ``` CGEventFlags CGEventGetFlags (     CGEventRef _Nullable event ); ``` |

Modified [CGEventGetIntegerValueField()](https://developer.apple.com/documentation/coregraphics/cgevent/1455885-getintegervaluefield)

|  | Declaration |
| --- | --- |
| From | ``` int64_t CGEventGetIntegerValueField (     CGEventRef event,     CGEventField field ); ``` |
| To | ``` int64_t CGEventGetIntegerValueField (     CGEventRef _Nullable event,     CGEventField field ); ``` |

Modified [CGEventGetLocation()](https://developer.apple.com/documentation/coregraphics/cgevent/1455788-location)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGEventGetLocation (     CGEventRef event ); ``` |
| To | ``` CGPoint CGEventGetLocation (     CGEventRef _Nullable event ); ``` |

Modified [CGEventGetTimestamp()](https://developer.apple.com/documentation/coregraphics/1455481-cgeventgettimestamp)

|  | Declaration |
| --- | --- |
| From | ``` CGEventTimestamp CGEventGetTimestamp (     CGEventRef event ); ``` |
| To | ``` CGEventTimestamp CGEventGetTimestamp (     CGEventRef _Nullable event ); ``` |

Modified [CGEventGetType()](https://developer.apple.com/documentation/coregraphics/1455634-cgeventgettype)

|  | Declaration |
| --- | --- |
| From | ``` CGEventType CGEventGetType (     CGEventRef event ); ``` |
| To | ``` CGEventType CGEventGetType (     CGEventRef _Nullable event ); ``` |

Modified [CGEventGetUnflippedLocation()](https://developer.apple.com/documentation/coregraphics/cgevent/1455589-unflippedlocation)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGEventGetUnflippedLocation (     CGEventRef event ); ``` |
| To | ``` CGPoint CGEventGetUnflippedLocation (     CGEventRef _Nullable event ); ``` |

Modified [CGEventKeyboardGetUnicodeString()](https://developer.apple.com/documentation/coregraphics/1456120-cgeventkeyboardgetunicodestring)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventKeyboardGetUnicodeString (     CGEventRef event,     UniCharCount maxStringLength,     UniCharCount *actualStringLength,     UniChar unicodeString[] ); ``` |
| To | ``` void CGEventKeyboardGetUnicodeString (     CGEventRef _Nullable event,     UniCharCount maxStringLength,     UniCharCount * _Nullable actualStringLength,     UniChar * _Nullable unicodeString ); ``` |

Modified [CGEventKeyboardSetUnicodeString()](https://developer.apple.com/documentation/coregraphics/cgevent/1456028-keyboardsetunicodestring)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventKeyboardSetUnicodeString (     CGEventRef event,     UniCharCount stringLength,     const UniChar unicodeString[] ); ``` |
| To | ``` void CGEventKeyboardSetUnicodeString (     CGEventRef _Nullable event,     UniCharCount stringLength,     const UniChar * _Nullable unicodeString ); ``` |

Modified [CGEventPost()](https://developer.apple.com/documentation/coregraphics/cgevent/1456527-post)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventPost (     CGEventTapLocation tap,     CGEventRef event ); ``` |
| To | ``` void CGEventPost (     CGEventTapLocation tap,     CGEventRef _Nullable event ); ``` |

Modified [CGEventPostToPSN()](https://developer.apple.com/documentation/coregraphics/1455313-cgeventposttopsn)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventPostToPSN (     void *processSerialNumber,     CGEventRef event ); ``` |
| To | ``` void CGEventPostToPSN (     void * _Nullable processSerialNumber,     CGEventRef _Nullable event ); ``` |

Modified [CGEventSetDoubleValueField()](https://developer.apple.com/documentation/coregraphics/1455526-cgeventsetdoublevaluefield)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetDoubleValueField (     CGEventRef event,     CGEventField field,     double value ); ``` |
| To | ``` void CGEventSetDoubleValueField (     CGEventRef _Nullable event,     CGEventField field,     double value ); ``` |

Modified [CGEventSetFlags()](https://developer.apple.com/documentation/coregraphics/1455044-cgeventsetflags)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetFlags (     CGEventRef event,     CGEventFlags flags ); ``` |
| To | ``` void CGEventSetFlags (     CGEventRef _Nullable event,     CGEventFlags flags ); ``` |

Modified [CGEventSetIntegerValueField()](https://developer.apple.com/documentation/coregraphics/1455556-cgeventsetintegervaluefield)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetIntegerValueField (     CGEventRef event,     CGEventField field,     int64_t value ); ``` |
| To | ``` void CGEventSetIntegerValueField (     CGEventRef _Nullable event,     CGEventField field,     int64_t value ); ``` |

Modified [CGEventSetLocation()](https://developer.apple.com/documentation/coregraphics/1456389-cgeventsetlocation)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetLocation (     CGEventRef event,     CGPoint location ); ``` |
| To | ``` void CGEventSetLocation (     CGEventRef _Nullable event,     CGPoint location ); ``` |

Modified [CGEventSetSource()](https://developer.apple.com/documentation/coregraphics/1455500-cgeventsetsource)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetSource (     CGEventRef event,     CGEventSourceRef source ); ``` |
| To | ``` void CGEventSetSource (     CGEventRef _Nullable event,     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSetTimestamp()](https://developer.apple.com/documentation/coregraphics/1456611-cgeventsettimestamp)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetTimestamp (     CGEventRef event,     CGEventTimestamp timestamp ); ``` |
| To | ``` void CGEventSetTimestamp (     CGEventRef _Nullable event,     CGEventTimestamp timestamp ); ``` |

Modified [CGEventSetType()](https://developer.apple.com/documentation/coregraphics/1454300-cgeventsettype)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSetType (     CGEventRef event,     CGEventType type ); ``` |
| To | ``` void CGEventSetType (     CGEventRef _Nullable event,     CGEventType type ); ``` |

Modified [CGEventTapCreate()](https://developer.apple.com/documentation/coregraphics/cgevent/1454426-tapcreate)

|  | Declaration |
| --- | --- |
| From | ``` CFMachPortRef CGEventTapCreate (     CGEventTapLocation tap,     CGEventTapPlacement place,     CGEventTapOptions options,     CGEventMask eventsOfInterest,     CGEventTapCallBack callback,     void *userInfo ); ``` |
| To | ``` CFMachPortRef _Nullable CGEventTapCreate (     CGEventTapLocation tap,     CGEventTapPlacement place,     CGEventTapOptions options,     CGEventMask eventsOfInterest,     CGEventTapCallBack _Nullable callback,     void * _Nullable userInfo ); ``` |

Modified [CGEventTapCreateForPSN()](https://developer.apple.com/documentation/coregraphics/1454828-cgeventtapcreateforpsn)

|  | Declaration |
| --- | --- |
| From | ``` CFMachPortRef CGEventTapCreateForPSN (     void *processSerialNumber,     CGEventTapPlacement place,     CGEventTapOptions options,     CGEventMask eventsOfInterest,     CGEventTapCallBack callback,     void *userInfo ); ``` |
| To | ``` CFMachPortRef _Nullable CGEventTapCreateForPSN (     void * _Nonnull processSerialNumber,     CGEventTapPlacement place,     CGEventTapOptions options,     CGEventMask eventsOfInterest,     CGEventTapCallBack _Nullable callback,     void * _Nullable userInfo ); ``` |

Modified [CGEventTapEnable()](https://developer.apple.com/documentation/coregraphics/1455445-cgeventtapenable)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventTapEnable (     CFMachPortRef tap,     bool enable ); ``` |
| To | ``` void CGEventTapEnable (     CFMachPortRef _Nonnull tap,     bool enable ); ``` |

Modified [CGEventTapIsEnabled()](https://developer.apple.com/documentation/coregraphics/cgevent/1456102-tapisenabled)

|  | Declaration |
| --- | --- |
| From | ``` bool CGEventTapIsEnabled (     CFMachPortRef tap ); ``` |
| To | ``` bool CGEventTapIsEnabled (     CFMachPortRef _Nonnull tap ); ``` |

Modified [CGEventTapPostEvent()](https://developer.apple.com/documentation/coregraphics/cgevent/1455172-tappostevent)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventTapPostEvent (     CGEventTapProxy proxy,     CGEventRef event ); ``` |
| To | ``` void CGEventTapPostEvent (     CGEventTapProxy _Nullable proxy,     CGEventRef _Nullable event ); ``` |

Modified [CGGetEventTapList()](https://developer.apple.com/documentation/coregraphics/1455395-cggeteventtaplist)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGGetEventTapList (     uint32_t maxNumberOfTaps,     CGEventTapInformation tapList[],     uint32_t *eventTapCount ); ``` |
| To | ``` CGError CGGetEventTapList (     uint32_t maxNumberOfTaps,     CGEventTapInformation * _Nullable tapList,     uint32_t * _Nullable eventTapCount ); ``` |

#### CGEventSource.h

Modified [CGEventSourceCreate()](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408776-init)

|  | Declaration |
| --- | --- |
| From | ``` CGEventSourceRef CGEventSourceCreate (     CGEventSourceStateID stateID ); ``` |
| To | ``` CGEventSourceRef _Nullable CGEventSourceCreate (     CGEventSourceStateID stateID ); ``` |

Modified [CGEventSourceGetKeyboardType()](https://developer.apple.com/documentation/coregraphics/1408787-cgeventsourcegetkeyboardtype)

|  | Declaration |
| --- | --- |
| From | ``` CGEventSourceKeyboardType CGEventSourceGetKeyboardType (     CGEventSourceRef source ); ``` |
| To | ``` CGEventSourceKeyboardType CGEventSourceGetKeyboardType (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSourceGetLocalEventsFilterDuringSuppressionState()](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408785-getlocaleventsfilterduringsuppre)

|  | Declaration |
| --- | --- |
| From | ``` CGEventFilterMask CGEventSourceGetLocalEventsFilterDuringSuppressionState (     CGEventSourceRef source,     CGEventSuppressionState state ); ``` |
| To | ``` CGEventFilterMask CGEventSourceGetLocalEventsFilterDuringSuppressionState (     CGEventSourceRef _Nullable source,     CGEventSuppressionState state ); ``` |

Modified [CGEventSourceGetLocalEventsSuppressionInterval()](https://developer.apple.com/documentation/coregraphics/1408774-cgeventsourcegetlocaleventssuppr)

|  | Declaration |
| --- | --- |
| From | ``` CFTimeInterval CGEventSourceGetLocalEventsSuppressionInterval (     CGEventSourceRef source ); ``` |
| To | ``` CFTimeInterval CGEventSourceGetLocalEventsSuppressionInterval (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSourceGetPixelsPerLine()](https://developer.apple.com/documentation/coregraphics/1408775-cgeventsourcegetpixelsperline)

|  | Declaration |
| --- | --- |
| From | ``` double CGEventSourceGetPixelsPerLine (     CGEventSourceRef source ); ``` |
| To | ``` double CGEventSourceGetPixelsPerLine (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSourceGetSourceStateID()](https://developer.apple.com/documentation/coregraphics/1408772-cgeventsourcegetsourcestateid)

|  | Declaration |
| --- | --- |
| From | ``` CGEventSourceStateID CGEventSourceGetSourceStateID (     CGEventSourceRef source ); ``` |
| To | ``` CGEventSourceStateID CGEventSourceGetSourceStateID (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSourceGetUserData()](https://developer.apple.com/documentation/coregraphics/1408777-cgeventsourcegetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` int64_t CGEventSourceGetUserData (     CGEventSourceRef source ); ``` |
| To | ``` int64_t CGEventSourceGetUserData (     CGEventSourceRef _Nullable source ); ``` |

Modified [CGEventSourceSetKeyboardType()](https://developer.apple.com/documentation/coregraphics/1408795-cgeventsourcesetkeyboardtype)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSourceSetKeyboardType (     CGEventSourceRef source,     CGEventSourceKeyboardType keyboardType ); ``` |
| To | ``` void CGEventSourceSetKeyboardType (     CGEventSourceRef _Nullable source,     CGEventSourceKeyboardType keyboardType ); ``` |

Modified [CGEventSourceSetLocalEventsFilterDuringSuppressionState()](https://developer.apple.com/documentation/coregraphics/cgeventsource/1408770-setlocaleventsfilterduringsuppre)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSourceSetLocalEventsFilterDuringSuppressionState (     CGEventSourceRef source,     CGEventFilterMask filter,     CGEventSuppressionState state ); ``` |
| To | ``` void CGEventSourceSetLocalEventsFilterDuringSuppressionState (     CGEventSourceRef _Nullable source,     CGEventFilterMask filter,     CGEventSuppressionState state ); ``` |

Modified [CGEventSourceSetLocalEventsSuppressionInterval()](https://developer.apple.com/documentation/coregraphics/1408783-cgeventsourcesetlocaleventssuppr)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSourceSetLocalEventsSuppressionInterval (     CGEventSourceRef source,     CFTimeInterval seconds ); ``` |
| To | ``` void CGEventSourceSetLocalEventsSuppressionInterval (     CGEventSourceRef _Nullable source,     CFTimeInterval seconds ); ``` |

Modified [CGEventSourceSetPixelsPerLine()](https://developer.apple.com/documentation/coregraphics/1408766-cgeventsourcesetpixelsperline)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSourceSetPixelsPerLine (     CGEventSourceRef source,     double pixelsPerLine ); ``` |
| To | ``` void CGEventSourceSetPixelsPerLine (     CGEventSourceRef _Nullable source,     double pixelsPerLine ); ``` |

Modified [CGEventSourceSetUserData()](https://developer.apple.com/documentation/coregraphics/1408779-cgeventsourcesetuserdata)

|  | Declaration |
| --- | --- |
| From | ``` void CGEventSourceSetUserData (     CGEventSourceRef source,     int64_t userData ); ``` |
| To | ``` void CGEventSourceSetUserData (     CGEventSourceRef _Nullable source,     int64_t userData ); ``` |

#### CGFont.h

Removed [kCGFontIndexInvalid](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgfontindexinvalid)Removed [kCGFontIndexMax](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgfontindexmax)Removed [kCGGlyphMax](https://developer.apple.com/documentation/coregraphics/cgfont/font_table_index_values/kcgglyphmax)Added CGGlypDeprecatedEnumAdded [kCGFontIndexInvalid](https://developer.apple.com/documentation/coregraphics/kcgfontindexinvalid)Added [kCGFontIndexMax](https://developer.apple.com/documentation/coregraphics/kcgfontindexmax)Added [kCGGlyphMax](https://developer.apple.com/documentation/coregraphics/kcgglyphmax)Modified [CGFontCanCreatePostScriptSubset()](https://developer.apple.com/documentation/coregraphics/cgfont/1396365-cancreatepostscriptsubset)

|  | Declaration |
| --- | --- |
| From | ``` bool CGFontCanCreatePostScriptSubset (     CGFontRef font,     CGFontPostScriptFormat format ); ``` |
| To | ``` bool CGFontCanCreatePostScriptSubset (     CGFontRef _Nullable font,     CGFontPostScriptFormat format ); ``` |

Modified [CGFontCopyFullName()](https://developer.apple.com/documentation/coregraphics/1396357-cgfontcopyfullname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGFontCopyFullName (     CGFontRef font ); ``` |
| To | ``` CFStringRef _Nullable CGFontCopyFullName (     CGFontRef _Nullable font ); ``` |

Modified [CGFontCopyGlyphNameForGlyph()](https://developer.apple.com/documentation/coregraphics/1396349-cgfontcopyglyphnameforglyph)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGFontCopyGlyphNameForGlyph (     CGFontRef font,     CGGlyph glyph ); ``` |
| To | ``` CFStringRef _Nullable CGFontCopyGlyphNameForGlyph (     CGFontRef _Nullable font,     CGGlyph glyph ); ``` |

Modified [CGFontCopyPostScriptName()](https://developer.apple.com/documentation/coregraphics/cgfont/1396346-postscriptname)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGFontCopyPostScriptName (     CGFontRef font ); ``` |
| To | ``` CFStringRef _Nullable CGFontCopyPostScriptName (     CGFontRef _Nullable font ); ``` |

Modified [CGFontCopyTableForTag()](https://developer.apple.com/documentation/coregraphics/cgfont/1396402-table)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGFontCopyTableForTag (     CGFontRef font,     uint32_t tag ); ``` |
| To | ``` CFDataRef _Nullable CGFontCopyTableForTag (     CGFontRef _Nullable font,     uint32_t tag ); ``` |

Modified [CGFontCopyTableTags()](https://developer.apple.com/documentation/coregraphics/cgfont/1396392-tabletags)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGFontCopyTableTags (     CGFontRef font ); ``` |
| To | ``` CFArrayRef _Nullable CGFontCopyTableTags (     CGFontRef _Nullable font ); ``` |

Modified [CGFontCopyVariationAxes()](https://developer.apple.com/documentation/coregraphics/cgfont/1396376-variationaxes)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGFontCopyVariationAxes (     CGFontRef font ); ``` |
| To | ``` CFArrayRef _Nullable CGFontCopyVariationAxes (     CGFontRef _Nullable font ); ``` |

Modified [CGFontCopyVariations()](https://developer.apple.com/documentation/coregraphics/1396355-cgfontcopyvariations)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGFontCopyVariations (     CGFontRef font ); ``` |
| To | ``` CFDictionaryRef _Nullable CGFontCopyVariations (     CGFontRef _Nullable font ); ``` |

Modified [CGFontCreateCopyWithVariations()](https://developer.apple.com/documentation/coregraphics/cgfont/1396373-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CGFontCreateCopyWithVariations (     CGFontRef font,     CFDictionaryRef variations ); ``` |
| To | ``` CGFontRef _Nullable CGFontCreateCopyWithVariations (     CGFontRef _Nullable font,     CFDictionaryRef _Nullable variations ); ``` |

Modified [CGFontCreatePostScriptEncoding()](https://developer.apple.com/documentation/coregraphics/1396348-cgfontcreatepostscriptencoding)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGFontCreatePostScriptEncoding (     CGFontRef font,     const CGGlyph encoding[256] ); ``` |
| To | ``` CFDataRef _Nullable CGFontCreatePostScriptEncoding (     CGFontRef _Nullable font,     const CGGlyph encoding[256] ); ``` |

Modified [CGFontCreatePostScriptSubset()](https://developer.apple.com/documentation/coregraphics/cgfont/1396324-createpostscriptsubset)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGFontCreatePostScriptSubset (     CGFontRef font,     CFStringRef subsetName,     CGFontPostScriptFormat format,     const CGGlyph glyphs[],     size_t count,     const CGGlyph encoding[256] ); ``` |
| To | ``` CFDataRef _Nullable CGFontCreatePostScriptSubset (     CGFontRef _Nullable font,     CFStringRef _Nullable subsetName,     CGFontPostScriptFormat format,     const CGGlyph * _Nullable glyphs,     size_t count,     const CGGlyph encoding[256] ); ``` |

Modified [CGFontCreateWithDataProvider()](https://developer.apple.com/documentation/coregraphics/1396367-cgfontcreatewithdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CGFontCreateWithDataProvider (     CGDataProviderRef provider ); ``` |
| To | ``` CGFontRef _Nullable CGFontCreateWithDataProvider (     CGDataProviderRef _Nullable provider ); ``` |

Modified [CGFontCreateWithFontName()](https://developer.apple.com/documentation/coregraphics/1396330-cgfontcreatewithfontname)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CGFontCreateWithFontName (     CFStringRef name ); ``` |
| To | ``` CGFontRef _Nullable CGFontCreateWithFontName (     CFStringRef _Nullable name ); ``` |

Modified [CGFontCreateWithPlatformFont()](https://developer.apple.com/documentation/coregraphics/1396334-cgfontcreatewithplatformfont)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CGFontCreateWithPlatformFont (     void *platformFontReference ); ``` |
| To | ``` CGFontRef _Nullable CGFontCreateWithPlatformFont (     void * _Nullable platformFontReference ); ``` |

Modified [CGFontGetAscent()](https://developer.apple.com/documentation/coregraphics/1396359-cgfontgetascent)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetAscent (     CGFontRef font ); ``` |
| To | ``` int CGFontGetAscent (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetCapHeight()](https://developer.apple.com/documentation/coregraphics/cgfont/1396338-capheight)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetCapHeight (     CGFontRef font ); ``` |
| To | ``` int CGFontGetCapHeight (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetDescent()](https://developer.apple.com/documentation/coregraphics/1396351-cgfontgetdescent)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetDescent (     CGFontRef font ); ``` |
| To | ``` int CGFontGetDescent (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetFontBBox()](https://developer.apple.com/documentation/coregraphics/cgfont/1396353-fontbbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGFontGetFontBBox (     CGFontRef font ); ``` |
| To | ``` CGRect CGFontGetFontBBox (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetGlyphAdvances()](https://developer.apple.com/documentation/coregraphics/1396332-cgfontgetglyphadvances)

|  | Declaration |
| --- | --- |
| From | ``` bool CGFontGetGlyphAdvances (     CGFontRef font,     const CGGlyph glyphs[],     size_t count,     int advances[] ); ``` |
| To | ``` bool CGFontGetGlyphAdvances (     CGFontRef _Nullable font,     const CGGlyph * _Nonnull glyphs,     size_t count,     int * _Nonnull advances ); ``` |

Modified [CGFontGetGlyphBBoxes()](https://developer.apple.com/documentation/coregraphics/1396342-cgfontgetglyphbboxes)

|  | Declaration |
| --- | --- |
| From | ``` bool CGFontGetGlyphBBoxes (     CGFontRef font,     const CGGlyph glyphs[],     size_t count,     CGRect bboxes[] ); ``` |
| To | ``` bool CGFontGetGlyphBBoxes (     CGFontRef _Nullable font,     const CGGlyph * _Nonnull glyphs,     size_t count,     CGRect * _Nonnull bboxes ); ``` |

Modified [CGFontGetGlyphWithGlyphName()](https://developer.apple.com/documentation/coregraphics/cgfont/1396340-getglyphwithglyphname)

|  | Declaration |
| --- | --- |
| From | ``` CGGlyph CGFontGetGlyphWithGlyphName (     CGFontRef font,     CFStringRef name ); ``` |
| To | ``` CGGlyph CGFontGetGlyphWithGlyphName (     CGFontRef _Nullable font,     CFStringRef _Nullable name ); ``` |

Modified [CGFontGetItalicAngle()](https://developer.apple.com/documentation/coregraphics/cgfont/1396404-italicangle)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CGFontGetItalicAngle (     CGFontRef font ); ``` |
| To | ``` CGFloat CGFontGetItalicAngle (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetLeading()](https://developer.apple.com/documentation/coregraphics/cgfont/1396390-leading)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetLeading (     CGFontRef font ); ``` |
| To | ``` int CGFontGetLeading (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetNumberOfGlyphs()](https://developer.apple.com/documentation/coregraphics/cgfont/1396371-numberofglyphs)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGFontGetNumberOfGlyphs (     CGFontRef font ); ``` |
| To | ``` size_t CGFontGetNumberOfGlyphs (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetStemV()](https://developer.apple.com/documentation/coregraphics/cgfont/1396380-stemv)

|  | Declaration |
| --- | --- |
| From | ``` CGFloat CGFontGetStemV (     CGFontRef font ); ``` |
| To | ``` CGFloat CGFontGetStemV (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetUnitsPerEm()](https://developer.apple.com/documentation/coregraphics/1396344-cgfontgetunitsperem)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetUnitsPerEm (     CGFontRef font ); ``` |
| To | ``` int CGFontGetUnitsPerEm (     CGFontRef _Nullable font ); ``` |

Modified [CGFontGetXHeight()](https://developer.apple.com/documentation/coregraphics/1396410-cgfontgetxheight)

|  | Declaration |
| --- | --- |
| From | ``` int CGFontGetXHeight (     CGFontRef font ); ``` |
| To | ``` int CGFontGetXHeight (     CGFontRef _Nullable font ); ``` |

Modified [CGFontRelease()](https://developer.apple.com/documentation/coregraphics/1396363-cgfontrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGFontRelease (     CGFontRef font ); ``` |
| To | ``` void CGFontRelease (     CGFontRef _Nullable font ); ``` |

Modified [CGFontRetain()](https://developer.apple.com/documentation/coregraphics/1396384-cgfontretain)

|  | Declaration |
| --- | --- |
| From | ``` CGFontRef CGFontRetain (     CGFontRef font ); ``` |
| To | ``` CGFontRef _Nullable CGFontRetain (     CGFontRef _Nullable font ); ``` |

#### CGFunction.h

Modified [CGFunctionCreate()](https://developer.apple.com/documentation/coregraphics/cgfunction/1390862-init)

|  | Declaration |
| --- | --- |
| From | ``` CGFunctionRef CGFunctionCreate (     void *info,     size_t domainDimension,     const CGFloat *domain,     size_t rangeDimension,     const CGFloat *range,     const CGFunctionCallbacks *callbacks ); ``` |
| To | ``` CGFunctionRef _Nullable CGFunctionCreate (     void * _Nullable info,     size_t domainDimension,     const CGFloat * _Nullable domain,     size_t rangeDimension,     const CGFloat * _Nullable range,     const CGFunctionCallbacks * _Nullable callbacks ); ``` |

Modified [CGFunctionRelease()](https://developer.apple.com/documentation/coregraphics/1390864-cgfunctionrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGFunctionRelease (     CGFunctionRef function ); ``` |
| To | ``` void CGFunctionRelease (     CGFunctionRef _Nullable function ); ``` |

Modified [CGFunctionRetain()](https://developer.apple.com/documentation/coregraphics/1390869-cgfunctionretain)

|  | Declaration |
| --- | --- |
| From | ``` CGFunctionRef CGFunctionRetain (     CGFunctionRef function ); ``` |
| To | ``` CGFunctionRef _Nullable CGFunctionRetain (     CGFunctionRef _Nullable function ); ``` |

#### CGGeometry.h

Modified [CGPointCreateDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/cgpoint/1455382-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGPointCreateDictionaryRepresentation (     CGPoint point ); ``` |
| To | ``` CFDictionaryRef _Nonnull CGPointCreateDictionaryRepresentation (     CGPoint point ); ``` |

Modified [CGPointMakeWithDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/1455338-cgpointmakewithdictionaryreprese)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPointMakeWithDictionaryRepresentation (     CFDictionaryRef dict,     CGPoint *point ); ``` |
| To | ``` bool CGPointMakeWithDictionaryRepresentation (     CFDictionaryRef _Nullable dict,     CGPoint * _Nullable point ); ``` |

Modified [CGRectCreateDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/1455760-cgrectcreatedictionaryrepresenta)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGRectCreateDictionaryRepresentation (     CGRect ); ``` |
| To | ``` CFDictionaryRef _Nonnull CGRectCreateDictionaryRepresentation (     CGRect ); ``` |

Modified [CGRectDivide()](https://developer.apple.com/documentation/coregraphics/1455925-cgrectdivide)

|  | Declaration |
| --- | --- |
| From | ``` void CGRectDivide (     CGRect rect,     CGRect *slice,     CGRect *remainder,     CGFloat amount,     CGRectEdge edge ); ``` |
| To | ``` void CGRectDivide (     CGRect rect,     CGRect * _Nonnull slice,     CGRect * _Nonnull remainder,     CGFloat amount,     CGRectEdge edge ); ``` |

Modified [CGRectMakeWithDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/1456558-cgrectmakewithdictionaryrepresen)

|  | Declaration |
| --- | --- |
| From | ``` bool CGRectMakeWithDictionaryRepresentation (     CFDictionaryRef dict,     CGRect *rect ); ``` |
| To | ``` bool CGRectMakeWithDictionaryRepresentation (     CFDictionaryRef _Nullable dict,     CGRect * _Nullable rect ); ``` |

Modified [CGSizeCreateDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/cgsize/1455274-dictionaryrepresentation)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGSizeCreateDictionaryRepresentation (     CGSize size ); ``` |
| To | ``` CFDictionaryRef _Nonnull CGSizeCreateDictionaryRepresentation (     CGSize size ); ``` |

Modified [CGSizeMakeWithDictionaryRepresentation()](https://developer.apple.com/documentation/coregraphics/1454318-cgsizemakewithdictionaryrepresen)

|  | Declaration |
| --- | --- |
| From | ``` bool CGSizeMakeWithDictionaryRepresentation (     CFDictionaryRef dict,     CGSize *size ); ``` |
| To | ``` bool CGSizeMakeWithDictionaryRepresentation (     CFDictionaryRef _Nullable dict,     CGSize * _Nullable size ); ``` |

#### CGGradient.h

Modified [CGGradientCreateWithColorComponents()](https://developer.apple.com/documentation/coregraphics/cggradient/1398454-init)

|  | Declaration |
| --- | --- |
| From | ``` CGGradientRef CGGradientCreateWithColorComponents (     CGColorSpaceRef space,     const CGFloat components[],     const CGFloat locations[],     size_t count ); ``` |
| To | ``` CGGradientRef _Nullable CGGradientCreateWithColorComponents (     CGColorSpaceRef _Nullable space,     const CGFloat * _Nullable components,     const CGFloat * _Nullable locations,     size_t count ); ``` |

Modified [CGGradientCreateWithColors()](https://developer.apple.com/documentation/coregraphics/cggradient/1398458-init)

|  | Declaration |
| --- | --- |
| From | ``` CGGradientRef CGGradientCreateWithColors (     CGColorSpaceRef space,     CFArrayRef colors,     const CGFloat locations[] ); ``` |
| To | ``` CGGradientRef _Nullable CGGradientCreateWithColors (     CGColorSpaceRef _Nullable space,     CFArrayRef _Nullable colors,     const CGFloat * _Nullable locations ); ``` |

Modified [CGGradientRelease()](https://developer.apple.com/documentation/coregraphics/1398460-cggradientrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGGradientRelease (     CGGradientRef gradient ); ``` |
| To | ``` void CGGradientRelease (     CGGradientRef _Nullable gradient ); ``` |

Modified [CGGradientRetain()](https://developer.apple.com/documentation/coregraphics/1398456-cggradientretain)

|  | Declaration |
| --- | --- |
| From | ``` CGGradientRef CGGradientRetain (     CGGradientRef gradient ); ``` |
| To | ``` CGGradientRef _Nullable CGGradientRetain (     CGGradientRef _Nullable gradient ); ``` |

#### CGImage.h

Added [CGImageGetUTType()](https://developer.apple.com/documentation/coregraphics/1456067-cgimagegetuttype)Modified [CGImageCreate()](https://developer.apple.com/documentation/coregraphics/cgimage/1455149-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGColorSpaceRef space,     CGBitmapInfo bitmapInfo,     CGDataProviderRef provider,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGColorSpaceRef _Nullable space,     CGBitmapInfo bitmapInfo,     CGDataProviderRef _Nullable provider,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageCreateCopy()](https://developer.apple.com/documentation/coregraphics/cgimage/1455615-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateCopy (     CGImageRef image ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateCopy (     CGImageRef _Nullable image ); ``` |

Modified [CGImageCreateCopyWithColorSpace()](https://developer.apple.com/documentation/coregraphics/cgimage/1455355-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateCopyWithColorSpace (     CGImageRef image,     CGColorSpaceRef space ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateCopyWithColorSpace (     CGImageRef _Nullable image,     CGColorSpaceRef _Nullable space ); ``` |

Modified [CGImageCreateWithImageInRect()](https://developer.apple.com/documentation/coregraphics/cgimage/1454683-cropping)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithImageInRect (     CGImageRef image,     CGRect rect ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithImageInRect (     CGImageRef _Nullable image,     CGRect rect ); ``` |

Modified [CGImageCreateWithJPEGDataProvider()](https://developer.apple.com/documentation/coregraphics/cgimage/1454920-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithJPEGDataProvider (     CGDataProviderRef source,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithJPEGDataProvider (     CGDataProviderRef _Nullable source,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageCreateWithMask()](https://developer.apple.com/documentation/coregraphics/1456337-cgimagecreatewithmask)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithMask (     CGImageRef image,     CGImageRef mask ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithMask (     CGImageRef _Nullable image,     CGImageRef _Nullable mask ); ``` |

Modified [CGImageCreateWithMaskingColors()](https://developer.apple.com/documentation/coregraphics/cgimage/1454358-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithMaskingColors (     CGImageRef image,     const CGFloat components[] ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithMaskingColors (     CGImageRef _Nullable image,     const CGFloat * _Nullable components ); ``` |

Modified [CGImageCreateWithPNGDataProvider()](https://developer.apple.com/documentation/coregraphics/cgimage/1454993-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageCreateWithPNGDataProvider (     CGDataProviderRef source,     const CGFloat decode[],     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |
| To | ``` CGImageRef _Nullable CGImageCreateWithPNGDataProvider (     CGDataProviderRef _Nullable source,     const CGFloat * _Nullable decode,     bool shouldInterpolate,     CGColorRenderingIntent intent ); ``` |

Modified [CGImageGetAlphaInfo()](https://developer.apple.com/documentation/coregraphics/1455401-cgimagegetalphainfo)

|  | Declaration |
| --- | --- |
| From | ``` CGImageAlphaInfo CGImageGetAlphaInfo (     CGImageRef image ); ``` |
| To | ``` CGImageAlphaInfo CGImageGetAlphaInfo (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetBitmapInfo()](https://developer.apple.com/documentation/coregraphics/cgimage/1454200-bitmapinfo)

|  | Declaration |
| --- | --- |
| From | ``` CGBitmapInfo CGImageGetBitmapInfo (     CGImageRef image ); ``` |
| To | ``` CGBitmapInfo CGImageGetBitmapInfo (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetBitsPerComponent()](https://developer.apple.com/documentation/coregraphics/cgimage/1454980-bitspercomponent)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageGetBitsPerComponent (     CGImageRef image ); ``` |
| To | ``` size_t CGImageGetBitsPerComponent (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetBitsPerPixel()](https://developer.apple.com/documentation/coregraphics/cgimage/1454599-bitsperpixel)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageGetBitsPerPixel (     CGImageRef image ); ``` |
| To | ``` size_t CGImageGetBitsPerPixel (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetBytesPerRow()](https://developer.apple.com/documentation/coregraphics/cgimage/1455425-bytesperrow)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageGetBytesPerRow (     CGImageRef image ); ``` |
| To | ``` size_t CGImageGetBytesPerRow (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetColorSpace()](https://developer.apple.com/documentation/coregraphics/cgimage/1454858-colorspace)

|  | Declaration |
| --- | --- |
| From | ``` CGColorSpaceRef CGImageGetColorSpace (     CGImageRef image ); ``` |
| To | ``` CGColorSpaceRef _Nullable CGImageGetColorSpace (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetDataProvider()](https://developer.apple.com/documentation/coregraphics/cgimage/1455260-dataprovider)

|  | Declaration |
| --- | --- |
| From | ``` CGDataProviderRef CGImageGetDataProvider (     CGImageRef image ); ``` |
| To | ``` CGDataProviderRef _Nullable CGImageGetDataProvider (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetDecode()](https://developer.apple.com/documentation/coregraphics/1454575-cgimagegetdecode)

|  | Declaration |
| --- | --- |
| From | ``` const CGFloat * CGImageGetDecode (     CGImageRef image ); ``` |
| To | ``` const CGFloat * _Nullable CGImageGetDecode (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetHeight()](https://developer.apple.com/documentation/coregraphics/1455829-cgimagegetheight)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageGetHeight (     CGImageRef image ); ``` |
| To | ``` size_t CGImageGetHeight (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetRenderingIntent()](https://developer.apple.com/documentation/coregraphics/1456350-cgimagegetrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` CGColorRenderingIntent CGImageGetRenderingIntent (     CGImageRef image ); ``` |
| To | ``` CGColorRenderingIntent CGImageGetRenderingIntent (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetShouldInterpolate()](https://developer.apple.com/documentation/coregraphics/1455363-cgimagegetshouldinterpolate)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageGetShouldInterpolate (     CGImageRef image ); ``` |
| To | ``` bool CGImageGetShouldInterpolate (     CGImageRef _Nullable image ); ``` |

Modified [CGImageGetWidth()](https://developer.apple.com/documentation/coregraphics/cgimage/1456148-width)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGImageGetWidth (     CGImageRef image ); ``` |
| To | ``` size_t CGImageGetWidth (     CGImageRef _Nullable image ); ``` |

Modified [CGImageIsMask()](https://developer.apple.com/documentation/coregraphics/cgimage/1454229-ismask)

|  | Declaration |
| --- | --- |
| From | ``` bool CGImageIsMask (     CGImageRef image ); ``` |
| To | ``` bool CGImageIsMask (     CGImageRef _Nullable image ); ``` |

Modified [CGImageMaskCreate()](https://developer.apple.com/documentation/coregraphics/1455089-cgimagemaskcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageMaskCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGDataProviderRef provider,     const CGFloat decode[],     bool shouldInterpolate ); ``` |
| To | ``` CGImageRef _Nullable CGImageMaskCreate (     size_t width,     size_t height,     size_t bitsPerComponent,     size_t bitsPerPixel,     size_t bytesPerRow,     CGDataProviderRef _Nullable provider,     const CGFloat * _Nullable decode,     bool shouldInterpolate ); ``` |

Modified [CGImageRelease()](https://developer.apple.com/documentation/coregraphics/1556742-cgimagerelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGImageRelease (     CGImageRef image ); ``` |
| To | ``` void CGImageRelease (     CGImageRef _Nullable image ); ``` |

Modified [CGImageRetain()](https://developer.apple.com/documentation/coregraphics/1556741-cgimageretain)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGImageRetain (     CGImageRef image ); ``` |
| To | ``` CGImageRef _Nullable CGImageRetain (     CGImageRef _Nullable image ); ``` |

#### CGLayer.h

Modified [CGContextDrawLayerAtPoint()](https://developer.apple.com/documentation/coregraphics/1450894-cgcontextdrawlayeratpoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawLayerAtPoint (     CGContextRef context,     CGPoint point,     CGLayerRef layer ); ``` |
| To | ``` void CGContextDrawLayerAtPoint (     CGContextRef _Nullable context,     CGPoint point,     CGLayerRef _Nullable layer ); ``` |

Modified [CGContextDrawLayerInRect()](https://developer.apple.com/documentation/coregraphics/1450896-cgcontextdrawlayerinrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGContextDrawLayerInRect (     CGContextRef context,     CGRect rect,     CGLayerRef layer ); ``` |
| To | ``` void CGContextDrawLayerInRect (     CGContextRef _Nullable context,     CGRect rect,     CGLayerRef _Nullable layer ); ``` |

Modified [CGLayerCreateWithContext()](https://developer.apple.com/documentation/coregraphics/1450892-cglayercreatewithcontext)

|  | Declaration |
| --- | --- |
| From | ``` CGLayerRef CGLayerCreateWithContext (     CGContextRef context,     CGSize size,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` CGLayerRef _Nullable CGLayerCreateWithContext (     CGContextRef _Nullable context,     CGSize size,     CFDictionaryRef _Nullable auxiliaryInfo ); ``` |

Modified [CGLayerGetContext()](https://developer.apple.com/documentation/coregraphics/1450902-cglayergetcontext)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGLayerGetContext (     CGLayerRef layer ); ``` |
| To | ``` CGContextRef _Nullable CGLayerGetContext (     CGLayerRef _Nullable layer ); ``` |

Modified [CGLayerGetSize()](https://developer.apple.com/documentation/coregraphics/cglayer/1450890-size)

|  | Declaration |
| --- | --- |
| From | ``` CGSize CGLayerGetSize (     CGLayerRef layer ); ``` |
| To | ``` CGSize CGLayerGetSize (     CGLayerRef _Nullable layer ); ``` |

Modified [CGLayerRelease()](https://developer.apple.com/documentation/coregraphics/1450898-cglayerrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGLayerRelease (     CGLayerRef layer ); ``` |
| To | ``` void CGLayerRelease (     CGLayerRef _Nullable layer ); ``` |

Modified [CGLayerRetain()](https://developer.apple.com/documentation/coregraphics/1450900-cglayerretain)

|  | Declaration |
| --- | --- |
| From | ``` CGLayerRef CGLayerRetain (     CGLayerRef layer ); ``` |
| To | ``` CGLayerRef _Nullable CGLayerRetain (     CGLayerRef _Nullable layer ); ``` |

#### CGPath.h

Modified [CGPathAddArc()](https://developer.apple.com/documentation/coregraphics/1411147-cgpathaddarc)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddArc (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat endAngle,     bool clockwise ); ``` |
| To | ``` void CGPathAddArc (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat endAngle,     bool clockwise ); ``` |

Modified [CGPathAddArcToPoint()](https://developer.apple.com/documentation/coregraphics/1411173-cgpathaddarctopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddArcToPoint (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat x1,     CGFloat y1,     CGFloat x2,     CGFloat y2,     CGFloat radius ); ``` |
| To | ``` void CGPathAddArcToPoint (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat x1,     CGFloat y1,     CGFloat x2,     CGFloat y2,     CGFloat radius ); ``` |

Modified [CGPathAddCurveToPoint()](https://developer.apple.com/documentation/coregraphics/1411212-cgpathaddcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddCurveToPoint (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat cp1x,     CGFloat cp1y,     CGFloat cp2x,     CGFloat cp2y,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGPathAddCurveToPoint (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat cp1x,     CGFloat cp1y,     CGFloat cp2x,     CGFloat cp2y,     CGFloat x,     CGFloat y ); ``` |

Modified [CGPathAddEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1411222-cgpathaddellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddEllipseInRect (     CGMutablePathRef path,     const CGAffineTransform *m,     CGRect rect ); ``` |
| To | ``` void CGPathAddEllipseInRect (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGRect rect ); ``` |

Modified [CGPathAddLines()](https://developer.apple.com/documentation/coregraphics/1411171-cgpathaddlines)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddLines (     CGMutablePathRef path,     const CGAffineTransform *m,     const CGPoint points[],     size_t count ); ``` |
| To | ``` void CGPathAddLines (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     const CGPoint * _Nullable points,     size_t count ); ``` |

Modified [CGPathAddLineToPoint()](https://developer.apple.com/documentation/coregraphics/1411138-cgpathaddlinetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddLineToPoint (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGPathAddLineToPoint (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat x,     CGFloat y ); ``` |

Modified [CGPathAddPath()](https://developer.apple.com/documentation/coregraphics/1411201-cgpathaddpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddPath (     CGMutablePathRef path1,     const CGAffineTransform *m,     CGPathRef path2 ); ``` |
| To | ``` void CGPathAddPath (     CGMutablePathRef _Nullable path1,     const CGAffineTransform * _Nullable m,     CGPathRef _Nullable path2 ); ``` |

Modified [CGPathAddQuadCurveToPoint()](https://developer.apple.com/documentation/coregraphics/1411157-cgpathaddquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddQuadCurveToPoint (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat cpx,     CGFloat cpy,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGPathAddQuadCurveToPoint (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat cpx,     CGFloat cpy,     CGFloat x,     CGFloat y ); ``` |

Modified [CGPathAddRect()](https://developer.apple.com/documentation/coregraphics/1411144-cgpathaddrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddRect (     CGMutablePathRef path,     const CGAffineTransform *m,     CGRect rect ); ``` |
| To | ``` void CGPathAddRect (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGRect rect ); ``` |

Modified [CGPathAddRects()](https://developer.apple.com/documentation/coregraphics/1411153-cgpathaddrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddRects (     CGMutablePathRef path,     const CGAffineTransform *m,     const CGRect rects[],     size_t count ); ``` |
| To | ``` void CGPathAddRects (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     const CGRect * _Nullable rects,     size_t count ); ``` |

Modified [CGPathAddRelativeArc()](https://developer.apple.com/documentation/coregraphics/1411136-cgpathaddrelativearc)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddRelativeArc (     CGMutablePathRef path,     const CGAffineTransform *matrix,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat delta ); ``` |
| To | ``` void CGPathAddRelativeArc (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable matrix,     CGFloat x,     CGFloat y,     CGFloat radius,     CGFloat startAngle,     CGFloat delta ); ``` |

Modified [CGPathAddRoundedRect()](https://developer.apple.com/documentation/coregraphics/1411124-cgpathaddroundedrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathAddRoundedRect (     CGMutablePathRef path,     const CGAffineTransform *transform,     CGRect rect,     CGFloat cornerWidth,     CGFloat cornerHeight ); ``` |
| To | ``` void CGPathAddRoundedRect (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable transform,     CGRect rect,     CGFloat cornerWidth,     CGFloat cornerHeight ); ``` |

Modified [CGPathApply()](https://developer.apple.com/documentation/coregraphics/cgpath/1411203-apply)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathApply (     CGPathRef path,     void *info,     CGPathApplierFunction function ); ``` |
| To | ``` void CGPathApply (     CGPathRef _Nullable path,     void * _Nullable info,     CGPathApplierFunction _Nullable function ); ``` |

Modified [CGPathCloseSubpath()](https://developer.apple.com/documentation/coregraphics/1411188-cgpathclosesubpath)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathCloseSubpath (     CGMutablePathRef path ); ``` |
| To | ``` void CGPathCloseSubpath (     CGMutablePathRef _Nullable path ); ``` |

Modified [CGPathContainsPoint()](https://developer.apple.com/documentation/coregraphics/1411175-cgpathcontainspoint)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPathContainsPoint (     CGPathRef path,     const CGAffineTransform *m,     CGPoint point,     bool eoFill ); ``` |
| To | ``` bool CGPathContainsPoint (     CGPathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGPoint point,     bool eoFill ); ``` |

Modified [CGPathCreateCopy()](https://developer.apple.com/documentation/coregraphics/1411211-cgpathcreatecopy)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateCopy (     CGPathRef path ); ``` |
| To | ``` CGPathRef _Nullable CGPathCreateCopy (     CGPathRef _Nullable path ); ``` |

Modified [CGPathCreateCopyByDashingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411134-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateCopyByDashingPath (     CGPathRef path,     const CGAffineTransform *transform,     CGFloat phase,     const CGFloat *lengths,     size_t count ); ``` |
| To | ``` CGPathRef _Nullable CGPathCreateCopyByDashingPath (     CGPathRef _Nullable path,     const CGAffineTransform * _Nullable transform,     CGFloat phase,     const CGFloat * _Nullable lengths,     size_t count ); ``` |

Modified [CGPathCreateCopyByStrokingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411128-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateCopyByStrokingPath (     CGPathRef path,     const CGAffineTransform *transform,     CGFloat lineWidth,     CGLineCap lineCap,     CGLineJoin lineJoin,     CGFloat miterLimit ); ``` |
| To | ``` CGPathRef _Nullable CGPathCreateCopyByStrokingPath (     CGPathRef _Nullable path,     const CGAffineTransform * _Nullable transform,     CGFloat lineWidth,     CGLineCap lineCap,     CGLineJoin lineJoin,     CGFloat miterLimit ); ``` |

Modified [CGPathCreateCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/cgpath/1411161-copy)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateCopyByTransformingPath (     CGPathRef path,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nullable CGPathCreateCopyByTransformingPath (     CGPathRef _Nullable path,     const CGAffineTransform * _Nullable transform ); ``` |

Modified [CGPathCreateMutable()](https://developer.apple.com/documentation/coregraphics/1411209-cgpathcreatemutable)

|  | Declaration |
| --- | --- |
| From | ``` CGMutablePathRef CGPathCreateMutable (     void ); ``` |
| To | ``` CGMutablePathRef _Nonnull CGPathCreateMutable (     void ); ``` |

Modified [CGPathCreateMutableCopy()](https://developer.apple.com/documentation/coregraphics/cgpath/1411196-mutablecopy)

|  | Declaration |
| --- | --- |
| From | ``` CGMutablePathRef CGPathCreateMutableCopy (     CGPathRef path ); ``` |
| To | ``` CGMutablePathRef _Nullable CGPathCreateMutableCopy (     CGPathRef _Nullable path ); ``` |

Modified [CGPathCreateMutableCopyByTransformingPath()](https://developer.apple.com/documentation/coregraphics/1411150-cgpathcreatemutablecopybytransfo)

|  | Declaration |
| --- | --- |
| From | ``` CGMutablePathRef CGPathCreateMutableCopyByTransformingPath (     CGPathRef path,     const CGAffineTransform *transform ); ``` |
| To | ``` CGMutablePathRef _Nullable CGPathCreateMutableCopyByTransformingPath (     CGPathRef _Nullable path,     const CGAffineTransform * _Nullable transform ); ``` |

Modified [CGPathCreateWithEllipseInRect()](https://developer.apple.com/documentation/coregraphics/1411177-cgpathcreatewithellipseinrect)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateWithEllipseInRect (     CGRect rect,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nonnull CGPathCreateWithEllipseInRect (     CGRect rect,     const CGAffineTransform * _Nullable transform ); ``` |

Modified [CGPathCreateWithRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411155-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateWithRect (     CGRect rect,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nonnull CGPathCreateWithRect (     CGRect rect,     const CGAffineTransform * _Nullable transform ); ``` |

Modified [CGPathCreateWithRoundedRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411218-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathCreateWithRoundedRect (     CGRect rect,     CGFloat cornerWidth,     CGFloat cornerHeight,     const CGAffineTransform *transform ); ``` |
| To | ``` CGPathRef _Nonnull CGPathCreateWithRoundedRect (     CGRect rect,     CGFloat cornerWidth,     CGFloat cornerHeight,     const CGAffineTransform * _Nullable transform ); ``` |

Modified [CGPathEqualToPath()](https://developer.apple.com/documentation/coregraphics/1411167-cgpathequaltopath)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPathEqualToPath (     CGPathRef path1,     CGPathRef path2 ); ``` |
| To | ``` bool CGPathEqualToPath (     CGPathRef _Nullable path1,     CGPathRef _Nullable path2 ); ``` |

Modified [CGPathGetBoundingBox()](https://developer.apple.com/documentation/coregraphics/cgpath/1411165-boundingbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPathGetBoundingBox (     CGPathRef path ); ``` |
| To | ``` CGRect CGPathGetBoundingBox (     CGPathRef _Nullable path ); ``` |

Modified [CGPathGetCurrentPoint()](https://developer.apple.com/documentation/coregraphics/1411132-cgpathgetcurrentpoint)

|  | Declaration |
| --- | --- |
| From | ``` CGPoint CGPathGetCurrentPoint (     CGPathRef path ); ``` |
| To | ``` CGPoint CGPathGetCurrentPoint (     CGPathRef _Nullable path ); ``` |

Modified [CGPathGetPathBoundingBox()](https://developer.apple.com/documentation/coregraphics/cgpath/1411200-boundingboxofpath)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPathGetPathBoundingBox (     CGPathRef path ); ``` |
| To | ``` CGRect CGPathGetPathBoundingBox (     CGPathRef _Nullable path ); ``` |

Modified [CGPathIsEmpty()](https://developer.apple.com/documentation/coregraphics/1411149-cgpathisempty)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPathIsEmpty (     CGPathRef path ); ``` |
| To | ``` bool CGPathIsEmpty (     CGPathRef _Nullable path ); ``` |

Modified [CGPathIsRect()](https://developer.apple.com/documentation/coregraphics/cgpath/1411163-isrect)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPathIsRect (     CGPathRef path,     CGRect *rect ); ``` |
| To | ``` bool CGPathIsRect (     CGPathRef _Nullable path,     CGRect * _Nullable rect ); ``` |

Modified [CGPathMoveToPoint()](https://developer.apple.com/documentation/coregraphics/1411146-cgpathmovetopoint)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathMoveToPoint (     CGMutablePathRef path,     const CGAffineTransform *m,     CGFloat x,     CGFloat y ); ``` |
| To | ``` void CGPathMoveToPoint (     CGMutablePathRef _Nullable path,     const CGAffineTransform * _Nullable m,     CGFloat x,     CGFloat y ); ``` |

Modified [CGPathRelease()](https://developer.apple.com/documentation/coregraphics/1411148-cgpathrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPathRelease (     CGPathRef path ); ``` |
| To | ``` void CGPathRelease (     CGPathRef _Nullable path ); ``` |

Modified [CGPathRetain()](https://developer.apple.com/documentation/coregraphics/1411181-cgpathretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPathRef CGPathRetain (     CGPathRef path ); ``` |
| To | ``` CGPathRef _Nullable CGPathRetain (     CGPathRef _Nullable path ); ``` |

#### CGPattern.h

Modified [CGPatternCreate()](https://developer.apple.com/documentation/coregraphics/cgpattern/1454997-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPatternRef CGPatternCreate (     void *info,     CGRect bounds,     CGAffineTransform matrix,     CGFloat xStep,     CGFloat yStep,     CGPatternTiling tiling,     bool isColored,     const CGPatternCallbacks *callbacks ); ``` |
| To | ``` CGPatternRef _Nullable CGPatternCreate (     void * _Nullable info,     CGRect bounds,     CGAffineTransform matrix,     CGFloat xStep,     CGFloat yStep,     CGPatternTiling tiling,     bool isColored,     const CGPatternCallbacks * _Nullable callbacks ); ``` |

Modified [CGPatternRelease()](https://developer.apple.com/documentation/coregraphics/1552266-cgpatternrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPatternRelease (     CGPatternRef pattern ); ``` |
| To | ``` void CGPatternRelease (     CGPatternRef _Nullable pattern ); ``` |

Modified [CGPatternRetain()](https://developer.apple.com/documentation/coregraphics/1552265-cgpatternretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPatternRef CGPatternRetain (     CGPatternRef pattern ); ``` |
| To | ``` CGPatternRef _Nullable CGPatternRetain (     CGPatternRef _Nullable pattern ); ``` |

#### CGPDFArray.h

Modified [CGPDFArrayGetArray()](https://developer.apple.com/documentation/coregraphics/1454834-cgpdfarraygetarray)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetArray (     CGPDFArrayRef array,     size_t index,     CGPDFArrayRef *value ); ``` |
| To | ``` bool CGPDFArrayGetArray (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFArrayRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFArrayGetBoolean()](https://developer.apple.com/documentation/coregraphics/1454504-cgpdfarraygetboolean)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetBoolean (     CGPDFArrayRef array,     size_t index,     CGPDFBoolean *value ); ``` |
| To | ``` bool CGPDFArrayGetBoolean (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFBoolean * _Nullable value ); ``` |

Modified [CGPDFArrayGetCount()](https://developer.apple.com/documentation/coregraphics/1455207-cgpdfarraygetcount)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGPDFArrayGetCount (     CGPDFArrayRef array ); ``` |
| To | ``` size_t CGPDFArrayGetCount (     CGPDFArrayRef _Nullable array ); ``` |

Modified [CGPDFArrayGetDictionary()](https://developer.apple.com/documentation/coregraphics/1454139-cgpdfarraygetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetDictionary (     CGPDFArrayRef array,     size_t index,     CGPDFDictionaryRef *value ); ``` |
| To | ``` bool CGPDFArrayGetDictionary (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFDictionaryRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFArrayGetInteger()](https://developer.apple.com/documentation/coregraphics/1456053-cgpdfarraygetinteger)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetInteger (     CGPDFArrayRef array,     size_t index,     CGPDFInteger *value ); ``` |
| To | ``` bool CGPDFArrayGetInteger (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFInteger * _Nullable value ); ``` |

Modified [CGPDFArrayGetName()](https://developer.apple.com/documentation/coregraphics/1455034-cgpdfarraygetname)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetName (     CGPDFArrayRef array,     size_t index,     const char **value ); ``` |
| To | ``` bool CGPDFArrayGetName (     CGPDFArrayRef _Nullable array,     size_t index,     const char * _Nullable * _Nullable value ); ``` |

Modified [CGPDFArrayGetNull()](https://developer.apple.com/documentation/coregraphics/1456173-cgpdfarraygetnull)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetNull (     CGPDFArrayRef array,     size_t index ); ``` |
| To | ``` bool CGPDFArrayGetNull (     CGPDFArrayRef _Nullable array,     size_t index ); ``` |

Modified [CGPDFArrayGetNumber()](https://developer.apple.com/documentation/coregraphics/1455374-cgpdfarraygetnumber)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetNumber (     CGPDFArrayRef array,     size_t index,     CGPDFReal *value ); ``` |
| To | ``` bool CGPDFArrayGetNumber (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFReal * _Nullable value ); ``` |

Modified [CGPDFArrayGetObject()](https://developer.apple.com/documentation/coregraphics/1456631-cgpdfarraygetobject)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetObject (     CGPDFArrayRef array,     size_t index,     CGPDFObjectRef *value ); ``` |
| To | ``` bool CGPDFArrayGetObject (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFObjectRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFArrayGetStream()](https://developer.apple.com/documentation/coregraphics/1454424-cgpdfarraygetstream)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetStream (     CGPDFArrayRef array,     size_t index,     CGPDFStreamRef *value ); ``` |
| To | ``` bool CGPDFArrayGetStream (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFStreamRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFArrayGetString()](https://developer.apple.com/documentation/coregraphics/1456104-cgpdfarraygetstring)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFArrayGetString (     CGPDFArrayRef array,     size_t index,     CGPDFStringRef *value ); ``` |
| To | ``` bool CGPDFArrayGetString (     CGPDFArrayRef _Nullable array,     size_t index,     CGPDFStringRef  _Nullable * _Nullable value ); ``` |

#### CGPDFContext.h

Modified [CGPDFContextAddDestinationAtPoint()](https://developer.apple.com/documentation/coregraphics/1455424-cgpdfcontextadddestinationatpoin)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextAddDestinationAtPoint (     CGContextRef context,     CFStringRef name,     CGPoint point ); ``` |
| To | ``` void CGPDFContextAddDestinationAtPoint (     CGContextRef _Nullable context,     CFStringRef _Nonnull name,     CGPoint point ); ``` |

Modified [CGPDFContextAddDocumentMetadata()](https://developer.apple.com/documentation/coregraphics/1456026-cgpdfcontextadddocumentmetadata)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextAddDocumentMetadata (     CGContextRef context,     CFDataRef metadata ); ``` |
| To | ``` void CGPDFContextAddDocumentMetadata (     CGContextRef _Nullable context,     CFDataRef _Nullable metadata ); ``` |

Modified [CGPDFContextBeginPage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456578-beginpdfpage)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextBeginPage (     CGContextRef context,     CFDictionaryRef pageInfo ); ``` |
| To | ``` void CGPDFContextBeginPage (     CGContextRef _Nullable context,     CFDictionaryRef _Nullable pageInfo ); ``` |

Modified [CGPDFContextClose()](https://developer.apple.com/documentation/coregraphics/1454306-cgpdfcontextclose)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextClose (     CGContextRef context ); ``` |
| To | ``` void CGPDFContextClose (     CGContextRef _Nullable context ); ``` |

Modified [CGPDFContextCreate()](https://developer.apple.com/documentation/coregraphics/1454204-cgpdfcontextcreate)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGPDFContextCreate (     CGDataConsumerRef consumer,     const CGRect *mediaBox,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` CGContextRef _Nullable CGPDFContextCreate (     CGDataConsumerRef _Nullable consumer,     const CGRect * _Nullable mediaBox,     CFDictionaryRef _Nullable auxiliaryInfo ); ``` |

Modified [CGPDFContextCreateWithURL()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456290-init)

|  | Declaration |
| --- | --- |
| From | ``` CGContextRef CGPDFContextCreateWithURL (     CFURLRef url,     const CGRect *mediaBox,     CFDictionaryRef auxiliaryInfo ); ``` |
| To | ``` CGContextRef _Nullable CGPDFContextCreateWithURL (     CFURLRef _Nullable url,     const CGRect * _Nullable mediaBox,     CFDictionaryRef _Nullable auxiliaryInfo ); ``` |

Modified [CGPDFContextEndPage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456122-endpdfpage)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextEndPage (     CGContextRef context ); ``` |
| To | ``` void CGPDFContextEndPage (     CGContextRef _Nullable context ); ``` |

Modified [CGPDFContextSetDestinationForRect()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456459-setdestination)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextSetDestinationForRect (     CGContextRef context,     CFStringRef name,     CGRect rect ); ``` |
| To | ``` void CGPDFContextSetDestinationForRect (     CGContextRef _Nullable context,     CFStringRef _Nonnull name,     CGRect rect ); ``` |

Modified [CGPDFContextSetURLForRect()](https://developer.apple.com/documentation/coregraphics/1455622-cgpdfcontextseturlforrect)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFContextSetURLForRect (     CGContextRef context,     CFURLRef url,     CGRect rect ); ``` |
| To | ``` void CGPDFContextSetURLForRect (     CGContextRef _Nullable context,     CFURLRef _Nonnull url,     CGRect rect ); ``` |

#### CGPDFDictionary.h

Modified [CGPDFDictionaryApplyFunction()](https://developer.apple.com/documentation/coregraphics/1430216-cgpdfdictionaryapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFDictionaryApplyFunction (     CGPDFDictionaryRef dict,     CGPDFDictionaryApplierFunction function,     void *info ); ``` |
| To | ``` void CGPDFDictionaryApplyFunction (     CGPDFDictionaryRef _Nullable dict,     CGPDFDictionaryApplierFunction _Nullable function,     void * _Nullable info ); ``` |

Modified [CGPDFDictionaryGetArray()](https://developer.apple.com/documentation/coregraphics/1430229-cgpdfdictionarygetarray)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetArray (     CGPDFDictionaryRef dict,     const char *key,     CGPDFArrayRef *value ); ``` |
| To | ``` bool CGPDFDictionaryGetArray (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFArrayRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetBoolean()](https://developer.apple.com/documentation/coregraphics/1430226-cgpdfdictionarygetboolean)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetBoolean (     CGPDFDictionaryRef dict,     const char *key,     CGPDFBoolean *value ); ``` |
| To | ``` bool CGPDFDictionaryGetBoolean (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFBoolean * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetCount()](https://developer.apple.com/documentation/coregraphics/1430218-cgpdfdictionarygetcount)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGPDFDictionaryGetCount (     CGPDFDictionaryRef dict ); ``` |
| To | ``` size_t CGPDFDictionaryGetCount (     CGPDFDictionaryRef _Nullable dict ); ``` |

Modified [CGPDFDictionaryGetDictionary()](https://developer.apple.com/documentation/coregraphics/1430220-cgpdfdictionarygetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetDictionary (     CGPDFDictionaryRef dict,     const char *key,     CGPDFDictionaryRef *value ); ``` |
| To | ``` bool CGPDFDictionaryGetDictionary (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFDictionaryRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetInteger()](https://developer.apple.com/documentation/coregraphics/1430231-cgpdfdictionarygetinteger)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetInteger (     CGPDFDictionaryRef dict,     const char *key,     CGPDFInteger *value ); ``` |
| To | ``` bool CGPDFDictionaryGetInteger (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFInteger * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetName()](https://developer.apple.com/documentation/coregraphics/1430230-cgpdfdictionarygetname)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetName (     CGPDFDictionaryRef dict,     const char *key,     const char **value ); ``` |
| To | ``` bool CGPDFDictionaryGetName (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     const char * _Nullable * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetNumber()](https://developer.apple.com/documentation/coregraphics/1430228-cgpdfdictionarygetnumber)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetNumber (     CGPDFDictionaryRef dict,     const char *key,     CGPDFReal *value ); ``` |
| To | ``` bool CGPDFDictionaryGetNumber (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFReal * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetObject()](https://developer.apple.com/documentation/coregraphics/1430214-cgpdfdictionarygetobject)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetObject (     CGPDFDictionaryRef dict,     const char *key,     CGPDFObjectRef *value ); ``` |
| To | ``` bool CGPDFDictionaryGetObject (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFObjectRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetStream()](https://developer.apple.com/documentation/coregraphics/1430213-cgpdfdictionarygetstream)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetStream (     CGPDFDictionaryRef dict,     const char *key,     CGPDFStreamRef *value ); ``` |
| To | ``` bool CGPDFDictionaryGetStream (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFStreamRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFDictionaryGetString()](https://developer.apple.com/documentation/coregraphics/1430224-cgpdfdictionarygetstring)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDictionaryGetString (     CGPDFDictionaryRef dict,     const char *key,     CGPDFStringRef *value ); ``` |
| To | ``` bool CGPDFDictionaryGetString (     CGPDFDictionaryRef _Nullable dict,     const char * _Nonnull key,     CGPDFStringRef  _Nullable * _Nullable value ); ``` |

#### CGPDFDocument.h

Modified [CGPDFDocumentAllowsCopying()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402588-allowscopying)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDocumentAllowsCopying (     CGPDFDocumentRef document ); ``` |
| To | ``` bool CGPDFDocumentAllowsCopying (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentAllowsPrinting()](https://developer.apple.com/documentation/coregraphics/1402594-cgpdfdocumentallowsprinting)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDocumentAllowsPrinting (     CGPDFDocumentRef document ); ``` |
| To | ``` bool CGPDFDocumentAllowsPrinting (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentCreateWithProvider()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402603-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDocumentRef CGPDFDocumentCreateWithProvider (     CGDataProviderRef provider ); ``` |
| To | ``` CGPDFDocumentRef _Nullable CGPDFDocumentCreateWithProvider (     CGDataProviderRef _Nullable provider ); ``` |

Modified [CGPDFDocumentCreateWithURL()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402585-init)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDocumentRef CGPDFDocumentCreateWithURL (     CFURLRef url ); ``` |
| To | ``` CGPDFDocumentRef _Nullable CGPDFDocumentCreateWithURL (     CFURLRef _Nullable url ); ``` |

Modified [CGPDFDocumentGetArtBox()](https://developer.apple.com/documentation/coregraphics/1402601-cgpdfdocumentgetartbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFDocumentGetArtBox (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` CGRect CGPDFDocumentGetArtBox (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetBleedBox()](https://developer.apple.com/documentation/coregraphics/1402596-cgpdfdocumentgetbleedbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFDocumentGetBleedBox (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` CGRect CGPDFDocumentGetBleedBox (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetCatalog()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402606-catalog)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDictionaryRef CGPDFDocumentGetCatalog (     CGPDFDocumentRef document ); ``` |
| To | ``` CGPDFDictionaryRef _Nullable CGPDFDocumentGetCatalog (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentGetCropBox()](https://developer.apple.com/documentation/coregraphics/1402598-cgpdfdocumentgetcropbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFDocumentGetCropBox (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` CGRect CGPDFDocumentGetCropBox (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetID()](https://developer.apple.com/documentation/coregraphics/1402600-cgpdfdocumentgetid)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFArrayRef CGPDFDocumentGetID (     CGPDFDocumentRef document ); ``` |
| To | ``` CGPDFArrayRef _Nullable CGPDFDocumentGetID (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentGetInfo()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402589-info)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDictionaryRef CGPDFDocumentGetInfo (     CGPDFDocumentRef document ); ``` |
| To | ``` CGPDFDictionaryRef _Nullable CGPDFDocumentGetInfo (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentGetMediaBox()](https://developer.apple.com/documentation/coregraphics/1402592-cgpdfdocumentgetmediabox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFDocumentGetMediaBox (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` CGRect CGPDFDocumentGetMediaBox (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetNumberOfPages()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402595-numberofpages)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGPDFDocumentGetNumberOfPages (     CGPDFDocumentRef document ); ``` |
| To | ``` size_t CGPDFDocumentGetNumberOfPages (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentGetPage()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402586-page)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFPageRef CGPDFDocumentGetPage (     CGPDFDocumentRef document,     size_t pageNumber ); ``` |
| To | ``` CGPDFPageRef _Nullable CGPDFDocumentGetPage (     CGPDFDocumentRef _Nullable document,     size_t pageNumber ); ``` |

Modified [CGPDFDocumentGetRotationAngle()](https://developer.apple.com/documentation/coregraphics/1402602-cgpdfdocumentgetrotationangle)

|  | Declaration |
| --- | --- |
| From | ``` int CGPDFDocumentGetRotationAngle (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` int CGPDFDocumentGetRotationAngle (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetTrimBox()](https://developer.apple.com/documentation/coregraphics/1402590-cgpdfdocumentgettrimbox)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFDocumentGetTrimBox (     CGPDFDocumentRef document,     int page ); ``` |
| To | ``` CGRect CGPDFDocumentGetTrimBox (     CGPDFDocumentRef _Nullable document,     int page ); ``` |

Modified [CGPDFDocumentGetVersion()](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402604-getversion)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFDocumentGetVersion (     CGPDFDocumentRef document,     int *majorVersion,     int *minorVersion ); ``` |
| To | ``` void CGPDFDocumentGetVersion (     CGPDFDocumentRef _Nullable document,     int * _Nonnull majorVersion,     int * _Nonnull minorVersion ); ``` |

Modified [CGPDFDocumentIsEncrypted()](https://developer.apple.com/documentation/coregraphics/1402591-cgpdfdocumentisencrypted)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDocumentIsEncrypted (     CGPDFDocumentRef document ); ``` |
| To | ``` bool CGPDFDocumentIsEncrypted (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentIsUnlocked()](https://developer.apple.com/documentation/coregraphics/1402607-cgpdfdocumentisunlocked)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDocumentIsUnlocked (     CGPDFDocumentRef document ); ``` |
| To | ``` bool CGPDFDocumentIsUnlocked (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentRelease()](https://developer.apple.com/documentation/coregraphics/1402593-cgpdfdocumentrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFDocumentRelease (     CGPDFDocumentRef document ); ``` |
| To | ``` void CGPDFDocumentRelease (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentRetain()](https://developer.apple.com/documentation/coregraphics/1402587-cgpdfdocumentretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDocumentRef CGPDFDocumentRetain (     CGPDFDocumentRef document ); ``` |
| To | ``` CGPDFDocumentRef _Nullable CGPDFDocumentRetain (     CGPDFDocumentRef _Nullable document ); ``` |

Modified [CGPDFDocumentUnlockWithPassword()](https://developer.apple.com/documentation/coregraphics/1402599-cgpdfdocumentunlockwithpassword)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFDocumentUnlockWithPassword (     CGPDFDocumentRef document,     const char *password ); ``` |
| To | ``` bool CGPDFDocumentUnlockWithPassword (     CGPDFDocumentRef _Nullable document,     const char * _Nonnull password ); ``` |

#### CGPDFObject.h

Modified [CGPDFObjectGetType()](https://developer.apple.com/documentation/coregraphics/1455189-cgpdfobjectgettype)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFObjectType CGPDFObjectGetType (     CGPDFObjectRef object ); ``` |
| To | ``` CGPDFObjectType CGPDFObjectGetType (     CGPDFObjectRef _Nullable object ); ``` |

Modified [CGPDFObjectGetValue()](https://developer.apple.com/documentation/coregraphics/1456508-cgpdfobjectgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFObjectGetValue (     CGPDFObjectRef object,     CGPDFObjectType type,     void *value ); ``` |
| To | ``` bool CGPDFObjectGetValue (     CGPDFObjectRef _Nullable object,     CGPDFObjectType type,     void * _Nullable value ); ``` |

#### CGPDFOperatorTable.h

Modified [CGPDFOperatorTableCreate()](https://developer.apple.com/documentation/coregraphics/1455932-cgpdfoperatortablecreate)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFOperatorTableRef CGPDFOperatorTableCreate (     void ); ``` |
| To | ``` CGPDFOperatorTableRef _Nullable CGPDFOperatorTableCreate (     void ); ``` |

Modified [CGPDFOperatorTableRelease()](https://developer.apple.com/documentation/coregraphics/1455277-cgpdfoperatortablerelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFOperatorTableRelease (     CGPDFOperatorTableRef table ); ``` |
| To | ``` void CGPDFOperatorTableRelease (     CGPDFOperatorTableRef _Nullable table ); ``` |

Modified [CGPDFOperatorTableRetain()](https://developer.apple.com/documentation/coregraphics/1454547-cgpdfoperatortableretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFOperatorTableRef CGPDFOperatorTableRetain (     CGPDFOperatorTableRef table ); ``` |
| To | ``` CGPDFOperatorTableRef _Nullable CGPDFOperatorTableRetain (     CGPDFOperatorTableRef _Nullable table ); ``` |

Modified [CGPDFOperatorTableSetCallback()](https://developer.apple.com/documentation/coregraphics/1454118-cgpdfoperatortablesetcallback)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFOperatorTableSetCallback (     CGPDFOperatorTableRef table,     const char *name,     CGPDFOperatorCallback callback ); ``` |
| To | ``` void CGPDFOperatorTableSetCallback (     CGPDFOperatorTableRef _Nullable table,     const char * _Nullable name,     CGPDFOperatorCallback _Nullable callback ); ``` |

#### CGPDFPage.h

Modified [CGPDFPageGetBoxRect()](https://developer.apple.com/documentation/coregraphics/1456114-cgpdfpagegetboxrect)

|  | Declaration |
| --- | --- |
| From | ``` CGRect CGPDFPageGetBoxRect (     CGPDFPageRef page,     CGPDFBox box ); ``` |
| To | ``` CGRect CGPDFPageGetBoxRect (     CGPDFPageRef _Nullable page,     CGPDFBox box ); ``` |

Modified [CGPDFPageGetDictionary()](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1455125-dictionary)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDictionaryRef CGPDFPageGetDictionary (     CGPDFPageRef page ); ``` |
| To | ``` CGPDFDictionaryRef _Nullable CGPDFPageGetDictionary (     CGPDFPageRef _Nullable page ); ``` |

Modified [CGPDFPageGetDocument()](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1456166-document)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDocumentRef CGPDFPageGetDocument (     CGPDFPageRef page ); ``` |
| To | ``` CGPDFDocumentRef _Nullable CGPDFPageGetDocument (     CGPDFPageRef _Nullable page ); ``` |

Modified [CGPDFPageGetDrawingTransform()](https://developer.apple.com/documentation/coregraphics/1454893-cgpdfpagegetdrawingtransform)

|  | Declaration |
| --- | --- |
| From | ``` CGAffineTransform CGPDFPageGetDrawingTransform (     CGPDFPageRef page,     CGPDFBox box,     CGRect rect,     int rotate,     bool preserveAspectRatio ); ``` |
| To | ``` CGAffineTransform CGPDFPageGetDrawingTransform (     CGPDFPageRef _Nullable page,     CGPDFBox box,     CGRect rect,     int rotate,     bool preserveAspectRatio ); ``` |

Modified [CGPDFPageGetPageNumber()](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1454587-pagenumber)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGPDFPageGetPageNumber (     CGPDFPageRef page ); ``` |
| To | ``` size_t CGPDFPageGetPageNumber (     CGPDFPageRef _Nullable page ); ``` |

Modified [CGPDFPageGetRotationAngle()](https://developer.apple.com/documentation/coregraphics/1455550-cgpdfpagegetrotationangle)

|  | Declaration |
| --- | --- |
| From | ``` int CGPDFPageGetRotationAngle (     CGPDFPageRef page ); ``` |
| To | ``` int CGPDFPageGetRotationAngle (     CGPDFPageRef _Nullable page ); ``` |

Modified [CGPDFPageRelease()](https://developer.apple.com/documentation/coregraphics/1571724-cgpdfpagerelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFPageRelease (     CGPDFPageRef page ); ``` |
| To | ``` void CGPDFPageRelease (     CGPDFPageRef _Nullable page ); ``` |

Modified [CGPDFPageRetain()](https://developer.apple.com/documentation/coregraphics/1571723-cgpdfpageretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFPageRef CGPDFPageRetain (     CGPDFPageRef page ); ``` |
| To | ``` CGPDFPageRef _Nullable CGPDFPageRetain (     CGPDFPageRef _Nullable page ); ``` |

#### CGPDFScanner.h

Modified [CGPDFScannerCreate()](https://developer.apple.com/documentation/coregraphics/1454410-cgpdfscannercreate)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFScannerRef CGPDFScannerCreate (     CGPDFContentStreamRef cs,     CGPDFOperatorTableRef table,     void *info ); ``` |
| To | ``` CGPDFScannerRef _Nonnull CGPDFScannerCreate (     CGPDFContentStreamRef _Nonnull cs,     CGPDFOperatorTableRef _Nullable table,     void * _Nullable info ); ``` |

Modified [CGPDFScannerGetContentStream()](https://developer.apple.com/documentation/coregraphics/1454724-cgpdfscannergetcontentstream)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFContentStreamRef CGPDFScannerGetContentStream (     CGPDFScannerRef scanner ); ``` |
| To | ``` CGPDFContentStreamRef _Nonnull CGPDFScannerGetContentStream (     CGPDFScannerRef _Nonnull scanner ); ``` |

Modified [CGPDFScannerPopArray()](https://developer.apple.com/documentation/coregraphics/1454360-cgpdfscannerpoparray)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopArray (     CGPDFScannerRef scanner,     CGPDFArrayRef *value ); ``` |
| To | ``` bool CGPDFScannerPopArray (     CGPDFScannerRef _Nonnull scanner,     CGPDFArrayRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerPopBoolean()](https://developer.apple.com/documentation/coregraphics/1454663-cgpdfscannerpopboolean)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopBoolean (     CGPDFScannerRef scanner,     CGPDFBoolean *value ); ``` |
| To | ``` bool CGPDFScannerPopBoolean (     CGPDFScannerRef _Nonnull scanner,     CGPDFBoolean * _Nullable value ); ``` |

Modified [CGPDFScannerPopDictionary()](https://developer.apple.com/documentation/coregraphics/1456538-cgpdfscannerpopdictionary)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopDictionary (     CGPDFScannerRef scanner,     CGPDFDictionaryRef *value ); ``` |
| To | ``` bool CGPDFScannerPopDictionary (     CGPDFScannerRef _Nonnull scanner,     CGPDFDictionaryRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerPopInteger()](https://developer.apple.com/documentation/coregraphics/1454399-cgpdfscannerpopinteger)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopInteger (     CGPDFScannerRef scanner,     CGPDFInteger *value ); ``` |
| To | ``` bool CGPDFScannerPopInteger (     CGPDFScannerRef _Nonnull scanner,     CGPDFInteger * _Nullable value ); ``` |

Modified [CGPDFScannerPopName()](https://developer.apple.com/documentation/coregraphics/1454584-cgpdfscannerpopname)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopName (     CGPDFScannerRef scanner,     const char **value ); ``` |
| To | ``` bool CGPDFScannerPopName (     CGPDFScannerRef _Nonnull scanner,     const char * _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerPopNumber()](https://developer.apple.com/documentation/coregraphics/1456297-cgpdfscannerpopnumber)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopNumber (     CGPDFScannerRef scanner,     CGPDFReal *value ); ``` |
| To | ``` bool CGPDFScannerPopNumber (     CGPDFScannerRef _Nonnull scanner,     CGPDFReal * _Nullable value ); ``` |

Modified [CGPDFScannerPopObject()](https://developer.apple.com/documentation/coregraphics/1455971-cgpdfscannerpopobject)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopObject (     CGPDFScannerRef scanner,     CGPDFObjectRef *value ); ``` |
| To | ``` bool CGPDFScannerPopObject (     CGPDFScannerRef _Nonnull scanner,     CGPDFObjectRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerPopStream()](https://developer.apple.com/documentation/coregraphics/1454561-cgpdfscannerpopstream)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopStream (     CGPDFScannerRef scanner,     CGPDFStreamRef *value ); ``` |
| To | ``` bool CGPDFScannerPopStream (     CGPDFScannerRef _Nonnull scanner,     CGPDFStreamRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerPopString()](https://developer.apple.com/documentation/coregraphics/1455018-cgpdfscannerpopstring)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerPopString (     CGPDFScannerRef scanner,     CGPDFStringRef *value ); ``` |
| To | ``` bool CGPDFScannerPopString (     CGPDFScannerRef _Nonnull scanner,     CGPDFStringRef  _Nullable * _Nullable value ); ``` |

Modified [CGPDFScannerRelease()](https://developer.apple.com/documentation/coregraphics/1454962-cgpdfscannerrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGPDFScannerRelease (     CGPDFScannerRef scanner ); ``` |
| To | ``` void CGPDFScannerRelease (     CGPDFScannerRef _Nullable scanner ); ``` |

Modified [CGPDFScannerRetain()](https://developer.apple.com/documentation/coregraphics/1455810-cgpdfscannerretain)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFScannerRef CGPDFScannerRetain (     CGPDFScannerRef scanner ); ``` |
| To | ``` CGPDFScannerRef _Nullable CGPDFScannerRetain (     CGPDFScannerRef _Nullable scanner ); ``` |

Modified [CGPDFScannerScan()](https://developer.apple.com/documentation/coregraphics/1454698-cgpdfscannerscan)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPDFScannerScan (     CGPDFScannerRef scanner ); ``` |
| To | ``` bool CGPDFScannerScan (     CGPDFScannerRef _Nullable scanner ); ``` |

#### CGPDFStream.h

Modified [CGPDFStreamCopyData()](https://developer.apple.com/documentation/coregraphics/1454657-cgpdfstreamcopydata)

|  | Declaration |
| --- | --- |
| From | ``` CFDataRef CGPDFStreamCopyData (     CGPDFStreamRef stream,     CGPDFDataFormat *format ); ``` |
| To | ``` CFDataRef _Nullable CGPDFStreamCopyData (     CGPDFStreamRef _Nullable stream,     CGPDFDataFormat * _Nullable format ); ``` |

Modified [CGPDFStreamGetDictionary()](https://developer.apple.com/documentation/coregraphics/1456118-cgpdfstreamgetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CGPDFDictionaryRef CGPDFStreamGetDictionary (     CGPDFStreamRef stream ); ``` |
| To | ``` CGPDFDictionaryRef _Nullable CGPDFStreamGetDictionary (     CGPDFStreamRef _Nullable stream ); ``` |

#### CGPDFString.h

Modified [CGPDFStringCopyDate()](https://developer.apple.com/documentation/coregraphics/1454295-cgpdfstringcopydate)

|  | Declaration |
| --- | --- |
| From | ``` CFDateRef CGPDFStringCopyDate (     CGPDFStringRef string ); ``` |
| To | ``` CFDateRef _Nullable CGPDFStringCopyDate (     CGPDFStringRef _Nullable string ); ``` |

Modified [CGPDFStringCopyTextString()](https://developer.apple.com/documentation/coregraphics/1456234-cgpdfstringcopytextstring)

|  | Declaration |
| --- | --- |
| From | ``` CFStringRef CGPDFStringCopyTextString (     CGPDFStringRef string ); ``` |
| To | ``` CFStringRef _Nullable CGPDFStringCopyTextString (     CGPDFStringRef _Nullable string ); ``` |

Modified [CGPDFStringGetBytePtr()](https://developer.apple.com/documentation/coregraphics/1455978-cgpdfstringgetbyteptr)

|  | Declaration |
| --- | --- |
| From | ``` const unsigned char * CGPDFStringGetBytePtr (     CGPDFStringRef string ); ``` |
| To | ``` const unsigned char * _Nullable CGPDFStringGetBytePtr (     CGPDFStringRef _Nullable string ); ``` |

Modified [CGPDFStringGetLength()](https://developer.apple.com/documentation/coregraphics/1454095-cgpdfstringgetlength)

|  | Declaration |
| --- | --- |
| From | ``` size_t CGPDFStringGetLength (     CGPDFStringRef string ); ``` |
| To | ``` size_t CGPDFStringGetLength (     CGPDFStringRef _Nullable string ); ``` |

#### CGPSConverter.h

Modified [CGPSConverterAbort()](https://developer.apple.com/documentation/coregraphics/1455046-cgpsconverterabort)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPSConverterAbort (     CGPSConverterRef converter ); ``` |
| To | ``` bool CGPSConverterAbort (     CGPSConverterRef _Nonnull converter ); ``` |

Modified [CGPSConverterConvert()](https://developer.apple.com/documentation/coregraphics/1455368-cgpsconverterconvert)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPSConverterConvert (     CGPSConverterRef converter,     CGDataProviderRef provider,     CGDataConsumerRef consumer,     CFDictionaryRef options ); ``` |
| To | ``` bool CGPSConverterConvert (     CGPSConverterRef _Nonnull converter,     CGDataProviderRef _Nonnull provider,     CGDataConsumerRef _Nonnull consumer,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGPSConverterCreate()](https://developer.apple.com/documentation/coregraphics/1454773-cgpsconvertercreate)

|  | Declaration |
| --- | --- |
| From | ``` CGPSConverterRef CGPSConverterCreate (     void *info,     const CGPSConverterCallbacks *callbacks,     CFDictionaryRef options ); ``` |
| To | ``` CGPSConverterRef _Nullable CGPSConverterCreate (     void * _Nullable info,     const CGPSConverterCallbacks * _Nonnull callbacks,     CFDictionaryRef _Nullable options ); ``` |

Modified [CGPSConverterIsConverting()](https://developer.apple.com/documentation/coregraphics/1454582-cgpsconverterisconverting)

|  | Declaration |
| --- | --- |
| From | ``` bool CGPSConverterIsConverting (     CGPSConverterRef converter ); ``` |
| To | ``` bool CGPSConverterIsConverting (     CGPSConverterRef _Nonnull converter ); ``` |

#### CGRemoteOperation.h

Modified [CGRegisterScreenRefreshCallback()](https://developer.apple.com/documentation/coregraphics/1541774-cgregisterscreenrefreshcallback)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGRegisterScreenRefreshCallback (     CGScreenRefreshCallback callback,     void *userInfo ); ``` |
| To | ``` CGError CGRegisterScreenRefreshCallback (     CGScreenRefreshCallback _Nonnull callback,     void * _Nullable userInfo ); ``` |

Modified [CGReleaseScreenRefreshRects()](https://developer.apple.com/documentation/coregraphics/1541780-cgreleasescreenrefreshrects)

|  | Declaration |
| --- | --- |
| From | ``` void CGReleaseScreenRefreshRects (     CGRect *rects ); ``` |
| To | ``` void CGReleaseScreenRefreshRects (     CGRect * _Nullable rects ); ``` |

Modified [CGScreenRegisterMoveCallback()](https://developer.apple.com/documentation/coregraphics/1541791-cgscreenregistermovecallback)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGScreenRegisterMoveCallback (     CGScreenUpdateMoveCallback callback,     void *userInfo ); ``` |
| To | ``` CGError CGScreenRegisterMoveCallback (     CGScreenUpdateMoveCallback _Nonnull callback,     void * _Nullable userInfo ); ``` |

Modified [CGScreenUnregisterMoveCallback()](https://developer.apple.com/documentation/coregraphics/1541795-cgscreenunregistermovecallback)

|  | Declaration |
| --- | --- |
| From | ``` void CGScreenUnregisterMoveCallback (     CGScreenUpdateMoveCallback callback,     void *userInfo ); ``` |
| To | ``` void CGScreenUnregisterMoveCallback (     CGScreenUpdateMoveCallback _Nonnull callback,     void * _Nullable userInfo ); ``` |

Modified [CGUnregisterScreenRefreshCallback()](https://developer.apple.com/documentation/coregraphics/1541807-cgunregisterscreenrefreshcallbac)

|  | Declaration |
| --- | --- |
| From | ``` void CGUnregisterScreenRefreshCallback (     CGScreenRefreshCallback callback,     void *userInfo ); ``` |
| To | ``` void CGUnregisterScreenRefreshCallback (     CGScreenRefreshCallback _Nonnull callback,     void * _Nullable userInfo ); ``` |

Modified [CGWaitForScreenRefreshRects()](https://developer.apple.com/documentation/coregraphics/1541809-cgwaitforscreenrefreshrects)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGWaitForScreenRefreshRects (     CGRect **rects,     uint32_t *count ); ``` |
| To | ``` CGError CGWaitForScreenRefreshRects (     CGRect * _Nullable * _Nullable rects,     uint32_t * _Nullable count ); ``` |

Modified [CGWaitForScreenUpdateRects()](https://developer.apple.com/documentation/coregraphics/1541790-cgwaitforscreenupdaterects)

|  | Declaration |
| --- | --- |
| From | ``` CGError CGWaitForScreenUpdateRects (     CGScreenUpdateOperation requestedOperations,     CGScreenUpdateOperation *currentOperation,     CGRect **rects,     size_t *rectCount,     CGScreenUpdateMoveDelta *delta ); ``` |
| To | ``` CGError CGWaitForScreenUpdateRects (     CGScreenUpdateOperation requestedOperations,     CGScreenUpdateOperation * _Nullable currentOperation,     CGRect * _Nullable * _Nullable rects,     size_t * _Nullable rectCount,     CGScreenUpdateMoveDelta * _Nullable delta ); ``` |

Modified [CGWindowServerCFMachPort()](https://developer.apple.com/documentation/coregraphics/1541813-cgwindowservercfmachport)

|  | Declaration |
| --- | --- |
| From | ``` CFMachPortRef CGWindowServerCFMachPort (     void ); ``` |
| To | ``` CFMachPortRef _Nullable CGWindowServerCFMachPort (     void ); ``` |

Modified [CGWindowServerCreateServerPort()](https://developer.apple.com/documentation/coregraphics/1454440-cgwindowservercreateserverport)

|  | Declaration |
| --- | --- |
| From | ``` CFMachPortRef CGWindowServerCreateServerPort (     void ); ``` |
| To | ``` CFMachPortRef _Nullable CGWindowServerCreateServerPort (     void ); ``` |

#### CGSession.h

Modified [CGSessionCopyCurrentDictionary()](https://developer.apple.com/documentation/coregraphics/1454780-cgsessioncopycurrentdictionary)

|  | Declaration |
| --- | --- |
| From | ``` CFDictionaryRef CGSessionCopyCurrentDictionary (     void ); ``` |
| To | ``` CFDictionaryRef _Nullable CGSessionCopyCurrentDictionary (     void ); ``` |

#### CGShading.h

Modified [CGShadingCreateAxial()](https://developer.apple.com/documentation/coregraphics/1455224-cgshadingcreateaxial)

|  | Declaration |
| --- | --- |
| From | ``` CGShadingRef CGShadingCreateAxial (     CGColorSpaceRef space,     CGPoint start,     CGPoint end,     CGFunctionRef function,     bool extendStart,     bool extendEnd ); ``` |
| To | ``` CGShadingRef _Nullable CGShadingCreateAxial (     CGColorSpaceRef _Nullable space,     CGPoint start,     CGPoint end,     CGFunctionRef _Nullable function,     bool extendStart,     bool extendEnd ); ``` |

Modified [CGShadingCreateRadial()](https://developer.apple.com/documentation/coregraphics/1456399-cgshadingcreateradial)

|  | Declaration |
| --- | --- |
| From | ``` CGShadingRef CGShadingCreateRadial (     CGColorSpaceRef space,     CGPoint start,     CGFloat startRadius,     CGPoint end,     CGFloat endRadius,     CGFunctionRef function,     bool extendStart,     bool extendEnd ); ``` |
| To | ``` CGShadingRef _Nullable CGShadingCreateRadial (     CGColorSpaceRef _Nullable space,     CGPoint start,     CGFloat startRadius,     CGPoint end,     CGFloat endRadius,     CGFunctionRef _Nullable function,     bool extendStart,     bool extendEnd ); ``` |

Modified [CGShadingRelease()](https://developer.apple.com/documentation/coregraphics/1573766-cgshadingrelease)

|  | Declaration |
| --- | --- |
| From | ``` void CGShadingRelease (     CGShadingRef shading ); ``` |
| To | ``` void CGShadingRelease (     CGShadingRef _Nullable shading ); ``` |

Modified [CGShadingRetain()](https://developer.apple.com/documentation/coregraphics/1573767-cgshadingretain)

|  | Declaration |
| --- | --- |
| From | ``` CGShadingRef CGShadingRetain (     CGShadingRef shading ); ``` |
| To | ``` CGShadingRef _Nullable CGShadingRetain (     CGShadingRef _Nullable shading ); ``` |

#### CGWindow.h

Modified [CGWindowListCopyWindowInfo()](https://developer.apple.com/documentation/coregraphics/1455137-cgwindowlistcopywindowinfo)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGWindowListCopyWindowInfo (     CGWindowListOption option,     CGWindowID relativeToWindow ); ``` |
| To | ``` CFArrayRef _Nullable CGWindowListCopyWindowInfo (     CGWindowListOption option,     CGWindowID relativeToWindow ); ``` |

Modified [CGWindowListCreate()](https://developer.apple.com/documentation/coregraphics/1552209-cgwindowlistcreate)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGWindowListCreate (     CGWindowListOption option,     CGWindowID relativeToWindow ); ``` |
| To | ``` CFArrayRef _Nullable CGWindowListCreate (     CGWindowListOption option,     CGWindowID relativeToWindow ); ``` |

Modified [CGWindowListCreateDescriptionFromArray()](https://developer.apple.com/documentation/coregraphics/1455215-cgwindowlistcreatedescriptionfro)

|  | Declaration |
| --- | --- |
| From | ``` CFArrayRef CGWindowListCreateDescriptionFromArray (     CFArrayRef windowArray ); ``` |
| To | ``` CFArrayRef _Nullable CGWindowListCreateDescriptionFromArray (     CFArrayRef _Nullable windowArray ); ``` |

Modified [CGWindowListCreateImage()](https://developer.apple.com/documentation/coregraphics/1454852-cgwindowlistcreateimage)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGWindowListCreateImage (     CGRect screenBounds,     CGWindowListOption listOption,     CGWindowID windowID,     CGWindowImageOption imageOption ); ``` |
| To | ``` CGImageRef _Nullable CGWindowListCreateImage (     CGRect screenBounds,     CGWindowListOption listOption,     CGWindowID windowID,     CGWindowImageOption imageOption ); ``` |

Modified [CGWindowListCreateImageFromArray()](https://developer.apple.com/documentation/coregraphics/cgimage/1455730-init)

|  | Declaration |
| --- | --- |
| From | ``` CGImageRef CGWindowListCreateImageFromArray (     CGRect screenBounds,     CFArrayRef windowArray,     CGWindowImageOption imageOption ); ``` |
| To | ``` CGImageRef _Nullable CGWindowListCreateImageFromArray (     CGRect screenBounds,     CFArrayRef _Nonnull windowArray,     CGWindowImageOption imageOption ); ``` |

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

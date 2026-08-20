---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/CoreGraphics.html
archived_at: '2026-07-18T02:57:38.362084Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# CoreGraphics Changes for Swift

### CoreGraphics

Removed [CGBitmapInfo.ByteOrderDefault](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapbyteorderdefault)Removed CGColorConverterTransformType [enum]Removed CGColorConverterTransformType.applySpaceRemoved CGColorConverterTransformType.fromSpaceRemoved CGColorConverterTransformType.toSpaceRemoved [CGDataConsumerCallbacks.init(putBytes: CGDataConsumerPutBytesCallback?, releaseConsumer: CGDataConsumerReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1454242-init)Removed [CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback?, releaseBytePointer: CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1455604-init)Removed [CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CGDataProviderGetBytesCallback?, skipForward: CGDataProviderSkipForwardCallback?, rewind: CGDataProviderRewindCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1456529-init)Removed CGFloat.advancedBy(_: CGFloat) -> CGFloatRemoved CGFloat.distanceTo(_: CGFloat) -> CGFloatRemoved CGFloat.isSignalingRemoved CGFloat.isSignMinusRemoved CGFloat.maxRemoved CGFloat.minRemoved CGFloat.NaNRemoved CGFloat.quietNaNRemoved [CGFunctionCallbacks.init(version: UInt32, evaluate: CGFunctionEvaluateCallback?, releaseInfo: CGFunctionReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1454863-init)Removed CGPatternCallbacks.init(version: UInt32, drawPattern: CGPatternDrawPatternCallback?, releaseInfo: CGPatternReleaseInfoCallback?)Removed CGRect.contains(_: CGRect) -> BoolRemoved CGRect.contains(_: CGPoint) -> BoolRemoved CGRect.divide(_: CGFloat, fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)Removed CGRect.heightRemoved CGRect.infiniteRemoved CGRect.insetBy(dx: CGFloat, dy: CGFloat) -> CGRectRemoved CGRect.insetInPlace(dx: CGFloat, dy: CGFloat)Removed CGRect.integralRemoved CGRect.intersect(_: CGRect) -> CGRectRemoved CGRect.intersectInPlace(_: CGRect)Removed CGRect.intersects(_: CGRect) -> BoolRemoved CGRect.isEmptyRemoved CGRect.isInfiniteRemoved CGRect.isNullRemoved CGRect.makeIntegralInPlace()Removed CGRect.maxXRemoved CGRect.maxYRemoved CGRect.midXRemoved CGRect.midYRemoved CGRect.minXRemoved CGRect.minYRemoved CGRect.nullRemoved CGRect.offsetBy(dx: CGFloat, dy: CGFloat) -> CGRectRemoved CGRect.offsetInPlace(dx: CGFloat, dy: CGFloat)Removed CGRect.standardizedRemoved CGRect.standardizeInPlace()Removed CGRect.union(_: CGRect) -> CGRectRemoved CGRect.unionInPlace(_: CGRect)Removed CGRect.widthRemoved %(_: CGFloat, _: CGFloat) -> CGFloatRemoved %=(_: CGFloat, _: CGFloat)Removed +(_: CGFloat) -> CGFloatRemoved ++(_: CGFloat) -> CGFloatRemoved ++(_: CGFloat) -> CGFloatRemoved -(_: CGFloat) -> CGFloatRemoved --(_: CGFloat) -> CGFloatRemoved --(_: CGFloat) -> CGFloatRemoved <(_: CGFloat, _: CGFloat) -> BoolRemoved ==(_: CGFloat, _: CGFloat) -> BoolRemoved ceil(_: CGFloat) -> CGFloatRemoved [CGAffineTransformEqualToTransform(_: CGAffineTransform, _: CGAffineTransform) -> Bool](https://developer.apple.com/documentation/coregraphics/1455732-cgaffinetransformequaltotransfor)Removed CGAffineTransformIdentityRemoved [CGAffineTransformIdentity](https://developer.apple.com/documentation/coregraphics/cgaffinetransformidentity)Removed [CGAffineTransformMake(_: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1455865-cgaffinetransformmake)Removed CGColorConverterRemoved CGColorConverterCreateSimple(_: CGColorSpace?, _: CGColorSpace?) -> CGColorConverterRefRemoved CGColorConverterGetTypeID() -> CFTypeIDRemoved CGColorConverterRelease(_: CGColorConverterRef)Removed [CGColorEqualToColor(_: CGColor?, _: CGColor?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455217-cgcolorequaltocolor)Removed [CGColorGetComponents(_: CGColor?) -> UnsafePointer<CGFloat>](https://developer.apple.com/documentation/coregraphics/1455930-cgcolorgetcomponents)Removed [CGColorSpaceGetColorTable(_: CGColorSpace?, _: UnsafeMutablePointer<UInt8>)](https://developer.apple.com/documentation/coregraphics/1408853-cgcolorspacegetcolortable)Removed [CGColorSpaceGetColorTableCount(_: CGColorSpace?) -> Int](https://developer.apple.com/documentation/coregraphics/1408883-cgcolorspacegetcolortablecount)Removed [CGContextAddArc(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: Int32)](https://developer.apple.com/documentation/coregraphics/1455756-cgcontextaddarc)Removed [CGContextAddArcToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456238-cgcontextaddarctopoint)Removed [CGContextAddCurveToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456393-cgcontextaddcurvetopoint)Removed [CGContextAddLines(_: CGContext?, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1455461-cgcontextaddlines)Removed [CGContextAddLineToPoint(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455213-cgcontextaddlinetopoint)Removed [CGContextAddQuadCurveToPoint(_: CGContext?, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454268-cgcontextaddquadcurvetopoint)Removed [CGContextAddRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454734-cgcontextaddrects)Removed [CGContextClip(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455262-cgcontextclip)Removed [CGContextClipToRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454626-cgcontextcliptorects)Removed [CGContextDrawImage(_: CGContext?, _: CGRect, _: CGImage?)](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage)Removed [CGContextDrawLayerAtPoint(_: CGContext?, _: CGPoint, _: CGLayer?)](https://developer.apple.com/documentation/coregraphics/1450894-cgcontextdrawlayeratpoint)Removed [CGContextDrawLayerInRect(_: CGContext?, _: CGRect, _: CGLayer?)](https://developer.apple.com/documentation/coregraphics/1450896-cgcontextdrawlayerinrect)Removed [CGContextDrawTiledImage(_: CGContext?, _: CGRect, _: CGImage?)](https://developer.apple.com/documentation/coregraphics/1456240-cgcontextdrawtiledimage)Removed [CGContextEOClip(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1455944-cgcontexteoclip)Removed [CGContextEOFillPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1454865-cgcontexteofillpath)Removed [CGContextFillPath(_: CGContext?)](https://developer.apple.com/documentation/coregraphics/1456306-cgcontextfillpath)Removed [CGContextFillRects(_: CGContext?, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454132-cgcontextfillrects)Removed [CGContextGetTextPosition(_: CGContext?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1454687-cgcontextgettextposition)Removed [CGContextMoveToPoint(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454738-cgcontextmovetopoint)Removed [CGContextSetInterpolationQuality(_: CGContext?, _: CGInterpolationQuality)](https://developer.apple.com/documentation/coregraphics/1455656-cgcontextsetinterpolationquality)Removed [CGContextSetLineDash(_: CGContext?, _: CGFloat, _: UnsafePointer<CGFloat>, _: Int)](https://developer.apple.com/documentation/coregraphics/1455911-cgcontextsetlinedash)Removed [CGContextSetTextMatrix(_: CGContext?, _: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/1455611-cgcontextsettextmatrix)Removed [CGContextSetTextPosition(_: CGContext?, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456069-cgcontextsettextposition)Removed [CGContextShowGlyphsAtPositions(_: CGContext?, _: UnsafePointer<CGGlyph>, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1456200-cgcontextshowglyphsatpositions)Removed [CGContextStrokeLineSegments(_: CGContext?, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1454389-cgcontextstrokelinesegments)Removed [CGImageCreateWithMaskingColors(_: CGImage?, _: UnsafePointer<CGFloat>) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454358-cgimagecreatewithmaskingcolors)Removed [CGPathAddArc(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: Bool)](https://developer.apple.com/documentation/coregraphics/1411147-cgpathaddarc)Removed [CGPathAddArcToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411173-cgpathaddarctopoint)Removed [CGPathAddCurveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411212-cgpathaddcurvetopoint)Removed [CGPathAddEllipseInRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1411222-cgpathaddellipseinrect)Removed [CGPathAddLines(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: UnsafePointer<CGPoint>, _: Int)](https://developer.apple.com/documentation/coregraphics/1411171-cgpathaddlines)Removed [CGPathAddLineToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411138-cgpathaddlinetopoint)Removed [CGPathAddPath(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGPath?)](https://developer.apple.com/documentation/coregraphics/1411201-cgpathaddpath)Removed [CGPathAddQuadCurveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411157-cgpathaddquadcurvetopoint)Removed [CGPathAddRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect)](https://developer.apple.com/documentation/coregraphics/1411144-cgpathaddrect)Removed [CGPathAddRects(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: UnsafePointer<CGRect>, _: Int)](https://developer.apple.com/documentation/coregraphics/1411153-cgpathaddrects)Removed [CGPathAddRelativeArc(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411136-cgpathaddrelativearc)Removed [CGPathAddRoundedRect(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGRect, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411124-cgpathaddroundedrect)Removed [CGPathContainsPoint(_: CGPath?, _: UnsafePointer<CGAffineTransform>, _: CGPoint, _: Bool) -> Bool](https://developer.apple.com/documentation/coregraphics/1411175-cgpathcontainspoint)Removed [CGPathEqualToPath(_: CGPath?, _: CGPath?) -> Bool](https://developer.apple.com/documentation/coregraphics/1411167-cgpathequaltopath)Removed [CGPathMoveToPoint(_: CGMutablePath?, _: UnsafePointer<CGAffineTransform>, _: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411146-cgpathmovetopoint)Removed [CGPointMake(_: CGFloat, _: CGFloat) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1455746-cgpointmake)Removed [CGPointMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGPoint>) -> Bool](https://developer.apple.com/documentation/coregraphics/1455338-cgpointmakewithdictionaryreprese)Removed [CGPointZero](https://developer.apple.com/documentation/coregraphics/cgpointzero)Removed CGPointZeroRemoved [CGRectDivide(_: CGRect, _: UnsafeMutablePointer<CGRect>, _: UnsafeMutablePointer<CGRect>, _: CGFloat, _: CGRectEdge)](https://developer.apple.com/documentation/coregraphics/1455925-cgrectdivide)Removed [CGRectMake(_: CGFloat, _: CGFloat, _: CGFloat, _: CGFloat) -> CGRect](https://developer.apple.com/documentation/coregraphics/1455245-cgrectmake)Removed [CGRectMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/coregraphics/1456558-cgrectmakewithdictionaryrepresen)Removed [CGRectZero](https://developer.apple.com/documentation/coregraphics/cgrectzero)Removed CGRectZeroRemoved [CGSizeMake(_: CGFloat, _: CGFloat) -> CGSize](https://developer.apple.com/documentation/coregraphics/1455082-cgsizemake)Removed [CGSizeMakeWithDictionaryRepresentation(_: CFDictionary?, _: UnsafeMutablePointer<CGSize>) -> Bool](https://developer.apple.com/documentation/coregraphics/1454318-cgsizemakewithdictionaryrepresen)Removed CGSizeZeroRemoved [CGSizeZero](https://developer.apple.com/documentation/coregraphics/cgsizezero)Removed [CGVectorMake(_: CGFloat, _: CGFloat) -> CGVector](https://developer.apple.com/documentation/coregraphics/1454811-cgvectormake)Removed fabs(_: CGFloat) -> CGFloatRemoved floor(_: CGFloat) -> CGFloatRemoved fma(_: CGFloat, _: CGFloat, _: CGFloat) -> CGFloatRemoved fmod(_: CGFloat, _: CGFloat) -> CGFloatRemoved fpclassify(_: CGFloat) -> IntRemoved isfinite(_: CGFloat) -> BoolRemoved isinf(_: CGFloat) -> BoolRemoved isnan(_: CGFloat) -> BoolRemoved isnormal(_: CGFloat) -> BoolRemoved [kCGColorSpaceGenericGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgray)Removed [kCGColorSpaceGenericRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgb)Removed remainder(_: CGFloat, _: CGFloat) -> CGFloatRemoved round(_: CGFloat) -> CGFloatRemoved signbit(_: CGFloat) -> IntRemoved sqrt(_: CGFloat) -> CGFloatRemoved trunc(_: CGFloat) -> CGFloatAdded [CGAffineTransform.identity](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1455180-identity)Added [CGColor.components](https://developer.apple.com/documentation/coregraphics/cgcolor/2427146-components)Added [CGColor.conversionBlackPointCompensation](https://developer.apple.com/documentation/coregraphics/kcgcolorconversionblackpointcompensation)Added [CGColorConversionInfo](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninforef)Added [CGColorConversionInfo.init(src: CGColorSpace, dst: CGColorSpace)](https://developer.apple.com/documentation/coregraphics/2113677-cgcolorconversioninfocreate)Added [CGColorConversionInfo.typeID](https://developer.apple.com/documentation/coregraphics/2113681-cgcolorconversioninfogettypeid)Added [CGColorConversionInfoTransformType [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype)Added [CGColorConversionInfoTransformType.transformApplySpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/transformapplyspace)Added [CGColorConversionInfoTransformType.transformFromSpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/transformfromspace)Added [CGColorConversionInfoTransformType.transformToSpace](https://developer.apple.com/documentation/coregraphics/cgcolorconversioninfotransformtype/transformtospace)Added [CGColorSpace.colorTable](https://developer.apple.com/documentation/coregraphics/cgcolorspace/2427153-colortable)Added [CGColorSpace.copyICCData() -> CFData?](https://developer.apple.com/documentation/coregraphics/1644732-cgcolorspacecopyiccdata)Added [CGColorSpace.extendedGray](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1644736-extendedgray)Added [CGColorSpace.extendedLinearGray](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1690959-extendedlineargray)Added [CGColorSpace.extendedLinearSRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1690961-extendedlinearsrgb)Added [CGColorSpace.extendedSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceextendedsrgb)Added [CGColorSpace.isWideGamutRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1644737-iswidegamutrgb)Added [CGColorSpace.linearGray](https://developer.apple.com/documentation/coregraphics/kcgcolorspacelineargray)Added [CGColorSpace.linearSRGB](https://developer.apple.com/documentation/coregraphics/kcgcolorspacelinearsrgb)Added [CGColorSpace.name](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408903-name)Added [CGColorSpace.supportsOutput](https://developer.apple.com/documentation/coregraphics/1690958-cgcolorspacesupportsoutput)Added [CGContext.addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427129-addarc)Added [CGContext.addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427122-addarc)Added [CGContext.addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427127-addcurve)Added [CGContext.addLine(to: CGPoint)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427159-addline)Added [CGContext.addLines(between: [CGPoint])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427136-addlines)Added [CGContext.addQuadCurve(to: CGPoint, control: CGPoint)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427151-addquadcurve)Added [CGContext.addRects(_: [CGRect])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427132-addrects)Added [CGContext.clip(to: [CGRect])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427135-clip)Added [CGContext.clip(using: CGPathFillRule)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427152-clip)Added [CGContext.draw(_: CGLayer, at: CGPoint)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427141-draw)Added [CGContext.draw(_: CGLayer, in: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427126-draw)Added [CGContext.draw(_: CGImage, in: CGRect, byTiling: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427134-draw)Added [CGContext.fill(_: [CGRect])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427149-fill)Added [CGContext.fillPath(using: CGPathFillRule)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427156-fillpath)Added [CGContext.move(to: CGPoint)](https://developer.apple.com/documentation/coregraphics/cgcontext/2427138-move)Added [CGContext.setLineDash(phase: CGFloat, lengths: [CGFloat])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427130-setlinedash)Added [CGContext.showGlyphs(_: [CGGlyph], at: [CGPoint])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427142-showglyphs)Added [CGContext.strokeLineSegments(between: [CGPoint])](https://developer.apple.com/documentation/coregraphics/cgcontext/2427116-strokelinesegments)Added [CGContext.textPosition](https://developer.apple.com/documentation/coregraphics/cgcontext/1454687-textposition)Added [CGDataConsumerCallbacks.init(putBytes: CoreGraphics.CGDataConsumerPutBytesCallback?, releaseConsumer: CoreGraphics.CGDataConsumerReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1454242-init)Added [CGDataProviderDirectCallbacks.init(version: UInt32, getBytePointer: CoreGraphics.CGDataProviderGetBytePointerCallback?, releaseBytePointer: CoreGraphics.CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition: CoreGraphics.CGDataProviderGetBytesAtPositionCallback?, releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1455604-init)Added [CGDataProviderSequentialCallbacks.init(version: UInt32, getBytes: CoreGraphics.CGDataProviderGetBytesCallback?, skipForward: CoreGraphics.CGDataProviderSkipForwardCallback?, rewind: CoreGraphics.CGDataProviderRewindCallback?, releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1456529-init)Added CGFloat.add(_: CGFloat)Added [CGFloat.addProduct(_: CGFloat, _: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgfloat/2299982-addproduct)Added [CGFloat.advanced(by: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat/1645826-advanced)Added [CGFloat.binade](https://developer.apple.com/documentation/coregraphics/cgfloat/1845201-binade)Added [CGFloat.bitPattern](https://developer.apple.com/documentation/coregraphics/cgfloat/1845212-bitpattern)Added [CGFloat.customMirror](https://developer.apple.com/documentation/coregraphics/cgfloat/1645821-custommirror)Added [CGFloat.distance(to: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgfloat/1645824-distance)Added CGFloat.divide(by: CGFloat)Added [CGFloat.exponent](https://developer.apple.com/documentation/coregraphics/cgfloat/1845221-exponent)Added [CGFloat.exponentBitCount](https://developer.apple.com/documentation/coregraphics/cgfloat/1845233-exponentbitcount)Added [CGFloat.exponentBitPattern](https://developer.apple.com/documentation/coregraphics/cgfloat/1845216-exponentbitpattern)Added [CGFloat.formRemainder(dividingBy: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgfloat/2299980-formremainder)Added [CGFloat.formSquareRoot()](https://developer.apple.com/documentation/coregraphics/cgfloat/2299985-formsquareroot)Added [CGFloat.formTruncatingRemainder(dividingBy: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845231-formtruncatingremainder)Added [CGFloat.greatestFiniteMagnitude](https://developer.apple.com/documentation/coregraphics/cgfloat/1845207-greatestfinitemagnitude)Added [CGFloat.init(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845223-init)Added [CGFloat.init(bitPattern: UInt)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845218-init)Added [CGFloat.init(nan: CGFloat.RawSignificand, signaling: Bool)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845228-init)Added [CGFloat.init(sign: FloatingPointSign, exponent: Int, significand: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845203-init)Added [CGFloat.init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt)](https://developer.apple.com/documentation/coregraphics/cgfloat/1845204-init)Added [CGFloat.isCanonical](https://developer.apple.com/documentation/coregraphics/cgfloat/1845215-iscanonical)Added [CGFloat.isEqual(to: CGFloat) -> Bool](https://developer.apple.com/documentation/coregraphics/cgfloat/1845219-isequal)Added [CGFloat.isLess(than: CGFloat) -> Bool](https://developer.apple.com/documentation/coregraphics/cgfloat/1845208-isless)Added [CGFloat.isLessThanOrEqualTo(_: CGFloat) -> Bool](https://developer.apple.com/documentation/coregraphics/cgfloat/1845211-islessthanorequalto)Added [CGFloat.isSignalingNaN](https://developer.apple.com/documentation/coregraphics/cgfloat/1845222-issignalingnan)Added [CGFloat.leastNonzeroMagnitude](https://developer.apple.com/documentation/coregraphics/cgfloat/1845210-leastnonzeromagnitude)Added [CGFloat.leastNormalMagnitude](https://developer.apple.com/documentation/coregraphics/cgfloat/1845209-leastnormalmagnitude)Added CGFloat.multiply(by: CGFloat)Added [CGFloat.nan](https://developer.apple.com/documentation/coregraphics/cgfloat/1645832-nan)Added [CGFloat.negate()](https://developer.apple.com/documentation/coregraphics/cgfloat/1845229-negate)Added [CGFloat.nextUp](https://developer.apple.com/documentation/coregraphics/cgfloat/1845224-nextup)Added [CGFloat.pi](https://developer.apple.com/documentation/coregraphics/cgfloat/1845230-pi)Added [CGFloat.round(_: FloatingPointRoundingRule)](https://developer.apple.com/documentation/coregraphics/cgfloat/2299989-round)Added [CGFloat.sign](https://developer.apple.com/documentation/coregraphics/cgfloat/1845206-sign)Added [CGFloat.signalingNaN](https://developer.apple.com/documentation/coregraphics/cgfloat/1845213-signalingnan)Added [CGFloat.significand](https://developer.apple.com/documentation/coregraphics/cgfloat/1845232-significand)Added [CGFloat.significandBitCount](https://developer.apple.com/documentation/coregraphics/cgfloat/1845227-significandbitcount)Added [CGFloat.significandBitPattern](https://developer.apple.com/documentation/coregraphics/cgfloat/1845214-significandbitpattern)Added [CGFloat.significandWidth](https://developer.apple.com/documentation/coregraphics/cgfloat/1845225-significandwidth)Added CGFloat.subtract(_: CGFloat)Added [CGFloat.ulp](https://developer.apple.com/documentation/coregraphics/cgfloat/1845236-ulp)Added [CGFunctionCallbacks.init(version: UInt32, evaluate: CoreGraphics.CGFunctionEvaluateCallback?, releaseInfo: CoreGraphics.CGFunctionReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1454863-init)Added [CGImage.copy(maskingColorComponents: [CGFloat]) -> CGImage?](https://developer.apple.com/documentation/coregraphics/cgimage/1454358-copy)Added [CGImageByteOrderInfo [enum]](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo)Added [CGImageByteOrderInfo.order16Big](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/order16big)Added [CGImageByteOrderInfo.order16Little](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteorder16little)Added [CGImageByteOrderInfo.order32Big](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/order32big)Added [CGImageByteOrderInfo.order32Little](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/order32little)Added [CGImageByteOrderInfo.orderMask](https://developer.apple.com/documentation/coregraphics/cgimagebyteorderinfo/kcgimagebyteordermask)Added [CGMutablePath.addArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, endAngle: CGFloat, clockwise: Bool, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427140-addarc)Added [CGMutablePath.addArc(tangent1End: CGPoint, tangent2End: CGPoint, radius: CGFloat, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427124-addarc)Added [CGMutablePath.addCurve(to: CGPoint, control1: CGPoint, control2: CGPoint, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427158-addcurve)Added [CGMutablePath.addEllipse(in: CGRect, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427120-addellipse)Added [CGMutablePath.addLine(to: CGPoint, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427121-addline)Added [CGMutablePath.addLines(between: [CGPoint], transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427154-addlines)Added [CGMutablePath.addPath(_: CGPath, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427150-addpath)Added [CGMutablePath.addQuadCurve(to: CGPoint, control: CGPoint, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427128-addquadcurve)Added [CGMutablePath.addRect(_: CGRect, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427119-addrect)Added [CGMutablePath.addRects(_: [CGRect], transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427131-addrects)Added [CGMutablePath.addRelativeArc(center: CGPoint, radius: CGFloat, startAngle: CGFloat, delta: CGFloat, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427147-addrelativearc)Added [CGMutablePath.addRoundedRect(in: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427144-addroundedrect)Added [CGMutablePath.move(to: CGPoint, transform: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgmutablepath/2427143-move)Added [CGPath.contains(_: CGPoint, using: CGPathFillRule, transform: CGAffineTransform) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpath/2427117-contains)Added [CGPath.copy(dashingWithPhase: CGFloat, lengths: [CGFloat], transform: CGAffineTransform) -> CGPath](https://developer.apple.com/documentation/coregraphics/cgpath/2427137-copy)Added [CGPath.copy(strokingWithWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat, transform: CGAffineTransform) -> CGPath](https://developer.apple.com/documentation/coregraphics/cgpath/2427133-copy)Added [CGPathFillRule [enum]](https://developer.apple.com/documentation/coregraphics/cgpathfillrule)Added [CGPathFillRule.evenOdd](https://developer.apple.com/documentation/coregraphics/cgpathfillrule/evenodd)Added [CGPathFillRule.winding](https://developer.apple.com/documentation/coregraphics/cgpathfillrule/winding)Added [CGPatternCallbacks.init(version: UInt32, drawPattern: CoreGraphics.CGPatternDrawPatternCallback?, releaseInfo: CoreGraphics.CGPatternReleaseInfoCallback?)](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/1778247-init)Added [CGPoint.customMirror](https://developer.apple.com/documentation/coregraphics/cgpoint/1645834-custommirror)Added [CGPoint.customPlaygroundQuickLook](https://developer.apple.com/documentation/coregraphics/cgpoint/1645835-customplaygroundquicklook)Added [CGPoint.debugDescription](https://developer.apple.com/documentation/coregraphics/cgpoint/1645825-debugdescription)Added [CGPoint.init(dictionaryRepresentation: CFDictionary)](https://developer.apple.com/documentation/coregraphics/cgpoint/2427118-init)Added [CGRect.customMirror](https://developer.apple.com/documentation/coregraphics/cgrect/1645833-custommirror)Added [CGRect.customPlaygroundQuickLook](https://developer.apple.com/documentation/coregraphics/cgrect/1645827-customplaygroundquicklook)Added [CGRect.debugDescription](https://developer.apple.com/documentation/coregraphics/cgrect/1645823-debugdescription)Added [CGRect.divided(atDistance: CGFloat, from: CGRectEdge) -> (slice: CGRect, remainder: CGRect)](https://developer.apple.com/documentation/coregraphics/cgrect/2299988-divided)Added [CGRect.init(dictionaryRepresentation: CFDictionary)](https://developer.apple.com/documentation/coregraphics/cgrect/2427139-init)Added [CGSize.customMirror](https://developer.apple.com/documentation/coregraphics/cgsize/1645828-custommirror)Added [CGSize.customPlaygroundQuickLook](https://developer.apple.com/documentation/coregraphics/cgsize/1645830-customplaygroundquicklook)Added [CGSize.debugDescription](https://developer.apple.com/documentation/coregraphics/cgsize/1645822-debugdescription)Added [CGSize.init(dictionaryRepresentation: CFDictionary)](https://developer.apple.com/documentation/coregraphics/cgsize/2427155-init)Added [IOSurfaceRef](https://developer.apple.com/documentation/iosurface/iosurfaceref)Added ==(_: CGPath, _: CGPath) -> BoolAdded ==(_: CGAffineTransform, _: CGAffineTransform) -> BoolAdded ==(_: CGColor, _: CGColor) -> BoolAdded [CGFloat.Exponent](https://developer.apple.com/documentation/coregraphics/cgfloat/exponent)Added [CGFloat.RawSignificand](https://developer.apple.com/documentation/coregraphics/cgfloat/rawsignificand)Modified [CGAffineTransform [struct]](https://developer.apple.com/documentation/coregraphics/cgaffinetransform)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat     init()     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat) } ``` | -- |
| To | ``` struct CGAffineTransform {     var a: CGFloat     var b: CGFloat     var c: CGFloat     var d: CGFloat     var tx: CGFloat     var ty: CGFloat     init()     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat)     static let identity: CGAffineTransform     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat)      init(translationX tx: CGFloat, y ty: CGFloat)      init(scaleX sx: CGFloat, y sy: CGFloat)      init(rotationAngle angle: CGFloat)     var isIdentity: Bool { get }     func translatedBy(x tx: CGFloat, y ty: CGFloat) -> CGAffineTransform     func scaledBy(x sx: CGFloat, y sy: CGFloat) -> CGAffineTransform     func rotated(by angle: CGFloat) -> CGAffineTransform     func inverted() -> CGAffineTransform     func concatenating(_ t2: CGAffineTransform) -> CGAffineTransform     func __equalTo(_ t2: CGAffineTransform) -> Bool     static var identity: CGAffineTransform { get } } extension CGAffineTransform {     static let identity: CGAffineTransform     init(a a: CGFloat, b b: CGFloat, c c: CGFloat, d d: CGFloat, tx tx: CGFloat, ty ty: CGFloat)      init(translationX tx: CGFloat, y ty: CGFloat)      init(scaleX sx: CGFloat, y sy: CGFloat)      init(rotationAngle angle: CGFloat)     var isIdentity: Bool { get }     func translatedBy(x tx: CGFloat, y ty: CGFloat) -> CGAffineTransform     func scaledBy(x sx: CGFloat, y sy: CGFloat) -> CGAffineTransform     func rotated(by angle: CGFloat) -> CGAffineTransform     func inverted() -> CGAffineTransform     func concatenating(_ t2: CGAffineTransform) -> CGAffineTransform     func __equalTo(_ t2: CGAffineTransform) -> Bool } extension CGAffineTransform {     static var identity: CGAffineTransform { get } } extension CGAffineTransform : Equatable { } ``` | Equatable |

Modified [CGAffineTransform.concatenating(_: CGAffineTransform) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1455996-concatenating)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformConcat(_:_:) | ``` func CGAffineTransformConcat(_ t1: CGAffineTransform, _ t2: CGAffineTransform) -> CGAffineTransform ``` |
| To | concatenating(_:) | ``` func concatenating(_ t2: CGAffineTransform) -> CGAffineTransform ``` |

Modified [CGAffineTransform.init(rotationAngle: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455666-cgaffinetransformmakerotation)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformMakeRotation(_:) | ``` func CGAffineTransformMakeRotation(_ angle: CGFloat) -> CGAffineTransform ``` |
| To | init(rotationAngle:) | ``` init(rotationAngle angle: CGFloat) ``` |

Modified [CGAffineTransform.init(scaleX: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1455016-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformMakeScale(_:_:) | ``` func CGAffineTransformMakeScale(_ sx: CGFloat, _ sy: CGFloat) -> CGAffineTransform ``` |
| To | init(scaleX:y:) | ``` init(scaleX sx: CGFloat, y sy: CGFloat) ``` |

Modified [CGAffineTransform.init(translationX: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1454909-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformMakeTranslation(_:_:) | ``` func CGAffineTransformMakeTranslation(_ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform ``` |
| To | init(translationX:y:) | ``` init(translationX tx: CGFloat, y ty: CGFloat) ``` |

Modified [CGAffineTransform.inverted() -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1455264-inverted)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformInvert(_:) | ``` func CGAffineTransformInvert(_ t: CGAffineTransform) -> CGAffineTransform ``` |
| To | inverted() | ``` func inverted() -> CGAffineTransform ``` |

Modified [CGAffineTransform.CGAffineTransformIsIdentity(_: CGAffineTransform) -> Bool](https://developer.apple.com/documentation/coregraphics/1455754-cgaffinetransformisidentity)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGAffineTransformIsIdentity(_:) | ``` func CGAffineTransformIsIdentity(_ t: CGAffineTransform) -> Bool ``` | tvOS 9.0 | -- |
| To | isIdentity | ``` var isIdentity: Bool { get } ``` | tvOS 10.0 | yes |

Modified [CGAffineTransform.rotated(by: CGFloat) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1455962-cgaffinetransformrotate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformRotate(_:_:) | ``` func CGAffineTransformRotate(_ t: CGAffineTransform, _ angle: CGFloat) -> CGAffineTransform ``` |
| To | rotated(by:) | ``` func rotated(by angle: CGFloat) -> CGAffineTransform ``` |

Modified [CGAffineTransform.scaledBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1455882-cgaffinetransformscale)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformScale(_:_:_:) | ``` func CGAffineTransformScale(_ t: CGAffineTransform, _ sx: CGFloat, _ sy: CGFloat) -> CGAffineTransform ``` |
| To | scaledBy(x:y:) | ``` func scaledBy(x sx: CGFloat, y sy: CGFloat) -> CGAffineTransform ``` |

Modified [CGAffineTransform.translatedBy(x: CGFloat, y: CGFloat) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform/1455822-translatedby)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGAffineTransformTranslate(_:_:_:) | ``` func CGAffineTransformTranslate(_ t: CGAffineTransform, _ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform ``` |
| To | translatedBy(x:y:) | ``` func translatedBy(x tx: CGFloat, y ty: CGFloat) -> CGAffineTransform ``` |

Modified [CGBitmapInfo [struct]](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGBitmapInfo : OptionSetType {     init(rawValue rawValue: UInt32)     static var AlphaInfoMask: CGBitmapInfo { get }     static var FloatInfoMask: CGBitmapInfo { get }     static var FloatComponents: CGBitmapInfo { get }     static var ByteOrderMask: CGBitmapInfo { get }     static var ByteOrderDefault: CGBitmapInfo { get }     static var ByteOrder16Little: CGBitmapInfo { get }     static var ByteOrder32Little: CGBitmapInfo { get }     static var ByteOrder16Big: CGBitmapInfo { get }     static var ByteOrder32Big: CGBitmapInfo { get } } ``` | OptionSetType |
| To | ``` struct CGBitmapInfo : OptionSet {     init(rawValue rawValue: UInt32)     static var alphaInfoMask: CGBitmapInfo { get }     static var floatInfoMask: CGBitmapInfo { get }     static var floatComponents: CGBitmapInfo { get }     static var byteOrderMask: CGBitmapInfo { get }     static var byteOrderDefault: CGBitmapInfo { get }     static var byteOrder16Little: CGBitmapInfo { get }     static var byteOrder32Little: CGBitmapInfo { get }     static var byteOrder16Big: CGBitmapInfo { get }     static var byteOrder32Big: CGBitmapInfo { get }     func intersect(_ other: CGBitmapInfo) -> CGBitmapInfo     func exclusiveOr(_ other: CGBitmapInfo) -> CGBitmapInfo     mutating func unionInPlace(_ other: CGBitmapInfo)     mutating func intersectInPlace(_ other: CGBitmapInfo)     mutating func exclusiveOrInPlace(_ other: CGBitmapInfo)     func isSubsetOf(_ other: CGBitmapInfo) -> Bool     func isDisjointWith(_ other: CGBitmapInfo) -> Bool     func isSupersetOf(_ other: CGBitmapInfo) -> Bool     mutating func subtractInPlace(_ other: CGBitmapInfo)     func isStrictSupersetOf(_ other: CGBitmapInfo) -> Bool     func isStrictSubsetOf(_ other: CGBitmapInfo) -> Bool } extension CGBitmapInfo {     func union(_ other: CGBitmapInfo) -> CGBitmapInfo     func intersection(_ other: CGBitmapInfo) -> CGBitmapInfo     func symmetricDifference(_ other: CGBitmapInfo) -> CGBitmapInfo } extension CGBitmapInfo {     func contains(_ member: CGBitmapInfo) -> Bool     mutating func insert(_ newMember: CGBitmapInfo) -> (inserted: Bool, memberAfterInsert: CGBitmapInfo)     mutating func remove(_ member: CGBitmapInfo) -> CGBitmapInfo?     mutating func update(with newMember: CGBitmapInfo) -> CGBitmapInfo? } extension CGBitmapInfo {     convenience init()     mutating func formUnion(_ other: CGBitmapInfo)     mutating func formIntersection(_ other: CGBitmapInfo)     mutating func formSymmetricDifference(_ other: CGBitmapInfo) } extension CGBitmapInfo {     convenience init<S : Sequence where S.Iterator.Element == CGBitmapInfo>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CGBitmapInfo...)     mutating func subtract(_ other: CGBitmapInfo)     func isSubset(of other: CGBitmapInfo) -> Bool     func isSuperset(of other: CGBitmapInfo) -> Bool     func isDisjoint(with other: CGBitmapInfo) -> Bool     func subtracting(_ other: CGBitmapInfo) -> CGBitmapInfo     var isEmpty: Bool { get }     func isStrictSuperset(of other: CGBitmapInfo) -> Bool     func isStrictSubset(of other: CGBitmapInfo) -> Bool } ``` | OptionSet |

Modified [CGBitmapInfo.alphaInfoMask](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/1454277-alphainfomask)

|  | Declaration |
| --- | --- |
| From | ``` static var AlphaInfoMask: CGBitmapInfo { get } ``` |
| To | ``` static var alphaInfoMask: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.byteOrder16Big](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapbyteorder16big)

|  | Declaration |
| --- | --- |
| From | ``` static var ByteOrder16Big: CGBitmapInfo { get } ``` |
| To | ``` static var byteOrder16Big: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.byteOrder16Little](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapbyteorder16little)

|  | Declaration |
| --- | --- |
| From | ``` static var ByteOrder16Little: CGBitmapInfo { get } ``` |
| To | ``` static var byteOrder16Little: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.byteOrder32Big](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/1456467-byteorder32big)

|  | Declaration |
| --- | --- |
| From | ``` static var ByteOrder32Big: CGBitmapInfo { get } ``` |
| To | ``` static var byteOrder32Big: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.byteOrder32Little](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapbyteorder32little)

|  | Declaration |
| --- | --- |
| From | ``` static var ByteOrder32Little: CGBitmapInfo { get } ``` |
| To | ``` static var byteOrder32Little: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.byteOrderMask](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/1456552-byteordermask)

|  | Declaration |
| --- | --- |
| From | ``` static var ByteOrderMask: CGBitmapInfo { get } ``` |
| To | ``` static var byteOrderMask: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.floatComponents](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapfloatcomponents)

|  | Declaration |
| --- | --- |
| From | ``` static var FloatComponents: CGBitmapInfo { get } ``` |
| To | ``` static var floatComponents: CGBitmapInfo { get } ``` |

Modified [CGBitmapInfo.floatInfoMask](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo/kcgbitmapfloatinfomask)

|  | Declaration |
| --- | --- |
| From | ``` static var FloatInfoMask: CGBitmapInfo { get } ``` |
| To | ``` static var floatInfoMask: CGBitmapInfo { get } ``` |

Modified [CGBlendMode [enum]](https://developer.apple.com/documentation/coregraphics/cgblendmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CGBlendMode : Int32 {     case Normal     case Multiply     case Screen     case Overlay     case Darken     case Lighten     case ColorDodge     case ColorBurn     case SoftLight     case HardLight     case Difference     case Exclusion     case Hue     case Saturation     case Color     case Luminosity     case Clear     case Copy     case SourceIn     case SourceOut     case SourceAtop     case DestinationOver     case DestinationIn     case DestinationOut     case DestinationAtop     case XOR     case PlusDarker     case PlusLighter } ``` |
| To | ``` enum CGBlendMode : Int32 {     case normal     case multiply     case screen     case overlay     case darken     case lighten     case colorDodge     case colorBurn     case softLight     case hardLight     case difference     case exclusion     case hue     case saturation     case color     case luminosity     case clear     case copy     case sourceIn     case sourceOut     case sourceAtop     case destinationOver     case destinationIn     case destinationOut     case destinationAtop     case xor     case plusDarker     case plusLighter } ``` |

Modified [CGBlendMode.clear](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeclear)

|  | Declaration |
| --- | --- |
| From | ``` case Clear ``` |
| To | ``` case clear ``` |

Modified [CGBlendMode.color](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodecolor)

|  | Declaration |
| --- | --- |
| From | ``` case Color ``` |
| To | ``` case color ``` |

Modified [CGBlendMode.colorBurn](https://developer.apple.com/documentation/coregraphics/cgblendmode/colorburn)

|  | Declaration |
| --- | --- |
| From | ``` case ColorBurn ``` |
| To | ``` case colorBurn ``` |

Modified [CGBlendMode.colorDodge](https://developer.apple.com/documentation/coregraphics/cgblendmode/colordodge)

|  | Declaration |
| --- | --- |
| From | ``` case ColorDodge ``` |
| To | ``` case colorDodge ``` |

Modified [CGBlendMode.copy](https://developer.apple.com/documentation/coregraphics/cgblendmode/copy)

|  | Declaration |
| --- | --- |
| From | ``` case Copy ``` |
| To | ``` case copy ``` |

Modified [CGBlendMode.darken](https://developer.apple.com/documentation/coregraphics/cgblendmode/darken)

|  | Declaration |
| --- | --- |
| From | ``` case Darken ``` |
| To | ``` case darken ``` |

Modified [CGBlendMode.destinationAtop](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationatop)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationAtop ``` |
| To | ``` case destinationAtop ``` |

Modified [CGBlendMode.destinationIn](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodedestinationin)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationIn ``` |
| To | ``` case destinationIn ``` |

Modified [CGBlendMode.destinationOut](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationout)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationOut ``` |
| To | ``` case destinationOut ``` |

Modified [CGBlendMode.destinationOver](https://developer.apple.com/documentation/coregraphics/cgblendmode/destinationover)

|  | Declaration |
| --- | --- |
| From | ``` case DestinationOver ``` |
| To | ``` case destinationOver ``` |

Modified [CGBlendMode.difference](https://developer.apple.com/documentation/coregraphics/cgblendmode/difference)

|  | Declaration |
| --- | --- |
| From | ``` case Difference ``` |
| To | ``` case difference ``` |

Modified [CGBlendMode.exclusion](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeexclusion)

|  | Declaration |
| --- | --- |
| From | ``` case Exclusion ``` |
| To | ``` case exclusion ``` |

Modified [CGBlendMode.hardLight](https://developer.apple.com/documentation/coregraphics/cgblendmode/hardlight)

|  | Declaration |
| --- | --- |
| From | ``` case HardLight ``` |
| To | ``` case hardLight ``` |

Modified [CGBlendMode.hue](https://developer.apple.com/documentation/coregraphics/cgblendmode/hue)

|  | Declaration |
| --- | --- |
| From | ``` case Hue ``` |
| To | ``` case hue ``` |

Modified [CGBlendMode.lighten](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodelighten)

|  | Declaration |
| --- | --- |
| From | ``` case Lighten ``` |
| To | ``` case lighten ``` |

Modified [CGBlendMode.luminosity](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeluminosity)

|  | Declaration |
| --- | --- |
| From | ``` case Luminosity ``` |
| To | ``` case luminosity ``` |

Modified [CGBlendMode.multiply](https://developer.apple.com/documentation/coregraphics/cgblendmode/multiply)

|  | Declaration |
| --- | --- |
| From | ``` case Multiply ``` |
| To | ``` case multiply ``` |

Modified [CGBlendMode.normal](https://developer.apple.com/documentation/coregraphics/cgblendmode/normal)

|  | Declaration |
| --- | --- |
| From | ``` case Normal ``` |
| To | ``` case normal ``` |

Modified [CGBlendMode.overlay](https://developer.apple.com/documentation/coregraphics/cgblendmode/overlay)

|  | Declaration |
| --- | --- |
| From | ``` case Overlay ``` |
| To | ``` case overlay ``` |

Modified [CGBlendMode.plusDarker](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodeplusdarker)

|  | Declaration |
| --- | --- |
| From | ``` case PlusDarker ``` |
| To | ``` case plusDarker ``` |

Modified [CGBlendMode.plusLighter](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodepluslighter)

|  | Declaration |
| --- | --- |
| From | ``` case PlusLighter ``` |
| To | ``` case plusLighter ``` |

Modified [CGBlendMode.saturation](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodesaturation)

|  | Declaration |
| --- | --- |
| From | ``` case Saturation ``` |
| To | ``` case saturation ``` |

Modified [CGBlendMode.screen](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodescreen)

|  | Declaration |
| --- | --- |
| From | ``` case Screen ``` |
| To | ``` case screen ``` |

Modified [CGBlendMode.softLight](https://developer.apple.com/documentation/coregraphics/cgblendmode/softlight)

|  | Declaration |
| --- | --- |
| From | ``` case SoftLight ``` |
| To | ``` case softLight ``` |

Modified [CGBlendMode.sourceAtop](https://developer.apple.com/documentation/coregraphics/cgblendmode/sourceatop)

|  | Declaration |
| --- | --- |
| From | ``` case SourceAtop ``` |
| To | ``` case sourceAtop ``` |

Modified [CGBlendMode.sourceIn](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodesourcein)

|  | Declaration |
| --- | --- |
| From | ``` case SourceIn ``` |
| To | ``` case sourceIn ``` |

Modified [CGBlendMode.sourceOut](https://developer.apple.com/documentation/coregraphics/cgblendmode/sourceout)

|  | Declaration |
| --- | --- |
| From | ``` case SourceOut ``` |
| To | ``` case sourceOut ``` |

Modified [CGBlendMode.xor](https://developer.apple.com/documentation/coregraphics/cgblendmode/kcgblendmodexor)

|  | Declaration |
| --- | --- |
| From | ``` case XOR ``` |
| To | ``` case xor ``` |

Modified [CGColor](https://developer.apple.com/documentation/coregraphics/cgcolor)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CGColor { } ``` | -- |
| To | ``` class CGColor {     var components: [CGFloat]? { get }      init?(colorSpace space: CGColorSpace, components components: UnsafePointer<CGFloat>)      init(gray gray: CGFloat, alpha alpha: CGFloat)      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(genericCMYKCyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     class func __constantColor(for colorName: CFString) -> CGColor?      init?(patternSpace space: CGColorSpace, pattern pattern: CGPattern, components components: UnsafePointer<CGFloat>)     func copy() -> CGColor?     func copy(alpha alpha: CGFloat) -> CGColor?     func converted(to _: CGColorSpace, intent intent: CGColorRenderingIntent, options options: CFDictionary?) -> CGColor?     func __equalTo(_ color2: CGColor) -> Bool     var numberOfComponents: Int { get }     var __unsafeComponents: UnsafePointer<CGFloat>? { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace? { get }     var pattern: CGPattern? { get }     class var typeID: CFTypeID { get }     class let __whiteColorName: CFString     class let __blackColorName: CFString     class let __clearColorName: CFString     class let conversionBlackPointCompensation: CFString } extension CGColor {      init?(colorSpace space: CGColorSpace, components components: UnsafePointer<CGFloat>)      init(gray gray: CGFloat, alpha alpha: CGFloat)      init(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     init(genericCMYKCyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     class func __constantColor(for colorName: CFString) -> CGColor?      init?(patternSpace space: CGColorSpace, pattern pattern: CGPattern, components components: UnsafePointer<CGFloat>)     func copy() -> CGColor?     func copy(alpha alpha: CGFloat) -> CGColor?     func converted(to _: CGColorSpace, intent intent: CGColorRenderingIntent, options options: CFDictionary?) -> CGColor?     func __equalTo(_ color2: CGColor) -> Bool     var numberOfComponents: Int { get }     var __unsafeComponents: UnsafePointer<CGFloat>? { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace? { get }     var pattern: CGPattern? { get }     class var typeID: CFTypeID { get }     class let __whiteColorName: CFString     class let __blackColorName: CFString     class let __clearColorName: CFString } extension CGColor {     class let conversionBlackPointCompensation: CFString } extension CGColor : Equatable { } extension CGColor {     var components: [CGFloat]? { get } } ``` | Equatable |

Modified [CGColor.CGColorGetAlpha(_: CGColor?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456637-cgcolorgetalpha)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorGetAlpha(_:) | ``` func CGColorGetAlpha(_ color: CGColor?) -> CGFloat ``` | -- |
| To | alpha | ``` var alpha: CGFloat { get } ``` | yes |

Modified [CGColor.CGColorGetColorSpace(_: CGColor?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1455744-cgcolorgetcolorspace)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorGetColorSpace(_:) | ``` func CGColorGetColorSpace(_ color: CGColor?) -> CGColorSpace? ``` | -- |
| To | colorSpace | ``` var colorSpace: CGColorSpace? { get } ``` | yes |

Modified [CGColor.converted(to: CGColorSpace, intent: CGColorRenderingIntent, options: CFDictionary?) -> CGColor?](https://developer.apple.com/documentation/coregraphics/1455493-cgcolorcreatecopybymatchingtocol)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorCreateCopyByMatchingToColorSpace(_:_:_:_:) | ``` func CGColorCreateCopyByMatchingToColorSpace(_ _: CGColorSpace?, _ intent: CGColorRenderingIntent, _ color: CGColor?, _ options: CFDictionary?) -> CGColor? ``` |
| To | converted(to:intent:options:) | ``` func converted(to _: CGColorSpace, intent intent: CGColorRenderingIntent, options options: CFDictionary?) -> CGColor? ``` |

Modified [CGColor.copy() -> CGColor?](https://developer.apple.com/documentation/coregraphics/cgcolor/1456134-copy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGColorCreateCopy(_:) | ``` func CGColorCreateCopy(_ color: CGColor?) -> CGColor? ``` | tvOS 9.0 |
| To | copy() | ``` func copy() -> CGColor? ``` | tvOS 10.0 |

Modified [CGColor.copy(alpha: CGFloat) -> CGColor?](https://developer.apple.com/documentation/coregraphics/cgcolor/1455986-copy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGColorCreateCopyWithAlpha(_:_:) | ``` func CGColorCreateCopyWithAlpha(_ color: CGColor?, _ alpha: CGFloat) -> CGColor? ``` | tvOS 9.0 |
| To | copy(alpha:) | ``` func copy(alpha alpha: CGFloat) -> CGColor? ``` | tvOS 10.0 |

Modified [CGColor.init(colorSpace: CGColorSpace, components: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/1455927-cgcolorcreate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorCreate(_:_:) | ``` func CGColorCreate(_ space: CGColorSpace?, _ components: UnsafePointer<CGFloat>) -> CGColor? ``` |
| To | init(colorSpace:components:) | ``` init?(colorSpace space: CGColorSpace, components components: UnsafePointer<CGFloat>) ``` |

Modified [CGColor.init(patternSpace: CGColorSpace, pattern: CGPattern, components: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcolor/1455687-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorCreateWithPattern(_:_:_:) | ``` func CGColorCreateWithPattern(_ space: CGColorSpace?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) -> CGColor? ``` |
| To | init(patternSpace:pattern:components:) | ``` init?(patternSpace space: CGColorSpace, pattern pattern: CGPattern, components components: UnsafePointer<CGFloat>) ``` |

Modified [CGColor.CGColorGetNumberOfComponents(_: CGColor?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcolor/1454130-numberofcomponents)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorGetNumberOfComponents(_:) | ``` func CGColorGetNumberOfComponents(_ color: CGColor?) -> Int ``` | -- |
| To | numberOfComponents | ``` var numberOfComponents: Int { get } ``` | yes |

Modified [CGColor.CGColorGetPattern(_: CGColor?) -> CGPattern?](https://developer.apple.com/documentation/coregraphics/1455937-cgcolorgetpattern)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorGetPattern(_:) | ``` func CGColorGetPattern(_ color: CGColor?) -> CGPattern? ``` | -- |
| To | pattern | ``` var pattern: CGPattern? { get } ``` | yes |

Modified [CGColor.CGColorGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgcolor/1455568-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorGetTypeID() | ``` func CGColorGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGColorRenderingIntent [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent)

|  | Declaration |
| --- | --- |
| From | ``` enum CGColorRenderingIntent : Int32 {     case RenderingIntentDefault     case RenderingIntentAbsoluteColorimetric     case RenderingIntentRelativeColorimetric     case RenderingIntentPerceptual     case RenderingIntentSaturation } ``` |
| To | ``` enum CGColorRenderingIntent : Int32 {     case defaultIntent     case absoluteColorimetric     case relativeColorimetric     case perceptual     case saturation } ``` |

Modified [CGColorRenderingIntent.absoluteColorimetric](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/absolutecolorimetric)

|  | Declaration |
| --- | --- |
| From | ``` case RenderingIntentAbsoluteColorimetric ``` |
| To | ``` case absoluteColorimetric ``` |

Modified [CGColorRenderingIntent.defaultIntent](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/defaultintent)

|  | Declaration |
| --- | --- |
| From | ``` case RenderingIntentDefault ``` |
| To | ``` case defaultIntent ``` |

Modified [CGColorRenderingIntent.perceptual](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/kcgrenderingintentperceptual)

|  | Declaration |
| --- | --- |
| From | ``` case RenderingIntentPerceptual ``` |
| To | ``` case perceptual ``` |

Modified [CGColorRenderingIntent.relativeColorimetric](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/relativecolorimetric)

|  | Declaration |
| --- | --- |
| From | ``` case RenderingIntentRelativeColorimetric ``` |
| To | ``` case relativeColorimetric ``` |

Modified [CGColorRenderingIntent.saturation](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent/kcgrenderingintentsaturation)

|  | Declaration |
| --- | --- |
| From | ``` case RenderingIntentSaturation ``` |
| To | ``` case saturation ``` |

Modified [CGColorSpace](https://developer.apple.com/documentation/coregraphics/cgcolorspace)

|  | Declaration |
| --- | --- |
| From | ``` class CGColorSpace { } ``` |
| To | ``` class CGColorSpace {     var colorTable: [UInt8]? { get }     class let genericGray: CFString     class let genericRGB: CFString     class let genericCMYK: CFString     class let displayP3: CFString     class let genericRGBLinear: CFString     class let adobeRGB1998: CFString     class let sRGB: CFString     class let genericGrayGamma2_2: CFString     class let genericXYZ: CFString     class let acescgLinear: CFString     class let itur_709: CFString     class let itur_2020: CFString     class let rommrgb: CFString     class let dcip3: CFString     class let extendedSRGB: CFString     class let linearSRGB: CFString     class let extendedLinearSRGB: CFString     class let extendedGray: CFString     class let linearGray: CFString     class let extendedLinearGray: CFString     init?(calibratedGrayWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: CGFloat)     init?(calibratedRGBWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: UnsafePointer<CGFloat>!, matrix matrix: UnsafePointer<CGFloat>!)     init?(labWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, range range: UnsafePointer<CGFloat>!)      init?(iccProfileData data: CFData)     init?(iccBasedNComponents nComponents: Int, range range: UnsafePointer<CGFloat>?, profile profile: CGDataProvider, alternate alternate: CGColorSpace?)     init?(indexedBaseSpace baseSpace: CGColorSpace, last lastIndex: Int, colorTable colorTable: UnsafePointer<UInt8>)     init?(patternBaseSpace baseSpace: CGColorSpace?)      init?(platformColorSpaceRef ref: UnsafeRawPointer)      init?(name name: CFString)     var name: CFString? { get }     class var typeID: CFTypeID { get }     var numberOfComponents: Int { get }     var model: CGColorSpaceModel { get }     var baseColorSpace: CGColorSpace? { get }     var __colorTableCount: Int { get }     func __unsafeGetColorTable(_ table: UnsafeMutablePointer<UInt8>)     var iccData: CFData? { get }     func copyICCData() -> CFData?     var isWideGamutRGB: Bool { get }     var supportsOutput: Bool { get } } extension CGColorSpace {     class let genericGray: CFString     class let genericRGB: CFString     class let genericCMYK: CFString     class let displayP3: CFString     class let genericRGBLinear: CFString     class let adobeRGB1998: CFString     class let sRGB: CFString     class let genericGrayGamma2_2: CFString     class let genericXYZ: CFString     class let acescgLinear: CFString     class let itur_709: CFString     class let itur_2020: CFString     class let rommrgb: CFString     class let dcip3: CFString     class let extendedSRGB: CFString     class let linearSRGB: CFString     class let extendedLinearSRGB: CFString     class let extendedGray: CFString     class let linearGray: CFString     class let extendedLinearGray: CFString     init?(calibratedGrayWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: CGFloat)     init?(calibratedRGBWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: UnsafePointer<CGFloat>!, matrix matrix: UnsafePointer<CGFloat>!)     init?(labWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, range range: UnsafePointer<CGFloat>!)      init?(iccProfileData data: CFData)     init?(iccBasedNComponents nComponents: Int, range range: UnsafePointer<CGFloat>?, profile profile: CGDataProvider, alternate alternate: CGColorSpace?)     init?(indexedBaseSpace baseSpace: CGColorSpace, last lastIndex: Int, colorTable colorTable: UnsafePointer<UInt8>)     init?(patternBaseSpace baseSpace: CGColorSpace?)      init?(platformColorSpaceRef ref: UnsafeRawPointer)      init?(name name: CFString)     var name: CFString? { get }     class var typeID: CFTypeID { get }     var numberOfComponents: Int { get }     var model: CGColorSpaceModel { get }     var baseColorSpace: CGColorSpace? { get }     var __colorTableCount: Int { get }     func __unsafeGetColorTable(_ table: UnsafeMutablePointer<UInt8>)     var iccData: CFData? { get }     func copyICCData() -> CFData?     var isWideGamutRGB: Bool { get }     var supportsOutput: Bool { get } } extension CGColorSpace {     var colorTable: [UInt8]? { get } } ``` |

Modified [CGColorSpace.acescgLinear](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408841-acescglinear)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceACESCGLinear | ``` let kCGColorSpaceACESCGLinear: CFString ``` |
| To | acescgLinear | ``` class let acescgLinear: CFString ``` |

Modified [CGColorSpace.adobeRGB1998](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceadobergb1998)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceAdobeRGB1998 | ``` let kCGColorSpaceAdobeRGB1998: CFString ``` |
| To | adobeRGB1998 | ``` class let adobeRGB1998: CFString ``` |

Modified [CGColorSpace.CGColorSpaceGetBaseColorSpace(_: CGColorSpace?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408839-basecolorspace)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorSpaceGetBaseColorSpace(_:) | ``` func CGColorSpaceGetBaseColorSpace(_ space: CGColorSpace?) -> CGColorSpace? ``` | -- |
| To | baseColorSpace | ``` var baseColorSpace: CGColorSpace? { get } ``` | yes |

Modified [CGColorSpace.dcip3](https://developer.apple.com/documentation/coregraphics/kcgcolorspacedcip3)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceDCIP3 | ``` let kCGColorSpaceDCIP3: CFString ``` |
| To | dcip3 | ``` class let dcip3: CFString ``` |

Modified [CGColorSpace.displayP3](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408916-displayp3)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceDisplayP3 | ``` let kCGColorSpaceDisplayP3: CFString ``` |
| To | displayP3 | ``` class let displayP3: CFString ``` |

Modified [CGColorSpace.genericCMYK](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericcmyk)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceGenericCMYK | ``` let kCGColorSpaceGenericCMYK: CFString ``` |
| To | genericCMYK | ``` class let genericCMYK: CFString ``` |

Modified [CGColorSpace.genericGrayGamma2_2](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericgraygamma2_2)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceGenericGrayGamma2_2 | ``` let kCGColorSpaceGenericGrayGamma2_2: CFString ``` |
| To | genericGrayGamma2_2 | ``` class let genericGrayGamma2_2: CFString ``` |

Modified [CGColorSpace.genericRGBLinear](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericrgblinear)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceGenericRGBLinear | ``` let kCGColorSpaceGenericRGBLinear: CFString ``` |
| To | genericRGBLinear | ``` class let genericRGBLinear: CFString ``` |

Modified [CGColorSpace.genericXYZ](https://developer.apple.com/documentation/coregraphics/kcgcolorspacegenericxyz)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceGenericXYZ | ``` let kCGColorSpaceGenericXYZ: CFString ``` |
| To | genericXYZ | ``` class let genericXYZ: CFString ``` |

Modified [CGColorSpace.CGColorSpaceCopyICCProfile(_: CGColorSpace?) -> CFData?](https://developer.apple.com/documentation/coregraphics/1408889-cgcolorspacecopyiccprofile)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGColorSpaceCopyICCProfile(_:) | ``` func CGColorSpaceCopyICCProfile(_ space: CGColorSpace?) -> CFData? ``` | tvOS 9.0 | -- |
| To | iccData | ``` var iccData: CFData? { get } ``` | tvOS 10.0 | yes |

Modified [CGColorSpace.init(calibratedGrayWhitePoint: UnsafePointer<CGFloat>!, blackPoint: UnsafePointer<CGFloat>!, gamma: CGFloat)](https://developer.apple.com/documentation/coregraphics/1408887-cgcolorspacecreatecalibratedgray)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateCalibratedGray(_:_:_:) | ``` func CGColorSpaceCreateCalibratedGray(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: CGFloat) -> CGColorSpace? ``` |
| To | init(calibratedGrayWhitePoint:blackPoint:gamma:) | ``` init?(calibratedGrayWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: CGFloat) ``` |

Modified [CGColorSpace.init(calibratedRGBWhitePoint: UnsafePointer<CGFloat>!, blackPoint: UnsafePointer<CGFloat>!, gamma: UnsafePointer<CGFloat>!, matrix: UnsafePointer<CGFloat>!)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408861-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateCalibratedRGB(_:_:_:_:) | ``` func CGColorSpaceCreateCalibratedRGB(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ gamma: UnsafePointer<CGFloat>, _ matrix: UnsafePointer<CGFloat>) -> CGColorSpace? ``` |
| To | init(calibratedRGBWhitePoint:blackPoint:gamma:matrix:) | ``` init?(calibratedRGBWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, gamma gamma: UnsafePointer<CGFloat>!, matrix matrix: UnsafePointer<CGFloat>!) ``` |

Modified [CGColorSpace.init(iccBasedNComponents: Int, range: UnsafePointer<CGFloat>?, profile: CGDataProvider, alternate: CGColorSpace?)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408881-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateICCBased(_:_:_:_:) | ``` func CGColorSpaceCreateICCBased(_ nComponents: Int, _ range: UnsafePointer<CGFloat>, _ profile: CGDataProvider?, _ alternate: CGColorSpace?) -> CGColorSpace? ``` |
| To | init(iccBasedNComponents:range:profile:alternate:) | ``` init?(iccBasedNComponents nComponents: Int, range range: UnsafePointer<CGFloat>?, profile profile: CGDataProvider, alternate alternate: CGColorSpace?) ``` |

Modified [CGColorSpace.init(iccProfileData: CFData)](https://developer.apple.com/documentation/coregraphics/1408895-cgcolorspacecreatewithiccprofile)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateWithICCProfile(_:) | ``` func CGColorSpaceCreateWithICCProfile(_ data: CFData?) -> CGColorSpace? ``` |
| To | init(iccProfileData:) | ``` init?(iccProfileData data: CFData) ``` |

Modified [CGColorSpace.init(indexedBaseSpace: CGColorSpace, last: Int, colorTable: UnsafePointer<UInt8>)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408899-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateIndexed(_:_:_:) | ``` func CGColorSpaceCreateIndexed(_ baseSpace: CGColorSpace?, _ lastIndex: Int, _ colorTable: UnsafePointer<UInt8>) -> CGColorSpace? ``` |
| To | init(indexedBaseSpace:last:colorTable:) | ``` init?(indexedBaseSpace baseSpace: CGColorSpace, last lastIndex: Int, colorTable colorTable: UnsafePointer<UInt8>) ``` |

Modified [CGColorSpace.init(labWhitePoint: UnsafePointer<CGFloat>!, blackPoint: UnsafePointer<CGFloat>!, range: UnsafePointer<CGFloat>!)](https://developer.apple.com/documentation/coregraphics/1408879-cgcolorspacecreatelab)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateLab(_:_:_:) | ``` func CGColorSpaceCreateLab(_ whitePoint: UnsafePointer<CGFloat>, _ blackPoint: UnsafePointer<CGFloat>, _ range: UnsafePointer<CGFloat>) -> CGColorSpace? ``` |
| To | init(labWhitePoint:blackPoint:range:) | ``` init?(labWhitePoint whitePoint: UnsafePointer<CGFloat>!, blackPoint blackPoint: UnsafePointer<CGFloat>!, range range: UnsafePointer<CGFloat>!) ``` |

Modified [CGColorSpace.init(name: CFString)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408921-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateWithName(_:) | ``` func CGColorSpaceCreateWithName(_ name: CFString?) -> CGColorSpace? ``` |
| To | init(name:) | ``` init?(name name: CFString) ``` |

Modified [CGColorSpace.init(patternBaseSpace: CGColorSpace?)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408869-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreatePattern(_:) | ``` func CGColorSpaceCreatePattern(_ baseSpace: CGColorSpace?) -> CGColorSpace? ``` |
| To | init(patternBaseSpace:) | ``` init?(patternBaseSpace baseSpace: CGColorSpace?) ``` |

Modified [CGColorSpace.init(platformColorSpaceRef: UnsafeRawPointer)](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408850-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceCreateWithPlatformColorSpace(_:) | ``` func CGColorSpaceCreateWithPlatformColorSpace(_ ref: UnsafePointer<Void>) -> CGColorSpace? ``` |
| To | init(platformColorSpaceRef:) | ``` init?(platformColorSpaceRef ref: UnsafeRawPointer) ``` |

Modified [CGColorSpace.itur_2020](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceitur_2020)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceITUR_2020 | ``` let kCGColorSpaceITUR_2020: CFString ``` |
| To | itur_2020 | ``` class let itur_2020: CFString ``` |

Modified [CGColorSpace.itur_709](https://developer.apple.com/documentation/coregraphics/kcgcolorspaceitur_709)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceITUR_709 | ``` let kCGColorSpaceITUR_709: CFString ``` |
| To | itur_709 | ``` class let itur_709: CFString ``` |

Modified [CGColorSpace.CGColorSpaceGetModel(_: CGColorSpace?) -> CGColorSpaceModel](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408854-model)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorSpaceGetModel(_:) | ``` func CGColorSpaceGetModel(_ space: CGColorSpace?) -> CGColorSpaceModel ``` | -- |
| To | model | ``` var model: CGColorSpaceModel { get } ``` | yes |

Modified [CGColorSpace.CGColorSpaceGetNumberOfComponents(_: CGColorSpace?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408848-numberofcomponents)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGColorSpaceGetNumberOfComponents(_:) | ``` func CGColorSpaceGetNumberOfComponents(_ space: CGColorSpace?) -> Int ``` | -- |
| To | numberOfComponents | ``` var numberOfComponents: Int { get } ``` | yes |

Modified [CGColorSpace.rommrgb](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408912-rommrgb)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceROMMRGB | ``` let kCGColorSpaceROMMRGB: CFString ``` |
| To | rommrgb | ``` class let rommrgb: CFString ``` |

Modified [CGColorSpace.sRGB](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408871-srgb)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGColorSpaceSRGB | ``` let kCGColorSpaceSRGB: CFString ``` |
| To | sRGB | ``` class let sRGB: CFString ``` |

Modified [CGColorSpace.CGColorSpaceGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgcolorspace/1408926-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGColorSpaceGetTypeID() | ``` func CGColorSpaceGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGColorSpaceModel [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel)

|  | Declaration |
| --- | --- |
| From | ``` enum CGColorSpaceModel : Int32 {     case Unknown     case Monochrome     case RGB     case CMYK     case Lab     case DeviceN     case Indexed     case Pattern } ``` |
| To | ``` enum CGColorSpaceModel : Int32 {     case unknown     case monochrome     case rgb     case cmyk     case lab     case deviceN     case indexed     case pattern } ``` |

Modified [CGColorSpaceModel.cmyk](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/cmyk)

|  | Declaration |
| --- | --- |
| From | ``` case CMYK ``` |
| To | ``` case cmyk ``` |

Modified [CGColorSpaceModel.deviceN](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodeldevicen)

|  | Declaration |
| --- | --- |
| From | ``` case DeviceN ``` |
| To | ``` case deviceN ``` |

Modified [CGColorSpaceModel.indexed](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodelindexed)

|  | Declaration |
| --- | --- |
| From | ``` case Indexed ``` |
| To | ``` case indexed ``` |

Modified [CGColorSpaceModel.lab](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/lab)

|  | Declaration |
| --- | --- |
| From | ``` case Lab ``` |
| To | ``` case lab ``` |

Modified [CGColorSpaceModel.monochrome](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/monochrome)

|  | Declaration |
| --- | --- |
| From | ``` case Monochrome ``` |
| To | ``` case monochrome ``` |

Modified [CGColorSpaceModel.pattern](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/kcgcolorspacemodelpattern)

|  | Declaration |
| --- | --- |
| From | ``` case Pattern ``` |
| To | ``` case pattern ``` |

Modified [CGColorSpaceModel.rgb](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/rgb)

|  | Declaration |
| --- | --- |
| From | ``` case RGB ``` |
| To | ``` case rgb ``` |

Modified [CGColorSpaceModel.unknown](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel/unknown)

|  | Declaration |
| --- | --- |
| From | ``` case Unknown ``` |
| To | ``` case unknown ``` |

Modified [CGContext](https://developer.apple.com/documentation/coregraphics/cgcontextref)

|  | Declaration |
| --- | --- |
| From | ``` class CGContext { } ``` |
| To | ``` class CGContext {      init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32, releaseCallback releaseCallback: CoreGraphics.CGBitmapContextReleaseDataCallback?, releaseInfo releaseInfo: UnsafeMutableRawPointer?)      init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32)     var data: UnsafeMutableRawPointer? { get }     var width: Int { get }     var height: Int { get }     var bitsPerComponent: Int { get }     var bitsPerPixel: Int { get }     var bytesPerRow: Int { get }     var colorSpace: CGColorSpace? { get }     var alphaInfo: CGImageAlphaInfo { get }     var bitmapInfo: CGBitmapInfo { get }     func makeImage() -> CGImage?     func setLineDash(phase phase: CGFloat, lengths lengths: [CGFloat])     func move(to point: CGPoint)     func addLine(to point: CGPoint)     func addCurve(to end: CGPoint, control1 control1: CGPoint, control2 control2: CGPoint)     func addQuadCurve(to end: CGPoint, control control: CGPoint)     func addRects(_ rects: [CGRect])     func addLines(between points: [CGPoint])     func addArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func addArc(tangent1End tangent1End: CGPoint, tangent2End tangent2End: CGPoint, radius radius: CGFloat)     func fillPath(using rule: CGPathFillRule = default)     func clip(using rule: CGPathFillRule = default)     func fill(_ rects: [CGRect])     func strokeLineSegments(between points: [CGPoint])     func clip(to rects: [CGRect])     func draw(_ image: CGImage, in rect: CGRect, byTiling byTiling: Bool = default)     var textPosition: CGPoint     func showGlyphs(_ glyphs: [CGGlyph], at positions: [CGPoint])     func draw(_ layer: CGLayer, in rect: CGRect)     func draw(_ layer: CGLayer, at point: CGPoint)     class var typeID: CFTypeID { get }     func saveGState()     func restoreGState()     func scaleBy(x sx: CGFloat, y sy: CGFloat)     func translateBy(x tx: CGFloat, y ty: CGFloat)     func rotate(by angle: CGFloat)     func concatenate(_ transform: CGAffineTransform)     var ctm: CGAffineTransform { get }     func setLineWidth(_ width: CGFloat)     func setLineCap(_ cap: CGLineCap)     func setLineJoin(_ join: CGLineJoin)     func setMiterLimit(_ limit: CGFloat)     func __setLineDash(phase phase: CGFloat, lengths lengths: UnsafePointer<CGFloat>?, count count: Int)     func setFlatness(_ flatness: CGFloat)     func setAlpha(_ alpha: CGFloat)     func setBlendMode(_ mode: CGBlendMode)     func beginPath()     func __moveTo(x x: CGFloat, y y: CGFloat)     func __addLineTo(x x: CGFloat, y y: CGFloat)     func __addCurveTo(cp1x cp1x: CGFloat, cp1y cp1y: CGFloat, cp2x cp2x: CGFloat, cp2y cp2y: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func __addQuadCurveTo(cpx cpx: CGFloat, cpy cpy: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func closePath()     func addRect(_ rect: CGRect)     func __addRects(_ rects: UnsafePointer<CGRect>?, count count: Int)     func __addLines(between points: UnsafePointer<CGPoint>?, count count: Int)     func addEllipse(in rect: CGRect)     func __addArc(centerX x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Int32)     func __addArc(x1 x1: CGFloat, y1 y1: CGFloat, x2 x2: CGFloat, y2 y2: CGFloat, radius radius: CGFloat)     func addPath(_ path: CGPath)     func replacePathWithStrokedPath()     var isPathEmpty: Bool { get }     var currentPointOfPath: CGPoint { get }     var boundingBoxOfPath: CGRect { get }     var path: CGPath? { get }     func pathContains(_ point: CGPoint, mode mode: CGPathDrawingMode) -> Bool     func drawPath(using mode: CGPathDrawingMode)     func __fillPath()     func __eoFillPath()     func strokePath()     func fill(_ rect: CGRect)     func __fill(_ rects: UnsafePointer<CGRect>?, count count: Int)     func stroke(_ rect: CGRect)     func stroke(_ rect: CGRect, width width: CGFloat)     func clear(_ rect: CGRect)     func fillEllipse(in rect: CGRect)     func strokeEllipse(in rect: CGRect)     func __strokeLineSegments(between points: UnsafePointer<CGPoint>?, count count: Int)     func __clip()     func __eoClip()     func clip(to rect: CGRect, mask mask: CGImage)     var boundingBoxOfClipPath: CGRect { get }     func clip(to rect: CGRect)     func __clip(to rects: UnsafePointer<CGRect>, count count: Int)     func setFillColor(_ color: CGColor)     func setStrokeColor(_ color: CGColor)     func setFillColorSpace(_ space: CGColorSpace)     func setStrokeColorSpace(_ space: CGColorSpace)     func setFillColor(_ components: UnsafePointer<CGFloat>)     func setStrokeColor(_ components: UnsafePointer<CGFloat>)     func setFillPattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>)     func setStrokePattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>)     func setPatternPhase(_ phase: CGSize)     func setFillColor(gray gray: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(gray gray: CGFloat, alpha alpha: CGFloat)     func setFillColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     func setFillColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     func setRenderingIntent(_ intent: CGColorRenderingIntent)     func __draw(in rect: CGRect, image image: CGImage)     func __draw(in rect: CGRect, byTiling image: CGImage)     var interpolationQuality: CGInterpolationQuality     func setShadow(offset offset: CGSize, blur blur: CGFloat, color color: CGColor?)     func setShadow(offset offset: CGSize, blur blur: CGFloat)     func drawLinearGradient(_ gradient: CGGradient, start startPoint: CGPoint, end endPoint: CGPoint, options options: CGGradientDrawingOptions)     func drawRadialGradient(_ gradient: CGGradient, startCenter startCenter: CGPoint, startRadius startRadius: CGFloat, endCenter endCenter: CGPoint, endRadius endRadius: CGFloat, options options: CGGradientDrawingOptions)     func drawShading(_ shading: CGShading)     func setCharacterSpacing(_ spacing: CGFloat)     func __setTextPosition(x x: CGFloat, y y: CGFloat)     var __textPosition: CGPoint { get }     var textMatrix: CGAffineTransform     func setTextDrawingMode(_ mode: CGTextDrawingMode)     func setFont(_ font: CGFont)     func setFontSize(_ size: CGFloat)     func __showGlyphs(_ glyphs: UnsafePointer<CGGlyph>, atPositions Lpositions: UnsafePointer<CGPoint>, count count: Int)     func drawPDFPage(_ page: CGPDFPage)     func beginPage(mediaBox mediaBox: UnsafePointer<CGRect>?)     func endPage()     func flush()     func synchronize()     func setShouldAntialias(_ shouldAntialias: Bool)     func setAllowsAntialiasing(_ allowsAntialiasing: Bool)     func setShouldSmoothFonts(_ shouldSmoothFonts: Bool)     func setAllowsFontSmoothing(_ allowsFontSmoothing: Bool)     func setShouldSubpixelPositionFonts(_ shouldSubpixelPositionFonts: Bool)     func setAllowsFontSubpixelPositioning(_ allowsFontSubpixelPositioning: Bool)     func setShouldSubpixelQuantizeFonts(_ shouldSubpixelQuantizeFonts: Bool)     func setAllowsFontSubpixelQuantization(_ allowsFontSubpixelQuantization: Bool)     func beginTransparencyLayer(auxiliaryInfo auxiliaryInfo: CFDictionary?)     func beginTransparencyLayer(in rect: CGRect, auxiliaryInfo auxInfo: CFDictionary?)     func endTransparencyLayer()     var userSpaceToDeviceSpaceTransform: CGAffineTransform { get }     func convertToDeviceSpace(_ point: CGPoint) -> CGPoint     func convertToUserSpace(_ point: CGPoint) -> CGPoint     func convertToDeviceSpace(_ size: CGSize) -> CGSize     func convertToUserSpace(_ size: CGSize) -> CGSize     func convertToDeviceSpace(_ rect: CGRect) -> CGRect     func convertToUserSpace(_ rect: CGRect) -> CGRect     func selectFont(name name: UnsafePointer<Int8>, size size: CGFloat, textEncoding textEncoding: CGTextEncoding)     func showText(string string: UnsafePointer<Int8>, length length: Int)     func showTextAtPoint(x x: CGFloat, y y: CGFloat, string string: UnsafePointer<Int8>, length length: Int)     func showGlyphs(g g: UnsafePointer<CGGlyph>?, count count: Int)     func showGlyphsAtPoint(x x: CGFloat, y y: CGFloat, glyphs glyphs: UnsafePointer<CGGlyph>?, count count: Int)     func showGlyphsWithAdvances(glyphs glyphs: UnsafePointer<CGGlyph>?, advances advances: UnsafePointer<CGSize>?, count count: Int)     func drawPDFDocument(_ rect: CGRect, document document: CGPDFDocument, page page: Int32)     func __draw(in rect: CGRect, layer layer: CGLayer)     func __draw(at point: CGPoint, layer layer: CGLayer)      init?(consumer consumer: CGDataConsumer, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)      init?(_ url: CFURL, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)     func closePDF()     func beginPDFPage(_ pageInfo: CFDictionary?)     func endPDFPage()     func addDocumentMetadata(_ metadata: CFData?)     func setURL(_ url: CFURL, for rect: CGRect)     func addDestination(_ name: CFString, at point: CGPoint)     func setDestination(_ name: CFString, for rect: CGRect) } extension CGContext {      init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32, releaseCallback releaseCallback: CoreGraphics.CGBitmapContextReleaseDataCallback?, releaseInfo releaseInfo: UnsafeMutableRawPointer?)      init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32)     var data: UnsafeMutableRawPointer? { get }     var width: Int { get }     var height: Int { get }     var bitsPerComponent: Int { get }     var bitsPerPixel: Int { get }     var bytesPerRow: Int { get }     var colorSpace: CGColorSpace? { get }     var alphaInfo: CGImageAlphaInfo { get }     var bitmapInfo: CGBitmapInfo { get }     func makeImage() -> CGImage? } extension CGContext {     class var typeID: CFTypeID { get }     func saveGState()     func restoreGState()     func scaleBy(x sx: CGFloat, y sy: CGFloat)     func translateBy(x tx: CGFloat, y ty: CGFloat)     func rotate(by angle: CGFloat)     func concatenate(_ transform: CGAffineTransform)     var ctm: CGAffineTransform { get }     func setLineWidth(_ width: CGFloat)     func setLineCap(_ cap: CGLineCap)     func setLineJoin(_ join: CGLineJoin)     func setMiterLimit(_ limit: CGFloat)     func __setLineDash(phase phase: CGFloat, lengths lengths: UnsafePointer<CGFloat>?, count count: Int)     func setFlatness(_ flatness: CGFloat)     func setAlpha(_ alpha: CGFloat)     func setBlendMode(_ mode: CGBlendMode)     func beginPath()     func __moveTo(x x: CGFloat, y y: CGFloat)     func __addLineTo(x x: CGFloat, y y: CGFloat)     func __addCurveTo(cp1x cp1x: CGFloat, cp1y cp1y: CGFloat, cp2x cp2x: CGFloat, cp2y cp2y: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func __addQuadCurveTo(cpx cpx: CGFloat, cpy cpy: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func closePath()     func addRect(_ rect: CGRect)     func __addRects(_ rects: UnsafePointer<CGRect>?, count count: Int)     func __addLines(between points: UnsafePointer<CGPoint>?, count count: Int)     func addEllipse(in rect: CGRect)     func __addArc(centerX x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Int32)     func __addArc(x1 x1: CGFloat, y1 y1: CGFloat, x2 x2: CGFloat, y2 y2: CGFloat, radius radius: CGFloat)     func addPath(_ path: CGPath)     func replacePathWithStrokedPath()     var isPathEmpty: Bool { get }     var currentPointOfPath: CGPoint { get }     var boundingBoxOfPath: CGRect { get }     var path: CGPath? { get }     func pathContains(_ point: CGPoint, mode mode: CGPathDrawingMode) -> Bool     func drawPath(using mode: CGPathDrawingMode)     func __fillPath()     func __eoFillPath()     func strokePath()     func fill(_ rect: CGRect)     func __fill(_ rects: UnsafePointer<CGRect>?, count count: Int)     func stroke(_ rect: CGRect)     func stroke(_ rect: CGRect, width width: CGFloat)     func clear(_ rect: CGRect)     func fillEllipse(in rect: CGRect)     func strokeEllipse(in rect: CGRect)     func __strokeLineSegments(between points: UnsafePointer<CGPoint>?, count count: Int)     func __clip()     func __eoClip()     func clip(to rect: CGRect, mask mask: CGImage)     var boundingBoxOfClipPath: CGRect { get }     func clip(to rect: CGRect)     func __clip(to rects: UnsafePointer<CGRect>, count count: Int)     func setFillColor(_ color: CGColor)     func setStrokeColor(_ color: CGColor)     func setFillColorSpace(_ space: CGColorSpace)     func setStrokeColorSpace(_ space: CGColorSpace)     func setFillColor(_ components: UnsafePointer<CGFloat>)     func setStrokeColor(_ components: UnsafePointer<CGFloat>)     func setFillPattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>)     func setStrokePattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>)     func setPatternPhase(_ phase: CGSize)     func setFillColor(gray gray: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(gray gray: CGFloat, alpha alpha: CGFloat)     func setFillColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat)     func setFillColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     func setStrokeColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat)     func setRenderingIntent(_ intent: CGColorRenderingIntent)     func __draw(in rect: CGRect, image image: CGImage)     func __draw(in rect: CGRect, byTiling image: CGImage)     var interpolationQuality: CGInterpolationQuality     func setShadow(offset offset: CGSize, blur blur: CGFloat, color color: CGColor?)     func setShadow(offset offset: CGSize, blur blur: CGFloat)     func drawLinearGradient(_ gradient: CGGradient, start startPoint: CGPoint, end endPoint: CGPoint, options options: CGGradientDrawingOptions)     func drawRadialGradient(_ gradient: CGGradient, startCenter startCenter: CGPoint, startRadius startRadius: CGFloat, endCenter endCenter: CGPoint, endRadius endRadius: CGFloat, options options: CGGradientDrawingOptions)     func drawShading(_ shading: CGShading)     func setCharacterSpacing(_ spacing: CGFloat)     func __setTextPosition(x x: CGFloat, y y: CGFloat)     var __textPosition: CGPoint { get }     var textMatrix: CGAffineTransform     func setTextDrawingMode(_ mode: CGTextDrawingMode)     func setFont(_ font: CGFont)     func setFontSize(_ size: CGFloat)     func __showGlyphs(_ glyphs: UnsafePointer<CGGlyph>, atPositions Lpositions: UnsafePointer<CGPoint>, count count: Int)     func drawPDFPage(_ page: CGPDFPage)     func beginPage(mediaBox mediaBox: UnsafePointer<CGRect>?)     func endPage()     func flush()     func synchronize()     func setShouldAntialias(_ shouldAntialias: Bool)     func setAllowsAntialiasing(_ allowsAntialiasing: Bool)     func setShouldSmoothFonts(_ shouldSmoothFonts: Bool)     func setAllowsFontSmoothing(_ allowsFontSmoothing: Bool)     func setShouldSubpixelPositionFonts(_ shouldSubpixelPositionFonts: Bool)     func setAllowsFontSubpixelPositioning(_ allowsFontSubpixelPositioning: Bool)     func setShouldSubpixelQuantizeFonts(_ shouldSubpixelQuantizeFonts: Bool)     func setAllowsFontSubpixelQuantization(_ allowsFontSubpixelQuantization: Bool)     func beginTransparencyLayer(auxiliaryInfo auxiliaryInfo: CFDictionary?)     func beginTransparencyLayer(in rect: CGRect, auxiliaryInfo auxInfo: CFDictionary?)     func endTransparencyLayer()     var userSpaceToDeviceSpaceTransform: CGAffineTransform { get }     func convertToDeviceSpace(_ point: CGPoint) -> CGPoint     func convertToUserSpace(_ point: CGPoint) -> CGPoint     func convertToDeviceSpace(_ size: CGSize) -> CGSize     func convertToUserSpace(_ size: CGSize) -> CGSize     func convertToDeviceSpace(_ rect: CGRect) -> CGRect     func convertToUserSpace(_ rect: CGRect) -> CGRect     func selectFont(name name: UnsafePointer<Int8>, size size: CGFloat, textEncoding textEncoding: CGTextEncoding)     func showText(string string: UnsafePointer<Int8>, length length: Int)     func showTextAtPoint(x x: CGFloat, y y: CGFloat, string string: UnsafePointer<Int8>, length length: Int)     func showGlyphs(g g: UnsafePointer<CGGlyph>?, count count: Int)     func showGlyphsAtPoint(x x: CGFloat, y y: CGFloat, glyphs glyphs: UnsafePointer<CGGlyph>?, count count: Int)     func showGlyphsWithAdvances(glyphs glyphs: UnsafePointer<CGGlyph>?, advances advances: UnsafePointer<CGSize>?, count count: Int)     func drawPDFDocument(_ rect: CGRect, document document: CGPDFDocument, page page: Int32) } extension CGContext {     func __draw(in rect: CGRect, layer layer: CGLayer)     func __draw(at point: CGPoint, layer layer: CGLayer) } extension CGContext {      init?(consumer consumer: CGDataConsumer, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)      init?(_ url: CFURL, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?)     func closePDF()     func beginPDFPage(_ pageInfo: CFDictionary?)     func endPDFPage()     func addDocumentMetadata(_ metadata: CFData?)     func setURL(_ url: CFURL, for rect: CGRect)     func addDestination(_ name: CFString, at point: CGPoint)     func setDestination(_ name: CFString, for rect: CGRect) } extension CGContext {     func draw(_ layer: CGLayer, in rect: CGRect)     func draw(_ layer: CGLayer, at point: CGPoint) } extension CGContext {     func setLineDash(phase phase: CGFloat, lengths lengths: [CGFloat])     func move(to point: CGPoint)     func addLine(to point: CGPoint)     func addCurve(to end: CGPoint, control1 control1: CGPoint, control2 control2: CGPoint)     func addQuadCurve(to end: CGPoint, control control: CGPoint)     func addRects(_ rects: [CGRect])     func addLines(between points: [CGPoint])     func addArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func addArc(tangent1End tangent1End: CGPoint, tangent2End tangent2End: CGPoint, radius radius: CGFloat)     func fillPath(using rule: CGPathFillRule = default)     func clip(using rule: CGPathFillRule = default)     func fill(_ rects: [CGRect])     func strokeLineSegments(between points: [CGPoint])     func clip(to rects: [CGRect])     func draw(_ image: CGImage, in rect: CGRect, byTiling byTiling: Bool = default)     var textPosition: CGPoint     func showGlyphs(_ glyphs: [CGGlyph], at positions: [CGPoint]) } ``` |

Modified [CGContext.addDestination(_: CFString, at: CGPoint)](https://developer.apple.com/documentation/coregraphics/1455424-cgpdfcontextadddestinationatpoin)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextAddDestinationAtPoint(_:_:_:) | ``` func CGPDFContextAddDestinationAtPoint(_ context: CGContext?, _ name: CFString, _ point: CGPoint) ``` |
| To | addDestination(_:at:) | ``` func addDestination(_ name: CFString, at point: CGPoint) ``` |

Modified [CGContext.addDocumentMetadata(_: CFData?)](https://developer.apple.com/documentation/coregraphics/1456026-cgpdfcontextadddocumentmetadata)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextAddDocumentMetadata(_:_:) | ``` func CGPDFContextAddDocumentMetadata(_ context: CGContext?, _ metadata: CFData?) ``` |
| To | addDocumentMetadata(_:) | ``` func addDocumentMetadata(_ metadata: CFData?) ``` |

Modified [CGContext.addEllipse(in: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456420-addellipse)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextAddEllipseInRect(_:_:) | ``` func CGContextAddEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | addEllipse(in:) | ``` func addEllipse(in rect: CGRect) ``` |

Modified [CGContext.addPath(_: CGPath)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456628-addpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextAddPath(_:_:) | ``` func CGContextAddPath(_ c: CGContext?, _ path: CGPath?) ``` |
| To | addPath(_:) | ``` func addPath(_ path: CGPath) ``` |

Modified [CGContext.addRect(_: CGRect)](https://developer.apple.com/documentation/coregraphics/1456617-cgcontextaddrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextAddRect(_:_:) | ``` func CGContextAddRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | addRect(_:) | ``` func addRect(_ rect: CGRect) ``` |

Modified [CGContext.CGBitmapContextGetAlphaInfo(_: CGContext?) -> CGImageAlphaInfo](https://developer.apple.com/documentation/coregraphics/1454960-cgbitmapcontextgetalphainfo)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetAlphaInfo(_:) | ``` func CGBitmapContextGetAlphaInfo(_ context: CGContext?) -> CGImageAlphaInfo ``` | -- |
| To | alphaInfo | ``` var alphaInfo: CGImageAlphaInfo { get } ``` | yes |

Modified [CGContext.beginPage(mediaBox: UnsafePointer<CGRect>?)](https://developer.apple.com/documentation/coregraphics/1454794-cgcontextbeginpage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextBeginPage(_:_:) | ``` func CGContextBeginPage(_ c: CGContext?, _ mediaBox: UnsafePointer<CGRect>) ``` |
| To | beginPage(mediaBox:) | ``` func beginPage(mediaBox mediaBox: UnsafePointer<CGRect>?) ``` |

Modified [CGContext.beginPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456635-beginpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextBeginPath(_:) | ``` func CGContextBeginPath(_ c: CGContext?) ``` |
| To | beginPath() | ``` func beginPath() ``` |

Modified [CGContext.beginPDFPage(_: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456578-beginpdfpage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextBeginPage(_:_:) | ``` func CGPDFContextBeginPage(_ context: CGContext?, _ pageInfo: CFDictionary?) ``` |
| To | beginPDFPage(_:) | ``` func beginPDFPage(_ pageInfo: CFDictionary?) ``` |

Modified [CGContext.beginTransparencyLayer(auxiliaryInfo: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456011-begintransparencylayer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextBeginTransparencyLayer(_:_:) | ``` func CGContextBeginTransparencyLayer(_ c: CGContext?, _ auxiliaryInfo: CFDictionary?) ``` |
| To | beginTransparencyLayer(auxiliaryInfo:) | ``` func beginTransparencyLayer(auxiliaryInfo auxiliaryInfo: CFDictionary?) ``` |

Modified [CGContext.beginTransparencyLayer(in: CGRect, auxiliaryInfo: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/1454368-cgcontextbegintransparencylayerw)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextBeginTransparencyLayerWithRect(_:_:_:) | ``` func CGContextBeginTransparencyLayerWithRect(_ c: CGContext?, _ rect: CGRect, _ auxInfo: CFDictionary?) ``` |
| To | beginTransparencyLayer(in:auxiliaryInfo:) | ``` func beginTransparencyLayer(in rect: CGRect, auxiliaryInfo auxInfo: CFDictionary?) ``` |

Modified [CGContext.CGBitmapContextGetBitmapInfo(_: CGContext?) -> CGBitmapInfo](https://developer.apple.com/documentation/coregraphics/1455839-cgbitmapcontextgetbitmapinfo)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetBitmapInfo(_:) | ``` func CGBitmapContextGetBitmapInfo(_ context: CGContext?) -> CGBitmapInfo ``` | -- |
| To | bitmapInfo | ``` var bitmapInfo: CGBitmapInfo { get } ``` | yes |

Modified [CGContext.CGBitmapContextGetBitsPerComponent(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1455383-cgbitmapcontextgetbitspercompone)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetBitsPerComponent(_:) | ``` func CGBitmapContextGetBitsPerComponent(_ context: CGContext?) -> Int ``` | -- |
| To | bitsPerComponent | ``` var bitsPerComponent: Int { get } ``` | yes |

Modified [CGContext.CGBitmapContextGetBitsPerPixel(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1455946-cgbitmapcontextgetbitsperpixel)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetBitsPerPixel(_:) | ``` func CGBitmapContextGetBitsPerPixel(_ context: CGContext?) -> Int ``` | -- |
| To | bitsPerPixel | ``` var bitsPerPixel: Int { get } ``` | yes |

Modified [CGContext.CGContextGetClipBoundingBox(_: CGContext?) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgcontext/1455387-boundingboxofclippath)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextGetClipBoundingBox(_:) | ``` func CGContextGetClipBoundingBox(_ c: CGContext?) -> CGRect ``` | -- |
| To | boundingBoxOfClipPath | ``` var boundingBoxOfClipPath: CGRect { get } ``` | yes |

Modified [CGContext.CGContextGetPathBoundingBox(_: CGContext?) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgcontext/1454577-boundingboxofpath)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextGetPathBoundingBox(_:) | ``` func CGContextGetPathBoundingBox(_ c: CGContext?) -> CGRect ``` | -- |
| To | boundingBoxOfPath | ``` var boundingBoxOfPath: CGRect { get } ``` | yes |

Modified [CGContext.CGBitmapContextGetBytesPerRow(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcontext/1456129-bytesperrow)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetBytesPerRow(_:) | ``` func CGBitmapContextGetBytesPerRow(_ context: CGContext?) -> Int ``` | -- |
| To | bytesPerRow | ``` var bytesPerRow: Int { get } ``` | yes |

Modified [CGContext.clear(_: CGRect)](https://developer.apple.com/documentation/coregraphics/1456457-cgcontextclearrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextClearRect(_:_:) | ``` func CGContextClearRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | clear(_:) | ``` func clear(_ rect: CGRect) ``` |

Modified [CGContext.clip(to: CGRect)](https://developer.apple.com/documentation/coregraphics/1454716-cgcontextcliptorect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextClipToRect(_:_:) | ``` func CGContextClipToRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | clip(to:) | ``` func clip(to rect: CGRect) ``` |

Modified [CGContext.clip(to: CGRect, mask: CGImage)](https://developer.apple.com/documentation/coregraphics/1456497-cgcontextcliptomask)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextClipToMask(_:_:_:) | ``` func CGContextClipToMask(_ c: CGContext?, _ rect: CGRect, _ mask: CGImage?) ``` |
| To | clip(to:mask:) | ``` func clip(to rect: CGRect, mask mask: CGImage) ``` |

Modified [CGContext.closePath()](https://developer.apple.com/documentation/coregraphics/1454508-cgcontextclosepath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextClosePath(_:) | ``` func CGContextClosePath(_ c: CGContext?) ``` |
| To | closePath() | ``` func closePath() ``` |

Modified [CGContext.closePDF()](https://developer.apple.com/documentation/coregraphics/1454306-cgpdfcontextclose)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextClose(_:) | ``` func CGPDFContextClose(_ context: CGContext?) ``` |
| To | closePDF() | ``` func closePDF() ``` |

Modified [CGContext.CGBitmapContextGetColorSpace(_: CGContext?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/1454058-cgbitmapcontextgetcolorspace)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetColorSpace(_:) | ``` func CGBitmapContextGetColorSpace(_ context: CGContext?) -> CGColorSpace? ``` | -- |
| To | colorSpace | ``` var colorSpace: CGColorSpace? { get } ``` | yes |

Modified [CGContext.concatenate(_: CGAffineTransform)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454897-concatenate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConcatCTM(_:_:) | ``` func CGContextConcatCTM(_ c: CGContext?, _ transform: CGAffineTransform) ``` |
| To | concatenate(_:) | ``` func concatenate(_ transform: CGAffineTransform) ``` |

Modified [CGContext.convertToDeviceSpace(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgcontext/1456017-converttodevicespace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertRectToDeviceSpace(_:_:) | ``` func CGContextConvertRectToDeviceSpace(_ c: CGContext?, _ rect: CGRect) -> CGRect ``` |
| To | convertToDeviceSpace(_:) | ``` func convertToDeviceSpace(_ rect: CGRect) -> CGRect ``` |

Modified [CGContext.convertToDeviceSpace(_: CGSize) -> CGSize](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertSizeToDeviceSpace(_:_:) | ``` func CGContextConvertSizeToDeviceSpace(_ c: CGContext?, _ size: CGSize) -> CGSize ``` |
| To | convertToDeviceSpace(_:) | ``` func convertToDeviceSpace(_ size: CGSize) -> CGSize ``` |

Modified [CGContext.convertToDeviceSpace(_: CGPoint) -> CGPoint](https://developer.apple.com/documentation/coregraphics/cgcontext/1455916-converttodevicespace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertPointToDeviceSpace(_:_:) | ``` func CGContextConvertPointToDeviceSpace(_ c: CGContext?, _ point: CGPoint) -> CGPoint ``` |
| To | convertToDeviceSpace(_:) | ``` func convertToDeviceSpace(_ point: CGPoint) -> CGPoint ``` |

Modified [CGContext.convertToUserSpace(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/1454165-cgcontextconvertrecttouserspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertRectToUserSpace(_:_:) | ``` func CGContextConvertRectToUserSpace(_ c: CGContext?, _ rect: CGRect) -> CGRect ``` |
| To | convertToUserSpace(_:) | ``` func convertToUserSpace(_ rect: CGRect) -> CGRect ``` |

Modified [CGContext.convertToUserSpace(_: CGSize) -> CGSize](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertSizeToUserSpace(_:_:) | ``` func CGContextConvertSizeToUserSpace(_ c: CGContext?, _ size: CGSize) -> CGSize ``` |
| To | convertToUserSpace(_:) | ``` func convertToUserSpace(_ size: CGSize) -> CGSize ``` |

Modified [CGContext.convertToUserSpace(_: CGPoint) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1456451-cgcontextconvertpointtouserspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextConvertPointToUserSpace(_:_:) | ``` func CGContextConvertPointToUserSpace(_ c: CGContext?, _ point: CGPoint) -> CGPoint ``` |
| To | convertToUserSpace(_:) | ``` func convertToUserSpace(_ point: CGPoint) -> CGPoint ``` |

Modified [CGContext.CGContextGetCTM(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgcontext/1454691-ctm)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextGetCTM(_:) | ``` func CGContextGetCTM(_ c: CGContext?) -> CGAffineTransform ``` | -- |
| To | ctm | ``` var ctm: CGAffineTransform { get } ``` | yes |

Modified [CGContext.CGContextGetPathCurrentPoint(_: CGContext?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/1454788-cgcontextgetpathcurrentpoint)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextGetPathCurrentPoint(_:) | ``` func CGContextGetPathCurrentPoint(_ c: CGContext?) -> CGPoint ``` | -- |
| To | currentPointOfPath | ``` var currentPointOfPath: CGPoint { get } ``` | yes |

Modified [CGContext.CGBitmapContextGetData(_: CGContext?) -> UnsafeMutablePointer<Void>](https://developer.apple.com/documentation/coregraphics/1455517-cgbitmapcontextgetdata)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetData(_:) | ``` func CGBitmapContextGetData(_ context: CGContext?) -> UnsafeMutablePointer<Void> ``` | -- |
| To | data | ``` var data: UnsafeMutableRawPointer? { get } ``` | yes |

Modified [CGContext.drawLinearGradient(_: CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](https://developer.apple.com/documentation/coregraphics/1454782-cgcontextdrawlineargradient)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextDrawLinearGradient(_:_:_:_:_:) | ``` func CGContextDrawLinearGradient(_ c: CGContext?, _ gradient: CGGradient?, _ startPoint: CGPoint, _ endPoint: CGPoint, _ options: CGGradientDrawingOptions) ``` |
| To | drawLinearGradient(_:start:end:options:) | ``` func drawLinearGradient(_ gradient: CGGradient, start startPoint: CGPoint, end endPoint: CGPoint, options options: CGGradientDrawingOptions) ``` |

Modified [CGContext.drawPath(using: CGPathDrawingMode)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455195-drawpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextDrawPath(_:_:) | ``` func CGContextDrawPath(_ c: CGContext?, _ mode: CGPathDrawingMode) ``` |
| To | drawPath(using:) | ``` func drawPath(using mode: CGPathDrawingMode) ``` |

Modified [CGContext.drawPDFPage(_: CGPDFPage)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456255-drawpdfpage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextDrawPDFPage(_:_:) | ``` func CGContextDrawPDFPage(_ c: CGContext?, _ page: CGPDFPage?) ``` |
| To | drawPDFPage(_:) | ``` func drawPDFPage(_ page: CGPDFPage) ``` |

Modified [CGContext.drawRadialGradient(_: CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](https://developer.apple.com/documentation/coregraphics/1455923-cgcontextdrawradialgradient)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextDrawRadialGradient(_:_:_:_:_:_:_:) | ``` func CGContextDrawRadialGradient(_ c: CGContext?, _ gradient: CGGradient?, _ startCenter: CGPoint, _ startRadius: CGFloat, _ endCenter: CGPoint, _ endRadius: CGFloat, _ options: CGGradientDrawingOptions) ``` |
| To | drawRadialGradient(_:startCenter:startRadius:endCenter:endRadius:options:) | ``` func drawRadialGradient(_ gradient: CGGradient, startCenter startCenter: CGPoint, startRadius startRadius: CGFloat, endCenter endCenter: CGPoint, endRadius endRadius: CGFloat, options options: CGGradientDrawingOptions) ``` |

Modified [CGContext.drawShading(_: CGShading)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456643-drawshading)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextDrawShading(_:_:) | ``` func CGContextDrawShading(_ c: CGContext?, _ shading: CGShading?) ``` |
| To | drawShading(_:) | ``` func drawShading(_ shading: CGShading) ``` |

Modified [CGContext.endPage()](https://developer.apple.com/documentation/coregraphics/1455027-cgcontextendpage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextEndPage(_:) | ``` func CGContextEndPage(_ c: CGContext?) ``` |
| To | endPage() | ``` func endPage() ``` |

Modified [CGContext.endPDFPage()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456122-endpdfpage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextEndPage(_:) | ``` func CGPDFContextEndPage(_ context: CGContext?) ``` |
| To | endPDFPage() | ``` func endPDFPage() ``` |

Modified [CGContext.endTransparencyLayer()](https://developer.apple.com/documentation/coregraphics/1456554-cgcontextendtransparencylayer)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextEndTransparencyLayer(_:) | ``` func CGContextEndTransparencyLayer(_ c: CGContext?) ``` |
| To | endTransparencyLayer() | ``` func endTransparencyLayer() ``` |

Modified [CGContext.fill(_: CGRect)](https://developer.apple.com/documentation/coregraphics/1454700-cgcontextfillrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextFillRect(_:_:) | ``` func CGContextFillRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | fill(_:) | ``` func fill(_ rect: CGRect) ``` |

Modified [CGContext.fillEllipse(in: CGRect)](https://developer.apple.com/documentation/coregraphics/1454371-cgcontextfillellipseinrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextFillEllipseInRect(_:_:) | ``` func CGContextFillEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | fillEllipse(in:) | ``` func fillEllipse(in rect: CGRect) ``` |

Modified [CGContext.flush()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454895-flush)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextFlush(_:) | ``` func CGContextFlush(_ c: CGContext?) ``` |
| To | flush() | ``` func flush() ``` |

Modified [CGContext.CGBitmapContextGetHeight(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/1454681-cgbitmapcontextgetheight)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetHeight(_:) | ``` func CGBitmapContextGetHeight(_ context: CGContext?) -> Int ``` | -- |
| To | height | ``` var height: Int { get } ``` | yes |

Modified [CGContext.init(_: CFURL, mediaBox: UnsafePointer<CGRect>?, _: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/1456290-cgpdfcontextcreatewithurl)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextCreateWithURL(_:_:_:) | ``` func CGPDFContextCreateWithURL(_ url: CFURL?, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary?) -> CGContext? ``` |
| To | init(_:mediaBox:_:) | ``` init?(_ url: CFURL, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?) ``` |

Modified [CGContext.init(consumer: CGDataConsumer, mediaBox: UnsafePointer<CGRect>?, _: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/1454204-cgpdfcontextcreate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextCreate(_:_:_:) | ``` func CGPDFContextCreate(_ consumer: CGDataConsumer?, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary?) -> CGContext? ``` |
| To | init(consumer:mediaBox:_:) | ``` init?(consumer consumer: CGDataConsumer, mediaBox mediaBox: UnsafePointer<CGRect>?, _ auxiliaryInfo: CFDictionary?) ``` |

Modified [CGContext.init(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32)](https://developer.apple.com/documentation/coregraphics/1455939-cgbitmapcontextcreate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGBitmapContextCreate(_:_:_:_:_:_:_:) | ``` func CGBitmapContextCreate(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: UInt32) -> CGContext? ``` |
| To | init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:) | ``` init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32) ``` |

Modified [CGContext.init(data: UnsafeMutableRawPointer?, width: Int, height: Int, bitsPerComponent: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: UInt32, releaseCallback: CoreGraphics.CGBitmapContextReleaseDataCallback?, releaseInfo: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coregraphics/1454984-cgbitmapcontextcreatewithdata)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGBitmapContextCreateWithData(_:_:_:_:_:_:_:_:_:) | ``` func CGBitmapContextCreateWithData(_ data: UnsafeMutablePointer<Void>, _ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: UInt32, _ releaseCallback: CGBitmapContextReleaseDataCallback?, _ releaseInfo: UnsafeMutablePointer<Void>) -> CGContext? ``` |
| To | init(data:width:height:bitsPerComponent:bytesPerRow:space:bitmapInfo:releaseCallback:releaseInfo:) | ``` init?(data data: UnsafeMutableRawPointer?, width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: UInt32, releaseCallback releaseCallback: CoreGraphics.CGBitmapContextReleaseDataCallback?, releaseInfo releaseInfo: UnsafeMutableRawPointer?) ``` |

Modified [CGContext.CGContextGetInterpolationQuality(_: CGContext?) -> CGInterpolationQuality](https://developer.apple.com/documentation/coregraphics/1454940-cgcontextgetinterpolationquality)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextGetInterpolationQuality(_:) | ``` func CGContextGetInterpolationQuality(_ c: CGContext?) -> CGInterpolationQuality ``` |
| To | interpolationQuality | ``` var interpolationQuality: CGInterpolationQuality ``` |

Modified [CGContext.CGContextIsPathEmpty(_: CGContext?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455772-cgcontextispathempty)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextIsPathEmpty(_:) | ``` func CGContextIsPathEmpty(_ c: CGContext?) -> Bool ``` | -- |
| To | isPathEmpty | ``` var isPathEmpty: Bool { get } ``` | yes |

Modified [CGContext.makeImage() -> CGImage?](https://developer.apple.com/documentation/coregraphics/cgcontext/1454225-makeimage)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGBitmapContextCreateImage(_:) | ``` func CGBitmapContextCreateImage(_ context: CGContext?) -> CGImage? ``` |
| To | makeImage() | ``` func makeImage() -> CGImage? ``` |

Modified [CGContext.CGContextCopyPath(_: CGContext?) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1455397-cgcontextcopypath)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGContextCopyPath(_:) | ``` func CGContextCopyPath(_ c: CGContext?) -> CGPath? ``` | tvOS 9.0 | -- |
| To | path | ``` var path: CGPath? { get } ``` | tvOS 10.0 | yes |

Modified [CGContext.pathContains(_: CGPoint, mode: CGPathDrawingMode) -> Bool](https://developer.apple.com/documentation/coregraphics/cgcontext/1454778-pathcontains)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextPathContainsPoint(_:_:_:) | ``` func CGContextPathContainsPoint(_ c: CGContext?, _ point: CGPoint, _ mode: CGPathDrawingMode) -> Bool ``` |
| To | pathContains(_:mode:) | ``` func pathContains(_ point: CGPoint, mode mode: CGPathDrawingMode) -> Bool ``` |

Modified [CGContext.replacePathWithStrokedPath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454517-replacepathwithstrokedpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextReplacePathWithStrokedPath(_:) | ``` func CGContextReplacePathWithStrokedPath(_ c: CGContext?) ``` |
| To | replacePathWithStrokedPath() | ``` func replacePathWithStrokedPath() ``` |

Modified [CGContext.restoreGState()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455391-restoregstate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextRestoreGState(_:) | ``` func CGContextRestoreGState(_ c: CGContext?) ``` |
| To | restoreGState() | ``` func restoreGState() ``` |

Modified [CGContext.rotate(by: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456228-rotate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextRotateCTM(_:_:) | ``` func CGContextRotateCTM(_ c: CGContext?, _ angle: CGFloat) ``` |
| To | rotate(by:) | ``` func rotate(by angle: CGFloat) ``` |

Modified [CGContext.saveGState()](https://developer.apple.com/documentation/coregraphics/cgcontext/1456156-savegstate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSaveGState(_:) | ``` func CGContextSaveGState(_ c: CGContext?) ``` |
| To | saveGState() | ``` func saveGState() ``` |

Modified [CGContext.scaleBy(x: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454659-scaleby)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextScaleCTM(_:_:_:) | ``` func CGContextScaleCTM(_ c: CGContext?, _ sx: CGFloat, _ sy: CGFloat) ``` |
| To | scaleBy(x:y:) | ``` func scaleBy(x sx: CGFloat, y sy: CGFloat) ``` |

Modified [CGContext.setAllowsAntialiasing(_: Bool)](https://developer.apple.com/documentation/coregraphics/1456310-cgcontextsetallowsantialiasing)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetAllowsAntialiasing(_:_:) | ``` func CGContextSetAllowsAntialiasing(_ c: CGContext?, _ allowsAntialiasing: Bool) ``` |
| To | setAllowsAntialiasing(_:) | ``` func setAllowsAntialiasing(_ allowsAntialiasing: Bool) ``` |

Modified [CGContext.setAllowsFontSmoothing(_: Bool)](https://developer.apple.com/documentation/coregraphics/1454767-cgcontextsetallowsfontsmoothing)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetAllowsFontSmoothing(_:_:) | ``` func CGContextSetAllowsFontSmoothing(_ c: CGContext?, _ allowsFontSmoothing: Bool) ``` |
| To | setAllowsFontSmoothing(_:) | ``` func setAllowsFontSmoothing(_ allowsFontSmoothing: Bool) ``` |

Modified [CGContext.setAllowsFontSubpixelPositioning(_: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454942-setallowsfontsubpixelpositioning)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetAllowsFontSubpixelPositioning(_:_:) | ``` func CGContextSetAllowsFontSubpixelPositioning(_ c: CGContext?, _ allowsFontSubpixelPositioning: Bool) ``` |
| To | setAllowsFontSubpixelPositioning(_:) | ``` func setAllowsFontSubpixelPositioning(_ allowsFontSubpixelPositioning: Bool) ``` |

Modified [CGContext.setAllowsFontSubpixelQuantization(_: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456263-setallowsfontsubpixelquantizatio)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetAllowsFontSubpixelQuantization(_:_:) | ``` func CGContextSetAllowsFontSubpixelQuantization(_ c: CGContext?, _ allowsFontSubpixelQuantization: Bool) ``` |
| To | setAllowsFontSubpixelQuantization(_:) | ``` func setAllowsFontSubpixelQuantization(_ allowsFontSubpixelQuantization: Bool) ``` |

Modified [CGContext.setAlpha(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456404-setalpha)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetAlpha(_:_:) | ``` func CGContextSetAlpha(_ c: CGContext?, _ alpha: CGFloat) ``` |
| To | setAlpha(_:) | ``` func setAlpha(_ alpha: CGFloat) ``` |

Modified [CGContext.setBlendMode(_: CGBlendMode)](https://developer.apple.com/documentation/coregraphics/1455994-cgcontextsetblendmode)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetBlendMode(_:_:) | ``` func CGContextSetBlendMode(_ c: CGContext?, _ mode: CGBlendMode) ``` |
| To | setBlendMode(_:) | ``` func setBlendMode(_ mode: CGBlendMode) ``` |

Modified [CGContext.setCharacterSpacing(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/1454786-cgcontextsetcharacterspacing)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetCharacterSpacing(_:_:) | ``` func CGContextSetCharacterSpacing(_ c: CGContext?, _ spacing: CGFloat) ``` |
| To | setCharacterSpacing(_:) | ``` func setCharacterSpacing(_ spacing: CGFloat) ``` |

Modified [CGContext.setDestination(_: CFString, for: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456459-setdestination)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextSetDestinationForRect(_:_:_:) | ``` func CGPDFContextSetDestinationForRect(_ context: CGContext?, _ name: CFString, _ rect: CGRect) ``` |
| To | setDestination(_:for:) | ``` func setDestination(_ name: CFString, for rect: CGRect) ``` |

Modified [CGContext.setFillColor(_: CGColor)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454079-setfillcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFillColorWithColor(_:_:) | ``` func CGContextSetFillColorWithColor(_ c: CGContext?, _ color: CGColor?) ``` |
| To | setFillColor(_:) | ``` func setFillColor(_ color: CGColor) ``` |

Modified [CGContext.setFillColor(_: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/1455296-cgcontextsetfillcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFillColor(_:_:) | ``` func CGContextSetFillColor(_ c: CGContext?, _ components: UnsafePointer<CGFloat>) ``` |
| To | setFillColor(_:) | ``` func setFillColor(_ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContext.setFillColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454214-setfillcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetCMYKFillColor(_:_:_:_:_:_:) | ``` func CGContextSetCMYKFillColor(_ c: CGContext?, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |
| To | setFillColor(cyan:magenta:yellow:black:alpha:) | ``` func setFillColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setFillColor(gray: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454255-setfillcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetGrayFillColor(_:_:_:) | ``` func CGContextSetGrayFillColor(_ c: CGContext?, _ gray: CGFloat, _ alpha: CGFloat) ``` |
| To | setFillColor(gray:alpha:) | ``` func setFillColor(gray gray: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setFillColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455624-cgcontextsetrgbfillcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetRGBFillColor(_:_:_:_:_:) | ``` func CGContextSetRGBFillColor(_ c: CGContext?, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |
| To | setFillColor(red:green:blue:alpha:) | ``` func setFillColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setFillColorSpace(_: CGColorSpace)](https://developer.apple.com/documentation/coregraphics/1455151-cgcontextsetfillcolorspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFillColorSpace(_:_:) | ``` func CGContextSetFillColorSpace(_ c: CGContext?, _ space: CGColorSpace?) ``` |
| To | setFillColorSpace(_:) | ``` func setFillColorSpace(_ space: CGColorSpace) ``` |

Modified [CGContext.setFillPattern(_: CGPattern, colorComponents: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456334-setfillpattern)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFillPattern(_:_:_:) | ``` func CGContextSetFillPattern(_ c: CGContext?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) ``` |
| To | setFillPattern(_:colorComponents:) | ``` func setFillPattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>) ``` |

Modified [CGContext.setFlatness(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455798-setflatness)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFlatness(_:_:) | ``` func CGContextSetFlatness(_ c: CGContext?, _ flatness: CGFloat) ``` |
| To | setFlatness(_:) | ``` func setFlatness(_ flatness: CGFloat) ``` |

Modified [CGContext.setFont(_: CGFont)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454950-setfont)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFont(_:_:) | ``` func CGContextSetFont(_ c: CGContext?, _ font: CGFont?) ``` |
| To | setFont(_:) | ``` func setFont(_ font: CGFont) ``` |

Modified [CGContext.setFontSize(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456426-setfontsize)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetFontSize(_:_:) | ``` func CGContextSetFontSize(_ c: CGContext?, _ size: CGFloat) ``` |
| To | setFontSize(_:) | ``` func setFontSize(_ size: CGFloat) ``` |

Modified [CGContext.setLineCap(_: CGLineCap)](https://developer.apple.com/documentation/coregraphics/1454326-cgcontextsetlinecap)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetLineCap(_:_:) | ``` func CGContextSetLineCap(_ c: CGContext?, _ cap: CGLineCap) ``` |
| To | setLineCap(_:) | ``` func setLineCap(_ cap: CGLineCap) ``` |

Modified [CGContext.setLineJoin(_: CGLineJoin)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455973-setlinejoin)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetLineJoin(_:_:) | ``` func CGContextSetLineJoin(_ c: CGContext?, _ join: CGLineJoin) ``` |
| To | setLineJoin(_:) | ``` func setLineJoin(_ join: CGLineJoin) ``` |

Modified [CGContext.setLineWidth(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455270-setlinewidth)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetLineWidth(_:_:) | ``` func CGContextSetLineWidth(_ c: CGContext?, _ width: CGFloat) ``` |
| To | setLineWidth(_:) | ``` func setLineWidth(_ width: CGFloat) ``` |

Modified [CGContext.setMiterLimit(_: CGFloat)](https://developer.apple.com/documentation/coregraphics/1456499-cgcontextsetmiterlimit)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetMiterLimit(_:_:) | ``` func CGContextSetMiterLimit(_ c: CGContext?, _ limit: CGFloat) ``` |
| To | setMiterLimit(_:) | ``` func setMiterLimit(_ limit: CGFloat) ``` |

Modified [CGContext.setPatternPhase(_: CGSize)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455334-setpatternphase)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetPatternPhase(_:_:) | ``` func CGContextSetPatternPhase(_ c: CGContext?, _ phase: CGSize) ``` |
| To | setPatternPhase(_:) | ``` func setPatternPhase(_ phase: CGSize) ``` |

Modified [CGContext.setRenderingIntent(_: CGColorRenderingIntent)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455544-setrenderingintent)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetRenderingIntent(_:_:) | ``` func CGContextSetRenderingIntent(_ c: CGContext?, _ intent: CGColorRenderingIntent) ``` |
| To | setRenderingIntent(_:) | ``` func setRenderingIntent(_ intent: CGColorRenderingIntent) ``` |

Modified [CGContext.setShadow(offset: CGSize, blur: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456082-setshadow)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShadow(_:_:_:) | ``` func CGContextSetShadow(_ c: CGContext?, _ offset: CGSize, _ blur: CGFloat) ``` |
| To | setShadow(offset:blur:) | ``` func setShadow(offset offset: CGSize, blur blur: CGFloat) ``` |

Modified [CGContext.setShadow(offset: CGSize, blur: CGFloat, color: CGColor?)](https://developer.apple.com/documentation/coregraphics/1455205-cgcontextsetshadowwithcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShadowWithColor(_:_:_:_:) | ``` func CGContextSetShadowWithColor(_ c: CGContext?, _ offset: CGSize, _ blur: CGFloat, _ color: CGColor?) ``` |
| To | setShadow(offset:blur:color:) | ``` func setShadow(offset offset: CGSize, blur blur: CGFloat, color color: CGColor?) ``` |

Modified [CGContext.setShouldAntialias(_: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455178-setshouldantialias)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShouldAntialias(_:_:) | ``` func CGContextSetShouldAntialias(_ c: CGContext?, _ shouldAntialias: Bool) ``` |
| To | setShouldAntialias(_:) | ``` func setShouldAntialias(_ shouldAntialias: Bool) ``` |

Modified [CGContext.setShouldSmoothFonts(_: Bool)](https://developer.apple.com/documentation/coregraphics/1455816-cgcontextsetshouldsmoothfonts)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShouldSmoothFonts(_:_:) | ``` func CGContextSetShouldSmoothFonts(_ c: CGContext?, _ shouldSmoothFonts: Bool) ``` |
| To | setShouldSmoothFonts(_:) | ``` func setShouldSmoothFonts(_ shouldSmoothFonts: Bool) ``` |

Modified [CGContext.setShouldSubpixelPositionFonts(_: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455671-setshouldsubpixelpositionfonts)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShouldSubpixelPositionFonts(_:_:) | ``` func CGContextSetShouldSubpixelPositionFonts(_ c: CGContext?, _ shouldSubpixelPositionFonts: Bool) ``` |
| To | setShouldSubpixelPositionFonts(_:) | ``` func setShouldSubpixelPositionFonts(_ shouldSubpixelPositionFonts: Bool) ``` |

Modified [CGContext.setShouldSubpixelQuantizeFonts(_: Bool)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455766-setshouldsubpixelquantizefonts)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetShouldSubpixelQuantizeFonts(_:_:) | ``` func CGContextSetShouldSubpixelQuantizeFonts(_ c: CGContext?, _ shouldSubpixelQuantizeFonts: Bool) ``` |
| To | setShouldSubpixelQuantizeFonts(_:) | ``` func setShouldSubpixelQuantizeFonts(_ shouldSubpixelQuantizeFonts: Bool) ``` |

Modified [CGContext.setStrokeColor(_: CGColor)](https://developer.apple.com/documentation/coregraphics/1456196-cgcontextsetstrokecolorwithcolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetStrokeColorWithColor(_:_:) | ``` func CGContextSetStrokeColorWithColor(_ c: CGContext?, _ color: CGColor?) ``` |
| To | setStrokeColor(_:) | ``` func setStrokeColor(_ color: CGColor) ``` |

Modified [CGContext.setStrokeColor(_: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456283-setstrokecolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetStrokeColor(_:_:) | ``` func CGContextSetStrokeColor(_ c: CGContext?, _ components: UnsafePointer<CGFloat>) ``` |
| To | setStrokeColor(_:) | ``` func setStrokeColor(_ components: UnsafePointer<CGFloat>) ``` |

Modified [CGContext.setStrokeColor(cyan: CGFloat, magenta: CGFloat, yellow: CGFloat, black: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455358-setstrokecolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetCMYKStrokeColor(_:_:_:_:_:_:) | ``` func CGContextSetCMYKStrokeColor(_ c: CGContext?, _ cyan: CGFloat, _ magenta: CGFloat, _ yellow: CGFloat, _ black: CGFloat, _ alpha: CGFloat) ``` |
| To | setStrokeColor(cyan:magenta:yellow:black:alpha:) | ``` func setStrokeColor(cyan cyan: CGFloat, magenta magenta: CGFloat, yellow yellow: CGFloat, black black: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setStrokeColor(gray: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1455209-setstrokecolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetGrayStrokeColor(_:_:_:) | ``` func CGContextSetGrayStrokeColor(_ c: CGContext?, _ gray: CGFloat, _ alpha: CGFloat) ``` |
| To | setStrokeColor(gray:alpha:) | ``` func setStrokeColor(gray gray: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setStrokeColor(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1456378-setstrokecolor)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetRGBStrokeColor(_:_:_:_:_:) | ``` func CGContextSetRGBStrokeColor(_ c: CGContext?, _ red: CGFloat, _ green: CGFloat, _ blue: CGFloat, _ alpha: CGFloat) ``` |
| To | setStrokeColor(red:green:blue:alpha:) | ``` func setStrokeColor(red red: CGFloat, green green: CGFloat, blue blue: CGFloat, alpha alpha: CGFloat) ``` |

Modified [CGContext.setStrokeColorSpace(_: CGColorSpace)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454396-setstrokecolorspace)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetStrokeColorSpace(_:_:) | ``` func CGContextSetStrokeColorSpace(_ c: CGContext?, _ space: CGColorSpace?) ``` |
| To | setStrokeColorSpace(_:) | ``` func setStrokeColorSpace(_ space: CGColorSpace) ``` |

Modified [CGContext.setStrokePattern(_: CGPattern, colorComponents: UnsafePointer<CGFloat>)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454796-setstrokepattern)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetStrokePattern(_:_:_:) | ``` func CGContextSetStrokePattern(_ c: CGContext?, _ pattern: CGPattern?, _ components: UnsafePointer<CGFloat>) ``` |
| To | setStrokePattern(_:colorComponents:) | ``` func setStrokePattern(_ pattern: CGPattern, colorComponents components: UnsafePointer<CGFloat>) ``` |

Modified [CGContext.setTextDrawingMode(_: CGTextDrawingMode)](https://developer.apple.com/documentation/coregraphics/1454253-cgcontextsettextdrawingmode)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSetTextDrawingMode(_:_:) | ``` func CGContextSetTextDrawingMode(_ c: CGContext?, _ mode: CGTextDrawingMode) ``` |
| To | setTextDrawingMode(_:) | ``` func setTextDrawingMode(_ mode: CGTextDrawingMode) ``` |

Modified [CGContext.setURL(_: CFURL, for: CGRect)](https://developer.apple.com/documentation/coregraphics/1455622-cgpdfcontextseturlforrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFContextSetURLForRect(_:_:_:) | ``` func CGPDFContextSetURLForRect(_ context: CGContext?, _ url: CFURL, _ rect: CGRect) ``` |
| To | setURL(_:for:) | ``` func setURL(_ url: CFURL, for rect: CGRect) ``` |

Modified [CGContext.stroke(_: CGRect)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454675-stroke)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextStrokeRect(_:_:) | ``` func CGContextStrokeRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | stroke(_:) | ``` func stroke(_ rect: CGRect) ``` |

Modified [CGContext.stroke(_: CGRect, width: CGFloat)](https://developer.apple.com/documentation/coregraphics/cgcontext/1454679-stroke)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextStrokeRectWithWidth(_:_:_:) | ``` func CGContextStrokeRectWithWidth(_ c: CGContext?, _ rect: CGRect, _ width: CGFloat) ``` |
| To | stroke(_:width:) | ``` func stroke(_ rect: CGRect, width width: CGFloat) ``` |

Modified [CGContext.strokeEllipse(in: CGRect)](https://developer.apple.com/documentation/coregraphics/1455774-cgcontextstrokeellipseinrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextStrokeEllipseInRect(_:_:) | ``` func CGContextStrokeEllipseInRect(_ c: CGContext?, _ rect: CGRect) ``` |
| To | strokeEllipse(in:) | ``` func strokeEllipse(in rect: CGRect) ``` |

Modified [CGContext.strokePath()](https://developer.apple.com/documentation/coregraphics/cgcontext/1454490-strokepath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextStrokePath(_:) | ``` func CGContextStrokePath(_ c: CGContext?) ``` |
| To | strokePath() | ``` func strokePath() ``` |

Modified [CGContext.synchronize()](https://developer.apple.com/documentation/coregraphics/cgcontext/1455450-synchronize)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextSynchronize(_:) | ``` func CGContextSynchronize(_ c: CGContext?) ``` |
| To | synchronize() | ``` func synchronize() ``` |

Modified [CGContext.CGContextGetTextMatrix(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1456154-cgcontextgettextmatrix)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextGetTextMatrix(_:) | ``` func CGContextGetTextMatrix(_ c: CGContext?) -> CGAffineTransform ``` |
| To | textMatrix | ``` var textMatrix: CGAffineTransform ``` |

Modified [CGContext.translateBy(x: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coregraphics/1455286-cgcontexttranslatectm)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextTranslateCTM(_:_:_:) | ``` func CGContextTranslateCTM(_ c: CGContext?, _ tx: CGFloat, _ ty: CGFloat) ``` |
| To | translateBy(x:y:) | ``` func translateBy(x tx: CGFloat, y ty: CGFloat) ``` |

Modified [CGContext.CGContextGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1455504-cgcontextgettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGContextGetTypeID() | ``` func CGContextGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGContext.CGContextGetUserSpaceToDeviceSpaceTransform(_: CGContext?) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1455677-cgcontextgetuserspacetodevicespa)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGContextGetUserSpaceToDeviceSpaceTransform(_:) | ``` func CGContextGetUserSpaceToDeviceSpaceTransform(_ c: CGContext?) -> CGAffineTransform ``` | -- |
| To | userSpaceToDeviceSpaceTransform | ``` var userSpaceToDeviceSpaceTransform: CGAffineTransform { get } ``` | yes |

Modified [CGContext.CGBitmapContextGetWidth(_: CGContext?) -> Int](https://developer.apple.com/documentation/coregraphics/cgcontext/1455607-width)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGBitmapContextGetWidth(_:) | ``` func CGBitmapContextGetWidth(_ context: CGContext?) -> Int ``` | -- |
| To | width | ``` var width: Int { get } ``` | yes |

Modified [CGDataConsumer](https://developer.apple.com/documentation/coregraphics/cgdataconsumerref)

|  | Declaration |
| --- | --- |
| From | ``` class CGDataConsumer { } ``` |
| To | ``` class CGDataConsumer {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, cbks cbks: UnsafePointer<CGDataConsumerCallbacks>)     init?(url url: CFURL)     init?(data data: CFMutableData) } extension CGDataConsumer {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, cbks cbks: UnsafePointer<CGDataConsumerCallbacks>)     init?(url url: CFURL)     init?(data data: CFMutableData) } ``` |

Modified [CGDataConsumer.init(data: CFMutableData)](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/1456292-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataConsumerCreateWithCFData(_:) | ``` func CGDataConsumerCreateWithCFData(_ data: CFMutableData?) -> CGDataConsumer? ``` |
| To | init(data:) | ``` init?(data data: CFMutableData) ``` |

Modified [CGDataConsumer.init(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](https://developer.apple.com/documentation/coregraphics/1456428-cgdataconsumercreate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataConsumerCreate(_:_:) | ``` func CGDataConsumerCreate(_ info: UnsafeMutablePointer<Void>, _ cbks: UnsafePointer<CGDataConsumerCallbacks>) -> CGDataConsumer? ``` |
| To | init(info:cbks:) | ``` init?(info info: UnsafeMutableRawPointer?, cbks cbks: UnsafePointer<CGDataConsumerCallbacks>) ``` |

Modified [CGDataConsumer.init(url: CFURL)](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/1454474-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataConsumerCreateWithURL(_:) | ``` func CGDataConsumerCreateWithURL(_ url: CFURL?) -> CGDataConsumer? ``` |
| To | init(url:) | ``` init?(url url: CFURL) ``` |

Modified [CGDataConsumer.CGDataConsumerGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1455226-cgdataconsumergettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataConsumerGetTypeID() | ``` func CGDataConsumerGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGDataConsumerCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataConsumerCallbacks {     var putBytes: CGDataConsumerPutBytesCallback?     var releaseConsumer: CGDataConsumerReleaseInfoCallback?     init()     init(putBytes putBytes: CGDataConsumerPutBytesCallback?, releaseConsumer releaseConsumer: CGDataConsumerReleaseInfoCallback?) } ``` |
| To | ``` struct CGDataConsumerCallbacks {     var putBytes: CoreGraphics.CGDataConsumerPutBytesCallback?     var releaseConsumer: CoreGraphics.CGDataConsumerReleaseInfoCallback?     init()     init(putBytes putBytes: CoreGraphics.CGDataConsumerPutBytesCallback?, releaseConsumer releaseConsumer: CoreGraphics.CGDataConsumerReleaseInfoCallback?) } ``` |

Modified [CGDataConsumerCallbacks.putBytes](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1455040-putbytes)

|  | Declaration |
| --- | --- |
| From | ``` var putBytes: CGDataConsumerPutBytesCallback? ``` |
| To | ``` var putBytes: CoreGraphics.CGDataConsumerPutBytesCallback? ``` |

Modified [CGDataConsumerCallbacks.releaseConsumer](https://developer.apple.com/documentation/coregraphics/cgdataconsumercallbacks/1454472-releaseconsumer)

|  | Declaration |
| --- | --- |
| From | ``` var releaseConsumer: CGDataConsumerReleaseInfoCallback? ``` |
| To | ``` var releaseConsumer: CoreGraphics.CGDataConsumerReleaseInfoCallback? ``` |

Modified [CGDataProvider](https://developer.apple.com/documentation/coregraphics/cgdataprovider)

|  | Declaration |
| --- | --- |
| From | ``` class CGDataProvider { } ``` |
| To | ``` class CGDataProvider {     class var typeID: CFTypeID { get }     init?(sequentialInfo info: UnsafeMutableRawPointer?, callbacks callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)     init?(directInfo info: UnsafeMutableRawPointer?, size size: off_t, callbacks callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)     init?(dataInfo info: UnsafeMutableRawPointer?, data data: UnsafeRawPointer, size size: Int, releaseData releaseData: CoreGraphics.CGDataProviderReleaseDataCallback)     init?(data data: CFData)     init?(url url: CFURL)     init?(filename filename: UnsafePointer<Int8>)     var data: CFData? { get } } extension CGDataProvider {     class var typeID: CFTypeID { get }     init?(sequentialInfo info: UnsafeMutableRawPointer?, callbacks callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)     init?(directInfo info: UnsafeMutableRawPointer?, size size: off_t, callbacks callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)     init?(dataInfo info: UnsafeMutableRawPointer?, data data: UnsafeRawPointer, size size: Int, releaseData releaseData: CoreGraphics.CGDataProviderReleaseDataCallback)     init?(data data: CFData)     init?(url url: CFURL)     init?(filename filename: UnsafePointer<Int8>)     var data: CFData? { get } } ``` |

Modified [CGDataProvider.CGDataProviderCopyData(_: CGDataProvider?) -> CFData?](https://developer.apple.com/documentation/coregraphics/1408309-cgdataprovidercopydata)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGDataProviderCopyData(_:) | ``` func CGDataProviderCopyData(_ provider: CGDataProvider?) -> CFData? ``` | tvOS 9.0 | -- |
| To | data | ``` var data: CFData? { get } ``` | tvOS 10.0 | yes |

Modified [CGDataProvider.init(data: CFData)](https://developer.apple.com/documentation/coregraphics/1408284-cgdataprovidercreatewithcfdata)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateWithCFData(_:) | ``` func CGDataProviderCreateWithCFData(_ data: CFData?) -> CGDataProvider? ``` |
| To | init(data:) | ``` init?(data data: CFData) ``` |

Modified [CGDataProvider.init(dataInfo: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CoreGraphics.CGDataProviderReleaseDataCallback)](https://developer.apple.com/documentation/coregraphics/1408288-cgdataprovidercreatewithdata)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateWithData(_:_:_:_:) | ``` func CGDataProviderCreateWithData(_ info: UnsafeMutablePointer<Void>, _ data: UnsafePointer<Void>, _ size: Int, _ releaseData: CGDataProviderReleaseDataCallback?) -> CGDataProvider? ``` |
| To | init(dataInfo:data:size:releaseData:) | ``` init?(dataInfo info: UnsafeMutableRawPointer?, data data: UnsafeRawPointer, size size: Int, releaseData releaseData: CoreGraphics.CGDataProviderReleaseDataCallback) ``` |

Modified [CGDataProvider.init(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408282-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateDirect(_:_:_:) | ``` func CGDataProviderCreateDirect(_ info: UnsafeMutablePointer<Void>, _ size: off_t, _ callbacks: UnsafePointer<CGDataProviderDirectCallbacks>) -> CGDataProvider? ``` |
| To | init(directInfo:size:callbacks:) | ``` init?(directInfo info: UnsafeMutableRawPointer?, size size: off_t, callbacks callbacks: UnsafePointer<CGDataProviderDirectCallbacks>) ``` |

Modified [CGDataProvider.init(filename: UnsafePointer<Int8>)](https://developer.apple.com/documentation/coregraphics/1408294-cgdataprovidercreatewithfilename)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateWithFilename(_:) | ``` func CGDataProviderCreateWithFilename(_ filename: UnsafePointer<Int8>) -> CGDataProvider? ``` |
| To | init(filename:) | ``` init?(filename filename: UnsafePointer<Int8>) ``` |

Modified [CGDataProvider.init(sequentialInfo: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)](https://developer.apple.com/documentation/coregraphics/1408291-cgdataprovidercreatesequential)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateSequential(_:_:) | ``` func CGDataProviderCreateSequential(_ info: UnsafeMutablePointer<Void>, _ callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>) -> CGDataProvider? ``` |
| To | init(sequentialInfo:callbacks:) | ``` init?(sequentialInfo info: UnsafeMutableRawPointer?, callbacks callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>) ``` |

Modified [CGDataProvider.init(url: CFURL)](https://developer.apple.com/documentation/coregraphics/1408327-cgdataprovidercreatewithurl)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderCreateWithURL(_:) | ``` func CGDataProviderCreateWithURL(_ url: CFURL?) -> CGDataProvider? ``` |
| To | init(url:) | ``` init?(url url: CFURL) ``` |

Modified [CGDataProvider.CGDataProviderGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgdataprovider/1408290-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGDataProviderGetTypeID() | ``` func CGDataProviderGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGDataProviderDirectCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CGDataProviderGetBytePointerCallback?     var releaseBytePointer: CGDataProviderReleaseBytePointerCallback?     var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?     var releaseInfo: CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytePointer getBytePointer: CGDataProviderGetBytePointerCallback?, releaseBytePointer releaseBytePointer: CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback?) } ``` |
| To | ``` struct CGDataProviderDirectCallbacks {     var version: UInt32     var getBytePointer: CoreGraphics.CGDataProviderGetBytePointerCallback?     var releaseBytePointer: CoreGraphics.CGDataProviderReleaseBytePointerCallback?     var getBytesAtPosition: CoreGraphics.CGDataProviderGetBytesAtPositionCallback?     var releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytePointer getBytePointer: CoreGraphics.CGDataProviderGetBytePointerCallback?, releaseBytePointer releaseBytePointer: CoreGraphics.CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition getBytesAtPosition: CoreGraphics.CGDataProviderGetBytesAtPositionCallback?, releaseInfo releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?) } ``` |

Modified [CGDataProviderDirectCallbacks.getBytePointer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408292-getbytepointer)

|  | Declaration |
| --- | --- |
| From | ``` var getBytePointer: CGDataProviderGetBytePointerCallback? ``` |
| To | ``` var getBytePointer: CoreGraphics.CGDataProviderGetBytePointerCallback? ``` |

Modified [CGDataProviderDirectCallbacks.getBytesAtPosition](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408298-getbytesatposition)

|  | Declaration |
| --- | --- |
| From | ``` var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback? ``` |
| To | ``` var getBytesAtPosition: CoreGraphics.CGDataProviderGetBytesAtPositionCallback? ``` |

Modified [CGDataProviderDirectCallbacks.releaseBytePointer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408302-releasebytepointer)

|  | Declaration |
| --- | --- |
| From | ``` var releaseBytePointer: CGDataProviderReleaseBytePointerCallback? ``` |
| To | ``` var releaseBytePointer: CoreGraphics.CGDataProviderReleaseBytePointerCallback? ``` |

Modified [CGDataProviderDirectCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks/1408286-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGDataProviderReleaseInfoCallback? ``` |
| To | ``` var releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback? ``` |

Modified [CGDataProviderSequentialCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CGDataProviderGetBytesCallback?     var skipForward: CGDataProviderSkipForwardCallback?     var rewind: CGDataProviderRewindCallback?     var releaseInfo: CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytes getBytes: CGDataProviderGetBytesCallback?, skipForward skipForward: CGDataProviderSkipForwardCallback?, rewind rewind: CGDataProviderRewindCallback?, releaseInfo releaseInfo: CGDataProviderReleaseInfoCallback?) } ``` |
| To | ``` struct CGDataProviderSequentialCallbacks {     var version: UInt32     var getBytes: CoreGraphics.CGDataProviderGetBytesCallback?     var skipForward: CoreGraphics.CGDataProviderSkipForwardCallback?     var rewind: CoreGraphics.CGDataProviderRewindCallback?     var releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?     init()     init(version version: UInt32, getBytes getBytes: CoreGraphics.CGDataProviderGetBytesCallback?, skipForward skipForward: CoreGraphics.CGDataProviderSkipForwardCallback?, rewind rewind: CoreGraphics.CGDataProviderRewindCallback?, releaseInfo releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback?) } ``` |

Modified [CGDataProviderSequentialCallbacks.getBytes](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408274-getbytes)

|  | Declaration |
| --- | --- |
| From | ``` var getBytes: CGDataProviderGetBytesCallback? ``` |
| To | ``` var getBytes: CoreGraphics.CGDataProviderGetBytesCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408306-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGDataProviderReleaseInfoCallback? ``` |
| To | ``` var releaseInfo: CoreGraphics.CGDataProviderReleaseInfoCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.rewind](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408300-rewind)

|  | Declaration |
| --- | --- |
| From | ``` var rewind: CGDataProviderRewindCallback? ``` |
| To | ``` var rewind: CoreGraphics.CGDataProviderRewindCallback? ``` |

Modified [CGDataProviderSequentialCallbacks.skipForward](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks/1408272-skipforward)

|  | Declaration |
| --- | --- |
| From | ``` var skipForward: CGDataProviderSkipForwardCallback? ``` |
| To | ``` var skipForward: CoreGraphics.CGDataProviderSkipForwardCallback? ``` |

Modified [CGError [enum]](https://developer.apple.com/documentation/coregraphics/cgerror)

|  | Declaration |
| --- | --- |
| From | ``` enum CGError : Int32 {     case Success     case Failure     case IllegalArgument     case InvalidConnection     case InvalidContext     case CannotComplete     case NotImplemented     case RangeCheck     case TypeCheck     case InvalidOperation     case NoneAvailable } ``` |
| To | ``` enum CGError : Int32 {     case success     case failure     case illegalArgument     case invalidConnection     case invalidContext     case cannotComplete     case notImplemented     case rangeCheck     case typeCheck     case invalidOperation     case noneAvailable } ``` |

Modified [CGError.cannotComplete](https://developer.apple.com/documentation/coregraphics/cgerror/cannotcomplete)

|  | Declaration |
| --- | --- |
| From | ``` case CannotComplete ``` |
| To | ``` case cannotComplete ``` |

Modified [CGError.failure](https://developer.apple.com/documentation/coregraphics/cgerror/failure)

|  | Declaration |
| --- | --- |
| From | ``` case Failure ``` |
| To | ``` case failure ``` |

Modified [CGError.illegalArgument](https://developer.apple.com/documentation/coregraphics/cgerror/illegalargument)

|  | Declaration |
| --- | --- |
| From | ``` case IllegalArgument ``` |
| To | ``` case illegalArgument ``` |

Modified [CGError.invalidConnection](https://developer.apple.com/documentation/coregraphics/cgerror/invalidconnection)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidConnection ``` |
| To | ``` case invalidConnection ``` |

Modified [CGError.invalidContext](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorinvalidcontext)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidContext ``` |
| To | ``` case invalidContext ``` |

Modified [CGError.invalidOperation](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorinvalidoperation)

|  | Declaration |
| --- | --- |
| From | ``` case InvalidOperation ``` |
| To | ``` case invalidOperation ``` |

Modified [CGError.noneAvailable](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrornoneavailable)

|  | Declaration |
| --- | --- |
| From | ``` case NoneAvailable ``` |
| To | ``` case noneAvailable ``` |

Modified [CGError.notImplemented](https://developer.apple.com/documentation/coregraphics/cgerror/notimplemented)

|  | Declaration |
| --- | --- |
| From | ``` case NotImplemented ``` |
| To | ``` case notImplemented ``` |

Modified [CGError.rangeCheck](https://developer.apple.com/documentation/coregraphics/cgerror/rangecheck)

|  | Declaration |
| --- | --- |
| From | ``` case RangeCheck ``` |
| To | ``` case rangeCheck ``` |

Modified [CGError.success](https://developer.apple.com/documentation/coregraphics/cgerror/kcgerrorsuccess)

|  | Declaration |
| --- | --- |
| From | ``` case Success ``` |
| To | ``` case success ``` |

Modified [CGError.typeCheck](https://developer.apple.com/documentation/coregraphics/cgerror/typecheck)

|  | Declaration |
| --- | --- |
| From | ``` case TypeCheck ``` |
| To | ``` case typeCheck ``` |

Modified [CGFloat [struct]](https://developer.apple.com/documentation/coregraphics/cgfloat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } extension CGFloat : FloatingPointType {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: CGFloat { get }     static var NaN: CGFloat { get }     static var quietNaN: CGFloat { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get }     var floatingPointClass: FloatingPointClassification { get } } extension CGFloat {     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : _Reflectable { } extension CGFloat : CustomStringConvertible {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : FloatLiteralConvertible {     init(floatLiteral value: NativeType) } extension CGFloat : IntegerLiteralConvertible {     init(integerLiteral value: Int) } extension CGFloat : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat } extension CGFloat : Equatable { } extension CGFloat : Comparable { } extension CGFloat : Strideable {     func distanceTo(_ other: CGFloat) -> CGFloat     func advancedBy(_ amount: CGFloat) -> CGFloat } extension CGFloat : _CVarArgPassedAsDouble, _CVarArgAlignedType { } extension CGFloat : _ObjectiveCBridgeable {     init(_ number: NSNumber) } ``` | AbsoluteValuable, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |
| To | ``` struct CGFloat {     typealias NativeType = Double     init()     init(_ value: Float)     init(_ value: Double)     init(_ value: CGFloat)     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     var native: CGFloat.NativeType     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : BinaryFloatingPoint {     typealias RawSignificand = UInt     typealias Exponent = Int     static var exponentBitCount: Int { get }     static var significandBitCount: Int { get }     var bitPattern: UInt { get }     init(bitPattern bitPattern: UInt)     var sign: FloatingPointSign { get }     var exponentBitPattern: UInt { get }     var significandBitPattern: UInt { get }     init(sign sign: FloatingPointSign, exponentBitPattern exponentBitPattern: UInt, significandBitPattern significandBitPattern: UInt)     init(nan payload: CGFloat.RawSignificand, signaling signaling: Bool)     static var infinity: CGFloat { get }     static var nan: CGFloat { get }     static var signalingNaN: CGFloat { get }     static var quietNaN: CGFloat { get }     static var greatestFiniteMagnitude: CGFloat { get }     static var pi: CGFloat { get }     var ulp: CGFloat { get }     static var leastNormalMagnitude: CGFloat { get }     static var leastNonzeroMagnitude: CGFloat { get }     var exponent: Int { get }     var significand: CGFloat { get }     init(sign sign: FloatingPointSign, exponent exponent: Int, significand significand: CGFloat)     mutating func round(_ rule: FloatingPointRoundingRule)     var nextUp: CGFloat { get }     static func abs(_ x: CGFloat) -> CGFloat     mutating func negate()     mutating func add(_ other: CGFloat)     mutating func subtract(_ other: CGFloat)     mutating func multiply(by other: CGFloat)     mutating func divide(by other: CGFloat)     mutating func formTruncatingRemainder(dividingBy other: CGFloat)     mutating func formRemainder(dividingBy other: CGFloat)     mutating func formSquareRoot()     mutating func addProduct(_ lhs: CGFloat, _ rhs: CGFloat)     func isEqual(to other: CGFloat) -> Bool     func isLess(than other: CGFloat) -> Bool     func isLessThanOrEqualTo(_ other: CGFloat) -> Bool     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignalingNaN: Bool { get }     var isSignaling: Bool { get }     var isCanonical: Bool { get }     var floatingPointClass: FloatingPointClassification { get }     var binade: CGFloat { get }     var significandWidth: Int { get }     init(floatLiteral value: CGFloat.NativeType)     init(integerLiteral value: Int) } extension CGFloat : CustomReflectable {     var customMirror: Mirror { get } } extension CGFloat : CustomStringConvertible {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : Strideable {     func distance(to other: CGFloat) -> CGFloat     func advanced(by amount: CGFloat) -> CGFloat } extension CGFloat {     init(_ number: NSNumber) } ``` | BinaryFloatingPoint, CustomReflectable, CustomStringConvertible, Hashable, Strideable |

Modified CGFloat.abs(_: CGFloat) -> CGFloat [static]

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat ``` |
| To | ``` static func abs(_ x: CGFloat) -> CGFloat ``` |

Modified [CGFloat.init(floatLiteral: CGFloat.NativeType)](https://developer.apple.com/documentation/coregraphics/cgfloat/1455662-init)

|  | Declaration |
| --- | --- |
| From | ``` init(floatLiteral value: NativeType) ``` |
| To | ``` init(floatLiteral value: CGFloat.NativeType) ``` |

Modified [CGFloat.native](https://developer.apple.com/documentation/coregraphics/cgfloat/1455813-native)

|  | Declaration |
| --- | --- |
| From | ``` var native: NativeType ``` |
| To | ``` var native: CGFloat.NativeType ``` |

Modified [CGFont](https://developer.apple.com/documentation/coregraphics/cgfontref)

|  | Declaration |
| --- | --- |
| From | ``` class CGFont { } ``` |
| To | ``` class CGFont {     class var typeID: CFTypeID { get }     init?(platformFontPlatformFontReference platformFontReference: UnsafeMutableRawPointer)      init(_ provider: CGDataProvider)      init?(_ name: CFString)     func copy(withVariations variations: CFDictionary?) -> CGFont?     var numberOfGlyphs: Int { get }     var unitsPerEm: Int32 { get }     var postScriptName: CFString? { get }     var fullName: CFString? { get }     var ascent: Int32 { get }     var descent: Int32 { get }     var leading: Int32 { get }     var capHeight: Int32 { get }     var xHeight: Int32 { get }     var fontBBox: CGRect { get }     var italicAngle: CGFloat { get }     var stemV: CGFloat { get }     var variationAxes: CFArray? { get }     var variations: CFDictionary? { get }     func getGlyphAdvances(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, advances advances: UnsafeMutablePointer<Int32>) -> Bool     func getGlyphBBoxes(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, bboxes bboxes: UnsafeMutablePointer<CGRect>) -> Bool     func getGlyphWithGlyphName(name name: CFString) -> CGGlyph     func name(for glyph: CGGlyph) -> CFString?     func canCreatePostScriptSubset(_ format: CGFontPostScriptFormat) -> Bool     func createPostScriptSubset(subsetName subsetName: CFString, format format: CGFontPostScriptFormat, glyphs glyphs: UnsafePointer<CGGlyph>?, count count: Int, encoding encoding: UnsafePointer<CGGlyph>!) -> CFData?     func createPostScriptEncoding(encoding encoding: UnsafePointer<CGGlyph>!) -> CFData?     var tableTags: CFArray? { get }     func table(for tag: UInt32) -> CFData?     class let variationAxisName: CFString     class let variationAxisMinValue: CFString     class let variationAxisMaxValue: CFString     class let variationAxisDefaultValue: CFString } extension CGFont {     class var typeID: CFTypeID { get }     init?(platformFontPlatformFontReference platformFontReference: UnsafeMutableRawPointer)      init(_ provider: CGDataProvider)      init?(_ name: CFString)     func copy(withVariations variations: CFDictionary?) -> CGFont?     var numberOfGlyphs: Int { get }     var unitsPerEm: Int32 { get }     var postScriptName: CFString? { get }     var fullName: CFString? { get }     var ascent: Int32 { get }     var descent: Int32 { get }     var leading: Int32 { get }     var capHeight: Int32 { get }     var xHeight: Int32 { get }     var fontBBox: CGRect { get }     var italicAngle: CGFloat { get }     var stemV: CGFloat { get }     var variationAxes: CFArray? { get }     var variations: CFDictionary? { get }     func getGlyphAdvances(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, advances advances: UnsafeMutablePointer<Int32>) -> Bool     func getGlyphBBoxes(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, bboxes bboxes: UnsafeMutablePointer<CGRect>) -> Bool     func getGlyphWithGlyphName(name name: CFString) -> CGGlyph     func name(for glyph: CGGlyph) -> CFString?     func canCreatePostScriptSubset(_ format: CGFontPostScriptFormat) -> Bool     func createPostScriptSubset(subsetName subsetName: CFString, format format: CGFontPostScriptFormat, glyphs glyphs: UnsafePointer<CGGlyph>?, count count: Int, encoding encoding: UnsafePointer<CGGlyph>!) -> CFData?     func createPostScriptEncoding(encoding encoding: UnsafePointer<CGGlyph>!) -> CFData?     var tableTags: CFArray? { get }     func table(for tag: UInt32) -> CFData?     class let variationAxisName: CFString     class let variationAxisMinValue: CFString     class let variationAxisMaxValue: CFString     class let variationAxisDefaultValue: CFString } ``` |

Modified [CGFont.CGFontGetAscent(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/cgfont/1396359-ascent)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetAscent(_:) | ``` func CGFontGetAscent(_ font: CGFont?) -> Int32 ``` | -- |
| To | ascent | ``` var ascent: Int32 { get } ``` | yes |

Modified [CGFont.canCreatePostScriptSubset(_: CGFontPostScriptFormat) -> Bool](https://developer.apple.com/documentation/coregraphics/cgfont/1396365-cancreatepostscriptsubset)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCanCreatePostScriptSubset(_:_:) | ``` func CGFontCanCreatePostScriptSubset(_ font: CGFont?, _ format: CGFontPostScriptFormat) -> Bool ``` |
| To | canCreatePostScriptSubset(_:) | ``` func canCreatePostScriptSubset(_ format: CGFontPostScriptFormat) -> Bool ``` |

Modified [CGFont.CGFontGetCapHeight(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/cgfont/1396338-capheight)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetCapHeight(_:) | ``` func CGFontGetCapHeight(_ font: CGFont?) -> Int32 ``` | -- |
| To | capHeight | ``` var capHeight: Int32 { get } ``` | yes |

Modified [CGFont.copy(withVariations: CFDictionary?) -> CGFont?](https://developer.apple.com/documentation/coregraphics/cgfont/1396373-copy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGFontCreateCopyWithVariations(_:_:) | ``` func CGFontCreateCopyWithVariations(_ font: CGFont?, _ variations: CFDictionary?) -> CGFont? ``` | tvOS 9.0 |
| To | copy(withVariations:) | ``` func copy(withVariations variations: CFDictionary?) -> CGFont? ``` | tvOS 10.0 |

Modified [CGFont.createPostScriptEncoding(encoding: UnsafePointer<CGGlyph>!) -> CFData?](https://developer.apple.com/documentation/coregraphics/1396348-cgfontcreatepostscriptencoding)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCreatePostScriptEncoding(_:_:) | ``` func CGFontCreatePostScriptEncoding(_ font: CGFont?, _ encoding: UnsafePointer<CGGlyph>) -> CFData? ``` |
| To | createPostScriptEncoding(encoding:) | ``` func createPostScriptEncoding(encoding encoding: UnsafePointer<CGGlyph>!) -> CFData? ``` |

Modified [CGFont.createPostScriptSubset(subsetName: CFString, format: CGFontPostScriptFormat, glyphs: UnsafePointer<CGGlyph>?, count: Int, encoding: UnsafePointer<CGGlyph>!) -> CFData?](https://developer.apple.com/documentation/coregraphics/1396324-cgfontcreatepostscriptsubset)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCreatePostScriptSubset(_:_:_:_:_:_:) | ``` func CGFontCreatePostScriptSubset(_ font: CGFont?, _ subsetName: CFString?, _ format: CGFontPostScriptFormat, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ encoding: UnsafePointer<CGGlyph>) -> CFData? ``` |
| To | createPostScriptSubset(subsetName:format:glyphs:count:encoding:) | ``` func createPostScriptSubset(subsetName subsetName: CFString, format format: CGFontPostScriptFormat, glyphs glyphs: UnsafePointer<CGGlyph>?, count count: Int, encoding encoding: UnsafePointer<CGGlyph>!) -> CFData? ``` |

Modified [CGFont.CGFontGetDescent(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396351-cgfontgetdescent)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetDescent(_:) | ``` func CGFontGetDescent(_ font: CGFont?) -> Int32 ``` | -- |
| To | descent | ``` var descent: Int32 { get } ``` | yes |

Modified [CGFont.CGFontGetFontBBox(_: CGFont?) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgfont/1396353-fontbbox)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetFontBBox(_:) | ``` func CGFontGetFontBBox(_ font: CGFont?) -> CGRect ``` | -- |
| To | fontBBox | ``` var fontBBox: CGRect { get } ``` | yes |

Modified [CGFont.CGFontCopyFullName(_: CGFont?) -> CFString?](https://developer.apple.com/documentation/coregraphics/cgfont/1396357-fullname)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGFontCopyFullName(_:) | ``` func CGFontCopyFullName(_ font: CGFont?) -> CFString? ``` | tvOS 9.0 | -- |
| To | fullName | ``` var fullName: CFString? { get } ``` | tvOS 10.0 | yes |

Modified [CGFont.getGlyphAdvances(glyphs: UnsafePointer<CGGlyph>, count: Int, advances: UnsafeMutablePointer<Int32>) -> Bool](https://developer.apple.com/documentation/coregraphics/cgfont/1396332-getglyphadvances)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontGetGlyphAdvances(_:_:_:_:) | ``` func CGFontGetGlyphAdvances(_ font: CGFont?, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ advances: UnsafeMutablePointer<Int32>) -> Bool ``` |
| To | getGlyphAdvances(glyphs:count:advances:) | ``` func getGlyphAdvances(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, advances advances: UnsafeMutablePointer<Int32>) -> Bool ``` |

Modified [CGFont.getGlyphBBoxes(glyphs: UnsafePointer<CGGlyph>, count: Int, bboxes: UnsafeMutablePointer<CGRect>) -> Bool](https://developer.apple.com/documentation/coregraphics/1396342-cgfontgetglyphbboxes)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontGetGlyphBBoxes(_:_:_:_:) | ``` func CGFontGetGlyphBBoxes(_ font: CGFont?, _ glyphs: UnsafePointer<CGGlyph>, _ count: Int, _ bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | getGlyphBBoxes(glyphs:count:bboxes:) | ``` func getGlyphBBoxes(glyphs glyphs: UnsafePointer<CGGlyph>, count count: Int, bboxes bboxes: UnsafeMutablePointer<CGRect>) -> Bool ``` |

Modified [CGFont.getGlyphWithGlyphName(name: CFString) -> CGGlyph](https://developer.apple.com/documentation/coregraphics/cgfont/1396340-getglyphwithglyphname)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontGetGlyphWithGlyphName(_:_:) | ``` func CGFontGetGlyphWithGlyphName(_ font: CGFont?, _ name: CFString?) -> CGGlyph ``` |
| To | getGlyphWithGlyphName(name:) | ``` func getGlyphWithGlyphName(name name: CFString) -> CGGlyph ``` |

Modified [CGFont.init(_: CFString)](https://developer.apple.com/documentation/coregraphics/cgfont/1396330-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCreateWithFontName(_:) | ``` func CGFontCreateWithFontName(_ name: CFString?) -> CGFont? ``` |
| To | init(_:) | ``` init?(_ name: CFString) ``` |

Modified [CGFont.init(_: CGDataProvider)](https://developer.apple.com/documentation/coregraphics/cgfont/1396367-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCreateWithDataProvider(_:) | ``` func CGFontCreateWithDataProvider(_ provider: CGDataProvider?) -> CGFont? ``` |
| To | init(_:) | ``` init(_ provider: CGDataProvider) ``` |

Modified [CGFont.CGFontGetItalicAngle(_: CGFont?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgfont/1396404-italicangle)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetItalicAngle(_:) | ``` func CGFontGetItalicAngle(_ font: CGFont?) -> CGFloat ``` | -- |
| To | italicAngle | ``` var italicAngle: CGFloat { get } ``` | yes |

Modified [CGFont.CGFontGetLeading(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396390-cgfontgetleading)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetLeading(_:) | ``` func CGFontGetLeading(_ font: CGFont?) -> Int32 ``` | -- |
| To | leading | ``` var leading: Int32 { get } ``` | yes |

Modified [CGFont.name(for: CGGlyph) -> CFString?](https://developer.apple.com/documentation/coregraphics/1396349-cgfontcopyglyphnameforglyph)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCopyGlyphNameForGlyph(_:_:) | ``` func CGFontCopyGlyphNameForGlyph(_ font: CGFont?, _ glyph: CGGlyph) -> CFString? ``` |
| To | name(for:) | ``` func name(for glyph: CGGlyph) -> CFString? ``` |

Modified [CGFont.CGFontGetNumberOfGlyphs(_: CGFont?) -> Int](https://developer.apple.com/documentation/coregraphics/1396371-cgfontgetnumberofglyphs)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetNumberOfGlyphs(_:) | ``` func CGFontGetNumberOfGlyphs(_ font: CGFont?) -> Int ``` | -- |
| To | numberOfGlyphs | ``` var numberOfGlyphs: Int { get } ``` | yes |

Modified [CGFont.CGFontCopyPostScriptName(_: CGFont?) -> CFString?](https://developer.apple.com/documentation/coregraphics/cgfont/1396346-postscriptname)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGFontCopyPostScriptName(_:) | ``` func CGFontCopyPostScriptName(_ font: CGFont?) -> CFString? ``` | tvOS 9.0 | -- |
| To | postScriptName | ``` var postScriptName: CFString? { get } ``` | tvOS 10.0 | yes |

Modified [CGFont.CGFontGetStemV(_: CGFont?) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1396380-cgfontgetstemv)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetStemV(_:) | ``` func CGFontGetStemV(_ font: CGFont?) -> CGFloat ``` | -- |
| To | stemV | ``` var stemV: CGFloat { get } ``` | yes |

Modified [CGFont.table(for: UInt32) -> CFData?](https://developer.apple.com/documentation/coregraphics/1396402-cgfontcopytablefortag)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontCopyTableForTag(_:_:) | ``` func CGFontCopyTableForTag(_ font: CGFont?, _ tag: UInt32) -> CFData? ``` |
| To | table(for:) | ``` func table(for tag: UInt32) -> CFData? ``` |

Modified [CGFont.CGFontCopyTableTags(_: CGFont?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1396392-cgfontcopytabletags)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGFontCopyTableTags(_:) | ``` func CGFontCopyTableTags(_ font: CGFont?) -> CFArray? ``` | tvOS 9.0 | -- |
| To | tableTags | ``` var tableTags: CFArray? { get } ``` | tvOS 10.0 | yes |

Modified [CGFont.CGFontGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1396369-cgfontgettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFontGetTypeID() | ``` func CGFontGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGFont.CGFontGetUnitsPerEm(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396344-cgfontgetunitsperem)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetUnitsPerEm(_:) | ``` func CGFontGetUnitsPerEm(_ font: CGFont?) -> Int32 ``` | -- |
| To | unitsPerEm | ``` var unitsPerEm: Int32 { get } ``` | yes |

Modified [CGFont.CGFontCopyVariationAxes(_: CGFont?) -> CFArray?](https://developer.apple.com/documentation/coregraphics/cgfont/1396376-variationaxes)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGFontCopyVariationAxes(_:) | ``` func CGFontCopyVariationAxes(_ font: CGFont?) -> CFArray? ``` | tvOS 9.0 | -- |
| To | variationAxes | ``` var variationAxes: CFArray? { get } ``` | tvOS 10.0 | yes |

Modified [CGFont.variationAxisDefaultValue](https://developer.apple.com/documentation/coregraphics/cgfont/1396394-variationaxisdefaultvalue)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGFontVariationAxisDefaultValue | ``` let kCGFontVariationAxisDefaultValue: CFString ``` |
| To | variationAxisDefaultValue | ``` class let variationAxisDefaultValue: CFString ``` |

Modified [CGFont.variationAxisMaxValue](https://developer.apple.com/documentation/coregraphics/kcgfontvariationaxismaxvalue)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGFontVariationAxisMaxValue | ``` let kCGFontVariationAxisMaxValue: CFString ``` |
| To | variationAxisMaxValue | ``` class let variationAxisMaxValue: CFString ``` |

Modified [CGFont.variationAxisMinValue](https://developer.apple.com/documentation/coregraphics/cgfont/1396322-variationaxisminvalue)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGFontVariationAxisMinValue | ``` let kCGFontVariationAxisMinValue: CFString ``` |
| To | variationAxisMinValue | ``` class let variationAxisMinValue: CFString ``` |

Modified [CGFont.variationAxisName](https://developer.apple.com/documentation/coregraphics/cgfont/1396398-variationaxisname)

|  | Name | Declaration |
| --- | --- | --- |
| From | kCGFontVariationAxisName | ``` let kCGFontVariationAxisName: CFString ``` |
| To | variationAxisName | ``` class let variationAxisName: CFString ``` |

Modified [CGFont.CGFontCopyVariations(_: CGFont?) -> CFDictionary?](https://developer.apple.com/documentation/coregraphics/1396355-cgfontcopyvariations)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGFontCopyVariations(_:) | ``` func CGFontCopyVariations(_ font: CGFont?) -> CFDictionary? ``` | tvOS 9.0 | -- |
| To | variations | ``` var variations: CFDictionary? { get } ``` | tvOS 10.0 | yes |

Modified [CGFont.CGFontGetXHeight(_: CGFont?) -> Int32](https://developer.apple.com/documentation/coregraphics/1396410-cgfontgetxheight)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGFontGetXHeight(_:) | ``` func CGFontGetXHeight(_ font: CGFont?) -> Int32 ``` | -- |
| To | xHeight | ``` var xHeight: Int32 { get } ``` | yes |

Modified [CGFontPostScriptFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat)

|  | Declaration |
| --- | --- |
| From | ``` enum CGFontPostScriptFormat : Int32 {     case Type1     case Type3     case Type42 } ``` |
| To | ``` enum CGFontPostScriptFormat : Int32 {     case type1     case type3     case type42 } ``` |

Modified [CGFontPostScriptFormat.type1](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/type1)

|  | Declaration |
| --- | --- |
| From | ``` case Type1 ``` |
| To | ``` case type1 ``` |

Modified [CGFontPostScriptFormat.type3](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/kcgfontpostscriptformattype3)

|  | Declaration |
| --- | --- |
| From | ``` case Type3 ``` |
| To | ``` case type3 ``` |

Modified [CGFontPostScriptFormat.type42](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat/type42)

|  | Declaration |
| --- | --- |
| From | ``` case Type42 ``` |
| To | ``` case type42 ``` |

Modified [CGFunction](https://developer.apple.com/documentation/coregraphics/cgfunction)

|  | Declaration |
| --- | --- |
| From | ``` class CGFunction { } ``` |
| To | ``` class CGFunction {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, domainDimension domainDimension: Int, domain domain: UnsafePointer<CGFloat>?, rangeDimension rangeDimension: Int, range range: UnsafePointer<CGFloat>?, callbacks callbacks: UnsafePointer<CGFunctionCallbacks>) } extension CGFunction {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, domainDimension domainDimension: Int, domain domain: UnsafePointer<CGFloat>?, rangeDimension rangeDimension: Int, range range: UnsafePointer<CGFloat>?, callbacks callbacks: UnsafePointer<CGFunctionCallbacks>) } ``` |

Modified [CGFunction.init(info: UnsafeMutableRawPointer?, domainDimension: Int, domain: UnsafePointer<CGFloat>?, rangeDimension: Int, range: UnsafePointer<CGFloat>?, callbacks: UnsafePointer<CGFunctionCallbacks>)](https://developer.apple.com/documentation/coregraphics/1390862-cgfunctioncreate)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFunctionCreate(_:_:_:_:_:_:) | ``` func CGFunctionCreate(_ info: UnsafeMutablePointer<Void>, _ domainDimension: Int, _ domain: UnsafePointer<CGFloat>, _ rangeDimension: Int, _ range: UnsafePointer<CGFloat>, _ callbacks: UnsafePointer<CGFunctionCallbacks>) -> CGFunction? ``` |
| To | init(info:domainDimension:domain:rangeDimension:range:callbacks:) | ``` init?(info info: UnsafeMutableRawPointer?, domainDimension domainDimension: Int, domain domain: UnsafePointer<CGFloat>?, rangeDimension rangeDimension: Int, range range: UnsafePointer<CGFloat>?, callbacks callbacks: UnsafePointer<CGFunctionCallbacks>) ``` |

Modified [CGFunction.CGFunctionGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgfunction/1390879-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGFunctionGetTypeID() | ``` func CGFunctionGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGFunctionCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CGFunctionEvaluateCallback?     var releaseInfo: CGFunctionReleaseInfoCallback?     init()     init(version version: UInt32, evaluate evaluate: CGFunctionEvaluateCallback?, releaseInfo releaseInfo: CGFunctionReleaseInfoCallback?) } ``` |
| To | ``` struct CGFunctionCallbacks {     var version: UInt32     var evaluate: CoreGraphics.CGFunctionEvaluateCallback?     var releaseInfo: CoreGraphics.CGFunctionReleaseInfoCallback?     init()     init(version version: UInt32, evaluate evaluate: CoreGraphics.CGFunctionEvaluateCallback?, releaseInfo releaseInfo: CoreGraphics.CGFunctionReleaseInfoCallback?) } ``` |

Modified [CGFunctionCallbacks.evaluate](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1390866-evaluate)

|  | Declaration |
| --- | --- |
| From | ``` var evaluate: CGFunctionEvaluateCallback? ``` |
| To | ``` var evaluate: CoreGraphics.CGFunctionEvaluateCallback? ``` |

Modified [CGFunctionCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/1390868-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGFunctionReleaseInfoCallback? ``` |
| To | ``` var releaseInfo: CoreGraphics.CGFunctionReleaseInfoCallback? ``` |

Modified [CGGlyphDeprecatedEnum [enum]](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum)

|  | Declaration |
| --- | --- |
| From | ``` enum CGGlyphDeprecatedEnum : Int32 {     case Min     case Max } ``` |
| To | ``` enum CGGlyphDeprecatedEnum : Int32 {     case min     case max } ``` |

Modified [CGGlyphDeprecatedEnum.max](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmax)

|  | Declaration |
| --- | --- |
| From | ``` case Max ``` |
| To | ``` case max ``` |

Modified [CGGlyphDeprecatedEnum.min](https://developer.apple.com/documentation/coregraphics/cgglyphdeprecatedenum/cgglyphmin)

|  | Declaration |
| --- | --- |
| From | ``` case Min ``` |
| To | ``` case min ``` |

Modified [CGGradient](https://developer.apple.com/documentation/coregraphics/cggradient)

|  | Declaration |
| --- | --- |
| From | ``` class CGGradient { } ``` |
| To | ``` class CGGradient {     class var typeID: CFTypeID { get }      init?(colorSpace space: CGColorSpace, colorComponents components: UnsafePointer<CGFloat>, locations locations: UnsafePointer<CGFloat>?, count count: Int)     init?(colorsSpace space: CGColorSpace?, colors colors: CFArray, locations locations: UnsafePointer<CGFloat>?) } extension CGGradient {     class var typeID: CFTypeID { get }      init?(colorSpace space: CGColorSpace, colorComponents components: UnsafePointer<CGFloat>, locations locations: UnsafePointer<CGFloat>?, count count: Int)     init?(colorsSpace space: CGColorSpace?, colors colors: CFArray, locations locations: UnsafePointer<CGFloat>?) } ``` |

Modified [CGGradient.init(colorSpace: CGColorSpace, colorComponents: UnsafePointer<CGFloat>, locations: UnsafePointer<CGFloat>?, count: Int)](https://developer.apple.com/documentation/coregraphics/cggradient/1398454-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGGradientCreateWithColorComponents(_:_:_:_:) | ``` func CGGradientCreateWithColorComponents(_ space: CGColorSpace?, _ components: UnsafePointer<CGFloat>, _ locations: UnsafePointer<CGFloat>, _ count: Int) -> CGGradient? ``` |
| To | init(colorSpace:colorComponents:locations:count:) | ``` init?(colorSpace space: CGColorSpace, colorComponents components: UnsafePointer<CGFloat>, locations locations: UnsafePointer<CGFloat>?, count count: Int) ``` |

Modified [CGGradient.init(colorsSpace: CGColorSpace?, colors: CFArray, locations: UnsafePointer<CGFloat>?)](https://developer.apple.com/documentation/coregraphics/cggradient/1398458-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGGradientCreateWithColors(_:_:_:) | ``` func CGGradientCreateWithColors(_ space: CGColorSpace?, _ colors: CFArray?, _ locations: UnsafePointer<CGFloat>) -> CGGradient? ``` |
| To | init(colorsSpace:colors:locations:) | ``` init?(colorsSpace space: CGColorSpace?, colors colors: CFArray, locations locations: UnsafePointer<CGFloat>?) ``` |

Modified [CGGradient.CGGradientGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cggradient/1398453-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGGradientGetTypeID() | ``` func CGGradientGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGGradientDrawingOptions [struct]](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGGradientDrawingOptions : OptionSetType {     init(rawValue rawValue: UInt32)     static var DrawsBeforeStartLocation: CGGradientDrawingOptions { get }     static var DrawsAfterEndLocation: CGGradientDrawingOptions { get } } ``` | OptionSetType |
| To | ``` struct CGGradientDrawingOptions : OptionSet {     init(rawValue rawValue: UInt32)     static var drawsBeforeStartLocation: CGGradientDrawingOptions { get }     static var drawsAfterEndLocation: CGGradientDrawingOptions { get }     func intersect(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions     func exclusiveOr(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions     mutating func unionInPlace(_ other: CGGradientDrawingOptions)     mutating func intersectInPlace(_ other: CGGradientDrawingOptions)     mutating func exclusiveOrInPlace(_ other: CGGradientDrawingOptions)     func isSubsetOf(_ other: CGGradientDrawingOptions) -> Bool     func isDisjointWith(_ other: CGGradientDrawingOptions) -> Bool     func isSupersetOf(_ other: CGGradientDrawingOptions) -> Bool     mutating func subtractInPlace(_ other: CGGradientDrawingOptions)     func isStrictSupersetOf(_ other: CGGradientDrawingOptions) -> Bool     func isStrictSubsetOf(_ other: CGGradientDrawingOptions) -> Bool } extension CGGradientDrawingOptions {     func union(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions     func intersection(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions     func symmetricDifference(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions } extension CGGradientDrawingOptions {     func contains(_ member: CGGradientDrawingOptions) -> Bool     mutating func insert(_ newMember: CGGradientDrawingOptions) -> (inserted: Bool, memberAfterInsert: CGGradientDrawingOptions)     mutating func remove(_ member: CGGradientDrawingOptions) -> CGGradientDrawingOptions?     mutating func update(with newMember: CGGradientDrawingOptions) -> CGGradientDrawingOptions? } extension CGGradientDrawingOptions {     convenience init()     mutating func formUnion(_ other: CGGradientDrawingOptions)     mutating func formIntersection(_ other: CGGradientDrawingOptions)     mutating func formSymmetricDifference(_ other: CGGradientDrawingOptions) } extension CGGradientDrawingOptions {     convenience init<S : Sequence where S.Iterator.Element == CGGradientDrawingOptions>(_ sequence: S)     convenience init(arrayLiteral arrayLiteral: CGGradientDrawingOptions...)     mutating func subtract(_ other: CGGradientDrawingOptions)     func isSubset(of other: CGGradientDrawingOptions) -> Bool     func isSuperset(of other: CGGradientDrawingOptions) -> Bool     func isDisjoint(with other: CGGradientDrawingOptions) -> Bool     func subtracting(_ other: CGGradientDrawingOptions) -> CGGradientDrawingOptions     var isEmpty: Bool { get }     func isStrictSuperset(of other: CGGradientDrawingOptions) -> Bool     func isStrictSubset(of other: CGGradientDrawingOptions) -> Bool } ``` | OptionSet |

Modified [CGGradientDrawingOptions.drawsAfterEndLocation](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions/kcggradientdrawsafterendlocation)

|  | Declaration |
| --- | --- |
| From | ``` static var DrawsAfterEndLocation: CGGradientDrawingOptions { get } ``` |
| To | ``` static var drawsAfterEndLocation: CGGradientDrawingOptions { get } ``` |

Modified [CGGradientDrawingOptions.drawsBeforeStartLocation](https://developer.apple.com/documentation/coregraphics/cggradientdrawingoptions/kcggradientdrawsbeforestartlocation)

|  | Declaration |
| --- | --- |
| From | ``` static var DrawsBeforeStartLocation: CGGradientDrawingOptions { get } ``` |
| To | ``` static var drawsBeforeStartLocation: CGGradientDrawingOptions { get } ``` |

Modified [CGImage](https://developer.apple.com/documentation/coregraphics/cgimage)

|  | Declaration |
| --- | --- |
| From | ``` class CGImage { } ``` |
| To | ``` class CGImage {     func copy(maskingColorComponents components: [CGFloat]) -> CGImage?     class var typeID: CFTypeID { get }     init?(width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: CGBitmapInfo, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     init?(maskWidth width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool)     func copy() -> CGImage?     init?(jpegDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     init?(pngDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     func cropping(to rect: CGRect) -> CGImage?     func masking(_ mask: CGImage) -> CGImage?     func __copy(maskingColorComponents components: UnsafePointer<CGFloat>) -> CGImage?     func copy(colorSpace space: CGColorSpace) -> CGImage?     var isMask: Bool { get }     var width: Int { get }     var height: Int { get }     var bitsPerComponent: Int { get }     var bitsPerPixel: Int { get }     var bytesPerRow: Int { get }     var colorSpace: CGColorSpace? { get }     var alphaInfo: CGImageAlphaInfo { get }     var dataProvider: CGDataProvider? { get }     var decode: UnsafePointer<CGFloat>? { get }     var shouldInterpolate: Bool { get }     var renderingIntent: CGColorRenderingIntent { get }     var bitmapInfo: CGBitmapInfo { get }     var utType: CFString? { get } } extension CGImage {     class var typeID: CFTypeID { get }     init?(width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: CGBitmapInfo, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     init?(maskWidth width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool)     func copy() -> CGImage?     init?(jpegDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     init?(pngDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent)     func cropping(to rect: CGRect) -> CGImage?     func masking(_ mask: CGImage) -> CGImage?     func __copy(maskingColorComponents components: UnsafePointer<CGFloat>) -> CGImage?     func copy(colorSpace space: CGColorSpace) -> CGImage?     var isMask: Bool { get }     var width: Int { get }     var height: Int { get }     var bitsPerComponent: Int { get }     var bitsPerPixel: Int { get }     var bytesPerRow: Int { get }     var colorSpace: CGColorSpace? { get }     var alphaInfo: CGImageAlphaInfo { get }     var dataProvider: CGDataProvider? { get }     var decode: UnsafePointer<CGFloat>? { get }     var shouldInterpolate: Bool { get }     var renderingIntent: CGColorRenderingIntent { get }     var bitmapInfo: CGBitmapInfo { get }     var utType: CFString? { get } } extension CGImage {     func copy(maskingColorComponents components: [CGFloat]) -> CGImage? } ``` |

Modified [CGImage.CGImageGetAlphaInfo(_: CGImage?) -> CGImageAlphaInfo](https://developer.apple.com/documentation/coregraphics/cgimage/1455401-alphainfo)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetAlphaInfo(_:) | ``` func CGImageGetAlphaInfo(_ image: CGImage?) -> CGImageAlphaInfo ``` | -- |
| To | alphaInfo | ``` var alphaInfo: CGImageAlphaInfo { get } ``` | yes |

Modified [CGImage.CGImageGetBitmapInfo(_: CGImage?) -> CGBitmapInfo](https://developer.apple.com/documentation/coregraphics/1454200-cgimagegetbitmapinfo)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetBitmapInfo(_:) | ``` func CGImageGetBitmapInfo(_ image: CGImage?) -> CGBitmapInfo ``` | -- |
| To | bitmapInfo | ``` var bitmapInfo: CGBitmapInfo { get } ``` | yes |

Modified [CGImage.CGImageGetBitsPerComponent(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1454980-cgimagegetbitspercomponent)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetBitsPerComponent(_:) | ``` func CGImageGetBitsPerComponent(_ image: CGImage?) -> Int ``` | -- |
| To | bitsPerComponent | ``` var bitsPerComponent: Int { get } ``` | yes |

Modified [CGImage.CGImageGetBitsPerPixel(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/1454599-cgimagegetbitsperpixel)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetBitsPerPixel(_:) | ``` func CGImageGetBitsPerPixel(_ image: CGImage?) -> Int ``` | -- |
| To | bitsPerPixel | ``` var bitsPerPixel: Int { get } ``` | yes |

Modified [CGImage.CGImageGetBytesPerRow(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/cgimage/1455425-bytesperrow)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetBytesPerRow(_:) | ``` func CGImageGetBytesPerRow(_ image: CGImage?) -> Int ``` | -- |
| To | bytesPerRow | ``` var bytesPerRow: Int { get } ``` | yes |

Modified [CGImage.CGImageGetColorSpace(_: CGImage?) -> CGColorSpace?](https://developer.apple.com/documentation/coregraphics/cgimage/1454858-colorspace)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetColorSpace(_:) | ``` func CGImageGetColorSpace(_ image: CGImage?) -> CGColorSpace? ``` | -- |
| To | colorSpace | ``` var colorSpace: CGColorSpace? { get } ``` | yes |

Modified [CGImage.copy() -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455615-cgimagecreatecopy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGImageCreateCopy(_:) | ``` func CGImageCreateCopy(_ image: CGImage?) -> CGImage? ``` | tvOS 9.0 |
| To | copy() | ``` func copy() -> CGImage? ``` | tvOS 10.0 |

Modified [CGImage.copy(colorSpace: CGColorSpace) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1455355-cgimagecreatecopywithcolorspace)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGImageCreateCopyWithColorSpace(_:_:) | ``` func CGImageCreateCopyWithColorSpace(_ image: CGImage?, _ space: CGColorSpace?) -> CGImage? ``` | tvOS 9.0 |
| To | copy(colorSpace:) | ``` func copy(colorSpace space: CGColorSpace) -> CGImage? ``` | tvOS 10.0 |

Modified [CGImage.cropping(to: CGRect) -> CGImage?](https://developer.apple.com/documentation/coregraphics/1454683-cgimagecreatewithimageinrect)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGImageCreateWithImageInRect(_:_:) | ``` func CGImageCreateWithImageInRect(_ image: CGImage?, _ rect: CGRect) -> CGImage? ``` | tvOS 9.0 |
| To | cropping(to:) | ``` func cropping(to rect: CGRect) -> CGImage? ``` | tvOS 10.0 |

Modified [CGImage.CGImageGetDataProvider(_: CGImage?) -> CGDataProvider?](https://developer.apple.com/documentation/coregraphics/1455260-cgimagegetdataprovider)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetDataProvider(_:) | ``` func CGImageGetDataProvider(_ image: CGImage?) -> CGDataProvider? ``` | -- |
| To | dataProvider | ``` var dataProvider: CGDataProvider? { get } ``` | yes |

Modified [CGImage.CGImageGetDecode(_: CGImage?) -> UnsafePointer<CGFloat>](https://developer.apple.com/documentation/coregraphics/1454575-cgimagegetdecode)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetDecode(_:) | ``` func CGImageGetDecode(_ image: CGImage?) -> UnsafePointer<CGFloat> ``` | -- |
| To | decode | ``` var decode: UnsafePointer<CGFloat>? { get } ``` | yes |

Modified [CGImage.CGImageGetHeight(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/cgimage/1455829-height)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetHeight(_:) | ``` func CGImageGetHeight(_ image: CGImage?) -> Int ``` | -- |
| To | height | ``` var height: Int { get } ``` | yes |

Modified [CGImage.init(jpegDataProviderSource: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](https://developer.apple.com/documentation/coregraphics/1454920-cgimagecreatewithjpegdataprovide)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageCreateWithJPEGDataProvider(_:_:_:_:) | ``` func CGImageCreateWithJPEGDataProvider(_ source: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |
| To | init(jpegDataProviderSource:decode:shouldInterpolate:intent:) | ``` init?(jpegDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent) ``` |

Modified [CGImage.init(maskWidth: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool)](https://developer.apple.com/documentation/coregraphics/cgimage/1455089-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageMaskCreate(_:_:_:_:_:_:_:_:) | ``` func CGImageMaskCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ provider: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool) -> CGImage? ``` |
| To | init(maskWidth:height:bitsPerComponent:bitsPerPixel:bytesPerRow:provider:decode:shouldInterpolate:) | ``` init?(maskWidth width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool) ``` |

Modified [CGImage.init(pngDataProviderSource: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](https://developer.apple.com/documentation/coregraphics/1454993-cgimagecreatewithpngdataprovider)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageCreateWithPNGDataProvider(_:_:_:_:) | ``` func CGImageCreateWithPNGDataProvider(_ source: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |
| To | init(pngDataProviderSource:decode:shouldInterpolate:intent:) | ``` init?(pngDataProviderSource source: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent) ``` |

Modified [CGImage.init(width: Int, height: Int, bitsPerComponent: Int, bitsPerPixel: Int, bytesPerRow: Int, space: CGColorSpace, bitmapInfo: CGBitmapInfo, provider: CGDataProvider, decode: UnsafePointer<CGFloat>?, shouldInterpolate: Bool, intent: CGColorRenderingIntent)](https://developer.apple.com/documentation/coregraphics/cgimage/1455149-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageCreate(_:_:_:_:_:_:_:_:_:_:_:) | ``` func CGImageCreate(_ width: Int, _ height: Int, _ bitsPerComponent: Int, _ bitsPerPixel: Int, _ bytesPerRow: Int, _ space: CGColorSpace?, _ bitmapInfo: CGBitmapInfo, _ provider: CGDataProvider?, _ decode: UnsafePointer<CGFloat>, _ shouldInterpolate: Bool, _ intent: CGColorRenderingIntent) -> CGImage? ``` |
| To | init(width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:) | ``` init?(width width: Int, height height: Int, bitsPerComponent bitsPerComponent: Int, bitsPerPixel bitsPerPixel: Int, bytesPerRow bytesPerRow: Int, space space: CGColorSpace, bitmapInfo bitmapInfo: CGBitmapInfo, provider provider: CGDataProvider, decode decode: UnsafePointer<CGFloat>?, shouldInterpolate shouldInterpolate: Bool, intent intent: CGColorRenderingIntent) ``` |

Modified [CGImage.CGImageIsMask(_: CGImage?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454229-cgimageismask)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGImageIsMask(_:) | ``` func CGImageIsMask(_ image: CGImage?) -> Bool ``` | tvOS 9.0 | -- |
| To | isMask | ``` var isMask: Bool { get } ``` | tvOS 10.0 | yes |

Modified [CGImage.masking(_: CGImage) -> CGImage?](https://developer.apple.com/documentation/coregraphics/cgimage/1456337-masking)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGImageCreateWithMask(_:_:) | ``` func CGImageCreateWithMask(_ image: CGImage?, _ mask: CGImage?) -> CGImage? ``` | tvOS 9.0 |
| To | masking(_:) | ``` func masking(_ mask: CGImage) -> CGImage? ``` | tvOS 10.0 |

Modified [CGImage.CGImageGetRenderingIntent(_: CGImage?) -> CGColorRenderingIntent](https://developer.apple.com/documentation/coregraphics/1456350-cgimagegetrenderingintent)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetRenderingIntent(_:) | ``` func CGImageGetRenderingIntent(_ image: CGImage?) -> CGColorRenderingIntent ``` | -- |
| To | renderingIntent | ``` var renderingIntent: CGColorRenderingIntent { get } ``` | yes |

Modified [CGImage.CGImageGetShouldInterpolate(_: CGImage?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgimage/1455363-shouldinterpolate)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetShouldInterpolate(_:) | ``` func CGImageGetShouldInterpolate(_ image: CGImage?) -> Bool ``` | -- |
| To | shouldInterpolate | ``` var shouldInterpolate: Bool { get } ``` | yes |

Modified [CGImage.CGImageGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgimage/1455014-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGImageGetTypeID() | ``` func CGImageGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGImage.CGImageGetUTType(_: CGImage?) -> CFString?](https://developer.apple.com/documentation/coregraphics/cgimage/1456067-uttype)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetUTType(_:) | ``` func CGImageGetUTType(_ image: CGImage?) -> CFString? ``` | -- |
| To | utType | ``` var utType: CFString? { get } ``` | yes |

Modified [CGImage.CGImageGetWidth(_: CGImage?) -> Int](https://developer.apple.com/documentation/coregraphics/cgimage/1456148-width)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGImageGetWidth(_:) | ``` func CGImageGetWidth(_ image: CGImage?) -> Int ``` | -- |
| To | width | ``` var width: Int { get } ``` | yes |

Modified [CGImageAlphaInfo [enum]](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo)

|  | Declaration |
| --- | --- |
| From | ``` enum CGImageAlphaInfo : UInt32 {     case None     case PremultipliedLast     case PremultipliedFirst     case Last     case First     case NoneSkipLast     case NoneSkipFirst     case Only } ``` |
| To | ``` enum CGImageAlphaInfo : UInt32 {     case none     case premultipliedLast     case premultipliedFirst     case last     case first     case noneSkipLast     case noneSkipFirst     case alphaOnly } ``` |

Modified [CGImageAlphaInfo.alphaOnly](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphaonly)

|  | Declaration |
| --- | --- |
| From | ``` case Only ``` |
| To | ``` case alphaOnly ``` |

Modified [CGImageAlphaInfo.first](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/first)

|  | Declaration |
| --- | --- |
| From | ``` case First ``` |
| To | ``` case first ``` |

Modified [CGImageAlphaInfo.last](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphalast)

|  | Declaration |
| --- | --- |
| From | ``` case Last ``` |
| To | ``` case last ``` |

Modified [CGImageAlphaInfo.none](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphanone)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CGImageAlphaInfo.noneSkipFirst](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/noneskipfirst)

|  | Declaration |
| --- | --- |
| From | ``` case NoneSkipFirst ``` |
| To | ``` case noneSkipFirst ``` |

Modified [CGImageAlphaInfo.noneSkipLast](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphanoneskiplast)

|  | Declaration |
| --- | --- |
| From | ``` case NoneSkipLast ``` |
| To | ``` case noneSkipLast ``` |

Modified [CGImageAlphaInfo.premultipliedFirst](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphapremultipliedfirst)

|  | Declaration |
| --- | --- |
| From | ``` case PremultipliedFirst ``` |
| To | ``` case premultipliedFirst ``` |

Modified [CGImageAlphaInfo.premultipliedLast](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo/kcgimagealphapremultipliedlast)

|  | Declaration |
| --- | --- |
| From | ``` case PremultipliedLast ``` |
| To | ``` case premultipliedLast ``` |

Modified [CGInterpolationQuality [enum]](https://developer.apple.com/documentation/coregraphics/cginterpolationquality)

|  | Declaration |
| --- | --- |
| From | ``` enum CGInterpolationQuality : Int32 {     case Default     case None     case Low     case Medium     case High } ``` |
| To | ``` enum CGInterpolationQuality : Int32 {     case `default`     case none     case low     case medium     case high } ``` |

Modified [CGInterpolationQuality.default](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/default)

|  | Declaration |
| --- | --- |
| From | ``` case Default ``` |
| To | ``` case `default` ``` |

Modified [CGInterpolationQuality.high](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/kcginterpolationhigh)

|  | Declaration |
| --- | --- |
| From | ``` case High ``` |
| To | ``` case high ``` |

Modified [CGInterpolationQuality.low](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/low)

|  | Declaration |
| --- | --- |
| From | ``` case Low ``` |
| To | ``` case low ``` |

Modified [CGInterpolationQuality.medium](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/medium)

|  | Declaration |
| --- | --- |
| From | ``` case Medium ``` |
| To | ``` case medium ``` |

Modified [CGInterpolationQuality.none](https://developer.apple.com/documentation/coregraphics/cginterpolationquality/none)

|  | Declaration |
| --- | --- |
| From | ``` case None ``` |
| To | ``` case none ``` |

Modified [CGLayer](https://developer.apple.com/documentation/coregraphics/cglayer)

|  | Declaration |
| --- | --- |
| From | ``` class CGLayer { } ``` |
| To | ``` class CGLayer {      init?(_ context: CGContext, size size: CGSize, auxiliaryInfo auxiliaryInfo: CFDictionary?)     var size: CGSize { get }     var context: CGContext? { get }     class var typeID: CFTypeID { get } } extension CGLayer {      init?(_ context: CGContext, size size: CGSize, auxiliaryInfo auxiliaryInfo: CFDictionary?)     var size: CGSize { get }     var context: CGContext? { get }     class var typeID: CFTypeID { get } } ``` |

Modified [CGLayer.CGLayerGetContext(_: CGLayer?) -> CGContext?](https://developer.apple.com/documentation/coregraphics/1450902-cglayergetcontext)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGLayerGetContext(_:) | ``` func CGLayerGetContext(_ layer: CGLayer?) -> CGContext? ``` | -- |
| To | context | ``` var context: CGContext? { get } ``` | yes |

Modified [CGLayer.init(_: CGContext, size: CGSize, auxiliaryInfo: CFDictionary?)](https://developer.apple.com/documentation/coregraphics/1450892-cglayercreatewithcontext)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGLayerCreateWithContext(_:_:_:) | ``` func CGLayerCreateWithContext(_ context: CGContext?, _ size: CGSize, _ auxiliaryInfo: CFDictionary?) -> CGLayer? ``` |
| To | init(_:size:auxiliaryInfo:) | ``` init?(_ context: CGContext, size size: CGSize, auxiliaryInfo auxiliaryInfo: CFDictionary?) ``` |

Modified [CGLayer.CGLayerGetSize(_: CGLayer?) -> CGSize](https://developer.apple.com/documentation/coregraphics/cglayer/1450890-size)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGLayerGetSize(_:) | ``` func CGLayerGetSize(_ layer: CGLayer?) -> CGSize ``` | -- |
| To | size | ``` var size: CGSize { get } ``` | yes |

Modified [CGLayer.CGLayerGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1450888-cglayergettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGLayerGetTypeID() | ``` func CGLayerGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGLineCap [enum]](https://developer.apple.com/documentation/coregraphics/cglinecap)

|  | Declaration |
| --- | --- |
| From | ``` enum CGLineCap : Int32 {     case Butt     case Round     case Square } ``` |
| To | ``` enum CGLineCap : Int32 {     case butt     case round     case square } ``` |

Modified [CGLineCap.butt](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapbutt)

|  | Declaration |
| --- | --- |
| From | ``` case Butt ``` |
| To | ``` case butt ``` |

Modified [CGLineCap.round](https://developer.apple.com/documentation/coregraphics/cglinecap/round)

|  | Declaration |
| --- | --- |
| From | ``` case Round ``` |
| To | ``` case round ``` |

Modified [CGLineCap.square](https://developer.apple.com/documentation/coregraphics/cglinecap/kcglinecapsquare)

|  | Declaration |
| --- | --- |
| From | ``` case Square ``` |
| To | ``` case square ``` |

Modified [CGLineJoin [enum]](https://developer.apple.com/documentation/coregraphics/cglinejoin)

|  | Declaration |
| --- | --- |
| From | ``` enum CGLineJoin : Int32 {     case Miter     case Round     case Bevel } ``` |
| To | ``` enum CGLineJoin : Int32 {     case miter     case round     case bevel } ``` |

Modified [CGLineJoin.bevel](https://developer.apple.com/documentation/coregraphics/cglinejoin/bevel)

|  | Declaration |
| --- | --- |
| From | ``` case Bevel ``` |
| To | ``` case bevel ``` |

Modified [CGLineJoin.miter](https://developer.apple.com/documentation/coregraphics/cglinejoin/miter)

|  | Declaration |
| --- | --- |
| From | ``` case Miter ``` |
| To | ``` case miter ``` |

Modified [CGLineJoin.round](https://developer.apple.com/documentation/coregraphics/cglinejoin/round)

|  | Declaration |
| --- | --- |
| From | ``` case Round ``` |
| To | ``` case round ``` |

Modified [CGMutablePath](https://developer.apple.com/documentation/coregraphics/cgmutablepathref)

|  | Declaration |
| --- | --- |
| From | ``` class CGMutablePath { } ``` |
| To | ``` class CGMutablePath {     func addRoundedRect(in rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat, transform transform: CGAffineTransform = default)     func move(to point: CGPoint, transform transform: CGAffineTransform = default)     func addLine(to point: CGPoint, transform transform: CGAffineTransform = default)     func addQuadCurve(to end: CGPoint, control control: CGPoint, transform transform: CGAffineTransform = default)     func addCurve(to end: CGPoint, control1 control1: CGPoint, control2 control2: CGPoint, transform transform: CGAffineTransform = default)     func addRect(_ rect: CGRect, transform transform: CGAffineTransform = default)     func addRects(_ rects: [CGRect], transform transform: CGAffineTransform = default)     func addLines(between points: [CGPoint], transform transform: CGAffineTransform = default)     func addEllipse(in rect: CGRect, transform transform: CGAffineTransform = default)     func addRelativeArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, delta delta: CGFloat, transform transform: CGAffineTransform = default)     func addArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool, transform transform: CGAffineTransform = default)     func addArc(tangent1End tangent1End: CGPoint, tangent2End tangent2End: CGPoint, radius radius: CGFloat, transform transform: CGAffineTransform = default)     func addPath(_ path: CGPath, transform transform: CGAffineTransform = default)     init()     func __addRoundedRect(transform transform: UnsafePointer<CGAffineTransform>?, rect rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat)     func __moveTo(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat)     func __addLineTo(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat)     func __addQuadCurve(transform m: UnsafePointer<CGAffineTransform>?, cpx cpx: CGFloat, cpy cpy: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func __addCurve(transform m: UnsafePointer<CGAffineTransform>?, cp1x cp1x: CGFloat, cp1y cp1y: CGFloat, cp2x cp2x: CGFloat, cp2y cp2y: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func closeSubpath()     func __addRect(transform m: UnsafePointer<CGAffineTransform>?, rect rect: CGRect)     func __addRects(transform m: UnsafePointer<CGAffineTransform>?, rects rects: UnsafePointer<CGRect>?, count count: Int)     func __addLines(transform m: UnsafePointer<CGAffineTransform>?, between points: UnsafePointer<CGPoint>?, count count: Int)     func __addEllipse(transform m: UnsafePointer<CGAffineTransform>?, rect rect: CGRect)     func __addRelativeArc(transform matrix: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, delta delta: CGFloat)     func __addArc(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func __addArc(transform m: UnsafePointer<CGAffineTransform>?, x1 x1: CGFloat, y1 y1: CGFloat, x2 x2: CGFloat, y2 y2: CGFloat, radius radius: CGFloat)     func __addPath(transform m: UnsafePointer<CGAffineTransform>?, path path2: CGPath) } extension CGMutablePath {     init()     func __addRoundedRect(transform transform: UnsafePointer<CGAffineTransform>?, rect rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat)     func __moveTo(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat)     func __addLineTo(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat)     func __addQuadCurve(transform m: UnsafePointer<CGAffineTransform>?, cpx cpx: CGFloat, cpy cpy: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func __addCurve(transform m: UnsafePointer<CGAffineTransform>?, cp1x cp1x: CGFloat, cp1y cp1y: CGFloat, cp2x cp2x: CGFloat, cp2y cp2y: CGFloat, endingAtX x: CGFloat, y y: CGFloat)     func closeSubpath()     func __addRect(transform m: UnsafePointer<CGAffineTransform>?, rect rect: CGRect)     func __addRects(transform m: UnsafePointer<CGAffineTransform>?, rects rects: UnsafePointer<CGRect>?, count count: Int)     func __addLines(transform m: UnsafePointer<CGAffineTransform>?, between points: UnsafePointer<CGPoint>?, count count: Int)     func __addEllipse(transform m: UnsafePointer<CGAffineTransform>?, rect rect: CGRect)     func __addRelativeArc(transform matrix: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, delta delta: CGFloat)     func __addArc(transform m: UnsafePointer<CGAffineTransform>?, x x: CGFloat, y y: CGFloat, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool)     func __addArc(transform m: UnsafePointer<CGAffineTransform>?, x1 x1: CGFloat, y1 y1: CGFloat, x2 x2: CGFloat, y2 y2: CGFloat, radius radius: CGFloat)     func __addPath(transform m: UnsafePointer<CGAffineTransform>?, path path2: CGPath) } extension CGMutablePath {     func addRoundedRect(in rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat, transform transform: CGAffineTransform = default)     func move(to point: CGPoint, transform transform: CGAffineTransform = default)     func addLine(to point: CGPoint, transform transform: CGAffineTransform = default)     func addQuadCurve(to end: CGPoint, control control: CGPoint, transform transform: CGAffineTransform = default)     func addCurve(to end: CGPoint, control1 control1: CGPoint, control2 control2: CGPoint, transform transform: CGAffineTransform = default)     func addRect(_ rect: CGRect, transform transform: CGAffineTransform = default)     func addRects(_ rects: [CGRect], transform transform: CGAffineTransform = default)     func addLines(between points: [CGPoint], transform transform: CGAffineTransform = default)     func addEllipse(in rect: CGRect, transform transform: CGAffineTransform = default)     func addRelativeArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, delta delta: CGFloat, transform transform: CGAffineTransform = default)     func addArc(center center: CGPoint, radius radius: CGFloat, startAngle startAngle: CGFloat, endAngle endAngle: CGFloat, clockwise clockwise: Bool, transform transform: CGAffineTransform = default)     func addArc(tangent1End tangent1End: CGPoint, tangent2End tangent2End: CGPoint, radius radius: CGFloat, transform transform: CGAffineTransform = default)     func addPath(_ path: CGPath, transform transform: CGAffineTransform = default) } ``` |

Modified [CGMutablePath.closeSubpath()](https://developer.apple.com/documentation/coregraphics/1411188-cgpathclosesubpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCloseSubpath(_:) | ``` func CGPathCloseSubpath(_ path: CGMutablePath?) ``` |
| To | closeSubpath() | ``` func closeSubpath() ``` |

Modified [CGMutablePath.init()](https://developer.apple.com/documentation/coregraphics/1411209-cgpathcreatemutable)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateMutable() | ``` func CGPathCreateMutable() -> CGMutablePath ``` |
| To | init() | ``` init() ``` |

Modified [CGPath](https://developer.apple.com/documentation/coregraphics/cgpath)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CGPath { } ``` | -- |
| To | ``` class CGPath {     func copy(dashingWithPhase phase: CGFloat, lengths lengths: [CGFloat], transform transform: CGAffineTransform = default) -> CGPath     func copy(strokingWithWidth lineWidth: CGFloat, lineCap lineCap: CGLineCap, lineJoin lineJoin: CGLineJoin, miterLimit miterLimit: CGFloat, transform transform: CGAffineTransform = default) -> CGPath     func contains(_ point: CGPoint, using rule: CGPathFillRule = default, transform transform: CGAffineTransform = default) -> Bool     class var typeID: CFTypeID { get }     func copy() -> CGPath?     func copy(using transform: UnsafePointer<CGAffineTransform>?) -> CGPath?     func mutableCopy() -> CGMutablePath?     func mutableCopy(using transform: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?     init(rect rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?)     init(ellipseIn rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?)     init(roundedRect rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat, transform transform: UnsafePointer<CGAffineTransform>?)      init?(__byDashing path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, phase phase: CGFloat, lengths lengths: UnsafePointer<CGFloat>?, count count: Int)      init?(__byStroking path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, lineWidth lineWidth: CGFloat, lineCap lineCap: CGLineCap, lineJoin lineJoin: CGLineJoin, miterLimit miterLimit: CGFloat)     func __equalTo(_ path2: CGPath) -> Bool     var isEmpty: Bool { get }     func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool     var currentPoint: CGPoint { get }     var boundingBox: CGRect { get }     var boundingBoxOfPath: CGRect { get }     func __containsPoint(transform m: UnsafePointer<CGAffineTransform>?, point point: CGPoint, eoFill eoFill: Bool) -> Bool     func apply(info info: UnsafeMutableRawPointer?, function function: CoreGraphics.CGPathApplierFunction) } extension CGPath {     class var typeID: CFTypeID { get }     func copy() -> CGPath?     func copy(using transform: UnsafePointer<CGAffineTransform>?) -> CGPath?     func mutableCopy() -> CGMutablePath?     func mutableCopy(using transform: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?     init(rect rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?)     init(ellipseIn rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?)     init(roundedRect rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat, transform transform: UnsafePointer<CGAffineTransform>?)      init?(__byDashing path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, phase phase: CGFloat, lengths lengths: UnsafePointer<CGFloat>?, count count: Int)      init?(__byStroking path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, lineWidth lineWidth: CGFloat, lineCap lineCap: CGLineCap, lineJoin lineJoin: CGLineJoin, miterLimit miterLimit: CGFloat)     func __equalTo(_ path2: CGPath) -> Bool     var isEmpty: Bool { get }     func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool     var currentPoint: CGPoint { get }     var boundingBox: CGRect { get }     var boundingBoxOfPath: CGRect { get }     func __containsPoint(transform m: UnsafePointer<CGAffineTransform>?, point point: CGPoint, eoFill eoFill: Bool) -> Bool     func apply(info info: UnsafeMutableRawPointer?, function function: CoreGraphics.CGPathApplierFunction) } extension CGPath : Equatable { } extension CGPath {     func copy(dashingWithPhase phase: CGFloat, lengths lengths: [CGFloat], transform transform: CGAffineTransform = default) -> CGPath     func copy(strokingWithWidth lineWidth: CGFloat, lineCap lineCap: CGLineCap, lineJoin lineJoin: CGLineJoin, miterLimit miterLimit: CGFloat, transform transform: CGAffineTransform = default) -> CGPath     func contains(_ point: CGPoint, using rule: CGPathFillRule = default, transform transform: CGAffineTransform = default) -> Bool } ``` | Equatable |

Modified [CGPath.apply(info: UnsafeMutableRawPointer?, function: CoreGraphics.CGPathApplierFunction)](https://developer.apple.com/documentation/coregraphics/1411203-cgpathapply)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathApply(_:_:_:) | ``` func CGPathApply(_ path: CGPath?, _ info: UnsafeMutablePointer<Void>, _ function: CGPathApplierFunction?) ``` |
| To | apply(info:function:) | ``` func apply(info info: UnsafeMutableRawPointer?, function function: CoreGraphics.CGPathApplierFunction) ``` |

Modified [CGPath.CGPathGetBoundingBox(_: CGPath?) -> CGRect](https://developer.apple.com/documentation/coregraphics/1411165-cgpathgetboundingbox)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPathGetBoundingBox(_:) | ``` func CGPathGetBoundingBox(_ path: CGPath?) -> CGRect ``` | -- |
| To | boundingBox | ``` var boundingBox: CGRect { get } ``` | yes |

Modified [CGPath.CGPathGetPathBoundingBox(_: CGPath?) -> CGRect](https://developer.apple.com/documentation/coregraphics/1411200-cgpathgetpathboundingbox)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPathGetPathBoundingBox(_:) | ``` func CGPathGetPathBoundingBox(_ path: CGPath?) -> CGRect ``` | -- |
| To | boundingBoxOfPath | ``` var boundingBoxOfPath: CGRect { get } ``` | yes |

Modified [CGPath.copy() -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411211-cgpathcreatecopy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPathCreateCopy(_:) | ``` func CGPathCreateCopy(_ path: CGPath?) -> CGPath? ``` | tvOS 9.0 |
| To | copy() | ``` func copy() -> CGPath? ``` | tvOS 10.0 |

Modified [CGPath.copy(using: UnsafePointer<CGAffineTransform>?) -> CGPath?](https://developer.apple.com/documentation/coregraphics/1411161-cgpathcreatecopybytransformingpa)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPathCreateCopyByTransformingPath(_:_:) | ``` func CGPathCreateCopyByTransformingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath? ``` | tvOS 9.0 |
| To | copy(using:) | ``` func copy(using transform: UnsafePointer<CGAffineTransform>?) -> CGPath? ``` | tvOS 10.0 |

Modified [CGPath.CGPathGetCurrentPoint(_: CGPath?) -> CGPoint](https://developer.apple.com/documentation/coregraphics/cgpath/1411132-currentpoint)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPathGetCurrentPoint(_:) | ``` func CGPathGetCurrentPoint(_ path: CGPath?) -> CGPoint ``` | -- |
| To | currentPoint | ``` var currentPoint: CGPoint { get } ``` | yes |

Modified [CGPath.init(__byDashing: CGPath, transform: UnsafePointer<CGAffineTransform>?, phase: CGFloat, lengths: UnsafePointer<CGFloat>?, count: Int)](https://developer.apple.com/documentation/coregraphics/1411134-cgpathcreatecopybydashingpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateCopyByDashingPath(_:_:_:_:_:) | ``` func CGPathCreateCopyByDashingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>, _ phase: CGFloat, _ lengths: UnsafePointer<CGFloat>, _ count: Int) -> CGPath? ``` |
| To | init(__byDashing:transform:phase:lengths:count:) | ``` init?(__byDashing path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, phase phase: CGFloat, lengths lengths: UnsafePointer<CGFloat>?, count count: Int) ``` |

Modified [CGPath.init(__byStroking: CGPath, transform: UnsafePointer<CGAffineTransform>?, lineWidth: CGFloat, lineCap: CGLineCap, lineJoin: CGLineJoin, miterLimit: CGFloat)](https://developer.apple.com/documentation/coregraphics/1411128-cgpathcreatecopybystrokingpath)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateCopyByStrokingPath(_:_:_:_:_:_:) | ``` func CGPathCreateCopyByStrokingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>, _ lineWidth: CGFloat, _ lineCap: CGLineCap, _ lineJoin: CGLineJoin, _ miterLimit: CGFloat) -> CGPath? ``` |
| To | init(__byStroking:transform:lineWidth:lineCap:lineJoin:miterLimit:) | ``` init?(__byStroking path: CGPath, transform transform: UnsafePointer<CGAffineTransform>?, lineWidth lineWidth: CGFloat, lineCap lineCap: CGLineCap, lineJoin lineJoin: CGLineJoin, miterLimit miterLimit: CGFloat) ``` |

Modified [CGPath.init(ellipseIn: CGRect, transform: UnsafePointer<CGAffineTransform>?)](https://developer.apple.com/documentation/coregraphics/cgpath/1411177-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateWithEllipseInRect(_:_:) | ``` func CGPathCreateWithEllipseInRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |
| To | init(ellipseIn:transform:) | ``` init(ellipseIn rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?) ``` |

Modified [CGPath.init(rect: CGRect, transform: UnsafePointer<CGAffineTransform>?)](https://developer.apple.com/documentation/coregraphics/1411155-cgpathcreatewithrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateWithRect(_:_:) | ``` func CGPathCreateWithRect(_ rect: CGRect, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |
| To | init(rect:transform:) | ``` init(rect rect: CGRect, transform transform: UnsafePointer<CGAffineTransform>?) ``` |

Modified [CGPath.init(roundedRect: CGRect, cornerWidth: CGFloat, cornerHeight: CGFloat, transform: UnsafePointer<CGAffineTransform>?)](https://developer.apple.com/documentation/coregraphics/cgpath/1411218-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathCreateWithRoundedRect(_:_:_:_:) | ``` func CGPathCreateWithRoundedRect(_ rect: CGRect, _ cornerWidth: CGFloat, _ cornerHeight: CGFloat, _ transform: UnsafePointer<CGAffineTransform>) -> CGPath ``` |
| To | init(roundedRect:cornerWidth:cornerHeight:transform:) | ``` init(roundedRect rect: CGRect, cornerWidth cornerWidth: CGFloat, cornerHeight cornerHeight: CGFloat, transform transform: UnsafePointer<CGAffineTransform>?) ``` |

Modified [CGPath.CGPathIsEmpty(_: CGPath?) -> Bool](https://developer.apple.com/documentation/coregraphics/1411149-cgpathisempty)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGPathIsEmpty(_:) | ``` func CGPathIsEmpty(_ path: CGPath?) -> Bool ``` | tvOS 9.0 | -- |
| To | isEmpty | ``` var isEmpty: Bool { get } ``` | tvOS 10.0 | yes |

Modified [CGPath.isRect(_: UnsafeMutablePointer<CGRect>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1411163-cgpathisrect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathIsRect(_:_:) | ``` func CGPathIsRect(_ path: CGPath?, _ rect: UnsafeMutablePointer<CGRect>) -> Bool ``` |
| To | isRect(_:) | ``` func isRect(_ rect: UnsafeMutablePointer<CGRect>?) -> Bool ``` |

Modified [CGPath.mutableCopy() -> CGMutablePath?](https://developer.apple.com/documentation/coregraphics/1411196-cgpathcreatemutablecopy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPathCreateMutableCopy(_:) | ``` func CGPathCreateMutableCopy(_ path: CGPath?) -> CGMutablePath? ``` | tvOS 9.0 |
| To | mutableCopy() | ``` func mutableCopy() -> CGMutablePath? ``` | tvOS 10.0 |

Modified [CGPath.mutableCopy(using: UnsafePointer<CGAffineTransform>?) -> CGMutablePath?](https://developer.apple.com/documentation/coregraphics/cgpath/1411150-mutablecopy)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPathCreateMutableCopyByTransformingPath(_:_:) | ``` func CGPathCreateMutableCopyByTransformingPath(_ path: CGPath?, _ transform: UnsafePointer<CGAffineTransform>) -> CGMutablePath? ``` | tvOS 9.0 |
| To | mutableCopy(using:) | ``` func mutableCopy(using transform: UnsafePointer<CGAffineTransform>?) -> CGMutablePath? ``` | tvOS 10.0 |

Modified [CGPath.CGPathGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1411192-cgpathgettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPathGetTypeID() | ``` func CGPathGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGPathDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPathDrawingMode : Int32 {     case Fill     case EOFill     case Stroke     case FillStroke     case EOFillStroke } ``` |
| To | ``` enum CGPathDrawingMode : Int32 {     case fill     case eoFill     case stroke     case fillStroke     case eoFillStroke } ``` |

Modified [CGPathDrawingMode.eoFill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpatheofill)

|  | Declaration |
| --- | --- |
| From | ``` case EOFill ``` |
| To | ``` case eoFill ``` |

Modified [CGPathDrawingMode.eoFillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/eofillstroke)

|  | Declaration |
| --- | --- |
| From | ``` case EOFillStroke ``` |
| To | ``` case eoFillStroke ``` |

Modified [CGPathDrawingMode.fill](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/fill)

|  | Declaration |
| --- | --- |
| From | ``` case Fill ``` |
| To | ``` case fill ``` |

Modified [CGPathDrawingMode.fillStroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathfillstroke)

|  | Declaration |
| --- | --- |
| From | ``` case FillStroke ``` |
| To | ``` case fillStroke ``` |

Modified [CGPathDrawingMode.stroke](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode/kcgpathstroke)

|  | Declaration |
| --- | --- |
| From | ``` case Stroke ``` |
| To | ``` case stroke ``` |

Modified [CGPathElementType [enum]](https://developer.apple.com/documentation/coregraphics/cgpathelementtype)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPathElementType : Int32 {     case MoveToPoint     case AddLineToPoint     case AddQuadCurveToPoint     case AddCurveToPoint     case CloseSubpath } ``` |
| To | ``` enum CGPathElementType : Int32 {     case moveToPoint     case addLineToPoint     case addQuadCurveToPoint     case addCurveToPoint     case closeSubpath } ``` |

Modified [CGPathElementType.addCurveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` case AddCurveToPoint ``` |
| To | ``` case addCurveToPoint ``` |

Modified [CGPathElementType.addLineToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addlinetopoint)

|  | Declaration |
| --- | --- |
| From | ``` case AddLineToPoint ``` |
| To | ``` case addLineToPoint ``` |

Modified [CGPathElementType.addQuadCurveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/addquadcurvetopoint)

|  | Declaration |
| --- | --- |
| From | ``` case AddQuadCurveToPoint ``` |
| To | ``` case addQuadCurveToPoint ``` |

Modified [CGPathElementType.closeSubpath](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/closesubpath)

|  | Declaration |
| --- | --- |
| From | ``` case CloseSubpath ``` |
| To | ``` case closeSubpath ``` |

Modified [CGPathElementType.moveToPoint](https://developer.apple.com/documentation/coregraphics/cgpathelementtype/movetopoint)

|  | Declaration |
| --- | --- |
| From | ``` case MoveToPoint ``` |
| To | ``` case moveToPoint ``` |

Modified [CGPattern](https://developer.apple.com/documentation/coregraphics/cgpatternref)

|  | Declaration |
| --- | --- |
| From | ``` class CGPattern { } ``` |
| To | ``` class CGPattern {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, bounds bounds: CGRect, matrix matrix: CGAffineTransform, xStep xStep: CGFloat, yStep yStep: CGFloat, tiling tiling: CGPatternTiling, isColored isColored: Bool, callbacks callbacks: UnsafePointer<CGPatternCallbacks>) } extension CGPattern {     class var typeID: CFTypeID { get }     init?(info info: UnsafeMutableRawPointer?, bounds bounds: CGRect, matrix matrix: CGAffineTransform, xStep xStep: CGFloat, yStep yStep: CGFloat, tiling tiling: CGPatternTiling, isColored isColored: Bool, callbacks callbacks: UnsafePointer<CGPatternCallbacks>) } ``` |

Modified [CGPattern.init(info: UnsafeMutableRawPointer?, bounds: CGRect, matrix: CGAffineTransform, xStep: CGFloat, yStep: CGFloat, tiling: CGPatternTiling, isColored: Bool, callbacks: UnsafePointer<CGPatternCallbacks>)](https://developer.apple.com/documentation/coregraphics/cgpattern/1454997-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPatternCreate(_:_:_:_:_:_:_:_:) | ``` func CGPatternCreate(_ info: UnsafeMutablePointer<Void>, _ bounds: CGRect, _ matrix: CGAffineTransform, _ xStep: CGFloat, _ yStep: CGFloat, _ tiling: CGPatternTiling, _ isColored: Bool, _ callbacks: UnsafePointer<CGPatternCallbacks>) -> CGPattern? ``` |
| To | init(info:bounds:matrix:xStep:yStep:tiling:isColored:callbacks:) | ``` init?(info info: UnsafeMutableRawPointer?, bounds bounds: CGRect, matrix matrix: CGAffineTransform, xStep xStep: CGFloat, yStep yStep: CGFloat, tiling tiling: CGPatternTiling, isColored isColored: Bool, callbacks callbacks: UnsafePointer<CGPatternCallbacks>) ``` |

Modified [CGPattern.CGPatternGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1456445-cgpatterngettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPatternGetTypeID() | ``` func CGPatternGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGPatternCallbacks [struct]](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks)

|  | Declaration |
| --- | --- |
| From | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CGPatternDrawPatternCallback?     var releaseInfo: CGPatternReleaseInfoCallback?     init()     init(version version: UInt32, drawPattern drawPattern: CGPatternDrawPatternCallback?, releaseInfo releaseInfo: CGPatternReleaseInfoCallback?) } ``` |
| To | ``` struct CGPatternCallbacks {     var version: UInt32     var drawPattern: CoreGraphics.CGPatternDrawPatternCallback?     var releaseInfo: CoreGraphics.CGPatternReleaseInfoCallback?     init()     init(version version: UInt32, drawPattern drawPattern: CoreGraphics.CGPatternDrawPatternCallback?, releaseInfo releaseInfo: CoreGraphics.CGPatternReleaseInfoCallback?) } ``` |

Modified [CGPatternCallbacks.drawPattern](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/1454736-drawpattern)

|  | Declaration |
| --- | --- |
| From | ``` var drawPattern: CGPatternDrawPatternCallback? ``` |
| To | ``` var drawPattern: CoreGraphics.CGPatternDrawPatternCallback? ``` |

Modified [CGPatternCallbacks.releaseInfo](https://developer.apple.com/documentation/coregraphics/cgpatterncallbacks/1455379-releaseinfo)

|  | Declaration |
| --- | --- |
| From | ``` var releaseInfo: CGPatternReleaseInfoCallback? ``` |
| To | ``` var releaseInfo: CoreGraphics.CGPatternReleaseInfoCallback? ``` |

Modified [CGPatternTiling [enum]](https://developer.apple.com/documentation/coregraphics/cgpatterntiling)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPatternTiling : Int32 {     case NoDistortion     case ConstantSpacingMinimalDistortion     case ConstantSpacing } ``` |
| To | ``` enum CGPatternTiling : Int32 {     case noDistortion     case constantSpacingMinimalDistortion     case constantSpacing } ``` |

Modified [CGPatternTiling.constantSpacing](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/constantspacing)

|  | Declaration |
| --- | --- |
| From | ``` case ConstantSpacing ``` |
| To | ``` case constantSpacing ``` |

Modified [CGPatternTiling.constantSpacingMinimalDistortion](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/kcgpatterntilingconstantspacingminimaldistortion)

|  | Declaration |
| --- | --- |
| From | ``` case ConstantSpacingMinimalDistortion ``` |
| To | ``` case constantSpacingMinimalDistortion ``` |

Modified [CGPatternTiling.noDistortion](https://developer.apple.com/documentation/coregraphics/cgpatterntiling/nodistortion)

|  | Declaration |
| --- | --- |
| From | ``` case NoDistortion ``` |
| To | ``` case noDistortion ``` |

Modified [CGPDFBox [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfbox)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPDFBox : Int32 {     case MediaBox     case CropBox     case BleedBox     case TrimBox     case ArtBox } ``` |
| To | ``` enum CGPDFBox : Int32 {     case mediaBox     case cropBox     case bleedBox     case trimBox     case artBox } ``` |

Modified [CGPDFBox.artBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/artbox)

|  | Declaration |
| --- | --- |
| From | ``` case ArtBox ``` |
| To | ``` case artBox ``` |

Modified [CGPDFBox.bleedBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/bleedbox)

|  | Declaration |
| --- | --- |
| From | ``` case BleedBox ``` |
| To | ``` case bleedBox ``` |

Modified [CGPDFBox.cropBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdfcropbox)

|  | Declaration |
| --- | --- |
| From | ``` case CropBox ``` |
| To | ``` case cropBox ``` |

Modified [CGPDFBox.mediaBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdfmediabox)

|  | Declaration |
| --- | --- |
| From | ``` case MediaBox ``` |
| To | ``` case mediaBox ``` |

Modified [CGPDFBox.trimBox](https://developer.apple.com/documentation/coregraphics/cgpdfbox/kcgpdftrimbox)

|  | Declaration |
| --- | --- |
| From | ``` case TrimBox ``` |
| To | ``` case trimBox ``` |

Modified [CGPDFDataFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPDFDataFormat : Int32 {     case Raw     case JPEGEncoded     case JPEG2000 } ``` |
| To | ``` enum CGPDFDataFormat : Int32 {     case raw     case jpegEncoded     case JPEG2000 } ``` |

Modified [CGPDFDataFormat.jpegEncoded](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat/cgpdfdataformatjpegencoded)

|  | Declaration |
| --- | --- |
| From | ``` case JPEGEncoded ``` |
| To | ``` case jpegEncoded ``` |

Modified [CGPDFDataFormat.raw](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat/raw)

|  | Declaration |
| --- | --- |
| From | ``` case Raw ``` |
| To | ``` case raw ``` |

Modified [CGPDFDocument](https://developer.apple.com/documentation/coregraphics/cgpdfdocumentref)

|  | Declaration |
| --- | --- |
| From | ``` class CGPDFDocument { } ``` |
| To | ``` class CGPDFDocument {      init?(_ provider: CGDataProvider)      init?(_ url: CFURL)     func getVersion(majorVersion majorVersion: UnsafeMutablePointer<Int32>, minorVersion minorVersion: UnsafeMutablePointer<Int32>)     var isEncrypted: Bool { get }     func unlockWithPassword(_ password: UnsafePointer<Int8>) -> Bool     var isUnlocked: Bool { get }     var allowsPrinting: Bool { get }     var allowsCopying: Bool { get }     var numberOfPages: Int { get }     func page(at pageNumber: Int) -> CGPDFPage?     var catalog: CGPDFDictionaryRef? { get }     var info: CGPDFDictionaryRef? { get }     var fileIdentifier: CGPDFArrayRef? { get }     class var typeID: CFTypeID { get }     func getMediaBox(page page: Int32) -> CGRect     func getCropBox(page page: Int32) -> CGRect     func getBleedBox(page page: Int32) -> CGRect     func getTrimBox(page page: Int32) -> CGRect     func getArtBox(page page: Int32) -> CGRect     func getRotationAngle(page page: Int32) -> Int32 } extension CGPDFDocument {      init?(_ provider: CGDataProvider)      init?(_ url: CFURL)     func getVersion(majorVersion majorVersion: UnsafeMutablePointer<Int32>, minorVersion minorVersion: UnsafeMutablePointer<Int32>)     var isEncrypted: Bool { get }     func unlockWithPassword(_ password: UnsafePointer<Int8>) -> Bool     var isUnlocked: Bool { get }     var allowsPrinting: Bool { get }     var allowsCopying: Bool { get }     var numberOfPages: Int { get }     func page(at pageNumber: Int) -> CGPDFPage?     var catalog: CGPDFDictionaryRef? { get }     var info: CGPDFDictionaryRef? { get }     var fileIdentifier: CGPDFArrayRef? { get }     class var typeID: CFTypeID { get }     func getMediaBox(page page: Int32) -> CGRect     func getCropBox(page page: Int32) -> CGRect     func getBleedBox(page page: Int32) -> CGRect     func getTrimBox(page page: Int32) -> CGRect     func getArtBox(page page: Int32) -> CGRect     func getRotationAngle(page page: Int32) -> Int32 } ``` |

Modified [CGPDFDocument.CGPDFDocumentAllowsCopying(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402588-allowscopying)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentAllowsCopying(_:) | ``` func CGPDFDocumentAllowsCopying(_ document: CGPDFDocument?) -> Bool ``` | -- |
| To | allowsCopying | ``` var allowsCopying: Bool { get } ``` | yes |

Modified [CGPDFDocument.CGPDFDocumentAllowsPrinting(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/1402594-cgpdfdocumentallowsprinting)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentAllowsPrinting(_:) | ``` func CGPDFDocumentAllowsPrinting(_ document: CGPDFDocument?) -> Bool ``` | -- |
| To | allowsPrinting | ``` var allowsPrinting: Bool { get } ``` | yes |

Modified [CGPDFDocument.CGPDFDocumentGetCatalog(_: CGPDFDocument?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402606-catalog)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentGetCatalog(_:) | ``` func CGPDFDocumentGetCatalog(_ document: CGPDFDocument?) -> CGPDFDictionaryRef ``` | -- |
| To | catalog | ``` var catalog: CGPDFDictionaryRef? { get } ``` | yes |

Modified [CGPDFDocument.CGPDFDocumentGetID(_: CGPDFDocument?) -> CGPDFArrayRef](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402600-fileidentifier)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentGetID(_:) | ``` func CGPDFDocumentGetID(_ document: CGPDFDocument?) -> CGPDFArrayRef ``` | -- |
| To | fileIdentifier | ``` var fileIdentifier: CGPDFArrayRef? { get } ``` | yes |

Modified [CGPDFDocument.getVersion(majorVersion: UnsafeMutablePointer<Int32>, minorVersion: UnsafeMutablePointer<Int32>)](https://developer.apple.com/documentation/coregraphics/1402604-cgpdfdocumentgetversion)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentGetVersion(_:_:_:) | ``` func CGPDFDocumentGetVersion(_ document: CGPDFDocument?, _ majorVersion: UnsafeMutablePointer<Int32>, _ minorVersion: UnsafeMutablePointer<Int32>) ``` |
| To | getVersion(majorVersion:minorVersion:) | ``` func getVersion(majorVersion majorVersion: UnsafeMutablePointer<Int32>, minorVersion minorVersion: UnsafeMutablePointer<Int32>) ``` |

Modified [CGPDFDocument.CGPDFDocumentGetInfo(_: CGPDFDocument?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402589-info)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentGetInfo(_:) | ``` func CGPDFDocumentGetInfo(_ document: CGPDFDocument?) -> CGPDFDictionaryRef ``` | -- |
| To | info | ``` var info: CGPDFDictionaryRef? { get } ``` | yes |

Modified [CGPDFDocument.init(_: CFURL)](https://developer.apple.com/documentation/coregraphics/1402585-cgpdfdocumentcreatewithurl)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentCreateWithURL(_:) | ``` func CGPDFDocumentCreateWithURL(_ url: CFURL?) -> CGPDFDocument? ``` |
| To | init(_:) | ``` init?(_ url: CFURL) ``` |

Modified [CGPDFDocument.init(_: CGDataProvider)](https://developer.apple.com/documentation/coregraphics/1402603-cgpdfdocumentcreatewithprovider)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentCreateWithProvider(_:) | ``` func CGPDFDocumentCreateWithProvider(_ provider: CGDataProvider?) -> CGPDFDocument? ``` |
| To | init(_:) | ``` init?(_ provider: CGDataProvider) ``` |

Modified [CGPDFDocument.CGPDFDocumentIsEncrypted(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/1402591-cgpdfdocumentisencrypted)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentIsEncrypted(_:) | ``` func CGPDFDocumentIsEncrypted(_ document: CGPDFDocument?) -> Bool ``` | -- |
| To | isEncrypted | ``` var isEncrypted: Bool { get } ``` | yes |

Modified [CGPDFDocument.CGPDFDocumentIsUnlocked(_: CGPDFDocument?) -> Bool](https://developer.apple.com/documentation/coregraphics/1402607-cgpdfdocumentisunlocked)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentIsUnlocked(_:) | ``` func CGPDFDocumentIsUnlocked(_ document: CGPDFDocument?) -> Bool ``` | -- |
| To | isUnlocked | ``` var isUnlocked: Bool { get } ``` | yes |

Modified [CGPDFDocument.CGPDFDocumentGetNumberOfPages(_: CGPDFDocument?) -> Int](https://developer.apple.com/documentation/coregraphics/1402595-cgpdfdocumentgetnumberofpages)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFDocumentGetNumberOfPages(_:) | ``` func CGPDFDocumentGetNumberOfPages(_ document: CGPDFDocument?) -> Int ``` | -- |
| To | numberOfPages | ``` var numberOfPages: Int { get } ``` | yes |

Modified [CGPDFDocument.page(at: Int) -> CGPDFPage?](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402586-page)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentGetPage(_:_:) | ``` func CGPDFDocumentGetPage(_ document: CGPDFDocument?, _ pageNumber: Int) -> CGPDFPage? ``` |
| To | page(at:) | ``` func page(at pageNumber: Int) -> CGPDFPage? ``` |

Modified [CGPDFDocument.CGPDFDocumentGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1402597-cgpdfdocumentgettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentGetTypeID() | ``` func CGPDFDocumentGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGPDFDocument.unlockWithPassword(_: UnsafePointer<Int8>) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpdfdocument/1402599-unlockwithpassword)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFDocumentUnlockWithPassword(_:_:) | ``` func CGPDFDocumentUnlockWithPassword(_ document: CGPDFDocument?, _ password: UnsafePointer<Int8>) -> Bool ``` |
| To | unlockWithPassword(_:) | ``` func unlockWithPassword(_ password: UnsafePointer<Int8>) -> Bool ``` |

Modified [CGPDFObjectType [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype)

|  | Declaration |
| --- | --- |
| From | ``` enum CGPDFObjectType : Int32 {     case Null     case Boolean     case Integer     case Real     case Name     case String     case Array     case Dictionary     case Stream } ``` |
| To | ``` enum CGPDFObjectType : Int32 {     case null     case boolean     case integer     case real     case name     case string     case array     case dictionary     case stream } ``` |

Modified [CGPDFObjectType.array](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/array)

|  | Declaration |
| --- | --- |
| From | ``` case Array ``` |
| To | ``` case array ``` |

Modified [CGPDFObjectType.boolean](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypeboolean)

|  | Declaration |
| --- | --- |
| From | ``` case Boolean ``` |
| To | ``` case boolean ``` |

Modified [CGPDFObjectType.dictionary](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/dictionary)

|  | Declaration |
| --- | --- |
| From | ``` case Dictionary ``` |
| To | ``` case dictionary ``` |

Modified [CGPDFObjectType.integer](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypeinteger)

|  | Declaration |
| --- | --- |
| From | ``` case Integer ``` |
| To | ``` case integer ``` |

Modified [CGPDFObjectType.name](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypename)

|  | Declaration |
| --- | --- |
| From | ``` case Name ``` |
| To | ``` case name ``` |

Modified [CGPDFObjectType.null](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/null)

|  | Declaration |
| --- | --- |
| From | ``` case Null ``` |
| To | ``` case null ``` |

Modified [CGPDFObjectType.real](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/kcgpdfobjecttypereal)

|  | Declaration |
| --- | --- |
| From | ``` case Real ``` |
| To | ``` case real ``` |

Modified [CGPDFObjectType.stream](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/stream)

|  | Declaration |
| --- | --- |
| From | ``` case Stream ``` |
| To | ``` case stream ``` |

Modified [CGPDFObjectType.string](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype/string)

|  | Declaration |
| --- | --- |
| From | ``` case String ``` |
| To | ``` case string ``` |

Modified [CGPDFPage](https://developer.apple.com/documentation/coregraphics/cgpdfpageref)

|  | Declaration |
| --- | --- |
| From | ``` class CGPDFPage { } ``` |
| To | ``` class CGPDFPage {     var document: CGPDFDocument? { get }     var pageNumber: Int { get }     func getBoxRect(_ box: CGPDFBox) -> CGRect     var rotationAngle: Int32 { get }     func getDrawingTransform(_ box: CGPDFBox, rect rect: CGRect, rotate rotate: Int32, preserveAspectRatio preserveAspectRatio: Bool) -> CGAffineTransform     var dictionary: CGPDFDictionaryRef? { get }     class var typeID: CFTypeID { get } } extension CGPDFPage {     var document: CGPDFDocument? { get }     var pageNumber: Int { get }     func getBoxRect(_ box: CGPDFBox) -> CGRect     var rotationAngle: Int32 { get }     func getDrawingTransform(_ box: CGPDFBox, rect rect: CGRect, rotate rotate: Int32, preserveAspectRatio preserveAspectRatio: Bool) -> CGAffineTransform     var dictionary: CGPDFDictionaryRef? { get }     class var typeID: CFTypeID { get } } ``` |

Modified [CGPDFPage.CGPDFPageGetDictionary(_: CGPDFPage?) -> CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1455125-dictionary)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFPageGetDictionary(_:) | ``` func CGPDFPageGetDictionary(_ page: CGPDFPage?) -> CGPDFDictionaryRef ``` | -- |
| To | dictionary | ``` var dictionary: CGPDFDictionaryRef? { get } ``` | yes |

Modified [CGPDFPage.CGPDFPageGetDocument(_: CGPDFPage?) -> CGPDFDocument?](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1456166-document)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFPageGetDocument(_:) | ``` func CGPDFPageGetDocument(_ page: CGPDFPage?) -> CGPDFDocument? ``` | -- |
| To | document | ``` var document: CGPDFDocument? { get } ``` | yes |

Modified [CGPDFPage.getBoxRect(_: CGPDFBox) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1456114-getboxrect)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | CGPDFPageGetBoxRect(_:_:) | ``` func CGPDFPageGetBoxRect(_ page: CGPDFPage?, _ box: CGPDFBox) -> CGRect ``` | tvOS 9.0 |
| To | getBoxRect(_:) | ``` func getBoxRect(_ box: CGPDFBox) -> CGRect ``` | tvOS 10.0 |

Modified [CGPDFPage.getDrawingTransform(_: CGPDFBox, rect: CGRect, rotate: Int32, preserveAspectRatio: Bool) -> CGAffineTransform](https://developer.apple.com/documentation/coregraphics/1454893-cgpdfpagegetdrawingtransform)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFPageGetDrawingTransform(_:_:_:_:_:) | ``` func CGPDFPageGetDrawingTransform(_ page: CGPDFPage?, _ box: CGPDFBox, _ rect: CGRect, _ rotate: Int32, _ preserveAspectRatio: Bool) -> CGAffineTransform ``` |
| To | getDrawingTransform(_:rect:rotate:preserveAspectRatio:) | ``` func getDrawingTransform(_ box: CGPDFBox, rect rect: CGRect, rotate rotate: Int32, preserveAspectRatio preserveAspectRatio: Bool) -> CGAffineTransform ``` |

Modified [CGPDFPage.CGPDFPageGetPageNumber(_: CGPDFPage?) -> Int](https://developer.apple.com/documentation/coregraphics/cgpdfpage/1454587-pagenumber)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFPageGetPageNumber(_:) | ``` func CGPDFPageGetPageNumber(_ page: CGPDFPage?) -> Int ``` | -- |
| To | pageNumber | ``` var pageNumber: Int { get } ``` | yes |

Modified [CGPDFPage.CGPDFPageGetRotationAngle(_: CGPDFPage?) -> Int32](https://developer.apple.com/documentation/coregraphics/1455550-cgpdfpagegetrotationangle)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGPDFPageGetRotationAngle(_:) | ``` func CGPDFPageGetRotationAngle(_ page: CGPDFPage?) -> Int32 ``` | -- |
| To | rotationAngle | ``` var rotationAngle: Int32 { get } ``` | yes |

Modified [CGPDFPage.CGPDFPageGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/1454478-cgpdfpagegettypeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPDFPageGetTypeID() | ``` func CGPDFPageGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGPoint [struct]](https://developer.apple.com/documentation/coregraphics/cgpoint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint { get } } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint { get } } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } ``` | Equatable |
| To | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat)     func applying(_ t: CGAffineTransform) -> CGPoint     static let zero: CGPoint     init(x x: CGFloat, y y: CGFloat)     func equalTo(_ point2: CGPoint) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ point: UnsafeMutablePointer<CGPoint>) -> Bool     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     init?(dictionaryRepresentation dict: CFDictionary) } extension CGPoint {     func applying(_ t: CGAffineTransform) -> CGPoint } extension CGPoint : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGPoint : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGPoint {     static let zero: CGPoint     init(x x: CGFloat, y y: CGFloat)     func equalTo(_ point2: CGPoint) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ point: UnsafeMutablePointer<CGPoint>) -> Bool } extension CGPoint : Equatable { } extension CGPoint : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGPoint : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     init?(dictionaryRepresentation dict: CFDictionary) } ``` | CustomDebugStringConvertible, CustomPlaygroundQuickLookable, CustomReflectable, Equatable |

Modified [CGPoint.applying(_: CGAffineTransform) -> CGPoint](https://developer.apple.com/documentation/coregraphics/cgpoint/1454251-applying)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPointApplyAffineTransform(_:_:) | ``` func CGPointApplyAffineTransform(_ point: CGPoint, _ t: CGAffineTransform) -> CGPoint ``` |
| To | applying(_:) | ``` func applying(_ t: CGAffineTransform) -> CGPoint ``` |

Modified [CGPoint.CGPointCreateDictionaryRepresentation(_: CGPoint) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/cgpoint/1455382-dictionaryrepresentation)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGPointCreateDictionaryRepresentation(_:) | ``` func CGPointCreateDictionaryRepresentation(_ point: CGPoint) -> CFDictionary ``` | tvOS 9.0 | -- |
| To | dictionaryRepresentation | ``` var dictionaryRepresentation: CFDictionary { get } ``` | tvOS 10.0 | yes |

Modified [CGPoint.equalTo(_: CGPoint) -> Bool](https://developer.apple.com/documentation/coregraphics/cgpoint/1456179-equalto)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGPointEqualToPoint(_:_:) | ``` func CGPointEqualToPoint(_ point1: CGPoint, _ point2: CGPoint) -> Bool ``` |
| To | equalTo(_:) | ``` func equalTo(_ point2: CGPoint) -> Bool ``` |

Modified [CGRect [struct]](https://developer.apple.com/documentation/coregraphics/cgrect)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect { get }     static var infiniteRect: CGRect { get }     static var nullRect: CGRect { get }     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect { get }     static var infiniteRect: CGRect { get }     static var nullRect: CGRect { get }     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } ``` | Equatable |
| To | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize)     func applying(_ t: CGAffineTransform) -> CGRect     static let zero: CGRect     static let null: CGRect     static let infinite: CGRect     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var width: CGFloat { get }     var height: CGFloat { get }     func equalTo(_ rect2: CGRect) -> Bool     var standardized: CGRect { get }     var isEmpty: Bool { get }     var isNull: Bool { get }     var isInfinite: Bool { get }     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     var integral: CGRect { get }     func union(_ r2: CGRect) -> CGRect     func intersection(_ r2: CGRect) -> CGRect     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func __divided(slice slice: UnsafeMutablePointer<CGRect>, remainder remainder: UnsafeMutablePointer<CGRect>, atDistance amount: CGFloat, from edge: CGRectEdge)     func contains(_ point: CGPoint) -> Bool     func contains(_ rect2: CGRect) -> Bool     func intersects(_ rect2: CGRect) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ rect: UnsafeMutablePointer<CGRect>) -> Bool     static var zero: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     init?(dictionaryRepresentation dict: CFDictionary)     func divided(atDistance atDistance: CGFloat, from fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect {     func applying(_ t: CGAffineTransform) -> CGRect } extension CGRect : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGRect : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGRect {     static let zero: CGRect     static let null: CGRect     static let infinite: CGRect     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var width: CGFloat { get }     var height: CGFloat { get }     func equalTo(_ rect2: CGRect) -> Bool     var standardized: CGRect { get }     var isEmpty: Bool { get }     var isNull: Bool { get }     var isInfinite: Bool { get }     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     var integral: CGRect { get }     func union(_ r2: CGRect) -> CGRect     func intersection(_ r2: CGRect) -> CGRect     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func __divided(slice slice: UnsafeMutablePointer<CGRect>, remainder remainder: UnsafeMutablePointer<CGRect>, atDistance amount: CGFloat, from edge: CGRectEdge)     func contains(_ point: CGPoint) -> Bool     func contains(_ rect2: CGRect) -> Bool     func intersects(_ rect2: CGRect) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ rect: UnsafeMutablePointer<CGRect>) -> Bool } extension CGRect : Equatable { } extension CGRect : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGRect : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGRect {     static var zero: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     init?(dictionaryRepresentation dict: CFDictionary)     func divided(atDistance atDistance: CGFloat, from fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } ``` | CustomDebugStringConvertible, CustomPlaygroundQuickLookable, CustomReflectable, Equatable |

Modified [CGRect.applying(_: CGAffineTransform) -> CGRect](https://developer.apple.com/documentation/coregraphics/1455875-cgrectapplyaffinetransform)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectApplyAffineTransform(_:_:) | ``` func CGRectApplyAffineTransform(_ rect: CGRect, _ t: CGAffineTransform) -> CGRect ``` |
| To | applying(_:) | ``` func applying(_ t: CGAffineTransform) -> CGRect ``` |

Modified [CGRect.contains(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/cgrect/1454186-contains)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectContainsRect(_:_:) | ``` func CGRectContainsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool ``` |
| To | contains(_:) | ``` func contains(_ rect2: CGRect) -> Bool ``` |

Modified [CGRect.contains(_: CGPoint) -> Bool](https://developer.apple.com/documentation/coregraphics/1456316-cgrectcontainspoint)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectContainsPoint(_:_:) | ``` func CGRectContainsPoint(_ rect: CGRect, _ point: CGPoint) -> Bool ``` |
| To | contains(_:) | ``` func contains(_ point: CGPoint) -> Bool ``` |

Modified [CGRect.CGRectCreateDictionaryRepresentation(_: CGRect) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/cgrect/1455760-dictionaryrepresentation)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGRectCreateDictionaryRepresentation(_:) | ``` func CGRectCreateDictionaryRepresentation(_ _: CGRect) -> CFDictionary ``` | tvOS 9.0 | -- |
| To | dictionaryRepresentation | ``` var dictionaryRepresentation: CFDictionary { get } ``` | tvOS 10.0 | yes |

Modified [CGRect.equalTo(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/1456516-cgrectequaltorect)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectEqualToRect(_:_:) | ``` func CGRectEqualToRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool ``` |
| To | equalTo(_:) | ``` func equalTo(_ rect2: CGRect) -> Bool ``` |

Modified [CGRect.CGRectGetHeight(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgrect/1455645-height)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetHeight(_:) | ``` func CGRectGetHeight(_ rect: CGRect) -> CGFloat ``` | -- |
| To | height | ``` var height: CGFloat { get } ``` | yes |

Modified [CGRect.infinite](https://developer.apple.com/documentation/coregraphics/cgrectinfinite)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectInfinite | ``` let CGRectInfinite: CGRect ``` |
| To | infinite | ``` static let infinite: CGRect ``` |

Modified [CGRect.insetBy(dx: CGFloat, dy: CGFloat) -> CGRect](https://developer.apple.com/documentation/coregraphics/1454218-cgrectinset)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectInset(_:_:_:) | ``` func CGRectInset(_ rect: CGRect, _ dx: CGFloat, _ dy: CGFloat) -> CGRect ``` |
| To | insetBy(dx:dy:) | ``` func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect ``` |

Modified [CGRect.CGRectIntegral(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/1456348-cgrectintegral)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectIntegral(_:) | ``` func CGRectIntegral(_ rect: CGRect) -> CGRect ``` | -- |
| To | integral | ``` var integral: CGRect { get } ``` | yes |

Modified [CGRect.intersection(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/1455346-cgrectintersection)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectIntersection(_:_:) | ``` func CGRectIntersection(_ r1: CGRect, _ r2: CGRect) -> CGRect ``` |
| To | intersection(_:) | ``` func intersection(_ r2: CGRect) -> CGRect ``` |

Modified [CGRect.intersects(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/cgrect/1454747-intersects)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectIntersectsRect(_:_:) | ``` func CGRectIntersectsRect(_ rect1: CGRect, _ rect2: CGRect) -> Bool ``` |
| To | intersects(_:) | ``` func intersects(_ rect2: CGRect) -> Bool ``` |

Modified [CGRect.CGRectIsEmpty(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/cgrect/1454917-isempty)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectIsEmpty(_:) | ``` func CGRectIsEmpty(_ rect: CGRect) -> Bool ``` | -- |
| To | isEmpty | ``` var isEmpty: Bool { get } ``` | yes |

Modified [CGRect.CGRectIsInfinite(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/1455008-cgrectisinfinite)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectIsInfinite(_:) | ``` func CGRectIsInfinite(_ rect: CGRect) -> Bool ``` | -- |
| To | isInfinite | ``` var isInfinite: Bool { get } ``` | yes |

Modified [CGRect.CGRectIsNull(_: CGRect) -> Bool](https://developer.apple.com/documentation/coregraphics/1455471-cgrectisnull)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectIsNull(_:) | ``` func CGRectIsNull(_ rect: CGRect) -> Bool ``` | -- |
| To | isNull | ``` var isNull: Bool { get } ``` | yes |

Modified [CGRect.CGRectGetMaxX(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454334-cgrectgetmaxx)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMaxX(_:) | ``` func CGRectGetMaxX(_ rect: CGRect) -> CGFloat ``` | -- |
| To | maxX | ``` var maxX: CGFloat { get } ``` | yes |

Modified [CGRect.CGRectGetMaxY(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454060-cgrectgetmaxy)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMaxY(_:) | ``` func CGRectGetMaxY(_ rect: CGRect) -> CGFloat ``` | -- |
| To | maxY | ``` var maxY: CGFloat { get } ``` | yes |

Modified [CGRect.CGRectGetMidX(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456175-cgrectgetmidx)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMidX(_:) | ``` func CGRectGetMidX(_ rect: CGRect) -> CGFloat ``` | -- |
| To | midX | ``` var midX: CGFloat { get } ``` | yes |

Modified [CGRect.CGRectGetMidY(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456550-cgrectgetmidy)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMidY(_:) | ``` func CGRectGetMidY(_ rect: CGRect) -> CGFloat ``` | -- |
| To | midY | ``` var midY: CGFloat { get } ``` | yes |

Modified [CGRect.CGRectGetMinX(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/cgrect/1455948-minx)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMinX(_:) | ``` func CGRectGetMinX(_ rect: CGRect) -> CGFloat ``` | -- |
| To | minX | ``` var minX: CGFloat { get } ``` | yes |

Modified [CGRect.CGRectGetMinY(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454832-cgrectgetminy)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetMinY(_:) | ``` func CGRectGetMinY(_ rect: CGRect) -> CGFloat ``` | -- |
| To | minY | ``` var minY: CGFloat { get } ``` | yes |

Modified [CGRect.null](https://developer.apple.com/documentation/coregraphics/cgrect/1454271-null)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectNull | ``` let CGRectNull: CGRect ``` |
| To | null | ``` static let null: CGRect ``` |

Modified [CGRect.offsetBy(dx: CGFloat, dy: CGFloat) -> CGRect](https://developer.apple.com/documentation/coregraphics/1454841-cgrectoffset)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectOffset(_:_:_:) | ``` func CGRectOffset(_ rect: CGRect, _ dx: CGFloat, _ dy: CGFloat) -> CGRect ``` |
| To | offsetBy(dx:dy:) | ``` func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect ``` |

Modified [CGRect.CGRectStandardize(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgrect/1456432-standardized)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectStandardize(_:) | ``` func CGRectStandardize(_ rect: CGRect) -> CGRect ``` | -- |
| To | standardized | ``` var standardized: CGRect { get } ``` | yes |

Modified [CGRect.union(_: CGRect) -> CGRect](https://developer.apple.com/documentation/coregraphics/cgrect/1455837-union)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGRectUnion(_:_:) | ``` func CGRectUnion(_ r1: CGRect, _ r2: CGRect) -> CGRect ``` |
| To | union(_:) | ``` func union(_ r2: CGRect) -> CGRect ``` |

Modified [CGRect.CGRectGetWidth(_: CGRect) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454758-cgrectgetwidth)

|  | Name | Declaration | Readonly |
| --- | --- | --- | --- |
| From | CGRectGetWidth(_:) | ``` func CGRectGetWidth(_ rect: CGRect) -> CGFloat ``` | -- |
| To | width | ``` var width: CGFloat { get } ``` | yes |

Modified [CGRectEdge [enum]](https://developer.apple.com/documentation/coregraphics/cgrectedge)

|  | Declaration |
| --- | --- |
| From | ``` enum CGRectEdge : UInt32 {     case MinXEdge     case MinYEdge     case MaxXEdge     case MaxYEdge } ``` |
| To | ``` enum CGRectEdge : UInt32 {     case minXEdge     case minYEdge     case maxXEdge     case maxYEdge } ``` |

Modified [CGRectEdge.maxXEdge](https://developer.apple.com/documentation/coregraphics/cgrectedge/maxxedge)

|  | Declaration |
| --- | --- |
| From | ``` case MaxXEdge ``` |
| To | ``` case maxXEdge ``` |

Modified [CGRectEdge.maxYEdge](https://developer.apple.com/documentation/coregraphics/cgrectedge/cgrectmaxyedge)

|  | Declaration |
| --- | --- |
| From | ``` case MaxYEdge ``` |
| To | ``` case maxYEdge ``` |

Modified [CGRectEdge.minXEdge](https://developer.apple.com/documentation/coregraphics/cgrectedge/minxedge)

|  | Declaration |
| --- | --- |
| From | ``` case MinXEdge ``` |
| To | ``` case minXEdge ``` |

Modified [CGRectEdge.minYEdge](https://developer.apple.com/documentation/coregraphics/cgrectedge/cgrectminyedge)

|  | Declaration |
| --- | --- |
| From | ``` case MinYEdge ``` |
| To | ``` case minYEdge ``` |

Modified [CGShading](https://developer.apple.com/documentation/coregraphics/cgshadingref)

|  | Declaration |
| --- | --- |
| From | ``` class CGShading { } ``` |
| To | ``` class CGShading {     class var typeID: CFTypeID { get }     init?(axialSpace space: CGColorSpace, start start: CGPoint, end end: CGPoint, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool)     init?(radialSpace space: CGColorSpace, start start: CGPoint, startRadius startRadius: CGFloat, end end: CGPoint, endRadius endRadius: CGFloat, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool) } extension CGShading {     class var typeID: CFTypeID { get }     init?(axialSpace space: CGColorSpace, start start: CGPoint, end end: CGPoint, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool)     init?(radialSpace space: CGColorSpace, start start: CGPoint, startRadius startRadius: CGFloat, end end: CGPoint, endRadius endRadius: CGFloat, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool) } ``` |

Modified [CGShading.init(axialSpace: CGColorSpace, start: CGPoint, end: CGPoint, function: CGFunction, extendStart: Bool, extendEnd: Bool)](https://developer.apple.com/documentation/coregraphics/cgshading/1455224-init)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGShadingCreateAxial(_:_:_:_:_:_:) | ``` func CGShadingCreateAxial(_ space: CGColorSpace?, _ start: CGPoint, _ end: CGPoint, _ function: CGFunction?, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading? ``` |
| To | init(axialSpace:start:end:function:extendStart:extendEnd:) | ``` init?(axialSpace space: CGColorSpace, start start: CGPoint, end end: CGPoint, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool) ``` |

Modified [CGShading.init(radialSpace: CGColorSpace, start: CGPoint, startRadius: CGFloat, end: CGPoint, endRadius: CGFloat, function: CGFunction, extendStart: Bool, extendEnd: Bool)](https://developer.apple.com/documentation/coregraphics/1456399-cgshadingcreateradial)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGShadingCreateRadial(_:_:_:_:_:_:_:_:) | ``` func CGShadingCreateRadial(_ space: CGColorSpace?, _ start: CGPoint, _ startRadius: CGFloat, _ end: CGPoint, _ endRadius: CGFloat, _ function: CGFunction?, _ extendStart: Bool, _ extendEnd: Bool) -> CGShading? ``` |
| To | init(radialSpace:start:startRadius:end:endRadius:function:extendStart:extendEnd:) | ``` init?(radialSpace space: CGColorSpace, start start: CGPoint, startRadius startRadius: CGFloat, end end: CGPoint, endRadius endRadius: CGFloat, function function: CGFunction, extendStart extendStart: Bool, extendEnd extendEnd: Bool) ``` |

Modified [CGShading.CGShadingGetTypeID() -> CFTypeID](https://developer.apple.com/documentation/coregraphics/cgshading/1454302-typeid)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGShadingGetTypeID() | ``` func CGShadingGetTypeID() -> CFTypeID ``` |
| To | typeID | ``` class var typeID: CFTypeID { get } ``` |

Modified [CGSize [struct]](https://developer.apple.com/documentation/coregraphics/cgsize)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize { get } } extension CGSize : Equatable { } extension CGSize : _Reflectable { } extension CGSize : _Reflectable { } extension CGSize : Equatable { } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize { get } } ``` | Equatable |
| To | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat)     func applying(_ t: CGAffineTransform) -> CGSize     static let zero: CGSize     init(width width: CGFloat, height height: CGFloat)     func equalTo(_ size2: CGSize) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ size: UnsafeMutablePointer<CGSize>) -> Bool     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     init?(dictionaryRepresentation dict: CFDictionary) } extension CGSize {     func applying(_ t: CGAffineTransform) -> CGSize } extension CGSize : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGSize : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGSize {     static let zero: CGSize     init(width width: CGFloat, height height: CGFloat)     func equalTo(_ size2: CGSize) -> Bool     var dictionaryRepresentation: CFDictionary { get }     static func __setFromDictionaryRepresentation(_ dict: CFDictionary, _ size: UnsafeMutablePointer<CGSize>) -> Bool } extension CGSize : Equatable { } extension CGSize : CustomDebugStringConvertible {     var debugDescription: String { get } } extension CGSize : CustomReflectable, CustomPlaygroundQuickLookable {     var customMirror: Mirror { get }     var customPlaygroundQuickLook: PlaygroundQuickLook { get } } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     init?(dictionaryRepresentation dict: CFDictionary) } ``` | CustomDebugStringConvertible, CustomPlaygroundQuickLookable, CustomReflectable, Equatable |

Modified [CGSize.applying(_: CGAffineTransform) -> CGSize](https://developer.apple.com/documentation/coregraphics/cgsize/1454806-applying)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGSizeApplyAffineTransform(_:_:) | ``` func CGSizeApplyAffineTransform(_ size: CGSize, _ t: CGAffineTransform) -> CGSize ``` |
| To | applying(_:) | ``` func applying(_ t: CGAffineTransform) -> CGSize ``` |

Modified [CGSize.CGSizeCreateDictionaryRepresentation(_: CGSize) -> CFDictionary](https://developer.apple.com/documentation/coregraphics/cgsize/1455274-dictionaryrepresentation)

|  | Name | Declaration | Introduction | Readonly |
| --- | --- | --- | --- | --- |
| From | CGSizeCreateDictionaryRepresentation(_:) | ``` func CGSizeCreateDictionaryRepresentation(_ size: CGSize) -> CFDictionary ``` | tvOS 9.0 | -- |
| To | dictionaryRepresentation | ``` var dictionaryRepresentation: CFDictionary { get } ``` | tvOS 10.0 | yes |

Modified [CGSize.equalTo(_: CGSize) -> Bool](https://developer.apple.com/documentation/coregraphics/1455176-cgsizeequaltosize)

|  | Name | Declaration |
| --- | --- | --- |
| From | CGSizeEqualToSize(_:_:) | ``` func CGSizeEqualToSize(_ size1: CGSize, _ size2: CGSize) -> Bool ``` |
| To | equalTo(_:) | ``` func equalTo(_ size2: CGSize) -> Bool ``` |

Modified [CGTextDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode)

|  | Declaration |
| --- | --- |
| From | ``` enum CGTextDrawingMode : Int32 {     case Fill     case Stroke     case FillStroke     case Invisible     case FillClip     case StrokeClip     case FillStrokeClip     case Clip } ``` |
| To | ``` enum CGTextDrawingMode : Int32 {     case fill     case stroke     case fillStroke     case invisible     case fillClip     case strokeClip     case fillStrokeClip     case clip } ``` |

Modified [CGTextDrawingMode.clip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/clip)

|  | Declaration |
| --- | --- |
| From | ``` case Clip ``` |
| To | ``` case clip ``` |

Modified [CGTextDrawingMode.fill](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fill)

|  | Declaration |
| --- | --- |
| From | ``` case Fill ``` |
| To | ``` case fill ``` |

Modified [CGTextDrawingMode.fillClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillclip)

|  | Declaration |
| --- | --- |
| From | ``` case FillClip ``` |
| To | ``` case fillClip ``` |

Modified [CGTextDrawingMode.fillStroke](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillstroke)

|  | Declaration |
| --- | --- |
| From | ``` case FillStroke ``` |
| To | ``` case fillStroke ``` |

Modified [CGTextDrawingMode.fillStrokeClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/fillstrokeclip)

|  | Declaration |
| --- | --- |
| From | ``` case FillStrokeClip ``` |
| To | ``` case fillStrokeClip ``` |

Modified [CGTextDrawingMode.invisible](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/invisible)

|  | Declaration |
| --- | --- |
| From | ``` case Invisible ``` |
| To | ``` case invisible ``` |

Modified [CGTextDrawingMode.stroke](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/kcgtextstroke)

|  | Declaration |
| --- | --- |
| From | ``` case Stroke ``` |
| To | ``` case stroke ``` |

Modified [CGTextDrawingMode.strokeClip](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode/strokeclip)

|  | Declaration |
| --- | --- |
| From | ``` case StrokeClip ``` |
| To | ``` case strokeClip ``` |

Modified [CGVector [struct]](https://developer.apple.com/documentation/coregraphics/cgvector)

|  | Declaration |
| --- | --- |
| From | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector { get } } extension CGVector : Equatable { } extension CGVector : Equatable { } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector { get } } ``` |
| To | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat)     init(dx dx: CGFloat, dy dy: CGFloat)     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double) } extension CGVector {     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector : Equatable { } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double) } ``` |

Modified \*(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func *(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func *(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified \*=(_: CGFloat, _: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func *=(inout _ lhs: CGFloat, _ rhs: CGFloat) ``` |
| To | ``` func *=(_ lhs: inout CGFloat, _ rhs: CGFloat) ``` |

Modified +(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func +(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func +(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified +=(_: CGFloat, _: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func +=(inout _ lhs: CGFloat, _ rhs: CGFloat) ``` |
| To | ``` func +=(_ lhs: inout CGFloat, _ rhs: CGFloat) ``` |

Modified -(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func -(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func -(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified -=(_: CGFloat, _: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func -=(inout _ lhs: CGFloat, _ rhs: CGFloat) ``` |
| To | ``` func -=(_ lhs: inout CGFloat, _ rhs: CGFloat) ``` |

Modified /(_: CGFloat, _: CGFloat) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func /(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func /(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified /=(_: CGFloat, _: CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` func /=(inout _ lhs: CGFloat, _ rhs: CGFloat) ``` |
| To | ``` func /=(_ lhs: inout CGFloat, _ rhs: CGFloat) ``` |

Modified ==(_: CGSize, _: CGSize) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: CGSize, _ rhs: CGSize) -> Bool ``` |
| To | ``` func ==(_ lhs: CGSize, _ rhs: CGSize) -> Bool ``` |

Modified ==(_: CGVector, _: CGVector) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: CGVector, _ rhs: CGVector) -> Bool ``` |
| To | ``` func ==(_ lhs: CGVector, _ rhs: CGVector) -> Bool ``` |

Modified ==(_: CGRect, _: CGRect) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: CGRect, _ rhs: CGRect) -> Bool ``` |
| To | ``` func ==(_ lhs: CGRect, _ rhs: CGRect) -> Bool ``` |

Modified ==(_: CGPoint, _: CGPoint) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ==(_ lhs: CGPoint, _ rhs: CGPoint) -> Bool ``` |
| To | ``` func ==(_ lhs: CGPoint, _ rhs: CGPoint) -> Bool ``` |

Modified [acos(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456465-acos)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func acos(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func acos(_ x: CGFloat) -> CGFloat ``` |

Modified [acosh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455200-acosh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func acosh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func acosh(_ x: CGFloat) -> CGFloat ``` |

Modified [asin(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454580-asin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func asin(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func asin(_ x: CGFloat) -> CGFloat ``` |

Modified [asinh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456449-asinh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func asinh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func asinh(_ x: CGFloat) -> CGFloat ``` |

Modified [atan(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454322-atan)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atan(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func atan(_ x: CGFloat) -> CGFloat ``` |

Modified [atan2(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455332-atan2)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atan2(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func atan2(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [atanh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454527-atanh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func atanh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func atanh(_ x: CGFloat) -> CGFloat ``` |

Modified [cbrt(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455432-cbrt)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cbrt(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func cbrt(_ x: CGFloat) -> CGFloat ``` |

Modified [CGBitmapContextReleaseDataCallback](https://developer.apple.com/documentation/coregraphics/cgbitmapcontextreleasedatacallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGBitmapContextReleaseDataCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGBitmapContextReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGColorSpaceCreateDeviceCMYK() -> CGColorSpace](https://developer.apple.com/documentation/coregraphics/1408897-cgcolorspacecreatedevicecmyk)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace? ``` |
| To | ``` func CGColorSpaceCreateDeviceCMYK() -> CGColorSpace ``` |

Modified [CGColorSpaceCreateDeviceGray() -> CGColorSpace](https://developer.apple.com/documentation/coregraphics/1408908-cgcolorspacecreatedevicegray)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceGray() -> CGColorSpace? ``` |
| To | ``` func CGColorSpaceCreateDeviceGray() -> CGColorSpace ``` |

Modified [CGColorSpaceCreateDeviceRGB() -> CGColorSpace](https://developer.apple.com/documentation/coregraphics/1408837-cgcolorspacecreatedevicergb)

|  | Declaration |
| --- | --- |
| From | ``` func CGColorSpaceCreateDeviceRGB() -> CGColorSpace? ``` |
| To | ``` func CGColorSpaceCreateDeviceRGB() -> CGColorSpace ``` |

Modified [CGDataConsumerPutBytesCallback](https://developer.apple.com/documentation/coregraphics/cgdataconsumerputbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerPutBytesCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Int ``` |
| To | ``` typealias CGDataConsumerPutBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer, Int) -> Int ``` |

Modified [CGDataConsumerReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgdataconsumerreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataConsumerReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGDataConsumerReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGDataProviderGetBytePointerCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytepointercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytePointerCallback = (UnsafeMutablePointer<Void>) -> UnsafePointer<Void> ``` |
| To | ``` typealias CGDataProviderGetBytePointerCallback = (UnsafeMutableRawPointer?) -> UnsafeRawPointer? ``` |

Modified [CGDataProviderGetBytesAtPositionCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytesatpositioncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesAtPositionCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, off_t, Int) -> Int ``` |
| To | ``` typealias CGDataProviderGetBytesAtPositionCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, off_t, Int) -> Int ``` |

Modified [CGDataProviderGetBytesCallback](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytescallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderGetBytesCallback = (UnsafeMutablePointer<Void>, UnsafeMutablePointer<Void>, Int) -> Int ``` |
| To | ``` typealias CGDataProviderGetBytesCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, Int) -> Int ``` |

Modified [CGDataProviderReleaseBytePointerCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasebytepointercallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseBytePointerCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>) -> Void ``` |
| To | ``` typealias CGDataProviderReleaseBytePointerCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer) -> Swift.Void ``` |

Modified [CGDataProviderReleaseDataCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasedatacallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseDataCallback = (UnsafeMutablePointer<Void>, UnsafePointer<Void>, Int) -> Void ``` |
| To | ``` typealias CGDataProviderReleaseDataCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer, Int) -> Swift.Void ``` |

Modified [CGDataProviderReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGDataProviderReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGDataProviderRewindCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderrewindcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderRewindCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGDataProviderRewindCallback = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGDataProviderSkipForwardCallback](https://developer.apple.com/documentation/coregraphics/cgdataproviderskipforwardcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGDataProviderSkipForwardCallback = (UnsafeMutablePointer<Void>, off_t) -> off_t ``` |
| To | ``` typealias CGDataProviderSkipForwardCallback = (UnsafeMutableRawPointer?, off_t) -> off_t ``` |

Modified [CGFunctionEvaluateCallback](https://developer.apple.com/documentation/coregraphics/cgfunctionevaluatecallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionEvaluateCallback = (UnsafeMutablePointer<Void>, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Void ``` |
| To | ``` typealias CGFunctionEvaluateCallback = (UnsafeMutableRawPointer?, UnsafePointer<CGFloat>, UnsafeMutablePointer<CGFloat>) -> Swift.Void ``` |

Modified [CGFunctionReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgfunctionreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGFunctionReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGFunctionReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGPathApplierFunction](https://developer.apple.com/documentation/coregraphics/cgpathapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPathApplierFunction = (UnsafeMutablePointer<Void>, UnsafePointer<CGPathElement>) -> Void ``` |
| To | ``` typealias CGPathApplierFunction = (UnsafeMutableRawPointer?, UnsafePointer<CGPathElement>) -> Swift.Void ``` |

Modified [CGPatternDrawPatternCallback](https://developer.apple.com/documentation/coregraphics/cgpatterndrawpatterncallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternDrawPatternCallback = (UnsafeMutablePointer<Void>, CGContext?) -> Void ``` |
| To | ``` typealias CGPatternDrawPatternCallback = (UnsafeMutableRawPointer?, CGContext) -> Swift.Void ``` |

Modified [CGPatternReleaseInfoCallback](https://developer.apple.com/documentation/coregraphics/cgpatternreleaseinfocallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPatternReleaseInfoCallback = (UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGPatternReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGPDFArrayGetArray(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454834-cgpdfarraygetarray)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetArray(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool ``` |

Modified [CGPDFArrayGetBoolean(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454504-cgpdfarraygetboolean)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |
| To | ``` func CGPDFArrayGetBoolean(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool ``` |

Modified [CGPDFArrayGetDictionary(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454139-cgpdfarraygetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetDictionary(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool ``` |

Modified [CGPDFArrayGetInteger(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFInteger>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456053-cgpdfarraygetinteger)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |
| To | ``` func CGPDFArrayGetInteger(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFInteger>?) -> Bool ``` |

Modified [CGPDFArrayGetName(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455034-cgpdfarraygetname)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |
| To | ``` func CGPDFArrayGetName(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool ``` |

Modified [CGPDFArrayGetNumber(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFReal>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455374-cgpdfarraygetnumber)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |
| To | ``` func CGPDFArrayGetNumber(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFReal>?) -> Bool ``` |

Modified [CGPDFArrayGetObject(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456631-cgpdfarraygetobject)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetObject(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool ``` |

Modified [CGPDFArrayGetStream(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454424-cgpdfarraygetstream)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetStream(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool ``` |

Modified [CGPDFArrayGetString(_: CGPDFArrayRef, _: Int, _: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456104-cgpdfarraygetstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |
| To | ``` func CGPDFArrayGetString(_ array: CGPDFArrayRef, _ index: Int, _ value: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool ``` |

Modified [CGPDFArrayRef](https://developer.apple.com/documentation/coregraphics/cgpdfarrayref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFArrayRef = COpaquePointer ``` |
| To | ``` typealias CGPDFArrayRef = OpaquePointer ``` |

Modified [CGPDFContentStreamCreateWithPage(_: CGPDFPage) -> CGPDFContentStreamRef](https://developer.apple.com/documentation/coregraphics/1410047-cgpdfcontentstreamcreatewithpage)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage!) -> CGPDFContentStreamRef ``` |
| To | ``` func CGPDFContentStreamCreateWithPage(_ page: CGPDFPage) -> CGPDFContentStreamRef ``` |

Modified [CGPDFContentStreamGetResource(_: CGPDFContentStreamRef, _: UnsafePointer<Int8>, _: UnsafePointer<Int8>) -> CGPDFObjectRef?](https://developer.apple.com/documentation/coregraphics/1410044-cgpdfcontentstreamgetresource)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef ``` |
| To | ``` func CGPDFContentStreamGetResource(_ cs: CGPDFContentStreamRef, _ category: UnsafePointer<Int8>, _ name: UnsafePointer<Int8>) -> CGPDFObjectRef? ``` |

Modified [CGPDFContentStreamGetStreams(_: CGPDFContentStreamRef) -> CFArray?](https://developer.apple.com/documentation/coregraphics/1410048-cgpdfcontentstreamgetstreams)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray! ``` |
| To | ``` func CGPDFContentStreamGetStreams(_ cs: CGPDFContentStreamRef) -> CFArray? ``` |

Modified [CGPDFContentStreamRef](https://developer.apple.com/documentation/coregraphics/cgpdfcontentstreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFContentStreamRef = COpaquePointer ``` |
| To | ``` typealias CGPDFContentStreamRef = OpaquePointer ``` |

Modified [CGPDFDictionaryApplierFunction](https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryapplierfunction)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryApplierFunction = (UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGPDFDictionaryApplierFunction = (UnsafePointer<Int8>, CGPDFObjectRef, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGPDFDictionaryApplyFunction(_: CGPDFDictionaryRef, _: CoreGraphics.CGPDFDictionaryApplierFunction, _: UnsafeMutableRawPointer?)](https://developer.apple.com/documentation/coregraphics/1430216-cgpdfdictionaryapplyfunction)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CGPDFDictionaryApplierFunction?, _ info: UnsafeMutablePointer<Void>) ``` |
| To | ``` func CGPDFDictionaryApplyFunction(_ dict: CGPDFDictionaryRef, _ function: CoreGraphics.CGPDFDictionaryApplierFunction, _ info: UnsafeMutableRawPointer?) ``` |

Modified [CGPDFDictionaryGetArray(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430229-cgpdfdictionarygetarray)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetArray(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool ``` |

Modified [CGPDFDictionaryGetBoolean(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430226-cgpdfdictionarygetboolean)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetBoolean(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool ``` |

Modified [CGPDFDictionaryGetDictionary(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430220-cgpdfdictionarygetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetDictionary(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool ``` |

Modified [CGPDFDictionaryGetInteger(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFInteger>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430231-cgpdfdictionarygetinteger)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetInteger(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFInteger>?) -> Bool ``` |

Modified [CGPDFDictionaryGetName(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430230-cgpdfdictionarygetname)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetName(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool ``` |

Modified [CGPDFDictionaryGetNumber(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFReal>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430228-cgpdfdictionarygetnumber)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetNumber(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFReal>?) -> Bool ``` |

Modified [CGPDFDictionaryGetObject(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430214-cgpdfdictionarygetobject)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetObject(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool ``` |

Modified [CGPDFDictionaryGetStream(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430213-cgpdfdictionarygetstream)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetStream(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool ``` |

Modified [CGPDFDictionaryGetString(_: CGPDFDictionaryRef, _: UnsafePointer<Int8>, _: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1430224-cgpdfdictionarygetstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |
| To | ``` func CGPDFDictionaryGetString(_ dict: CGPDFDictionaryRef, _ key: UnsafePointer<Int8>, _ value: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool ``` |

Modified [CGPDFDictionaryRef](https://developer.apple.com/documentation/coregraphics/cgpdfdictionaryref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFDictionaryRef = COpaquePointer ``` |
| To | ``` typealias CGPDFDictionaryRef = OpaquePointer ``` |

Modified [CGPDFObjectGetValue(_: CGPDFObjectRef, _: CGPDFObjectType, _: UnsafeMutableRawPointer?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456508-cgpdfobjectgetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutablePointer<Void>) -> Bool ``` |
| To | ``` func CGPDFObjectGetValue(_ object: CGPDFObjectRef, _ type: CGPDFObjectType, _ value: UnsafeMutableRawPointer?) -> Bool ``` |

Modified [CGPDFObjectRef](https://developer.apple.com/documentation/coregraphics/cgpdfobjectref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFObjectRef = COpaquePointer ``` |
| To | ``` typealias CGPDFObjectRef = OpaquePointer ``` |

Modified [CGPDFOperatorCallback](https://developer.apple.com/documentation/coregraphics/cgpdfoperatorcallback)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorCallback = (CGPDFScannerRef, UnsafeMutablePointer<Void>) -> Void ``` |
| To | ``` typealias CGPDFOperatorCallback = (CGPDFScannerRef, UnsafeMutableRawPointer?) -> Swift.Void ``` |

Modified [CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef?](https://developer.apple.com/documentation/coregraphics/1455932-cgpdfoperatortablecreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef ``` |
| To | ``` func CGPDFOperatorTableCreate() -> CGPDFOperatorTableRef? ``` |

Modified [CGPDFOperatorTableRef](https://developer.apple.com/documentation/coregraphics/cgpdfoperatortableref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFOperatorTableRef = COpaquePointer ``` |
| To | ``` typealias CGPDFOperatorTableRef = OpaquePointer ``` |

Modified [CGPDFOperatorTableSetCallback(_: CGPDFOperatorTableRef, _: UnsafePointer<Int8>, _: CoreGraphics.CGPDFOperatorCallback)](https://developer.apple.com/documentation/coregraphics/1454118-cgpdfoperatortablesetcallback)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CGPDFOperatorCallback?) ``` |
| To | ``` func CGPDFOperatorTableSetCallback(_ table: CGPDFOperatorTableRef, _ name: UnsafePointer<Int8>, _ callback: CoreGraphics.CGPDFOperatorCallback) ``` |

Modified [CGPDFScannerCreate(_: CGPDFContentStreamRef, _: CGPDFOperatorTableRef?, _: UnsafeMutableRawPointer?) -> CGPDFScannerRef](https://developer.apple.com/documentation/coregraphics/1454410-cgpdfscannercreate)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef, _ info: UnsafeMutablePointer<Void>) -> CGPDFScannerRef ``` |
| To | ``` func CGPDFScannerCreate(_ cs: CGPDFContentStreamRef, _ table: CGPDFOperatorTableRef?, _ info: UnsafeMutableRawPointer?) -> CGPDFScannerRef ``` |

Modified [CGPDFScannerPopArray(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454360-cgpdfscannerpoparray)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFArrayRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopArray(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFArrayRef?>?) -> Bool ``` |

Modified [CGPDFScannerPopBoolean(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454663-cgpdfscannerpopboolean)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFBoolean>) -> Bool ``` |
| To | ``` func CGPDFScannerPopBoolean(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFBoolean>?) -> Bool ``` |

Modified [CGPDFScannerPopDictionary(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456538-cgpdfscannerpopdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFDictionaryRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopDictionary(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFDictionaryRef?>?) -> Bool ``` |

Modified [CGPDFScannerPopInteger(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFInteger>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454399-cgpdfscannerpopinteger)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFInteger>) -> Bool ``` |
| To | ``` func CGPDFScannerPopInteger(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFInteger>?) -> Bool ``` |

Modified [CGPDFScannerPopName(_: CGPDFScannerRef, _: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454584-cgpdfscannerpopname)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopName(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<UnsafePointer<Int8>>) -> Bool ``` |
| To | ``` func CGPDFScannerPopName(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<UnsafePointer<Int8>?>?) -> Bool ``` |

Modified [CGPDFScannerPopNumber(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFReal>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1456297-cgpdfscannerpopnumber)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFReal>) -> Bool ``` |
| To | ``` func CGPDFScannerPopNumber(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFReal>?) -> Bool ``` |

Modified [CGPDFScannerPopObject(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455971-cgpdfscannerpopobject)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFObjectRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopObject(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFObjectRef?>?) -> Bool ``` |

Modified [CGPDFScannerPopStream(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1454561-cgpdfscannerpopstream)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStreamRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopStream(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStreamRef?>?) -> Bool ``` |

Modified [CGPDFScannerPopString(_: CGPDFScannerRef, _: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool](https://developer.apple.com/documentation/coregraphics/1455018-cgpdfscannerpopstring)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFScannerPopString(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStringRef>) -> Bool ``` |
| To | ``` func CGPDFScannerPopString(_ scanner: CGPDFScannerRef, _ value: UnsafeMutablePointer<CGPDFStringRef?>?) -> Bool ``` |

Modified [CGPDFScannerRef](https://developer.apple.com/documentation/coregraphics/cgpdfscannerref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFScannerRef = COpaquePointer ``` |
| To | ``` typealias CGPDFScannerRef = OpaquePointer ``` |

Modified [CGPDFStreamGetDictionary(_: CGPDFStreamRef) -> CGPDFDictionaryRef?](https://developer.apple.com/documentation/coregraphics/1456118-cgpdfstreamgetdictionary)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef ``` |
| To | ``` func CGPDFStreamGetDictionary(_ stream: CGPDFStreamRef) -> CGPDFDictionaryRef? ``` |

Modified [CGPDFStreamRef](https://developer.apple.com/documentation/coregraphics/cgpdfstreamref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStreamRef = COpaquePointer ``` |
| To | ``` typealias CGPDFStreamRef = OpaquePointer ``` |

Modified [CGPDFStringGetBytePtr(_: CGPDFStringRef) -> UnsafePointer<UInt8>?](https://developer.apple.com/documentation/coregraphics/1455978-cgpdfstringgetbyteptr)

|  | Declaration |
| --- | --- |
| From | ``` func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8> ``` |
| To | ``` func CGPDFStringGetBytePtr(_ string: CGPDFStringRef) -> UnsafePointer<UInt8>? ``` |

Modified [CGPDFStringRef](https://developer.apple.com/documentation/coregraphics/cgpdfstringref)

|  | Declaration |
| --- | --- |
| From | ``` typealias CGPDFStringRef = COpaquePointer ``` |
| To | ``` typealias CGPDFStringRef = OpaquePointer ``` |

Modified [copysign(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454101-copysign)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func copysign(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func copysign(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [cos(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455193-cos)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cos(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func cos(_ x: CGFloat) -> CGFloat ``` |

Modified [cosh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455552-cosh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func cosh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func cosh(_ x: CGFloat) -> CGFloat ``` |

Modified [erf(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454212-erf)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func erf(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func erf(_ x: CGFloat) -> CGFloat ``` |

Modified [erfc(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455636-erfc)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func erfc(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func erfc(_ x: CGFloat) -> CGFloat ``` |

Modified [exp(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455628-exp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func exp(_ x: CGFloat) -> CGFloat ``` |

Modified [exp2(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455751-exp2)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func exp2(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func exp2(_ x: CGFloat) -> CGFloat ``` |

Modified [expm1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455892-expm1)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func expm1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func expm1(_ x: CGFloat) -> CGFloat ``` |

Modified [fdim(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454169-fdim)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fdim(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func fdim(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [fmax(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454365-fmax)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmax(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func fmax(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [fmin(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454631-fmin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func fmin(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func fmin(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified frexp(_: CGFloat) -> (CGFloat, Int)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func frexp(_ x: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` func frexp(_ x: CGFloat) -> (CGFloat, Int) ``` |

Modified [hypot(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456251-hypot)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func hypot(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func hypot(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [ilogb(_: CGFloat) -> Int](https://developer.apple.com/documentation/coregraphics/1454373-ilogb)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ilogb(_ x: CGFloat) -> Int ``` |
| To | ``` func ilogb(_ x: CGFloat) -> Int ``` |

Modified [j0(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455107-j0)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func j0(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func j0(_ x: CGFloat) -> CGFloat ``` |

Modified [j1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455116-j1)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func j1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func j1(_ x: CGFloat) -> CGFloat ``` |

Modified [jn(_: Int, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456281-jn)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func jn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |
| To | ``` func jn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |

Modified [ldexp(_: CGFloat, _: Int) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454868-ldexp)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func ldexp(_ x: CGFloat, _ n: Int) -> CGFloat ``` |
| To | ``` func ldexp(_ x: CGFloat, _ n: Int) -> CGFloat ``` |

Modified [lgamma(_: CGFloat) -> (CGFloat, Int)](https://developer.apple.com/documentation/coregraphics/1455415-lgamma)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func lgamma(_ x: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` func lgamma(_ x: CGFloat) -> (CGFloat, Int) ``` |

Modified [log(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456382-log)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func log(_ x: CGFloat) -> CGFloat ``` |

Modified [log10(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456602-log10)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log10(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func log10(_ x: CGFloat) -> CGFloat ``` |

Modified [log1p(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455279-log1p)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log1p(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func log1p(_ x: CGFloat) -> CGFloat ``` |

Modified [log2(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455770-log2)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func log2(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func log2(_ x: CGFloat) -> CGFloat ``` |

Modified [logb(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455887-logb)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func logb(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func logb(_ x: CGFloat) -> CGFloat ``` |

Modified modf(_: CGFloat) -> (CGFloat, CGFloat)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func modf(_ x: CGFloat) -> (CGFloat, CGFloat) ``` |
| To | ``` func modf(_ x: CGFloat) -> (CGFloat, CGFloat) ``` |

Modified [nan(_: String) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456512-nan)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nan(_ tag: String) -> CGFloat ``` |
| To | ``` func nan(_ tag: String) -> CGFloat ``` |

Modified [nearbyint(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455515-nearbyint)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nearbyint(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func nearbyint(_ x: CGFloat) -> CGFloat ``` |

Modified [nextafter(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454239-nextafter)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func nextafter(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func nextafter(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [pow(_: CGFloat, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456106-pow)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func pow(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |
| To | ``` func pow(_ lhs: CGFloat, _ rhs: CGFloat) -> CGFloat ``` |

Modified [remquo(_: CGFloat, _: CGFloat) -> (CGFloat, Int)](https://developer.apple.com/documentation/coregraphics/1455673-remquo)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func remquo(_ x: CGFloat, _ y: CGFloat) -> (CGFloat, Int) ``` |
| To | ``` func remquo(_ x: CGFloat, _ y: CGFloat) -> (CGFloat, Int) ``` |

Modified [rint(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455975-rint)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func rint(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func rint(_ x: CGFloat) -> CGFloat ``` |

Modified scalbn(_: CGFloat, _: Int) -> CGFloat

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func scalbn(_ x: CGFloat, _ n: Int) -> CGFloat ``` |
| To | ``` func scalbn(_ x: CGFloat, _ n: Int) -> CGFloat ``` |

Modified [sin(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456063-sin)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sin(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func sin(_ x: CGFloat) -> CGFloat ``` |

Modified [sinh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456648-sinh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func sinh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func sinh(_ x: CGFloat) -> CGFloat ``` |

Modified [tan(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454519-tan)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tan(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func tan(_ x: CGFloat) -> CGFloat ``` |

Modified [tanh(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454619-tanh)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tanh(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func tanh(_ x: CGFloat) -> CGFloat ``` |

Modified [tgamma(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454069-tgamma)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func tgamma(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func tgamma(_ x: CGFloat) -> CGFloat ``` |

Modified [y0(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1456014-y0)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func y0(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func y0(_ x: CGFloat) -> CGFloat ``` |

Modified [y1(_: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1454958-y1)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func y1(_ x: CGFloat) -> CGFloat ``` |
| To | ``` func y1(_ x: CGFloat) -> CGFloat ``` |

Modified [yn(_: Int, _: CGFloat) -> CGFloat](https://developer.apple.com/documentation/coregraphics/1455951-yn)

|  | Declaration |
| --- | --- |
| From | ``` @warn_unused_result func yn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |
| To | ``` func yn(_ n: Int, _ x: CGFloat) -> CGFloat ``` |

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

---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Accelerate.html
archived_at: '2026-07-18T02:56:21.438617Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Accelerate Changes

## Accelerate

Added DSPComplex.init()Added DSPComplex.init(real: Float, imag: Float)Added DSPDoubleComplex.init()Added DSPDoubleComplex.init(real: Double, imag: Double)Added DSPDoubleSplitComplex.init()Added DSPDoubleSplitComplex.init(realp: UnsafeMutablePointer<Double>, imagp: UnsafeMutablePointer<Double>)Added DSPSplitComplex.init()Added DSPSplitComplex.init(realp: UnsafeMutablePointer<Float>, imagp: UnsafeMutablePointer<Float>)Added vDSP_int24.init()Added vDSP_int24.init(bytes: (UInt8, UInt8, UInt8))Added vDSP_uint24.init()Added vDSP_uint24.init(bytes: (UInt8, UInt8, UInt8))Added vImageChannelDescription.init()Added vImageChannelDescription.init(min: CGFloat, zero: CGFloat, full: CGFloat, max: CGFloat)Added vImageRGBPrimaries.init()Added vImageRGBPrimaries.init(red_x: Float, green_x: Float, blue_x: Float, white_x: Float, red_y: Float, green_y: Float, blue_y: Float, white_y: Float)Added vImageTransferFunction.init()Added vImageTransferFunction.init(c0: CGFloat, c1: CGFloat, c2: CGFloat, c3: CGFloat, gamma: CGFloat, cutoff: CGFloat, c4: CGFloat, c5: CGFloat)Added vImage_ARGBToYpCbCr.init()Added vImage_ARGBToYpCbCr.init(opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added vImage_ARGBToYpCbCrMatrix.init()Added vImage_ARGBToYpCbCrMatrix.init(R_Yp: Float, G_Yp: Float, B_Yp: Float, R_Cb: Float, G_Cb: Float, B_Cb_R_Cr: Float, G_Cr: Float, B_Cr: Float)Added vImage_AffineTransform.init()Added vImage_AffineTransform.init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float)Added vImage_AffineTransform_Double.init()Added vImage_AffineTransform_Double.init(a: Double, b: Double, c: Double, d: Double, tx: Double, ty: Double)Added vImage_Buffer.init()Added vImage_Buffer.init(data: UnsafeMutablePointer<Void>, height: vImagePixelCount, width: vImagePixelCount, rowBytes: Int)Added vImage_CGImageFormat.init()Added vImage_CGImageFormat.init(bitsPerComponent: UInt32, bitsPerPixel: UInt32, colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo: CGBitmapInfo, version: UInt32, decode: UnsafePointer<CGFloat>, renderingIntent: CGColorRenderingIntent)Added vImage_YpCbCrPixelRange.init()Added vImage_YpCbCrPixelRange.init(Yp_bias: Int32, CbCr_bias: Int32, YpRangeMax: Int32, CbCrRangeMax: Int32, YpMax: Int32, YpMin: Int32, CbCrMax: Int32, CbCrMin: Int32)Added vImage_YpCbCrToARGB.init()Added vImage_YpCbCrToARGB.init(opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))Added vImage_YpCbCrToARGBMatrix.init()Added vImage_YpCbCrToARGBMatrix.init(Yp: Float, Cr_R: Float, Cr_G: Float, Cb_G: Float, Cb_B: Float)Modified DSPComplex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSPComplex {     var real: Float     var imag: Float } ``` |
| To | ``` struct DSPComplex {     var real: Float     var imag: Float     init()     init(real real: Float, imag imag: Float) } ``` |

Modified DSPDoubleComplex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSPDoubleComplex {     var real: Double     var imag: Double } ``` |
| To | ``` struct DSPDoubleComplex {     var real: Double     var imag: Double     init()     init(real real: Double, imag imag: Double) } ``` |

Modified DSPDoubleSplitComplex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSPDoubleSplitComplex {     var realp: UnsafeMutablePointer<Double>     var imagp: UnsafeMutablePointer<Double> } ``` |
| To | ``` struct DSPDoubleSplitComplex {     var realp: UnsafeMutablePointer<Double>     var imagp: UnsafeMutablePointer<Double>     init()     init(realp realp: UnsafeMutablePointer<Double>, imagp imagp: UnsafeMutablePointer<Double>) } ``` |

Modified DSPSplitComplex [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct DSPSplitComplex {     var realp: UnsafeMutablePointer<Float>     var imagp: UnsafeMutablePointer<Float> } ``` |
| To | ``` struct DSPSplitComplex {     var realp: UnsafeMutablePointer<Float>     var imagp: UnsafeMutablePointer<Float>     init()     init(realp realp: UnsafeMutablePointer<Float>, imagp imagp: UnsafeMutablePointer<Float>) } ``` |

Modified vDSP_int24 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vDSP_int24 {     var bytes: (UInt8, UInt8, UInt8) } ``` |
| To | ``` struct vDSP_int24 {     var bytes: (UInt8, UInt8, UInt8)     init()     init(bytes bytes: (UInt8, UInt8, UInt8)) } ``` |

Modified vDSP_uint24 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vDSP_uint24 {     var bytes: (UInt8, UInt8, UInt8) } ``` |
| To | ``` struct vDSP_uint24 {     var bytes: (UInt8, UInt8, UInt8)     init()     init(bytes bytes: (UInt8, UInt8, UInt8)) } ``` |

Modified vImageChannelDescription [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImageChannelDescription {     var min: CGFloat     var zero: CGFloat     var full: CGFloat     var max: CGFloat } ``` |
| To | ``` struct vImageChannelDescription {     var min: CGFloat     var zero: CGFloat     var full: CGFloat     var max: CGFloat     init()     init(min min: CGFloat, zero zero: CGFloat, full full: CGFloat, max max: CGFloat) } ``` |

Modified vImageRGBPrimaries [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImageRGBPrimaries {     var red_x: Float     var green_x: Float     var blue_x: Float     var white_x: Float     var red_y: Float     var green_y: Float     var blue_y: Float     var white_y: Float } ``` |
| To | ``` struct vImageRGBPrimaries {     var red_x: Float     var green_x: Float     var blue_x: Float     var white_x: Float     var red_y: Float     var green_y: Float     var blue_y: Float     var white_y: Float     init()     init(red_x red_x: Float, green_x green_x: Float, blue_x blue_x: Float, white_x white_x: Float, red_y red_y: Float, green_y green_y: Float, blue_y blue_y: Float, white_y white_y: Float) } ``` |

Modified vImageTransferFunction [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImageTransferFunction {     var c0: CGFloat     var c1: CGFloat     var c2: CGFloat     var c3: CGFloat     var gamma: CGFloat     var cutoff: CGFloat     var c4: CGFloat     var c5: CGFloat } ``` |
| To | ``` struct vImageTransferFunction {     var c0: CGFloat     var c1: CGFloat     var c2: CGFloat     var c3: CGFloat     var gamma: CGFloat     var cutoff: CGFloat     var c4: CGFloat     var c5: CGFloat     init()     init(c0 c0: CGFloat, c1 c1: CGFloat, c2 c2: CGFloat, c3 c3: CGFloat, gamma gamma: CGFloat, cutoff cutoff: CGFloat, c4 c4: CGFloat, c5 c5: CGFloat) } ``` |

Modified vImage_ARGBToYpCbCr [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_ARGBToYpCbCr {     var opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct vImage_ARGBToYpCbCr {     var opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(opaque opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified vImage_ARGBToYpCbCrMatrix [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_ARGBToYpCbCrMatrix {     var R_Yp: Float     var G_Yp: Float     var B_Yp: Float     var R_Cb: Float     var G_Cb: Float     var B_Cb_R_Cr: Float     var G_Cr: Float     var B_Cr: Float } ``` |
| To | ``` struct vImage_ARGBToYpCbCrMatrix {     var R_Yp: Float     var G_Yp: Float     var B_Yp: Float     var R_Cb: Float     var G_Cb: Float     var B_Cb_R_Cr: Float     var G_Cr: Float     var B_Cr: Float     init()     init(R_Yp R_Yp: Float, G_Yp G_Yp: Float, B_Yp B_Yp: Float, R_Cb R_Cb: Float, G_Cb G_Cb: Float, B_Cb_R_Cr B_Cb_R_Cr: Float, G_Cr G_Cr: Float, B_Cr B_Cr: Float) } ``` |

Modified vImage_AffineTransform [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_AffineTransform {     var a: Float     var b: Float     var c: Float     var d: Float     var tx: Float     var ty: Float } ``` |
| To | ``` struct vImage_AffineTransform {     var a: Float     var b: Float     var c: Float     var d: Float     var tx: Float     var ty: Float     init()     init(a a: Float, b b: Float, c c: Float, d d: Float, tx tx: Float, ty ty: Float) } ``` |

Modified vImage_AffineTransform_Double [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_AffineTransform_Double {     var a: Double     var b: Double     var c: Double     var d: Double     var tx: Double     var ty: Double } ``` |
| To | ``` struct vImage_AffineTransform_Double {     var a: Double     var b: Double     var c: Double     var d: Double     var tx: Double     var ty: Double     init()     init(a a: Double, b b: Double, c c: Double, d d: Double, tx tx: Double, ty ty: Double) } ``` |

Modified vImage_Buffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_Buffer {     var data: UnsafeMutablePointer<Void>     var height: vImagePixelCount     var width: vImagePixelCount     var rowBytes: UInt } ``` |
| To | ``` struct vImage_Buffer {     var data: UnsafeMutablePointer<Void>     var height: vImagePixelCount     var width: vImagePixelCount     var rowBytes: Int     init()     init(data data: UnsafeMutablePointer<Void>, height height: vImagePixelCount, width width: vImagePixelCount, rowBytes rowBytes: Int) } ``` |

Modified vImage_Buffer.rowBytes

|  | Declaration |
| --- | --- |
| From | ``` var rowBytes: UInt ``` |
| To | ``` var rowBytes: Int ``` |

Modified vImage_CGImageFormat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_CGImageFormat {     var bitsPerComponent: UInt32     var bitsPerPixel: UInt32     var colorSpace: Unmanaged<CGColorSpace>!     var bitmapInfo: CGBitmapInfo     var version: UInt32     var decode: UnsafePointer<CGFloat>     var renderingIntent: CGColorRenderingIntent } ``` |
| To | ``` struct vImage_CGImageFormat {     var bitsPerComponent: UInt32     var bitsPerPixel: UInt32     var colorSpace: Unmanaged<CGColorSpace>!     var bitmapInfo: CGBitmapInfo     var version: UInt32     var decode: UnsafePointer<CGFloat>     var renderingIntent: CGColorRenderingIntent     init()     init(bitsPerComponent bitsPerComponent: UInt32, bitsPerPixel bitsPerPixel: UInt32, colorSpace colorSpace: Unmanaged<CGColorSpace>!, bitmapInfo bitmapInfo: CGBitmapInfo, version version: UInt32, decode decode: UnsafePointer<CGFloat>, renderingIntent renderingIntent: CGColorRenderingIntent) } ``` |

Modified vImage_YpCbCrPixelRange [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_YpCbCrPixelRange {     var Yp_bias: Int32     var CbCr_bias: Int32     var YpRangeMax: Int32     var CbCrRangeMax: Int32     var YpMax: Int32     var YpMin: Int32     var CbCrMax: Int32     var CbCrMin: Int32 } ``` |
| To | ``` struct vImage_YpCbCrPixelRange {     var Yp_bias: Int32     var CbCr_bias: Int32     var YpRangeMax: Int32     var CbCrRangeMax: Int32     var YpMax: Int32     var YpMin: Int32     var CbCrMax: Int32     var CbCrMin: Int32     init()     init(Yp_bias Yp_bias: Int32, CbCr_bias CbCr_bias: Int32, YpRangeMax YpRangeMax: Int32, CbCrRangeMax CbCrRangeMax: Int32, YpMax YpMax: Int32, YpMin YpMin: Int32, CbCrMax CbCrMax: Int32, CbCrMin CbCrMin: Int32) } ``` |

Modified vImage_YpCbCrToARGB [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_YpCbCrToARGB {     var opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8) } ``` |
| To | ``` struct vImage_YpCbCrToARGB {     var opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)     init()     init(opaque opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)) } ``` |

Modified vImage_YpCbCrToARGBMatrix [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct vImage_YpCbCrToARGBMatrix {     var Yp: Float     var Cr_R: Float     var Cr_G: Float     var Cb_G: Float     var Cb_B: Float } ``` |
| To | ``` struct vImage_YpCbCrToARGBMatrix {     var Yp: Float     var Cr_R: Float     var Cr_G: Float     var Cb_G: Float     var Cb_B: Float     init()     init(Yp Yp: Float, Cr_R Cr_R: Float, Cr_G Cr_G: Float, Cb_G Cb_G: Float, Cb_B Cb_B: Float) } ``` |

Modified la_add_attributes(la_object_t, la_attribute_t)

|  | Declaration |
| --- | --- |
| From | ``` func la_add_attributes(_ object: la_object_t!, _ attributes: la_attribute_t) ``` |
| To | ``` func la_add_attributes(_ object: la_object_t, _ attributes: la_attribute_t) ``` |

Modified la_diagonal_matrix_from_vector(la_object_t, la_index_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_diagonal_matrix_from_vector(_ vector: la_object_t!, _ matrix_diagonal: la_index_t) -> la_object_t! ``` |
| To | ``` func la_diagonal_matrix_from_vector(_ vector: la_object_t, _ matrix_diagonal: la_index_t) -> la_object_t! ``` |

Modified la_difference(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_difference(_ obj_left: la_object_t!, _ obj_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_difference(_ obj_left: la_object_t, _ obj_right: la_object_t) -> la_object_t! ``` |

Modified la_elementwise_product(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_elementwise_product(_ obj_left: la_object_t!, _ obj_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_elementwise_product(_ obj_left: la_object_t, _ obj_right: la_object_t) -> la_object_t! ``` |

Modified la_inner_product(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_inner_product(_ vector_left: la_object_t!, _ vector_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_inner_product(_ vector_left: la_object_t, _ vector_right: la_object_t) -> la_object_t! ``` |

Modified la_matrix_cols(la_object_t) -> la_count_t

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_cols(_ matrix: la_object_t!) -> la_count_t ``` |
| To | ``` func la_matrix_cols(_ matrix: la_object_t) -> la_count_t ``` |

Modified la_matrix_from_splat(la_object_t, la_count_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_from_splat(_ splat: la_object_t!, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t) -> la_object_t! ``` |
| To | ``` func la_matrix_from_splat(_ splat: la_object_t, _ matrix_rows: la_count_t, _ matrix_cols: la_count_t) -> la_object_t! ``` |

Modified la_matrix_product(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_product(_ matrix_left: la_object_t!, _ matrix_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_matrix_product(_ matrix_left: la_object_t, _ matrix_right: la_object_t) -> la_object_t! ``` |

Modified la_matrix_rows(la_object_t) -> la_count_t

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_rows(_ matrix: la_object_t!) -> la_count_t ``` |
| To | ``` func la_matrix_rows(_ matrix: la_object_t) -> la_count_t ``` |

Modified la_matrix_slice(la_object_t, la_index_t, la_index_t, la_index_t, la_index_t, la_count_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_slice(_ matrix: la_object_t!, _ matrix_first_row: la_index_t, _ matrix_first_col: la_index_t, _ matrix_row_stride: la_index_t, _ matrix_col_stride: la_index_t, _ slice_rows: la_count_t, _ slice_cols: la_count_t) -> la_object_t! ``` |
| To | ``` func la_matrix_slice(_ matrix: la_object_t, _ matrix_first_row: la_index_t, _ matrix_first_col: la_index_t, _ matrix_row_stride: la_index_t, _ matrix_col_stride: la_index_t, _ slice_rows: la_count_t, _ slice_cols: la_count_t) -> la_object_t! ``` |

Modified la_matrix_to_double_buffer(UnsafeMutablePointer<Double>, la_count_t, la_object_t) -> la_status_t

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_to_double_buffer(_ buffer: UnsafeMutablePointer<Double>, _ buffer_row_stride: la_count_t, _ matrix: la_object_t!) -> la_status_t ``` |
| To | ``` func la_matrix_to_double_buffer(_ buffer: UnsafeMutablePointer<Double>, _ buffer_row_stride: la_count_t, _ matrix: la_object_t) -> la_status_t ``` |

Modified la_matrix_to_float_buffer(UnsafeMutablePointer<Float>, la_count_t, la_object_t) -> la_status_t

|  | Declaration |
| --- | --- |
| From | ``` func la_matrix_to_float_buffer(_ buffer: UnsafeMutablePointer<Float>, _ buffer_row_stride: la_count_t, _ matrix: la_object_t!) -> la_status_t ``` |
| To | ``` func la_matrix_to_float_buffer(_ buffer: UnsafeMutablePointer<Float>, _ buffer_row_stride: la_count_t, _ matrix: la_object_t) -> la_status_t ``` |

Modified la_norm_as_double(la_object_t, la_norm_t) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func la_norm_as_double(_ vector: la_object_t!, _ vector_norm: la_norm_t) -> Double ``` |
| To | ``` func la_norm_as_double(_ vector: la_object_t, _ vector_norm: la_norm_t) -> Double ``` |

Modified la_norm_as_float(la_object_t, la_norm_t) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func la_norm_as_float(_ vector: la_object_t!, _ vector_norm: la_norm_t) -> Float ``` |
| To | ``` func la_norm_as_float(_ vector: la_object_t, _ vector_norm: la_norm_t) -> Float ``` |

Modified la_normalized_vector(la_object_t, la_norm_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_normalized_vector(_ vector: la_object_t!, _ vector_norm: la_norm_t) -> la_object_t! ``` |
| To | ``` func la_normalized_vector(_ vector: la_object_t, _ vector_norm: la_norm_t) -> la_object_t! ``` |

Modified la_outer_product(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_outer_product(_ vector_left: la_object_t!, _ vector_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_outer_product(_ vector_left: la_object_t, _ vector_right: la_object_t) -> la_object_t! ``` |

Modified la_release(la_object_t)

|  | Declaration |
| --- | --- |
| From | ``` func la_release(_ object: la_object_t!) ``` |
| To | ``` func la_release(_ object: la_object_t) ``` |

Modified la_remove_attributes(la_object_t, la_attribute_t)

|  | Declaration |
| --- | --- |
| From | ``` func la_remove_attributes(_ object: la_object_t!, _ attributes: la_attribute_t) ``` |
| To | ``` func la_remove_attributes(_ object: la_object_t, _ attributes: la_attribute_t) ``` |

Modified la_retain(la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_retain(_ object: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_retain(_ object: la_object_t) -> la_object_t! ``` |

Modified la_scale_with_double(la_object_t, Double) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_scale_with_double(_ matrix: la_object_t!, _ scalar: Double) -> la_object_t! ``` |
| To | ``` func la_scale_with_double(_ matrix: la_object_t, _ scalar: Double) -> la_object_t! ``` |

Modified la_scale_with_float(la_object_t, Float) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_scale_with_float(_ matrix: la_object_t!, _ scalar: Float) -> la_object_t! ``` |
| To | ``` func la_scale_with_float(_ matrix: la_object_t, _ scalar: Float) -> la_object_t! ``` |

Modified la_solve(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_solve(_ matrix_system: la_object_t!, _ obj_rhs: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_solve(_ matrix_system: la_object_t, _ obj_rhs: la_object_t) -> la_object_t! ``` |

Modified la_splat_from_matrix_element(la_object_t, la_index_t, la_index_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_splat_from_matrix_element(_ matrix: la_object_t!, _ matrix_row: la_index_t, _ matrix_col: la_index_t) -> la_object_t! ``` |
| To | ``` func la_splat_from_matrix_element(_ matrix: la_object_t, _ matrix_row: la_index_t, _ matrix_col: la_index_t) -> la_object_t! ``` |

Modified la_splat_from_vector_element(la_object_t, la_index_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_splat_from_vector_element(_ vector: la_object_t!, _ vector_index: la_index_t) -> la_object_t! ``` |
| To | ``` func la_splat_from_vector_element(_ vector: la_object_t, _ vector_index: la_index_t) -> la_object_t! ``` |

Modified la_status(la_object_t) -> la_status_t

|  | Declaration |
| --- | --- |
| From | ``` func la_status(_ object: la_object_t!) -> la_status_t ``` |
| To | ``` func la_status(_ object: la_object_t) -> la_status_t ``` |

Modified la_sum(la_object_t, la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_sum(_ obj_left: la_object_t!, _ obj_right: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_sum(_ obj_left: la_object_t, _ obj_right: la_object_t) -> la_object_t! ``` |

Modified la_transpose(la_object_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_transpose(_ matrix: la_object_t!) -> la_object_t! ``` |
| To | ``` func la_transpose(_ matrix: la_object_t) -> la_object_t! ``` |

Modified la_vector_from_matrix_col(la_object_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_from_matrix_col(_ matrix: la_object_t!, _ matrix_col: la_count_t) -> la_object_t! ``` |
| To | ``` func la_vector_from_matrix_col(_ matrix: la_object_t, _ matrix_col: la_count_t) -> la_object_t! ``` |

Modified la_vector_from_matrix_diagonal(la_object_t, la_index_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_from_matrix_diagonal(_ matrix: la_object_t!, _ matrix_diagonal: la_index_t) -> la_object_t! ``` |
| To | ``` func la_vector_from_matrix_diagonal(_ matrix: la_object_t, _ matrix_diagonal: la_index_t) -> la_object_t! ``` |

Modified la_vector_from_matrix_row(la_object_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_from_matrix_row(_ matrix: la_object_t!, _ matrix_row: la_count_t) -> la_object_t! ``` |
| To | ``` func la_vector_from_matrix_row(_ matrix: la_object_t, _ matrix_row: la_count_t) -> la_object_t! ``` |

Modified la_vector_from_splat(la_object_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_from_splat(_ splat: la_object_t!, _ vector_length: la_count_t) -> la_object_t! ``` |
| To | ``` func la_vector_from_splat(_ splat: la_object_t, _ vector_length: la_count_t) -> la_object_t! ``` |

Modified la_vector_length(la_object_t) -> la_count_t

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_length(_ vector: la_object_t!) -> la_count_t ``` |
| To | ``` func la_vector_length(_ vector: la_object_t) -> la_count_t ``` |

Modified la_vector_slice(la_object_t, la_index_t, la_index_t, la_count_t) -> la_object_t!

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_slice(_ vector: la_object_t!, _ vector_first: la_index_t, _ vector_stride: la_index_t, _ slice_length: la_count_t) -> la_object_t! ``` |
| To | ``` func la_vector_slice(_ vector: la_object_t, _ vector_first: la_index_t, _ vector_stride: la_index_t, _ slice_length: la_count_t) -> la_object_t! ``` |

Modified la_vector_to_double_buffer(UnsafeMutablePointer<Double>, la_index_t, la_object_t) -> la_status_t

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_to_double_buffer(_ buffer: UnsafeMutablePointer<Double>, _ buffer_stride: la_index_t, _ vector: la_object_t!) -> la_status_t ``` |
| To | ``` func la_vector_to_double_buffer(_ buffer: UnsafeMutablePointer<Double>, _ buffer_stride: la_index_t, _ vector: la_object_t) -> la_status_t ``` |

Modified la_vector_to_float_buffer(UnsafeMutablePointer<Float>, la_index_t, la_object_t) -> la_status_t

|  | Declaration |
| --- | --- |
| From | ``` func la_vector_to_float_buffer(_ buffer: UnsafeMutablePointer<Float>, _ buffer_stride: la_index_t, _ vector: la_object_t!) -> la_status_t ``` |
| To | ``` func la_vector_to_float_buffer(_ buffer: UnsafeMutablePointer<Float>, _ buffer_stride: la_index_t, _ vector: la_object_t) -> la_status_t ``` |

Modified vImageBuffer_CopyToCVPixelBuffer(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_CGImageFormat>, CVPixelBuffer, vImageCVImageFormat!, UnsafePointer<CGFloat>, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageBuffer_CopyToCVPixelBuffer(_ buffer: UnsafePointer<vImage_Buffer>, _ bufferFormat: UnsafePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer!, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBuffer_CopyToCVPixelBuffer(_ buffer: UnsafePointer<vImage_Buffer>, _ bufferFormat: UnsafePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageBuffer_InitForCopyFromCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, vImageConverter, CVPixelBuffer, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageBuffer_InitForCopyFromCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter!, _ pixelBuffer: CVPixelBuffer!, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBuffer_InitForCopyFromCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter, _ pixelBuffer: CVPixelBuffer, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageBuffer_InitForCopyToCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, vImageConverter, CVPixelBuffer, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageBuffer_InitForCopyToCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter!, _ pixelBuffer: CVPixelBuffer!, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBuffer_InitForCopyToCVPixelBuffer(_ buffers: UnsafeMutablePointer<vImage_Buffer>, _ converter: vImageConverter, _ pixelBuffer: CVPixelBuffer, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageBuffer_InitWithCGImage(UnsafeMutablePointer<vImage_Buffer>, UnsafeMutablePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, CGImage, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageBuffer_InitWithCGImage(_ buf: UnsafeMutablePointer<vImage_Buffer>, _ format: UnsafeMutablePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ image: CGImage!, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBuffer_InitWithCGImage(_ buf: UnsafeMutablePointer<vImage_Buffer>, _ format: UnsafeMutablePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ image: CGImage, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageBuffer_InitWithCVPixelBuffer(UnsafeMutablePointer<vImage_Buffer>, UnsafeMutablePointer<vImage_CGImageFormat>, CVPixelBuffer, vImageCVImageFormat!, UnsafePointer<CGFloat>, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageBuffer_InitWithCVPixelBuffer(_ buffer: UnsafeMutablePointer<vImage_Buffer>, _ desiredFormat: UnsafeMutablePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer!, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageBuffer_InitWithCVPixelBuffer(_ buffer: UnsafeMutablePointer<vImage_Buffer>, _ desiredFormat: UnsafeMutablePointer<vImage_CGImageFormat>, _ cvPixelBuffer: CVPixelBuffer, _ cvImageFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageCVImageFormat_Copy(vImageConstCVImageFormat) -> Unmanaged<vImageCVImageFormat>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_Copy(_ format: vImageConstCVImageFormat!) -> Unmanaged<vImageCVImageFormat>! ``` |
| To | ``` func vImageCVImageFormat_Copy(_ format: vImageConstCVImageFormat) -> Unmanaged<vImageCVImageFormat>! ``` |

Modified vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_CopyChannelDescription(_ format: vImageCVImageFormat!, _ desc: UnsafePointer<vImageChannelDescription>, _ type: vImageBufferTypeCode) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_CopyChannelDescription(_ format: vImageCVImageFormat, _ desc: UnsafePointer<vImageChannelDescription>, _ type: vImageBufferTypeCode) -> vImage_Error ``` |

Modified vImageCVImageFormat_CopyConversionMatrix(vImageCVImageFormat, UnsafePointer<Void>, vImageMatrixType) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_CopyConversionMatrix(_ format: vImageCVImageFormat!, _ matrix: UnsafePointer<Void>, _ inType: vImageMatrixType) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_CopyConversionMatrix(_ format: vImageCVImageFormat, _ matrix: UnsafePointer<Void>, _ inType: vImageMatrixType) -> vImage_Error ``` |

Modified vImageCVImageFormat_GetAlphaHint(vImageConstCVImageFormat) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetAlphaHint(_ format: vImageConstCVImageFormat!) -> Int32 ``` |
| To | ``` func vImageCVImageFormat_GetAlphaHint(_ format: vImageConstCVImageFormat) -> Int32 ``` |

Modified vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetChannelCount(_ format: vImageConstCVImageFormat!) -> UInt32 ``` |
| To | ``` func vImageCVImageFormat_GetChannelCount(_ format: vImageConstCVImageFormat) -> UInt32 ``` |

Modified vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetChannelDescription(_ format: vImageConstCVImageFormat!, _ type: vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription> ``` |
| To | ``` func vImageCVImageFormat_GetChannelDescription(_ format: vImageConstCVImageFormat, _ type: vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription> ``` |

Modified vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetChannelNames(_ format: vImageConstCVImageFormat!) -> UnsafePointer<vImageBufferTypeCode> ``` |
| To | ``` func vImageCVImageFormat_GetChannelNames(_ format: vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode> ``` |

Modified vImageCVImageFormat_GetChromaSiting(vImageConstCVImageFormat) -> Unmanaged<CFString>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetChromaSiting(_ format: vImageConstCVImageFormat!) -> Unmanaged<CFString>! ``` |
| To | ``` func vImageCVImageFormat_GetChromaSiting(_ format: vImageConstCVImageFormat) -> Unmanaged<CFString>! ``` |

Modified vImageCVImageFormat_GetColorSpace(vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetColorSpace(_ format: vImageConstCVImageFormat!) -> Unmanaged<CGColorSpace>! ``` |
| To | ``` func vImageCVImageFormat_GetColorSpace(_ format: vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>! ``` |

Modified vImageCVImageFormat_GetConversionMatrix(vImageConstCVImageFormat, UnsafeMutablePointer<vImageMatrixType>) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetConversionMatrix(_ format: vImageConstCVImageFormat!, _ outType: UnsafeMutablePointer<vImageMatrixType>) -> UnsafePointer<Void> ``` |
| To | ``` func vImageCVImageFormat_GetConversionMatrix(_ format: vImageConstCVImageFormat, _ outType: UnsafeMutablePointer<vImageMatrixType>) -> UnsafePointer<Void> ``` |

Modified vImageCVImageFormat_GetFormatCode(vImageConstCVImageFormat) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetFormatCode(_ format: vImageConstCVImageFormat!) -> UInt32 ``` |
| To | ``` func vImageCVImageFormat_GetFormatCode(_ format: vImageConstCVImageFormat) -> UInt32 ``` |

Modified vImageCVImageFormat_GetUserData(vImageConstCVImageFormat) -> UnsafeMutablePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_GetUserData(_ format: vImageConstCVImageFormat!) -> UnsafeMutablePointer<Void> ``` |
| To | ``` func vImageCVImageFormat_GetUserData(_ format: vImageConstCVImageFormat) -> UnsafeMutablePointer<Void> ``` |

Modified vImageCVImageFormat_SetAlphaHint(vImageCVImageFormat, Int32) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetAlphaHint(_ format: vImageCVImageFormat!, _ alphaIsOne: Int32) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetAlphaHint(_ format: vImageCVImageFormat, _ alphaIsOne: Int32) -> vImage_Error ``` |

Modified vImageCVImageFormat_SetChromaSiting(vImageCVImageFormat, CFString!) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetChromaSiting(_ format: vImageCVImageFormat!, _ siting: CFString!) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetChromaSiting(_ format: vImageCVImageFormat, _ siting: CFString!) -> vImage_Error ``` |

Modified vImageCVImageFormat_SetColorSpace(vImageCVImageFormat, CGColorSpace!) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetColorSpace(_ format: vImageCVImageFormat!, _ colorspace: CGColorSpace!) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetColorSpace(_ format: vImageCVImageFormat, _ colorspace: CGColorSpace!) -> vImage_Error ``` |

Modified vImageCVImageFormat_SetUserData(vImageCVImageFormat, UnsafeMutablePointer<Void>, CFunctionPointer<((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)>) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat!, _ userData: UnsafeMutablePointer<Void>, _ userDataReleaseCallback: CFunctionPointer<((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)>) -> vImage_Error ``` |
| To | ``` func vImageCVImageFormat_SetUserData(_ format: vImageCVImageFormat, _ userData: UnsafeMutablePointer<Void>, _ userDataReleaseCallback: CFunctionPointer<((vImageCVImageFormat!, UnsafeMutablePointer<Void>) -> Void)>) -> vImage_Error ``` |

Modified vImageConvert_AnyToAny(vImageConverter, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutablePointer<Void>, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvert_AnyToAny(_ converter: vImageConverter!, _ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvert_AnyToAny(_ converter: vImageConverter, _ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutablePointer<Void>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageConvert_ChunkyToPlanar8(UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvert_ChunkyToPlanar8(_ srcChannels: UnsafeMutablePointer<UnsafePointer<Void>>, _ destPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ channelCount: UInt32, _ srcStrideBytes: UInt, _ srcWidth: vImagePixelCount, _ srcHeight: vImagePixelCount, _ srcRowBytes: UInt, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvert_ChunkyToPlanar8(_ srcChannels: UnsafeMutablePointer<UnsafePointer<Void>>, _ destPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ channelCount: UInt32, _ srcStrideBytes: Int, _ srcWidth: vImagePixelCount, _ srcHeight: vImagePixelCount, _ srcRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageConvert_ChunkyToPlanarF(UnsafeMutablePointer<UnsafePointer<Void>>, UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvert_ChunkyToPlanarF(_ srcChannels: UnsafeMutablePointer<UnsafePointer<Void>>, _ destPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ channelCount: UInt32, _ srcStrideBytes: UInt, _ srcWidth: vImagePixelCount, _ srcHeight: vImagePixelCount, _ srcRowBytes: UInt, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvert_ChunkyToPlanarF(_ srcChannels: UnsafeMutablePointer<UnsafePointer<Void>>, _ destPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ channelCount: UInt32, _ srcStrideBytes: Int, _ srcWidth: vImagePixelCount, _ srcHeight: vImagePixelCount, _ srcRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageConvert_PlanarToChunky8(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvert_PlanarToChunky8(_ srcPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ destChannels: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ channelCount: UInt32, _ destStrideBytes: UInt, _ destWidth: vImagePixelCount, _ destHeight: vImagePixelCount, _ destRowBytes: UInt, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvert_PlanarToChunky8(_ srcPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ destChannels: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ channelCount: UInt32, _ destStrideBytes: Int, _ destWidth: vImagePixelCount, _ destHeight: vImagePixelCount, _ destRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageConvert_PlanarToChunkyF(UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, UnsafeMutablePointer<UnsafeMutablePointer<Void>>, UInt32, Int, vImagePixelCount, vImagePixelCount, Int, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConvert_PlanarToChunkyF(_ srcPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ destChannels: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ channelCount: UInt32, _ destStrideBytes: UInt, _ destWidth: vImagePixelCount, _ destHeight: vImagePixelCount, _ destRowBytes: UInt, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConvert_PlanarToChunkyF(_ srcPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>>, _ destChannels: UnsafeMutablePointer<UnsafeMutablePointer<Void>>, _ channelCount: UInt32, _ destStrideBytes: Int, _ destWidth: vImagePixelCount, _ destHeight: vImagePixelCount, _ destRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageConverter_CreateForCGToCVImageFormat(UnsafePointer<vImage_CGImageFormat>, vImageCVImageFormat, UnsafePointer<CGFloat>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_CreateForCGToCVImageFormat(_ srcFormat: UnsafePointer<vImage_CGImageFormat>, _ destFormat: vImageCVImageFormat!, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |
| To | ``` func vImageConverter_CreateForCGToCVImageFormat(_ srcFormat: UnsafePointer<vImage_CGImageFormat>, _ destFormat: vImageCVImageFormat, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |

Modified vImageConverter_CreateForCVToCGImageFormat(vImageCVImageFormat, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_CreateForCVToCGImageFormat(_ srcFormat: vImageCVImageFormat!, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |
| To | ``` func vImageConverter_CreateForCVToCGImageFormat(_ srcFormat: vImageCVImageFormat, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |

Modified vImageConverter_CreateWithColorSyncCodeFragment(AnyObject, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<vImage_CGImageFormat>, UnsafePointer<CGFloat>, vImage_Flags, UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>!

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_CreateWithColorSyncCodeFragment(_ codeFragment: AnyObject!, _ srcFormat: UnsafePointer<vImage_CGImageFormat>, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |
| To | ``` func vImageConverter_CreateWithColorSyncCodeFragment(_ codeFragment: AnyObject, _ srcFormat: UnsafePointer<vImage_CGImageFormat>, _ destFormat: UnsafePointer<vImage_CGImageFormat>, _ backgroundColor: UnsafePointer<CGFloat>, _ flags: vImage_Flags, _ error: UnsafeMutablePointer<vImage_Error>) -> Unmanaged<vImageConverter>! ``` |

Modified vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_GetDestinationBufferOrder(_ converter: vImageConverter!) -> UnsafePointer<vImageBufferTypeCode> ``` |
| To | ``` func vImageConverter_GetDestinationBufferOrder(_ converter: vImageConverter) -> UnsafePointer<vImageBufferTypeCode> ``` |

Modified vImageConverter_GetNumberOfDestinationBuffers(vImageConverter) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_GetNumberOfDestinationBuffers(_ converter: vImageConverter!) -> UInt ``` |
| To | ``` func vImageConverter_GetNumberOfDestinationBuffers(_ converter: vImageConverter) -> UInt ``` |

Modified vImageConverter_GetNumberOfSourceBuffers(vImageConverter) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_GetNumberOfSourceBuffers(_ converter: vImageConverter!) -> UInt ``` |
| To | ``` func vImageConverter_GetNumberOfSourceBuffers(_ converter: vImageConverter) -> UInt ``` |

Modified vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_GetSourceBufferOrder(_ converter: vImageConverter!) -> UnsafePointer<vImageBufferTypeCode> ``` |
| To | ``` func vImageConverter_GetSourceBufferOrder(_ converter: vImageConverter) -> UnsafePointer<vImageBufferTypeCode> ``` |

Modified vImageConverter_MustOperateOutOfPlace(vImageConverter, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageConverter_MustOperateOutOfPlace(_ converter: vImageConverter!, _ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageConverter_MustOperateOutOfPlace(_ converter: vImageConverter, _ srcs: UnsafePointer<vImage_Buffer>, _ dests: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageCopyBuffer(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error

|  | Declaration |
| --- | --- |
| From | ``` func vImageCopyBuffer(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ pixelSize: UInt, _ flags: vImage_Flags) -> vImage_Error ``` |
| To | ``` func vImageCopyBuffer(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ pixelSize: Int, _ flags: vImage_Flags) -> vImage_Error ``` |

Modified vImageGetResamplingFilterSize(Float, CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, Float, vImage_Flags) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, _ kernelWidth: Float, _ flags: vImage_Flags) -> UInt ``` |
| To | ``` func vImageGetResamplingFilterSize(_ scale: Float, _ kernelFunc: CFunctionPointer<((UnsafePointer<Float>, UnsafeMutablePointer<Float>, UInt, UnsafeMutablePointer<Void>) -> Void)>, _ kernelWidth: Float, _ flags: vImage_Flags) -> Int ``` |

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

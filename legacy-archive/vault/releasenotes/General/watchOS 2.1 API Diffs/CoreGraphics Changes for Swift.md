---
title: watchOS 2.1 API Diffs
apple_id: TP40016636
resource_type: Release Note
platform: watchOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/watchOS21APIDiffs/Swift/CoreGraphics.html
archived_at: '2026-07-18T02:58:08.002270Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [watchOS 2.1 API Diffs](watchOS%202.0%20to%20watchOS%202.1%20API%20Differences.md)


# CoreGraphics Changes for Swift

### CoreGraphics

Modified [CGBlendMode [enum]](https://developer.apple.com/documentation/coregraphics/cgblendmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGColorRenderingIntent [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorrenderingintent)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGColorSpaceModel [enum]](https://developer.apple.com/documentation/coregraphics/cgcolorspacemodel)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGError [enum]](https://developer.apple.com/documentation/coregraphics/cgerror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGFloat [struct]](https://developer.apple.com/documentation/coregraphics/cgfloat)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CGFloat {     typealias NativeType = Float     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } extension CGFloat : FloatingPointType {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: CGFloat { get }     static var NaN: CGFloat { get }     static var quietNaN: CGFloat { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get }     var floatingPointClass: FloatingPointClassification { get } } extension CGFloat {     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : _Reflectable { } extension CGFloat : CustomStringConvertible {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : FloatLiteralConvertible {     init(floatLiteral value: NativeType) } extension CGFloat : IntegerLiteralConvertible {     init(integerLiteral value: Int) } extension CGFloat : SignedNumberType, AbsoluteValuable {     @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat } extension CGFloat : Equatable { } extension CGFloat : Comparable { } extension CGFloat : Strideable, _Strideable {     func distanceTo(_ other: CGFloat) -> CGFloat     func advancedBy(_ amount: CGFloat) -> CGFloat } extension CGFloat : _CVarArgPassedAsDouble, CVarArgType, _CVarArgAlignedType { } extension CGFloat : _ObjectiveCBridgeable {     init(_ number: NSNumber) } ``` | AbsoluteValuable, CVarArgType, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, SignedNumberType, Strideable |
| To | ``` struct CGFloat {     typealias NativeType = Float     init()     init(_ value: Float)     init(_ value: Double)     var native: NativeType } extension CGFloat : FloatingPointType {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: CGFloat { get }     static var NaN: CGFloat { get }     static var quietNaN: CGFloat { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get }     var floatingPointClass: FloatingPointClassification { get } } extension CGFloat {     static var min: CGFloat { get }     static var max: CGFloat { get } } extension CGFloat : _Reflectable { } extension CGFloat : CustomStringConvertible {     var description: String { get } } extension CGFloat : Hashable {     var hashValue: Int { get } } extension CGFloat : FloatLiteralConvertible {     init(floatLiteral value: NativeType) } extension CGFloat : IntegerLiteralConvertible {     init(integerLiteral value: Int) } extension CGFloat : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: CGFloat) -> CGFloat } extension CGFloat : Equatable { } extension CGFloat : Comparable { } extension CGFloat : Strideable {     func distanceTo(_ other: CGFloat) -> CGFloat     func advancedBy(_ amount: CGFloat) -> CGFloat } extension CGFloat : _CVarArgPassedAsDouble, _CVarArgAlignedType { } extension CGFloat : _ObjectiveCBridgeable {     init(_ number: NSNumber) } ``` | AbsoluteValuable, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |

Modified [CGFontPostScriptFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgfontpostscriptformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified CGGlypDeprecatedEnum [enum]

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGImageAlphaInfo [enum]](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGInterpolationQuality [enum]](https://developer.apple.com/documentation/coregraphics/cginterpolationquality)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGLineCap [enum]](https://developer.apple.com/documentation/coregraphics/cglinecap)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGLineJoin [enum]](https://developer.apple.com/documentation/coregraphics/cglinejoin)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPathDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgpathdrawingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPathElementType [enum]](https://developer.apple.com/documentation/coregraphics/cgpathelementtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPatternTiling [enum]](https://developer.apple.com/documentation/coregraphics/cgpatterntiling)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPDFBox [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfbox)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPDFDataFormat [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfdataformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPDFObjectType [enum]](https://developer.apple.com/documentation/coregraphics/cgpdfobjecttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGPoint [struct]](https://developer.apple.com/documentation/coregraphics/cgpoint)

|  | Declaration |
| --- | --- |
| From | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } ``` |
| To | ``` struct CGPoint {     var x: CGFloat     var y: CGFloat     init()     init(x x: CGFloat, y y: CGFloat) } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint { get } } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } extension CGPoint {     static var zero: CGPoint { get }     init(x x: Int, y y: Int)     init(x x: Double, y y: Double)     static var zeroPoint: CGPoint { get } } extension CGPoint : Equatable { } extension CGPoint : _Reflectable { } ``` |

Modified [CGRect [struct]](https://developer.apple.com/documentation/coregraphics/cgrect)

|  | Declaration |
| --- | --- |
| From | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect     static var infiniteRect: CGRect     static var nullRect: CGRect     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect     static var infiniteRect: CGRect     static var nullRect: CGRect     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } ``` |
| To | ``` struct CGRect {     var origin: CGPoint     var size: CGSize     init()     init(origin origin: CGPoint, size size: CGSize) } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect { get }     static var infiniteRect: CGRect { get }     static var nullRect: CGRect { get }     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } extension CGRect {     static var zero: CGRect { get }     static var null: CGRect { get }     static var infinite: CGRect { get }     init(x x: CGFloat, y y: CGFloat, width width: CGFloat, height height: CGFloat)     init(x x: Double, y y: Double, width width: Double, height height: Double)     init(x x: Int, y y: Int, width width: Int, height height: Int)     var width: CGFloat { get }     var height: CGFloat { get }     var minX: CGFloat { get }     var midX: CGFloat { get }     var maxX: CGFloat { get }     var minY: CGFloat { get }     var midY: CGFloat { get }     var maxY: CGFloat { get }     var isNull: Bool { get }     var isEmpty: Bool { get }     var isInfinite: Bool { get }     var standardized: CGRect { get }     var integral: CGRect { get }     mutating func standardizeInPlace()     mutating func makeIntegralInPlace()     @warn_unused_result(mutable_variant="insetInPlace")     func insetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func insetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="offsetInPlace")     func offsetBy(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     mutating func offsetInPlace(dx dx: CGFloat, dy dy: CGFloat)     @warn_unused_result(mutable_variant="unionInPlace")     func union(_ rect: CGRect) -> CGRect     mutating func unionInPlace(_ rect: CGRect)     @warn_unused_result(mutable_variant="intersectInPlace")     func intersect(_ rect: CGRect) -> CGRect     mutating func intersectInPlace(_ rect: CGRect)     @warn_unused_result     func divide(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect)     @warn_unused_result     func contains(_ rect: CGRect) -> Bool     @warn_unused_result     func contains(_ point: CGPoint) -> Bool     @warn_unused_result     func intersects(_ rect: CGRect) -> Bool     static var zeroRect: CGRect { get }     static var infiniteRect: CGRect { get }     static var nullRect: CGRect { get }     var standardizedRect: CGRect { get }     var integerRect: CGRect { get }     mutating func standardize() -> CGRect     mutating func integerize()     func rectByInsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func inset(dx dx: CGFloat, dy dy: CGFloat)     func rectByOffsetting(dx dx: CGFloat, dy dy: CGFloat) -> CGRect     func offset(dx dx: CGFloat, dy dy: CGFloat)     mutating func union(_ withRect: CGRect)     func rectByUnion(_ withRect: CGRect) -> CGRect     mutating func intersect(_ withRect: CGRect)     func rectByIntersecting(_ withRect: CGRect) -> CGRect     func rectsByDividing(_ atDistance: CGFloat, fromEdge fromEdge: CGRectEdge) -> (slice: CGRect, remainder: CGRect) } extension CGRect : Equatable { } extension CGRect : _Reflectable { } ``` |

Modified [CGRectEdge [enum]](https://developer.apple.com/documentation/coregraphics/cgrectedge)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGSize [struct]](https://developer.apple.com/documentation/coregraphics/cgsize)

|  | Declaration |
| --- | --- |
| From | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize } extension CGSize : Equatable { } extension CGSize : _Reflectable { } extension CGSize : _Reflectable { } extension CGSize : Equatable { } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize } ``` |
| To | ``` struct CGSize {     var width: CGFloat     var height: CGFloat     init()     init(width width: CGFloat, height height: CGFloat) } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize { get } } extension CGSize : Equatable { } extension CGSize : _Reflectable { } extension CGSize : _Reflectable { } extension CGSize : Equatable { } extension CGSize {     static var zero: CGSize { get }     init(width width: Int, height height: Int)     init(width width: Double, height height: Double)     static var zeroSize: CGSize { get } } ``` |

Modified [CGTextDrawingMode [enum]](https://developer.apple.com/documentation/coregraphics/cgtextdrawingmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGTextEncoding [enum]](https://developer.apple.com/documentation/coregraphics/cgtextencoding)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CGVector [struct]](https://developer.apple.com/documentation/coregraphics/cgvector)

|  | Declaration |
| --- | --- |
| From | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector } extension CGVector : Equatable { } extension CGVector : Equatable { } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector } ``` |
| To | ``` struct CGVector {     var dx: CGFloat     var dy: CGFloat     init()     init(dx dx: CGFloat, dy dy: CGFloat) } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector { get } } extension CGVector : Equatable { } extension CGVector : Equatable { } extension CGVector {     static var zero: CGVector { get }     init(dx dx: Int, dy dy: Int)     init(dx dx: Double, dy dy: Double)     static var zeroVector: CGVector { get } } ``` |

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

---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/QuartzCore.html
archived_at: '2026-07-18T02:53:41.131988Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# QuartzCore Changes for Swift

### QuartzCore

Removed CAAutoresizingMask.init(_: UInt32)Removed CAConstraint.constraintWithAttribute(_: CAConstraintAttribute, relativeTo: String!, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat) -> AnyObject! [class]Removed CAConstraintLayoutManager.layoutManager() -> AnyObject! [class]Removed CAEdgeAntialiasingMask.init(_: UInt32)Removed CIColor.alpha() -> CGFloatRemoved CIColor.blue() -> CGFloatRemoved CIColor.colorSpace() -> Unmanaged<CGColorSpace>!Removed CIColor.components() -> UnsafePointer<CGFloat>Removed CIColor.green() -> CGFloatRemoved CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat, alpha: CGFloat) -> CIColorRemoved CIColor.numberOfComponents() -> IntRemoved CIColor.red() -> CGFloatRemoved CIColor.stringRepresentation() -> String!Removed CIFilter.apply(_: CIKernel!, args: [AnyObject]!, options: (NSCopying, AnyObject)) -> CIImageRemoved CIFilter.attributes() -> [NSObject : AnyObject]!Removed CIFilter.init(name: String!, elements: (NSCopying, AnyObject))Removed CIFilter.inputKeys() -> [AnyObject]!Removed CIFilter.outputKeys() -> [AnyObject]!Removed CIFilterGenerator.classAttributes() -> [NSObject : AnyObject]!Removed CIFilterGenerator.exportedKeys() -> [NSObject : AnyObject]!Removed CIFilterGenerator.setClassAttributes(_: [NSObject : AnyObject]!)Removed CIFilterShape.shapeWithRect(_: CGRect) -> AnyObject! [class]Removed [CIImage.autoAdjustmentFilters() -> [AnyObject]!](https://developer.apple.com/documentation/coreimage/ciimage/1645889-autoadjustmentfilters)Removed CIImage.colorSpace() -> Unmanaged<CGColorSpace>!Removed CIImage.definition() -> CIFilterShape!Removed CIImage.extent() -> CGRectRemoved CIImage.properties() -> [NSObject : AnyObject]!Removed CIImage.url() -> NSURL!Removed CIImageAccumulator.extent() -> CGRectRemoved CIImageAccumulator.format() -> CIFormatRemoved CIKernel.name() -> String!Removed CISampler.definition() -> CIFilterShape!Removed CISampler.extent() -> CGRectRemoved CISampler.init(im: CIImage!, elements: (NSCopying, AnyObject))Removed CIVector.CGAffineTransformValue() -> CGAffineTransformRemoved CIVector.CGPointValue() -> CGPointRemoved CIVector.CGRectValue() -> CGRectRemoved CIVector.count() -> IntRemoved CIVector.stringRepresentation() -> String!Removed CIVector.W() -> CGFloatRemoved CIVector.X() -> CGFloatRemoved CIVector.Y() -> CGFloatRemoved CIVector.Z() -> CGFloatAdded [CAEmitterCell.contentsScale](https://developer.apple.com/documentation/quartzcore/caemittercell/1522197-contentsscale)Added [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable)Added [CAMetalDrawable.layer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478165-layer)Added [CAMetalDrawable.texture](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478159-texture)Added [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)Added [CAMetalLayer.colorspace](https://developer.apple.com/documentation/quartzcore/cametallayer/1478170-colorspace)Added [CAMetalLayer.device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device)Added [CAMetalLayer.drawableSize](https://developer.apple.com/documentation/quartzcore/cametallayer/1478174-drawablesize)Added [CAMetalLayer.framebufferOnly](https://developer.apple.com/documentation/quartzcore/cametallayer/1478168-framebufferonly)Added [CAMetalLayer.nextDrawable() -> CAMetalDrawable?](https://developer.apple.com/documentation/quartzcore/cametallayer/1478172-nextdrawable)Added [CAMetalLayer.pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat)Added [CAMetalLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/cametallayer/1478157-presentswithtransaction)Added [CAMetalLayer.wantsExtendedDynamicRangeContent](https://developer.apple.com/documentation/quartzcore/cametallayer/1478161-wantsextendeddynamicrangecontent)Added [CAOpenGLLayer.colorspace](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521873-colorspace)Added [CAOpenGLLayer.wantsExtendedDynamicRangeContent](https://developer.apple.com/documentation/quartzcore/caopengllayer/1521900-wantsextendeddynamicrangecontent)Added [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)Added [CASpringAnimation.damping](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412532-damping)Added [CASpringAnimation.initialVelocity](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412443-initialvelocity)Added [CASpringAnimation.mass](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412540-mass)Added [CASpringAnimation.settlingDuration](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412524-settlingduration)Added [CASpringAnimation.stiffness](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412515-stiffness)Added [CATextLayer.allowsFontSubpixelQuantization](https://developer.apple.com/documentation/quartzcore/catextlayer/1515300-allowsfontsubpixelquantization)Modified [CAAction](https://developer.apple.com/documentation/quartzcore/caaction)

|  | Declaration |
| --- | --- |
| From | ``` protocol CAAction {     func runActionForKey(_ event: String!, object anObject: AnyObject!, arguments dict: [NSObject : AnyObject]!) } ``` |
| To | ``` protocol CAAction {     func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) } ``` |

Modified [CAAction.runActionForKey(_: String, object: AnyObject, arguments: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/quartzcore/caaction/1410806-runactionforkey)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func runActionForKey(_ event: String!, object anObject: AnyObject!, arguments dict: [NSObject : AnyObject]!) ``` | OS X 10.10 |
| To | ``` func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) ``` | OS X 10.0 |

Modified [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CAAnimation : NSObject, NSCoding, NSCopying, CAMediaTiming, CAAction {     convenience init!()     class func animation() -> Self!     class func defaultValueForKey(_ key: String!) -> AnyObject!     func shouldArchiveValueForKey(_ key: String!) -> Bool     var timingFunction: CAMediaTimingFunction!     var delegate: AnyObject!     var removedOnCompletion: Bool } extension CAAnimation {     var usesSceneTimeBase: Bool     var fadeInDuration: CGFloat     var fadeOutDuration: CGFloat     var animationEvents: [AnyObject]! } ``` |
| To | ``` class CAAnimation : NSObject, NSCoding, NSCopying, CAMediaTiming, CAAction {     convenience init()     class func animation() -> Self     class func defaultValueForKey(_ key: String) -> AnyObject?     func shouldArchiveValueForKey(_ key: String) -> Bool     var timingFunction: CAMediaTimingFunction?     var delegate: AnyObject?     var removedOnCompletion: Bool } extension CAAnimation {     var usesSceneTimeBase: Bool     var fadeInDuration: CGFloat     var fadeOutDuration: CGFloat     var animationEvents: [SCNAnimationEvent]? } ``` |

Modified [CAAnimation.defaultValueForKey(_: String) -> AnyObject? [class]](https://developer.apple.com/documentation/quartzcore/caanimation/1412530-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |

Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` var delegate: AnyObject! ``` |
| To | ``` var delegate: AnyObject? ``` |

Modified [CAAnimation.shouldArchiveValueForKey(_: String) -> Bool](https://developer.apple.com/documentation/quartzcore/caanimation/1412525-shouldarchivevalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String!) -> Bool ``` |
| To | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |

Modified [CAAnimation.timingFunction](https://developer.apple.com/documentation/quartzcore/caanimation/1412456-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` var timingFunction: CAMediaTimingFunction! ``` |
| To | ``` var timingFunction: CAMediaTimingFunction? ``` |

Modified [CAAnimationGroup](https://developer.apple.com/documentation/quartzcore/caanimationgroup)

|  | Declaration |
| --- | --- |
| From | ``` class CAAnimationGroup : CAAnimation {     var animations: [AnyObject]! } ``` |
| To | ``` class CAAnimationGroup : CAAnimation {     var animations: [CAAnimation]? } ``` |

Modified [CAAnimationGroup.animations](https://developer.apple.com/documentation/quartzcore/caanimationgroup/1412516-animations)

|  | Declaration |
| --- | --- |
| From | ``` var animations: [AnyObject]! ``` |
| To | ``` var animations: [CAAnimation]? ``` |

Modified [CAAutoresizingMask [struct]](https://developer.apple.com/documentation/quartzcore/caautoresizingmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAAutoresizingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerNotSizable: CAAutoresizingMask { get }     static var LayerMinXMargin: CAAutoresizingMask { get }     static var LayerWidthSizable: CAAutoresizingMask { get }     static var LayerMaxXMargin: CAAutoresizingMask { get }     static var LayerMinYMargin: CAAutoresizingMask { get }     static var LayerHeightSizable: CAAutoresizingMask { get }     static var LayerMaxYMargin: CAAutoresizingMask { get } } ``` | RawOptionSetType |
| To | ``` struct CAAutoresizingMask : OptionSetType {     init(rawValue rawValue: UInt32)     static var LayerNotSizable: CAAutoresizingMask { get }     static var LayerMinXMargin: CAAutoresizingMask { get }     static var LayerWidthSizable: CAAutoresizingMask { get }     static var LayerMaxXMargin: CAAutoresizingMask { get }     static var LayerMinYMargin: CAAutoresizingMask { get }     static var LayerHeightSizable: CAAutoresizingMask { get }     static var LayerMaxYMargin: CAAutoresizingMask { get } } ``` | OptionSetType |

Modified [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CABasicAnimation : CAPropertyAnimation {     var fromValue: AnyObject!     var toValue: AnyObject!     var byValue: AnyObject! } ``` |
| To | ``` class CABasicAnimation : CAPropertyAnimation {     var fromValue: AnyObject?     var toValue: AnyObject?     var byValue: AnyObject? } ``` |

Modified [CABasicAnimation.byValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412445-byvalue)

|  | Declaration |
| --- | --- |
| From | ``` var byValue: AnyObject! ``` |
| To | ``` var byValue: AnyObject? ``` |

Modified [CABasicAnimation.fromValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412519-fromvalue)

|  | Declaration |
| --- | --- |
| From | ``` var fromValue: AnyObject! ``` |
| To | ``` var fromValue: AnyObject? ``` |

Modified [CABasicAnimation.toValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412523-tovalue)

|  | Declaration |
| --- | --- |
| From | ``` var toValue: AnyObject! ``` |
| To | ``` var toValue: AnyObject? ``` |

Modified [CAConstraint](https://developer.apple.com/documentation/quartzcore/caconstraint)

|  | Declaration |
| --- | --- |
| From | ``` class CAConstraint : NSObject, NSCoding {     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) -> AnyObject!     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat) -> AnyObject!     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute) -> AnyObject!     init!(attribute attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)     var attribute: CAConstraintAttribute { get }     var sourceName: String! { get }     var sourceAttribute: CAConstraintAttribute { get }     var scale: CGFloat { get }     var offset: CGFloat { get } } ``` |
| To | ``` class CAConstraint : NSObject, NSCoding {     convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) -> Self     convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat)     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat) -> Self     convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute)     class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute) -> Self     init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat)     var attribute: CAConstraintAttribute { get }     var sourceName: String { get }     var sourceAttribute: CAConstraintAttribute { get }     var scale: CGFloat { get }     var offset: CGFloat { get } } ``` |

Modified [CAConstraint.init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute)](https://developer.apple.com/documentation/quartzcore/caconstraint/1521924-init)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | constraintWithAttribute(_:relativeTo:attribute:) | ``` class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute) -> AnyObject! ``` | OS X 10.10 |
| To | init(attribute:relativeTo:attribute:) | ``` convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute) ``` | OS X 10.11 |

Modified [CAConstraint.init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, offset: CGFloat)](https://developer.apple.com/documentation/quartzcore/caconstraint/1522328-constraintwithattribute)

|  | Name | Declaration | Introduction |
| --- | --- | --- | --- |
| From | constraintWithAttribute(_:relativeTo:attribute:offset:) | ``` class func constraintWithAttribute(_ attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat) -> AnyObject! ``` | OS X 10.10 |
| To | init(attribute:relativeTo:attribute:offset:) | ``` convenience init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, offset c: CGFloat) ``` | OS X 10.11 |

Modified [CAConstraint.init(attribute: CAConstraintAttribute, relativeTo: String, attribute: CAConstraintAttribute, scale: CGFloat, offset: CGFloat)](https://developer.apple.com/documentation/quartzcore/caconstraint/1522213-initwithattribute)

|  | Declaration |
| --- | --- |
| From | ``` init!(attribute attr: CAConstraintAttribute, relativeTo srcId: String!, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) ``` |
| To | ``` init(attribute attr: CAConstraintAttribute, relativeTo srcId: String, attribute srcAttr: CAConstraintAttribute, scale m: CGFloat, offset c: CGFloat) ``` |

Modified [CAConstraint.sourceName](https://developer.apple.com/documentation/quartzcore/caconstraint/1522224-sourcename)

|  | Declaration |
| --- | --- |
| From | ``` var sourceName: String! { get } ``` |
| To | ``` var sourceName: String { get } ``` |

Modified [CAConstraintAttribute [enum]](https://developer.apple.com/documentation/quartzcore/caconstraintattribute)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int32 |

Modified [CAConstraintLayoutManager](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` class CAConstraintLayoutManager : NSObject {     class func layoutManager() -> AnyObject! } ``` |
| To | ``` class CAConstraintLayoutManager : NSObject {     convenience init()     class func layoutManager() -> Self } ``` |

Modified [CAEdgeAntialiasingMask [struct]](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAEdgeAntialiasingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | RawOptionSetType |
| To | ``` struct CAEdgeAntialiasingMask : OptionSetType {     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | OptionSetType |

Modified CAEmitterBehavior

|  | Declaration |
| --- | --- |
| From | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [AnyObject]!     init!(type type: String!) -> CAEmitterBehavior     class func behaviorWithType(_ type: String!) -> CAEmitterBehavior!     init!(type type: String!)     var type: String! { get }     var name: String!     var enabled: Bool     func inputKeys() -> [AnyObject]!     class func attributesForKey(_ key: String!) -> [NSObject : AnyObject]!     func attributesForKeyPath(_ keyPath: String!) -> [NSObject : AnyObject]! } ``` |
| To | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [String]      init(type type: String)     class func behaviorWithType(_ type: String) -> CAEmitterBehavior     init(type type: String)     var type: String { get }     var name: String?     var enabled: Bool     func inputKeys() -> [AnyObject]     class func attributesForKey(_ key: String) -> [NSObject : AnyObject]     func attributesForKeyPath(_ keyPath: String) -> [NSObject : AnyObject] } ``` |

Modified CAEmitterBehavior.attributesForKey(_: String) -> [NSObject : AnyObject] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func attributesForKey(_ key: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` class func attributesForKey(_ key: String) -> [NSObject : AnyObject] ``` |

Modified CAEmitterBehavior.attributesForKeyPath(_: String) -> [NSObject : AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func attributesForKeyPath(_ keyPath: String!) -> [NSObject : AnyObject]! ``` |
| To | ``` func attributesForKeyPath(_ keyPath: String) -> [NSObject : AnyObject] ``` |

Modified CAEmitterBehavior.behaviorTypes() -> [String] [class]

|  | Declaration |
| --- | --- |
| From | ``` class func behaviorTypes() -> [AnyObject]! ``` |
| To | ``` class func behaviorTypes() -> [String] ``` |

Modified CAEmitterBehavior.init(type: String)

|  | Declaration |
| --- | --- |
| From | ``` init!(type type: String!) ``` |
| To | ``` init(type type: String) ``` |

Modified CAEmitterBehavior.inputKeys() -> [AnyObject]

|  | Declaration |
| --- | --- |
| From | ``` func inputKeys() -> [AnyObject]! ``` |
| To | ``` func inputKeys() -> [AnyObject] ``` |

Modified CAEmitterBehavior.name

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified CAEmitterBehavior.type

|  | Declaration |
| --- | --- |
| From | ``` var type: String! { get } ``` |
| To | ``` var type: String { get } ``` |

Modified [CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell)

|  | Declaration |
| --- | --- |
| From | ``` class CAEmitterCell : NSObject, NSCoding, CAMediaTiming {     convenience init!()     class func emitterCell() -> Self!     class func defaultValueForKey(_ key: String!) -> AnyObject!     func shouldArchiveValueForKey(_ key: String!) -> Bool     var name: String!     var enabled: Bool     var birthRate: Float     var lifetime: Float     var lifetimeRange: Float     var emissionLatitude: CGFloat     var emissionLongitude: CGFloat     var emissionRange: CGFloat     var velocity: CGFloat     var velocityRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var zAcceleration: CGFloat     var scale: CGFloat     var scaleRange: CGFloat     var scaleSpeed: CGFloat     var spin: CGFloat     var spinRange: CGFloat     var color: CGColor!     var redRange: Float     var greenRange: Float     var blueRange: Float     var alphaRange: Float     var redSpeed: Float     var greenSpeed: Float     var blueSpeed: Float     var alphaSpeed: Float     var contents: AnyObject!     var contentsRect: CGRect     var minificationFilter: String!     var magnificationFilter: String!     var minificationFilterBias: Float     var emitterCells: [AnyObject]!     var style: [NSObject : AnyObject]! } ``` |
| To | ``` class CAEmitterCell : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func emitterCell() -> Self     class func defaultValueForKey(_ key: String) -> AnyObject?     func shouldArchiveValueForKey(_ key: String) -> Bool     var name: String?     var enabled: Bool     var birthRate: Float     var lifetime: Float     var lifetimeRange: Float     var emissionLatitude: CGFloat     var emissionLongitude: CGFloat     var emissionRange: CGFloat     var velocity: CGFloat     var velocityRange: CGFloat     var xAcceleration: CGFloat     var yAcceleration: CGFloat     var zAcceleration: CGFloat     var scale: CGFloat     var scaleRange: CGFloat     var scaleSpeed: CGFloat     var spin: CGFloat     var spinRange: CGFloat     var color: CGColor?     var redRange: Float     var greenRange: Float     var blueRange: Float     var alphaRange: Float     var redSpeed: Float     var greenSpeed: Float     var blueSpeed: Float     var alphaSpeed: Float     var contents: AnyObject?     var contentsRect: CGRect     var contentsScale: CGFloat     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var emitterCells: [CAEmitterCell]?     var style: [NSObject : AnyObject]? } ``` |

Modified [CAEmitterCell.color](https://developer.apple.com/documentation/quartzcore/caemittercell/1522322-color)

|  | Declaration |
| --- | --- |
| From | ``` var color: CGColor! ``` |
| To | ``` var color: CGColor? ``` |

Modified [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)

|  | Declaration |
| --- | --- |
| From | ``` var contents: AnyObject! ``` |
| To | ``` var contents: AnyObject? ``` |

Modified [CAEmitterCell.defaultValueForKey(_: String) -> AnyObject? [class]](https://developer.apple.com/documentation/quartzcore/caemittercell/1521964-defaultvalue)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |

Modified [CAEmitterCell.emitterCells](https://developer.apple.com/documentation/quartzcore/caemittercell/1521866-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` var emitterCells: [AnyObject]! ``` |
| To | ``` var emitterCells: [CAEmitterCell]? ``` |

Modified [CAEmitterCell.magnificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522228-magnificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` var magnificationFilter: String! ``` |
| To | ``` var magnificationFilter: String ``` |

Modified [CAEmitterCell.minificationFilter](https://developer.apple.com/documentation/quartzcore/caemittercell/1522222-minificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` var minificationFilter: String! ``` |
| To | ``` var minificationFilter: String ``` |

Modified [CAEmitterCell.name](https://developer.apple.com/documentation/quartzcore/caemittercell/1521909-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [CAEmitterCell.shouldArchiveValueForKey(_: String) -> Bool](https://developer.apple.com/documentation/quartzcore/caemittercell/1522005-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String!) -> Bool ``` |
| To | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |

Modified [CAEmitterCell.style](https://developer.apple.com/documentation/quartzcore/caemittercell/1521925-style)

|  | Declaration |
| --- | --- |
| From | ``` var style: [NSObject : AnyObject]! ``` |
| To | ``` var style: [NSObject : AnyObject]? ``` |

Modified [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAEmitterLayer : CALayer {     var emitterCells: [AnyObject]!     var birthRate: Float     var lifetime: Float     var emitterPosition: CGPoint     var emitterZPosition: CGFloat     var emitterSize: CGSize     var emitterDepth: CGFloat     var emitterShape: String!     var emitterMode: String!     var renderMode: String!     var preservesDepth: Bool     var velocity: Float     var scale: Float     var spin: Float     var seed: UInt32 } ``` |
| To | ``` class CAEmitterLayer : CALayer {     var emitterCells: [CAEmitterCell]?     var birthRate: Float     var lifetime: Float     var emitterPosition: CGPoint     var emitterZPosition: CGFloat     var emitterSize: CGSize     var emitterDepth: CGFloat     var emitterShape: String     var emitterMode: String     var renderMode: String     var preservesDepth: Bool     var velocity: Float     var scale: Float     var spin: Float     var seed: UInt32 } ``` |

Modified [CAEmitterLayer.emitterCells](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521923-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` var emitterCells: [AnyObject]! ``` |
| To | ``` var emitterCells: [CAEmitterCell]? ``` |

Modified [CAEmitterLayer.emitterMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522128-emittermode)

|  | Declaration |
| --- | --- |
| From | ``` var emitterMode: String! ``` |
| To | ``` var emitterMode: String ``` |

Modified [CAEmitterLayer.emitterShape](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521919-emittershape)

|  | Declaration |
| --- | --- |
| From | ``` var emitterShape: String! ``` |
| To | ``` var emitterShape: String ``` |

Modified [CAEmitterLayer.renderMode](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1522104-rendermode)

|  | Declaration |
| --- | --- |
| From | ``` var renderMode: String! ``` |
| To | ``` var renderMode: String ``` |

Modified [CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAGradientLayer : CALayer {     var colors: [AnyObject]!     var locations: [AnyObject]!     var startPoint: CGPoint     var endPoint: CGPoint     var type: String! } ``` |
| To | ``` class CAGradientLayer : CALayer {     var colors: [AnyObject]?     var locations: [NSNumber]?     var startPoint: CGPoint     var endPoint: CGPoint     var type: String } ``` |

Modified [CAGradientLayer.colors](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462403-colors)

|  | Declaration |
| --- | --- |
| From | ``` var colors: [AnyObject]! ``` |
| To | ``` var colors: [AnyObject]? ``` |

Modified [CAGradientLayer.locations](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462410-locations)

|  | Declaration |
| --- | --- |
| From | ``` var locations: [AnyObject]! ``` |
| To | ``` var locations: [NSNumber]? ``` |

Modified [CAGradientLayer.type](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462413-type)

|  | Declaration |
| --- | --- |
| From | ``` var type: String! ``` |
| To | ``` var type: String ``` |

Modified [CAKeyframeAnimation](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CAKeyframeAnimation : CAPropertyAnimation {     var values: [AnyObject]!     var path: CGPath!     var keyTimes: [AnyObject]!     var timingFunctions: [AnyObject]!     var calculationMode: String!     var tensionValues: [AnyObject]!     var continuityValues: [AnyObject]!     var biasValues: [AnyObject]!     var rotationMode: String! } ``` |
| To | ``` class CAKeyframeAnimation : CAPropertyAnimation {     var values: [AnyObject]?     var path: CGPath?     var keyTimes: [NSNumber]?     var timingFunctions: [CAMediaTimingFunction]?     var calculationMode: String     var tensionValues: [NSNumber]?     var continuityValues: [NSNumber]?     var biasValues: [NSNumber]?     var rotationMode: String? } ``` |

Modified [CAKeyframeAnimation.biasValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412485-biasvalues)

|  | Declaration |
| --- | --- |
| From | ``` var biasValues: [AnyObject]! ``` |
| To | ``` var biasValues: [NSNumber]? ``` |

Modified [CAKeyframeAnimation.calculationMode](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412500-calculationmode)

|  | Declaration |
| --- | --- |
| From | ``` var calculationMode: String! ``` |
| To | ``` var calculationMode: String ``` |

Modified [CAKeyframeAnimation.continuityValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412491-continuityvalues)

|  | Declaration |
| --- | --- |
| From | ``` var continuityValues: [AnyObject]! ``` |
| To | ``` var continuityValues: [NSNumber]? ``` |

Modified [CAKeyframeAnimation.keyTimes](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412522-keytimes)

|  | Declaration |
| --- | --- |
| From | ``` var keyTimes: [AnyObject]! ``` |
| To | ``` var keyTimes: [NSNumber]? ``` |

Modified [CAKeyframeAnimation.path](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412474-path)

|  | Declaration |
| --- | --- |
| From | ``` var path: CGPath! ``` |
| To | ``` var path: CGPath? ``` |

Modified [CAKeyframeAnimation.rotationMode](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412454-rotationmode)

|  | Declaration |
| --- | --- |
| From | ``` var rotationMode: String! ``` |
| To | ``` var rotationMode: String? ``` |

Modified [CAKeyframeAnimation.tensionValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412475-tensionvalues)

|  | Declaration |
| --- | --- |
| From | ``` var tensionValues: [AnyObject]! ``` |
| To | ``` var tensionValues: [NSNumber]? ``` |

Modified [CAKeyframeAnimation.timingFunctions](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412465-timingfunctions)

|  | Declaration |
| --- | --- |
| From | ``` var timingFunctions: [AnyObject]! ``` |
| To | ``` var timingFunctions: [CAMediaTimingFunction]? ``` |

Modified [CAKeyframeAnimation.values](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412498-values)

|  | Declaration |
| --- | --- |
| From | ``` var values: [AnyObject]! ``` |
| To | ``` var values: [AnyObject]? ``` |

Modified [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)

|  | Declaration |
| --- | --- |
| From | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init!()     class func layer() -> Self!     init!()     init!(layer layer: AnyObject!)     func presentationLayer() -> AnyObject!     func modelLayer() -> AnyObject!     class func defaultValueForKey(_ key: String!) -> AnyObject!     class func needsDisplayForKey(_ key: String!) -> Bool     func shouldArchiveValueForKey(_ key: String!) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var hidden: Bool     var doubleSided: Bool     var geometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer! { get }     func removeFromSuperlayer()     var sublayers: [AnyObject]!     func addSublayer(_ layer: CALayer!)     func insertSublayer(_ layer: CALayer!, atIndex idx: UInt32)     func insertSublayer(_ layer: CALayer!, below sibling: CALayer!)     func insertSublayer(_ layer: CALayer!, above sibling: CALayer!)     func replaceSublayer(_ layer: CALayer!, with layer2: CALayer!)     var sublayerTransform: CATransform3D     var mask: CALayer!     var masksToBounds: Bool     func convertPoint(_ p: CGPoint, fromLayer l: CALayer!) -> CGPoint     func convertPoint(_ p: CGPoint, toLayer l: CALayer!) -> CGPoint     func convertRect(_ r: CGRect, fromLayer l: CALayer!) -> CGRect     func convertRect(_ r: CGRect, toLayer l: CALayer!) -> CGRect     func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer!) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, toLayer l: CALayer!) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer!     func containsPoint(_ p: CGPoint) -> Bool     var contents: AnyObject!     var contentsRect: CGRect     var contentsGravity: String!     var contentsScale: CGFloat     var contentsCenter: CGRect     var minificationFilter: String!     var magnificationFilter: String!     var minificationFilterBias: Float     var opaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayInRect(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func drawInContext(_ ctx: CGContext!)     func renderInContext(_ ctx: CGContext!)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var backgroundColor: CGColor!     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor!     var opacity: Float     var compositingFilter: AnyObject!     var filters: [AnyObject]!     var backgroundFilters: [AnyObject]!     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor!     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath!     var autoresizingMask: CAAutoresizingMask     var layoutManager: AnyObject!     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     func resizeSublayersWithOldSize(_ size: CGSize)     func resizeWithOldSuperlayerSize(_ size: CGSize)     class func defaultActionForKey(_ event: String!) -> CAAction!     func actionForKey(_ event: String!) -> CAAction!     var actions: [NSObject : AnyObject]!     func addAnimation(_ anim: CAAnimation!, forKey key: String!)     func removeAllAnimations()     func removeAnimationForKey(_ key: String!)     func animationKeys() -> [AnyObject]!     func animationForKey(_ key: String!) -> CAAnimation!     var name: String!     weak var delegate: AnyObject!     var style: [NSObject : AnyObject]! } extension CALayer {     var constraints: [AnyObject]!     func addConstraint(_ c: CAConstraint!) } extension CALayer {     init!(remoteClientId client_id: UInt32) -> CALayer     class func layerWithRemoteClientId(_ client_id: UInt32) -> CALayer! } extension CALayer {     func scrollPoint(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` |
| To | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func layer() -> Self     init()     init(layer layer: AnyObject)     func presentationLayer() -> AnyObject?     func modelLayer() -> AnyObject     class func defaultValueForKey(_ key: String) -> AnyObject?     class func needsDisplayForKey(_ key: String) -> Bool     func shouldArchiveValueForKey(_ key: String) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var hidden: Bool     var doubleSided: Bool     var geometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer? { get }     func removeFromSuperlayer()     var sublayers: [CALayer]?     func addSublayer(_ layer: CALayer)     func insertSublayer(_ layer: CALayer, atIndex idx: UInt32)     func insertSublayer(_ layer: CALayer, below sibling: CALayer?)     func insertSublayer(_ layer: CALayer, above sibling: CALayer?)     func replaceSublayer(_ layer: CALayer, with layer2: CALayer)     var sublayerTransform: CATransform3D     var mask: CALayer?     var masksToBounds: Bool     func convertPoint(_ p: CGPoint, fromLayer l: CALayer?) -> CGPoint     func convertPoint(_ p: CGPoint, toLayer l: CALayer?) -> CGPoint     func convertRect(_ r: CGRect, fromLayer l: CALayer?) -> CGRect     func convertRect(_ r: CGRect, toLayer l: CALayer?) -> CGRect     func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer?) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, toLayer l: CALayer?) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer?     func containsPoint(_ p: CGPoint) -> Bool     var contents: AnyObject?     var contentsRect: CGRect     var contentsGravity: String     var contentsScale: CGFloat     var contentsCenter: CGRect     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var opaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayInRect(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func drawInContext(_ ctx: CGContext)     func renderInContext(_ ctx: CGContext)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var backgroundColor: CGColor?     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor?     var opacity: Float     var compositingFilter: AnyObject?     var filters: [AnyObject]?     var backgroundFilters: [AnyObject]?     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor?     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath?     var autoresizingMask: CAAutoresizingMask     var layoutManager: AnyObject?     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     func resizeSublayersWithOldSize(_ size: CGSize)     func resizeWithOldSuperlayerSize(_ size: CGSize)     class func defaultActionForKey(_ event: String) -> CAAction?     func actionForKey(_ event: String) -> CAAction?     var actions: [String : CAAction]?     func addAnimation(_ anim: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimationForKey(_ key: String)     func animationKeys() -> [String]?     func animationForKey(_ key: String) -> CAAnimation?     var name: String?     weak var delegate: AnyObject?     var style: [NSObject : AnyObject]? } extension CALayer {     var constraints: [CAConstraint]?     func addConstraint(_ c: CAConstraint) } extension CALayer {      init(remoteClientId client_id: UInt32)     class func layerWithRemoteClientId(_ client_id: UInt32) -> CALayer } extension CALayer {     func scrollPoint(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` |

Modified [CALayer.actionForKey(_: String) -> CAAction?](https://developer.apple.com/documentation/quartzcore/calayer/1410844-action)

|  | Declaration |
| --- | --- |
| From | ``` func actionForKey(_ event: String!) -> CAAction! ``` |
| To | ``` func actionForKey(_ event: String) -> CAAction? ``` |

Modified [CALayer.actions](https://developer.apple.com/documentation/quartzcore/calayer/1410789-actions)

|  | Declaration |
| --- | --- |
| From | ``` var actions: [NSObject : AnyObject]! ``` |
| To | ``` var actions: [String : CAAction]? ``` |

Modified [CALayer.addAnimation(_: CAAnimation, forKey: String?)](https://developer.apple.com/documentation/quartzcore/calayer/1410848-addanimation)

|  | Declaration |
| --- | --- |
| From | ``` func addAnimation(_ anim: CAAnimation!, forKey key: String!) ``` |
| To | ``` func addAnimation(_ anim: CAAnimation, forKey key: String?) ``` |

Modified [CALayer.addConstraint(_: CAConstraint)](https://developer.apple.com/documentation/quartzcore/calayer/1521899-addconstraint)

|  | Declaration |
| --- | --- |
| From | ``` func addConstraint(_ c: CAConstraint!) ``` |
| To | ``` func addConstraint(_ c: CAConstraint) ``` |

Modified [CALayer.addSublayer(_: CALayer)](https://developer.apple.com/documentation/quartzcore/calayer/1410833-addsublayer)

|  | Declaration |
| --- | --- |
| From | ``` func addSublayer(_ layer: CALayer!) ``` |
| To | ``` func addSublayer(_ layer: CALayer) ``` |

Modified [CALayer.animationForKey(_: String) -> CAAnimation?](https://developer.apple.com/documentation/quartzcore/calayer/1410808-animation)

|  | Declaration |
| --- | --- |
| From | ``` func animationForKey(_ key: String!) -> CAAnimation! ``` |
| To | ``` func animationForKey(_ key: String) -> CAAnimation? ``` |

Modified [CALayer.animationKeys() -> [String]?](https://developer.apple.com/documentation/quartzcore/calayer/1410937-animationkeys)

|  | Declaration |
| --- | --- |
| From | ``` func animationKeys() -> [AnyObject]! ``` |
| To | ``` func animationKeys() -> [String]? ``` |

Modified [CALayer.backgroundColor](https://developer.apple.com/documentation/quartzcore/calayer/1410966-backgroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundColor: CGColor! ``` |
| To | ``` var backgroundColor: CGColor? ``` |

Modified [CALayer.backgroundFilters](https://developer.apple.com/documentation/quartzcore/calayer/1410827-backgroundfilters)

|  | Declaration |
| --- | --- |
| From | ``` var backgroundFilters: [AnyObject]! ``` |
| To | ``` var backgroundFilters: [AnyObject]? ``` |

Modified [CALayer.borderColor](https://developer.apple.com/documentation/quartzcore/calayer/1410903-bordercolor)

|  | Declaration |
| --- | --- |
| From | ``` var borderColor: CGColor! ``` |
| To | ``` var borderColor: CGColor? ``` |

Modified [CALayer.compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter)

|  | Declaration |
| --- | --- |
| From | ``` var compositingFilter: AnyObject! ``` |
| To | ``` var compositingFilter: AnyObject? ``` |

Modified [CALayer.constraints](https://developer.apple.com/documentation/quartzcore/calayer/1521906-constraints)

|  | Declaration |
| --- | --- |
| From | ``` var constraints: [AnyObject]! ``` |
| To | ``` var constraints: [CAConstraint]? ``` |

Modified [CALayer.contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents)

|  | Declaration |
| --- | --- |
| From | ``` var contents: AnyObject! ``` |
| To | ``` var contents: AnyObject? ``` |

Modified [CALayer.contentsGravity](https://developer.apple.com/documentation/quartzcore/calayer/1410872-contentsgravity)

|  | Declaration |
| --- | --- |
| From | ``` var contentsGravity: String! ``` |
| To | ``` var contentsGravity: String ``` |

Modified [CALayer.contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.7 |

Modified [CALayer.convertPoint(_: CGPoint, fromLayer: CALayer?) -> CGPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410825-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ p: CGPoint, fromLayer l: CALayer!) -> CGPoint ``` |
| To | ``` func convertPoint(_ p: CGPoint, fromLayer l: CALayer?) -> CGPoint ``` |

Modified [CALayer.convertPoint(_: CGPoint, toLayer: CALayer?) -> CGPoint](https://developer.apple.com/documentation/quartzcore/calayer/1410881-convertpoint)

|  | Declaration |
| --- | --- |
| From | ``` func convertPoint(_ p: CGPoint, toLayer l: CALayer!) -> CGPoint ``` |
| To | ``` func convertPoint(_ p: CGPoint, toLayer l: CALayer?) -> CGPoint ``` |

Modified [CALayer.convertRect(_: CGRect, fromLayer: CALayer?) -> CGRect](https://developer.apple.com/documentation/quartzcore/calayer/1410948-convert)

|  | Declaration |
| --- | --- |
| From | ``` func convertRect(_ r: CGRect, fromLayer l: CALayer!) -> CGRect ``` |
| To | ``` func convertRect(_ r: CGRect, fromLayer l: CALayer?) -> CGRect ``` |

Modified [CALayer.convertRect(_: CGRect, toLayer: CALayer?) -> CGRect](https://developer.apple.com/documentation/quartzcore/calayer/1410742-convertrect)

|  | Declaration |
| --- | --- |
| From | ``` func convertRect(_ r: CGRect, toLayer l: CALayer!) -> CGRect ``` |
| To | ``` func convertRect(_ r: CGRect, toLayer l: CALayer?) -> CGRect ``` |

Modified [CALayer.convertTime(_: CFTimeInterval, fromLayer: CALayer?) -> CFTimeInterval](https://developer.apple.com/documentation/quartzcore/calayer/1410821-converttime)

|  | Declaration |
| --- | --- |
| From | ``` func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer!) -> CFTimeInterval ``` |
| To | ``` func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer?) -> CFTimeInterval ``` |

Modified [CALayer.convertTime(_: CFTimeInterval, toLayer: CALayer?) -> CFTimeInterval](https://developer.apple.com/documentation/quartzcore/calayer/1410823-converttime)

|  | Declaration |
| --- | --- |
| From | ``` func convertTime(_ t: CFTimeInterval, toLayer l: CALayer!) -> CFTimeInterval ``` |
| To | ``` func convertTime(_ t: CFTimeInterval, toLayer l: CALayer?) -> CFTimeInterval ``` |

Modified [CALayer.defaultActionForKey(_: String) -> CAAction? [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410954-defaultaction)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultActionForKey(_ event: String!) -> CAAction! ``` |
| To | ``` class func defaultActionForKey(_ event: String) -> CAAction? ``` |

Modified [CALayer.defaultValueForKey(_: String) -> AnyObject? [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410886-defaultvalueforkey)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultValueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` class func defaultValueForKey(_ key: String) -> AnyObject? ``` |

Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: AnyObject! ``` |
| To | ``` weak var delegate: AnyObject? ``` |

Modified [CALayer.drawInContext(_: CGContext)](https://developer.apple.com/documentation/quartzcore/calayer/1410757-drawincontext)

|  | Declaration |
| --- | --- |
| From | ``` func drawInContext(_ ctx: CGContext!) ``` |
| To | ``` func drawInContext(_ ctx: CGContext) ``` |

Modified [CALayer.drawsAsynchronously](https://developer.apple.com/documentation/quartzcore/calayer/1410974-drawsasynchronously)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified [CALayer.filters](https://developer.apple.com/documentation/quartzcore/calayer/1410901-filters)

|  | Declaration |
| --- | --- |
| From | ``` var filters: [AnyObject]! ``` |
| To | ``` var filters: [AnyObject]? ``` |

Modified [CALayer.hitTest(_: CGPoint) -> CALayer?](https://developer.apple.com/documentation/quartzcore/calayer/1410972-hittest)

|  | Declaration |
| --- | --- |
| From | ``` func hitTest(_ p: CGPoint) -> CALayer! ``` |
| To | ``` func hitTest(_ p: CGPoint) -> CALayer? ``` |

Modified [CALayer.init()](https://developer.apple.com/documentation/quartzcore/calayer/1410835-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [CALayer.init(layer: AnyObject)](https://developer.apple.com/documentation/quartzcore/calayer/1410842-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(layer layer: AnyObject!) ``` |
| To | ``` init(layer layer: AnyObject) ``` |

Modified [CALayer.init(remoteClientId: UInt32)](https://developer.apple.com/documentation/quartzcore/calayer/1522119-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(remoteClientId client_id: UInt32) -> CALayer ``` |
| To | ``` init(remoteClientId client_id: UInt32) ``` |

Modified [CALayer.insertSublayer(_: CALayer, above: CALayer?)](https://developer.apple.com/documentation/quartzcore/calayer/1410798-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` func insertSublayer(_ layer: CALayer!, above sibling: CALayer!) ``` |
| To | ``` func insertSublayer(_ layer: CALayer, above sibling: CALayer?) ``` |

Modified [CALayer.insertSublayer(_: CALayer, atIndex: UInt32)](https://developer.apple.com/documentation/quartzcore/calayer/1410944-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` func insertSublayer(_ layer: CALayer!, atIndex idx: UInt32) ``` |
| To | ``` func insertSublayer(_ layer: CALayer, atIndex idx: UInt32) ``` |

Modified [CALayer.insertSublayer(_: CALayer, below: CALayer?)](https://developer.apple.com/documentation/quartzcore/calayer/1410840-insertsublayer)

|  | Declaration |
| --- | --- |
| From | ``` func insertSublayer(_ layer: CALayer!, below sibling: CALayer!) ``` |
| To | ``` func insertSublayer(_ layer: CALayer, below sibling: CALayer?) ``` |

Modified [CALayer.layoutManager](https://developer.apple.com/documentation/quartzcore/calayer/1410749-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` var layoutManager: AnyObject! ``` |
| To | ``` var layoutManager: AnyObject? ``` |

Modified [CALayer.magnificationFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410907-magnificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` var magnificationFilter: String! ``` |
| To | ``` var magnificationFilter: String ``` |

Modified [CALayer.mask](https://developer.apple.com/documentation/quartzcore/calayer/1410861-mask)

|  | Declaration |
| --- | --- |
| From | ``` var mask: CALayer! ``` |
| To | ``` var mask: CALayer? ``` |

Modified [CALayer.minificationFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410898-minificationfilter)

|  | Declaration |
| --- | --- |
| From | ``` var minificationFilter: String! ``` |
| To | ``` var minificationFilter: String ``` |

Modified [CALayer.modelLayer() -> AnyObject](https://developer.apple.com/documentation/quartzcore/calayer/1410853-model)

|  | Declaration |
| --- | --- |
| From | ``` func modelLayer() -> AnyObject! ``` |
| To | ``` func modelLayer() -> AnyObject ``` |

Modified [CALayer.name](https://developer.apple.com/documentation/quartzcore/calayer/1410879-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! ``` |
| To | ``` var name: String? ``` |

Modified [CALayer.needsDisplayForKey(_: String) -> Bool [class]](https://developer.apple.com/documentation/quartzcore/calayer/1410769-needsdisplay)

|  | Declaration |
| --- | --- |
| From | ``` class func needsDisplayForKey(_ key: String!) -> Bool ``` |
| To | ``` class func needsDisplayForKey(_ key: String) -> Bool ``` |

Modified [CALayer.presentationLayer() -> AnyObject?](https://developer.apple.com/documentation/quartzcore/calayer/1410744-presentation)

|  | Declaration |
| --- | --- |
| From | ``` func presentationLayer() -> AnyObject! ``` |
| To | ``` func presentationLayer() -> AnyObject? ``` |

Modified [CALayer.removeAnimationForKey(_: String)](https://developer.apple.com/documentation/quartzcore/calayer/1410939-removeanimationforkey)

|  | Declaration |
| --- | --- |
| From | ``` func removeAnimationForKey(_ key: String!) ``` |
| To | ``` func removeAnimationForKey(_ key: String) ``` |

Modified [CALayer.renderInContext(_: CGContext)](https://developer.apple.com/documentation/quartzcore/calayer/1410909-render)

|  | Declaration |
| --- | --- |
| From | ``` func renderInContext(_ ctx: CGContext!) ``` |
| To | ``` func renderInContext(_ ctx: CGContext) ``` |

Modified [CALayer.replaceSublayer(_: CALayer, with: CALayer)](https://developer.apple.com/documentation/quartzcore/calayer/1410820-replacesublayer)

|  | Declaration |
| --- | --- |
| From | ``` func replaceSublayer(_ layer: CALayer!, with layer2: CALayer!) ``` |
| To | ``` func replaceSublayer(_ layer: CALayer, with layer2: CALayer) ``` |

Modified [CALayer.shadowColor](https://developer.apple.com/documentation/quartzcore/calayer/1410829-shadowcolor)

|  | Declaration |
| --- | --- |
| From | ``` var shadowColor: CGColor! ``` |
| To | ``` var shadowColor: CGColor? ``` |

Modified [CALayer.shadowPath](https://developer.apple.com/documentation/quartzcore/calayer/1410771-shadowpath)

|  | Declaration |
| --- | --- |
| From | ``` var shadowPath: CGPath! ``` |
| To | ``` var shadowPath: CGPath? ``` |

Modified [CALayer.shouldArchiveValueForKey(_: String) -> Bool](https://developer.apple.com/documentation/quartzcore/calayer/1410753-shouldarchivevalue)

|  | Declaration |
| --- | --- |
| From | ``` func shouldArchiveValueForKey(_ key: String!) -> Bool ``` |
| To | ``` func shouldArchiveValueForKey(_ key: String) -> Bool ``` |

Modified [CALayer.style](https://developer.apple.com/documentation/quartzcore/calayer/1410875-style)

|  | Declaration |
| --- | --- |
| From | ``` var style: [NSObject : AnyObject]! ``` |
| To | ``` var style: [NSObject : AnyObject]? ``` |

Modified [CALayer.sublayers](https://developer.apple.com/documentation/quartzcore/calayer/1410802-sublayers)

|  | Declaration |
| --- | --- |
| From | ``` var sublayers: [AnyObject]! ``` |
| To | ``` var sublayers: [CALayer]? ``` |

Modified [CALayer.superlayer](https://developer.apple.com/documentation/quartzcore/calayer/1410761-superlayer)

|  | Declaration |
| --- | --- |
| From | ``` var superlayer: CALayer! { get } ``` |
| To | ``` var superlayer: CALayer? { get } ``` |

Modified [CAMediaTiming](https://developer.apple.com/documentation/quartzcore/camediatiming)

|  | Declaration |
| --- | --- |
| From | ``` protocol CAMediaTiming {     var beginTime: CFTimeInterval { get set }     var duration: CFTimeInterval { get set }     var speed: Float { get set }     var timeOffset: CFTimeInterval { get set }     var repeatCount: Float { get set }     var repeatDuration: CFTimeInterval { get set }     var autoreverses: Bool { get set }     var fillMode: String! { get set } } ``` |
| To | ``` protocol CAMediaTiming {     var beginTime: CFTimeInterval { get set }     var duration: CFTimeInterval { get set }     var speed: Float { get set }     var timeOffset: CFTimeInterval { get set }     var repeatCount: Float { get set }     var repeatDuration: CFTimeInterval { get set }     var autoreverses: Bool { get set }     var fillMode: String { get set } } ``` |

Modified [CAMediaTiming.fillMode](https://developer.apple.com/documentation/quartzcore/camediatiming/1427656-fillmode)

|  | Declaration |
| --- | --- |
| From | ``` var fillMode: String! { get set } ``` |
| To | ``` var fillMode: String { get set } ``` |

Modified [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` class CAMediaTimingFunction : NSObject, NSCoding {     convenience init!(name name: String!)     class func functionWithName(_ name: String!) -> Self!     convenience init!(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     class func functionWithControlPoints(_ c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) -> Self!     init!(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) } ``` |
| To | ``` class CAMediaTimingFunction : NSObject, NSCoding {     convenience init(name name: String)     class func functionWithName(_ name: String) -> Self     convenience init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     class func functionWithControlPoints(_ c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) -> Self     init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float)     func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) } ``` |

Modified [CAMediaTimingFunction.init(controlPoints: Float, _: Float, _: Float, _: Float)](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1522235-initwithcontrolpoints)

|  | Declaration |
| --- | --- |
| From | ``` init!(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |
| To | ``` init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |

Modified [CAMediaTimingFunction.init(name: String)](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1521979-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(name name: String!) ``` |
| To | ``` convenience init(name name: String) ``` |

Modified [CAOpenGLLayer](https://developer.apple.com/documentation/quartzcore/caopengllayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAOpenGLLayer : CALayer {     var asynchronous: Bool     func canDrawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) -> Bool     func drawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>)     func copyCGLPixelFormatForDisplayMask(_ mask: UInt32) -> CGLPixelFormatObj     func releaseCGLPixelFormat(_ pf: CGLPixelFormatObj)     func copyCGLContextForPixelFormat(_ pf: CGLPixelFormatObj) -> CGLContextObj     func releaseCGLContext(_ ctx: CGLContextObj) } ``` |
| To | ``` class CAOpenGLLayer : CALayer {     var asynchronous: Bool     func canDrawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>) -> Bool     func drawInCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, forLayerTime t: CFTimeInterval, displayTime ts: UnsafePointer<CVTimeStamp>)     func copyCGLPixelFormatForDisplayMask(_ mask: UInt32) -> CGLPixelFormatObj     func releaseCGLPixelFormat(_ pf: CGLPixelFormatObj)     func copyCGLContextForPixelFormat(_ pf: CGLPixelFormatObj) -> CGLContextObj     func releaseCGLContext(_ ctx: CGLContextObj)     var colorspace: CGColorSpace     var wantsExtendedDynamicRangeContent: Bool } ``` |

Modified [CAPropertyAnimation](https://developer.apple.com/documentation/quartzcore/capropertyanimation)

|  | Declaration |
| --- | --- |
| From | ``` class CAPropertyAnimation : CAAnimation {     convenience init!(keyPath path: String!)     class func animationWithKeyPath(_ path: String!) -> Self!     var keyPath: String!     var additive: Bool     var cumulative: Bool     var valueFunction: CAValueFunction! } ``` |
| To | ``` class CAPropertyAnimation : CAAnimation {     convenience init(keyPath path: String?)     class func animationWithKeyPath(_ path: String?) -> Self     var keyPath: String?     var additive: Bool     var cumulative: Bool     var valueFunction: CAValueFunction? } ``` |

Modified [CAPropertyAnimation.init(keyPath: String?)](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412534-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(keyPath path: String!) ``` |
| To | ``` convenience init(keyPath path: String?) ``` |

Modified [CAPropertyAnimation.keyPath](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412496-keypath)

|  | Declaration |
| --- | --- |
| From | ``` var keyPath: String! ``` |
| To | ``` var keyPath: String? ``` |

Modified [CAPropertyAnimation.valueFunction](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412447-valuefunction)

|  | Declaration |
| --- | --- |
| From | ``` var valueFunction: CAValueFunction! ``` |
| To | ``` var valueFunction: CAValueFunction? ``` |

Modified [CARemoteLayerClient](https://developer.apple.com/documentation/quartzcore/caremotelayerclient)

|  | Declaration |
| --- | --- |
| From | ``` class CARemoteLayerClient : NSObject {     init!(serverPort port: mach_port_t)     func invalidate()     var clientId: UInt32 { get }     var layer: CALayer! } ``` |
| To | ``` class CARemoteLayerClient : NSObject {     init(serverPort port: mach_port_t)     func invalidate()     var clientId: UInt32 { get }     var layer: CALayer? } ``` |

Modified [CARemoteLayerClient.init(serverPort: mach_port_t)](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418377-initwithserverport)

|  | Declaration |
| --- | --- |
| From | ``` init!(serverPort port: mach_port_t) ``` |
| To | ``` init(serverPort port: mach_port_t) ``` |

Modified [CARemoteLayerClient.layer](https://developer.apple.com/documentation/quartzcore/caremotelayerclient/1418373-layer)

|  | Declaration |
| --- | --- |
| From | ``` var layer: CALayer! ``` |
| To | ``` var layer: CALayer? ``` |

Modified [CARemoteLayerServer](https://developer.apple.com/documentation/quartzcore/caremotelayerserver)

|  | Declaration |
| --- | --- |
| From | ``` class CARemoteLayerServer : NSObject {     class func sharedServer() -> CARemoteLayerServer!     var serverPort: mach_port_t { get } } ``` |
| To | ``` class CARemoteLayerServer : NSObject {     class func sharedServer() -> CARemoteLayerServer     var serverPort: mach_port_t { get } } ``` |

Modified [CARemoteLayerServer.sharedServer() -> CARemoteLayerServer [class]](https://developer.apple.com/documentation/quartzcore/caremotelayerserver/1521954-sharedserver)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedServer() -> CARemoteLayerServer! ``` |
| To | ``` class func sharedServer() -> CARemoteLayerServer ``` |

Modified [CARenderer](https://developer.apple.com/documentation/quartzcore/carenderer)

|  | Declaration |
| --- | --- |
| From | ``` class CARenderer : NSObject {     init!(CGLContext ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]!) -> CARenderer     class func rendererWithCGLContext(_ ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]!) -> CARenderer!     var layer: CALayer!     var bounds: CGRect     func beginFrameAtTime(_ t: CFTimeInterval, timeStamp ts: UnsafeMutablePointer<CVTimeStamp>)     func updateBounds() -> CGRect     func addUpdateRect(_ r: CGRect)     func render()     func nextFrameTime() -> CFTimeInterval     func endFrame() } ``` |
| To | ``` class CARenderer : NSObject {      init(CGLContext ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]?)     class func rendererWithCGLContext(_ ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]?) -> CARenderer     var layer: CALayer?     var bounds: CGRect     func beginFrameAtTime(_ t: CFTimeInterval, timeStamp ts: UnsafeMutablePointer<CVTimeStamp>)     func updateBounds() -> CGRect     func addUpdateRect(_ r: CGRect)     func render()     func nextFrameTime() -> CFTimeInterval     func endFrame() } ``` |

Modified [CARenderer.init(CGLContext: UnsafeMutablePointer<Void>, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/quartzcore/carenderer/1519589-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(CGLContext ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]!) -> CARenderer ``` |
| To | ``` init(CGLContext ctx: UnsafeMutablePointer<Void>, options dict: [NSObject : AnyObject]?) ``` |

Modified [CARenderer.layer](https://developer.apple.com/documentation/quartzcore/carenderer/1519583-layer)

|  | Declaration |
| --- | --- |
| From | ``` var layer: CALayer! ``` |
| To | ``` var layer: CALayer? ``` |

Modified [CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAReplicatorLayer : CALayer {     var instanceCount: Int     var preservesDepth: Bool     var instanceDelay: CFTimeInterval     var instanceTransform: CATransform3D     var instanceColor: CGColor!     var instanceRedOffset: Float     var instanceGreenOffset: Float     var instanceBlueOffset: Float     var instanceAlphaOffset: Float } ``` |
| To | ``` class CAReplicatorLayer : CALayer {     var instanceCount: Int     var preservesDepth: Bool     var instanceDelay: CFTimeInterval     var instanceTransform: CATransform3D     var instanceColor: CGColor?     var instanceRedOffset: Float     var instanceGreenOffset: Float     var instanceBlueOffset: Float     var instanceAlphaOffset: Float } ``` |

Modified [CAReplicatorLayer.instanceColor](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/1522154-instancecolor)

|  | Declaration |
| --- | --- |
| From | ``` var instanceColor: CGColor! ``` |
| To | ``` var instanceColor: CGColor? ``` |

Modified [CAScrollLayer](https://developer.apple.com/documentation/quartzcore/cascrolllayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAScrollLayer : CALayer {     func scrollToPoint(_ p: CGPoint)     func scrollToRect(_ r: CGRect)     var scrollMode: String! } ``` |
| To | ``` class CAScrollLayer : CALayer {     func scrollToPoint(_ p: CGPoint)     func scrollToRect(_ r: CGRect)     var scrollMode: String } ``` |

Modified [CAScrollLayer.scrollMode](https://developer.apple.com/documentation/quartzcore/cascrolllayer/1522111-scrollmode)

|  | Declaration |
| --- | --- |
| From | ``` var scrollMode: String! ``` |
| To | ``` var scrollMode: String ``` |

Modified [CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAShapeLayer : CALayer {     var path: CGPath!     var fillColor: CGColor!     var fillRule: String!     var strokeColor: CGColor!     var strokeStart: CGFloat     var strokeEnd: CGFloat     var lineWidth: CGFloat     var miterLimit: CGFloat     var lineCap: String!     var lineJoin: String!     var lineDashPhase: CGFloat     var lineDashPattern: [AnyObject]! } ``` |
| To | ``` class CAShapeLayer : CALayer {     var path: CGPath?     var fillColor: CGColor?     var fillRule: String     var strokeColor: CGColor?     var strokeStart: CGFloat     var strokeEnd: CGFloat     var lineWidth: CGFloat     var miterLimit: CGFloat     var lineCap: String     var lineJoin: String     var lineDashPhase: CGFloat     var lineDashPattern: [NSNumber]? } ``` |

Modified [CAShapeLayer.fillColor](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522248-fillcolor)

|  | Declaration |
| --- | --- |
| From | ``` var fillColor: CGColor! ``` |
| To | ``` var fillColor: CGColor? ``` |

Modified [CAShapeLayer.fillRule](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522146-fillrule)

|  | Declaration |
| --- | --- |
| From | ``` var fillRule: String! ``` |
| To | ``` var fillRule: String ``` |

Modified [CAShapeLayer.lineCap](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521905-linecap)

|  | Declaration |
| --- | --- |
| From | ``` var lineCap: String! ``` |
| To | ``` var lineCap: String ``` |

Modified [CAShapeLayer.lineDashPattern](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521921-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` var lineDashPattern: [AnyObject]! ``` |
| To | ``` var lineDashPattern: [NSNumber]? ``` |

Modified [CAShapeLayer.lineJoin](https://developer.apple.com/documentation/quartzcore/cashapelayer/1522147-linejoin)

|  | Declaration |
| --- | --- |
| From | ``` var lineJoin: String! ``` |
| To | ``` var lineJoin: String ``` |

Modified [CAShapeLayer.path](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521904-path)

|  | Declaration |
| --- | --- |
| From | ``` var path: CGPath! ``` |
| To | ``` var path: CGPath? ``` |

Modified [CAShapeLayer.strokeColor](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521897-strokecolor)

|  | Declaration |
| --- | --- |
| From | ``` var strokeColor: CGColor! ``` |
| To | ``` var strokeColor: CGColor? ``` |

Modified [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer)

|  | Declaration |
| --- | --- |
| From | ``` class CATextLayer : CALayer {     @NSCopying var string: AnyObject!     var font: AnyObject!     var fontSize: CGFloat     var foregroundColor: CGColor!     var wrapped: Bool     var truncationMode: String!     var alignmentMode: String! } ``` |
| To | ``` class CATextLayer : CALayer {     @NSCopying var string: AnyObject?     var font: AnyObject?     var fontSize: CGFloat     var foregroundColor: CGColor?     var wrapped: Bool     var truncationMode: String     var alignmentMode: String     var allowsFontSubpixelQuantization: Bool } ``` |

Modified [CATextLayer.alignmentMode](https://developer.apple.com/documentation/quartzcore/catextlayer/1515301-alignmentmode)

|  | Declaration |
| --- | --- |
| From | ``` var alignmentMode: String! ``` |
| To | ``` var alignmentMode: String ``` |

Modified [CATextLayer.font](https://developer.apple.com/documentation/quartzcore/catextlayer/1515303-font)

|  | Declaration |
| --- | --- |
| From | ``` var font: AnyObject! ``` |
| To | ``` var font: AnyObject? ``` |

Modified [CATextLayer.foregroundColor](https://developer.apple.com/documentation/quartzcore/catextlayer/1515305-foregroundcolor)

|  | Declaration |
| --- | --- |
| From | ``` var foregroundColor: CGColor! ``` |
| To | ``` var foregroundColor: CGColor? ``` |

Modified [CATextLayer.string](https://developer.apple.com/documentation/quartzcore/catextlayer/1515295-string)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var string: AnyObject! ``` |
| To | ``` @NSCopying var string: AnyObject? ``` |

Modified [CATextLayer.truncationMode](https://developer.apple.com/documentation/quartzcore/catextlayer/1515296-truncationmode)

|  | Declaration |
| --- | --- |
| From | ``` var truncationMode: String! ``` |
| To | ``` var truncationMode: String ``` |

Modified [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction)

|  | Declaration |
| --- | --- |
| From | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction!     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction!)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Void)!     class func setCompletionBlock(_ block: (() -> Void)!)     class func valueForKey(_ key: String!) -> AnyObject!     class func setValue(_ anObject: AnyObject!, forKey key: String!) } ``` |
| To | ``` class CATransaction : NSObject {     class func begin()     class func commit()     class func flush()     class func lock()     class func unlock()     class func animationDuration() -> CFTimeInterval     class func setAnimationDuration(_ dur: CFTimeInterval)     class func animationTimingFunction() -> CAMediaTimingFunction?     class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?)     class func disableActions() -> Bool     class func setDisableActions(_ flag: Bool)     class func completionBlock() -> (() -> Void)?     class func setCompletionBlock(_ block: (() -> Void)?)     class func valueForKey(_ key: String) -> AnyObject?     class func setValue(_ anObject: AnyObject?, forKey key: String) } ``` |

Modified [CATransaction.animationTimingFunction() -> CAMediaTimingFunction? [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448269-animationtimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` class func animationTimingFunction() -> CAMediaTimingFunction! ``` |
| To | ``` class func animationTimingFunction() -> CAMediaTimingFunction? ``` |

Modified [CATransaction.completionBlock() -> (() -> Void)? [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448280-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` class func completionBlock() -> (() -> Void)! ``` |
| To | ``` class func completionBlock() -> (() -> Void)? ``` |

Modified [CATransaction.setAnimationTimingFunction(_: CAMediaTimingFunction?) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448279-setanimationtimingfunction)

|  | Declaration |
| --- | --- |
| From | ``` class func setAnimationTimingFunction(_ function: CAMediaTimingFunction!) ``` |
| To | ``` class func setAnimationTimingFunction(_ function: CAMediaTimingFunction?) ``` |

Modified [CATransaction.setCompletionBlock(_: (() -> Void)?) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448281-setcompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` class func setCompletionBlock(_ block: (() -> Void)!) ``` |
| To | ``` class func setCompletionBlock(_ block: (() -> Void)?) ``` |

Modified [CATransaction.setValue(_: AnyObject?, forKey: String) [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448278-setvalue)

|  | Declaration |
| --- | --- |
| From | ``` class func setValue(_ anObject: AnyObject!, forKey key: String!) ``` |
| To | ``` class func setValue(_ anObject: AnyObject?, forKey key: String) ``` |

Modified [CATransaction.valueForKey(_: String) -> AnyObject? [class]](https://developer.apple.com/documentation/quartzcore/catransaction/1448259-value)

|  | Declaration |
| --- | --- |
| From | ``` class func valueForKey(_ key: String!) -> AnyObject! ``` |
| To | ``` class func valueForKey(_ key: String) -> AnyObject? ``` |

Modified [CATransition](https://developer.apple.com/documentation/quartzcore/catransition)

|  | Declaration |
| --- | --- |
| From | ``` class CATransition : CAAnimation {     var type: String!     var subtype: String!     var startProgress: Float     var endProgress: Float     var filter: AnyObject! } ``` |
| To | ``` class CATransition : CAAnimation {     var type: String     var subtype: String?     var startProgress: Float     var endProgress: Float     var filter: AnyObject? } ``` |

Modified [CATransition.filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter)

|  | Declaration |
| --- | --- |
| From | ``` var filter: AnyObject! ``` |
| To | ``` var filter: AnyObject? ``` |

Modified [CATransition.subtype](https://developer.apple.com/documentation/quartzcore/catransition/1412467-subtype)

|  | Declaration |
| --- | --- |
| From | ``` var subtype: String! ``` |
| To | ``` var subtype: String? ``` |

Modified [CATransition.type](https://developer.apple.com/documentation/quartzcore/catransition/1412502-type)

|  | Declaration |
| --- | --- |
| From | ``` var type: String! ``` |
| To | ``` var type: String ``` |

Modified [CAValueFunction](https://developer.apple.com/documentation/quartzcore/cavaluefunction)

|  | Declaration |
| --- | --- |
| From | ``` class CAValueFunction : NSObject, NSCoding {     convenience init!(name name: String!)     class func functionWithName(_ name: String!) -> Self!     var name: String! { get } } ``` |
| To | ``` class CAValueFunction : NSObject, NSCoding {     convenience init?(name name: String)     class func functionWithName(_ name: String) -> Self?     var name: String { get } } ``` |

Modified [CAValueFunction.init(name: String)](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1522115-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(name name: String!) ``` |
| To | ``` convenience init?(name name: String) ``` |

Modified [CAValueFunction.name](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1521888-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [CIColor](https://developer.apple.com/documentation/coreimage/cicolor)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIColor : NSObject, NSCoding, NSCopying {     init!(CGColor c: CGColor!) -> CIColor     class func colorWithCGColor(_ c: CGColor!) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> CIColor!     init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor!     init!(string representation: String!) -> CIColor     class func colorWithString(_ representation: String!) -> CIColor!     init!(CGColor c: CGColor!)     func numberOfComponents() -> Int     func components() -> UnsafePointer<CGFloat>     func alpha() -> CGFloat     func colorSpace() -> Unmanaged<CGColorSpace>!     func red() -> CGFloat     func green() -> CGFloat     func blue() -> CGFloat     func stringRepresentation() -> String! } extension CIColor {     init?(color color: NSColor) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIColor : NSObject, NSSecureCoding, NSCoding, NSCopying {     convenience init(CGColor c: CGColor)     class func colorWithCGColor(_ c: CGColor) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat) -> Self     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat)     class func colorWithRed(_ r: CGFloat, green g: CGFloat, blue b: CGFloat) -> Self     convenience init(string representation: String)     class func colorWithString(_ representation: String) -> Self     init(CGColor c: CGColor)     convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat, alpha a: CGFloat)     var numberOfComponents: Int { get }     var components: UnsafePointer<CGFloat> { get }     var alpha: CGFloat { get }     var colorSpace: CGColorSpace { get }     var red: CGFloat { get }     var green: CGFloat { get }     var blue: CGFloat { get }     var stringRepresentation: String { get } } extension CIColor {     convenience init?(color color: NSColor) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIColor.init(CGColor: CGColor)](https://developer.apple.com/documentation/coreimage/cicolor/1437821-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGColor c: CGColor!) ``` | QuartzCore |
| To | ``` init(CGColor c: CGColor) ``` | CoreImage |

Modified [CIColor.init(red: CGFloat, green: CGFloat, blue: CGFloat)](https://developer.apple.com/documentation/coreimage/cicolor/1437941-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(red r: CGFloat, green g: CGFloat, blue b: CGFloat) -> CIColor ``` | QuartzCore |
| To | ``` convenience init(red r: CGFloat, green g: CGFloat, blue b: CGFloat) ``` | CoreImage |

Modified [CIColor.init(string: String)](https://developer.apple.com/documentation/coreimage/cicolor/1438059-colorwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string representation: String!) -> CIColor ``` | QuartzCore |
| To | ``` convenience init(string representation: String) ``` | CoreImage |

Modified [CIContext](https://developer.apple.com/documentation/coreimage/cicontext)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIContext : NSObject {     init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext!     init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGLContext(_ ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, options dict: [NSObject : AnyObject]!) -> CIContext!     init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext     class func contextWithCGContext(_ ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext!     class func offlineGPUCount() -> UInt32     init!(forOfflineGPUAtIndex index: UInt32) -> CIContext     class func contextForOfflineGPUAtIndex(_ index: UInt32) -> CIContext!     init!(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext     class func contextForOfflineGPUAtIndex(_ index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext!     func drawImage(_ im: CIImage!, atPoint p: CGPoint, fromRect src: CGRect)     func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect)     func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage!     func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage!     func createCGLayerWithSize(_ size: CGSize, info d: CFDictionary!) -> CGLayer!     func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!)     func render(_ im: CIImage!, toIOSurface surface: IOSurface!, bounds r: CGRect, colorSpace cs: CGColorSpace!)     func reclaimResources()     func clearCaches() } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIContext : NSObject {      init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?)     class func contextWithCGLContext(_ cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?) -> CIContext      init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, options options: [String : AnyObject]?)     class func contextWithCGLContext(_ cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, options options: [String : AnyObject]?) -> CIContext      init(CGContext cgctx: CGContext, options options: [String : AnyObject]?)     class func contextWithCGContext(_ cgctx: CGContext, options options: [String : AnyObject]?) -> CIContext      init(options options: [String : AnyObject]?)     class func contextWithOptions(_ options: [String : AnyObject]?) -> CIContext      init(MTLDevice device: MTLDevice)     class func contextWithMTLDevice(_ device: MTLDevice) -> CIContext      init(MTLDevice device: MTLDevice, options options: [String : AnyObject]?)     class func contextWithMTLDevice(_ device: MTLDevice, options options: [String : AnyObject]?) -> CIContext     var workingColorSpace: CGColorSpace { get }     func drawImage(_ image: CIImage, atPoint atPoint: CGPoint, fromRect fromRect: CGRect)     func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect)     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage     func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage     func createCGLayerWithSize(_ size: CGSize, info info: CFDictionary?) -> CGLayer     func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toIOSurface surface: IOSurface, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer)     func render(_ image: CIImage, toCVPixelBuffer buffer: CVPixelBuffer, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?)     func render(_ image: CIImage, toMTLTexture texture: MTLTexture, commandBuffer commandBuffer: MTLCommandBuffer?, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace)     func reclaimResources()     func clearCaches()     func inputImageMaximumSize() -> CGSize     func outputImageMaximumSize() -> CGSize } extension CIContext {     class func offlineGPUCount() -> UInt32      init(forOfflineGPUAtIndex index: UInt32)     class func contextForOfflineGPUAtIndex(_ index: UInt32) -> CIContext      init(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj)     class func contextForOfflineGPUAtIndex(_ index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj) -> CIContext } ``` | OS X 10.4 | CoreImage |

Modified [CIContext.clearCaches()](https://developer.apple.com/documentation/coreimage/cicontext/1437790-clearcaches)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437784-createcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect) -> CGImage! ``` | QuartzCore |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect) -> CGImage ``` | CoreImage |

Modified [CIContext.createCGImage(_: CIImage, fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage](https://developer.apple.com/documentation/coreimage/cicontext/1437978-createcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func createCGImage(_ im: CIImage!, fromRect r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CGImage! ``` | QuartzCore |
| To | ``` func createCGImage(_ image: CIImage, fromRect fromRect: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CGImage ``` | CoreImage |

Modified [CIContext.createCGLayerWithSize(_: CGSize, info: CFDictionary?) -> CGLayer](https://developer.apple.com/documentation/coreimage/cicontext/1438267-createcglayerwithsize)

|  | Declaration | Introduction | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` func createCGLayerWithSize(_ size: CGSize, info d: CFDictionary!) -> CGLayer! ``` | OS X 10.10 | -- | QuartzCore |
| To | ``` func createCGLayerWithSize(_ size: CGSize, info info: CFDictionary?) -> CGLayer ``` | OS X 10.4 | OS X 10.11 | CoreImage |

Modified [CIContext.drawImage(_: CIImage, inRect: CGRect, fromRect: CGRect)](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func drawImage(_ im: CIImage!, inRect dest: CGRect, fromRect src: CGRect) ``` | QuartzCore |
| To | ``` func drawImage(_ image: CIImage, inRect inRect: CGRect, fromRect fromRect: CGRect) ``` | CoreImage |

Modified [CIContext.init(CGContext: CGContext, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1437864-contextwithcgcontext)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGContext ctx: CGContext!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | OS X 10.10 | QuartzCore |
| To | ``` init(CGContext cgctx: CGContext, options options: [String : AnyObject]?) ``` | OS X 10.4 | CoreImage |

Modified [CIContext.init(CGLContext: CGLContextObj, pixelFormat: CGLPixelFormatObj, colorSpace: CGColorSpace?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cicontext/1438137-contextwithcglcontext)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGLContext ctx: CGLContextObj, pixelFormat pf: CGLPixelFormatObj, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIContext ``` | QuartzCore |
| To | ``` init(CGLContext cglctx: CGLContextObj, pixelFormat pixelFormat: CGLPixelFormatObj, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIContext.init(forOfflineGPUAtIndex: UInt32)](https://developer.apple.com/documentation/coreimage/cicontext/1437772-contextforofflinegpuatindex)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(forOfflineGPUAtIndex index: UInt32) -> CIContext ``` | QuartzCore |
| To | ``` init(forOfflineGPUAtIndex index: UInt32) ``` | CoreImage |

Modified [CIContext.init(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [String : AnyObject]?, sharedContext: CGLContextObj)](https://developer.apple.com/documentation/coreimage/cicontext/1437758-contextforofflinegpuatindex)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace!, options options: [NSObject : AnyObject]!, sharedContext sharedContext: CGLContextObj) -> CIContext ``` | QuartzCore |
| To | ``` init(forOfflineGPUAtIndex index: UInt32, colorSpace colorSpace: CGColorSpace?, options options: [String : AnyObject]?, sharedContext sharedContext: CGLContextObj) ``` | CoreImage |

Modified [CIContext.offlineGPUCount() -> UInt32 [class]](https://developer.apple.com/documentation/coreimage/cicontext/1437817-offlinegpucount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIContext.reclaimResources()](https://developer.apple.com/documentation/coreimage/cicontext/1437967-reclaimresources)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIContext.render(_: CIImage, toBitmap: UnsafeMutablePointer<Void>, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437897-render)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func render(_ im: CIImage!, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rb: Int, bounds r: CGRect, format f: CIFormat, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` func render(_ image: CIImage, toBitmap data: UnsafeMutablePointer<Void>, rowBytes rowBytes: Int, bounds bounds: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIContext.render(_: CIImage, toIOSurface: IOSurface, bounds: CGRect, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/cicontext/1437778-render)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func render(_ im: CIImage!, toIOSurface surface: IOSurface!, bounds r: CGRect, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` func render(_ image: CIImage, toIOSurface surface: IOSurface, bounds bounds: CGRect, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIDetector](https://developer.apple.com/documentation/coreimage/cidetector)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIDetector : NSObject {     init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector     class func detectorOfType(_ type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector!     func featuresInImage(_ image: CIImage!) -> [AnyObject]!     func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIDetector : NSObject {      init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?)     class func detectorOfType(_ type: String, context context: CIContext?, options options: [String : AnyObject]?) -> CIDetector     func featuresInImage(_ image: CIImage) -> [CIFeature]     func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] } ``` | OS X 10.7 | CoreImage |

Modified [CIDetector.featuresInImage(_: CIImage) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438049-featuresinimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func featuresInImage(_ image: CIImage) -> [CIFeature] ``` | CoreImage |

Modified [CIDetector.featuresInImage(_: CIImage, options: [String : AnyObject]?) -> [CIFeature]](https://developer.apple.com/documentation/coreimage/cidetector/1438189-features)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func featuresInImage(_ image: CIImage!, options options: [NSObject : AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func featuresInImage(_ image: CIImage, options options: [String : AnyObject]?) -> [CIFeature] ``` | CoreImage |

Modified [CIDetector.init(ofType: String, context: CIContext?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cidetector/1437884-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(ofType type: String!, context context: CIContext!, options options: [NSObject : AnyObject]!) -> CIDetector ``` | QuartzCore |
| To | ``` init(ofType type: String, context context: CIContext?, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIFaceFeature](https://developer.apple.com/documentation/coreimage/cifacefeature)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.7 | CoreImage |

Modified [CIFaceFeature.bounds](https://developer.apple.com/documentation/coreimage/cifacefeature/1438068-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.faceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1437689-faceangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasFaceAngle](https://developer.apple.com/documentation/coreimage/cifacefeature/1438165-hasfaceangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasLeftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437900-haslefteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasMouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437976-hasmouthposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasRightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438076-hasrighteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasSmile](https://developer.apple.com/documentation/coreimage/cifacefeature/1437882-hassmile)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasTrackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437731-hastrackingframecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.hasTrackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437683-hastrackingid)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.leftEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437630-lefteyeclosed)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.leftEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1437923-lefteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.mouthPosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438020-mouthposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.rightEyeClosed](https://developer.apple.com/documentation/coreimage/cifacefeature/1437615-righteyeclosed)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.rightEyePosition](https://developer.apple.com/documentation/coreimage/cifacefeature/1438213-righteyeposition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.trackingFrameCount](https://developer.apple.com/documentation/coreimage/cifacefeature/1437953-trackingframecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFaceFeature.trackingID](https://developer.apple.com/documentation/coreimage/cifacefeature/1437709-trackingid)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeature](https://developer.apple.com/documentation/coreimage/cifeature)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIFeature : NSObject {     var type: String! { get }     var bounds: CGRect { get } } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIFeature : NSObject {     var type: String { get }     var bounds: CGRect { get } } ``` | OS X 10.7 | CoreImage |

Modified [CIFeature.bounds](https://developer.apple.com/documentation/coreimage/cifeature/1437782-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeature.type](https://developer.apple.com/documentation/coreimage/cifeature/1438092-type)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var type: String! { get } ``` | QuartzCore |
| To | ``` var type: String { get } ``` | CoreImage |

Modified [CIFilter](https://developer.apple.com/documentation/coreimage/cifilter)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIFilter : NSObject, NSCoding, NSCopying {     var outputImage: CIImage! { get }     func inputKeys() -> [AnyObject]!     func outputKeys() -> [AnyObject]!     func setDefaults()     func attributes() -> [NSObject : AnyObject]!     func apply(_ k: CIKernel!, arguments args: [AnyObject]!, options dict: [NSObject : AnyObject]!) -> CIImage! } extension CIFilter {     func viewForUIConfiguration(_ inUIConfiguration: [NSObject : AnyObject]!, excludedKeys inKeys: [AnyObject]!) -> IKFilterUIView! } extension CIFilter {     var name: String!     var enabled: Bool } extension CIFilter {     func apply(_ k: CIKernel!, args args: [AnyObject]!, options options: (NSCopying, AnyObject)...) -> CIImage     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } extension CIFilter {     init!(name name: String!) -> CIFilter     class func filterWithName(_ name: String!) -> CIFilter!     init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter     class func filterWithName(_ name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter!     class func filterNamesInCategory(_ category: String!) -> [AnyObject]!     class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]!     class func registerFilterName(_ name: String!, constructor anObject: CIFilterConstructor!, classAttributes attributes: [NSObject : AnyObject]!)     class func localizedNameForFilterName(_ filterName: String!) -> String!     class func localizedNameForCategory(_ category: String!) -> String!     class func localizedDescriptionForFilterName(_ filterName: String!) -> String!     class func localizedReferenceDocumentationForFilterName(_ filterName: String!) -> NSURL! } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData!     class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! } extension CIFilter {     init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter     class func filterWithImageURL(_ url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter!     init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter     class func filterWithImageData(_ data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter! } extension CIFilter {     func apply(_ k: CIKernel!, args args: [AnyObject]!, options options: (NSCopying, AnyObject)...) -> CIImage     convenience init(name name: String!, elements elements: (NSCopying, AnyObject)...) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIFilter : NSObject, NSSecureCoding, NSCoding, NSCopying {     var outputImage: CIImage? { get }     var name: String     var enabled: Bool     var inputKeys: [String] { get }     var outputKeys: [String] { get }     func setDefaults()     var attributes: [String : AnyObject] { get }     func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? } extension CIFilter {      init?(name name: String)     class func filterWithName(_ name: String) -> CIFilter?      init?(name name: String, withInputParameters params: [String : AnyObject]?)     class func filterWithName(_ name: String, withInputParameters params: [String : AnyObject]?) -> CIFilter?     class func filterNamesInCategory(_ category: String?) -> [String]     class func filterNamesInCategories(_ categories: [String]?) -> [String]     class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject])     class func localizedNameForFilterName(_ filterName: String) -> String?     class func localizedNameForCategory(_ category: String) -> String     class func localizedDescriptionForFilterName(_ filterName: String) -> String?     class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? } extension CIFilter {     class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData     class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] } extension CIFilter {      init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!)     class func filterWithImageURL(_ url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter!      init!(imageData data: NSData!, options options: [NSObject : AnyObject]!)     class func filterWithImageData(_ data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter! } extension CIFilter {     func viewForUIConfiguration(_ inUIConfiguration: [NSObject : AnyObject]!, excludedKeys inKeys: [AnyObject]!) -> IKFilterUIView! } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIFilter.apply(_: CIKernel, arguments: [AnyObject]?, options: [String : AnyObject]?) -> CIImage?](https://developer.apple.com/documentation/coreimage/cifilter/1438077-apply)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` func apply(_ k: CIKernel!, arguments args: [AnyObject]!, options dict: [NSObject : AnyObject]!) -> CIImage! ``` | OS X 10.10 | QuartzCore |
| To | ``` func apply(_ k: CIKernel, arguments args: [AnyObject]?, options dict: [String : AnyObject]?) -> CIImage? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.enabled](https://developer.apple.com/documentation/coreimage/cifilter/1438276-isenabled)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.5 | CoreImage |

Modified [CIFilter.filterArrayFromSerializedXMP(_: NSData, inputImageExtent: CGRect, error: NSErrorPointer) -> [CIFilter] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438237-filterarray)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData!, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterArrayFromSerializedXMP(_ xmpData: NSData, inputImageExtent extent: CGRect, error outError: NSErrorPointer) -> [CIFilter] ``` | CoreImage |

Modified [CIFilter.filterNamesInCategories(_: [String]?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437595-filternamesincategories)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterNamesInCategories(_ categories: [AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterNamesInCategories(_ categories: [String]?) -> [String] ``` | CoreImage |

Modified [CIFilter.filterNamesInCategory(_: String?) -> [String] [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438145-filternames)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func filterNamesInCategory(_ category: String!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` class func filterNamesInCategory(_ category: String?) -> [String] ``` | CoreImage |

Modified [CIFilter.init(imageData: NSData!, options: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/coreimage/cifilter/1437879-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init!(imageData data: NSData!, options options: [NSObject : AnyObject]!) ``` | CoreImage |

Modified [CIFilter.init(imageURL: NSURL!, options: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/coreimage/cifilter/1438096-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init!(imageURL url: NSURL!, options options: [NSObject : AnyObject]!) ``` | CoreImage |

Modified [CIFilter.init(name: String)](https://developer.apple.com/documentation/coreimage/cifilter/1438255-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(name name: String!) -> CIFilter ``` | QuartzCore |
| To | ``` init?(name name: String) ``` | CoreImage |

Modified [CIFilter.init(name: String, withInputParameters: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cifilter/1437894-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(name name: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIFilter ``` | QuartzCore |
| To | ``` init?(name name: String, withInputParameters params: [String : AnyObject]?) ``` | CoreImage |

Modified [CIFilter.localizedDescriptionForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437591-localizeddescription)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedDescriptionForFilterName(_ filterName: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedDescriptionForFilterName(_ filterName: String) -> String? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedNameForCategory(_: String) -> String [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438057-localizednameforcategory)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedNameForCategory(_ category: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedNameForCategory(_ category: String) -> String ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedNameForFilterName(_: String) -> String? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437697-localizednameforfiltername)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedNameForFilterName(_ filterName: String!) -> String! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedNameForFilterName(_ filterName: String) -> String? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.localizedReferenceDocumentationForFilterName(_: String) -> NSURL? [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437642-localizedreferencedocumentation)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func localizedReferenceDocumentationForFilterName(_ filterName: String!) -> NSURL! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func localizedReferenceDocumentationForFilterName(_ filterName: String) -> NSURL? ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.name](https://developer.apple.com/documentation/coreimage/cifilter/1437997-setname)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` var name: String! ``` | OS X 10.10 | QuartzCore |
| To | ``` var name: String ``` | OS X 10.5 | CoreImage |

Modified [CIFilter.outputImage](https://developer.apple.com/documentation/coreimage/cifilter/1438169-outputimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var outputImage: CIImage! { get } ``` | QuartzCore |
| To | ``` var outputImage: CIImage? { get } ``` | CoreImage |

Modified [CIFilter.registerFilterName(_: String, constructor: CIFilterConstructor, classAttributes: [String : AnyObject]) [class]](https://developer.apple.com/documentation/coreimage/cifilter/1437889-registername)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func registerFilterName(_ name: String!, constructor anObject: CIFilterConstructor!, classAttributes attributes: [NSObject : AnyObject]!) ``` | OS X 10.10 | QuartzCore |
| To | ``` class func registerFilterName(_ name: String, constructor anObject: CIFilterConstructor, classAttributes attributes: [String : AnyObject]) ``` | OS X 10.4 | CoreImage |

Modified [CIFilter.serializedXMPFromFilters(_: [CIFilter], inputImageExtent: CGRect) -> NSData [class]](https://developer.apple.com/documentation/coreimage/cifilter/1438006-serializedxmp)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func serializedXMPFromFilters(_ filters: [AnyObject]!, inputImageExtent extent: CGRect) -> NSData! ``` | QuartzCore |
| To | ``` class func serializedXMPFromFilters(_ filters: [CIFilter], inputImageExtent extent: CGRect) -> NSData ``` | CoreImage |

Modified [CIFilter.setDefaults()](https://developer.apple.com/documentation/coreimage/cifilter/1437902-setdefaults)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFilterConstructor](https://developer.apple.com/documentation/coreimage/cifilterconstructor)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` protocol CIFilterConstructor {     func filterWithName(_ name: String!) -> CIFilter! } ``` | QuartzCore |
| To | ``` protocol CIFilterConstructor {     func filterWithName(_ name: String) -> CIFilter? } ``` | CoreImage |

Modified [CIFilterConstructor.filterWithName(_: String) -> CIFilter?](https://developer.apple.com/documentation/coreimage/cifilterconstructor/1438018-filterwithname)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` func filterWithName(_ name: String!) -> CIFilter! ``` | OS X 10.10 | QuartzCore |
| To | ``` func filterWithName(_ name: String) -> CIFilter? ``` | OS X 10.4 | CoreImage |

Modified [CIFilterGenerator](https://developer.apple.com/documentation/coreimage/cifiltergenerator)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIFilterGenerator : NSObject, NSCoding, NSCopying, CIFilterConstructor {     init!() -> CIFilterGenerator     class func filterGenerator() -> CIFilterGenerator!     init!(contentsOfURL aURL: NSURL!) -> CIFilterGenerator     class func filterGeneratorWithContentsOfURL(_ aURL: NSURL!) -> CIFilterGenerator!     init!(contentsOfURL aURL: NSURL!)     func connectObject(_ sourceObject: AnyObject!, withKey sourceKey: String!, toObject targetObject: AnyObject!, withKey targetKey: String!)     func disconnectObject(_ sourceObject: AnyObject!, withKey key: String!, toObject targetObject: AnyObject!, withKey targetKey: String!)     func exportKey(_ key: String!, fromObject targetObject: AnyObject!, withName exportedKeyName: String!)     func removeExportedKey(_ exportedKeyName: String!)     func exportedKeys() -> [NSObject : AnyObject]!     func setAttributes(_ attributes: [NSObject : AnyObject]!, forExportedKey key: String!)     func classAttributes() -> [NSObject : AnyObject]!     func setClassAttributes(_ attributes: [NSObject : AnyObject]!)     func filter() -> CIFilter!     func registerFilterName(_ name: String!)     func writeToURL(_ aURL: NSURL!, atomically flag: Bool) -> Bool } ``` | AnyObject, CIFilterConstructor, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIFilterGenerator : NSObject, NSSecureCoding, NSCoding, NSCopying, CIFilterConstructor {      init()     class func filterGenerator() -> CIFilterGenerator      init?(contentsOfURL aURL: NSURL)     class func filterGeneratorWithContentsOfURL(_ aURL: NSURL) -> CIFilterGenerator?     init?(contentsOfURL aURL: NSURL)     func connectObject(_ sourceObject: AnyObject, withKey sourceKey: String?, toObject targetObject: AnyObject, withKey targetKey: String)     func disconnectObject(_ sourceObject: AnyObject, withKey key: String, toObject targetObject: AnyObject, withKey targetKey: String)     func exportKey(_ key: String, fromObject targetObject: AnyObject, withName exportedKeyName: String?)     func removeExportedKey(_ exportedKeyName: String)     var exportedKeys: [NSObject : AnyObject] { get }     func setAttributes(_ attributes: [NSObject : AnyObject], forExportedKey key: String)     var classAttributes: [NSObject : AnyObject]     func filter() -> CIFilter     func registerFilterName(_ name: String)     func writeToURL(_ aURL: NSURL, atomically flag: Bool) -> Bool } ``` | AnyObject, CIFilterConstructor, NSCoding, NSCopying, NSSecureCoding | OS X 10.5 | CoreImage |

Modified [CIFilterGenerator.connectObject(_: AnyObject, withKey: String?, toObject: AnyObject, withKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438159-connect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func connectObject(_ sourceObject: AnyObject!, withKey sourceKey: String!, toObject targetObject: AnyObject!, withKey targetKey: String!) ``` | QuartzCore |
| To | ``` func connectObject(_ sourceObject: AnyObject, withKey sourceKey: String?, toObject targetObject: AnyObject, withKey targetKey: String) ``` | CoreImage |

Modified [CIFilterGenerator.disconnectObject(_: AnyObject, withKey: String, toObject: AnyObject, withKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438075-disconnectobject)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func disconnectObject(_ sourceObject: AnyObject!, withKey key: String!, toObject targetObject: AnyObject!, withKey targetKey: String!) ``` | QuartzCore |
| To | ``` func disconnectObject(_ sourceObject: AnyObject, withKey key: String, toObject targetObject: AnyObject, withKey targetKey: String) ``` | CoreImage |

Modified [CIFilterGenerator.exportKey(_: String, fromObject: AnyObject, withName: String?)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438155-exportkey)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func exportKey(_ key: String!, fromObject targetObject: AnyObject!, withName exportedKeyName: String!) ``` | QuartzCore |
| To | ``` func exportKey(_ key: String, fromObject targetObject: AnyObject, withName exportedKeyName: String?) ``` | CoreImage |

Modified [CIFilterGenerator.filter() -> CIFilter](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438044-filter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func filter() -> CIFilter! ``` | QuartzCore |
| To | ``` func filter() -> CIFilter ``` | CoreImage |

Modified [CIFilterGenerator.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437742-initwithcontentsofurl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL aURL: NSURL!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL aURL: NSURL) ``` | CoreImage |

Modified [CIFilterGenerator.registerFilterName(_: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1437891-registerfiltername)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func registerFilterName(_ name: String!) ``` | QuartzCore |
| To | ``` func registerFilterName(_ name: String) ``` | CoreImage |

Modified [CIFilterGenerator.removeExportedKey(_: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438191-removeexportedkey)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func removeExportedKey(_ exportedKeyName: String!) ``` | QuartzCore |
| To | ``` func removeExportedKey(_ exportedKeyName: String) ``` | CoreImage |

Modified [CIFilterGenerator.setAttributes(_: [NSObject : AnyObject], forExportedKey: String)](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438069-setattributes)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setAttributes(_ attributes: [NSObject : AnyObject]!, forExportedKey key: String!) ``` | QuartzCore |
| To | ``` func setAttributes(_ attributes: [NSObject : AnyObject], forExportedKey key: String) ``` | CoreImage |

Modified [CIFilterGenerator.writeToURL(_: NSURL, atomically: Bool) -> Bool](https://developer.apple.com/documentation/coreimage/cifiltergenerator/1438179-write)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func writeToURL(_ aURL: NSURL!, atomically flag: Bool) -> Bool ``` | QuartzCore |
| To | ``` func writeToURL(_ aURL: NSURL, atomically flag: Bool) -> Bool ``` | CoreImage |

Modified [CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIFilterShape : NSObject, NSCopying {     class func shapeWithRect(_ r: CGRect) -> AnyObject!     init!(rect r: CGRect)     func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape!     func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape!     func unionWith(_ s2: CIFilterShape!) -> CIFilterShape!     func unionWithRect(_ r: CGRect) -> CIFilterShape!     func intersectWith(_ s2: CIFilterShape!) -> CIFilterShape!     func intersectWithRect(_ r: CGRect) -> CIFilterShape! } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIFilterShape : NSObject, NSCopying {     convenience init(rect r: CGRect)     class func shapeWithRect(_ r: CGRect) -> Self     init(rect r: CGRect)     func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape     func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape     func unionWith(_ s2: CIFilterShape) -> CIFilterShape     func unionWithRect(_ r: CGRect) -> CIFilterShape     func intersectWith(_ s2: CIFilterShape) -> CIFilterShape     func intersectWithRect(_ r: CGRect) -> CIFilterShape     var extent: CGRect { get } } ``` | OS X 10.4 | CoreImage |

Modified [CIFilterShape.init(rect: CGRect)](https://developer.apple.com/documentation/coreimage/cifiltershape/1437921-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(rect r: CGRect) ``` | QuartzCore |
| To | ``` init(rect r: CGRect) ``` | CoreImage |

Modified [CIFilterShape.insetByX(_: Int32, y: Int32) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437987-insetby)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func insetByX(_ dx: Int32, y dy: Int32) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.intersectWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437881-intersect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func intersectWith(_ s2: CIFilterShape!) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func intersectWith(_ s2: CIFilterShape) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.intersectWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437806-intersect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func intersectWithRect(_ r: CGRect) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func intersectWithRect(_ r: CGRect) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.transformBy(_: CGAffineTransform, interior: Bool) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437808-transformby)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func transformBy(_ m: CGAffineTransform, interior flag: Bool) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.unionWith(_: CIFilterShape) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1438227-unionwith)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func unionWith(_ s2: CIFilterShape!) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func unionWith(_ s2: CIFilterShape) -> CIFilterShape ``` | CoreImage |

Modified [CIFilterShape.unionWithRect(_: CGRect) -> CIFilterShape](https://developer.apple.com/documentation/coreimage/cifiltershape/1437601-unionwithrect)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func unionWithRect(_ r: CGRect) -> CIFilterShape! ``` | QuartzCore |
| To | ``` func unionWithRect(_ r: CGRect) -> CIFilterShape ``` | CoreImage |

Modified [CIImage](https://developer.apple.com/documentation/coreimage/ciimage)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIImage : NSObject, NSCoding, NSCopying {     init!(CGImage image: CGImage!) -> CIImage     class func imageWithCGImage(_ image: CGImage!) -> CIImage!     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGImage(_ image: CGImage!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CGLayer layer: CGLayer!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!) -> CIImage!     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithCGLayer(_ layer: CGLayer!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithBitmapData(_ d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace cs: CGColorSpace!) -> CIImage!     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) -> CIImage!     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) -> CIImage     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) -> CIImage!     init!(contentsOfURL url: NSURL!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!) -> CIImage!     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithContentsOfURL(_ url: NSURL!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(data data: NSData!) -> CIImage     class func imageWithData(_ data: NSData!) -> CIImage!     init!(data data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithData(_ data: NSData!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!) -> CIImage!     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!) -> CIImage!     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithCVPixelBuffer(_ buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(IOSurface surface: IOSurface!) -> CIImage     class func imageWithIOSurface(_ surface: IOSurface!) -> CIImage!     init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) -> CIImage     class func imageWithIOSurface(_ surface: IOSurface!, options d: [NSObject : AnyObject]!) -> CIImage!     init!(color color: CIColor!) -> CIImage     class func imageWithColor(_ color: CIColor!) -> CIImage!     class func emptyImage() -> CIImage!     init!(CGImage image: CGImage!)     init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!)     init!(CGLayer layer: CGLayer!)     init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!)     init!(data data: NSData!)     init!(data data: NSData!, options d: [NSObject : AnyObject]!)     init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!)     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!)     init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!)     init!(contentsOfURL url: NSURL!)     init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!)     init!(IOSurface surface: IOSurface!)     init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!)     init!(IOSurface surface: IOSurface!, plane plane: Int, format format: CIFormat, options d: [NSObject : AnyObject]!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!)     init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!)     init!(CVPixelBuffer buffer: CVPixelBuffer!)     init!(CVPixelBuffer buffer: CVPixelBuffer!, options dict: [NSObject : AnyObject]!)     init!(color color: CIColor!)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage!     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage!     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage!     func imageByCroppingToRect(_ r: CGRect) -> CIImage!     func imageByClampingToExtent() -> CIImage!     func extent() -> CGRect     func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage!     func properties() -> [NSObject : AnyObject]!     func definition() -> CIFilterShape!     func url() -> NSURL!     func colorSpace() -> Unmanaged<CGColorSpace>! } extension CIImage {     init?(bitmapImageRep bitmapImageRep: NSBitmapImageRep)     func drawInRect(_ rect: NSRect, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)     func drawAtPoint(_ point: NSPoint, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat) } extension CIImage {     func autoAdjustmentFilters() -> [AnyObject]!     func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! } extension CIImage {     init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIImage     class func imageWithImageProvider(_ p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) -> CIImage!     init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIImage : NSObject, NSSecureCoding, NSCoding, NSCopying {      init(CGImage image: CGImage)     class func imageWithCGImage(_ image: CGImage) -> CIImage      init(CGImage image: CGImage, options options: [String : AnyObject]?)     class func imageWithCGImage(_ image: CGImage, options options: [String : AnyObject]?) -> CIImage      init(CGLayer layer: CGLayer)     class func imageWithCGLayer(_ layer: CGLayer) -> CIImage      init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     class func imageWithCGLayer(_ layer: CGLayer, options options: [String : AnyObject]?) -> CIImage      init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     class func imageWithBitmapData(_ data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) -> CIImage      init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     class func imageWithTexture(_ name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) -> CIImage      init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     class func imageWithMTLTexture(_ texture: MTLTexture, options options: [String : AnyObject]?) -> CIImage      init?(contentsOfURL url: NSURL)     class func imageWithContentsOfURL(_ url: NSURL) -> CIImage?      init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     class func imageWithContentsOfURL(_ url: NSURL, options options: [String : AnyObject]?) -> CIImage?      init?(data data: NSData)     class func imageWithData(_ data: NSData) -> CIImage?      init?(data data: NSData, options options: [String : AnyObject]?)     class func imageWithData(_ data: NSData, options options: [String : AnyObject]?) -> CIImage?      init(CVImageBuffer imageBuffer: CVImageBuffer)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer) -> CIImage      init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     class func imageWithCVImageBuffer(_ imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer) -> CIImage      init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     class func imageWithCVPixelBuffer(_ pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?) -> CIImage      init(IOSurface surface: IOSurface)     class func imageWithIOSurface(_ surface: IOSurface) -> CIImage      init(IOSurface surface: IOSurface, options options: [String : AnyObject]?)     class func imageWithIOSurface(_ surface: IOSurface, options options: [String : AnyObject]?) -> CIImage      init(color color: CIColor)     class func imageWithColor(_ color: CIColor) -> CIImage     class func emptyImage() -> CIImage     init(CGImage image: CGImage)     init(CGImage image: CGImage, options options: [String : AnyObject]?)     init(CGLayer layer: CGLayer)     init(CGLayer layer: CGLayer, options options: [String : AnyObject]?)     init?(data data: NSData)     init?(data data: NSData, options options: [String : AnyObject]?)     init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?)     init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?)     init(MTLTexture texture: MTLTexture, options options: [String : AnyObject]?)     init?(contentsOfURL url: NSURL)     init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?)     init(IOSurface surface: IOSurface)     init(IOSurface surface: IOSurface, options options: [String : AnyObject]?)     init(IOSurface surface: IOSurface, plane plane: Int, format format: CIFormat, options options: [String : AnyObject]?)     init(CVImageBuffer imageBuffer: CVImageBuffer)     init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer)     init(CVPixelBuffer pixelBuffer: CVPixelBuffer, options options: [String : AnyObject]?)     init(color color: CIColor)     func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage     func imageByApplyingOrientation(_ orientation: Int32) -> CIImage     func imageTransformForOrientation(_ orientation: Int32) -> CGAffineTransform     func imageByCompositingOverImage(_ dest: CIImage) -> CIImage     func imageByCroppingToRect(_ rect: CGRect) -> CIImage     func imageByClampingToExtent() -> CIImage     func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage     var extent: CGRect { get }     var properties: [String : AnyObject] { get }     var definition: CIFilterShape { get }     var url: NSURL? { get }     var colorSpace: CGColorSpace? { get }     func regionOfInterestForImage(_ image: CIImage, inRect rect: CGRect) -> CGRect } extension CIImage {     init?(bitmapImageRep bitmapImageRep: NSBitmapImageRep)     func drawInRect(_ rect: NSRect, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat)     func drawAtPoint(_ point: NSPoint, fromRect fromRect: NSRect, operation op: NSCompositingOperation, fraction delta: CGFloat) } extension CIImage {     func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] } extension CIImage {      init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?)     class func imageWithImageProvider(_ p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) -> CIImage     init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIImage.autoAdjustmentFiltersWithOptions(_: [String : AnyObject]?) -> [CIFilter]](https://developer.apple.com/documentation/coreimage/ciimage/1437792-autoadjustmentfilterswithoptions)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func autoAdjustmentFiltersWithOptions(_ dict: [NSObject : AnyObject]!) -> [AnyObject]! ``` | QuartzCore |
| To | ``` func autoAdjustmentFiltersWithOptions(_ options: [String : AnyObject]?) -> [CIFilter] ``` | CoreImage |

Modified [CIImage.emptyImage() -> CIImage [class]](https://developer.apple.com/documentation/coreimage/ciimage/1438023-emptyimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class func emptyImage() -> CIImage! ``` | QuartzCore |
| To | ``` class func emptyImage() -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingFilter(_: String, withInputParameters: [String : AnyObject]?) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437589-imagebyapplyingfilter)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingFilter(_ filterName: String!, withInputParameters params: [NSObject : AnyObject]!) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingFilter(_ filterName: String, withInputParameters params: [String : AnyObject]?) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingOrientation(_: Int32) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438223-oriented)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingOrientation(_ orientation: Int32) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByApplyingTransform(_: CGAffineTransform) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1438203-imagebyapplyingtransform)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByApplyingTransform(_ matrix: CGAffineTransform) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByClampingToExtent() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437628-imagebyclampingtoextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByClampingToExtent() -> CIImage! ``` | QuartzCore |
| To | ``` func imageByClampingToExtent() -> CIImage ``` | CoreImage |

Modified [CIImage.imageByCompositingOverImage(_: CIImage) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437837-imagebycompositingoverimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByCompositingOverImage(_ dest: CIImage!) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByCompositingOverImage(_ dest: CIImage) -> CIImage ``` | CoreImage |

Modified [CIImage.imageByCroppingToRect(_: CGRect) -> CIImage](https://developer.apple.com/documentation/coreimage/ciimage/1437833-cropped)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func imageByCroppingToRect(_ r: CGRect) -> CIImage! ``` | QuartzCore |
| To | ``` func imageByCroppingToRect(_ rect: CGRect) -> CIImage ``` | CoreImage |

Modified [CIImage.imageTransformForOrientation(_: Int32) -> CGAffineTransform](https://developer.apple.com/documentation/coreimage/ciimage/1437930-orientationtransform)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIImage.init(bitmapData: NSData, bytesPerRow: Int, size: CGSize, format: CIFormat, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1437857-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(bitmapData d: NSData!, bytesPerRow bpr: Int, size size: CGSize, format f: CIFormat, colorSpace c: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(bitmapData data: NSData, bytesPerRow bytesPerRow: Int, size size: CGSize, format format: CIFormat, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIImage.init(CGImage: CGImage)](https://developer.apple.com/documentation/coreimage/ciimage/1437986-initwithcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGImage image: CGImage!) ``` | QuartzCore |
| To | ``` init(CGImage image: CGImage) ``` | CoreImage |

Modified [CIImage.init(CGImage: CGImage, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437764-initwithcgimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGImage image: CGImage!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(CGImage image: CGImage, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(CGLayer: CGLayer)](https://developer.apple.com/documentation/coreimage/ciimage/1438065-initwithcglayer)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGLayer layer: CGLayer!) ``` | -- | QuartzCore |
| To | ``` init(CGLayer layer: CGLayer) ``` | OS X 10.11 | CoreImage |

Modified [CIImage.init(CGLayer: CGLayer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437687-initwithcglayer)

|  | Declaration | Deprecation | Module |
| --- | --- | --- | --- |
| From | ``` init!(CGLayer layer: CGLayer!, options d: [NSObject : AnyObject]!) ``` | -- | QuartzCore |
| To | ``` init(CGLayer layer: CGLayer, options options: [String : AnyObject]?) ``` | OS X 10.11 | CoreImage |

Modified [CIImage.init(color: CIColor)](https://developer.apple.com/documentation/coreimage/ciimage/1437947-initwithcolor)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(color color: CIColor!) ``` | QuartzCore |
| To | ``` init(color color: CIColor) ``` | CoreImage |

Modified [CIImage.init(contentsOfURL: NSURL)](https://developer.apple.com/documentation/coreimage/ciimage/1437908-initwithcontentsofurl)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL url: NSURL) ``` | CoreImage |

Modified [CIImage.init(contentsOfURL: NSURL, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437867-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(contentsOfURL url: NSURL!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init?(contentsOfURL url: NSURL, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(CVImageBuffer: CVImageBuffer)](https://developer.apple.com/documentation/coreimage/ciimage/1438012-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!) ``` | QuartzCore |
| To | ``` init(CVImageBuffer imageBuffer: CVImageBuffer) ``` | CoreImage |

Modified [CIImage.init(CVImageBuffer: CVImageBuffer, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437617-initwithcvimagebuffer)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CVImageBuffer imageBuffer: CVImageBuffer!, options dict: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(CVImageBuffer imageBuffer: CVImageBuffer, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(data: NSData)](https://developer.apple.com/documentation/coreimage/ciimage/1437925-initwithdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(data data: NSData!) ``` | QuartzCore |
| To | ``` init?(data data: NSData) ``` | CoreImage |

Modified [CIImage.init(data: NSData, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438032-initwithdata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(data data: NSData!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init?(data data: NSData, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(imageProvider: AnyObject, size: Int, _: Int, format: CIFormat, colorSpace: CGColorSpace?, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437868-init)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` init!(imageProvider p: AnyObject!, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace!, options dict: [NSObject : AnyObject]!) ``` | OS X 10.10 | QuartzCore |
| To | ``` init(imageProvider p: AnyObject, size width: Int, _ height: Int, format f: CIFormat, colorSpace cs: CGColorSpace?, options options: [String : AnyObject]?) ``` | OS X 10.4 | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface)](https://developer.apple.com/documentation/coreimage/ciimage/1438030-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!) ``` | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface) ``` | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1438181-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!, options d: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImage.init(IOSurface: IOSurface, plane: Int, format: CIFormat, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437670-init)

|  | Declaration | Introduction | Deprecation | Module |
| --- | --- | --- | --- | --- |
| From | ``` init!(IOSurface surface: IOSurface!, plane plane: Int, format format: CIFormat, options d: [NSObject : AnyObject]!) ``` | OS X 10.10 | -- | QuartzCore |
| To | ``` init(IOSurface surface: IOSurface, plane plane: Int, format format: CIFormat, options options: [String : AnyObject]?) ``` | OS X 10.9 | OS X 10.11 | CoreImage |

Modified [CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, colorSpace: CGColorSpace?)](https://developer.apple.com/documentation/coreimage/ciimage/1438015-initwithtexture)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, colorSpace cs: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, colorSpace colorSpace: CGColorSpace?) ``` | CoreImage |

Modified [CIImage.init(texture: UInt32, size: CGSize, flipped: Bool, options: [String : AnyObject]?)](https://developer.apple.com/documentation/coreimage/ciimage/1437880-initwithtexture)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(texture name: UInt32, size size: CGSize, flipped flag: Bool, options options: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(texture name: UInt32, size size: CGSize, flipped flipped: Bool, options options: [String : AnyObject]?) ``` | CoreImage |

Modified [CIImageAccumulator](https://developer.apple.com/documentation/coreimage/ciimageaccumulator)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIImageAccumulator : NSObject {     init!(extent extent: CGRect, format format: CIFormat) -> CIImageAccumulator     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat) -> CIImageAccumulator!     init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) -> CIImageAccumulator     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) -> CIImageAccumulator!     init!(extent extent: CGRect, format format: CIFormat)     init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!)     func extent() -> CGRect     func format() -> CIFormat     func image() -> CIImage!     func setImage(_ im: CIImage!)     func setImage(_ im: CIImage!, dirtyRect r: CGRect)     func clear() } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIImageAccumulator : NSObject {     convenience init(extent extent: CGRect, format format: CIFormat)     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat) -> Self     convenience init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace)     class func imageAccumulatorWithExtent(_ extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace) -> Self     init(extent extent: CGRect, format format: CIFormat)     init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace)     var extent: CGRect { get }     var format: CIFormat { get }     func image() -> CIImage     func setImage(_ image: CIImage)     func setImage(_ image: CIImage, dirtyRect dirtyRect: CGRect)     func clear() } ``` | OS X 10.4 | CoreImage |

Modified [CIImageAccumulator.clear()](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427720-clear)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIImageAccumulator.image() -> CIImage](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427704-image)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func image() -> CIImage! ``` | QuartzCore |
| To | ``` func image() -> CIImage ``` | CoreImage |

Modified [CIImageAccumulator.init(extent: CGRect, format: CIFormat)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427718-initwithextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(extent extent: CGRect, format format: CIFormat) ``` | QuartzCore |
| To | ``` init(extent extent: CGRect, format format: CIFormat) ``` | CoreImage |

Modified [CIImageAccumulator.init(extent: CGRect, format: CIFormat, colorSpace: CGColorSpace)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427710-initwithextent)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace!) ``` | QuartzCore |
| To | ``` init(extent extent: CGRect, format format: CIFormat, colorSpace colorSpace: CGColorSpace) ``` | CoreImage |

Modified [CIImageAccumulator.setImage(_: CIImage)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427702-setimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setImage(_ im: CIImage!) ``` | QuartzCore |
| To | ``` func setImage(_ image: CIImage) ``` | CoreImage |

Modified [CIImageAccumulator.setImage(_: CIImage, dirtyRect: CGRect)](https://developer.apple.com/documentation/coreimage/ciimageaccumulator/1427706-setimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func setImage(_ im: CIImage!, dirtyRect r: CGRect) ``` | QuartzCore |
| To | ``` func setImage(_ image: CIImage, dirtyRect dirtyRect: CGRect) ``` | CoreImage |

Modified [CIKernel](https://developer.apple.com/documentation/coreimage/cikernel)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CIKernel : NSObject {     class func kernelsWithString(_ s: String!) -> [AnyObject]!     init!(string s: String!) -> CIKernel     class func kernelWithString(_ s: String!) -> CIKernel!     func name() -> String!     func setROISelector(_ aMethod: Selector) } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CIKernel : NSObject {     class func kernelsWithString(_ string: String) -> [CIKernel]?     convenience init?(string string: String)     class func kernelWithString(_ string: String) -> Self?     var name: String { get }     func setROISelector(_ method: Selector)     func applyWithExtent(_ extent: CGRect, roiCallback callback: CIKernelROICallback, arguments args: [AnyObject]?) -> CIImage? } ``` | OS X 10.4 | CoreImage |

Modified [CIKernel.init(string: String)](https://developer.apple.com/documentation/coreimage/cikernel/1437796-kernelwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string s: String!) -> CIKernel ``` | QuartzCore |
| To | ``` convenience init?(string string: String) ``` | CoreImage |

Modified [CIKernel.kernelsWithString(_: String) -> [CIKernel]? [class]](https://developer.apple.com/documentation/coreimage/cikernel/1437876-kernelswithstring)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class func kernelsWithString(_ s: String!) -> [AnyObject]! ``` | OS X 10.10 | QuartzCore |
| To | ``` class func kernelsWithString(_ string: String) -> [CIKernel]? ``` | OS X 10.4 | CoreImage |

Modified [CIKernel.setROISelector(_: Selector)](https://developer.apple.com/documentation/coreimage/cikernel/1437691-setroiselector)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIPlugIn](https://developer.apple.com/documentation/coreimage/ciplugin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [CIPlugIn.loadAllPlugIns() [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1437653-loadallplugins)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugIn.loadNonExecutablePlugIns() [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1437599-loadnonexecutableplugins)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugIn.loadPlugIn(_: NSURL!, allowExecutableCode: Bool) [class]](https://developer.apple.com/documentation/coreimage/ciplugin/1438187-loadplugin)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugInRegistration](https://developer.apple.com/documentation/coreimage/cipluginregistration)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIPlugInRegistration.load(_: UnsafeMutablePointer<Void>) -> Bool](https://developer.apple.com/documentation/coreimage/cipluginregistration/1437823-load)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature](https://developer.apple.com/documentation/coreimage/ciqrcodefeature)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String! { get } } ``` | QuartzCore |
| To | ``` class CIQRCodeFeature : CIFeature {     var bounds: CGRect { get }     var topLeft: CGPoint { get }     var topRight: CGPoint { get }     var bottomLeft: CGPoint { get }     var bottomRight: CGPoint { get }     var messageString: String { get } } ``` | CoreImage |

Modified [CIQRCodeFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437985-bottomleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.bottomRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438245-bottomright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.bounds](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438153-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.messageString](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1438035-messagestring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` var messageString: String! { get } ``` | QuartzCore |
| To | ``` var messageString: String { get } ``` | CoreImage |

Modified [CIQRCodeFeature.topLeft](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437780-topleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIQRCodeFeature.topRight](https://developer.apple.com/documentation/coreimage/ciqrcodefeature/1437896-topright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature](https://developer.apple.com/documentation/coreimage/cirectanglefeature)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bottomLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437878-bottomleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bottomRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437888-bottomright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.bounds](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438024-bounds)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.topLeft](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1437951-topleft)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIRectangleFeature.topRight](https://developer.apple.com/documentation/coreimage/cirectanglefeature/1438071-topright)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CISampler](https://developer.apple.com/documentation/coreimage/cisampler)

|  | Declaration | Introduction | Module |
| --- | --- | --- | --- |
| From | ``` class CISampler : NSObject, NSCopying {     init!(image im: CIImage!) -> CISampler     class func samplerWithImage(_ im: CIImage!) -> CISampler!     init!(image im: CIImage!, options dict: [NSObject : AnyObject]!) -> CISampler     class func samplerWithImage(_ im: CIImage!, options dict: [NSObject : AnyObject]!) -> CISampler!     init!(image im: CIImage!)     init!(image im: CIImage!, options dict: [NSObject : AnyObject]!)     func definition() -> CIFilterShape!     func extent() -> CGRect } extension CISampler {     convenience init(im im: CIImage!, elements elements: (NSCopying, AnyObject)...) } extension CISampler {     convenience init(im im: CIImage!, elements elements: (NSCopying, AnyObject)...) } ``` | OS X 10.10 | QuartzCore |
| To | ``` class CISampler : NSObject, NSCopying {     convenience init(image im: CIImage)     class func samplerWithImage(_ im: CIImage) -> Self     convenience init(image im: CIImage, options dict: [NSObject : AnyObject]?)     class func samplerWithImage(_ im: CIImage, options dict: [NSObject : AnyObject]?) -> Self     convenience init(image im: CIImage)     init(image im: CIImage, options dict: [NSObject : AnyObject]?)     var definition: CIFilterShape { get }     var extent: CGRect { get } } ``` | OS X 10.4 | CoreImage |

Modified [CISampler.init(image: CIImage)](https://developer.apple.com/documentation/coreimage/cisampler/1438117-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(image im: CIImage!) ``` | QuartzCore |
| To | ``` convenience init(image im: CIImage) ``` | CoreImage |

Modified [CISampler.init(image: CIImage, options: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/coreimage/cisampler/1437963-initwithimage)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(image im: CIImage!, options dict: [NSObject : AnyObject]!) ``` | QuartzCore |
| To | ``` init(image im: CIImage, options dict: [NSObject : AnyObject]?) ``` | CoreImage |

Modified [CIVector](https://developer.apple.com/documentation/coreimage/civector)

|  | Declaration | Protocols | Introduction | Module |
| --- | --- | --- | --- | --- |
| From | ``` class CIVector : NSObject, NSCopying, NSCoding {     init!(values values: UnsafePointer<CGFloat>, count count: Int) -> CIVector     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> CIVector!     init!(x x: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> CIVector!     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> CIVector!     init!(CGPoint p: CGPoint) -> CIVector     class func vectorWithCGPoint(_ p: CGPoint) -> CIVector!     init!(CGRect r: CGRect) -> CIVector     class func vectorWithCGRect(_ r: CGRect) -> CIVector!     init!(CGAffineTransform t: CGAffineTransform) -> CIVector     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> CIVector!     init!(string representation: String!) -> CIVector     class func vectorWithString(_ representation: String!) -> CIVector!     init!(values values: UnsafePointer<CGFloat>, count count: Int)     init!(x x: CGFloat)     init!(x x: CGFloat, y y: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat)     init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     init!(CGPoint p: CGPoint)     init!(CGRect r: CGRect)     init!(CGAffineTransform r: CGAffineTransform)     init!(string representation: String!)     func valueAtIndex(_ index: Int) -> CGFloat     func count() -> Int     func X() -> CGFloat     func Y() -> CGFloat     func Z() -> CGFloat     func W() -> CGFloat     func CGPointValue() -> CGPoint     func CGRectValue() -> CGRect     func CGAffineTransformValue() -> CGAffineTransform     func stringRepresentation() -> String! } ``` | AnyObject, NSCoding, NSCopying | OS X 10.10 | QuartzCore |
| To | ``` class CIVector : NSObject, NSCopying, NSSecureCoding, NSCoding {     convenience init(values values: UnsafePointer<CGFloat>, count count: Int)     class func vectorWithValues(_ values: UnsafePointer<CGFloat>, count count: Int) -> Self     convenience init(x x: CGFloat)     class func vectorWithX(_ x: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat) -> Self     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     class func vectorWithX(_ x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) -> Self     convenience init(CGPoint p: CGPoint)     class func vectorWithCGPoint(_ p: CGPoint) -> Self     convenience init(CGRect r: CGRect)     class func vectorWithCGRect(_ r: CGRect) -> Self     convenience init(CGAffineTransform t: CGAffineTransform)     class func vectorWithCGAffineTransform(_ t: CGAffineTransform) -> Self     convenience init(string representation: String)     class func vectorWithString(_ representation: String) -> Self     init(values values: UnsafePointer<CGFloat>, count count: Int)     convenience init(x x: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat)     convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat)     convenience init(CGPoint p: CGPoint)     convenience init(CGRect r: CGRect)     convenience init(CGAffineTransform r: CGAffineTransform)     convenience init(string representation: String)     func valueAtIndex(_ index: Int) -> CGFloat     var count: Int { get }     var X: CGFloat { get }     var Y: CGFloat { get }     var Z: CGFloat { get }     var W: CGFloat { get }     var CGPointValue: CGPoint { get }     var CGRectValue: CGRect { get }     var CGAffineTransformValue: CGAffineTransform { get }     var stringRepresentation: String { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding | OS X 10.4 | CoreImage |

Modified [CIVector.init(CGAffineTransform: CGAffineTransform)](https://developer.apple.com/documentation/coreimage/civector/1438102-initwithcgaffinetransform)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGAffineTransform r: CGAffineTransform) ``` | QuartzCore |
| To | ``` convenience init(CGAffineTransform r: CGAffineTransform) ``` | CoreImage |

Modified [CIVector.init(CGPoint: CGPoint)](https://developer.apple.com/documentation/coreimage/civector/1438133-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGPoint p: CGPoint) ``` | QuartzCore |
| To | ``` convenience init(CGPoint p: CGPoint) ``` | CoreImage |

Modified [CIVector.init(CGRect: CGRect)](https://developer.apple.com/documentation/coreimage/civector/1437644-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(CGRect r: CGRect) ``` | QuartzCore |
| To | ``` convenience init(CGRect r: CGRect) ``` | CoreImage |

Modified [CIVector.init(string: String)](https://developer.apple.com/documentation/coreimage/civector/1437938-initwithstring)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(string representation: String!) ``` | QuartzCore |
| To | ``` convenience init(string representation: String) ``` | CoreImage |

Modified [CIVector.init(values: UnsafePointer<CGFloat>, count: Int)](https://developer.apple.com/documentation/coreimage/civector/1437849-initwithvalues)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(values values: UnsafePointer<CGFloat>, count count: Int) ``` | QuartzCore |
| To | ``` init(values values: UnsafePointer<CGFloat>, count count: Int) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437657-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1437865-init)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438056-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat) ``` | CoreImage |

Modified [CIVector.init(x: CGFloat, y: CGFloat, z: CGFloat, w: CGFloat)](https://developer.apple.com/documentation/coreimage/civector/1438088-initwithx)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` init!(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` | QuartzCore |
| To | ``` convenience init(x x: CGFloat, y y: CGFloat, z z: CGFloat, w w: CGFloat) ``` | CoreImage |

Modified [CIVector.valueAtIndex(_: Int) -> CGFloat](https://developer.apple.com/documentation/coreimage/civector/1438207-value)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified NSObject.actionForLayer(_: CALayer, forKey: String) -> CAAction?

|  | Declaration |
| --- | --- |
| From | ``` func actionForLayer(_ layer: CALayer!, forKey event: String!) -> CAAction! ``` |
| To | ``` func actionForLayer(_ layer: CALayer, forKey event: String) -> CAAction? ``` |

Modified NSObject.animationDidStart(_: CAAnimation)

|  | Declaration |
| --- | --- |
| From | ``` func animationDidStart(_ anim: CAAnimation!) ``` |
| To | ``` func animationDidStart(_ anim: CAAnimation) ``` |

Modified NSObject.animationDidStop(_: CAAnimation, finished: Bool)

|  | Declaration |
| --- | --- |
| From | ``` func animationDidStop(_ anim: CAAnimation!, finished flag: Bool) ``` |
| To | ``` func animationDidStop(_ anim: CAAnimation, finished flag: Bool) ``` |

Modified NSObject.displayLayer(_: CALayer)

|  | Declaration |
| --- | --- |
| From | ``` func displayLayer(_ layer: CALayer!) ``` |
| To | ``` func displayLayer(_ layer: CALayer) ``` |

Modified NSObject.drawLayer(_: CALayer, inContext: CGContext)

|  | Declaration |
| --- | --- |
| From | ``` func drawLayer(_ layer: CALayer!, inContext ctx: CGContext!) ``` |
| To | ``` func drawLayer(_ layer: CALayer, inContext ctx: CGContext) ``` |

Modified NSObject.invalidateLayoutOfLayer(_: CALayer)

|  | Declaration |
| --- | --- |
| From | ``` func invalidateLayoutOfLayer(_ layer: CALayer!) ``` |
| To | ``` func invalidateLayoutOfLayer(_ layer: CALayer) ``` |

Modified NSObject.layoutSublayersOfLayer(_: CALayer)

|  | Declaration |
| --- | --- |
| From | ``` func layoutSublayersOfLayer(_ layer: CALayer!) ``` |
| To | ``` func layoutSublayersOfLayer(_ layer: CALayer) ``` |

Modified NSObject.preferredSizeOfLayer(_: CALayer) -> CGSize

|  | Declaration |
| --- | --- |
| From | ``` func preferredSizeOfLayer(_ layer: CALayer!) -> CGSize ``` |
| To | ``` func preferredSizeOfLayer(_ layer: CALayer) -> CGSize ``` |

Modified [NSObject.provideImageData(_: UnsafeMutablePointer<Void>, bytesPerRow: Int, origin: Int, _: Int, size: Int, _: Int, userInfo: AnyObject?)](https://developer.apple.com/documentation/objectivec/nsobject/1438175-provideimagedata)

|  | Declaration | Module |
| --- | --- | --- |
| From | ``` func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject!) ``` | QuartzCore |
| To | ``` func provideImageData(_ data: UnsafeMutablePointer<Void>, bytesPerRow rowbytes: Int, origin x: Int, _ y: Int, size width: Int, _ height: Int, userInfo info: AnyObject?) ``` | CoreImage |

Modified [NSValue.init(CATransform3D: CATransform3D)](https://developer.apple.com/documentation/foundation/nsvalue/1436556-valuewithcatransform3d)

|  | Declaration |
| --- | --- |
| From | ``` init!(CATransform3D t: CATransform3D) -> NSValue ``` |
| To | ``` init(CATransform3D t: CATransform3D) ``` |

Modified [CIDetectorAccuracy](https://developer.apple.com/documentation/coreimage/cidetectoraccuracy)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAccuracyHigh](https://developer.apple.com/documentation/coreimage/cidetectoraccuracyhigh)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAccuracyLow](https://developer.apple.com/documentation/coreimage/cidetectoraccuracylow)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorAspectRatio](https://developer.apple.com/documentation/coreimage/cidetectoraspectratio)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorEyeBlink](https://developer.apple.com/documentation/coreimage/cidetectoreyeblink)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorFocalLength](https://developer.apple.com/documentation/coreimage/cidetectorfocallength)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorImageOrientation](https://developer.apple.com/documentation/coreimage/cidetectorimageorientation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorMinFeatureSize](https://developer.apple.com/documentation/coreimage/cidetectorminfeaturesize)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorSmile](https://developer.apple.com/documentation/coreimage/cidetectorsmile)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTracking](https://developer.apple.com/documentation/coreimage/cidetectortracking)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeFace](https://developer.apple.com/documentation/coreimage/cidetectortypeface)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeQRCode](https://developer.apple.com/documentation/coreimage/cidetectortypeqrcode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIDetectorTypeRectangle](https://developer.apple.com/documentation/coreimage/cidetectortyperectangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeatureTypeFace](https://developer.apple.com/documentation/coreimage/cifeaturetypeface)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFeatureTypeRectangle](https://developer.apple.com/documentation/coreimage/cifeaturetyperectangle)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [CIFormat](https://developer.apple.com/documentation/coreimage/ciformat)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIActiveKeys](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438129-activekeys)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionColorSpace](https://developer.apple.com/documentation/coreimage/kciapplyoptioncolorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionDefinition](https://developer.apple.com/documentation/coreimage/kciapplyoptiondefinition)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionExtent](https://developer.apple.com/documentation/coreimage/kciapplyoptionextent)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIApplyOptionUserInfo](https://developer.apple.com/documentation/coreimage/kciapplyoptionuserinfo)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeClass](https://developer.apple.com/documentation/coreimage/kciattributeclass)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeDefault](https://developer.apple.com/documentation/coreimage/kciattributedefault)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeDescription](https://developer.apple.com/documentation/coreimage/kciattributedescription)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeDisplayName](https://developer.apple.com/documentation/coreimage/kciattributedisplayname)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterCategories](https://developer.apple.com/documentation/coreimage/kciattributefiltercategories)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterDisplayName](https://developer.apple.com/documentation/coreimage/kciattributefilterdisplayname)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeFilterName](https://developer.apple.com/documentation/coreimage/kciattributefiltername)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeIdentity](https://developer.apple.com/documentation/coreimage/kciattributeidentity)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeMax](https://developer.apple.com/documentation/coreimage/kciattributemax)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeMin](https://developer.apple.com/documentation/coreimage/kciattributemin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeName](https://developer.apple.com/documentation/coreimage/kciattributename)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeReferenceDocumentation](https://developer.apple.com/documentation/coreimage/kciattributereferencedocumentation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeSliderMax](https://developer.apple.com/documentation/coreimage/kciattributeslidermax)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeSliderMin](https://developer.apple.com/documentation/coreimage/kciattributeslidermin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeType](https://developer.apple.com/documentation/coreimage/kciattributetype)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeAngle](https://developer.apple.com/documentation/coreimage/kciattributetypeangle)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeBoolean](https://developer.apple.com/documentation/coreimage/kciattributetypeboolean)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeCount](https://developer.apple.com/documentation/coreimage/kciattributetypecount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeDistance](https://developer.apple.com/documentation/coreimage/kciattributetypedistance)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeGradient](https://developer.apple.com/documentation/coreimage/kciattributetypegradient)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeInteger](https://developer.apple.com/documentation/coreimage/kciattributetypeinteger)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypeOffset](https://developer.apple.com/documentation/coreimage/kciattributetypeoffset)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeOpaqueColor](https://developer.apple.com/documentation/coreimage/kciattributetypeopaquecolor)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIAttributeTypePosition](https://developer.apple.com/documentation/coreimage/kciattributetypeposition)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypePosition3](https://developer.apple.com/documentation/coreimage/kciattributetypeposition3)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeRectangle](https://developer.apple.com/documentation/coreimage/kciattributetyperectangle)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeScalar](https://developer.apple.com/documentation/coreimage/kciattributetypescalar)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIAttributeTypeTime](https://developer.apple.com/documentation/coreimage/kciattributetypetime)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryBlur](https://developer.apple.com/documentation/coreimage/kcicategoryblur)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryBuiltIn](https://developer.apple.com/documentation/coreimage/kcicategorybuiltin)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryColorAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorycoloradjustment)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryColorEffect](https://developer.apple.com/documentation/coreimage/kcicategorycoloreffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryCompositeOperation](https://developer.apple.com/documentation/coreimage/kcicategorycompositeoperation)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryDistortionEffect](https://developer.apple.com/documentation/coreimage/kcicategorydistortioneffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryFilterGenerator](https://developer.apple.com/documentation/coreimage/kcicategoryfiltergenerator)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCICategoryGenerator](https://developer.apple.com/documentation/coreimage/kcicategorygenerator)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryGeometryAdjustment](https://developer.apple.com/documentation/coreimage/kcicategorygeometryadjustment)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryGradient](https://developer.apple.com/documentation/coreimage/kcicategorygradient)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryHalftoneEffect](https://developer.apple.com/documentation/coreimage/kcicategoryhalftoneeffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryHighDynamicRange](https://developer.apple.com/documentation/coreimage/kcicategoryhighdynamicrange)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryInterlaced](https://developer.apple.com/documentation/coreimage/kcicategoryinterlaced)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryNonSquarePixels](https://developer.apple.com/documentation/coreimage/kcicategorynonsquarepixels)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryReduction](https://developer.apple.com/documentation/coreimage/kcicategoryreduction)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCICategorySharpen](https://developer.apple.com/documentation/coreimage/kcicategorysharpen)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryStillImage](https://developer.apple.com/documentation/coreimage/kcicategorystillimage)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryStylize](https://developer.apple.com/documentation/coreimage/kcicategorystylize)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryTileEffect](https://developer.apple.com/documentation/coreimage/kcicategorytileeffect)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryTransition](https://developer.apple.com/documentation/coreimage/kcicategorytransition)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCICategoryVideo](https://developer.apple.com/documentation/coreimage/kcicategoryvideo)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextOutputColorSpace](https://developer.apple.com/documentation/coreimage/cicontextoption/1438052-outputcolorspace)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextUseSoftwareRenderer](https://developer.apple.com/documentation/coreimage/cicontextoption/1438047-usesoftwarerenderer)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIContextWorkingColorSpace](https://developer.apple.com/documentation/coreimage/kcicontextworkingcolorspace)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.4 | QuartzCore |
| To | OS X 10.10 | CoreImage |

Modified [kCIFilterGeneratorExportedKey](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFilterGeneratorExportedKeyName](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeyname)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFilterGeneratorExportedKeyTargetObject](https://developer.apple.com/documentation/coreimage/kcifiltergeneratorexportedkeytargetobject)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatARGB8](https://developer.apple.com/documentation/coreimage/kciformatargb8)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBA16](https://developer.apple.com/documentation/coreimage/kciformatrgba16)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBAf](https://developer.apple.com/documentation/coreimage/kciformatrgbaf)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIFormatRGBAh](https://developer.apple.com/documentation/coreimage/kciformatrgbah)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustCrop](https://developer.apple.com/documentation/coreimage/kciimageautoadjustcrop)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustEnhance](https://developer.apple.com/documentation/coreimage/kciimageautoadjustenhance)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustFeatures](https://developer.apple.com/documentation/coreimage/kciimageautoadjustfeatures)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustLevel](https://developer.apple.com/documentation/coreimage/ciimageautoadjustmentoption/1438040-level)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageAutoAdjustRedEye](https://developer.apple.com/documentation/coreimage/kciimageautoadjustredeye)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageColorSpace](https://developer.apple.com/documentation/coreimage/ciimageoption/1438131-colorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProperties](https://developer.apple.com/documentation/coreimage/ciimageoption/1437679-properties)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProviderTileSize](https://developer.apple.com/documentation/coreimage/kciimageprovidertilesize)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageProviderUserInfo](https://developer.apple.com/documentation/coreimage/kciimageprovideruserinfo)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageTextureFormat](https://developer.apple.com/documentation/coreimage/ciimageoption/1437934-textureformat)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIImageTextureTarget](https://developer.apple.com/documentation/coreimage/kciimagetexturetarget)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAllowDraftModeKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438010-allowdraftmode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAngleKey](https://developer.apple.com/documentation/coreimage/kciinputanglekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputAspectRatioKey](https://developer.apple.com/documentation/coreimage/kciinputaspectratiokey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBackgroundImageKey](https://developer.apple.com/documentation/coreimage/kciinputbackgroundimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBiasKey](https://developer.apple.com/documentation/coreimage/kciinputbiaskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBoostKey](https://developer.apple.com/documentation/coreimage/kciinputboostkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBoostShadowAmountKey](https://developer.apple.com/documentation/coreimage/kciinputboostshadowamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputBrightnessKey](https://developer.apple.com/documentation/coreimage/kciinputbrightnesskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputCenterKey](https://developer.apple.com/documentation/coreimage/kciinputcenterkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputColorKey](https://developer.apple.com/documentation/coreimage/kciinputcolorkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputColorNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputcolornoisereductionamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputContrastKey](https://developer.apple.com/documentation/coreimage/kciinputcontrastkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputDecoderVersionKey](https://developer.apple.com/documentation/coreimage/kciinputdecoderversionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableChromaticNoiseTrackingKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438231-enablechromaticnoisetracking)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableSharpeningKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438016-enablesharpening)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEnableVendorLensCorrectionKey](https://developer.apple.com/documentation/coreimage/kciinputenablevendorlenscorrectionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputEVKey](https://developer.apple.com/documentation/coreimage/kciinputevkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputExtentKey](https://developer.apple.com/documentation/coreimage/kciinputextentkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputGradientImageKey](https://developer.apple.com/documentation/coreimage/kciinputgradientimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputIgnoreImageOrientationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437949-ignoreimageorientation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputImageKey](https://developer.apple.com/documentation/coreimage/kciinputimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputImageOrientationKey](https://developer.apple.com/documentation/coreimage/kciinputimageorientationkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputIntensityKey](https://developer.apple.com/documentation/coreimage/kciinputintensitykey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputLinearSpaceFilter](https://developer.apple.com/documentation/coreimage/kciinputlinearspacefilter)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputLuminanceNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/kciinputluminancenoisereductionamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputMaskImageKey](https://developer.apple.com/documentation/coreimage/kciinputmaskimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralChromaticityXKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437605-neutralchromaticityx)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralChromaticityYKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438039-neutralchromaticityy)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralLocationKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437915-neutrallocation)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralTemperatureKey](https://developer.apple.com/documentation/coreimage/kciinputneutraltemperaturekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNeutralTintKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438113-neutraltint)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437990-noisereductionamount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionContrastAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductioncontrastamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionDetailAmountKey](https://developer.apple.com/documentation/coreimage/kciinputnoisereductiondetailamountkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputNoiseReductionSharpnessAmountKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1438009-noisereductionsharpnessamount)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputRadiusKey](https://developer.apple.com/documentation/coreimage/kciinputradiuskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputRefractionKey](https://developer.apple.com/documentation/coreimage/kciinputrefractionkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputSaturationKey](https://developer.apple.com/documentation/coreimage/kciinputsaturationkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputScaleFactorKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437936-scalefactor)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputScaleKey](https://developer.apple.com/documentation/coreimage/kciinputscalekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputShadingImageKey](https://developer.apple.com/documentation/coreimage/kciinputshadingimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputSharpnessKey](https://developer.apple.com/documentation/coreimage/kciinputsharpnesskey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTargetImageKey](https://developer.apple.com/documentation/coreimage/kciinputtargetimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTimeKey](https://developer.apple.com/documentation/coreimage/kciinputtimekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputTransformKey](https://developer.apple.com/documentation/coreimage/kciinputtransformkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIInputWidthKey](https://developer.apple.com/documentation/coreimage/kciinputwidthkey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIOutputImageKey](https://developer.apple.com/documentation/coreimage/kcioutputimagekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIOutputNativeSizeKey](https://developer.apple.com/documentation/coreimage/kcioutputnativesizekey)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerAffineMatrix](https://developer.apple.com/documentation/coreimage/kcisampleraffinematrix)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerColorSpace](https://developer.apple.com/documentation/coreimage/kcisamplercolorspace)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterLinear](https://developer.apple.com/documentation/coreimage/kcisamplerfilterlinear)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterMode](https://developer.apple.com/documentation/coreimage/kcisamplerfiltermode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerFilterNearest](https://developer.apple.com/documentation/coreimage/kcisamplerfilternearest)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [kCISamplerWrapBlack](https://developer.apple.com/documentation/coreimage/kcisamplerwrapblack)

|  | Introduction | Module |
| --- | --- | --- |
| From | OS X 10.10 | QuartzCore |
| To | OS X 10.4 | CoreImage |

Modified [kCISamplerWrapClamp](https://developer.apple.com/documentation/coreimage/kcisamplerwrapclamp)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISamplerWrapMode](https://developer.apple.com/documentation/coreimage/kcisamplerwrapmode)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCISupportedDecoderVersionsKey](https://developer.apple.com/documentation/coreimage/cirawfilteroption/1437927-supporteddecoderversions)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUIParameterSet](https://developer.apple.com/documentation/coreimage/kciuiparameterset)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetAdvanced](https://developer.apple.com/documentation/coreimage/kciuisetadvanced)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetBasic](https://developer.apple.com/documentation/coreimage/kciuisetbasic)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetDevelopment](https://developer.apple.com/documentation/coreimage/kciuisetdevelopment)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

Modified [kCIUISetIntermediate](https://developer.apple.com/documentation/coreimage/kciuisetintermediate)

|  | Module |
| --- | --- |
| From | QuartzCore |
| To | CoreImage |

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

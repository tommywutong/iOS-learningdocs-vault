---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/QuartzCore.html
archived_at: '2026-07-18T02:56:57.457770Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# QuartzCore Changes for Swift

### QuartzCore

Removed CAEdgeAntialiasingMask.init(_: UInt32)Removed CAMetalLayer.newDrawable() -> CAMetalDrawable!Added [CAEAGLLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/caeagllayer/1618676-presentswithtransaction)Added [CAEmitterCell.contentsScale](https://developer.apple.com/documentation/quartzcore/caemittercell/1522197-contentsscale)Added [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)Added [CASpringAnimation.damping](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412532-damping)Added [CASpringAnimation.initialVelocity](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412443-initialvelocity)Added [CASpringAnimation.mass](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412540-mass)Added [CASpringAnimation.settlingDuration](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412524-settlingduration)Added [CASpringAnimation.stiffness](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412515-stiffness)Added [CATextLayer.allowsFontSubpixelQuantization](https://developer.apple.com/documentation/quartzcore/catextlayer/1515300-allowsfontsubpixelquantization)Modified [CAAction](https://developer.apple.com/documentation/quartzcore/caaction)

|  | Declaration |
| --- | --- |
| From | ``` protocol CAAction {     func runActionForKey(_ event: String!, object anObject: AnyObject!, arguments dict: [NSObject : AnyObject]!) } ``` |
| To | ``` protocol CAAction {     func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) } ``` |

Modified [CAAction.runActionForKey(_: String, object: AnyObject, arguments: [NSObject : AnyObject]?)](https://developer.apple.com/documentation/quartzcore/caaction/1410806-runactionforkey)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func runActionForKey(_ event: String!, object anObject: AnyObject!, arguments dict: [NSObject : AnyObject]!) ``` | iOS 8.0 |
| To | ``` func runActionForKey(_ event: String, object anObject: AnyObject, arguments dict: [NSObject : AnyObject]?) ``` | iOS 2.0 |

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

Modified [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)

|  | Declaration |
| --- | --- |
| From | ``` class CADisplayLink : NSObject {     init!(target target: AnyObject!, selector sel: Selector) -> CADisplayLink     class func displayLinkWithTarget(_ target: AnyObject!, selector sel: Selector) -> CADisplayLink!     func addToRunLoop(_ runloop: NSRunLoop!, forMode mode: String!)     func removeFromRunLoop(_ runloop: NSRunLoop!, forMode mode: String!)     func invalidate()     var timestamp: CFTimeInterval { get }     var duration: CFTimeInterval { get }     var paused: Bool     var frameInterval: Int } ``` |
| To | ``` class CADisplayLink : NSObject {      init(target target: AnyObject, selector sel: Selector)     class func displayLinkWithTarget(_ target: AnyObject, selector sel: Selector) -> CADisplayLink     func addToRunLoop(_ runloop: NSRunLoop, forMode mode: String)     func removeFromRunLoop(_ runloop: NSRunLoop, forMode mode: String)     func invalidate()     var timestamp: CFTimeInterval { get }     var duration: CFTimeInterval { get }     var paused: Bool     var frameInterval: Int } ``` |

Modified [CADisplayLink.addToRunLoop(_: NSRunLoop, forMode: String)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621323-add)

|  | Declaration |
| --- | --- |
| From | ``` func addToRunLoop(_ runloop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func addToRunLoop(_ runloop: NSRunLoop, forMode mode: String) ``` |

Modified [CADisplayLink.init(target: AnyObject, selector: Selector)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621228-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(target target: AnyObject!, selector sel: Selector) -> CADisplayLink ``` |
| To | ``` init(target target: AnyObject, selector sel: Selector) ``` |

Modified [CADisplayLink.removeFromRunLoop(_: NSRunLoop, forMode: String)](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621325-removefromrunloop)

|  | Declaration |
| --- | --- |
| From | ``` func removeFromRunLoop(_ runloop: NSRunLoop!, forMode mode: String!) ``` |
| To | ``` func removeFromRunLoop(_ runloop: NSRunLoop, forMode mode: String) ``` |

Modified [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAEAGLLayer : CALayer, EAGLDrawable { } ``` |
| To | ``` class CAEAGLLayer : CALayer, EAGLDrawable {     var presentsWithTransaction: Bool } ``` |

Modified [CAEdgeAntialiasingMask [struct]](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CAEdgeAntialiasingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | RawOptionSetType |
| To | ``` struct CAEdgeAntialiasingMask : OptionSetType {     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` | OptionSetType |

Modified CAEmitterBehavior

|  | Declaration |
| --- | --- |
| From | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [AnyObject]!     init!(type type: String!) -> CAEmitterBehavior     class func behaviorWithType(_ type: String!) -> CAEmitterBehavior!     init!(type type: String!)     var type: String! { get }     var name: String!     var enabled: Bool } ``` |
| To | ``` class CAEmitterBehavior : NSObject, NSCoding {     class func behaviorTypes() -> [String]      init(type type: String)     class func behaviorWithType(_ type: String) -> CAEmitterBehavior     init(type type: String)     var type: String { get }     var name: String?     var enabled: Bool } ``` |

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
| From | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init!()     class func layer() -> Self!     init!()     init!(layer layer: AnyObject!)     func presentationLayer() -> AnyObject!     func modelLayer() -> AnyObject!     class func defaultValueForKey(_ key: String!) -> AnyObject!     class func needsDisplayForKey(_ key: String!) -> Bool     func shouldArchiveValueForKey(_ key: String!) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var hidden: Bool     var doubleSided: Bool     var geometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer! { get }     func removeFromSuperlayer()     var sublayers: [AnyObject]!     func addSublayer(_ layer: CALayer!)     func insertSublayer(_ layer: CALayer!, atIndex idx: UInt32)     func insertSublayer(_ layer: CALayer!, below sibling: CALayer!)     func insertSublayer(_ layer: CALayer!, above sibling: CALayer!)     func replaceSublayer(_ layer: CALayer!, with layer2: CALayer!)     var sublayerTransform: CATransform3D     var mask: CALayer!     var masksToBounds: Bool     func convertPoint(_ p: CGPoint, fromLayer l: CALayer!) -> CGPoint     func convertPoint(_ p: CGPoint, toLayer l: CALayer!) -> CGPoint     func convertRect(_ r: CGRect, fromLayer l: CALayer!) -> CGRect     func convertRect(_ r: CGRect, toLayer l: CALayer!) -> CGRect     func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer!) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, toLayer l: CALayer!) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer!     func containsPoint(_ p: CGPoint) -> Bool     var contents: AnyObject!     var contentsRect: CGRect     var contentsGravity: String!     var contentsScale: CGFloat     var contentsCenter: CGRect     var minificationFilter: String!     var magnificationFilter: String!     var minificationFilterBias: Float     var opaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayInRect(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func drawInContext(_ ctx: CGContext!)     func renderInContext(_ ctx: CGContext!)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var allowsEdgeAntialiasing: Bool     var backgroundColor: CGColor!     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor!     var opacity: Float     var allowsGroupOpacity: Bool     var compositingFilter: AnyObject!     var filters: [AnyObject]!     var backgroundFilters: [AnyObject]!     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor!     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath!     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     class func defaultActionForKey(_ event: String!) -> CAAction!     func actionForKey(_ event: String!) -> CAAction!     var actions: [NSObject : AnyObject]!     func addAnimation(_ anim: CAAnimation!, forKey key: String!)     func removeAllAnimations()     func removeAnimationForKey(_ key: String!)     func animationKeys() -> [AnyObject]!     func animationForKey(_ key: String!) -> CAAnimation!     var name: String!     weak var delegate: AnyObject!     var style: [NSObject : AnyObject]! } extension CALayer {     func scrollPoint(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` |
| To | ``` class CALayer : NSObject, NSCoding, CAMediaTiming {     convenience init()     class func layer() -> Self     init()     init(layer layer: AnyObject)     func presentationLayer() -> AnyObject?     func modelLayer() -> AnyObject     class func defaultValueForKey(_ key: String) -> AnyObject?     class func needsDisplayForKey(_ key: String) -> Bool     func shouldArchiveValueForKey(_ key: String) -> Bool     var bounds: CGRect     var position: CGPoint     var zPosition: CGFloat     var anchorPoint: CGPoint     var anchorPointZ: CGFloat     var transform: CATransform3D     func affineTransform() -> CGAffineTransform     func setAffineTransform(_ m: CGAffineTransform)     var frame: CGRect     var hidden: Bool     var doubleSided: Bool     var geometryFlipped: Bool     func contentsAreFlipped() -> Bool     var superlayer: CALayer? { get }     func removeFromSuperlayer()     var sublayers: [CALayer]?     func addSublayer(_ layer: CALayer)     func insertSublayer(_ layer: CALayer, atIndex idx: UInt32)     func insertSublayer(_ layer: CALayer, below sibling: CALayer?)     func insertSublayer(_ layer: CALayer, above sibling: CALayer?)     func replaceSublayer(_ layer: CALayer, with layer2: CALayer)     var sublayerTransform: CATransform3D     var mask: CALayer?     var masksToBounds: Bool     func convertPoint(_ p: CGPoint, fromLayer l: CALayer?) -> CGPoint     func convertPoint(_ p: CGPoint, toLayer l: CALayer?) -> CGPoint     func convertRect(_ r: CGRect, fromLayer l: CALayer?) -> CGRect     func convertRect(_ r: CGRect, toLayer l: CALayer?) -> CGRect     func convertTime(_ t: CFTimeInterval, fromLayer l: CALayer?) -> CFTimeInterval     func convertTime(_ t: CFTimeInterval, toLayer l: CALayer?) -> CFTimeInterval     func hitTest(_ p: CGPoint) -> CALayer?     func containsPoint(_ p: CGPoint) -> Bool     var contents: AnyObject?     var contentsRect: CGRect     var contentsGravity: String     var contentsScale: CGFloat     var contentsCenter: CGRect     var minificationFilter: String     var magnificationFilter: String     var minificationFilterBias: Float     var opaque: Bool     func display()     func setNeedsDisplay()     func setNeedsDisplayInRect(_ r: CGRect)     func needsDisplay() -> Bool     func displayIfNeeded()     var needsDisplayOnBoundsChange: Bool     var drawsAsynchronously: Bool     func drawInContext(_ ctx: CGContext)     func renderInContext(_ ctx: CGContext)     var edgeAntialiasingMask: CAEdgeAntialiasingMask     var allowsEdgeAntialiasing: Bool     var backgroundColor: CGColor?     var cornerRadius: CGFloat     var borderWidth: CGFloat     var borderColor: CGColor?     var opacity: Float     var allowsGroupOpacity: Bool     var compositingFilter: AnyObject?     var filters: [AnyObject]?     var backgroundFilters: [AnyObject]?     var shouldRasterize: Bool     var rasterizationScale: CGFloat     var shadowColor: CGColor?     var shadowOpacity: Float     var shadowOffset: CGSize     var shadowRadius: CGFloat     var shadowPath: CGPath?     func preferredFrameSize() -> CGSize     func setNeedsLayout()     func needsLayout() -> Bool     func layoutIfNeeded()     func layoutSublayers()     class func defaultActionForKey(_ event: String) -> CAAction?     func actionForKey(_ event: String) -> CAAction?     var actions: [String : CAAction]?     func addAnimation(_ anim: CAAnimation, forKey key: String?)     func removeAllAnimations()     func removeAnimationForKey(_ key: String)     func animationKeys() -> [String]?     func animationForKey(_ key: String) -> CAAnimation?     var name: String?     weak var delegate: AnyObject?     var style: [NSObject : AnyObject]? } extension CALayer {     func scrollPoint(_ p: CGPoint)     func scrollRectToVisible(_ r: CGRect)     var visibleRect: CGRect { get } } ``` |

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
| From | iOS 8.0 |
| To | iOS 4.0 |

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
| From | iOS 8.0 |
| To | iOS 6.0 |

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

Modified [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable)

|  | Declaration |
| --- | --- |
| From | ``` protocol CAMetalDrawable : MTLDrawable, NSObjectProtocol {     var texture: MTLTexture! { get }     var layer: CAMetalLayer! { get } } ``` |
| To | ``` protocol CAMetalDrawable : MTLDrawable, NSObjectProtocol {     var texture: MTLTexture { get }     var layer: CAMetalLayer { get } } ``` |

Modified [CAMetalDrawable.layer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478165-layer)

|  | Declaration |
| --- | --- |
| From | ``` var layer: CAMetalLayer! { get } ``` |
| To | ``` var layer: CAMetalLayer { get } ``` |

Modified [CAMetalDrawable.texture](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478159-texture)

|  | Declaration |
| --- | --- |
| From | ``` var texture: MTLTexture! { get } ``` |
| To | ``` var texture: MTLTexture { get } ``` |

Modified [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)

|  | Declaration |
| --- | --- |
| From | ``` class CAMetalLayer : CALayer {     var device: MTLDevice!     var pixelFormat: MTLPixelFormat     var framebufferOnly: Bool     var drawableSize: CGSize     func nextDrawable() -> CAMetalDrawable!     func newDrawable() -> CAMetalDrawable!     var presentsWithTransaction: Bool } ``` |
| To | ``` class CAMetalLayer : CALayer {     var device: MTLDevice?     var pixelFormat: MTLPixelFormat     var framebufferOnly: Bool     var drawableSize: CGSize     func nextDrawable() -> CAMetalDrawable?     var presentsWithTransaction: Bool } ``` |

Modified [CAMetalLayer.device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device)

|  | Declaration |
| --- | --- |
| From | ``` var device: MTLDevice! ``` |
| To | ``` var device: MTLDevice? ``` |

Modified [CAMetalLayer.nextDrawable() -> CAMetalDrawable?](https://developer.apple.com/documentation/quartzcore/cametallayer/1478172-nextdrawable)

|  | Declaration |
| --- | --- |
| From | ``` func nextDrawable() -> CAMetalDrawable! ``` |
| To | ``` func nextDrawable() -> CAMetalDrawable? ``` |

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

Modified NSObject.layoutSublayersOfLayer(_: CALayer)

|  | Declaration |
| --- | --- |
| From | ``` func layoutSublayersOfLayer(_ layer: CALayer!) ``` |
| To | ``` func layoutSublayersOfLayer(_ layer: CALayer) ``` |

Modified [NSValue.init(CATransform3D: CATransform3D)](https://developer.apple.com/documentation/foundation/nsvalue/1436556-valuewithcatransform3d)

|  | Declaration |
| --- | --- |
| From | ``` init!(CATransform3D t: CATransform3D) -> NSValue ``` |
| To | ``` init(CATransform3D t: CATransform3D) ``` |

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

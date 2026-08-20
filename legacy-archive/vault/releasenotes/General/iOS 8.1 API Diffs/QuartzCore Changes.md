---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/QuartzCore.html
archived_at: '2026-07-18T02:56:15.840654Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

Removed CAEdgeAntialiasingMask.valueAdded CAEdgeAntialiasingMask.init(rawValue: UInt32)Added NSObject.actionForLayer(CALayer!, forKey: String!) -> CAAction!Added NSObject.animationDidStart(CAAnimation!)Added NSObject.animationDidStop(CAAnimation!, finished: Bool)Added NSObject.displayLayer(CALayer!)Added NSObject.drawLayer(CALayer!, inContext: CGContext!)Added NSObject.layoutSublayersOfLayer(CALayer!)Added NSValue.init(CATransform3D: CATransform3D)Added NSValue.CATransform3DValueModified CADisplayLink.init(target: AnyObject!, selector: Selector)

|  | Declaration |
| --- | --- |
| From | ``` init(target target: AnyObject!, selector sel: Selector) -> CADisplayLink ``` |
| To | ``` init!(target target: AnyObject!, selector sel: Selector) -> CADisplayLink ``` |

Modified CAEdgeAntialiasingMask [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CAEdgeAntialiasingMask : RawOptionSetType {     init(_ value: UInt32)     var value: UInt32     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` |
| To | ``` struct CAEdgeAntialiasingMask : RawOptionSetType {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     static var LayerLeftEdge: CAEdgeAntialiasingMask { get }     static var LayerRightEdge: CAEdgeAntialiasingMask { get }     static var LayerBottomEdge: CAEdgeAntialiasingMask { get }     static var LayerTopEdge: CAEdgeAntialiasingMask { get } } ``` |

Modified CAEdgeAntialiasingMask.init(_: UInt32)

|  | Declaration |
| --- | --- |
| From | ``` init(_ value: UInt32) ``` |
| To | ``` init(_ rawValue: UInt32) ``` |

Modified CAEmitterBehavior.init(type: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(type type: String!) ``` |
| To | ``` init!(type type: String!) ``` |

Modified CALayer.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified CALayer.init(layer: AnyObject!)

|  | Declaration |
| --- | --- |
| From | ``` init(layer layer: AnyObject!) ``` |
| To | ``` init!(layer layer: AnyObject!) ``` |

Modified CAMediaTimingFunction.init(controlPoints: Float, _: Float, _: Float, _: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |
| To | ``` init!(controlPoints c1x: Float, _ c1y: Float, _ c2x: Float, _ c2y: Float) ``` |

Modified CAMediaTimingFunction.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init!(name name: String!) ``` |

Modified CAPropertyAnimation.init(keyPath: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(keyPath path: String!) ``` |
| To | ``` convenience init!(keyPath path: String!) ``` |

Modified CAValueFunction.init(name: String!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(name name: String!) ``` |
| To | ``` convenience init!(name name: String!) ``` |

Modified CACurrentMediaTime() -> CFTimeInterval

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DConcat(CATransform3D, CATransform3D) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DEqualToTransform(CATransform3D, CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DGetAffineTransform(CATransform3D) -> CGAffineTransform

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DIdentity

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DInvert(CATransform3D) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DIsAffine(CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DIsIdentity(CATransform3D) -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DMakeAffineTransform(CGAffineTransform) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DRotate(CATransform3D, CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DScale(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified CATransform3DTranslate(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAAlignmentCenter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAAlignmentJustified

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAAlignmentLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAAlignmentNatural

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAAlignmentRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAAnimationCubic

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCAAnimationCubicPaced

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCAAnimationDiscrete

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAAnimationLinear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAAnimationPaced

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAAnimationRotateAuto

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAAnimationRotateAutoReverse

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAEmitterLayerAdditive

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerBackToFront

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerCircle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerCuboid

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerLine

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerOldestFirst

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerOldestLast

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerOutline

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerPoint

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerPoints

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerRectangle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerSphere

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerSurface

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerUnordered

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAEmitterLayerVolume

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kCAFillModeBackwards

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFillModeBoth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFillModeForwards

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFillModeRemoved

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFillRuleEvenOdd

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAFillRuleNonZero

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAFilterLinear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFilterNearest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAFilterTrilinear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAGradientLayerAxial

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAGravityBottom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityBottomLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityBottomRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityCenter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityResize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityResizeAspect

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityResizeAspectFill

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityTop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityTopLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAGravityTopRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCALineCapButt

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCALineCapRound

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCALineCapSquare

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCALineJoinBevel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCALineJoinMiter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCALineJoinRound

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAMediaTimingFunctionDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAMediaTimingFunctionEaseIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAMediaTimingFunctionEaseInEaseOut

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAMediaTimingFunctionEaseOut

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAMediaTimingFunctionLinear

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAOnOrderIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAOnOrderOut

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAScrollBoth

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAScrollHorizontally

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAScrollNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCAScrollVertically

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransactionAnimationDuration

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransactionAnimationTimingFunction

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCATransactionCompletionBlock

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kCATransactionDisableActions

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransition

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionFade

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionFromBottom

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionFromLeft

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionFromRight

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionFromTop

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionMoveIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionPush

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATransitionReveal

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 2.0 |

Modified kCATruncationEnd

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCATruncationMiddle

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCATruncationNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCATruncationStart

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.2 |

Modified kCAValueFunctionRotateX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionRotateY

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionRotateZ

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionScale

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionScaleX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionScaleY

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionScaleZ

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionTranslate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionTranslateX

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionTranslateY

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kCAValueFunctionTranslateZ

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

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

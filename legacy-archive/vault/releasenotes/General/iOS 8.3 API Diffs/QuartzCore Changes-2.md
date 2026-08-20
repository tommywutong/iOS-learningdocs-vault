---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/QuartzCore.html
archived_at: '2026-07-18T02:56:27.318306Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

Added CATransform3D.init()Added CATransform3D.init(m11: CGFloat, m12: CGFloat, m13: CGFloat, m14: CGFloat, m21: CGFloat, m22: CGFloat, m23: CGFloat, m24: CGFloat, m31: CGFloat, m32: CGFloat, m33: CGFloat, m34: CGFloat, m41: CGFloat, m42: CGFloat, m43: CGFloat, m44: CGFloat)Modified CAMediaTimingFunction.getControlPointAtIndex(Int, values: UnsafeMutablePointer<Float>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func getControlPointAtIndex(_ idx: UInt, values ptr: UnsafeMutablePointer<Float>) ``` | iOS 8.0 |
| To | ``` func getControlPointAtIndex(_ idx: Int, values ptr: UnsafeMutablePointer<Float>) ``` | iOS 8.3 |

Modified CATiledLayer.levelsOfDetail

|  | Declaration |
| --- | --- |
| From | ``` var levelsOfDetail: UInt ``` |
| To | ``` var levelsOfDetail: Int ``` |

Modified CATiledLayer.levelsOfDetailBias

|  | Declaration |
| --- | --- |
| From | ``` var levelsOfDetailBias: UInt ``` |
| To | ``` var levelsOfDetailBias: Int ``` |

Modified CATransform3D [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat } ``` |
| To | ``` struct CATransform3D {     var m11: CGFloat     var m12: CGFloat     var m13: CGFloat     var m14: CGFloat     var m21: CGFloat     var m22: CGFloat     var m23: CGFloat     var m24: CGFloat     var m31: CGFloat     var m32: CGFloat     var m33: CGFloat     var m34: CGFloat     var m41: CGFloat     var m42: CGFloat     var m43: CGFloat     var m44: CGFloat     init()     init(m11 m11: CGFloat, m12 m12: CGFloat, m13 m13: CGFloat, m14 m14: CGFloat, m21 m21: CGFloat, m22 m22: CGFloat, m23 m23: CGFloat, m24 m24: CGFloat, m31 m31: CGFloat, m32 m32: CGFloat, m33 m33: CGFloat, m34 m34: CGFloat, m41 m41: CGFloat, m42 m42: CGFloat, m43 m43: CGFloat, m44 m44: CGFloat) } ``` |

Modified kCAAlignmentCenter

|  | Declaration |
| --- | --- |
| From | ``` let kCAAlignmentCenter: NSString! ``` |
| To | ``` let kCAAlignmentCenter: String ``` |

Modified kCAAlignmentJustified

|  | Declaration |
| --- | --- |
| From | ``` let kCAAlignmentJustified: NSString! ``` |
| To | ``` let kCAAlignmentJustified: String ``` |

Modified kCAAlignmentLeft

|  | Declaration |
| --- | --- |
| From | ``` let kCAAlignmentLeft: NSString! ``` |
| To | ``` let kCAAlignmentLeft: String ``` |

Modified kCAAlignmentNatural

|  | Declaration |
| --- | --- |
| From | ``` let kCAAlignmentNatural: NSString! ``` |
| To | ``` let kCAAlignmentNatural: String ``` |

Modified kCAAlignmentRight

|  | Declaration |
| --- | --- |
| From | ``` let kCAAlignmentRight: NSString! ``` |
| To | ``` let kCAAlignmentRight: String ``` |

Modified kCAAnimationCubic

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationCubic: NSString! ``` |
| To | ``` let kCAAnimationCubic: String ``` |

Modified kCAAnimationCubicPaced

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationCubicPaced: NSString! ``` |
| To | ``` let kCAAnimationCubicPaced: String ``` |

Modified kCAAnimationDiscrete

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationDiscrete: NSString! ``` |
| To | ``` let kCAAnimationDiscrete: String ``` |

Modified kCAAnimationLinear

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationLinear: NSString! ``` |
| To | ``` let kCAAnimationLinear: String ``` |

Modified kCAAnimationPaced

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationPaced: NSString! ``` |
| To | ``` let kCAAnimationPaced: String ``` |

Modified kCAAnimationRotateAuto

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationRotateAuto: NSString! ``` |
| To | ``` let kCAAnimationRotateAuto: String ``` |

Modified kCAAnimationRotateAutoReverse

|  | Declaration |
| --- | --- |
| From | ``` let kCAAnimationRotateAutoReverse: NSString! ``` |
| To | ``` let kCAAnimationRotateAutoReverse: String ``` |

Modified kCAEmitterBehaviorAlignToMotion

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorAlignToMotion: NSString! ``` |
| To | ``` let kCAEmitterBehaviorAlignToMotion: String ``` |

Modified kCAEmitterBehaviorAttractor

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorAttractor: NSString! ``` |
| To | ``` let kCAEmitterBehaviorAttractor: String ``` |

Modified kCAEmitterBehaviorColorOverLife

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorColorOverLife: NSString! ``` |
| To | ``` let kCAEmitterBehaviorColorOverLife: String ``` |

Modified kCAEmitterBehaviorDrag

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorDrag: NSString! ``` |
| To | ``` let kCAEmitterBehaviorDrag: String ``` |

Modified kCAEmitterBehaviorLight

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorLight: NSString! ``` |
| To | ``` let kCAEmitterBehaviorLight: String ``` |

Modified kCAEmitterBehaviorValueOverLife

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorValueOverLife: NSString! ``` |
| To | ``` let kCAEmitterBehaviorValueOverLife: String ``` |

Modified kCAEmitterBehaviorWave

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterBehaviorWave: NSString! ``` |
| To | ``` let kCAEmitterBehaviorWave: String ``` |

Modified kCAEmitterLayerAdditive

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerAdditive: NSString! ``` |
| To | ``` let kCAEmitterLayerAdditive: String ``` |

Modified kCAEmitterLayerBackToFront

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerBackToFront: NSString! ``` |
| To | ``` let kCAEmitterLayerBackToFront: String ``` |

Modified kCAEmitterLayerCircle

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerCircle: NSString! ``` |
| To | ``` let kCAEmitterLayerCircle: String ``` |

Modified kCAEmitterLayerCuboid

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerCuboid: NSString! ``` |
| To | ``` let kCAEmitterLayerCuboid: String ``` |

Modified kCAEmitterLayerLine

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerLine: NSString! ``` |
| To | ``` let kCAEmitterLayerLine: String ``` |

Modified kCAEmitterLayerOldestFirst

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerOldestFirst: NSString! ``` |
| To | ``` let kCAEmitterLayerOldestFirst: String ``` |

Modified kCAEmitterLayerOldestLast

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerOldestLast: NSString! ``` |
| To | ``` let kCAEmitterLayerOldestLast: String ``` |

Modified kCAEmitterLayerOutline

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerOutline: NSString! ``` |
| To | ``` let kCAEmitterLayerOutline: String ``` |

Modified kCAEmitterLayerPoint

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerPoint: NSString! ``` |
| To | ``` let kCAEmitterLayerPoint: String ``` |

Modified kCAEmitterLayerPoints

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerPoints: NSString! ``` |
| To | ``` let kCAEmitterLayerPoints: String ``` |

Modified kCAEmitterLayerRectangle

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerRectangle: NSString! ``` |
| To | ``` let kCAEmitterLayerRectangle: String ``` |

Modified kCAEmitterLayerSphere

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerSphere: NSString! ``` |
| To | ``` let kCAEmitterLayerSphere: String ``` |

Modified kCAEmitterLayerSurface

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerSurface: NSString! ``` |
| To | ``` let kCAEmitterLayerSurface: String ``` |

Modified kCAEmitterLayerUnordered

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerUnordered: NSString! ``` |
| To | ``` let kCAEmitterLayerUnordered: String ``` |

Modified kCAEmitterLayerVolume

|  | Declaration |
| --- | --- |
| From | ``` let kCAEmitterLayerVolume: NSString! ``` |
| To | ``` let kCAEmitterLayerVolume: String ``` |

Modified kCAFillModeBackwards

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillModeBackwards: NSString! ``` |
| To | ``` let kCAFillModeBackwards: String ``` |

Modified kCAFillModeBoth

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillModeBoth: NSString! ``` |
| To | ``` let kCAFillModeBoth: String ``` |

Modified kCAFillModeForwards

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillModeForwards: NSString! ``` |
| To | ``` let kCAFillModeForwards: String ``` |

Modified kCAFillModeRemoved

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillModeRemoved: NSString! ``` |
| To | ``` let kCAFillModeRemoved: String ``` |

Modified kCAFillRuleEvenOdd

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillRuleEvenOdd: NSString! ``` |
| To | ``` let kCAFillRuleEvenOdd: String ``` |

Modified kCAFillRuleNonZero

|  | Declaration |
| --- | --- |
| From | ``` let kCAFillRuleNonZero: NSString! ``` |
| To | ``` let kCAFillRuleNonZero: String ``` |

Modified kCAFilterLinear

|  | Declaration |
| --- | --- |
| From | ``` let kCAFilterLinear: NSString! ``` |
| To | ``` let kCAFilterLinear: String ``` |

Modified kCAFilterNearest

|  | Declaration |
| --- | --- |
| From | ``` let kCAFilterNearest: NSString! ``` |
| To | ``` let kCAFilterNearest: String ``` |

Modified kCAFilterTrilinear

|  | Declaration |
| --- | --- |
| From | ``` let kCAFilterTrilinear: NSString! ``` |
| To | ``` let kCAFilterTrilinear: String ``` |

Modified kCAGradientLayerAxial

|  | Declaration |
| --- | --- |
| From | ``` let kCAGradientLayerAxial: NSString! ``` |
| To | ``` let kCAGradientLayerAxial: String ``` |

Modified kCAGravityBottom

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityBottom: NSString! ``` |
| To | ``` let kCAGravityBottom: String ``` |

Modified kCAGravityBottomLeft

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityBottomLeft: NSString! ``` |
| To | ``` let kCAGravityBottomLeft: String ``` |

Modified kCAGravityBottomRight

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityBottomRight: NSString! ``` |
| To | ``` let kCAGravityBottomRight: String ``` |

Modified kCAGravityCenter

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityCenter: NSString! ``` |
| To | ``` let kCAGravityCenter: String ``` |

Modified kCAGravityLeft

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityLeft: NSString! ``` |
| To | ``` let kCAGravityLeft: String ``` |

Modified kCAGravityResize

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityResize: NSString! ``` |
| To | ``` let kCAGravityResize: String ``` |

Modified kCAGravityResizeAspect

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityResizeAspect: NSString! ``` |
| To | ``` let kCAGravityResizeAspect: String ``` |

Modified kCAGravityResizeAspectFill

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityResizeAspectFill: NSString! ``` |
| To | ``` let kCAGravityResizeAspectFill: String ``` |

Modified kCAGravityRight

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityRight: NSString! ``` |
| To | ``` let kCAGravityRight: String ``` |

Modified kCAGravityTop

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityTop: NSString! ``` |
| To | ``` let kCAGravityTop: String ``` |

Modified kCAGravityTopLeft

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityTopLeft: NSString! ``` |
| To | ``` let kCAGravityTopLeft: String ``` |

Modified kCAGravityTopRight

|  | Declaration |
| --- | --- |
| From | ``` let kCAGravityTopRight: NSString! ``` |
| To | ``` let kCAGravityTopRight: String ``` |

Modified kCALineCapButt

|  | Declaration |
| --- | --- |
| From | ``` let kCALineCapButt: NSString! ``` |
| To | ``` let kCALineCapButt: String ``` |

Modified kCALineCapRound

|  | Declaration |
| --- | --- |
| From | ``` let kCALineCapRound: NSString! ``` |
| To | ``` let kCALineCapRound: String ``` |

Modified kCALineCapSquare

|  | Declaration |
| --- | --- |
| From | ``` let kCALineCapSquare: NSString! ``` |
| To | ``` let kCALineCapSquare: String ``` |

Modified kCALineJoinBevel

|  | Declaration |
| --- | --- |
| From | ``` let kCALineJoinBevel: NSString! ``` |
| To | ``` let kCALineJoinBevel: String ``` |

Modified kCALineJoinMiter

|  | Declaration |
| --- | --- |
| From | ``` let kCALineJoinMiter: NSString! ``` |
| To | ``` let kCALineJoinMiter: String ``` |

Modified kCALineJoinRound

|  | Declaration |
| --- | --- |
| From | ``` let kCALineJoinRound: NSString! ``` |
| To | ``` let kCALineJoinRound: String ``` |

Modified kCAMediaTimingFunctionDefault

|  | Declaration |
| --- | --- |
| From | ``` let kCAMediaTimingFunctionDefault: NSString! ``` |
| To | ``` let kCAMediaTimingFunctionDefault: String ``` |

Modified kCAMediaTimingFunctionEaseIn

|  | Declaration |
| --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseIn: NSString! ``` |
| To | ``` let kCAMediaTimingFunctionEaseIn: String ``` |

Modified kCAMediaTimingFunctionEaseInEaseOut

|  | Declaration |
| --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseInEaseOut: NSString! ``` |
| To | ``` let kCAMediaTimingFunctionEaseInEaseOut: String ``` |

Modified kCAMediaTimingFunctionEaseOut

|  | Declaration |
| --- | --- |
| From | ``` let kCAMediaTimingFunctionEaseOut: NSString! ``` |
| To | ``` let kCAMediaTimingFunctionEaseOut: String ``` |

Modified kCAMediaTimingFunctionLinear

|  | Declaration |
| --- | --- |
| From | ``` let kCAMediaTimingFunctionLinear: NSString! ``` |
| To | ``` let kCAMediaTimingFunctionLinear: String ``` |

Modified kCAOnOrderIn

|  | Declaration |
| --- | --- |
| From | ``` let kCAOnOrderIn: NSString! ``` |
| To | ``` let kCAOnOrderIn: String ``` |

Modified kCAOnOrderOut

|  | Declaration |
| --- | --- |
| From | ``` let kCAOnOrderOut: NSString! ``` |
| To | ``` let kCAOnOrderOut: String ``` |

Modified kCAScrollBoth

|  | Declaration |
| --- | --- |
| From | ``` let kCAScrollBoth: NSString! ``` |
| To | ``` let kCAScrollBoth: String ``` |

Modified kCAScrollHorizontally

|  | Declaration |
| --- | --- |
| From | ``` let kCAScrollHorizontally: NSString! ``` |
| To | ``` let kCAScrollHorizontally: String ``` |

Modified kCAScrollNone

|  | Declaration |
| --- | --- |
| From | ``` let kCAScrollNone: NSString! ``` |
| To | ``` let kCAScrollNone: String ``` |

Modified kCAScrollVertically

|  | Declaration |
| --- | --- |
| From | ``` let kCAScrollVertically: NSString! ``` |
| To | ``` let kCAScrollVertically: String ``` |

Modified kCATransactionAnimationDuration

|  | Declaration |
| --- | --- |
| From | ``` let kCATransactionAnimationDuration: NSString! ``` |
| To | ``` let kCATransactionAnimationDuration: String ``` |

Modified kCATransactionAnimationTimingFunction

|  | Declaration |
| --- | --- |
| From | ``` let kCATransactionAnimationTimingFunction: NSString! ``` |
| To | ``` let kCATransactionAnimationTimingFunction: String ``` |

Modified kCATransactionCompletionBlock

|  | Declaration |
| --- | --- |
| From | ``` let kCATransactionCompletionBlock: NSString! ``` |
| To | ``` let kCATransactionCompletionBlock: String ``` |

Modified kCATransactionDisableActions

|  | Declaration |
| --- | --- |
| From | ``` let kCATransactionDisableActions: NSString! ``` |
| To | ``` let kCATransactionDisableActions: String ``` |

Modified kCATransition

|  | Declaration |
| --- | --- |
| From | ``` let kCATransition: NSString! ``` |
| To | ``` let kCATransition: String ``` |

Modified kCATransitionFade

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionFade: NSString! ``` |
| To | ``` let kCATransitionFade: String ``` |

Modified kCATransitionFromBottom

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionFromBottom: NSString! ``` |
| To | ``` let kCATransitionFromBottom: String ``` |

Modified kCATransitionFromLeft

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionFromLeft: NSString! ``` |
| To | ``` let kCATransitionFromLeft: String ``` |

Modified kCATransitionFromRight

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionFromRight: NSString! ``` |
| To | ``` let kCATransitionFromRight: String ``` |

Modified kCATransitionFromTop

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionFromTop: NSString! ``` |
| To | ``` let kCATransitionFromTop: String ``` |

Modified kCATransitionMoveIn

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionMoveIn: NSString! ``` |
| To | ``` let kCATransitionMoveIn: String ``` |

Modified kCATransitionPush

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionPush: NSString! ``` |
| To | ``` let kCATransitionPush: String ``` |

Modified kCATransitionReveal

|  | Declaration |
| --- | --- |
| From | ``` let kCATransitionReveal: NSString! ``` |
| To | ``` let kCATransitionReveal: String ``` |

Modified kCATruncationEnd

|  | Declaration |
| --- | --- |
| From | ``` let kCATruncationEnd: NSString! ``` |
| To | ``` let kCATruncationEnd: String ``` |

Modified kCATruncationMiddle

|  | Declaration |
| --- | --- |
| From | ``` let kCATruncationMiddle: NSString! ``` |
| To | ``` let kCATruncationMiddle: String ``` |

Modified kCATruncationNone

|  | Declaration |
| --- | --- |
| From | ``` let kCATruncationNone: NSString! ``` |
| To | ``` let kCATruncationNone: String ``` |

Modified kCATruncationStart

|  | Declaration |
| --- | --- |
| From | ``` let kCATruncationStart: NSString! ``` |
| To | ``` let kCATruncationStart: String ``` |

Modified kCAValueFunctionRotateX

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionRotateX: NSString! ``` |
| To | ``` let kCAValueFunctionRotateX: String ``` |

Modified kCAValueFunctionRotateY

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionRotateY: NSString! ``` |
| To | ``` let kCAValueFunctionRotateY: String ``` |

Modified kCAValueFunctionRotateZ

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionRotateZ: NSString! ``` |
| To | ``` let kCAValueFunctionRotateZ: String ``` |

Modified kCAValueFunctionScale

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionScale: NSString! ``` |
| To | ``` let kCAValueFunctionScale: String ``` |

Modified kCAValueFunctionScaleX

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionScaleX: NSString! ``` |
| To | ``` let kCAValueFunctionScaleX: String ``` |

Modified kCAValueFunctionScaleY

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionScaleY: NSString! ``` |
| To | ``` let kCAValueFunctionScaleY: String ``` |

Modified kCAValueFunctionScaleZ

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionScaleZ: NSString! ``` |
| To | ``` let kCAValueFunctionScaleZ: String ``` |

Modified kCAValueFunctionTranslate

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionTranslate: NSString! ``` |
| To | ``` let kCAValueFunctionTranslate: String ``` |

Modified kCAValueFunctionTranslateX

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionTranslateX: NSString! ``` |
| To | ``` let kCAValueFunctionTranslateX: String ``` |

Modified kCAValueFunctionTranslateY

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionTranslateY: NSString! ``` |
| To | ``` let kCAValueFunctionTranslateY: String ``` |

Modified kCAValueFunctionTranslateZ

|  | Declaration |
| --- | --- |
| From | ``` let kCAValueFunctionTranslateZ: NSString! ``` |
| To | ``` let kCAValueFunctionTranslateZ: String ``` |

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

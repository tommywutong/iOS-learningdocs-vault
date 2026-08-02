---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/CoreMotion.html
archived_at: '2026-07-18T02:56:23.205601Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# CoreMotion Changes

## CoreMotion

Removed CMAttitudeReferenceFrame.init(_: UInt32)Removed CMAttitudeReferenceFrame.valueRemoved CMAttitudeReferenceFrameXArbitraryCorrectedZVerticalRemoved CMAttitudeReferenceFrameXArbitraryZVerticalRemoved CMAttitudeReferenceFrameXMagneticNorthZVerticalRemoved CMAttitudeReferenceFrameXTrueNorthZVerticalAdded CMAcceleration.init()Added CMAcceleration.init(x: Double, y: Double, z: Double)Added CMAttitudeReferenceFrame.XArbitraryCorrectedZVerticalAdded CMAttitudeReferenceFrame.XArbitraryZVerticalAdded CMAttitudeReferenceFrame.XMagneticNorthZVerticalAdded CMAttitudeReferenceFrame.XTrueNorthZVerticalAdded CMAttitudeReferenceFrame.init(_: UInt)Added CMAttitudeReferenceFrame.init(rawValue: UInt)Added CMCalibratedMagneticField.init()Added CMCalibratedMagneticField.init(field: CMMagneticField, accuracy: CMMagneticFieldCalibrationAccuracy)Added CMMagneticField.init()Added CMMagneticField.init(x: Double, y: Double, z: Double)Added CMQuaternion.init()Added CMQuaternion.init(x: Double, y: Double, z: Double, w: Double)Added CMRotationMatrix.init()Added CMRotationMatrix.init(m11: Double, m12: Double, m13: Double, m21: Double, m22: Double, m23: Double, m31: Double, m32: Double, m33: Double)Added CMRotationRate.init()Added CMRotationRate.init(x: Double, y: Double, z: Double)Modified CMAcceleration [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMAcceleration {     var x: Double     var y: Double     var z: Double } ``` |
| To | ``` struct CMAcceleration {     var x: Double     var y: Double     var z: Double     init()     init(x x: Double, y y: Double, z z: Double) } ``` |

Modified CMAttitudeReferenceFrame [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMAttitudeReferenceFrame {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CMAttitudeReferenceFrame : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var XArbitraryZVertical: CMAttitudeReferenceFrame { get }     static var XArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }     static var XMagneticNorthZVertical: CMAttitudeReferenceFrame { get }     static var XTrueNorthZVertical: CMAttitudeReferenceFrame { get } } ``` | RawOptionSetType |

Modified CMCalibratedMagneticField [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMCalibratedMagneticField {     var field: CMMagneticField     var accuracy: CMMagneticFieldCalibrationAccuracy } ``` |
| To | ``` struct CMCalibratedMagneticField {     var field: CMMagneticField     var accuracy: CMMagneticFieldCalibrationAccuracy     init()     init(field field: CMMagneticField, accuracy accuracy: CMMagneticFieldCalibrationAccuracy) } ``` |

Modified CMMagneticField [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMMagneticField {     var x: Double     var y: Double     var z: Double } ``` |
| To | ``` struct CMMagneticField {     var x: Double     var y: Double     var z: Double     init()     init(x x: Double, y y: Double, z z: Double) } ``` |

Modified CMMotionManager.availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame [class]

|  | Declaration |
| --- | --- |
| From | ``` class func availableAttitudeReferenceFrames() -> Int ``` |
| To | ``` class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame ``` |

Modified CMQuaternion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMQuaternion {     var x: Double     var y: Double     var z: Double     var w: Double } ``` |
| To | ``` struct CMQuaternion {     var x: Double     var y: Double     var z: Double     var w: Double     init()     init(x x: Double, y y: Double, z z: Double, w w: Double) } ``` |

Modified CMRotationMatrix [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMRotationMatrix {     var m11: Double     var m12: Double     var m13: Double     var m21: Double     var m22: Double     var m23: Double     var m31: Double     var m32: Double     var m33: Double } ``` |
| To | ``` struct CMRotationMatrix {     var m11: Double     var m12: Double     var m13: Double     var m21: Double     var m22: Double     var m23: Double     var m31: Double     var m32: Double     var m33: Double     init()     init(m11 m11: Double, m12 m12: Double, m13 m13: Double, m21 m21: Double, m22 m22: Double, m23 m23: Double, m31 m31: Double, m32 m32: Double, m33 m33: Double) } ``` |

Modified CMRotationRate [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CMRotationRate {     var x: Double     var y: Double     var z: Double } ``` |
| To | ``` struct CMRotationRate {     var x: Double     var y: Double     var z: Double     init()     init(x x: Double, y y: Double, z z: Double) } ``` |

Modified CMErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let CMErrorDomain: NSString! ``` |
| To | ``` let CMErrorDomain: String ``` |

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

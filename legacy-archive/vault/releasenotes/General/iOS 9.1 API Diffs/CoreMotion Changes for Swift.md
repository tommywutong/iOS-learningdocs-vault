---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreMotion.html
archived_at: '2026-07-18T02:57:07.598435Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreMotion Changes for Swift

### CoreMotion

Modified [CMAccelerometerData](https://developer.apple.com/documentation/coremotion/cmaccelerometerdata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMAltitudeData](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMAttitude](https://developer.apple.com/documentation/coremotion/cmattitude)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding, NSCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiplyByInverseOfAttitude(_ attitude: CMAttitude) } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiplyByInverseOfAttitude(_ attitude: CMAttitude) } ``` | NSCopying, NSSecureCoding |

Modified [CMDeviceMotion](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMError [struct]](https://developer.apple.com/documentation/coremotion/cmerror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMError : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct CMError : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

Modified [CMGyroData](https://developer.apple.com/documentation/coremotion/cmgyrodata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMLogItem](https://developer.apple.com/documentation/coremotion/cmlogitem)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMLogItem : NSObject, NSSecureCoding, NSCoding, NSCopying {     var timestamp: NSTimeInterval { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CMLogItem : NSObject, NSSecureCoding, NSCopying {     var timestamp: NSTimeInterval { get } } ``` | NSCopying, NSSecureCoding |

Modified [CMMagneticFieldCalibrationAccuracy [struct]](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMMagneticFieldCalibrationAccuracy : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |
| To | ``` struct CMMagneticFieldCalibrationAccuracy : RawRepresentable, Equatable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | Equatable, RawRepresentable |

Modified [CMMagnetometerData](https://developer.apple.com/documentation/coremotion/cmmagnetometerdata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMMotionActivityConfidence [enum]](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCoding, NSCopying {     var startDate: NSDate { get }     var endDate: NSDate { get }     var numberOfSteps: NSNumber { get }     var distance: NSNumber? { get }     var floorsAscended: NSNumber? { get }     var floorsDescended: NSNumber? { get }     var currentPace: NSNumber? { get }     var currentCadence: NSNumber? { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCopying {     var startDate: NSDate { get }     var endDate: NSDate { get }     var numberOfSteps: NSNumber { get }     var distance: NSNumber? { get }     var floorsAscended: NSNumber? { get }     var floorsDescended: NSNumber? { get }     var currentPace: NSNumber? { get }     var currentCadence: NSNumber? { get } } ``` | NSCopying, NSSecureCoding |

Modified [CMRecordedAccelerometerData](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMSensorDataList](https://developer.apple.com/documentation/coremotion/cmsensordatalist)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | NSFastEnumeration |

Modified [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

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

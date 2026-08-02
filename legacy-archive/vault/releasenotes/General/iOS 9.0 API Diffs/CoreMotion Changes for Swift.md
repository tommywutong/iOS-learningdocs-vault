---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/CoreMotion.html
archived_at: '2026-07-18T02:56:46.852644Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# CoreMotion Changes for Swift

### CoreMotion

Removed CMAttitudeReferenceFrame.init(_: UInt)Removed CMError.valueRemoved CMMagneticFieldCalibrationAccuracy.valueAdded CMError.init(rawValue: UInt32)Added CMError.rawValueAdded CMMagneticFieldCalibrationAccuracy.init(rawValue: Int32)Added CMMagneticFieldCalibrationAccuracy.rawValueAdded [CMPedometer.isCadenceAvailable() -> Bool [class]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613948-iscadenceavailable)Added [CMPedometer.isPaceAvailable() -> Bool [class]](https://developer.apple.com/documentation/coremotion/cmpedometer/1613938-ispaceavailable)Added [CMPedometerData.currentCadence](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613969-currentcadence)Added [CMPedometerData.currentPace](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613971-currentpace)Added [CMRecordedAccelerometerData](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata)Added [CMRecordedAccelerometerData.identifier](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/1616134-identifier)Added [CMRecordedAccelerometerData.startDate](https://developer.apple.com/documentation/coremotion/cmrecordedaccelerometerdata/1616130-startdate)Added [CMSensorDataList](https://developer.apple.com/documentation/coremotion/cmsensordatalist)Added [CMSensorRecorder](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)Added CMSensorRecorder.accelerometerDataFrom(_: NSDate, to: NSDate) -> CMSensorDataList?Added [CMSensorRecorder.accelerometerDataSince(_: UInt64) -> CMSensorDataList?](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1804909-accelerometerdatasince)Added [CMSensorRecorder.isAccelerometerRecordingAvailable() -> Bool [class]](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1615943-isaccelerometerrecordingavailabl)Added [CMSensorRecorder.isAuthorizedForRecording() -> Bool [class]](https://developer.apple.com/documentation/coremotion/cmsensorrecorder/1616021-isauthorizedforrecording)Added CMSensorRecorder.recordAccelerometerFor(_: NSTimeInterval)Modified [CMAltimeter](https://developer.apple.com/documentation/coremotion/cmaltimeter)

|  | Declaration |
| --- | --- |
| From | ``` class CMAltimeter : NSObject {     class func isRelativeAltitudeAvailable() -> Bool     func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMAltitudeHandler!)     func stopRelativeAltitudeUpdates() } ``` |
| To | ``` class CMAltimeter : NSObject {     class func isRelativeAltitudeAvailable() -> Bool     func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAltitudeHandler)     func stopRelativeAltitudeUpdates() } ``` |

Modified [CMAltimeter.startRelativeAltitudeUpdatesToQueue(_: NSOperationQueue, withHandler: CMAltitudeHandler)](https://developer.apple.com/documentation/coremotion/cmaltimeter/1616004-startrelativealtitudeupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMAltitudeHandler!) ``` |
| To | ``` func startRelativeAltitudeUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAltitudeHandler) ``` |

Modified [CMAltitudeData](https://developer.apple.com/documentation/coremotion/cmaltitudedata)

|  | Declaration |
| --- | --- |
| From | ``` class CMAltitudeData : CMLogItem {     var relativeAltitude: NSNumber! { get }     var pressure: NSNumber! { get } } ``` |
| To | ``` class CMAltitudeData : CMLogItem {     var relativeAltitude: NSNumber { get }     var pressure: NSNumber { get } } ``` |

Modified [CMAltitudeData.pressure](https://developer.apple.com/documentation/coremotion/cmaltitudedata/1616152-pressure)

|  | Declaration |
| --- | --- |
| From | ``` var pressure: NSNumber! { get } ``` |
| To | ``` var pressure: NSNumber { get } ``` |

Modified [CMAltitudeData.relativeAltitude](https://developer.apple.com/documentation/coremotion/cmaltitudedata/1615907-relativealtitude)

|  | Declaration |
| --- | --- |
| From | ``` var relativeAltitude: NSNumber! { get } ``` |
| To | ``` var relativeAltitude: NSNumber { get } ``` |

Modified [CMAttitude](https://developer.apple.com/documentation/coremotion/cmattitude)

|  | Declaration |
| --- | --- |
| From | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding, NSCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiplyByInverseOfAttitude(_ attitude: CMAttitude!) } ``` |
| To | ``` class CMAttitude : NSObject, NSCopying, NSSecureCoding, NSCoding {     var roll: Double { get }     var pitch: Double { get }     var yaw: Double { get }     var rotationMatrix: CMRotationMatrix { get }     var quaternion: CMQuaternion { get }     func multiplyByInverseOfAttitude(_ attitude: CMAttitude) } ``` |

Modified [CMAttitude.multiplyByInverseOfAttitude(_: CMAttitude)](https://developer.apple.com/documentation/coremotion/cmattitude/1615909-multiply)

|  | Declaration |
| --- | --- |
| From | ``` func multiplyByInverseOfAttitude(_ attitude: CMAttitude!) ``` |
| To | ``` func multiplyByInverseOfAttitude(_ attitude: CMAttitude) ``` |

Modified [CMAttitudeReferenceFrame [struct]](https://developer.apple.com/documentation/coremotion/cmattitudereferenceframe)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMAttitudeReferenceFrame : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var XArbitraryZVertical: CMAttitudeReferenceFrame { get }     static var XArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }     static var XMagneticNorthZVertical: CMAttitudeReferenceFrame { get }     static var XTrueNorthZVertical: CMAttitudeReferenceFrame { get } } ``` | RawOptionSetType |
| To | ``` struct CMAttitudeReferenceFrame : OptionSetType {     init(rawValue rawValue: UInt)     static var XArbitraryZVertical: CMAttitudeReferenceFrame { get }     static var XArbitraryCorrectedZVertical: CMAttitudeReferenceFrame { get }     static var XMagneticNorthZVertical: CMAttitudeReferenceFrame { get }     static var XTrueNorthZVertical: CMAttitudeReferenceFrame { get } } ``` | OptionSetType |

Modified [CMDeviceMotion](https://developer.apple.com/documentation/coremotion/cmdevicemotion)

|  | Declaration |
| --- | --- |
| From | ``` class CMDeviceMotion : CMLogItem {     var attitude: CMAttitude! { get }     var rotationRate: CMRotationRate { get }     var gravity: CMAcceleration { get }     var userAcceleration: CMAcceleration { get }     var magneticField: CMCalibratedMagneticField { get } } ``` |
| To | ``` class CMDeviceMotion : CMLogItem {     var attitude: CMAttitude { get }     var rotationRate: CMRotationRate { get }     var gravity: CMAcceleration { get }     var userAcceleration: CMAcceleration { get }     var magneticField: CMCalibratedMagneticField { get } } ``` |

Modified [CMDeviceMotion.attitude](https://developer.apple.com/documentation/coremotion/cmdevicemotion/1616050-attitude)

|  | Declaration |
| --- | --- |
| From | ``` var attitude: CMAttitude! { get } ``` |
| To | ``` var attitude: CMAttitude { get } ``` |

Modified [CMError [struct]](https://developer.apple.com/documentation/coremotion/cmerror)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMError {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct CMError : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [CMMagneticFieldCalibrationAccuracy [struct]](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CMMagneticFieldCalibrationAccuracy {     init(_ value: Int32)     var value: Int32 } ``` | -- |
| To | ``` struct CMMagneticFieldCalibrationAccuracy : RawRepresentable {     init(_ rawValue: Int32)     init(rawValue rawValue: Int32)     var rawValue: Int32 } ``` | RawRepresentable |

Modified [CMMotionActivity](https://developer.apple.com/documentation/coremotion/cmmotionactivity)

|  | Declaration |
| --- | --- |
| From | ``` class CMMotionActivity : CMLogItem {     var confidence: CMMotionActivityConfidence { get }     var startDate: NSDate! { get }     var unknown: Bool { get }     var stationary: Bool { get }     var walking: Bool { get }     var running: Bool { get }     var automotive: Bool { get }     var cycling: Bool { get } } ``` |
| To | ``` class CMMotionActivity : CMLogItem {     var confidence: CMMotionActivityConfidence { get }     var startDate: NSDate { get }     var unknown: Bool { get }     var stationary: Bool { get }     var walking: Bool { get }     var running: Bool { get }     var automotive: Bool { get }     var cycling: Bool { get } } ``` |

Modified [CMMotionActivity.startDate](https://developer.apple.com/documentation/coremotion/cmmotionactivity/1615453-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate { get } ``` |

Modified [CMMotionActivityConfidence [enum]](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [CMMotionActivityManager](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager)

|  | Declaration |
| --- | --- |
| From | ``` class CMMotionActivityManager : NSObject {     class func isActivityAvailable() -> Bool     func queryActivityStartingFromDate(_ start: NSDate!, toDate end: NSDate!, toQueue queue: NSOperationQueue!, withHandler handler: CMMotionActivityQueryHandler!)     func startActivityUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMMotionActivityHandler!)     func stopActivityUpdates() } ``` |
| To | ``` class CMMotionActivityManager : NSObject {     class func isActivityAvailable() -> Bool     func queryActivityStartingFromDate(_ start: NSDate, toDate end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMMotionActivityQueryHandler)     func startActivityUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMotionActivityHandler)     func stopActivityUpdates() } ``` |

Modified [CMMotionActivityManager.queryActivityStartingFromDate(_: NSDate, toDate: NSDate, toQueue: NSOperationQueue, withHandler: CMMotionActivityQueryHandler)](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615929-queryactivitystartingfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func queryActivityStartingFromDate(_ start: NSDate!, toDate end: NSDate!, toQueue queue: NSOperationQueue!, withHandler handler: CMMotionActivityQueryHandler!) ``` |
| To | ``` func queryActivityStartingFromDate(_ start: NSDate, toDate end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMMotionActivityQueryHandler) ``` |

Modified [CMMotionActivityManager.startActivityUpdatesToQueue(_: NSOperationQueue, withHandler: CMMotionActivityHandler)](https://developer.apple.com/documentation/coremotion/cmmotionactivitymanager/1615945-startactivityupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startActivityUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMMotionActivityHandler!) ``` |
| To | ``` func startActivityUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMotionActivityHandler) ``` |

Modified [CMMotionManager](https://developer.apple.com/documentation/coremotion/cmmotionmanager)

|  | Declaration |
| --- | --- |
| From | ``` class CMMotionManager : NSObject {     var accelerometerUpdateInterval: NSTimeInterval     var accelerometerAvailable: Bool { get }     var accelerometerActive: Bool { get }     var accelerometerData: CMAccelerometerData! { get }     func startAccelerometerUpdates()     func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMAccelerometerHandler!)     func stopAccelerometerUpdates()     var gyroUpdateInterval: NSTimeInterval     var gyroAvailable: Bool { get }     var gyroActive: Bool { get }     var gyroData: CMGyroData! { get }     func startGyroUpdates()     func startGyroUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMGyroHandler!)     func stopGyroUpdates()     var magnetometerUpdateInterval: NSTimeInterval     var magnetometerAvailable: Bool { get }     var magnetometerActive: Bool { get }     var magnetometerData: CMMagnetometerData! { get }     func startMagnetometerUpdates()     func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMMagnetometerHandler!)     func stopMagnetometerUpdates()     var deviceMotionUpdateInterval: NSTimeInterval     class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame     var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }     var deviceMotionAvailable: Bool { get }     var deviceMotionActive: Bool { get }     var deviceMotion: CMDeviceMotion! { get }     func startDeviceMotionUpdates()     func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMDeviceMotionHandler!)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue!, withHandler handler: CMDeviceMotionHandler!)     func stopDeviceMotionUpdates()     var showsDeviceMovementDisplay: Bool } ``` |
| To | ``` class CMMotionManager : NSObject {     var accelerometerUpdateInterval: NSTimeInterval     var accelerometerAvailable: Bool { get }     var accelerometerActive: Bool { get }     var accelerometerData: CMAccelerometerData? { get }     func startAccelerometerUpdates()     func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAccelerometerHandler)     func stopAccelerometerUpdates()     var gyroUpdateInterval: NSTimeInterval     var gyroAvailable: Bool { get }     var gyroActive: Bool { get }     var gyroData: CMGyroData? { get }     func startGyroUpdates()     func startGyroUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMGyroHandler)     func stopGyroUpdates()     var magnetometerUpdateInterval: NSTimeInterval     var magnetometerAvailable: Bool { get }     var magnetometerActive: Bool { get }     var magnetometerData: CMMagnetometerData? { get }     func startMagnetometerUpdates()     func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMagnetometerHandler)     func stopMagnetometerUpdates()     var deviceMotionUpdateInterval: NSTimeInterval     class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame     var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }     var deviceMotionAvailable: Bool { get }     var deviceMotionActive: Bool { get }     var deviceMotion: CMDeviceMotion? { get }     func startDeviceMotionUpdates()     func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame)     func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler)     func stopDeviceMotionUpdates()     var showsDeviceMovementDisplay: Bool } ``` |

Modified [CMMotionManager.accelerometerData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615992-accelerometerdata)

|  | Declaration |
| --- | --- |
| From | ``` var accelerometerData: CMAccelerometerData! { get } ``` |
| To | ``` var accelerometerData: CMAccelerometerData? { get } ``` |

Modified [CMMotionManager.deviceMotion](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616040-devicemotion)

|  | Declaration |
| --- | --- |
| From | ``` var deviceMotion: CMDeviceMotion! { get } ``` |
| To | ``` var deviceMotion: CMDeviceMotion? { get } ``` |

Modified [CMMotionManager.gyroData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616154-gyrodata)

|  | Declaration |
| --- | --- |
| From | ``` var gyroData: CMGyroData! { get } ``` |
| To | ``` var gyroData: CMGyroData? { get } ``` |

Modified [CMMotionManager.magnetometerData](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616032-magnetometerdata)

|  | Declaration |
| --- | --- |
| From | ``` var magnetometerData: CMMagnetometerData! { get } ``` |
| To | ``` var magnetometerData: CMMagnetometerData? { get } ``` |

Modified [CMMotionManager.startAccelerometerUpdatesToQueue(_: NSOperationQueue, withHandler: CMAccelerometerHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616148-startaccelerometerupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMAccelerometerHandler!) ``` |
| To | ``` func startAccelerometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMAccelerometerHandler) ``` |

Modified [CMMotionManager.startDeviceMotionUpdatesToQueue(_: NSOperationQueue, withHandler: CMDeviceMotionHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616048-startdevicemotionupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMDeviceMotionHandler!) ``` |
| To | ``` func startDeviceMotionUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler) ``` |

Modified [CMMotionManager.startDeviceMotionUpdatesUsingReferenceFrame(_: CMAttitudeReferenceFrame, toQueue: NSOperationQueue, withHandler: CMDeviceMotionHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616176-startdevicemotionupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue!, withHandler handler: CMDeviceMotionHandler!) ``` |
| To | ``` func startDeviceMotionUpdatesUsingReferenceFrame(_ referenceFrame: CMAttitudeReferenceFrame, toQueue queue: NSOperationQueue, withHandler handler: CMDeviceMotionHandler) ``` |

Modified [CMMotionManager.startGyroUpdatesToQueue(_: NSOperationQueue, withHandler: CMGyroHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1616104-startgyroupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startGyroUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMGyroHandler!) ``` |
| To | ``` func startGyroUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMGyroHandler) ``` |

Modified [CMMotionManager.startMagnetometerUpdatesToQueue(_: NSOperationQueue, withHandler: CMMagnetometerHandler)](https://developer.apple.com/documentation/coremotion/cmmotionmanager/1615968-startmagnetometerupdates)

|  | Declaration |
| --- | --- |
| From | ``` func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue!, withHandler handler: CMMagnetometerHandler!) ``` |
| To | ``` func startMagnetometerUpdatesToQueue(_ queue: NSOperationQueue, withHandler handler: CMMagnetometerHandler) ``` |

Modified [CMPedometer](https://developer.apple.com/documentation/coremotion/cmpedometer)

|  | Declaration |
| --- | --- |
| From | ``` class CMPedometer : NSObject {     class func isStepCountingAvailable() -> Bool     class func isDistanceAvailable() -> Bool     class func isFloorCountingAvailable() -> Bool     func queryPedometerDataFromDate(_ start: NSDate!, toDate end: NSDate!, withHandler handler: CMPedometerHandler!)     func startPedometerUpdatesFromDate(_ start: NSDate!, withHandler handler: CMPedometerHandler!)     func stopPedometerUpdates() } ``` |
| To | ``` class CMPedometer : NSObject {     class func isStepCountingAvailable() -> Bool     class func isDistanceAvailable() -> Bool     class func isFloorCountingAvailable() -> Bool     class func isPaceAvailable() -> Bool     class func isCadenceAvailable() -> Bool     func queryPedometerDataFromDate(_ start: NSDate, toDate end: NSDate, withHandler handler: CMPedometerHandler)     func startPedometerUpdatesFromDate(_ start: NSDate, withHandler handler: CMPedometerHandler)     func stopPedometerUpdates() } ``` |

Modified [CMPedometer.queryPedometerDataFromDate(_: NSDate, toDate: NSDate, withHandler: CMPedometerHandler)](https://developer.apple.com/documentation/coremotion/cmpedometer/1613946-querypedometerdata)

|  | Declaration |
| --- | --- |
| From | ``` func queryPedometerDataFromDate(_ start: NSDate!, toDate end: NSDate!, withHandler handler: CMPedometerHandler!) ``` |
| To | ``` func queryPedometerDataFromDate(_ start: NSDate, toDate end: NSDate, withHandler handler: CMPedometerHandler) ``` |

Modified [CMPedometer.startPedometerUpdatesFromDate(_: NSDate, withHandler: CMPedometerHandler)](https://developer.apple.com/documentation/coremotion/cmpedometer/1613950-startpedometerupdatesfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func startPedometerUpdatesFromDate(_ start: NSDate!, withHandler handler: CMPedometerHandler!) ``` |
| To | ``` func startPedometerUpdatesFromDate(_ start: NSDate, withHandler handler: CMPedometerHandler) ``` |

Modified [CMPedometerData](https://developer.apple.com/documentation/coremotion/cmpedometerdata)

|  | Declaration |
| --- | --- |
| From | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCoding, NSCopying {     var startDate: NSDate! { get }     var endDate: NSDate! { get }     var numberOfSteps: NSNumber! { get }     var distance: NSNumber! { get }     var floorsAscended: NSNumber! { get }     var floorsDescended: NSNumber! { get } } ``` |
| To | ``` class CMPedometerData : NSObject, NSSecureCoding, NSCoding, NSCopying {     var startDate: NSDate { get }     var endDate: NSDate { get }     var numberOfSteps: NSNumber { get }     var distance: NSNumber? { get }     var floorsAscended: NSNumber? { get }     var floorsDescended: NSNumber? { get }     var currentPace: NSNumber? { get }     var currentCadence: NSNumber? { get } } ``` |

Modified [CMPedometerData.distance](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613944-distance)

|  | Declaration |
| --- | --- |
| From | ``` var distance: NSNumber! { get } ``` |
| To | ``` var distance: NSNumber? { get } ``` |

Modified [CMPedometerData.endDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613952-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate { get } ``` |

Modified [CMPedometerData.floorsAscended](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613961-floorsascended)

|  | Declaration |
| --- | --- |
| From | ``` var floorsAscended: NSNumber! { get } ``` |
| To | ``` var floorsAscended: NSNumber? { get } ``` |

Modified [CMPedometerData.floorsDescended](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613940-floorsdescended)

|  | Declaration |
| --- | --- |
| From | ``` var floorsDescended: NSNumber! { get } ``` |
| To | ``` var floorsDescended: NSNumber? { get } ``` |

Modified [CMPedometerData.numberOfSteps](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613965-numberofsteps)

|  | Declaration |
| --- | --- |
| From | ``` var numberOfSteps: NSNumber! { get } ``` |
| To | ``` var numberOfSteps: NSNumber { get } ``` |

Modified [CMPedometerData.startDate](https://developer.apple.com/documentation/coremotion/cmpedometerdata/1613942-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate { get } ``` |

Modified [CMStepCounter](https://developer.apple.com/documentation/coremotion/cmstepcounter)

|  | Declaration |
| --- | --- |
| From | ``` class CMStepCounter : NSObject {     class func isStepCountingAvailable() -> Bool     func queryStepCountStartingFrom(_ start: NSDate!, to end: NSDate!, toQueue queue: NSOperationQueue!, withHandler handler: CMStepQueryHandler!)     func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue!, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler!)     func stopStepCountingUpdates() } ``` |
| To | ``` class CMStepCounter : NSObject {     class func isStepCountingAvailable() -> Bool     func queryStepCountStartingFrom(_ start: NSDate, to end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMStepQueryHandler)     func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler)     func stopStepCountingUpdates() } ``` |

Modified [CMStepCounter.queryStepCountStartingFrom(_: NSDate, to: NSDate, toQueue: NSOperationQueue, withHandler: CMStepQueryHandler)](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616166-querystepcountstartingfrom)

|  | Declaration |
| --- | --- |
| From | ``` func queryStepCountStartingFrom(_ start: NSDate!, to end: NSDate!, toQueue queue: NSOperationQueue!, withHandler handler: CMStepQueryHandler!) ``` |
| To | ``` func queryStepCountStartingFrom(_ start: NSDate, to end: NSDate, toQueue queue: NSOperationQueue, withHandler handler: CMStepQueryHandler) ``` |

Modified [CMStepCounter.startStepCountingUpdatesToQueue(_: NSOperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](https://developer.apple.com/documentation/coremotion/cmstepcounter/1616151-startstepcountingupdatestoqueue)

|  | Declaration |
| --- | --- |
| From | ``` func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue!, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler!) ``` |
| To | ``` func startStepCountingUpdatesToQueue(_ queue: NSOperationQueue, updateOn stepCounts: Int, withHandler handler: CMStepUpdateHandler) ``` |

Modified [CMAccelerometerHandler](https://developer.apple.com/documentation/coremotion/cmaccelerometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAccelerometerHandler = (CMAccelerometerData!, NSError!) -> Void ``` |
| To | ``` typealias CMAccelerometerHandler = (CMAccelerometerData?, NSError?) -> Void ``` |

Modified [CMAltitudeHandler](https://developer.apple.com/documentation/coremotion/cmaltitudehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMAltitudeHandler = (CMAltitudeData!, NSError!) -> Void ``` |
| To | ``` typealias CMAltitudeHandler = (CMAltitudeData?, NSError?) -> Void ``` |

Modified [CMDeviceMotionHandler](https://developer.apple.com/documentation/coremotion/cmdevicemotionhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMDeviceMotionHandler = (CMDeviceMotion!, NSError!) -> Void ``` |
| To | ``` typealias CMDeviceMotionHandler = (CMDeviceMotion?, NSError?) -> Void ``` |

Modified [CMGyroHandler](https://developer.apple.com/documentation/coremotion/cmgyrohandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMGyroHandler = (CMGyroData!, NSError!) -> Void ``` |
| To | ``` typealias CMGyroHandler = (CMGyroData?, NSError?) -> Void ``` |

Modified [CMMagnetometerHandler](https://developer.apple.com/documentation/coremotion/cmmagnetometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMagnetometerHandler = (CMMagnetometerData!, NSError!) -> Void ``` |
| To | ``` typealias CMMagnetometerHandler = (CMMagnetometerData?, NSError?) -> Void ``` |

Modified [CMMotionActivityHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMotionActivityHandler = (CMMotionActivity!) -> Void ``` |
| To | ``` typealias CMMotionActivityHandler = (CMMotionActivity?) -> Void ``` |

Modified [CMMotionActivityQueryHandler](https://developer.apple.com/documentation/coremotion/cmmotionactivityqueryhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMMotionActivityQueryHandler = ([AnyObject]!, NSError!) -> Void ``` |
| To | ``` typealias CMMotionActivityQueryHandler = ([CMMotionActivity]?, NSError?) -> Void ``` |

Modified [CMPedometerHandler](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMPedometerHandler = (CMPedometerData!, NSError!) -> Void ``` |
| To | ``` typealias CMPedometerHandler = (CMPedometerData?, NSError?) -> Void ``` |

Modified [CMStepQueryHandler](https://developer.apple.com/documentation/coremotion/cmstepqueryhandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMStepQueryHandler = (Int, NSError!) -> Void ``` |
| To | ``` typealias CMStepQueryHandler = (Int, NSError?) -> Void ``` |

Modified [CMStepUpdateHandler](https://developer.apple.com/documentation/coremotion/cmstepupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` typealias CMStepUpdateHandler = (Int, NSDate!, NSError!) -> Void ``` |
| To | ``` typealias CMStepUpdateHandler = (Int, NSDate, NSError?) -> Void ``` |

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

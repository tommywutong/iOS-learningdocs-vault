---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/HealthKit.html
archived_at: '2026-07-18T02:56:51.508984Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# HealthKit Changes for Swift

### HealthKit

Removed HKQueryOptions.init(_: UInt)Removed HKStatisticsOptions.init(_: UInt)Added [HKAnchoredObjectQuery.init(type: HKSampleType, predicate: NSPredicate?, anchor: HKQueryAnchor?, limit: Int, resultsHandler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615071-initwithtype)Added [HKAnchoredObjectQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615691-updatehandler)Added [HKCategorySample.init(type: HKCategoryType, value: Int, startDate: NSDate, endDate: NSDate, device: HKDevice?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615287-categorysamplewithtype)Added [HKCategoryValue [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalue)Added [HKCategoryValue.NotApplicable](https://developer.apple.com/documentation/healthkit/hkcategoryvalue/hkcategoryvaluenotapplicable)Added [HKCategoryValueAppleStandHour [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour)Added [HKCategoryValueAppleStandHour.Idle](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/idle)Added [HKCategoryValueAppleStandHour.Stood](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/hkcategoryvalueapplestandhourstood)Added [HKCategoryValueCervicalMucusQuality [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality)Added [HKCategoryValueCervicalMucusQuality.Creamy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/creamy)Added [HKCategoryValueCervicalMucusQuality.Dry](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/dry)Added [HKCategoryValueCervicalMucusQuality.EggWhite](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualityeggwhite)Added [HKCategoryValueCervicalMucusQuality.Sticky](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualitysticky)Added [HKCategoryValueCervicalMucusQuality.Watery](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/watery)Added [HKCategoryValueMenstrualFlow [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow)Added [HKCategoryValueMenstrualFlow.Heavy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/heavy)Added [HKCategoryValueMenstrualFlow.Light](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/hkcategoryvaluemenstrualflowlight)Added [HKCategoryValueMenstrualFlow.Medium](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/hkcategoryvaluemenstrualflowmedium)Added [HKCategoryValueMenstrualFlow.Unspecified](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/unspecified)Added [HKCategoryValueOvulationTestResult [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult)Added [HKCategoryValueOvulationTestResult.Indeterminate](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/hkcategoryvalueovulationtestresultindeterminate)Added [HKCategoryValueOvulationTestResult.Negative](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/negative)Added [HKCategoryValueOvulationTestResult.Positive](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/hkcategoryvalueovulationtestresultpositive)Added [HKCorrelation.init(type: HKCorrelationType, startDate: NSDate, endDate: NSDate, objects: Set<HKSample>, device: HKDevice?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614363-correlationwithtype)Added [HKDeletedObject](https://developer.apple.com/documentation/healthkit/hkdeletedobject)Added [HKDeletedObject.UUID](https://developer.apple.com/documentation/healthkit/hkdeletedobject/1615423-uuid)Added [HKDevice](https://developer.apple.com/documentation/healthkit/hkdevice)Added [HKDevice.firmwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615749-firmwareversion)Added [HKDevice.hardwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615540-hardwareversion)Added [HKDevice.init(name: String?, manufacturer: String?, model: String?, hardwareVersion: String?, firmwareVersion: String?, softwareVersion: String?, localIdentifier: String?, UDIDeviceIdentifier: String?)](https://developer.apple.com/documentation/healthkit/hkdevice/1615582-initwithname)Added [HKDevice.localDevice() -> HKDevice [class]](https://developer.apple.com/documentation/healthkit/hkdevice/1615276-local)Added [HKDevice.localIdentifier](https://developer.apple.com/documentation/healthkit/hkdevice/1615785-localidentifier)Added [HKDevice.manufacturer](https://developer.apple.com/documentation/healthkit/hkdevice/1615305-manufacturer)Added [HKDevice.model](https://developer.apple.com/documentation/healthkit/hkdevice/1615761-model)Added [HKDevice.name](https://developer.apple.com/documentation/healthkit/hkdevice/1615731-name)Added [HKDevice.softwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615262-softwareversion)Added [HKDevice.UDIDeviceIdentifier](https://developer.apple.com/documentation/healthkit/hkdevice/1615296-udideviceidentifier)Added [HKErrorCode.ErrorAnotherWorkoutSessionStarted](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerroranotherworkoutsessionstarted)Added [HKErrorCode.ErrorUserExitedWorkoutSession](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerroruserexitedworkoutsession)Added [HKFitzpatrickSkinType [enum]](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype)Added [HKFitzpatrickSkinType.I](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypei)Added [HKFitzpatrickSkinType.II](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/ii)Added [HKFitzpatrickSkinType.III](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/iii)Added [HKFitzpatrickSkinType.IV](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypeiv)Added [HKFitzpatrickSkinType.NotSet](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypenotset)Added [HKFitzpatrickSkinType.V](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypev)Added [HKFitzpatrickSkinType.VI](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/vi)Added [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)Added [HKFitzpatrickSkinTypeObject.skinType](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject/1614174-skintype)Added [HKHealthStore.deleteObjects(_: [HKObject], withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614163-delete)Added [HKHealthStore.deleteObjectsOfType(_: HKObjectType, predicate: NSPredicate, withCompletion: (Bool, Int, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614162-deleteobjects)Added [HKHealthStore.earliestPermittedSampleDate() -> NSDate](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614166-earliestpermittedsampledate)Added [HKHealthStore.fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614161-fitzpatrickskintypewitherror)Added [HKHealthStore.handleAuthorizationForExtensionWithCompletion(_: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614153-handleauthorizationforextension)Added [HKHealthStore.splitTotalEnergy(_: HKQuantity, startDate: NSDate, endDate: NSDate, resultsHandler: (HKQuantity?, HKQuantity?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614170-splittotalenergy)Added [HKObject.device](https://developer.apple.com/documentation/healthkit/hkobject/1615622-device)Added [HKObject.sourceRevision](https://developer.apple.com/documentation/healthkit/hkobject/1615483-sourcerevision)Added [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, startDate: NSDate, endDate: NSDate, device: HKDevice?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615019-quantitysamplewithtype)Added [HKQuery.predicateForObjectsFromDevices(_: Set<HKDevice>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614765-predicateforobjects)Added [HKQuery.predicateForObjectsFromSourceRevisions(_: Set<HKSourceRevision>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614791-predicateforobjects)Added [HKQuery.predicateForObjectsWithDeviceProperty(_: String, allowedValues: Set<String>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614775-predicateforobjects)Added [HKQueryAnchor](https://developer.apple.com/documentation/healthkit/hkqueryanchor)Added [HKQueryAnchor.init(fromValue: Int)](https://developer.apple.com/documentation/healthkit/hkqueryanchor/1615355-init)Added [HKSourceRevision](https://developer.apple.com/documentation/healthkit/hksourcerevision)Added [HKSourceRevision.init(source: HKSource, version: String)](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614799-init)Added [HKSourceRevision.source](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614797-source)Added [HKSourceRevision.version](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614798-version)Added [HKUnit.cupImperialUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615506-cupimperialunit)Added [HKUnit.cupUSUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615542-cupus)Added [HKUnit.yardUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615106-yardunit)Added [HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate, endDate: NSDate, duration: NSTimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615048-init)Added [HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate, endDate: NSDate, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615713-workoutwithactivitytype)Added [HKCategoryTypeIdentifierAppleStandHour](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615539-applestandhour)Added [HKCategoryTypeIdentifierCervicalMucusQuality](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifiercervicalmucusquality)Added [HKCategoryTypeIdentifierIntermenstrualBleeding](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifierintermenstrualbleeding)Added [HKCategoryTypeIdentifierMenstrualFlow](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615136-menstrualflow)Added [HKCategoryTypeIdentifierOvulationTestResult](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615252-ovulationtestresult)Added [HKCategoryTypeIdentifierSexualActivity](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615769-sexualactivity)Added [HKCharacteristicTypeIdentifierFitzpatrickSkinType](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifierfitzpatrickskintype)Added [HKDevicePropertyKeyFirmwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyfirmwareversion)Added [HKDevicePropertyKeyHardwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyhardwareversion)Added [HKDevicePropertyKeyLocalIdentifier](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeylocalidentifier)Added [HKDevicePropertyKeyManufacturer](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeymanufacturer)Added [HKDevicePropertyKeyModel](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeymodel)Added [HKDevicePropertyKeyName](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyname)Added [HKDevicePropertyKeySoftwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeysoftwareversion)Added [HKDevicePropertyKeyUDIDeviceIdentifier](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyudideviceidentifier)Added [HKMetadataKeyMenstrualCycleStart](https://developer.apple.com/documentation/healthkit/hkmetadatakeymenstrualcyclestart)Added [HKMetadataKeySexualActivityProtectionUsed](https://developer.apple.com/documentation/healthkit/hkmetadatakeysexualactivityprotectionused)Added [HKPredicateKeyPathDevice](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathdevice)Added [HKPredicateKeyPathSourceRevision](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathsourcerevision)Added [HKQuantityTypeIdentifierBasalBodyTemperature](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbasalbodytemperature)Added [HKQuantityTypeIdentifierDietaryWater](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierdietarywater)Added [HKQuantityTypeIdentifierUVExposure](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifieruvexposure)Modified [HKAnchoredObjectQuery](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKAnchoredObjectQuery : HKQuery {     init!(type type: HKSampleType!, predicate predicate: NSPredicate!, anchor anchor: Int, limit limit: Int, completionHandler handler: ((HKAnchoredObjectQuery!, [AnyObject]!, Int, NSError!) -> Void)!) } ``` |
| To | ``` class HKAnchoredObjectQuery : HKQuery {     var updateHandler: ((HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void)?     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: (HKAnchoredObjectQuery, [HKSample]?, Int, NSError?) -> Void)     init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: HKQueryAnchor?, limit limit: Int, resultsHandler handler: (HKAnchoredObjectQuery, [HKSample]?, [HKDeletedObject]?, HKQueryAnchor?, NSError?) -> Void) } ``` |

Modified [HKAnchoredObjectQuery.init(type: HKSampleType, predicate: NSPredicate?, anchor: Int, limit: Int, completionHandler: (HKAnchoredObjectQuery, [HKSample]?, Int, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615388-initwithtype)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` init!(type type: HKSampleType!, predicate predicate: NSPredicate!, anchor anchor: Int, limit limit: Int, completionHandler handler: ((HKAnchoredObjectQuery!, [AnyObject]!, Int, NSError!) -> Void)!) ``` | -- |
| To | ``` init(type type: HKSampleType, predicate predicate: NSPredicate?, anchor anchor: Int, limit limit: Int, completionHandler handler: (HKAnchoredObjectQuery, [HKSample]?, Int, NSError?) -> Void) ``` | iOS 9.0 |

Modified [HKAuthorizationStatus [enum]](https://developer.apple.com/documentation/healthkit/hkauthorizationstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKBiologicalSex [enum]](https://developer.apple.com/documentation/healthkit/hkbiologicalsex)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBiologicalSexObject : NSObject {     var biologicalSex: HKBiologicalSex { get } } ``` | AnyObject |
| To | ``` class HKBiologicalSexObject : NSObject, NSCopying, NSSecureCoding, NSCoding {     var biologicalSex: HKBiologicalSex { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |

Modified [HKBloodType [enum]](https://developer.apple.com/documentation/healthkit/hkbloodtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKBloodTypeObject : NSObject {     var bloodType: HKBloodType { get } } ``` | AnyObject |
| To | ``` class HKBloodTypeObject : NSObject, NSCopying, NSSecureCoding, NSCoding {     var bloodType: HKBloodType { get } } ``` | AnyObject, NSCoding, NSCopying, NSSecureCoding |

Modified [HKBodyTemperatureSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkbodytemperaturesensorlocation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKCategorySample](https://developer.apple.com/documentation/healthkit/hkcategorysample)

|  | Declaration |
| --- | --- |
| From | ``` class HKCategorySample : HKSample {     var categoryType: HKCategoryType! { get }     var value: Int { get }     init!()     convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!)     class func categorySampleWithType(_ type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) -> Self!     convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!)     class func categorySampleWithType(_ type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!) -> Self! } ``` |
| To | ``` class HKCategorySample : HKSample {     var categoryType: HKCategoryType { get }     var value: Int { get }     init()     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func categorySampleWithType(_ type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |

Modified [HKCategorySample.categoryType](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615560-categorytype)

|  | Declaration |
| --- | --- |
| From | ``` var categoryType: HKCategoryType! { get } ``` |
| To | ``` var categoryType: HKCategoryType { get } ``` |

Modified [HKCategorySample.init(type: HKCategoryType, value: Int, startDate: NSDate, endDate: NSDate)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615063-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate) ``` |

Modified [HKCategorySample.init(type: HKCategoryType, value: Int, startDate: NSDate, endDate: NSDate, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615596-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type type: HKCategoryType!, value value: Int, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(type type: HKCategoryType, value value: Int, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) ``` |

Modified [HKCategoryValueSleepAnalysis [enum]](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKCorrelation](https://developer.apple.com/documentation/healthkit/hkcorrelation)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class HKCorrelation : HKSample, NSSecureCoding, NSCoding {     var correlationType: HKCorrelationType! { get }     var objects: Set<NSObject>! { get }     convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!)     class func correlationWithType(_ correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!) -> Self!     convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!, metadata metadata: [NSObject : AnyObject]!)     class func correlationWithType(_ correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!, metadata metadata: [NSObject : AnyObject]!) -> Self!     func objectsForType(_ objectType: HKObjectType!) -> Set<NSObject>! } ``` | AnyObject, NSCoding, NSSecureCoding |
| To | ``` class HKCorrelation : HKSample {     var correlationType: HKCorrelationType { get }     var objects: Set<HKSample> { get }     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>) -> Self     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func correlationWithType(_ correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self     func objectsForType(_ objectType: HKObjectType) -> Set<HKSample> } ``` | AnyObject |

Modified [HKCorrelation.correlationType](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614365-correlationtype)

|  | Declaration |
| --- | --- |
| From | ``` var correlationType: HKCorrelationType! { get } ``` |
| To | ``` var correlationType: HKCorrelationType { get } ``` |

Modified [HKCorrelation.init(type: HKCorrelationType, startDate: NSDate, endDate: NSDate, objects: Set<HKSample>)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614359-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!) ``` |
| To | ``` convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>) ``` |

Modified [HKCorrelation.init(type: HKCorrelationType, startDate: NSDate, endDate: NSDate, objects: Set<HKSample>, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614362-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type correlationType: HKCorrelationType!, startDate startDate: NSDate!, endDate endDate: NSDate!, objects objects: Set<NSObject>!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(type correlationType: HKCorrelationType, startDate startDate: NSDate, endDate endDate: NSDate, objects objects: Set<HKSample>, metadata metadata: [String : AnyObject]?) ``` |

Modified [HKCorrelation.objects](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614364-objects)

|  | Declaration |
| --- | --- |
| From | ``` var objects: Set<NSObject>! { get } ``` |
| To | ``` var objects: Set<HKSample> { get } ``` |

Modified [HKCorrelation.objectsForType(_: HKObjectType) -> Set<HKSample>](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614360-objects)

|  | Declaration |
| --- | --- |
| From | ``` func objectsForType(_ objectType: HKObjectType!) -> Set<NSObject>! ``` |
| To | ``` func objectsForType(_ objectType: HKObjectType) -> Set<HKSample> ``` |

Modified [HKCorrelationQuery](https://developer.apple.com/documentation/healthkit/hkcorrelationquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKCorrelationQuery : HKQuery {     @NSCopying var correlationType: HKCorrelationType! { get }     var samplePredicates: [NSObject : AnyObject]! { get }     init!(type correlationType: HKCorrelationType!, predicate predicate: NSPredicate!, samplePredicates samplePredicates: [NSObject : AnyObject]!, completion completion: ((HKCorrelationQuery!, [AnyObject]!, NSError!) -> Void)!) } ``` |
| To | ``` class HKCorrelationQuery : HKQuery {     @NSCopying var correlationType: HKCorrelationType { get }     var samplePredicates: [HKSampleType : NSPredicate]? { get }     init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: (HKCorrelationQuery, [HKCorrelation]?, NSError?) -> Void) } ``` |

Modified [HKCorrelationQuery.correlationType](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614146-correlationtype)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var correlationType: HKCorrelationType! { get } ``` |
| To | ``` @NSCopying var correlationType: HKCorrelationType { get } ``` |

Modified [HKCorrelationQuery.init(type: HKCorrelationType, predicate: NSPredicate?, samplePredicates: [HKSampleType : NSPredicate]?, completion: (HKCorrelationQuery, [HKCorrelation]?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614145-initwithtype)

|  | Declaration |
| --- | --- |
| From | ``` init!(type correlationType: HKCorrelationType!, predicate predicate: NSPredicate!, samplePredicates samplePredicates: [NSObject : AnyObject]!, completion completion: ((HKCorrelationQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` init(type correlationType: HKCorrelationType, predicate predicate: NSPredicate?, samplePredicates samplePredicates: [HKSampleType : NSPredicate]?, completion completion: (HKCorrelationQuery, [HKCorrelation]?, NSError?) -> Void) ``` |

Modified [HKCorrelationQuery.samplePredicates](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614147-samplepredicates)

|  | Declaration |
| --- | --- |
| From | ``` var samplePredicates: [NSObject : AnyObject]! { get } ``` |
| To | ``` var samplePredicates: [HKSampleType : NSPredicate]? { get } ``` |

Modified [HKErrorCode [enum]](https://developer.apple.com/documentation/healthkit/hkerrorcode)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum HKErrorCode : Int {     case NoError     case ErrorHealthDataUnavailable     case ErrorHealthDataRestricted     case ErrorInvalidArgument     case ErrorAuthorizationDenied     case ErrorAuthorizationNotDetermined     case ErrorDatabaseInaccessible     case ErrorUserCanceled } ``` | -- |
| To | ``` enum HKErrorCode : Int {     case NoError     case ErrorHealthDataUnavailable     case ErrorHealthDataRestricted     case ErrorInvalidArgument     case ErrorAuthorizationDenied     case ErrorAuthorizationNotDetermined     case ErrorDatabaseInaccessible     case ErrorUserCanceled     case ErrorAnotherWorkoutSessionStarted     case ErrorUserExitedWorkoutSession } ``` | Int |

Modified [HKHealthStore](https://developer.apple.com/documentation/healthkit/hkhealthstore)

|  | Declaration |
| --- | --- |
| From | ``` class HKHealthStore : NSObject {     class func isHealthDataAvailable() -> Bool     func authorizationStatusForType(_ type: HKObjectType!) -> HKAuthorizationStatus     func requestAuthorizationToShareTypes(_ typesToShare: Set<NSObject>!, readTypes typesToRead: Set<NSObject>!, completion completion: ((Bool, NSError!) -> Void)!)     func saveObject(_ object: HKObject!, withCompletion completion: ((Bool, NSError!) -> Void)!)     func saveObjects(_ objects: [AnyObject]!, withCompletion completion: ((Bool, NSError!) -> Void)!)     func deleteObject(_ object: HKObject!, withCompletion completion: ((Bool, NSError!) -> Void)!)     func executeQuery(_ query: HKQuery!)     func stopQuery(_ query: HKQuery!)     func dateOfBirthWithError(_ error: NSErrorPointer) -> NSDate?     func biologicalSexWithError(_ error: NSErrorPointer) -> HKBiologicalSexObject?     func bloodTypeWithError(_ error: NSErrorPointer) -> HKBloodTypeObject? } extension HKHealthStore {     func addSamples(_ samples: [AnyObject]!, toWorkout workout: HKWorkout!, completion completion: ((Bool, NSError!) -> Void)!) } extension HKHealthStore {     func enableBackgroundDeliveryForType(_ type: HKObjectType!, frequency frequency: HKUpdateFrequency, withCompletion completion: ((Bool, NSError!) -> Void)!)     func disableBackgroundDeliveryForType(_ type: HKObjectType!, withCompletion completion: ((Bool, NSError!) -> Void)!)     func disableAllBackgroundDeliveryWithCompletion(_ completion: ((Bool, NSError!) -> Void)!) } extension HKHealthStore {     func preferredUnitsForQuantityTypes(_ quantityTypes: Set<NSObject>!, completion completion: (([NSObject : AnyObject]!, NSError!) -> Void)!) } ``` |
| To | ``` class HKHealthStore : NSObject {     class func isHealthDataAvailable() -> Bool     func authorizationStatusForType(_ type: HKObjectType) -> HKAuthorizationStatus     func requestAuthorizationToShareTypes(_ typesToShare: Set<HKSampleType>?, readTypes typesToRead: Set<HKObjectType>?, completion completion: (Bool, NSError?) -> Void)     func handleAuthorizationForExtensionWithCompletion(_ completion: (Bool, NSError?) -> Void)     func earliestPermittedSampleDate() -> NSDate     func saveObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void)     func saveObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void)     func deleteObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void)     func deleteObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void)     func deleteObjectsOfType(_ objectType: HKObjectType, predicate predicate: NSPredicate, withCompletion completion: (Bool, Int, NSError?) -> Void)     func executeQuery(_ query: HKQuery)     func stopQuery(_ query: HKQuery)     func splitTotalEnergy(_ totalEnergy: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, resultsHandler resultsHandler: (HKQuantity?, HKQuantity?, NSError?) -> Void)     func dateOfBirth() throws -> NSDate     func biologicalSex() throws -> HKBiologicalSexObject     func bloodType() throws -> HKBloodTypeObject     func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject } extension HKHealthStore {     func addSamples(_ samples: [HKSample], toWorkout workout: HKWorkout, completion completion: (Bool, NSError?) -> Void)     func startWorkoutSession(_ workoutSession: HKWorkoutSession)     func endWorkoutSession(_ workoutSession: HKWorkoutSession) } extension HKHealthStore {     func enableBackgroundDeliveryForType(_ type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: (Bool, NSError?) -> Void)     func disableBackgroundDeliveryForType(_ type: HKObjectType, withCompletion completion: (Bool, NSError?) -> Void)     func disableAllBackgroundDeliveryWithCompletion(_ completion: (Bool, NSError?) -> Void) } extension HKHealthStore {     func preferredUnitsForQuantityTypes(_ quantityTypes: Set<HKQuantityType>, completion completion: ([HKQuantityType : HKUnit], NSError?) -> Void) } ``` |

Modified [HKHealthStore.addSamples(_: [HKSample], toWorkout: HKWorkout, completion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614165-addsamples)

|  | Declaration |
| --- | --- |
| From | ``` func addSamples(_ samples: [AnyObject]!, toWorkout workout: HKWorkout!, completion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func addSamples(_ samples: [HKSample], toWorkout workout: HKWorkout, completion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.authorizationStatusForType(_: HKObjectType) -> HKAuthorizationStatus](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614154-authorizationstatus)

|  | Declaration |
| --- | --- |
| From | ``` func authorizationStatusForType(_ type: HKObjectType!) -> HKAuthorizationStatus ``` |
| To | ``` func authorizationStatusForType(_ type: HKObjectType) -> HKAuthorizationStatus ``` |

Modified [HKHealthStore.biologicalSex() throws -> HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614171-biologicalsex)

|  | Declaration |
| --- | --- |
| From | ``` func biologicalSexWithError(_ error: NSErrorPointer) -> HKBiologicalSexObject? ``` |
| To | ``` func biologicalSex() throws -> HKBiologicalSexObject ``` |

Modified [HKHealthStore.bloodType() throws -> HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614164-bloodtypewitherror)

|  | Declaration |
| --- | --- |
| From | ``` func bloodTypeWithError(_ error: NSErrorPointer) -> HKBloodTypeObject? ``` |
| To | ``` func bloodType() throws -> HKBloodTypeObject ``` |

Modified [HKHealthStore.dateOfBirth() throws -> NSDate](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614160-dateofbirthwitherror)

|  | Declaration |
| --- | --- |
| From | ``` func dateOfBirthWithError(_ error: NSErrorPointer) -> NSDate? ``` |
| To | ``` func dateOfBirth() throws -> NSDate ``` |

Modified [HKHealthStore.deleteObject(_: HKObject, withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614155-delete)

|  | Declaration |
| --- | --- |
| From | ``` func deleteObject(_ object: HKObject!, withCompletion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func deleteObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.disableAllBackgroundDeliveryWithCompletion(_: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614158-disableallbackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func disableAllBackgroundDeliveryWithCompletion(_ completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func disableAllBackgroundDeliveryWithCompletion(_ completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.disableBackgroundDeliveryForType(_: HKObjectType, withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614177-disablebackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func disableBackgroundDeliveryForType(_ type: HKObjectType!, withCompletion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func disableBackgroundDeliveryForType(_ type: HKObjectType, withCompletion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.enableBackgroundDeliveryForType(_: HKObjectType, frequency: HKUpdateFrequency, withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614175-enablebackgrounddelivery)

|  | Declaration |
| --- | --- |
| From | ``` func enableBackgroundDeliveryForType(_ type: HKObjectType!, frequency frequency: HKUpdateFrequency, withCompletion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func enableBackgroundDeliveryForType(_ type: HKObjectType, frequency frequency: HKUpdateFrequency, withCompletion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.executeQuery(_: HKQuery)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614179-execute)

|  | Declaration |
| --- | --- |
| From | ``` func executeQuery(_ query: HKQuery!) ``` |
| To | ``` func executeQuery(_ query: HKQuery) ``` |

Modified [HKHealthStore.preferredUnitsForQuantityTypes(_: Set<HKQuantityType>, completion: ([HKQuantityType : HKUnit], NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614172-preferredunits)

|  | Declaration |
| --- | --- |
| From | ``` func preferredUnitsForQuantityTypes(_ quantityTypes: Set<NSObject>!, completion completion: (([NSObject : AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func preferredUnitsForQuantityTypes(_ quantityTypes: Set<HKQuantityType>, completion completion: ([HKQuantityType : HKUnit], NSError?) -> Void) ``` |

Modified [HKHealthStore.requestAuthorizationToShareTypes(_: Set<HKSampleType>?, readTypes: Set<HKObjectType>?, completion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorizationtosharetypes)

|  | Declaration |
| --- | --- |
| From | ``` func requestAuthorizationToShareTypes(_ typesToShare: Set<NSObject>!, readTypes typesToRead: Set<NSObject>!, completion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func requestAuthorizationToShareTypes(_ typesToShare: Set<HKSampleType>?, readTypes typesToRead: Set<HKObjectType>?, completion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.saveObject(_: HKObject, withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614168-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveObject(_ object: HKObject!, withCompletion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func saveObject(_ object: HKObject, withCompletion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.saveObjects(_: [HKObject], withCompletion: (Bool, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614176-save)

|  | Declaration |
| --- | --- |
| From | ``` func saveObjects(_ objects: [AnyObject]!, withCompletion completion: ((Bool, NSError!) -> Void)!) ``` |
| To | ``` func saveObjects(_ objects: [HKObject], withCompletion completion: (Bool, NSError?) -> Void) ``` |

Modified [HKHealthStore.stopQuery(_: HKQuery)](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614173-stopquery)

|  | Declaration |
| --- | --- |
| From | ``` func stopQuery(_ query: HKQuery!) ``` |
| To | ``` func stopQuery(_ query: HKQuery) ``` |

Modified [HKHeartRateSensorLocation [enum]](https://developer.apple.com/documentation/healthkit/hkheartratesensorlocation)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKMetricPrefix [enum]](https://developer.apple.com/documentation/healthkit/hkmetricprefix)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKObject](https://developer.apple.com/documentation/healthkit/hkobject)

|  | Declaration |
| --- | --- |
| From | ``` class HKObject : NSObject, NSSecureCoding, NSCoding {     var UUID: NSUUID! { get }     var source: HKSource! { get }     var metadata: [NSObject : AnyObject]! { get }     init!() } ``` |
| To | ``` class HKObject : NSObject, NSSecureCoding, NSCoding {     var UUID: NSUUID { get }     var source: HKSource { get }     var sourceRevision: HKSourceRevision { get }     var device: HKDevice? { get }     var metadata: [String : AnyObject]? { get }     init() } ``` |

Modified [HKObject.metadata](https://developer.apple.com/documentation/healthkit/hkobject/1615598-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: [NSObject : AnyObject]! { get } ``` |
| To | ``` var metadata: [String : AnyObject]? { get } ``` |

Modified [HKObject.source](https://developer.apple.com/documentation/healthkit/hkobject/1615781-source)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var source: HKSource! { get } ``` | -- |
| To | ``` var source: HKSource { get } ``` | iOS 9.0 |

Modified [HKObject.UUID](https://developer.apple.com/documentation/healthkit/hkobject/1615721-uuid)

|  | Declaration |
| --- | --- |
| From | ``` var UUID: NSUUID! { get } ``` |
| To | ``` var UUID: NSUUID { get } ``` |

Modified [HKObjectType](https://developer.apple.com/documentation/healthkit/hkobjecttype)

|  | Declaration |
| --- | --- |
| From | ``` class HKObjectType : NSObject, NSSecureCoding, NSCoding, NSCopying {     var identifier: String! { get }     init!()     class func quantityTypeForIdentifier(_ identifier: String!) -> HKQuantityType!     class func categoryTypeForIdentifier(_ identifier: String!) -> HKCategoryType!     class func characteristicTypeForIdentifier(_ identifier: String!) -> HKCharacteristicType!     class func correlationTypeForIdentifier(_ identifier: String!) -> HKCorrelationType!     class func workoutType() -> HKWorkoutType! } ``` |
| To | ``` class HKObjectType : NSObject, NSSecureCoding, NSCoding, NSCopying {     var identifier: String { get }     init()     class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType?     class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType?     class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType?     class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType?     class func workoutType() -> HKWorkoutType } ``` |

Modified [HKObjectType.categoryTypeForIdentifier(_: String) -> HKCategoryType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615526-categorytype)

|  | Declaration |
| --- | --- |
| From | ``` class func categoryTypeForIdentifier(_ identifier: String!) -> HKCategoryType! ``` |
| To | ``` class func categoryTypeForIdentifier(_ identifier: String) -> HKCategoryType? ``` |

Modified [HKObjectType.characteristicTypeForIdentifier(_: String) -> HKCharacteristicType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615558-characteristictype)

|  | Declaration |
| --- | --- |
| From | ``` class func characteristicTypeForIdentifier(_ identifier: String!) -> HKCharacteristicType! ``` |
| To | ``` class func characteristicTypeForIdentifier(_ identifier: String) -> HKCharacteristicType? ``` |

Modified [HKObjectType.correlationTypeForIdentifier(_: String) -> HKCorrelationType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615580-correlationtype)

|  | Declaration |
| --- | --- |
| From | ``` class func correlationTypeForIdentifier(_ identifier: String!) -> HKCorrelationType! ``` |
| To | ``` class func correlationTypeForIdentifier(_ identifier: String) -> HKCorrelationType? ``` |

Modified [HKObjectType.identifier](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615294-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String { get } ``` |

Modified [HKObjectType.quantityTypeForIdentifier(_: String) -> HKQuantityType? [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615298-quantitytypeforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` class func quantityTypeForIdentifier(_ identifier: String!) -> HKQuantityType! ``` |
| To | ``` class func quantityTypeForIdentifier(_ identifier: String) -> HKQuantityType? ``` |

Modified [HKObjectType.workoutType() -> HKWorkoutType [class]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615132-workouttype)

|  | Declaration |
| --- | --- |
| From | ``` class func workoutType() -> HKWorkoutType! ``` |
| To | ``` class func workoutType() -> HKWorkoutType ``` |

Modified [HKObserverQuery](https://developer.apple.com/documentation/healthkit/hkobserverquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKObserverQuery : HKQuery {     init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, updateHandler updateHandler: ((HKObserverQuery!, HKObserverQueryCompletionHandler!, NSError!) -> Void)!) } ``` |
| To | ``` class HKObserverQuery : HKQuery {     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, NSError?) -> Void) } ``` |

Modified [HKObserverQuery.init(sampleType: HKSampleType, predicate: NSPredicate?, updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkobserverquery/1615317-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, updateHandler updateHandler: ((HKObserverQuery!, HKObserverQueryCompletionHandler!, NSError!) -> Void)!) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, updateHandler updateHandler: (HKObserverQuery, HKObserverQueryCompletionHandler, NSError?) -> Void) ``` |

Modified [HKQuantity](https://developer.apple.com/documentation/healthkit/hkquantity)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuantity : NSObject, NSSecureCoding, NSCoding, NSCopying {     init!()     convenience init!(unit unit: HKUnit!, doubleValue value: Double)     class func quantityWithUnit(_ unit: HKUnit!, doubleValue value: Double) -> Self!     func isCompatibleWithUnit(_ unit: HKUnit!) -> Bool     func doubleValueForUnit(_ unit: HKUnit!) -> Double     func compare(_ quantity: HKQuantity) -> NSComparisonResult } ``` |
| To | ``` class HKQuantity : NSObject, NSSecureCoding, NSCoding, NSCopying {     init()     convenience init(unit unit: HKUnit, doubleValue value: Double)     class func quantityWithUnit(_ unit: HKUnit, doubleValue value: Double) -> Self     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool     func doubleValueForUnit(_ unit: HKUnit) -> Double     func compare(_ quantity: HKQuantity) -> NSComparisonResult } ``` |

Modified [HKQuantity.doubleValueForUnit(_: HKUnit) -> Double](https://developer.apple.com/documentation/healthkit/hkquantity/1615245-doublevalueforunit)

|  | Declaration |
| --- | --- |
| From | ``` func doubleValueForUnit(_ unit: HKUnit!) -> Double ``` |
| To | ``` func doubleValueForUnit(_ unit: HKUnit) -> Double ``` |

Modified [HKQuantity.init(unit: HKUnit, doubleValue: Double)](https://developer.apple.com/documentation/healthkit/hkquantity/1615035-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(unit unit: HKUnit!, doubleValue value: Double) ``` |
| To | ``` convenience init(unit unit: HKUnit, doubleValue value: Double) ``` |

Modified [HKQuantity.isCompatibleWithUnit(_: HKUnit) -> Bool](https://developer.apple.com/documentation/healthkit/hkquantity/1615508-iscompatiblewithunit)

|  | Declaration |
| --- | --- |
| From | ``` func isCompatibleWithUnit(_ unit: HKUnit!) -> Bool ``` |
| To | ``` func isCompatibleWithUnit(_ unit: HKUnit) -> Bool ``` |

Modified [HKQuantityAggregationStyle [enum]](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKQuantitySample](https://developer.apple.com/documentation/healthkit/hkquantitysample)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuantitySample : HKSample {     var quantityType: HKQuantityType! { get }     var quantity: HKQuantity! { get }     convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!)     class func quantitySampleWithType(_ quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!) -> Self!     convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!)     class func quantitySampleWithType(_ quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) -> Self! } ``` |
| To | ``` class HKQuantitySample : HKSample {     var quantityType: HKQuantityType { get }     var quantity: HKQuantity { get }     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) -> Self     convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func quantitySampleWithType(_ quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |

Modified [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, startDate: NSDate, endDate: NSDate)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615016-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate) ``` |

Modified [HKQuantitySample.init(type: HKQuantityType, quantity: HKQuantity, startDate: NSDate, endDate: NSDate, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615017-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type quantityType: HKQuantityType!, quantity quantity: HKQuantity!, startDate startDate: NSDate!, endDate endDate: NSDate!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(type quantityType: HKQuantityType, quantity quantity: HKQuantity, startDate startDate: NSDate, endDate endDate: NSDate, metadata metadata: [String : AnyObject]?) ``` |

Modified [HKQuantitySample.quantity](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615015-quantity)

|  | Declaration |
| --- | --- |
| From | ``` var quantity: HKQuantity! { get } ``` |
| To | ``` var quantity: HKQuantity { get } ``` |

Modified [HKQuantitySample.quantityType](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615020-quantitytype)

|  | Declaration |
| --- | --- |
| From | ``` var quantityType: HKQuantityType! { get } ``` |
| To | ``` var quantityType: HKQuantityType { get } ``` |

Modified [HKQuantityType](https://developer.apple.com/documentation/healthkit/hkquantitytype)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuantityType : HKSampleType {     var aggregationStyle: HKQuantityAggregationStyle { get }     func isCompatibleWithUnit(_ unit: HKUnit!) -> Bool } ``` |
| To | ``` class HKQuantityType : HKSampleType {     var aggregationStyle: HKQuantityAggregationStyle { get }     func isCompatibleWithUnit(_ unit: HKUnit) -> Bool } ``` |

Modified [HKQuantityType.isCompatibleWithUnit(_: HKUnit) -> Bool](https://developer.apple.com/documentation/healthkit/hkquantitytype/1615719-iscompatiblewithunit)

|  | Declaration |
| --- | --- |
| From | ``` func isCompatibleWithUnit(_ unit: HKUnit!) -> Bool ``` |
| To | ``` func isCompatibleWithUnit(_ unit: HKUnit) -> Bool ``` |

Modified [HKQuery](https://developer.apple.com/documentation/healthkit/hkquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKQuery : NSObject {     var sampleType: HKSampleType! { get }     var predicate: NSPredicate! { get }     init!() } extension HKQuery {     class func predicateForObjectsWithMetadataKey(_ key: String!) -> NSPredicate!     class func predicateForObjectsWithMetadataKey(_ key: String!, allowedValues allowedValues: [AnyObject]!) -> NSPredicate!     class func predicateForObjectsWithMetadataKey(_ key: String!, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject!) -> NSPredicate!     class func predicateForObjectsFromSource(_ source: HKSource!) -> NSPredicate!     class func predicateForObjectsFromSources(_ sources: Set<NSObject>!) -> NSPredicate!     class func predicateForObjectWithUUID(_ UUID: NSUUID!) -> NSPredicate!     class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSObject>!) -> NSPredicate!     class func predicateForObjectsWithNoCorrelation() -> NSPredicate!     class func predicateForObjectsFromWorkout(_ workout: HKWorkout!) -> NSPredicate! } extension HKQuery {     class func predicateForSamplesWithStartDate(_ startDate: NSDate!, endDate endDate: NSDate!, options options: HKQueryOptions) -> NSPredicate! } extension HKQuery {     class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity!) -> NSPredicate! } extension HKQuery {     class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate! } extension HKQuery {     class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate!     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate!     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity!) -> NSPredicate!     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity!) -> NSPredicate! } ``` |
| To | ``` class HKQuery : NSObject {     var sampleType: HKSampleType { get }     var predicate: NSPredicate? { get }     init() } extension HKQuery {     class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate     class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate     class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate     class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate     class func predicateForObjectsFromSourceRevisions(_ sourceRevisions: Set<HKSourceRevision>) -> NSPredicate     class func predicateForObjectsFromDevices(_ devices: Set<HKDevice>) -> NSPredicate     class func predicateForObjectsWithDeviceProperty(_ key: String, allowedValues allowedValues: Set<String>) -> NSPredicate     class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate     class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate     class func predicateForObjectsWithNoCorrelation() -> NSPredicate     class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate } extension HKQuery {     class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate } extension HKQuery {     class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate } extension HKQuery {     class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate } extension HKQuery {     class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate     class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate } ``` |

Modified [HKQuery.predicate](https://developer.apple.com/documentation/healthkit/hkquery/1614763-predicate)

|  | Declaration |
| --- | --- |
| From | ``` var predicate: NSPredicate! { get } ``` |
| To | ``` var predicate: NSPredicate? { get } ``` |

Modified [HKQuery.predicateForCategorySamplesWithOperatorType(_: NSPredicateOperatorType, value: Int) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614781-predicateforcategorysampleswitho)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate! ``` |
| To | ``` class func predicateForCategorySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, value value: Int) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsFromSource(_: HKSource) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614769-predicateforobjectsfromsource)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromSource(_ source: HKSource!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsFromSource(_ source: HKSource) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsFromSources(_: Set<HKSource>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614767-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromSources(_ sources: Set<NSObject>!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsFromSources(_ sources: Set<HKSource>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsFromWorkout(_: HKWorkout) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614773-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsFromWorkout(_ workout: HKWorkout!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsFromWorkout(_ workout: HKWorkout) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsWithMetadataKey(_: String) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614782-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsWithMetadataKey(_ key: String) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsWithMetadataKey(_: String, allowedValues: [AnyObject]) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614780-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String!, allowedValues allowedValues: [AnyObject]!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsWithMetadataKey(_ key: String, allowedValues allowedValues: [AnyObject]) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsWithMetadataKey(_: String, operatorType: NSPredicateOperatorType, value: AnyObject) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614764-predicateforobjectswithmetadatak)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithMetadataKey(_ key: String!, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsWithMetadataKey(_ key: String, operatorType operatorType: NSPredicateOperatorType, value value: AnyObject) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsWithNoCorrelation() -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614762-predicateforobjectswithnocorrela)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithNoCorrelation() -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsWithNoCorrelation() -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectsWithUUIDs(_: Set<NSUUID>) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614785-predicateforobjects)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSObject>!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectsWithUUIDs(_ UUIDs: Set<NSUUID>) -> NSPredicate ``` |

Modified [HKQuery.predicateForObjectWithUUID(_: NSUUID) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614783-predicateforobject)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForObjectWithUUID(_ UUID: NSUUID!) -> NSPredicate! ``` |
| To | ``` class func predicateForObjectWithUUID(_ UUID: NSUUID) -> NSPredicate ``` |

Modified [HKQuery.predicateForQuantitySamplesWithOperatorType(_: NSPredicateOperatorType, quantity: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614761-predicateforquantitysamples)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity!) -> NSPredicate! ``` |
| To | ``` class func predicateForQuantitySamplesWithOperatorType(_ operatorType: NSPredicateOperatorType, quantity quantity: HKQuantity) -> NSPredicate ``` |

Modified [HKQuery.predicateForSamplesWithStartDate(_: NSDate?, endDate: NSDate?, options: HKQueryOptions) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614771-predicateforsampleswithstartdate)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForSamplesWithStartDate(_ startDate: NSDate!, endDate endDate: NSDate!, options options: HKQueryOptions) -> NSPredicate! ``` |
| To | ``` class func predicateForSamplesWithStartDate(_ startDate: NSDate?, endDate endDate: NSDate?, options options: HKQueryOptions) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkoutsWithOperatorType(_: NSPredicateOperatorType, duration: NSTimeInterval) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614772-predicateforworkouts)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate! ``` |
| To | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, duration duration: NSTimeInterval) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkoutsWithOperatorType(_: NSPredicateOperatorType, totalDistance: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614779-predicateforworkoutswithoperator)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity!) -> NSPredicate! ``` |
| To | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalDistance totalDistance: HKQuantity) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkoutsWithOperatorType(_: NSPredicateOperatorType, totalEnergyBurned: HKQuantity) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614788-predicateforworkouts)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity!) -> NSPredicate! ``` |
| To | ``` class func predicateForWorkoutsWithOperatorType(_ operatorType: NSPredicateOperatorType, totalEnergyBurned totalEnergyBurned: HKQuantity) -> NSPredicate ``` |

Modified [HKQuery.predicateForWorkoutsWithWorkoutActivityType(_: HKWorkoutActivityType) -> NSPredicate [class]](https://developer.apple.com/documentation/healthkit/hkquery/1614787-predicateforworkoutswithworkouta)

|  | Declaration |
| --- | --- |
| From | ``` class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate! ``` |
| To | ``` class func predicateForWorkoutsWithWorkoutActivityType(_ workoutActivityType: HKWorkoutActivityType) -> NSPredicate ``` |

Modified [HKQuery.sampleType](https://developer.apple.com/documentation/healthkit/hkquery/1614789-sampletype)

|  | Declaration |
| --- | --- |
| From | ``` var sampleType: HKSampleType! { get } ``` |
| To | ``` var sampleType: HKSampleType { get } ``` |

Modified [HKQueryOptions [struct]](https://developer.apple.com/documentation/healthkit/hkqueryoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct HKQueryOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: HKQueryOptions { get }     static var StrictStartDate: HKQueryOptions { get }     static var StrictEndDate: HKQueryOptions { get } } ``` | RawOptionSetType |
| To | ``` struct HKQueryOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var None: HKQueryOptions { get }     static var StrictStartDate: HKQueryOptions { get }     static var StrictEndDate: HKQueryOptions { get } } ``` | OptionSetType |

Modified [HKSample](https://developer.apple.com/documentation/healthkit/hksample)

|  | Declaration |
| --- | --- |
| From | ``` class HKSample : HKObject {     var sampleType: HKSampleType! { get }     var startDate: NSDate! { get }     var endDate: NSDate! { get } } ``` |
| To | ``` class HKSample : HKObject {     var sampleType: HKSampleType { get }     var startDate: NSDate { get }     var endDate: NSDate { get } } ``` |

Modified [HKSample.endDate](https://developer.apple.com/documentation/healthkit/hksample/1615170-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate { get } ``` |

Modified [HKSample.sampleType](https://developer.apple.com/documentation/healthkit/hksample/1615744-sampletype)

|  | Declaration |
| --- | --- |
| From | ``` var sampleType: HKSampleType! { get } ``` |
| To | ``` var sampleType: HKSampleType { get } ``` |

Modified [HKSample.startDate](https://developer.apple.com/documentation/healthkit/hksample/1615481-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate { get } ``` |

Modified [HKSampleQuery](https://developer.apple.com/documentation/healthkit/hksamplequery)

|  | Declaration |
| --- | --- |
| From | ``` class HKSampleQuery : HKQuery {     var limit: Int { get }     var sortDescriptors: [AnyObject]! { get }     init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, limit limit: Int, sortDescriptors sortDescriptors: [AnyObject]!, resultsHandler resultsHandler: ((HKSampleQuery!, [AnyObject]!, NSError!) -> Void)!) } ``` |
| To | ``` class HKSampleQuery : HKQuery {     var limit: Int { get }     var sortDescriptors: [NSSortDescriptor]? { get }     init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: (HKSampleQuery, [HKSample]?, NSError?) -> Void) } ``` |

Modified [HKSampleQuery.init(sampleType: HKSampleType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, resultsHandler: (HKSampleQuery, [HKSample]?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hksamplequery/1615055-initwithsampletype)

|  | Declaration |
| --- | --- |
| From | ``` init!(sampleType sampleType: HKSampleType!, predicate predicate: NSPredicate!, limit limit: Int, sortDescriptors sortDescriptors: [AnyObject]!, resultsHandler resultsHandler: ((HKSampleQuery!, [AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, predicate predicate: NSPredicate?, limit limit: Int, sortDescriptors sortDescriptors: [NSSortDescriptor]?, resultsHandler resultsHandler: (HKSampleQuery, [HKSample]?, NSError?) -> Void) ``` |

Modified [HKSampleQuery.sortDescriptors](https://developer.apple.com/documentation/healthkit/hksamplequery/1615128-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` var sortDescriptors: [AnyObject]! { get } ``` |
| To | ``` var sortDescriptors: [NSSortDescriptor]? { get } ``` |

Modified [HKSource](https://developer.apple.com/documentation/healthkit/hksource)

|  | Declaration |
| --- | --- |
| From | ``` class HKSource : NSObject, NSSecureCoding, NSCoding, NSCopying {     var name: String! { get }     var bundleIdentifier: String! { get }     class func defaultSource() -> HKSource!     init!() } ``` |
| To | ``` class HKSource : NSObject, NSSecureCoding, NSCoding, NSCopying {     var name: String { get }     var bundleIdentifier: String { get }     class func defaultSource() -> HKSource     init() } ``` |

Modified [HKSource.bundleIdentifier](https://developer.apple.com/documentation/healthkit/hksource/1615704-bundleidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var bundleIdentifier: String! { get } ``` |
| To | ``` var bundleIdentifier: String { get } ``` |

Modified [HKSource.defaultSource() -> HKSource [class]](https://developer.apple.com/documentation/healthkit/hksource/1615046-defaultsource)

|  | Declaration |
| --- | --- |
| From | ``` class func defaultSource() -> HKSource! ``` |
| To | ``` class func defaultSource() -> HKSource ``` |

Modified [HKSource.name](https://developer.apple.com/documentation/healthkit/hksource/1615115-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HKSourceQuery](https://developer.apple.com/documentation/healthkit/hksourcequery)

|  | Declaration |
| --- | --- |
| From | ``` class HKSourceQuery : HKQuery {     init!(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, Set<NSObject>!, NSError!) -> Void)!) } ``` |
| To | ``` class HKSourceQuery : HKQuery {     init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: (HKSourceQuery, Set<HKSource>?, NSError?) -> Void) } ``` |

Modified [HKSourceQuery.init(sampleType: HKSampleType, samplePredicate: NSPredicate?, completionHandler: (HKSourceQuery, Set<HKSource>?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hksourcequery/1614367-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(sampleType sampleType: HKSampleType!, samplePredicate objectPredicate: NSPredicate!, completionHandler completionHandler: ((HKSourceQuery!, Set<NSObject>!, NSError!) -> Void)!) ``` |
| To | ``` init(sampleType sampleType: HKSampleType, samplePredicate objectPredicate: NSPredicate?, completionHandler completionHandler: (HKSourceQuery, Set<HKSource>?, NSError?) -> Void) ``` |

Modified [HKStatistics](https://developer.apple.com/documentation/healthkit/hkstatistics)

|  | Declaration |
| --- | --- |
| From | ``` class HKStatistics : NSObject, NSSecureCoding, NSCoding, NSCopying {     var quantityType: HKQuantityType! { get }     var startDate: NSDate! { get }     var endDate: NSDate! { get }     var sources: [AnyObject]! { get }     init!()     func averageQuantityForSource(_ source: HKSource!) -> HKQuantity!     func averageQuantity() -> HKQuantity!     func minimumQuantityForSource(_ source: HKSource!) -> HKQuantity!     func minimumQuantity() -> HKQuantity!     func maximumQuantityForSource(_ source: HKSource!) -> HKQuantity!     func maximumQuantity() -> HKQuantity!     func sumQuantityForSource(_ source: HKSource!) -> HKQuantity!     func sumQuantity() -> HKQuantity! } ``` |
| To | ``` class HKStatistics : NSObject, NSSecureCoding, NSCoding, NSCopying {     var quantityType: HKQuantityType { get }     var startDate: NSDate { get }     var endDate: NSDate { get }     var sources: [HKSource]? { get }     init()     func averageQuantityForSource(_ source: HKSource) -> HKQuantity?     func averageQuantity() -> HKQuantity?     func minimumQuantityForSource(_ source: HKSource) -> HKQuantity?     func minimumQuantity() -> HKQuantity?     func maximumQuantityForSource(_ source: HKSource) -> HKQuantity?     func maximumQuantity() -> HKQuantity?     func sumQuantityForSource(_ source: HKSource) -> HKQuantity?     func sumQuantity() -> HKQuantity? } ``` |

Modified [HKStatistics.averageQuantity() -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615386-averagequantity)

|  | Declaration |
| --- | --- |
| From | ``` func averageQuantity() -> HKQuantity! ``` |
| To | ``` func averageQuantity() -> HKQuantity? ``` |

Modified [HKStatistics.averageQuantityForSource(_: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615307-averagequantity)

|  | Declaration |
| --- | --- |
| From | ``` func averageQuantityForSource(_ source: HKSource!) -> HKQuantity! ``` |
| To | ``` func averageQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.endDate](https://developer.apple.com/documentation/healthkit/hkstatistics/1615067-enddate)

|  | Declaration |
| --- | --- |
| From | ``` var endDate: NSDate! { get } ``` |
| To | ``` var endDate: NSDate { get } ``` |

Modified [HKStatistics.maximumQuantity() -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615519-maximumquantity)

|  | Declaration |
| --- | --- |
| From | ``` func maximumQuantity() -> HKQuantity! ``` |
| To | ``` func maximumQuantity() -> HKQuantity? ``` |

Modified [HKStatistics.maximumQuantityForSource(_: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615630-maximumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func maximumQuantityForSource(_ source: HKSource!) -> HKQuantity! ``` |
| To | ``` func maximumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.minimumQuantity() -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615638-minimumquantity)

|  | Declaration |
| --- | --- |
| From | ``` func minimumQuantity() -> HKQuantity! ``` |
| To | ``` func minimumQuantity() -> HKQuantity? ``` |

Modified [HKStatistics.minimumQuantityForSource(_: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615065-minimumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func minimumQuantityForSource(_ source: HKSource!) -> HKQuantity! ``` |
| To | ``` func minimumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |

Modified [HKStatistics.quantityType](https://developer.apple.com/documentation/healthkit/hkstatistics/1615476-quantitytype)

|  | Declaration |
| --- | --- |
| From | ``` var quantityType: HKQuantityType! { get } ``` |
| To | ``` var quantityType: HKQuantityType { get } ``` |

Modified [HKStatistics.sources](https://developer.apple.com/documentation/healthkit/hkstatistics/1615222-sources)

|  | Declaration |
| --- | --- |
| From | ``` var sources: [AnyObject]! { get } ``` |
| To | ``` var sources: [HKSource]? { get } ``` |

Modified [HKStatistics.startDate](https://developer.apple.com/documentation/healthkit/hkstatistics/1615351-startdate)

|  | Declaration |
| --- | --- |
| From | ``` var startDate: NSDate! { get } ``` |
| To | ``` var startDate: NSDate { get } ``` |

Modified [HKStatistics.sumQuantity() -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615680-sumquantity)

|  | Declaration |
| --- | --- |
| From | ``` func sumQuantity() -> HKQuantity! ``` |
| To | ``` func sumQuantity() -> HKQuantity? ``` |

Modified [HKStatistics.sumQuantityForSource(_: HKSource) -> HKQuantity?](https://developer.apple.com/documentation/healthkit/hkstatistics/1615502-sumquantityforsource)

|  | Declaration |
| --- | --- |
| From | ``` func sumQuantityForSource(_ source: HKSource!) -> HKQuantity! ``` |
| To | ``` func sumQuantityForSource(_ source: HKSource) -> HKQuantity? ``` |

Modified [HKStatisticsCollection](https://developer.apple.com/documentation/healthkit/hkstatisticscollection)

|  | Declaration |
| --- | --- |
| From | ``` class HKStatisticsCollection : NSObject {     init!()     func statisticsForDate(_ date: NSDate!) -> HKStatistics!     func enumerateStatisticsFromDate(_ startDate: NSDate!, toDate endDate: NSDate!, withBlock block: ((HKStatistics!, UnsafeMutablePointer<ObjCBool>) -> Void)!)     func statistics() -> [AnyObject]!     func sources() -> Set<NSObject>! } ``` |
| To | ``` class HKStatisticsCollection : NSObject {     init()     func statisticsForDate(_ date: NSDate) -> HKStatistics?     func enumerateStatisticsFromDate(_ startDate: NSDate, toDate endDate: NSDate, withBlock block: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)     func statistics() -> [HKStatistics]     func sources() -> Set<HKSource> } ``` |

Modified [HKStatisticsCollection.enumerateStatisticsFromDate(_: NSDate, toDate: NSDate, withBlock: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void)](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615783-enumeratestatisticsfromdate)

|  | Declaration |
| --- | --- |
| From | ``` func enumerateStatisticsFromDate(_ startDate: NSDate!, toDate endDate: NSDate!, withBlock block: ((HKStatistics!, UnsafeMutablePointer<ObjCBool>) -> Void)!) ``` |
| To | ``` func enumerateStatisticsFromDate(_ startDate: NSDate, toDate endDate: NSDate, withBlock block: (HKStatistics, UnsafeMutablePointer<ObjCBool>) -> Void) ``` |

Modified [HKStatisticsCollection.sources() -> Set<HKSource>](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615456-sources)

|  | Declaration |
| --- | --- |
| From | ``` func sources() -> Set<NSObject>! ``` |
| To | ``` func sources() -> Set<HKSource> ``` |

Modified [HKStatisticsCollection.statistics() -> [HKStatistics]](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615550-statistics)

|  | Declaration |
| --- | --- |
| From | ``` func statistics() -> [AnyObject]! ``` |
| To | ``` func statistics() -> [HKStatistics] ``` |

Modified [HKStatisticsCollection.statisticsForDate(_: NSDate) -> HKStatistics?](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615300-statistics)

|  | Declaration |
| --- | --- |
| From | ``` func statisticsForDate(_ date: NSDate!) -> HKStatistics! ``` |
| To | ``` func statisticsForDate(_ date: NSDate) -> HKStatistics? ``` |

Modified [HKStatisticsCollectionQuery](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKStatisticsCollectionQuery : HKQuery {     var anchorDate: NSDate! { get }     var options: HKStatisticsOptions { get }     @NSCopying var intervalComponents: NSDateComponents! { get }     var initialResultsHandler: ((HKStatisticsCollectionQuery!, HKStatisticsCollection!, NSError!) -> Void)!     var statisticsUpdateHandler: ((HKStatisticsCollectionQuery!, HKStatistics!, HKStatisticsCollection!, NSError!) -> Void)!     init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate!, intervalComponents intervalComponents: NSDateComponents!) } ``` |
| To | ``` class HKStatisticsCollectionQuery : HKQuery {     var anchorDate: NSDate { get }     var options: HKStatisticsOptions { get }     @NSCopying var intervalComponents: NSDateComponents { get }     var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, NSError?) -> Void)?     var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, NSError?) -> Void)?     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate, intervalComponents intervalComponents: NSDateComponents) } ``` |

Modified [HKStatisticsCollectionQuery.anchorDate](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615241-anchordate)

|  | Declaration |
| --- | --- |
| From | ``` var anchorDate: NSDate! { get } ``` |
| To | ``` var anchorDate: NSDate { get } ``` |

Modified [HKStatisticsCollectionQuery.init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, anchorDate: NSDate, intervalComponents: NSDateComponents)](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615199-initwithquantitytype)

|  | Declaration |
| --- | --- |
| From | ``` init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate!, intervalComponents intervalComponents: NSDateComponents!) ``` |
| To | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, anchorDate anchorDate: NSDate, intervalComponents intervalComponents: NSDateComponents) ``` |

Modified [HKStatisticsCollectionQuery.initialResultsHandler](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615755-initialresultshandler)

|  | Declaration |
| --- | --- |
| From | ``` var initialResultsHandler: ((HKStatisticsCollectionQuery!, HKStatisticsCollection!, NSError!) -> Void)! ``` |
| To | ``` var initialResultsHandler: ((HKStatisticsCollectionQuery, HKStatisticsCollection?, NSError?) -> Void)? ``` |

Modified [HKStatisticsCollectionQuery.intervalComponents](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615108-intervalcomponents)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var intervalComponents: NSDateComponents! { get } ``` |
| To | ``` @NSCopying var intervalComponents: NSDateComponents { get } ``` |

Modified [HKStatisticsCollectionQuery.statisticsUpdateHandler](https://developer.apple.com/documentation/healthkit/hkstatisticscollectionquery/1615723-statisticsupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var statisticsUpdateHandler: ((HKStatisticsCollectionQuery!, HKStatistics!, HKStatisticsCollection!, NSError!) -> Void)! ``` |
| To | ``` var statisticsUpdateHandler: ((HKStatisticsCollectionQuery, HKStatistics?, HKStatisticsCollection?, NSError?) -> Void)? ``` |

Modified [HKStatisticsOptions [struct]](https://developer.apple.com/documentation/healthkit/hkstatisticsoptions)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct HKStatisticsOptions : RawOptionSetType {     init(_ rawValue: UInt)     init(rawValue rawValue: UInt)     static var None: HKStatisticsOptions { get }     static var SeparateBySource: HKStatisticsOptions { get }     static var DiscreteAverage: HKStatisticsOptions { get }     static var DiscreteMin: HKStatisticsOptions { get }     static var DiscreteMax: HKStatisticsOptions { get }     static var CumulativeSum: HKStatisticsOptions { get } } ``` | RawOptionSetType |
| To | ``` struct HKStatisticsOptions : OptionSetType {     init(rawValue rawValue: UInt)     static var None: HKStatisticsOptions { get }     static var SeparateBySource: HKStatisticsOptions { get }     static var DiscreteAverage: HKStatisticsOptions { get }     static var DiscreteMin: HKStatisticsOptions { get }     static var DiscreteMax: HKStatisticsOptions { get }     static var CumulativeSum: HKStatisticsOptions { get } } ``` | OptionSetType |

Modified [HKStatisticsQuery](https://developer.apple.com/documentation/healthkit/hkstatisticsquery)

|  | Declaration |
| --- | --- |
| From | ``` class HKStatisticsQuery : HKQuery {     init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, completionHandler handler: ((HKStatisticsQuery!, HKStatistics!, NSError!) -> Void)!) } ``` |
| To | ``` class HKStatisticsQuery : HKQuery {     init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, completionHandler handler: (HKStatisticsQuery, HKStatistics?, NSError?) -> Void) } ``` |

Modified [HKStatisticsQuery.init(quantityType: HKQuantityType, quantitySamplePredicate: NSPredicate?, options: HKStatisticsOptions, completionHandler: (HKStatisticsQuery, HKStatistics?, NSError?) -> Void)](https://developer.apple.com/documentation/healthkit/hkstatisticsquery/1615536-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(quantityType quantityType: HKQuantityType!, quantitySamplePredicate quantitySamplePredicate: NSPredicate!, options options: HKStatisticsOptions, completionHandler handler: ((HKStatisticsQuery!, HKStatistics!, NSError!) -> Void)!) ``` |
| To | ``` init(quantityType quantityType: HKQuantityType, quantitySamplePredicate quantitySamplePredicate: NSPredicate?, options options: HKStatisticsOptions, completionHandler handler: (HKStatisticsQuery, HKStatistics?, NSError?) -> Void) ``` |

Modified [HKUnit](https://developer.apple.com/documentation/healthkit/hkunit)

|  | Declaration |
| --- | --- |
| From | ``` class HKUnit : NSObject, NSSecureCoding, NSCoding, NSCopying {     var unitString: String! { get }     init!()     convenience init!(fromString string: String!)     class func unitFromString(_ string: String!) -> Self!     convenience init!(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit)     class func unitFromMassFormatterUnit(_ massFormatterUnit: NSMassFormatterUnit) -> Self!     class func massFormatterUnitFromUnit(_ unit: HKUnit!) -> NSMassFormatterUnit     convenience init!(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit)     class func unitFromLengthFormatterUnit(_ lengthFormatterUnit: NSLengthFormatterUnit) -> Self!     class func lengthFormatterUnitFromUnit(_ unit: HKUnit!) -> NSLengthFormatterUnit     convenience init!(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit)     class func unitFromEnergyFormatterUnit(_ energyFormatterUnit: NSEnergyFormatterUnit) -> Self!     class func energyFormatterUnitFromUnit(_ unit: HKUnit!) -> NSEnergyFormatterUnit     func isNull() -> Bool } extension HKUnit {     class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func gramUnit() -> Self!     class func ounceUnit() -> Self!     class func poundUnit() -> Self!     class func stoneUnit() -> Self!     class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self!     class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self! } extension HKUnit {     class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func meterUnit() -> Self!     class func inchUnit() -> Self!     class func footUnit() -> Self!     class func mileUnit() -> Self! } extension HKUnit {     class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func literUnit() -> Self!     class func fluidOunceUSUnit() -> Self!     class func fluidOunceImperialUnit() -> Self!     class func pintUSUnit() -> Self!     class func pintImperialUnit() -> Self! } extension HKUnit {     class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func pascalUnit() -> Self!     class func millimeterOfMercuryUnit() -> Self!     class func centimeterOfWaterUnit() -> Self!     class func atmosphereUnit() -> Self! } extension HKUnit {     class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func secondUnit() -> Self!     class func minuteUnit() -> Self!     class func hourUnit() -> Self!     class func dayUnit() -> Self! } extension HKUnit {     class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func jouleUnit() -> Self!     class func calorieUnit() -> Self!     class func kilocalorieUnit() -> Self! } extension HKUnit {     class func degreeCelsiusUnit() -> Self!     class func degreeFahrenheitUnit() -> Self!     class func kelvinUnit() -> Self! } extension HKUnit {     class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self!     class func siemenUnit() -> Self! } extension HKUnit {     class func countUnit() -> Self!     class func percentUnit() -> Self! } extension HKUnit {     func unitMultipliedByUnit(_ unit: HKUnit!) -> HKUnit!     func unitDividedByUnit(_ unit: HKUnit!) -> HKUnit!     func unitRaisedToPower(_ power: Int) -> HKUnit!     func reciprocalUnit() -> HKUnit! } ``` |
| To | ``` class HKUnit : NSObject, NSSecureCoding, NSCoding, NSCopying {     var unitString: String { get }     init()     convenience init(fromString string: String)     class func unitFromString(_ string: String) -> Self     convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit)     class func unitFromMassFormatterUnit(_ massFormatterUnit: NSMassFormatterUnit) -> Self     class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit     convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit)     class func unitFromLengthFormatterUnit(_ lengthFormatterUnit: NSLengthFormatterUnit) -> Self     class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit     convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit)     class func unitFromEnergyFormatterUnit(_ energyFormatterUnit: NSEnergyFormatterUnit) -> Self     class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit     func isNull() -> Bool } extension HKUnit {     class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func gramUnit() -> Self     class func ounceUnit() -> Self     class func poundUnit() -> Self     class func stoneUnit() -> Self     class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self     class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self } extension HKUnit {     class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func meterUnit() -> Self     class func inchUnit() -> Self     class func footUnit() -> Self     class func yardUnit() -> Self     class func mileUnit() -> Self } extension HKUnit {     class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func literUnit() -> Self     class func fluidOunceUSUnit() -> Self     class func fluidOunceImperialUnit() -> Self     class func pintUSUnit() -> Self     class func pintImperialUnit() -> Self     class func cupUSUnit() -> Self     class func cupImperialUnit() -> Self } extension HKUnit {     class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func pascalUnit() -> Self     class func millimeterOfMercuryUnit() -> Self     class func centimeterOfWaterUnit() -> Self     class func atmosphereUnit() -> Self } extension HKUnit {     class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func secondUnit() -> Self     class func minuteUnit() -> Self     class func hourUnit() -> Self     class func dayUnit() -> Self } extension HKUnit {     class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func jouleUnit() -> Self     class func calorieUnit() -> Self     class func kilocalorieUnit() -> Self } extension HKUnit {     class func degreeCelsiusUnit() -> Self     class func degreeFahrenheitUnit() -> Self     class func kelvinUnit() -> Self } extension HKUnit {     class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self     class func siemenUnit() -> Self } extension HKUnit {     class func countUnit() -> Self     class func percentUnit() -> Self } extension HKUnit {     func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit     func unitDividedByUnit(_ unit: HKUnit) -> HKUnit     func unitRaisedToPower(_ power: Int) -> HKUnit     func reciprocalUnit() -> HKUnit } ``` |

Modified [HKUnit.atmosphereUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615672-atmosphereunit)

|  | Declaration |
| --- | --- |
| From | ``` class func atmosphereUnit() -> Self! ``` |
| To | ``` class func atmosphereUnit() -> Self ``` |

Modified [HKUnit.calorieUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615359-calorie)

|  | Declaration |
| --- | --- |
| From | ``` class func calorieUnit() -> Self! ``` |
| To | ``` class func calorieUnit() -> Self ``` |

Modified [HKUnit.centimeterOfWaterUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615036-centimeterofwater)

|  | Declaration |
| --- | --- |
| From | ``` class func centimeterOfWaterUnit() -> Self! ``` |
| To | ``` class func centimeterOfWaterUnit() -> Self ``` |

Modified [HKUnit.countUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615529-countunit)

|  | Declaration |
| --- | --- |
| From | ``` class func countUnit() -> Self! ``` |
| To | ``` class func countUnit() -> Self ``` |

Modified [HKUnit.dayUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615707-dayunit)

|  | Declaration |
| --- | --- |
| From | ``` class func dayUnit() -> Self! ``` |
| To | ``` class func dayUnit() -> Self ``` |

Modified [HKUnit.degreeCelsiusUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615180-degreecelsius)

|  | Declaration |
| --- | --- |
| From | ``` class func degreeCelsiusUnit() -> Self! ``` |
| To | ``` class func degreeCelsiusUnit() -> Self ``` |

Modified [HKUnit.degreeFahrenheitUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615444-degreefahrenheitunit)

|  | Declaration |
| --- | --- |
| From | ``` class func degreeFahrenheitUnit() -> Self! ``` |
| To | ``` class func degreeFahrenheitUnit() -> Self ``` |

Modified [HKUnit.energyFormatterUnitFromUnit(_: HKUnit) -> NSEnergyFormatterUnit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615211-energyformatterunitfromunit)

|  | Declaration |
| --- | --- |
| From | ``` class func energyFormatterUnitFromUnit(_ unit: HKUnit!) -> NSEnergyFormatterUnit ``` |
| To | ``` class func energyFormatterUnitFromUnit(_ unit: HKUnit) -> NSEnergyFormatterUnit ``` |

Modified [HKUnit.fluidOunceImperialUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615614-fluidounceimperial)

|  | Declaration |
| --- | --- |
| From | ``` class func fluidOunceImperialUnit() -> Self! ``` |
| To | ``` class func fluidOunceImperialUnit() -> Self ``` |

Modified [HKUnit.fluidOunceUSUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615310-fluidounceus)

|  | Declaration |
| --- | --- |
| From | ``` class func fluidOunceUSUnit() -> Self! ``` |
| To | ``` class func fluidOunceUSUnit() -> Self ``` |

Modified [HKUnit.footUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615043-footunit)

|  | Declaration |
| --- | --- |
| From | ``` class func footUnit() -> Self! ``` |
| To | ``` class func footUnit() -> Self ``` |

Modified [HKUnit.gramUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615050-gramunit)

|  | Declaration |
| --- | --- |
| From | ``` class func gramUnit() -> Self! ``` |
| To | ``` class func gramUnit() -> Self ``` |

Modified [HKUnit.gramUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615164-gramunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func gramUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.hourUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615214-hourunit)

|  | Declaration |
| --- | --- |
| From | ``` class func hourUnit() -> Self! ``` |
| To | ``` class func hourUnit() -> Self ``` |

Modified [HKUnit.inchUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615144-inch)

|  | Declaration |
| --- | --- |
| From | ``` class func inchUnit() -> Self! ``` |
| To | ``` class func inchUnit() -> Self ``` |

Modified [HKUnit.init(fromEnergyFormatterUnit: NSEnergyFormatterUnit)](https://developer.apple.com/documentation/healthkit/hkunit/1615218-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit) ``` |
| To | ``` convenience init(fromEnergyFormatterUnit energyFormatterUnit: NSEnergyFormatterUnit) ``` |

Modified [HKUnit.init(fromLengthFormatterUnit: NSLengthFormatterUnit)](https://developer.apple.com/documentation/healthkit/hkunit/1615057-unitfromlengthformatterunit)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit) ``` |
| To | ``` convenience init(fromLengthFormatterUnit lengthFormatterUnit: NSLengthFormatterUnit) ``` |

Modified [HKUnit.init(fromMassFormatterUnit: NSMassFormatterUnit)](https://developer.apple.com/documentation/healthkit/hkunit/1615182-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit) ``` |
| To | ``` convenience init(fromMassFormatterUnit massFormatterUnit: NSMassFormatterUnit) ``` |

Modified [HKUnit.init(fromString: String)](https://developer.apple.com/documentation/healthkit/hkunit/1615733-unitfromstring)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(fromString string: String!) ``` |
| To | ``` convenience init(fromString string: String) ``` |

Modified [HKUnit.jouleUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615640-jouleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func jouleUnit() -> Self! ``` |
| To | ``` class func jouleUnit() -> Self ``` |

Modified [HKUnit.jouleUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615248-jouleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func jouleUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.kelvinUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615289-kelvin)

|  | Declaration |
| --- | --- |
| From | ``` class func kelvinUnit() -> Self! ``` |
| To | ``` class func kelvinUnit() -> Self ``` |

Modified [HKUnit.kilocalorieUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615576-kilocalorieunit)

|  | Declaration |
| --- | --- |
| From | ``` class func kilocalorieUnit() -> Self! ``` |
| To | ``` class func kilocalorieUnit() -> Self ``` |

Modified [HKUnit.lengthFormatterUnitFromUnit(_: HKUnit) -> NSLengthFormatterUnit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615309-lengthformatterunit)

|  | Declaration |
| --- | --- |
| From | ``` class func lengthFormatterUnitFromUnit(_ unit: HKUnit!) -> NSLengthFormatterUnit ``` |
| To | ``` class func lengthFormatterUnitFromUnit(_ unit: HKUnit) -> NSLengthFormatterUnit ``` |

Modified [HKUnit.literUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615768-liter)

|  | Declaration |
| --- | --- |
| From | ``` class func literUnit() -> Self! ``` |
| To | ``` class func literUnit() -> Self ``` |

Modified [HKUnit.literUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615369-literunit)

|  | Declaration |
| --- | --- |
| From | ``` class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func literUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.massFormatterUnitFromUnit(_: HKUnit) -> NSMassFormatterUnit [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615100-massformatterunitfromunit)

|  | Declaration |
| --- | --- |
| From | ``` class func massFormatterUnitFromUnit(_ unit: HKUnit!) -> NSMassFormatterUnit ``` |
| To | ``` class func massFormatterUnitFromUnit(_ unit: HKUnit) -> NSMassFormatterUnit ``` |

Modified [HKUnit.meterUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615061-meter)

|  | Declaration |
| --- | --- |
| From | ``` class func meterUnit() -> Self! ``` |
| To | ``` class func meterUnit() -> Self ``` |

Modified [HKUnit.meterUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615489-meterunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func meterUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.mileUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615390-mileunit)

|  | Declaration |
| --- | --- |
| From | ``` class func mileUnit() -> Self! ``` |
| To | ``` class func mileUnit() -> Self ``` |

Modified [HKUnit.millimeterOfMercuryUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615410-millimeterofmercury)

|  | Declaration |
| --- | --- |
| From | ``` class func millimeterOfMercuryUnit() -> Self! ``` |
| To | ``` class func millimeterOfMercuryUnit() -> Self ``` |

Modified [HKUnit.minuteUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615362-minute)

|  | Declaration |
| --- | --- |
| From | ``` class func minuteUnit() -> Self! ``` |
| To | ``` class func minuteUnit() -> Self ``` |

Modified [HKUnit.moleUnitWithMetricPrefix(_: HKMetricPrefix, molarMass: Double) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615608-moleunit)

|  | Declaration |
| --- | --- |
| From | ``` class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self! ``` |
| To | ``` class func moleUnitWithMetricPrefix(_ prefix: HKMetricPrefix, molarMass gramsPerMole: Double) -> Self ``` |

Modified [HKUnit.moleUnitWithMolarMass(_: Double) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615515-moleunitwithmolarmass)

|  | Declaration |
| --- | --- |
| From | ``` class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self! ``` |
| To | ``` class func moleUnitWithMolarMass(_ gramsPerMole: Double) -> Self ``` |

Modified [HKUnit.ounceUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615118-ounceunit)

|  | Declaration |
| --- | --- |
| From | ``` class func ounceUnit() -> Self! ``` |
| To | ``` class func ounceUnit() -> Self ``` |

Modified [HKUnit.pascalUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615172-pascal)

|  | Declaration |
| --- | --- |
| From | ``` class func pascalUnit() -> Self! ``` |
| To | ``` class func pascalUnit() -> Self ``` |

Modified [HKUnit.pascalUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615168-pascalunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func pascalUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.percentUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615517-percent)

|  | Declaration |
| --- | --- |
| From | ``` class func percentUnit() -> Self! ``` |
| To | ``` class func percentUnit() -> Self ``` |

Modified [HKUnit.pintImperialUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615306-pintimperial)

|  | Declaration |
| --- | --- |
| From | ``` class func pintImperialUnit() -> Self! ``` |
| To | ``` class func pintImperialUnit() -> Self ``` |

Modified [HKUnit.pintUSUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615528-pintus)

|  | Declaration |
| --- | --- |
| From | ``` class func pintUSUnit() -> Self! ``` |
| To | ``` class func pintUSUnit() -> Self ``` |

Modified [HKUnit.poundUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615563-poundunit)

|  | Declaration |
| --- | --- |
| From | ``` class func poundUnit() -> Self! ``` |
| To | ``` class func poundUnit() -> Self ``` |

Modified [HKUnit.reciprocalUnit() -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615494-reciprocalunit)

|  | Declaration |
| --- | --- |
| From | ``` func reciprocalUnit() -> HKUnit! ``` |
| To | ``` func reciprocalUnit() -> HKUnit ``` |

Modified [HKUnit.secondUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615440-second)

|  | Declaration |
| --- | --- |
| From | ``` class func secondUnit() -> Self! ``` |
| To | ``` class func secondUnit() -> Self ``` |

Modified [HKUnit.secondUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615644-secondunit)

|  | Declaration |
| --- | --- |
| From | ``` class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func secondUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.siemenUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615703-siemen)

|  | Declaration |
| --- | --- |
| From | ``` class func siemenUnit() -> Self! ``` |
| To | ``` class func siemenUnit() -> Self ``` |

Modified [HKUnit.siemenUnitWithMetricPrefix(_: HKMetricPrefix) -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615648-siemenunitwithmetricprefix)

|  | Declaration |
| --- | --- |
| From | ``` class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self! ``` |
| To | ``` class func siemenUnitWithMetricPrefix(_ prefix: HKMetricPrefix) -> Self ``` |

Modified [HKUnit.stoneUnit() -> Self [class]](https://developer.apple.com/documentation/healthkit/hkunit/1615318-stoneunit)

|  | Declaration |
| --- | --- |
| From | ``` class func stoneUnit() -> Self! ``` |
| To | ``` class func stoneUnit() -> Self ``` |

Modified [HKUnit.unitDividedByUnit(_: HKUnit) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615242-unitdividedbyunit)

|  | Declaration |
| --- | --- |
| From | ``` func unitDividedByUnit(_ unit: HKUnit!) -> HKUnit! ``` |
| To | ``` func unitDividedByUnit(_ unit: HKUnit) -> HKUnit ``` |

Modified [HKUnit.unitMultipliedByUnit(_: HKUnit) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615718-unitmultiplied)

|  | Declaration |
| --- | --- |
| From | ``` func unitMultipliedByUnit(_ unit: HKUnit!) -> HKUnit! ``` |
| To | ``` func unitMultipliedByUnit(_ unit: HKUnit) -> HKUnit ``` |

Modified [HKUnit.unitRaisedToPower(_: Int) -> HKUnit](https://developer.apple.com/documentation/healthkit/hkunit/1615495-unitraised)

|  | Declaration |
| --- | --- |
| From | ``` func unitRaisedToPower(_ power: Int) -> HKUnit! ``` |
| To | ``` func unitRaisedToPower(_ power: Int) -> HKUnit ``` |

Modified [HKUnit.unitString](https://developer.apple.com/documentation/healthkit/hkunit/1615499-unitstring)

|  | Declaration |
| --- | --- |
| From | ``` var unitString: String! { get } ``` |
| To | ``` var unitString: String { get } ``` |

Modified [HKUpdateFrequency [enum]](https://developer.apple.com/documentation/healthkit/hkupdatefrequency)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HKWorkout](https://developer.apple.com/documentation/healthkit/hkworkout)

|  | Declaration |
| --- | --- |
| From | ``` class HKWorkout : HKSample {     var workoutActivityType: HKWorkoutActivityType { get }     var workoutEvents: [AnyObject]! { get }     var duration: NSTimeInterval { get }     var totalEnergyBurned: HKQuantity! { get }     var totalDistance: HKQuantity! { get }     convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!) -> Self!     convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, workoutEvents workoutEvents: [AnyObject]!, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, workoutEvents workoutEvents: [AnyObject]!, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) -> Self!     convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) -> Self! } ``` |
| To | ``` class HKWorkout : HKSample {     var workoutActivityType: HKWorkoutActivityType { get }     var workoutEvents: [HKWorkoutEvent]? { get }     var duration: NSTimeInterval { get }     var totalEnergyBurned: HKQuantity? { get }     var totalDistance: HKQuantity? { get }     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) -> Self     convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?)     class func workoutWithActivityType(_ workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, device device: HKDevice?, metadata metadata: [String : AnyObject]?) -> Self } ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate, endDate: NSDate)](https://developer.apple.com/documentation/healthkit/hkworkout/1615340-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate, endDate: NSDate, duration: NSTimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615739-workoutwithactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, duration duration: NSTimeInterval, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) ``` |

Modified [HKWorkout.init(activityType: HKWorkoutActivityType, startDate: NSDate, endDate: NSDate, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : AnyObject]?)](https://developer.apple.com/documentation/healthkit/hkworkout/1615212-init)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate!, endDate endDate: NSDate!, workoutEvents workoutEvents: [AnyObject]!, totalEnergyBurned totalEnergyBurned: HKQuantity!, totalDistance totalDistance: HKQuantity!, metadata metadata: [NSObject : AnyObject]!) ``` |
| To | ``` convenience init(activityType workoutActivityType: HKWorkoutActivityType, startDate startDate: NSDate, endDate endDate: NSDate, workoutEvents workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned totalEnergyBurned: HKQuantity?, totalDistance totalDistance: HKQuantity?, metadata metadata: [String : AnyObject]?) ``` |

Modified [HKWorkout.totalDistance](https://developer.apple.com/documentation/healthkit/hkworkout/1615756-totaldistance)

|  | Declaration |
| --- | --- |
| From | ``` var totalDistance: HKQuantity! { get } ``` |
| To | ``` var totalDistance: HKQuantity? { get } ``` |

Modified [HKWorkout.totalEnergyBurned](https://developer.apple.com/documentation/healthkit/hkworkout/1615491-totalenergyburned)

|  | Declaration |
| --- | --- |
| From | ``` var totalEnergyBurned: HKQuantity! { get } ``` |
| To | ``` var totalEnergyBurned: HKQuantity? { get } ``` |

Modified [HKWorkout.workoutEvents](https://developer.apple.com/documentation/healthkit/hkworkout/1615424-workoutevents)

|  | Declaration |
| --- | --- |
| From | ``` var workoutEvents: [AnyObject]! { get } ``` |
| To | ``` var workoutEvents: [HKWorkoutEvent]? { get } ``` |

Modified [HKWorkoutActivityType [enum]](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [HKWorkoutEvent](https://developer.apple.com/documentation/healthkit/hkworkoutevent)

|  | Declaration |
| --- | --- |
| From | ``` class HKWorkoutEvent : NSObject, NSSecureCoding, NSCoding {     var type: HKWorkoutEventType { get }     @NSCopying var date: NSDate! { get }     convenience init!(type type: HKWorkoutEventType, date date: NSDate!)     class func workoutEventWithType(_ type: HKWorkoutEventType, date date: NSDate!) -> Self!     init!() } ``` |
| To | ``` class HKWorkoutEvent : NSObject, NSSecureCoding, NSCoding {     var type: HKWorkoutEventType { get }     @NSCopying var date: NSDate { get }     convenience init(type type: HKWorkoutEventType, date date: NSDate)     class func workoutEventWithType(_ type: HKWorkoutEventType, date date: NSDate) -> Self     init() } ``` |

Modified [HKWorkoutEvent.date](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1615392-date)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var date: NSDate! { get } ``` |
| To | ``` @NSCopying var date: NSDate { get } ``` |

Modified [HKWorkoutEvent.init(type: HKWorkoutEventType, date: NSDate)](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1615600-workouteventwithtype)

|  | Declaration |
| --- | --- |
| From | ``` convenience init!(type type: HKWorkoutEventType, date date: NSDate!) ``` |
| To | ``` convenience init(type type: HKWorkoutEventType, date date: NSDate) ``` |

Modified [HKWorkoutEventType [enum]](https://developer.apple.com/documentation/healthkit/hkworkouteventtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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

---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/HomeKit.html
archived_at: '2026-07-18T02:56:52.225739Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# HomeKit Changes for Swift

### HomeKit

Added [HMAccessory.category](https://developer.apple.com/documentation/homekit/hmaccessory/1615275-category)Added [HMAccessory.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaccessory/1615261-uniqueidentifier)Added [HMAccessory.uniqueIdentifiersForBridgedAccessories](https://developer.apple.com/documentation/homekit/hmaccessory/1615278-uniqueidentifiersforbridgedacces)Added [HMAccessoryCategory](https://developer.apple.com/documentation/homekit/hmaccessorycategory)Added [HMAccessoryCategory.categoryType](https://developer.apple.com/documentation/homekit/hmaccessorycategory/1619926-categorytype)Added [HMAccessoryCategory.localizedDescription](https://developer.apple.com/documentation/homekit/hmaccessorycategory/1619924-localizeddescription)Added [HMAction.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaction/1624923-uniqueidentifier)Added [HMActionSet.actionSetType](https://developer.apple.com/documentation/homekit/hmactionset/1616794-actionsettype)Added [HMActionSet.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmactionset/1616789-uniqueidentifier)Added [HMCharacteristic.localizedDescription](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624185-localizeddescription)Added [HMCharacteristic.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624187-uniqueidentifier)Added [HMCharacteristicEvent](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)Added [HMCharacteristicEvent.characteristic](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617203-characteristic)Added [HMCharacteristicEvent.init(characteristic: HMCharacteristic, triggerValue: NSCopying?)](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617201-initwithcharacteristic)Added [HMCharacteristicEvent.triggerValue](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617200-triggervalue)Added [HMCharacteristicEvent.updateTriggerValue(_: NSCopying?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617202-updatetriggervalue)Added [HMCharacteristicValueAirParticulateSize [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize)Added [HMCharacteristicValueAirParticulateSize.Size10](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/size10)Added [HMCharacteristicValueAirParticulateSize.Size2_5](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/hmcharacteristicvalueairparticulatesize2_5)Added [HMCharacteristicValueAirQuality [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality)Added [HMCharacteristicValueAirQuality.Excellent](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/excellent)Added [HMCharacteristicValueAirQuality.Fair](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualityfair)Added [HMCharacteristicValueAirQuality.Good](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/good)Added [HMCharacteristicValueAirQuality.Inferior](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualityinferior)Added [HMCharacteristicValueAirQuality.Poor](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/poor)Added [HMCharacteristicValueAirQuality.Unknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/unknown)Added [HMCharacteristicValueCurrentSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate)Added [HMCharacteristicValueCurrentSecuritySystemState.AwayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstateawayarm)Added [HMCharacteristicValueCurrentSecuritySystemState.Disarmed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/disarmed)Added [HMCharacteristicValueCurrentSecuritySystemState.NightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/nightarm)Added [HMCharacteristicValueCurrentSecuritySystemState.StayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstatestayarm)Added [HMCharacteristicValueCurrentSecuritySystemState.Triggered](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/triggered)Added [HMCharacteristicValuePositionState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate)Added [HMCharacteristicValuePositionState.Closing](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstateclosing)Added [HMCharacteristicValuePositionState.Opening](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/opening)Added [HMCharacteristicValuePositionState.Stopped](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstatestopped)Added [HMCharacteristicValueTargetSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate)Added [HMCharacteristicValueTargetSecuritySystemState.AwayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/awayarm)Added [HMCharacteristicValueTargetSecuritySystemState.Disarm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatedisarm)Added [HMCharacteristicValueTargetSecuritySystemState.NightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatenightarm)Added [HMCharacteristicValueTargetSecuritySystemState.StayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatestayarm)Added [HMErrorCode.CannotRemoveBuiltinActionSet](https://developer.apple.com/documentation/homekit/hmerror/code/cannotremovebuiltinactionset)Added [HMErrorCode.LocationForHomeDisabled](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodelocationforhomedisabled)Added [HMErrorCode.NotAuthorizedForLocationServices](https://developer.apple.com/documentation/homekit/hmerror/code/notauthorizedforlocationservices)Added [HMEvent](https://developer.apple.com/documentation/homekit/hmevent)Added [HMEvent.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmevent/1619881-uniqueidentifier)Added [HMEventTrigger](https://developer.apple.com/documentation/homekit/hmeventtrigger)Added [HMEventTrigger.addEvent(_: HMEvent, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624416-addevent)Added [HMEventTrigger.events](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624413-events)Added [HMEventTrigger.init(name: String, events: [HMEvent], predicate: NSPredicate?)](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624402-initwithname)Added [HMEventTrigger.predicate](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624405-predicate)Added [HMEventTrigger.predicateForEvaluatingTriggerOccurringAfterDateWithComponents(_: NSDateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624414-predicateforevaluatingtriggerocc)Added [HMEventTrigger.predicateForEvaluatingTriggerOccurringAfterSignificantEvent(_: String, applyingOffset: NSDateComponents?) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624406-predicateforevaluatingtriggerocc)Added [HMEventTrigger.predicateForEvaluatingTriggerOccurringBeforeDateWithComponents(_: NSDateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624408-predicateforevaluatingtriggerocc)Added [HMEventTrigger.predicateForEvaluatingTriggerOccurringBeforeSignificantEvent(_: String, applyingOffset: NSDateComponents?) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624401-predicateforevaluatingtrigger)Added [HMEventTrigger.predicateForEvaluatingTriggerOccurringOnDateWithComponents(_: NSDateComponents) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624407-predicateforevaluatingtriggerocc)Added [HMEventTrigger.predicateForEvaluatingTriggerWithCharacteristic(_: HMCharacteristic, relatedBy: NSPredicateOperatorType, toValue: AnyObject) -> NSPredicate [class]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624409-predicateforevaluatingtrigger)Added [HMEventTrigger.removeEvent(_: HMEvent, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624403-removeevent)Added [HMEventTrigger.updatePredicate(_: NSPredicate?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624411-updatepredicate)Added [HMHome.builtinActionSetOfType(_: String) -> HMActionSet?](https://developer.apple.com/documentation/homekit/hmhome/1620238-builtinactionsetoftype)Added [HMHome.currentUser](https://developer.apple.com/documentation/homekit/hmhome/1620255-currentuser)Added [HMHome.homeAccessControlForUser(_: HMUser) -> HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhome/1620214-homeaccesscontrolforuser)Added [HMHome.manageUsersWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620268-manageuserswithcompletionhandler)Added [HMHome.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmhome/1620243-uniqueidentifier)Added [HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)Added [HMHomeAccessControl.administrator](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol/1624331-administrator)Added [HMLocationEvent](https://developer.apple.com/documentation/homekit/hmlocationevent)Added [HMLocationEvent.init(region: CLRegion)](https://developer.apple.com/documentation/homekit/hmlocationevent/1624981-initwithregion)Added [HMLocationEvent.region](https://developer.apple.com/documentation/homekit/hmlocationevent/1624980-region)Added [HMLocationEvent.updateRegion(_: CLRegion, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmlocationevent/1624982-updateregion)Added [HMRoom.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmroom/1618291-uniqueidentifier)Added [HMService.localizedDescription](https://developer.apple.com/documentation/homekit/hmservice/1615890-localizeddescription)Added [HMService.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservice/1615883-uniqueidentifier)Added [HMService.userInteractive](https://developer.apple.com/documentation/homekit/hmservice/1615891-userinteractive)Added [HMServiceGroup.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservicegroup/1616991-uniqueidentifier)Added [HMTrigger.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmtrigger/1620720-uniqueidentifier)Added [HMUser.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmuser/1620013-uniqueidentifier)Added [HMZone.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmzone/1624766-uniqueidentifier)Added [HMAccessoryCategoryTypeBridge](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypebridge)Added [HMAccessoryCategoryTypeDoor](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypedoor)Added [HMAccessoryCategoryTypeDoorLock](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypedoorlock)Added [HMAccessoryCategoryTypeFan](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypefan)Added [HMAccessoryCategoryTypeGarageDoorOpener](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypegaragedooropener)Added [HMAccessoryCategoryTypeLightbulb](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypelightbulb)Added [HMAccessoryCategoryTypeOther](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeother)Added [HMAccessoryCategoryTypeOutlet](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeoutlet)Added [HMAccessoryCategoryTypeProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeprogrammableswitch)Added [HMAccessoryCategoryTypeSecuritySystem](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypesecuritysystem)Added [HMAccessoryCategoryTypeSensor](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypesensor)Added [HMAccessoryCategoryTypeSwitch](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeswitch)Added [HMAccessoryCategoryTypeThermostat](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypethermostat)Added [HMAccessoryCategoryTypeWindow](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypewindow)Added [HMAccessoryCategoryTypeWindowCovering](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypewindowcovering)Added [HMActionSetTypeHomeArrival](https://developer.apple.com/documentation/homekit/hmactionsettypehomearrival)Added [HMActionSetTypeHomeDeparture](https://developer.apple.com/documentation/homekit/hmactionsettypehomedeparture)Added [HMActionSetTypeSleep](https://developer.apple.com/documentation/homekit/hmactionsettypesleep)Added [HMActionSetTypeUserDefined](https://developer.apple.com/documentation/homekit/hmactionsettypeuserdefined)Added [HMActionSetTypeWakeUp](https://developer.apple.com/documentation/homekit/hmactionsettypewakeup)Added [HMCharacteristicKeyPath](https://developer.apple.com/documentation/homekit/hmcharacteristickeypath)Added [HMCharacteristicTypeAirParticulateDensity](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairparticulatedensity)Added [HMCharacteristicTypeAirParticulateSize](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairparticulatesize)Added [HMCharacteristicTypeAirQuality](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairquality)Added [HMCharacteristicTypeBatteryLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypebatterylevel)Added [HMCharacteristicTypeCarbonDioxideDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidedetected)Added [HMCharacteristicTypeCarbonDioxideLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidelevel)Added [HMCharacteristicTypeCarbonDioxidePeakLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidepeaklevel)Added [HMCharacteristicTypeCarbonMonoxideDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidedetected)Added [HMCharacteristicTypeCarbonMonoxideLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidelevel)Added [HMCharacteristicTypeCarbonMonoxidePeakLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidepeaklevel)Added [HMCharacteristicTypeChargingState](https://developer.apple.com/documentation/homekit/hmcharacteristictypechargingstate)Added [HMCharacteristicTypeContactState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecontactstate)Added [HMCharacteristicTypeCurrentHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrenthorizontaltilt)Added [HMCharacteristicTypeCurrentLightLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentlightlevel)Added [HMCharacteristicTypeCurrentPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentposition)Added [HMCharacteristicTypeCurrentSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentsecuritysystemstate)Added [HMCharacteristicTypeCurrentVerticalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentverticaltilt)Added [HMCharacteristicTypeFirmwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypefirmwareversion)Added [HMCharacteristicTypeHardwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypehardwareversion)Added [HMCharacteristicTypeHoldPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypeholdposition)Added [HMCharacteristicTypeInputEvent](https://developer.apple.com/documentation/homekit/hmcharacteristictypeinputevent)Added [HMCharacteristicTypeLeakDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeleakdetected)Added [HMCharacteristicTypeOccupancyDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoccupancydetected)Added [HMCharacteristicTypeOutputState](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoutputstate)Added [HMCharacteristicTypePositionState](https://developer.apple.com/documentation/homekit/hmcharacteristictypepositionstate)Added [HMCharacteristicTypeSecuritySystemAlarmType](https://developer.apple.com/documentation/homekit/hmcharacteristictypesecuritysystemalarmtype)Added [HMCharacteristicTypeSmokeDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypesmokedetected)Added [HMCharacteristicTypeSoftwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypesoftwareversion)Added [HMCharacteristicTypeStatusActive](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusactive)Added [HMCharacteristicTypeStatusFault](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusfault)Added [HMCharacteristicTypeStatusJammed](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusjammed)Added [HMCharacteristicTypeStatusLowBattery](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatuslowbattery)Added [HMCharacteristicTypeStatusTampered](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatustampered)Added [HMCharacteristicTypeTargetHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargethorizontaltilt)Added [HMCharacteristicTypeTargetPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetposition)Added [HMCharacteristicTypeTargetSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetsecuritysystemstate)Added [HMCharacteristicTypeTargetVerticalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetverticaltilt)Added [HMCharacteristicValueKeyPath](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluekeypath)Added [HMServiceTypeAirQualitySensor](https://developer.apple.com/documentation/homekit/hmservicetypeairqualitysensor)Added [HMServiceTypeBattery](https://developer.apple.com/documentation/homekit/hmservicetypebattery)Added [HMServiceTypeCarbonDioxideSensor](https://developer.apple.com/documentation/homekit/hmservicetypecarbondioxidesensor)Added [HMServiceTypeCarbonMonoxideSensor](https://developer.apple.com/documentation/homekit/hmservicetypecarbonmonoxidesensor)Added [HMServiceTypeContactSensor](https://developer.apple.com/documentation/homekit/hmservicetypecontactsensor)Added [HMServiceTypeDoor](https://developer.apple.com/documentation/homekit/hmservicetypedoor)Added [HMServiceTypeHumiditySensor](https://developer.apple.com/documentation/homekit/hmservicetypehumiditysensor)Added [HMServiceTypeLeakSensor](https://developer.apple.com/documentation/homekit/hmservicetypeleaksensor)Added [HMServiceTypeLightSensor](https://developer.apple.com/documentation/homekit/hmservicetypelightsensor)Added [HMServiceTypeMotionSensor](https://developer.apple.com/documentation/homekit/hmservicetypemotionsensor)Added [HMServiceTypeOccupancySensor](https://developer.apple.com/documentation/homekit/hmservicetypeoccupancysensor)Added [HMServiceTypeSecuritySystem](https://developer.apple.com/documentation/homekit/hmservicetypesecuritysystem)Added [HMServiceTypeSmokeSensor](https://developer.apple.com/documentation/homekit/hmservicetypesmokesensor)Added [HMServiceTypeStatefulProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmservicetypestatefulprogrammableswitch)Added [HMServiceTypeStatelessProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmservicetypestatelessprogrammableswitch)Added [HMServiceTypeTemperatureSensor](https://developer.apple.com/documentation/homekit/hmservicetypetemperaturesensor)Added [HMServiceTypeWindow](https://developer.apple.com/documentation/homekit/hmservicetypewindow)Added [HMServiceTypeWindowCovering](https://developer.apple.com/documentation/homekit/hmservicetypewindowcovering)Added [HMSignificantEventSunrise](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624412-sunrise)Added [HMSignificantEventSunset](https://developer.apple.com/documentation/homekit/hmsignificanteventsunset)Modified [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory)

|  | Declaration |
| --- | --- |
| From | ``` class HMAccessory : NSObject {     var name: String! { get }     @NSCopying var identifier: NSUUID! { get }     weak var delegate: HMAccessoryDelegate?     var reachable: Bool { get }     var bridged: Bool { get }     var identifiersForBridgedAccessories: [AnyObject]! { get }     weak var room: HMRoom! { get }     var services: [AnyObject]! { get }     var blocked: Bool { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func identifyWithCompletionHandler(_ completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMAccessory : NSObject {     var name: String { get }     @NSCopying var identifier: NSUUID { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     weak var delegate: HMAccessoryDelegate?     var reachable: Bool { get }     var bridged: Bool { get }     var identifiersForBridgedAccessories: [NSUUID]? { get }     var uniqueIdentifiersForBridgedAccessories: [NSUUID]? { get }     var category: HMAccessoryCategory { get }     weak var room: HMRoom? { get }     var services: [HMService] { get }     var blocked: Bool { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func identifyWithCompletionHandler(_ completion: (NSError?) -> Void) } ``` |

Modified [HMAccessory.identifier](https://developer.apple.com/documentation/homekit/hmaccessory/1615284-identifier)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @NSCopying var identifier: NSUUID! { get } ``` | -- |
| To | ``` @NSCopying var identifier: NSUUID { get } ``` | iOS 9.0 |

Modified [HMAccessory.identifiersForBridgedAccessories](https://developer.apple.com/documentation/homekit/hmaccessory/1615265-identifiersforbridgedaccessories)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var identifiersForBridgedAccessories: [AnyObject]! { get } ``` | -- |
| To | ``` var identifiersForBridgedAccessories: [NSUUID]? { get } ``` | iOS 9.0 |

Modified [HMAccessory.identifyWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmaccessory/1615259-identify)

|  | Declaration |
| --- | --- |
| From | ``` func identifyWithCompletionHandler(_ completion: ((NSError!) -> Void)!) ``` |
| To | ``` func identifyWithCompletionHandler(_ completion: (NSError?) -> Void) ``` |

Modified [HMAccessory.name](https://developer.apple.com/documentation/homekit/hmaccessory/1615253-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMAccessory.room](https://developer.apple.com/documentation/homekit/hmaccessory/1615282-room)

|  | Declaration |
| --- | --- |
| From | ``` weak var room: HMRoom! { get } ``` |
| To | ``` weak var room: HMRoom? { get } ``` |

Modified [HMAccessory.services](https://developer.apple.com/documentation/homekit/hmaccessory/1615250-services)

|  | Declaration |
| --- | --- |
| From | ``` var services: [AnyObject]! { get } ``` |
| To | ``` var services: [HMService] { get } ``` |

Modified [HMAccessory.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmaccessory/1615277-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMAccessoryBrowser](https://developer.apple.com/documentation/homekit/hmaccessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` class HMAccessoryBrowser : NSObject {     weak var delegate: HMAccessoryBrowserDelegate?     var discoveredAccessories: [AnyObject]! { get }     func startSearchingForNewAccessories()     func stopSearchingForNewAccessories() } ``` |
| To | ``` class HMAccessoryBrowser : NSObject {     weak var delegate: HMAccessoryBrowserDelegate?     var discoveredAccessories: [HMAccessory] { get }     func startSearchingForNewAccessories()     func stopSearchingForNewAccessories() } ``` |

Modified [HMAccessoryBrowser.discoveredAccessories](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/1622406-discoveredaccessories)

|  | Declaration |
| --- | --- |
| From | ``` var discoveredAccessories: [AnyObject]! { get } ``` |
| To | ``` var discoveredAccessories: [HMAccessory] { get } ``` |

Modified [HMAccessoryBrowserDelegate](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMAccessoryBrowserDelegate : NSObjectProtocol {     optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory!)     optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory!) } ``` |
| To | ``` protocol HMAccessoryBrowserDelegate : NSObjectProtocol {     optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory)     optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory) } ``` |

Modified [HMAccessoryBrowserDelegate.accessoryBrowser(_: HMAccessoryBrowser, didFindNewAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/1622402-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory) ``` |

Modified [HMAccessoryBrowserDelegate.accessoryBrowser(_: HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmaccessorybrowserdelegate/1622407-accessorybrowser)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory) ``` |

Modified [HMAccessoryDelegate](https://developer.apple.com/documentation/homekit/hmaccessorydelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidUpdateName(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService!)     optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService!)     optional func accessoryDidUpdateServices(_ accessory: HMAccessory)     optional func accessoryDidUpdateReachability(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, service service: HMService!, didUpdateValueForCharacteristic characteristic: HMCharacteristic!) } ``` |
| To | ``` protocol HMAccessoryDelegate : NSObjectProtocol {     optional func accessoryDidUpdateName(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService)     optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService)     optional func accessoryDidUpdateServices(_ accessory: HMAccessory)     optional func accessoryDidUpdateReachability(_ accessory: HMAccessory)     optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueForCharacteristic characteristic: HMCharacteristic) } ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, didUpdateAssociatedServiceTypeForService: HMService)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615267-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService!) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService) ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, didUpdateNameForService: HMService)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615263-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService!) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService) ``` |

Modified [HMAccessoryDelegate.accessory(_: HMAccessory, service: HMService, didUpdateValueForCharacteristic: HMCharacteristic)](https://developer.apple.com/documentation/homekit/hmaccessorydelegate/1615286-accessory)

|  | Declaration |
| --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory, service service: HMService!, didUpdateValueForCharacteristic characteristic: HMCharacteristic!) ``` |
| To | ``` optional func accessory(_ accessory: HMAccessory, service service: HMService, didUpdateValueForCharacteristic characteristic: HMCharacteristic) ``` |

Modified [HMAction](https://developer.apple.com/documentation/homekit/hmaction)

|  | Declaration |
| --- | --- |
| From | ``` class HMAction : NSObject { } ``` |
| To | ``` class HMAction : NSObject {     @NSCopying var uniqueIdentifier: NSUUID { get } } ``` |

Modified [HMActionSet](https://developer.apple.com/documentation/homekit/hmactionset)

|  | Declaration |
| --- | --- |
| From | ``` class HMActionSet : NSObject {     init!()     var name: String! { get }     var actions: Set<NSObject>! { get }     var executing: Bool { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func addAction(_ action: HMAction!, completionHandler completion: ((NSError!) -> Void)!)     func removeAction(_ action: HMAction!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMActionSet : NSObject {     init()     var name: String { get }     var actions: Set<HMAction> { get }     var executing: Bool { get }     var actionSetType: String { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void)     func removeAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMActionSet.actions](https://developer.apple.com/documentation/homekit/hmactionset/1616790-actions)

|  | Declaration |
| --- | --- |
| From | ``` var actions: Set<NSObject>! { get } ``` |
| To | ``` var actions: Set<HMAction> { get } ``` |

Modified [HMActionSet.addAction(_: HMAction, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmactionset/1616798-addaction)

|  | Declaration |
| --- | --- |
| From | ``` func addAction(_ action: HMAction!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMActionSet.name](https://developer.apple.com/documentation/homekit/hmactionset/1616795-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMActionSet.removeAction(_: HMAction, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmactionset/1616787-removeaction)

|  | Declaration |
| --- | --- |
| From | ``` func removeAction(_ action: HMAction!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeAction(_ action: HMAction, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMActionSet.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmactionset/1616797-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` class HMCharacteristic : NSObject {     var characteristicType: String! { get }     weak var service: HMService! { get }     var properties: [AnyObject]! { get }     var metadata: HMCharacteristicMetadata! { get }     @NSCopying var value: AnyObject! { get }     var notificationEnabled: Bool { get }     func writeValue(_ value: AnyObject!, completionHandler completion: ((NSError!) -> Void)!)     func readValueWithCompletionHandler(_ completion: ((NSError!) -> Void)!)     func enableNotification(_ enable: Bool, completionHandler completion: ((NSError!) -> Void)!)     func updateAuthorizationData(_ data: NSData!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMCharacteristic : NSObject {     var characteristicType: String { get }     var localizedDescription: String { get }     weak var service: HMService? { get }     var properties: [String] { get }     var metadata: HMCharacteristicMetadata? { get }     @NSCopying var value: AnyObject? { get }     var notificationEnabled: Bool { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func writeValue(_ value: AnyObject?, completionHandler completion: (NSError?) -> Void)     func readValueWithCompletionHandler(_ completion: (NSError?) -> Void)     func enableNotification(_ enable: Bool, completionHandler completion: (NSError?) -> Void)     func updateAuthorizationData(_ data: NSData?, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMCharacteristic.characteristicType](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624197-characteristictype)

|  | Declaration |
| --- | --- |
| From | ``` var characteristicType: String! { get } ``` |
| To | ``` var characteristicType: String { get } ``` |

Modified [HMCharacteristic.enableNotification(_: Bool, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624189-enablenotification)

|  | Declaration |
| --- | --- |
| From | ``` func enableNotification(_ enable: Bool, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func enableNotification(_ enable: Bool, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMCharacteristic.metadata](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624196-metadata)

|  | Declaration |
| --- | --- |
| From | ``` var metadata: HMCharacteristicMetadata! { get } ``` |
| To | ``` var metadata: HMCharacteristicMetadata? { get } ``` |

Modified [HMCharacteristic.properties](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624186-properties)

|  | Declaration |
| --- | --- |
| From | ``` var properties: [AnyObject]! { get } ``` |
| To | ``` var properties: [String] { get } ``` |

Modified [HMCharacteristic.readValueWithCompletionHandler(_: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624188-readvaluewithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func readValueWithCompletionHandler(_ completion: ((NSError!) -> Void)!) ``` |
| To | ``` func readValueWithCompletionHandler(_ completion: (NSError?) -> Void) ``` |

Modified [HMCharacteristic.service](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624184-service)

|  | Declaration |
| --- | --- |
| From | ``` weak var service: HMService! { get } ``` |
| To | ``` weak var service: HMService? { get } ``` |

Modified [HMCharacteristic.updateAuthorizationData(_: NSData?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624193-updateauthorizationdata)

|  | Declaration |
| --- | --- |
| From | ``` func updateAuthorizationData(_ data: NSData!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateAuthorizationData(_ data: NSData?, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMCharacteristic.value](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624195-value)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var value: AnyObject! { get } ``` |
| To | ``` @NSCopying var value: AnyObject? { get } ``` |

Modified [HMCharacteristic.writeValue(_: AnyObject?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624191-writevalue)

|  | Declaration |
| --- | --- |
| From | ``` func writeValue(_ value: AnyObject!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func writeValue(_ value: AnyObject?, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMCharacteristicMetadata](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata)

|  | Declaration |
| --- | --- |
| From | ``` class HMCharacteristicMetadata : NSObject {     var minimumValue: NSNumber! { get }     var maximumValue: NSNumber! { get }     var stepValue: NSNumber! { get }     var maxLength: NSNumber! { get }     var format: String! { get }     var units: String! { get }     var manufacturerDescription: String! { get } } ``` |
| To | ``` class HMCharacteristicMetadata : NSObject {     var minimumValue: NSNumber? { get }     var maximumValue: NSNumber? { get }     var stepValue: NSNumber? { get }     var maxLength: NSNumber? { get }     var format: String? { get }     var units: String? { get }     var manufacturerDescription: String? { get } } ``` |

Modified [HMCharacteristicMetadata.format](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621266-format)

|  | Declaration |
| --- | --- |
| From | ``` var format: String! { get } ``` |
| To | ``` var format: String? { get } ``` |

Modified [HMCharacteristicMetadata.manufacturerDescription](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621247-manufacturerdescription)

|  | Declaration |
| --- | --- |
| From | ``` var manufacturerDescription: String! { get } ``` |
| To | ``` var manufacturerDescription: String? { get } ``` |

Modified [HMCharacteristicMetadata.maximumValue](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621261-maximumvalue)

|  | Declaration |
| --- | --- |
| From | ``` var maximumValue: NSNumber! { get } ``` |
| To | ``` var maximumValue: NSNumber? { get } ``` |

Modified [HMCharacteristicMetadata.maxLength](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621258-maxlength)

|  | Declaration |
| --- | --- |
| From | ``` var maxLength: NSNumber! { get } ``` |
| To | ``` var maxLength: NSNumber? { get } ``` |

Modified [HMCharacteristicMetadata.minimumValue](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621256-minimumvalue)

|  | Declaration |
| --- | --- |
| From | ``` var minimumValue: NSNumber! { get } ``` |
| To | ``` var minimumValue: NSNumber? { get } ``` |

Modified [HMCharacteristicMetadata.stepValue](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621263-stepvalue)

|  | Declaration |
| --- | --- |
| From | ``` var stepValue: NSNumber! { get } ``` |
| To | ``` var stepValue: NSNumber? { get } ``` |

Modified [HMCharacteristicMetadata.units](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata/1621253-units)

|  | Declaration |
| --- | --- |
| From | ``` var units: String! { get } ``` |
| To | ``` var units: String? { get } ``` |

Modified [HMCharacteristicValueDoorState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicValueHeatingCooling [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicValueLockMechanismLastKnownAction [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicValueLockMechanismState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicValueRotationDirection [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluerotationdirection)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicValueTemperatureUnit [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetemperatureunit)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction)

|  | Declaration |
| --- | --- |
| From | ``` class HMCharacteristicWriteAction : HMAction {     convenience init!()     init!(characteristic characteristic: HMCharacteristic!, targetValue targetValue: AnyObject!)     var characteristic: HMCharacteristic! { get }     @NSCopying var targetValue: AnyObject! { get }     func updateTargetValue(_ targetValue: AnyObject!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMCharacteristicWriteAction : HMAction {     convenience init()     init(characteristic characteristic: HMCharacteristic, targetValue targetValue: NSCopying)     var characteristic: HMCharacteristic { get }     @NSCopying var targetValue: NSCopying { get }     func updateTargetValue(_ targetValue: NSCopying, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMCharacteristicWriteAction.characteristic](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621974-characteristic)

|  | Declaration |
| --- | --- |
| From | ``` var characteristic: HMCharacteristic! { get } ``` |
| To | ``` var characteristic: HMCharacteristic { get } ``` |

Modified [HMCharacteristicWriteAction.init(characteristic: HMCharacteristic, targetValue: NSCopying)](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621976-initwithcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` init!(characteristic characteristic: HMCharacteristic!, targetValue targetValue: AnyObject!) ``` |
| To | ``` init(characteristic characteristic: HMCharacteristic, targetValue targetValue: NSCopying) ``` |

Modified [HMCharacteristicWriteAction.targetValue](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621973-targetvalue)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var targetValue: AnyObject! { get } ``` |
| To | ``` @NSCopying var targetValue: NSCopying { get } ``` |

Modified [HMCharacteristicWriteAction.updateTargetValue(_: NSCopying, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621972-updatetargetvalue)

|  | Declaration |
| --- | --- |
| From | ``` func updateTargetValue(_ targetValue: AnyObject!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateTargetValue(_ targetValue: NSCopying, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMErrorCode [enum]](https://developer.apple.com/documentation/homekit/hmerror/code)

|  | Declaration | Protocols | Introduction | Raw Value Type |
| --- | --- | --- | --- | --- |
| From | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked } ``` | Equatable, Hashable, RawRepresentable | iOS 8.1 | -- |
| To | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices } extension HMErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension HMErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | iOS 8.0 | Int |

Modified [HMHome](https://developer.apple.com/documentation/homekit/hmhome)

|  | Declaration |
| --- | --- |
| From | ``` class HMHome : NSObject {     init!()     weak var delegate: HMHomeDelegate?     var name: String! { get }     var primary: Bool { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var accessories: [AnyObject]! { get }     func addAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!)     func removeAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!)     func assignAccessory(_ accessory: HMAccessory!, toRoom room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!)     func servicesWithTypes(_ serviceTypes: [AnyObject]!) -> [AnyObject]!     func unblockAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var users: [AnyObject]! { get }     func addUserWithCompletionHandler(_ completion: ((HMUser!, NSError!) -> Void)!)     func removeUser(_ user: HMUser!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var rooms: [AnyObject]! { get }     func addRoomWithName(_ roomName: String!, completionHandler completion: ((HMRoom!, NSError!) -> Void)!)     func removeRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!)     func roomForEntireHome() -> HMRoom! } extension HMHome {     var zones: [AnyObject]! { get }     func addZoneWithName(_ zoneName: String!, completionHandler completion: ((HMZone!, NSError!) -> Void)!)     func removeZone(_ zone: HMZone!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var serviceGroups: [AnyObject]! { get }     func addServiceGroupWithName(_ serviceGroupName: String!, completionHandler completion: ((HMServiceGroup!, NSError!) -> Void)!)     func removeServiceGroup(_ group: HMServiceGroup!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var actionSets: [AnyObject]! { get }     func addActionSetWithName(_ actionSetName: String!, completionHandler completion: ((HMActionSet!, NSError!) -> Void)!)     func removeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!)     func executeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!) } extension HMHome {     var triggers: [AnyObject]! { get }     func addTrigger(_ trigger: HMTrigger!, completionHandler completion: ((NSError!) -> Void)!)     func removeTrigger(_ trigger: HMTrigger!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMHome : NSObject {     init()     weak var delegate: HMHomeDelegate?     var name: String { get }     var primary: Bool { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var accessories: [HMAccessory] { get }     func addAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void)     func removeAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void)     func assignAccessory(_ accessory: HMAccessory, toRoom room: HMRoom, completionHandler completion: (NSError?) -> Void)     func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]?     func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var currentUser: HMUser { get }     var users: [HMUser] { get }     func manageUsersWithCompletionHandler(_ completion: (NSError?) -> Void)     func addUserWithCompletionHandler(_ completion: (HMUser?, NSError?) -> Void)     func removeUser(_ user: HMUser, completionHandler completion: (NSError?) -> Void)     func homeAccessControlForUser(_ user: HMUser) -> HMHomeAccessControl } extension HMHome {     var rooms: [HMRoom] { get }     func addRoomWithName(_ roomName: String, completionHandler completion: (HMRoom?, NSError?) -> Void)     func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void)     func roomForEntireHome() -> HMRoom } extension HMHome {     var zones: [HMZone] { get }     func addZoneWithName(_ zoneName: String, completionHandler completion: (HMZone?, NSError?) -> Void)     func removeZone(_ zone: HMZone, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var serviceGroups: [HMServiceGroup] { get }     func addServiceGroupWithName(_ serviceGroupName: String, completionHandler completion: (HMServiceGroup?, NSError?) -> Void)     func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: (NSError?) -> Void) } extension HMHome {     var actionSets: [HMActionSet] { get }     func addActionSetWithName(_ actionSetName: String, completionHandler completion: (HMActionSet?, NSError?) -> Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func builtinActionSetOfType(_ actionSetType: String) -> HMActionSet? } extension HMHome {     var triggers: [HMTrigger] { get }     func addTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void)     func removeTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMHome.accessories](https://developer.apple.com/documentation/homekit/hmhome/1620275-accessories)

|  | Declaration |
| --- | --- |
| From | ``` var accessories: [AnyObject]! { get } ``` |
| To | ``` var accessories: [HMAccessory] { get } ``` |

Modified [HMHome.actionSets](https://developer.apple.com/documentation/homekit/hmhome/1620257-actionsets)

|  | Declaration |
| --- | --- |
| From | ``` var actionSets: [AnyObject]! { get } ``` |
| To | ``` var actionSets: [HMActionSet] { get } ``` |

Modified [HMHome.addAccessory(_: HMAccessory, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620216-addaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func addAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.addActionSetWithName(_: String, completionHandler: (HMActionSet?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620231-addactionsetwithname)

|  | Declaration |
| --- | --- |
| From | ``` func addActionSetWithName(_ actionSetName: String!, completionHandler completion: ((HMActionSet!, NSError!) -> Void)!) ``` |
| To | ``` func addActionSetWithName(_ actionSetName: String, completionHandler completion: (HMActionSet?, NSError?) -> Void) ``` |

Modified [HMHome.addRoomWithName(_: String, completionHandler: (HMRoom?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620236-addroomwithname)

|  | Declaration |
| --- | --- |
| From | ``` func addRoomWithName(_ roomName: String!, completionHandler completion: ((HMRoom!, NSError!) -> Void)!) ``` |
| To | ``` func addRoomWithName(_ roomName: String, completionHandler completion: (HMRoom?, NSError?) -> Void) ``` |

Modified [HMHome.addServiceGroupWithName(_: String, completionHandler: (HMServiceGroup?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620269-addservicegroup)

|  | Declaration |
| --- | --- |
| From | ``` func addServiceGroupWithName(_ serviceGroupName: String!, completionHandler completion: ((HMServiceGroup!, NSError!) -> Void)!) ``` |
| To | ``` func addServiceGroupWithName(_ serviceGroupName: String, completionHandler completion: (HMServiceGroup?, NSError?) -> Void) ``` |

Modified [HMHome.addTrigger(_: HMTrigger, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620271-addtrigger)

|  | Declaration |
| --- | --- |
| From | ``` func addTrigger(_ trigger: HMTrigger!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.addUserWithCompletionHandler(_: (HMUser?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620213-adduserwithcompletionhandler)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func addUserWithCompletionHandler(_ completion: ((HMUser!, NSError!) -> Void)!) ``` | -- |
| To | ``` func addUserWithCompletionHandler(_ completion: (HMUser?, NSError?) -> Void) ``` | iOS 9.0 |

Modified [HMHome.addZoneWithName(_: String, completionHandler: (HMZone?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620212-addzone)

|  | Declaration |
| --- | --- |
| From | ``` func addZoneWithName(_ zoneName: String!, completionHandler completion: ((HMZone!, NSError!) -> Void)!) ``` |
| To | ``` func addZoneWithName(_ zoneName: String, completionHandler completion: (HMZone?, NSError?) -> Void) ``` |

Modified [HMHome.assignAccessory(_: HMAccessory, toRoom: HMRoom, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620265-assignaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func assignAccessory(_ accessory: HMAccessory!, toRoom room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func assignAccessory(_ accessory: HMAccessory, toRoom room: HMRoom, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.executeActionSet(_: HMActionSet, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620256-executeactionset)

|  | Declaration |
| --- | --- |
| From | ``` func executeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func executeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.name](https://developer.apple.com/documentation/homekit/hmhome/1620250-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMHome.removeAccessory(_: HMAccessory, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620245-removeaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func removeAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.removeActionSet(_: HMActionSet, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620225-removeactionset)

|  | Declaration |
| --- | --- |
| From | ``` func removeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.removeRoom(_: HMRoom, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620246-removeroom)

|  | Declaration |
| --- | --- |
| From | ``` func removeRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.removeServiceGroup(_: HMServiceGroup, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620230-removeservicegroup)

|  | Declaration |
| --- | --- |
| From | ``` func removeServiceGroup(_ group: HMServiceGroup!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeServiceGroup(_ group: HMServiceGroup, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.removeTrigger(_: HMTrigger, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620220-removetrigger)

|  | Declaration |
| --- | --- |
| From | ``` func removeTrigger(_ trigger: HMTrigger!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeTrigger(_ trigger: HMTrigger, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.removeUser(_: HMUser, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620251-removeuser)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func removeUser(_ user: HMUser!, completionHandler completion: ((NSError!) -> Void)!) ``` | -- |
| To | ``` func removeUser(_ user: HMUser, completionHandler completion: (NSError?) -> Void) ``` | iOS 9.0 |

Modified [HMHome.removeZone(_: HMZone, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620223-removezone)

|  | Declaration |
| --- | --- |
| From | ``` func removeZone(_ zone: HMZone!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeZone(_ zone: HMZone, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.roomForEntireHome() -> HMRoom](https://developer.apple.com/documentation/homekit/hmhome/1620227-roomforentirehome)

|  | Declaration |
| --- | --- |
| From | ``` func roomForEntireHome() -> HMRoom! ``` |
| To | ``` func roomForEntireHome() -> HMRoom ``` |

Modified [HMHome.rooms](https://developer.apple.com/documentation/homekit/hmhome/1620276-rooms)

|  | Declaration |
| --- | --- |
| From | ``` var rooms: [AnyObject]! { get } ``` |
| To | ``` var rooms: [HMRoom] { get } ``` |

Modified [HMHome.serviceGroups](https://developer.apple.com/documentation/homekit/hmhome/1620266-servicegroups)

|  | Declaration |
| --- | --- |
| From | ``` var serviceGroups: [AnyObject]! { get } ``` |
| To | ``` var serviceGroups: [HMServiceGroup] { get } ``` |

Modified [HMHome.servicesWithTypes(_: [String]) -> [HMService]?](https://developer.apple.com/documentation/homekit/hmhome/1620235-serviceswithtypes)

|  | Declaration |
| --- | --- |
| From | ``` func servicesWithTypes(_ serviceTypes: [AnyObject]!) -> [AnyObject]! ``` |
| To | ``` func servicesWithTypes(_ serviceTypes: [String]) -> [HMService]? ``` |

Modified [HMHome.triggers](https://developer.apple.com/documentation/homekit/hmhome/1620218-triggers)

|  | Declaration |
| --- | --- |
| From | ``` var triggers: [AnyObject]! { get } ``` |
| To | ``` var triggers: [HMTrigger] { get } ``` |

Modified [HMHome.unblockAccessory(_: HMAccessory, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620260-unblockaccessory)

|  | Declaration |
| --- | --- |
| From | ``` func unblockAccessory(_ accessory: HMAccessory!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func unblockAccessory(_ accessory: HMAccessory, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhome/1620240-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHome.users](https://developer.apple.com/documentation/homekit/hmhome/1620254-users)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var users: [AnyObject]! { get } ``` | -- |
| To | ``` var users: [HMUser] { get } ``` | iOS 9.0 |

Modified [HMHome.zones](https://developer.apple.com/documentation/homekit/hmhome/1620224-zones)

|  | Declaration |
| --- | --- |
| From | ``` var zones: [AnyObject]! { get } ``` |
| To | ``` var zones: [HMZone] { get } ``` |

Modified [HMHomeDelegate](https://developer.apple.com/documentation/homekit/hmhomedelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMHomeDelegate : NSObjectProtocol {     optional func homeDidUpdateName(_ home: HMHome)     optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory!)     optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory!)     optional func home(_ home: HMHome, didAddUser user: HMUser!)     optional func home(_ home: HMHome, didRemoveUser user: HMUser!)     optional func home(_ home: HMHome, didUpdateRoom room: HMRoom!, forAccessory accessory: HMAccessory!)     optional func home(_ home: HMHome, didAddRoom room: HMRoom!)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!)     optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom!)     optional func home(_ home: HMHome, didAddZone zone: HMZone!)     optional func home(_ home: HMHome, didRemoveZone zone: HMZone!)     optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone!)     optional func home(_ home: HMHome, didAddRoom room: HMRoom!, toZone zone: HMZone!)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!, fromZone zone: HMZone!)     optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup!)     optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup!)     optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup!)     optional func home(_ home: HMHome, didAddService service: HMService!, toServiceGroup group: HMServiceGroup!)     optional func home(_ home: HMHome, didRemoveService service: HMService!, fromServiceGroup group: HMServiceGroup!)     optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet!)     optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet!)     optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet!)     optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet!)     optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger!)     optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger!)     optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger!)     optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger!)     optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory!)     optional func home(_ home: HMHome, didEncounterError error: NSError!, forAccessory accessory: HMAccessory!) } ``` |
| To | ``` protocol HMHomeDelegate : NSObjectProtocol {     optional func homeDidUpdateName(_ home: HMHome)     optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didAddUser user: HMUser)     optional func home(_ home: HMHome, didRemoveUser user: HMUser)     optional func home(_ home: HMHome, didUpdateRoom room: HMRoom, forAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didAddRoom room: HMRoom)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom)     optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom)     optional func home(_ home: HMHome, didAddZone zone: HMZone)     optional func home(_ home: HMHome, didRemoveZone zone: HMZone)     optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone)     optional func home(_ home: HMHome, didAddRoom room: HMRoom, toZone zone: HMZone)     optional func home(_ home: HMHome, didRemoveRoom room: HMRoom, fromZone zone: HMZone)     optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didAddService service: HMService, toServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didRemoveService service: HMService, fromServiceGroup group: HMServiceGroup)     optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet)     optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger)     optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory)     optional func home(_ home: HMHome, didEncounterError error: NSError, forAccessory accessory: HMAccessory) } ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620215-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddActionSet: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620277-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddRoom: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620244-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddRoom: HMRoom, toZone: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620241-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom!, toZone zone: HMZone!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom, toZone zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddService: HMService, toServiceGroup: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620274-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddService service: HMService!, toServiceGroup group: HMServiceGroup!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddService service: HMService, toServiceGroup group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddServiceGroup: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620211-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddTrigger: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620258-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddUser: HMUser)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620217-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddUser user: HMUser!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddUser user: HMUser) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didAddZone: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620249-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didAddZone zone: HMZone!) ``` |
| To | ``` optional func home(_ home: HMHome, didAddZone zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didEncounterError: NSError, forAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620247-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didEncounterError error: NSError!, forAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func home(_ home: HMHome, didEncounterError error: NSError, forAccessory accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620263-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveActionSet: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620267-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveRoom: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620270-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveRoom: HMRoom, fromZone: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620222-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!, fromZone zone: HMZone!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom, fromZone zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveService: HMService, fromServiceGroup: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620242-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveService service: HMService!, fromServiceGroup group: HMServiceGroup!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveService service: HMService, fromServiceGroup group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveServiceGroup: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620226-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveTrigger: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620262-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveUser: HMUser)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620232-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveUser user: HMUser!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveUser user: HMUser) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didRemoveZone: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620221-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didRemoveZone zone: HMZone!) ``` |
| To | ``` optional func home(_ home: HMHome, didRemoveZone zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUnblockAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620252-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateActionsForActionSet: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620259-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameForActionSet: HMActionSet)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620248-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameForRoom: HMRoom)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620272-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameForServiceGroup: HMServiceGroup)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620253-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameForTrigger: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620239-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateNameForZone: HMZone)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620228-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateRoom: HMRoom, forAccessory: HMAccessory)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620237-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateRoom room: HMRoom!, forAccessory accessory: HMAccessory!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateRoom room: HMRoom, forAccessory accessory: HMAccessory) ``` |

Modified [HMHomeDelegate.home(_: HMHome, didUpdateTrigger: HMTrigger)](https://developer.apple.com/documentation/homekit/hmhomedelegate/1620219-home)

|  | Declaration |
| --- | --- |
| From | ``` optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger!) ``` |
| To | ``` optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger) ``` |

Modified [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager)

|  | Declaration |
| --- | --- |
| From | ``` class HMHomeManager : NSObject {     weak var delegate: HMHomeManagerDelegate?     var primaryHome: HMHome! { get }     var homes: [AnyObject]! { get }     func updatePrimaryHome(_ home: HMHome!, completionHandler completion: ((NSError!) -> Void)!)     func addHomeWithName(_ homeName: String!, completionHandler completion: ((HMHome!, NSError!) -> Void)!)     func removeHome(_ home: HMHome!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMHomeManager : NSObject {     weak var delegate: HMHomeManagerDelegate?     var primaryHome: HMHome? { get }     var homes: [HMHome] { get }     func updatePrimaryHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void)     func addHomeWithName(_ homeName: String, completionHandler completion: (HMHome?, NSError?) -> Void)     func removeHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMHomeManager.addHomeWithName(_: String, completionHandler: (HMHome?, NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhomemanager/1616747-addhomewithname)

|  | Declaration |
| --- | --- |
| From | ``` func addHomeWithName(_ homeName: String!, completionHandler completion: ((HMHome!, NSError!) -> Void)!) ``` |
| To | ``` func addHomeWithName(_ homeName: String, completionHandler completion: (HMHome?, NSError?) -> Void) ``` |

Modified [HMHomeManager.homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes)

|  | Declaration |
| --- | --- |
| From | ``` var homes: [AnyObject]! { get } ``` |
| To | ``` var homes: [HMHome] { get } ``` |

Modified [HMHomeManager.primaryHome](https://developer.apple.com/documentation/homekit/hmhomemanager/1616745-primaryhome)

|  | Declaration |
| --- | --- |
| From | ``` var primaryHome: HMHome! { get } ``` |
| To | ``` var primaryHome: HMHome? { get } ``` |

Modified [HMHomeManager.removeHome(_: HMHome, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhomemanager/1616754-removehome)

|  | Declaration |
| --- | --- |
| From | ``` func removeHome(_ home: HMHome!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHomeManager.updatePrimaryHome(_: HMHome, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmhomemanager/1616746-updateprimaryhome)

|  | Declaration |
| --- | --- |
| From | ``` func updatePrimaryHome(_ home: HMHome!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updatePrimaryHome(_ home: HMHome, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMHomeManagerDelegate](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol HMHomeManagerDelegate : NSObjectProtocol {     optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager)     optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager)     optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome!)     optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome!) } ``` |
| To | ``` protocol HMHomeManagerDelegate : NSObjectProtocol {     optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager)     optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager)     optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome)     optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome) } ``` |

Modified [HMHomeManagerDelegate.homeManager(_: HMHomeManager, didAddHome: HMHome)](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616755-homemanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome!) ``` |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome) ``` |

Modified [HMHomeManagerDelegate.homeManager(_: HMHomeManager, didRemoveHome: HMHome)](https://developer.apple.com/documentation/homekit/hmhomemanagerdelegate/1616753-homemanager)

|  | Declaration |
| --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome!) ``` |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome) ``` |

Modified [HMRoom](https://developer.apple.com/documentation/homekit/hmroom)

|  | Declaration |
| --- | --- |
| From | ``` class HMRoom : NSObject {     init!()     var name: String! { get }     var accessories: [AnyObject]! { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMRoom : NSObject {     init()     var name: String { get }     var accessories: [HMAccessory] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMRoom.accessories](https://developer.apple.com/documentation/homekit/hmroom/1618288-accessories)

|  | Declaration |
| --- | --- |
| From | ``` var accessories: [AnyObject]! { get } ``` |
| To | ``` var accessories: [HMAccessory] { get } ``` |

Modified [HMRoom.name](https://developer.apple.com/documentation/homekit/hmroom/1618287-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMRoom.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmroom/1618289-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMService](https://developer.apple.com/documentation/homekit/hmservice)

|  | Declaration |
| --- | --- |
| From | ``` class HMService : NSObject {     weak var accessory: HMAccessory! { get }     var serviceType: String! { get }     var name: String! { get }     var associatedServiceType: String! { get }     var characteristics: [AnyObject]! { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func updateAssociatedServiceType(_ serviceType: String!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMService : NSObject {     weak var accessory: HMAccessory? { get }     var serviceType: String { get }     var localizedDescription: String { get }     var name: String { get }     var associatedServiceType: String? { get }     var characteristics: [HMCharacteristic] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     var userInteractive: Bool { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func updateAssociatedServiceType(_ serviceType: String?, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMService.accessory](https://developer.apple.com/documentation/homekit/hmservice/1615884-accessory)

|  | Declaration |
| --- | --- |
| From | ``` weak var accessory: HMAccessory! { get } ``` |
| To | ``` weak var accessory: HMAccessory? { get } ``` |

Modified [HMService.associatedServiceType](https://developer.apple.com/documentation/homekit/hmservice/1615889-associatedservicetype)

|  | Declaration |
| --- | --- |
| From | ``` var associatedServiceType: String! { get } ``` |
| To | ``` var associatedServiceType: String? { get } ``` |

Modified [HMService.characteristics](https://developer.apple.com/documentation/homekit/hmservice/1615893-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` var characteristics: [AnyObject]! { get } ``` |
| To | ``` var characteristics: [HMCharacteristic] { get } ``` |

Modified [HMService.name](https://developer.apple.com/documentation/homekit/hmservice/1615888-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMService.serviceType](https://developer.apple.com/documentation/homekit/hmservice/1615885-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` var serviceType: String! { get } ``` |
| To | ``` var serviceType: String { get } ``` |

Modified [HMService.updateAssociatedServiceType(_: String?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmservice/1615886-updateassociatedservicetype)

|  | Declaration |
| --- | --- |
| From | ``` func updateAssociatedServiceType(_ serviceType: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateAssociatedServiceType(_ serviceType: String?, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMService.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmservice/1615887-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup)

|  | Declaration |
| --- | --- |
| From | ``` class HMServiceGroup : NSObject {     init!()     var name: String! { get }     var services: [AnyObject]! { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func addService(_ service: HMService!, completionHandler completion: ((NSError!) -> Void)!)     func removeService(_ service: HMService!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMServiceGroup : NSObject {     init()     var name: String { get }     var services: [HMService] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addService(_ service: HMService, completionHandler completion: (NSError?) -> Void)     func removeService(_ service: HMService, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMServiceGroup.addService(_: HMService, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmservicegroup/1616997-addservice)

|  | Declaration |
| --- | --- |
| From | ``` func addService(_ service: HMService!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addService(_ service: HMService, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMServiceGroup.name](https://developer.apple.com/documentation/homekit/hmservicegroup/1616996-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMServiceGroup.removeService(_: HMService, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmservicegroup/1616994-removeservice)

|  | Declaration |
| --- | --- |
| From | ``` func removeService(_ service: HMService!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeService(_ service: HMService, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMServiceGroup.services](https://developer.apple.com/documentation/homekit/hmservicegroup/1616993-services)

|  | Declaration |
| --- | --- |
| From | ``` var services: [AnyObject]! { get } ``` |
| To | ``` var services: [HMService] { get } ``` |

Modified [HMServiceGroup.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmservicegroup/1616992-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger)

|  | Declaration |
| --- | --- |
| From | ``` class HMTimerTrigger : HMTrigger {     convenience init!()     init!(name name: String!, fireDate fireDate: NSDate!, timeZone timeZone: NSTimeZone!, recurrence recurrence: NSDateComponents!, recurrenceCalendar recurrenceCalendar: NSCalendar!)     @NSCopying var fireDate: NSDate! { get }     @NSCopying var timeZone: NSTimeZone! { get }     @NSCopying var recurrence: NSDateComponents! { get }     @NSCopying var recurrenceCalendar: NSCalendar! { get }     func updateFireDate(_ fireDate: NSDate!, completionHandler completion: ((NSError!) -> Void)!)     func updateTimeZone(_ timeZone: NSTimeZone!, completionHandler completion: ((NSError!) -> Void)!)     func updateRecurrence(_ recurrence: NSDateComponents!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMTimerTrigger : HMTrigger {     convenience init()     init(name name: String, fireDate fireDate: NSDate, timeZone timeZone: NSTimeZone?, recurrence recurrence: NSDateComponents?, recurrenceCalendar recurrenceCalendar: NSCalendar?)     @NSCopying var fireDate: NSDate { get }     @NSCopying var timeZone: NSTimeZone? { get }     @NSCopying var recurrence: NSDateComponents? { get }     @NSCopying var recurrenceCalendar: NSCalendar? { get }     func updateFireDate(_ fireDate: NSDate, completionHandler completion: (NSError?) -> Void)     func updateTimeZone(_ timeZone: NSTimeZone?, completionHandler completion: (NSError?) -> Void)     func updateRecurrence(_ recurrence: NSDateComponents?, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMTimerTrigger.fireDate](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616261-firedate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var fireDate: NSDate! { get } ``` |
| To | ``` @NSCopying var fireDate: NSDate { get } ``` |

Modified [HMTimerTrigger.init(name: String, fireDate: NSDate, timeZone: NSTimeZone?, recurrence: NSDateComponents?, recurrenceCalendar: NSCalendar?)](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616266-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(name name: String!, fireDate fireDate: NSDate!, timeZone timeZone: NSTimeZone!, recurrence recurrence: NSDateComponents!, recurrenceCalendar recurrenceCalendar: NSCalendar!) ``` |
| To | ``` init(name name: String, fireDate fireDate: NSDate, timeZone timeZone: NSTimeZone?, recurrence recurrence: NSDateComponents?, recurrenceCalendar recurrenceCalendar: NSCalendar?) ``` |

Modified [HMTimerTrigger.recurrence](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616260-recurrence)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recurrence: NSDateComponents! { get } ``` |
| To | ``` @NSCopying var recurrence: NSDateComponents? { get } ``` |

Modified [HMTimerTrigger.recurrenceCalendar](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616264-recurrencecalendar)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var recurrenceCalendar: NSCalendar! { get } ``` |
| To | ``` @NSCopying var recurrenceCalendar: NSCalendar? { get } ``` |

Modified [HMTimerTrigger.timeZone](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616268-timezone)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeZone: NSTimeZone! { get } ``` |
| To | ``` @NSCopying var timeZone: NSTimeZone? { get } ``` |

Modified [HMTimerTrigger.updateFireDate(_: NSDate, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616262-updatefiredate)

|  | Declaration |
| --- | --- |
| From | ``` func updateFireDate(_ fireDate: NSDate!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateFireDate(_ fireDate: NSDate, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTimerTrigger.updateRecurrence(_: NSDateComponents?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616267-updaterecurrence)

|  | Declaration |
| --- | --- |
| From | ``` func updateRecurrence(_ recurrence: NSDateComponents!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateRecurrence(_ recurrence: NSDateComponents?, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTimerTrigger.updateTimeZone(_: NSTimeZone?, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtimertrigger/1616265-updatetimezone)

|  | Declaration |
| --- | --- |
| From | ``` func updateTimeZone(_ timeZone: NSTimeZone!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateTimeZone(_ timeZone: NSTimeZone?, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTrigger](https://developer.apple.com/documentation/homekit/hmtrigger)

|  | Declaration |
| --- | --- |
| From | ``` class HMTrigger : NSObject {     init!()     var name: String! { get }     var enabled: Bool { get }     var actionSets: [AnyObject]! { get }     @NSCopying var lastFireDate: NSDate! { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func addActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!)     func removeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!)     func enable(_ enable: Bool, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMTrigger : NSObject {     init()     var name: String { get }     var enabled: Bool { get }     var actionSets: [HMActionSet] { get }     @NSCopying var lastFireDate: NSDate? { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void)     func enable(_ enable: Bool, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMTrigger.actionSets](https://developer.apple.com/documentation/homekit/hmtrigger/1620721-actionsets)

|  | Declaration |
| --- | --- |
| From | ``` var actionSets: [AnyObject]! { get } ``` |
| To | ``` var actionSets: [HMActionSet] { get } ``` |

Modified [HMTrigger.addActionSet(_: HMActionSet, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtrigger/1620716-addactionset)

|  | Declaration |
| --- | --- |
| From | ``` func addActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTrigger.enable(_: Bool, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtrigger/1620714-enable)

|  | Declaration |
| --- | --- |
| From | ``` func enable(_ enable: Bool, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func enable(_ enable: Bool, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTrigger.lastFireDate](https://developer.apple.com/documentation/homekit/hmtrigger/1620715-lastfiredate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastFireDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lastFireDate: NSDate? { get } ``` |

Modified [HMTrigger.name](https://developer.apple.com/documentation/homekit/hmtrigger/1620717-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMTrigger.removeActionSet(_: HMActionSet, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtrigger/1620718-removeactionset)

|  | Declaration |
| --- | --- |
| From | ``` func removeActionSet(_ actionSet: HMActionSet!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeActionSet(_ actionSet: HMActionSet, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMTrigger.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmtrigger/1620722-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMUser](https://developer.apple.com/documentation/homekit/hmuser)

|  | Declaration |
| --- | --- |
| From | ``` class HMUser : NSObject {     init!()     var name: String! { get } } ``` |
| To | ``` class HMUser : NSObject {     init()     var name: String { get }     @NSCopying var uniqueIdentifier: NSUUID { get } } ``` |

Modified [HMUser.name](https://developer.apple.com/documentation/homekit/hmuser/1620011-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMZone](https://developer.apple.com/documentation/homekit/hmzone)

|  | Declaration |
| --- | --- |
| From | ``` class HMZone : NSObject {     init!()     var name: String! { get }     var rooms: [AnyObject]! { get }     func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!)     func addRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!)     func removeRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!) } ``` |
| To | ``` class HMZone : NSObject {     init()     var name: String { get }     var rooms: [HMRoom] { get }     @NSCopying var uniqueIdentifier: NSUUID { get }     func updateName(_ name: String, completionHandler completion: (NSError?) -> Void)     func addRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void)     func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void) } ``` |

Modified [HMZone.addRoom(_: HMRoom, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmzone/1624764-addroom)

|  | Declaration |
| --- | --- |
| From | ``` func addRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func addRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMZone.name](https://developer.apple.com/documentation/homekit/hmzone/1624765-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [HMZone.removeRoom(_: HMRoom, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmzone/1624768-removeroom)

|  | Declaration |
| --- | --- |
| From | ``` func removeRoom(_ room: HMRoom!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func removeRoom(_ room: HMRoom, completionHandler completion: (NSError?) -> Void) ``` |

Modified [HMZone.rooms](https://developer.apple.com/documentation/homekit/hmzone/1624763-rooms)

|  | Declaration |
| --- | --- |
| From | ``` var rooms: [AnyObject]! { get } ``` |
| To | ``` var rooms: [HMRoom] { get } ``` |

Modified [HMZone.updateName(_: String, completionHandler: (NSError?) -> Void)](https://developer.apple.com/documentation/homekit/hmzone/1624767-updatename)

|  | Declaration |
| --- | --- |
| From | ``` func updateName(_ name: String!, completionHandler completion: ((NSError!) -> Void)!) ``` |
| To | ``` func updateName(_ name: String, completionHandler completion: (NSError?) -> Void) ``` |

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

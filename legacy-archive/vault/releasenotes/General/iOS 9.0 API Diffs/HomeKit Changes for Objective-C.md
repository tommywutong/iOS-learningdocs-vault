---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/HomeKit.html
archived_at: '2026-07-18T02:56:34.358739Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# HomeKit Changes for Objective-C

### HomeKit

#### HMAccessory.h

Added [HMAccessory.category](https://developer.apple.com/documentation/homekit/hmaccessory/1615275-category)Added [HMAccessory.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaccessory/1615261-uniqueidentifier)Added [HMAccessory.uniqueIdentifiersForBridgedAccessories](https://developer.apple.com/documentation/homekit/hmaccessory/1615278-uniqueidentifiersforbridgedacces)Modified [HMAccessory.identifier](https://developer.apple.com/documentation/homekit/hmaccessory/1615284-identifier)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [HMAccessory.identifiersForBridgedAccessories](https://developer.apple.com/documentation/homekit/hmaccessory/1615265-identifiersforbridgedaccessories)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *identifiersForBridgedAccessories ``` | -- |
| To | ``` @property(readonly, copy, nonatomic, nullable) NSArray<NSUUID *> *identifiersForBridgedAccessories ``` | iOS 9.0 |

Modified [HMAccessory.services](https://developer.apple.com/documentation/homekit/hmaccessory/1615250-services)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *services ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMService *> *services ``` |

#### HMAccessoryBrowser.h

Modified [HMAccessoryBrowser.discoveredAccessories](https://developer.apple.com/documentation/homekit/hmaccessorybrowser/1622406-discoveredaccessories)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *discoveredAccessories ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMAccessory *> *discoveredAccessories ``` |

#### HMAccessoryCategory.h (Added)

Added [HMAccessoryCategory](https://developer.apple.com/documentation/homekit/hmaccessorycategory)Added [HMAccessoryCategory.categoryType](https://developer.apple.com/documentation/homekit/hmaccessorycategory/1619926-categorytype)Added [HMAccessoryCategory.localizedDescription](https://developer.apple.com/documentation/homekit/hmaccessorycategory/1619924-localizeddescription)

#### HMAccessoryCategoryTypes.h (Added)

Added [HMAccessoryCategoryTypeBridge](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypebridge)Added [HMAccessoryCategoryTypeDoor](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypedoor)Added [HMAccessoryCategoryTypeDoorLock](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypedoorlock)Added [HMAccessoryCategoryTypeFan](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypefan)Added [HMAccessoryCategoryTypeGarageDoorOpener](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypegaragedooropener)Added [HMAccessoryCategoryTypeLightbulb](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypelightbulb)Added [HMAccessoryCategoryTypeOther](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeother)Added [HMAccessoryCategoryTypeOutlet](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeoutlet)Added [HMAccessoryCategoryTypeProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeprogrammableswitch)Added [HMAccessoryCategoryTypeSecuritySystem](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypesecuritysystem)Added [HMAccessoryCategoryTypeSensor](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypesensor)Added [HMAccessoryCategoryTypeSwitch](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypeswitch)Added [HMAccessoryCategoryTypeThermostat](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypethermostat)Added [HMAccessoryCategoryTypeWindow](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypewindow)Added [HMAccessoryCategoryTypeWindowCovering](https://developer.apple.com/documentation/homekit/hmaccessorycategorytypewindowcovering)

#### HMAction.h

Added [HMAction.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmaction/1624923-uniqueidentifier)

#### HMActionSet.h

Added [HMActionSet.actionSetType](https://developer.apple.com/documentation/homekit/hmactionset/1616794-actionsettype)Added [HMActionSet.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmactionset/1616789-uniqueidentifier)Added [HMActionSetTypeHomeArrival](https://developer.apple.com/documentation/homekit/hmactionsettypehomearrival)Added [HMActionSetTypeHomeDeparture](https://developer.apple.com/documentation/homekit/hmactionsettypehomedeparture)Added [HMActionSetTypeSleep](https://developer.apple.com/documentation/homekit/hmactionsettypesleep)Added [HMActionSetTypeUserDefined](https://developer.apple.com/documentation/homekit/hmactionsettypeuserdefined)Added [HMActionSetTypeWakeUp](https://developer.apple.com/documentation/homekit/hmactionsettypewakeup)Modified [HMActionSet.actions](https://developer.apple.com/documentation/homekit/hmactionset/1616790-actions)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSSet *actions ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSSet<HMAction *> *actions ``` |

#### HMCharacteristic.h

Added [HMCharacteristic.localizedDescription](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624185-localizeddescription)Added [HMCharacteristic.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624187-uniqueidentifier)Modified [HMCharacteristic.properties](https://developer.apple.com/documentation/homekit/hmcharacteristic/1624186-properties)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *properties ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<NSString *> *properties ``` |

Modified [HMCharacteristicPropertyReadable](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertyreadable)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicPropertySupportsEventNotification](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertysupportsevent)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicPropertyWritable](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertywritable)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeAdminOnlyAccess](https://developer.apple.com/documentation/homekit/hmcharacteristictypeadminonlyaccess)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeAudioFeedback](https://developer.apple.com/documentation/homekit/hmcharacteristictypeaudiofeedback)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeBrightness](https://developer.apple.com/documentation/homekit/hmcharacteristictypebrightness)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCoolingThreshold](https://developer.apple.com/documentation/homekit/hmcharacteristictypecoolingthreshold)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentDoorState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentdoorstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentHeatingCooling](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentheatingcooling)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentLockMechanismState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentlockmechanismstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentRelativeHumidity](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentrelativehumidity)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentTemperature](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrenttemperature)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeHeatingThreshold](https://developer.apple.com/documentation/homekit/hmcharacteristictypeheatingthreshold)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeHue](https://developer.apple.com/documentation/homekit/hmcharacteristictypehue)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeIdentify](https://developer.apple.com/documentation/homekit/hmcharacteristictypeidentify)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockManagementAutoSecureTimeout](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementautosecuretimeout)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockManagementControlPoint](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementcontrolpoint)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockMechanismLastKnownAction](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmechanismlastknownaction)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLogs](https://developer.apple.com/documentation/homekit/hmcharacteristictypelogs)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeManufacturer](https://developer.apple.com/documentation/homekit/hmcharacteristictypemanufacturer)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeModel](https://developer.apple.com/documentation/homekit/hmcharacteristictypemodel)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeMotionDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypemotiondetected)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeName](https://developer.apple.com/documentation/homekit/hmcharacteristictypename)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeObstructionDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeobstructiondetected)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeOutletInUse](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoutletinuse)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypePowerState](https://developer.apple.com/documentation/homekit/hmcharacteristictypepowerstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeRotationDirection](https://developer.apple.com/documentation/homekit/hmcharacteristictyperotationdirection)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeRotationSpeed](https://developer.apple.com/documentation/homekit/hmcharacteristictyperotationspeed)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeSaturation](https://developer.apple.com/documentation/homekit/hmcharacteristictypesaturation)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeSerialNumber](https://developer.apple.com/documentation/homekit/hmcharacteristictypeserialnumber)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetDoorState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetdoorstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetHeatingCooling](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetheatingcooling)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetLockMechanismState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetlockmechanismstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetRelativeHumidity](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetrelativehumidity)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetTemperature](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargettemperature)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTemperatureUnits](https://developer.apple.com/documentation/homekit/hmcharacteristictypetemperatureunits)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypeversion)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

#### HMCharacteristicDefines.h

Added [HMCharacteristicValueAirParticulateSize](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize)Added [HMCharacteristicValueAirParticulateSize10](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/hmcharacteristicvalueairparticulatesize10)Added [HMCharacteristicValueAirParticulateSize2_5](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize/hmcharacteristicvalueairparticulatesize2_5)Added [HMCharacteristicValueAirQuality](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality)Added [HMCharacteristicValueAirQualityExcellent](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/excellent)Added [HMCharacteristicValueAirQualityFair](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/fair)Added [HMCharacteristicValueAirQualityGood](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/good)Added [HMCharacteristicValueAirQualityInferior](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualityinferior)Added [HMCharacteristicValueAirQualityPoor](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/hmcharacteristicvalueairqualitypoor)Added [HMCharacteristicValueAirQualityUnknown](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality/unknown)Added [HMCharacteristicValueCurrentSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate)Added [HMCharacteristicValueCurrentSecuritySystemStateAwayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstateawayarm)Added [HMCharacteristicValueCurrentSecuritySystemStateDisarmed](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/disarmed)Added [HMCharacteristicValueCurrentSecuritySystemStateNightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/hmcharacteristicvaluecurrentsecuritysystemstatenightarm)Added [HMCharacteristicValueCurrentSecuritySystemStateStayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/stayarm)Added [HMCharacteristicValueCurrentSecuritySystemStateTriggered](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate/triggered)Added [HMCharacteristicValuePositionState](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate)Added [HMCharacteristicValuePositionStateClosing](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstateclosing)Added [HMCharacteristicValuePositionStateOpening](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstateopening)Added [HMCharacteristicValuePositionStateStopped](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate/hmcharacteristicvaluepositionstatestopped)Added [HMCharacteristicValueTargetSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate)Added [HMCharacteristicValueTargetSecuritySystemStateAwayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstateawayarm)Added [HMCharacteristicValueTargetSecuritySystemStateDisarm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatedisarm)Added [HMCharacteristicValueTargetSecuritySystemStateNightArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatenightarm)Added [HMCharacteristicValueTargetSecuritySystemStateStayArm](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate/hmcharacteristicvaluetargetsecuritysystemstatestayarm)

#### HMCharacteristicEvent.h (Added)

Added [HMCharacteristicEvent](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)Added [HMCharacteristicEvent.characteristic](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617203-characteristic)Added [-[HMCharacteristicEvent initWithCharacteristic:triggerValue:]](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617201-initwithcharacteristic)Added [HMCharacteristicEvent.triggerValue](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617200-triggervalue)Added [-[HMCharacteristicEvent updateTriggerValue:completionHandler:]](https://developer.apple.com/documentation/homekit/hmcharacteristicevent/1617202-updatetriggervalue)

#### HMCharacteristicTypes.h (Added)

Added [HMCharacteristicTypeAirParticulateDensity](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairparticulatedensity)Added [HMCharacteristicTypeAirParticulateSize](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairparticulatesize)Added [HMCharacteristicTypeAirQuality](https://developer.apple.com/documentation/homekit/hmcharacteristictypeairquality)Added [HMCharacteristicTypeBatteryLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypebatterylevel)Added [HMCharacteristicTypeCarbonDioxideDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidedetected)Added [HMCharacteristicTypeCarbonDioxideLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidelevel)Added [HMCharacteristicTypeCarbonDioxidePeakLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbondioxidepeaklevel)Added [HMCharacteristicTypeCarbonMonoxideDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidedetected)Added [HMCharacteristicTypeCarbonMonoxideLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidelevel)Added [HMCharacteristicTypeCarbonMonoxidePeakLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecarbonmonoxidepeaklevel)Added [HMCharacteristicTypeChargingState](https://developer.apple.com/documentation/homekit/hmcharacteristictypechargingstate)Added [HMCharacteristicTypeContactState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecontactstate)Added [HMCharacteristicTypeCurrentHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrenthorizontaltilt)Added [HMCharacteristicTypeCurrentLightLevel](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentlightlevel)Added [HMCharacteristicTypeCurrentPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentposition)Added [HMCharacteristicTypeCurrentSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentsecuritysystemstate)Added [HMCharacteristicTypeCurrentVerticalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentverticaltilt)Added [HMCharacteristicTypeFirmwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypefirmwareversion)Added [HMCharacteristicTypeHardwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypehardwareversion)Added [HMCharacteristicTypeHoldPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypeholdposition)Added [HMCharacteristicTypeInputEvent](https://developer.apple.com/documentation/homekit/hmcharacteristictypeinputevent)Added [HMCharacteristicTypeLeakDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeleakdetected)Added [HMCharacteristicTypeOccupancyDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoccupancydetected)Added [HMCharacteristicTypeOutputState](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoutputstate)Added [HMCharacteristicTypePositionState](https://developer.apple.com/documentation/homekit/hmcharacteristictypepositionstate)Added [HMCharacteristicTypeSecuritySystemAlarmType](https://developer.apple.com/documentation/homekit/hmcharacteristictypesecuritysystemalarmtype)Added [HMCharacteristicTypeSmokeDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypesmokedetected)Added [HMCharacteristicTypeSoftwareVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypesoftwareversion)Added [HMCharacteristicTypeStatusActive](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusactive)Added [HMCharacteristicTypeStatusFault](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusfault)Added [HMCharacteristicTypeStatusJammed](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatusjammed)Added [HMCharacteristicTypeStatusLowBattery](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatuslowbattery)Added [HMCharacteristicTypeStatusTampered](https://developer.apple.com/documentation/homekit/hmcharacteristictypestatustampered)Added [HMCharacteristicTypeTargetHorizontalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargethorizontaltilt)Added [HMCharacteristicTypeTargetPosition](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetposition)Added [HMCharacteristicTypeTargetSecuritySystemState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetsecuritysystemstate)Added [HMCharacteristicTypeTargetVerticalTilt](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetverticaltilt)Modified [HMCharacteristicPropertyReadable](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertyreadable)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicPropertySupportsEventNotification](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertysupportsevent)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicPropertyWritable](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertywritable)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeAdminOnlyAccess](https://developer.apple.com/documentation/homekit/hmcharacteristictypeadminonlyaccess)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeAudioFeedback](https://developer.apple.com/documentation/homekit/hmcharacteristictypeaudiofeedback)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeBrightness](https://developer.apple.com/documentation/homekit/hmcharacteristictypebrightness)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCoolingThreshold](https://developer.apple.com/documentation/homekit/hmcharacteristictypecoolingthreshold)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentDoorState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentdoorstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentHeatingCooling](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentheatingcooling)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentLockMechanismState](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentlockmechanismstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentRelativeHumidity](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentrelativehumidity)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeCurrentTemperature](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrenttemperature)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeHeatingThreshold](https://developer.apple.com/documentation/homekit/hmcharacteristictypeheatingthreshold)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeHue](https://developer.apple.com/documentation/homekit/hmcharacteristictypehue)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeIdentify](https://developer.apple.com/documentation/homekit/hmcharacteristictypeidentify)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockManagementAutoSecureTimeout](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementautosecuretimeout)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockManagementControlPoint](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmanagementcontrolpoint)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLockMechanismLastKnownAction](https://developer.apple.com/documentation/homekit/hmcharacteristictypelockmechanismlastknownaction)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeLogs](https://developer.apple.com/documentation/homekit/hmcharacteristictypelogs)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeManufacturer](https://developer.apple.com/documentation/homekit/hmcharacteristictypemanufacturer)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeModel](https://developer.apple.com/documentation/homekit/hmcharacteristictypemodel)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeMotionDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypemotiondetected)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeName](https://developer.apple.com/documentation/homekit/hmcharacteristictypename)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeObstructionDetected](https://developer.apple.com/documentation/homekit/hmcharacteristictypeobstructiondetected)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeOutletInUse](https://developer.apple.com/documentation/homekit/hmcharacteristictypeoutletinuse)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypePowerState](https://developer.apple.com/documentation/homekit/hmcharacteristictypepowerstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeRotationDirection](https://developer.apple.com/documentation/homekit/hmcharacteristictyperotationdirection)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeRotationSpeed](https://developer.apple.com/documentation/homekit/hmcharacteristictyperotationspeed)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeSaturation](https://developer.apple.com/documentation/homekit/hmcharacteristictypesaturation)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeSerialNumber](https://developer.apple.com/documentation/homekit/hmcharacteristictypeserialnumber)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetDoorState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetdoorstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetHeatingCooling](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetheatingcooling)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetLockMechanismState](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetlockmechanismstate)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetRelativeHumidity](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargetrelativehumidity)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTargetTemperature](https://developer.apple.com/documentation/homekit/hmcharacteristictypetargettemperature)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeTemperatureUnits](https://developer.apple.com/documentation/homekit/hmcharacteristictypetemperatureunits)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

Modified [HMCharacteristicTypeVersion](https://developer.apple.com/documentation/homekit/hmcharacteristictypeversion)

|  | Header |
| --- | --- |
| From | HomeKit/HMCharacteristic.h |
| To | HomeKit/HMCharacteristicTypes.h |

#### HMCharacteristicWriteAction.h

Modified [-[HMCharacteristicWriteAction initWithCharacteristic:targetValue:]](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621976-initwithcharacteristic)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCharacteristic:(HMCharacteristic *)characteristic targetValue:(id)targetValue ``` |
| To | ``` - (instancetype _Nonnull)initWithCharacteristic:(HMCharacteristic * _Nonnull)characteristic targetValue:(TargetValueType _Nonnull)targetValue ``` |

Modified [HMCharacteristicWriteAction.targetValue](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621973-targetvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) id targetValue ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) TargetValueType targetValue ``` |

Modified [-[HMCharacteristicWriteAction updateTargetValue:completionHandler:]](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction/1621972-updatetargetvalue)

|  | Declaration |
| --- | --- |
| From | ``` - (void)updateTargetValue:(id)targetValue completionHandler:(void (^)(NSError *error))completion ``` |
| To | ``` - (void)updateTargetValue:(TargetValueType _Nonnull)targetValue completionHandler:(void (^ _Nonnull)(NSError * _Nullable error))completion ``` |

#### HMError.h

Added [HMErrorCodeCannotRemoveBuiltinActionSet](https://developer.apple.com/documentation/homekit/hmerror/code/cannotremovebuiltinactionset)Added [HMErrorCodeLocationForHomeDisabled](https://developer.apple.com/documentation/homekit/hmerror/code/locationforhomedisabled)Added [HMErrorCodeNotAuthorizedForLocationServices](https://developer.apple.com/documentation/homekit/hmerror/code/notauthorizedforlocationservices)Modified [HMErrorCodeCannotUnblockNonBridgeAccessory](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcodecannotunblocknonbridgeaccessory)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 8.0 |

Modified [HMErrorCodeDeviceLocked](https://developer.apple.com/documentation/homekit/hmerror/code/devicelocked)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 8.0 |

#### HMEvent.h (Added)

Added [HMEvent](https://developer.apple.com/documentation/homekit/hmevent)Added [HMEvent.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmevent/1619881-uniqueidentifier)

#### HMEventTrigger.h (Added)

Added [HMEventTrigger](https://developer.apple.com/documentation/homekit/hmeventtrigger)Added [-[HMEventTrigger addEvent:completionHandler:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624416-addevent)Added [HMEventTrigger.events](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624413-events)Added [-[HMEventTrigger initWithName:events:predicate:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624402-initwithname)Added [HMEventTrigger.predicate](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624405-predicate)Added [+[HMEventTrigger predicateForEvaluatingTriggerOccurringAfterDateWithComponents:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624414-predicateforevaluatingtriggerocc)Added [+[HMEventTrigger predicateForEvaluatingTriggerOccurringAfterSignificantEvent:applyingOffset:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624406-predicateforevaluatingtriggerocc)Added [+[HMEventTrigger predicateForEvaluatingTriggerOccurringBeforeDateWithComponents:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624408-predicateforevaluatingtrigger)Added [+[HMEventTrigger predicateForEvaluatingTriggerOccurringBeforeSignificantEvent:applyingOffset:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624401-predicateforevaluatingtrigger)Added [+[HMEventTrigger predicateForEvaluatingTriggerOccurringOnDateWithComponents:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624407-predicateforevaluatingtrigger)Added [+[HMEventTrigger predicateForEvaluatingTriggerWithCharacteristic:relatedBy:toValue:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624409-predicateforevaluatingtrigger)Added [-[HMEventTrigger removeEvent:completionHandler:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624403-removeevent)Added [-[HMEventTrigger updatePredicate:completionHandler:]](https://developer.apple.com/documentation/homekit/hmeventtrigger/1624411-updatepredicate)Added [HMCharacteristicKeyPath](https://developer.apple.com/documentation/homekit/hmcharacteristickeypath)Added [HMCharacteristicValueKeyPath](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluekeypath)Added [HMSignificantEventSunrise](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624412-sunrise)Added [HMSignificantEventSunset](https://developer.apple.com/documentation/homekit/hmsignificantevent/1624417-sunset)

#### HMHome.h

Added [-[HMHome builtinActionSetOfType:]](https://developer.apple.com/documentation/homekit/hmhome/1620238-builtinactionsetoftype)Added [HMHome.currentUser](https://developer.apple.com/documentation/homekit/hmhome/1620255-currentuser)Added [-[HMHome homeAccessControlForUser:]](https://developer.apple.com/documentation/homekit/hmhome/1620214-homeaccesscontrolforuser)Added [-[HMHome manageUsersWithCompletionHandler:]](https://developer.apple.com/documentation/homekit/hmhome/1620268-manageuserswithcompletionhandler)Added [HMHome.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmhome/1620243-uniqueidentifier)Modified [HMHome.accessories](https://developer.apple.com/documentation/homekit/hmhome/1620275-accessories)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *accessories ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMAccessory *> *accessories ``` |

Modified [HMHome.actionSets](https://developer.apple.com/documentation/homekit/hmhome/1620257-actionsets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *actionSets ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMActionSet *> *actionSets ``` |

Modified [-[HMHome addUserWithCompletionHandler:]](https://developer.apple.com/documentation/homekit/hmhome/1620213-adduserwithcompletionhandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [-[HMHome removeUser:completionHandler:]](https://developer.apple.com/documentation/homekit/hmhome/1620251-removeuser)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

Modified [HMHome.rooms](https://developer.apple.com/documentation/homekit/hmhome/1620276-rooms)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *rooms ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMRoom *> *rooms ``` |

Modified [HMHome.serviceGroups](https://developer.apple.com/documentation/homekit/hmhome/1620266-servicegroups)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *serviceGroups ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMServiceGroup *> *serviceGroups ``` |

Modified [-[HMHome servicesWithTypes:]](https://developer.apple.com/documentation/homekit/hmhome/1620235-serviceswithtypes)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)servicesWithTypes:(NSArray *)serviceTypes ``` |
| To | ``` - (NSArray<HMService *> * _Nullable)servicesWithTypes:(NSArray<NSString *> * _Nonnull)serviceTypes ``` |

Modified [HMHome.triggers](https://developer.apple.com/documentation/homekit/hmhome/1620218-triggers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *triggers ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMTrigger *> *triggers ``` |

Modified [HMHome.users](https://developer.apple.com/documentation/homekit/hmhome/1620254-users)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *users ``` | -- |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMUser *> *users ``` | iOS 9.0 |

Modified [HMHome.zones](https://developer.apple.com/documentation/homekit/hmhome/1620224-zones)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *zones ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMZone *> *zones ``` |

#### HMHomeAccessControl.h (Added)

Added [HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)Added [HMHomeAccessControl.administrator](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol/1624331-administrator)

#### HMHomeManager.h

Modified [HMHomeManager.homes](https://developer.apple.com/documentation/homekit/hmhomemanager/1616751-homes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *homes ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMHome *> *homes ``` |

#### HMLocationEvent.h (Added)

Added [HMLocationEvent](https://developer.apple.com/documentation/homekit/hmlocationevent)Added [-[HMLocationEvent initWithRegion:]](https://developer.apple.com/documentation/homekit/hmlocationevent/1624981-initwithregion)Added [HMLocationEvent.region](https://developer.apple.com/documentation/homekit/hmlocationevent/1624980-region)Added [-[HMLocationEvent updateRegion:completionHandler:]](https://developer.apple.com/documentation/homekit/hmlocationevent/1624982-updateregion)

#### HMRoom.h

Added [HMRoom.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmroom/1618291-uniqueidentifier)Modified [HMRoom.accessories](https://developer.apple.com/documentation/homekit/hmroom/1618288-accessories)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *accessories ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMAccessory *> *accessories ``` |

#### HMService.h

Added [HMService.localizedDescription](https://developer.apple.com/documentation/homekit/hmservice/1615890-localizeddescription)Added [HMService.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservice/1615883-uniqueidentifier)Added [HMService.userInteractive](https://developer.apple.com/documentation/homekit/hmservice/1615891-userinteractive)Modified [HMService.characteristics](https://developer.apple.com/documentation/homekit/hmservice/1615893-characteristics)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *characteristics ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMCharacteristic *> *characteristics ``` |

Modified [HMServiceTypeAccessoryInformation](https://developer.apple.com/documentation/homekit/hmservicetypeaccessoryinformation)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeFan](https://developer.apple.com/documentation/homekit/hmservicetypefan)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeGarageDoorOpener](https://developer.apple.com/documentation/homekit/hmservicetypegaragedooropener)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLightbulb](https://developer.apple.com/documentation/homekit/hmservicetypelightbulb)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLockManagement](https://developer.apple.com/documentation/homekit/hmservicetypelockmanagement)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLockMechanism](https://developer.apple.com/documentation/homekit/hmservicetypelockmechanism)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeOutlet](https://developer.apple.com/documentation/homekit/hmservicetypeoutlet)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeSwitch](https://developer.apple.com/documentation/homekit/hmservicetypeswitch)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeThermostat](https://developer.apple.com/documentation/homekit/hmservicetypethermostat)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

#### HMServiceGroup.h

Added [HMServiceGroup.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmservicegroup/1616991-uniqueidentifier)Modified [HMServiceGroup.services](https://developer.apple.com/documentation/homekit/hmservicegroup/1616993-services)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *services ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMService *> *services ``` |

#### HMServiceTypes.h (Added)

Added [HMServiceTypeAirQualitySensor](https://developer.apple.com/documentation/homekit/hmservicetypeairqualitysensor)Added [HMServiceTypeBattery](https://developer.apple.com/documentation/homekit/hmservicetypebattery)Added [HMServiceTypeCarbonDioxideSensor](https://developer.apple.com/documentation/homekit/hmservicetypecarbondioxidesensor)Added [HMServiceTypeCarbonMonoxideSensor](https://developer.apple.com/documentation/homekit/hmservicetypecarbonmonoxidesensor)Added [HMServiceTypeContactSensor](https://developer.apple.com/documentation/homekit/hmservicetypecontactsensor)Added [HMServiceTypeDoor](https://developer.apple.com/documentation/homekit/hmservicetypedoor)Added [HMServiceTypeHumiditySensor](https://developer.apple.com/documentation/homekit/hmservicetypehumiditysensor)Added [HMServiceTypeLeakSensor](https://developer.apple.com/documentation/homekit/hmservicetypeleaksensor)Added [HMServiceTypeLightSensor](https://developer.apple.com/documentation/homekit/hmservicetypelightsensor)Added [HMServiceTypeMotionSensor](https://developer.apple.com/documentation/homekit/hmservicetypemotionsensor)Added [HMServiceTypeOccupancySensor](https://developer.apple.com/documentation/homekit/hmservicetypeoccupancysensor)Added [HMServiceTypeSecuritySystem](https://developer.apple.com/documentation/homekit/hmservicetypesecuritysystem)Added [HMServiceTypeSmokeSensor](https://developer.apple.com/documentation/homekit/hmservicetypesmokesensor)Added [HMServiceTypeStatefulProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmservicetypestatefulprogrammableswitch)Added [HMServiceTypeStatelessProgrammableSwitch](https://developer.apple.com/documentation/homekit/hmservicetypestatelessprogrammableswitch)Added [HMServiceTypeTemperatureSensor](https://developer.apple.com/documentation/homekit/hmservicetypetemperaturesensor)Added [HMServiceTypeWindow](https://developer.apple.com/documentation/homekit/hmservicetypewindow)Added [HMServiceTypeWindowCovering](https://developer.apple.com/documentation/homekit/hmservicetypewindowcovering)Modified [HMServiceTypeAccessoryInformation](https://developer.apple.com/documentation/homekit/hmservicetypeaccessoryinformation)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeFan](https://developer.apple.com/documentation/homekit/hmservicetypefan)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeGarageDoorOpener](https://developer.apple.com/documentation/homekit/hmservicetypegaragedooropener)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLightbulb](https://developer.apple.com/documentation/homekit/hmservicetypelightbulb)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLockManagement](https://developer.apple.com/documentation/homekit/hmservicetypelockmanagement)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeLockMechanism](https://developer.apple.com/documentation/homekit/hmservicetypelockmechanism)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeOutlet](https://developer.apple.com/documentation/homekit/hmservicetypeoutlet)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeSwitch](https://developer.apple.com/documentation/homekit/hmservicetypeswitch)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

Modified [HMServiceTypeThermostat](https://developer.apple.com/documentation/homekit/hmservicetypethermostat)

|  | Header |
| --- | --- |
| From | HomeKit/HMService.h |
| To | HomeKit/HMServiceTypes.h |

#### HMTrigger.h

Added [HMTrigger.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmtrigger/1620720-uniqueidentifier)Modified [HMTrigger.actionSets](https://developer.apple.com/documentation/homekit/hmtrigger/1620721-actionsets)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *actionSets ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMActionSet *> *actionSets ``` |

#### HMUser.h

Added [HMUser.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmuser/1620013-uniqueidentifier)

#### HMZone.h

Added [HMZone.uniqueIdentifier](https://developer.apple.com/documentation/homekit/hmzone/1624766-uniqueidentifier)Modified [HMZone.rooms](https://developer.apple.com/documentation/homekit/hmzone/1624763-rooms)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, nonatomic) NSArray *rooms ``` |
| To | ``` @property(readonly, copy, nonatomic, nonnull) NSArray<HMRoom *> *rooms ``` |

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

---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/HealthKit.html
archived_at: '2026-07-18T02:56:34.221015Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# HealthKit Changes for Objective-C

### HealthKit

#### HKAnchoredObjectQuery.h

Added [-[HKAnchoredObjectQuery initWithType:predicate:anchor:limit:resultsHandler:]](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615071-initwithtype)Added [HKAnchoredObjectQuery.updateHandler](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615691-updatehandler)Added [HKQueryAnchor](https://developer.apple.com/documentation/healthkit/hkqueryanchor)Added [+[HKQueryAnchor anchorFromValue:]](https://developer.apple.com/documentation/healthkit/hkqueryanchor/1615355-init)Modified [-[HKAnchoredObjectQuery initWithType:predicate:anchor:limit:completionHandler:]](https://developer.apple.com/documentation/healthkit/hkanchoredobjectquery/1615388-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (instancetype)initWithType:(HKSampleType *)type predicate:(NSPredicate *)predicate anchor:(NSUInteger)anchor limit:(NSUInteger)limit completionHandler:(void (^)(HKAnchoredObjectQuery *query, NSArray *results, NSUInteger newAnchor, NSError *error))handler ``` | -- |
| To | ``` - (instancetype _Nonnull)initWithType:(HKSampleType * _Nonnull)type predicate:(NSPredicate * _Nullable)predicate anchor:(NSUInteger)anchor limit:(NSUInteger)limit completionHandler:(void (^ _Nonnull)(HKAnchoredObjectQuery * _Nonnull query, NSArray<__kindof HKSample *> * _Nullable results, NSUInteger newAnchor, NSError * _Nullable error))handler ``` | iOS 9.0 |

#### HKCategorySample.h

Added [+[HKCategorySample categorySampleWithType:value:startDate:endDate:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615287-init)Modified [+[HKCategorySample categorySampleWithType:value:startDate:endDate:metadata:]](https://developer.apple.com/documentation/healthkit/hkcategorysample/1615596-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)categorySampleWithType:(HKCategoryType *)type value:(NSInteger)value startDate:(NSDate *)startDate endDate:(NSDate *)endDate metadata:(NSDictionary *)metadata ``` |
| To | ``` + (instancetype _Nonnull)categorySampleWithType:(HKCategoryType * _Nonnull)type value:(NSInteger)value startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate metadata:(NSDictionary<NSString *,id> * _Nullable)metadata ``` |

#### HKCorrelation.h

Added [+[HKCorrelation correlationWithType:startDate:endDate:objects:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614363-correlationwithtype)Modified [HKCorrelation](https://developer.apple.com/documentation/healthkit/hkcorrelation)

|  | Protocols |
| --- | --- |
| From | NSSecureCoding |
| To | -- |

Modified [+[HKCorrelation correlationWithType:startDate:endDate:objects:]](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614359-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)correlationWithType:(HKCorrelationType *)correlationType startDate:(NSDate *)startDate endDate:(NSDate *)endDate objects:(NSSet *)objects ``` |
| To | ``` + (instancetype _Nonnull)correlationWithType:(HKCorrelationType * _Nonnull)correlationType startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate objects:(NSSet<HKSample *> * _Nonnull)objects ``` |

Modified [+[HKCorrelation correlationWithType:startDate:endDate:objects:metadata:]](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614362-correlationwithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)correlationWithType:(HKCorrelationType *)correlationType startDate:(NSDate *)startDate endDate:(NSDate *)endDate objects:(NSSet *)objects metadata:(NSDictionary *)metadata ``` |
| To | ``` + (instancetype _Nonnull)correlationWithType:(HKCorrelationType * _Nonnull)correlationType startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate objects:(NSSet<HKSample *> * _Nonnull)objects metadata:(NSDictionary<NSString *,id> * _Nullable)metadata ``` |

Modified [HKCorrelation.objects](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614364-objects)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSSet *objects ``` |
| To | ``` @property(readonly, copy, nonnull) NSSet<__kindof HKSample *> *objects ``` |

Modified [-[HKCorrelation objectsForType:]](https://developer.apple.com/documentation/healthkit/hkcorrelation/1614360-objects)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)objectsForType:(HKObjectType *)objectType ``` |
| To | ``` - (NSSet<__kindof HKSample *> * _Nonnull)objectsForType:(HKObjectType * _Nonnull)objectType ``` |

#### HKCorrelationQuery.h

Modified [-[HKCorrelationQuery initWithType:predicate:samplePredicates:completion:]](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614145-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithType:(HKCorrelationType *)correlationType predicate:(NSPredicate *)predicate samplePredicates:(NSDictionary *)samplePredicates completion:(void (^)(HKCorrelationQuery *query, NSArray *correlations, NSError *error))completion ``` |
| To | ``` - (instancetype _Nonnull)initWithType:(HKCorrelationType * _Nonnull)correlationType predicate:(NSPredicate * _Nullable)predicate samplePredicates:(NSDictionary<HKSampleType *,NSPredicate *> * _Nullable)samplePredicates completion:(void (^ _Nonnull)(HKCorrelationQuery * _Nonnull query, NSArray<HKCorrelation *> * _Nullable correlations, NSError * _Nullable error))completion ``` |

Modified [HKCorrelationQuery.samplePredicates](https://developer.apple.com/documentation/healthkit/hkcorrelationquery/1614147-samplepredicates)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *samplePredicates ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<__kindof HKSampleType *,NSPredicate *> *samplePredicates ``` |

#### HKDefines.h

Added #def HK_AVAILABLE_WATCHOS_ONLYAdded #def HK_CLASS_AVAILABLE_WATCHOS_ONLYAdded [HKCategoryValue](https://developer.apple.com/documentation/healthkit/hkcategoryvalue)Added [HKCategoryValueAppleStandHour](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour)Added [HKCategoryValueAppleStandHourIdle](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/hkcategoryvalueapplestandhouridle)Added [HKCategoryValueAppleStandHourStood](https://developer.apple.com/documentation/healthkit/hkcategoryvalueapplestandhour/hkcategoryvalueapplestandhourstood)Added [HKCategoryValueCervicalMucusQuality](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality)Added [HKCategoryValueCervicalMucusQualityCreamy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualitycreamy)Added [HKCategoryValueCervicalMucusQualityDry](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/dry)Added [HKCategoryValueCervicalMucusQualityEggWhite](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualityeggwhite)Added [HKCategoryValueCervicalMucusQualitySticky](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualitysticky)Added [HKCategoryValueCervicalMucusQualityWatery](https://developer.apple.com/documentation/healthkit/hkcategoryvaluecervicalmucusquality/hkcategoryvaluecervicalmucusqualitywatery)Added [HKCategoryValueMenstrualFlow](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow)Added [HKCategoryValueMenstrualFlowHeavy](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/hkcategoryvaluemenstrualflowheavy)Added [HKCategoryValueMenstrualFlowLight](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/light)Added [HKCategoryValueMenstrualFlowMedium](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/medium)Added [HKCategoryValueMenstrualFlowUnspecified](https://developer.apple.com/documentation/healthkit/hkcategoryvaluemenstrualflow/unspecified)Added [HKCategoryValueNotApplicable](https://developer.apple.com/documentation/healthkit/hkcategoryvalue/notapplicable)Added [HKCategoryValueOvulationTestResult](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult)Added [HKCategoryValueOvulationTestResultIndeterminate](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/indeterminate)Added [HKCategoryValueOvulationTestResultNegative](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/hkcategoryvalueovulationtestresultnegative)Added [HKCategoryValueOvulationTestResultPositive](https://developer.apple.com/documentation/healthkit/hkcategoryvalueovulationtestresult/positive)Added [HKErrorAnotherWorkoutSessionStarted](https://developer.apple.com/documentation/healthkit/hkerrorcode/hkerroranotherworkoutsessionstarted)Added [HKErrorUserExitedWorkoutSession](https://developer.apple.com/documentation/healthkit/hkerror/code/erroruserexitedworkoutsession)Added [HKFitzpatrickSkinType](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype)Added [HKFitzpatrickSkinTypeI](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/i)Added [HKFitzpatrickSkinTypeII](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/ii)Added [HKFitzpatrickSkinTypeIII](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypeiii)Added [HKFitzpatrickSkinTypeIV](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypeiv)Added [HKFitzpatrickSkinTypeNotSet](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/notset)Added [HKFitzpatrickSkinTypeV](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/v)Added [HKFitzpatrickSkinTypeVI](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintype/hkfitzpatrickskintypevi)

#### HKDeletedObject.h (Added)

Added [HKDeletedObject](https://developer.apple.com/documentation/healthkit/hkdeletedobject)Added [HKDeletedObject.UUID](https://developer.apple.com/documentation/healthkit/hkdeletedobject/1615423-uuid)

#### HKDevice.h (Added)

Added [HKDevice](https://developer.apple.com/documentation/healthkit/hkdevice)Added [HKDevice.firmwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615749-firmwareversion)Added [HKDevice.hardwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615540-hardwareversion)Added [-[HKDevice initWithName:manufacturer:model:hardwareVersion:firmwareVersion:softwareVersion:localIdentifier:UDIDeviceIdentifier:]](https://developer.apple.com/documentation/healthkit/hkdevice/1615582-initwithname)Added [+[HKDevice localDevice]](https://developer.apple.com/documentation/healthkit/hkdevice/1615276-localdevice)Added [HKDevice.localIdentifier](https://developer.apple.com/documentation/healthkit/hkdevice/1615785-localidentifier)Added [HKDevice.manufacturer](https://developer.apple.com/documentation/healthkit/hkdevice/1615305-manufacturer)Added [HKDevice.model](https://developer.apple.com/documentation/healthkit/hkdevice/1615761-model)Added [HKDevice.name](https://developer.apple.com/documentation/healthkit/hkdevice/1615731-name)Added [HKDevice.softwareVersion](https://developer.apple.com/documentation/healthkit/hkdevice/1615262-softwareversion)Added [HKDevice.UDIDeviceIdentifier](https://developer.apple.com/documentation/healthkit/hkdevice/1615296-udideviceidentifier)Added [HKDevicePropertyKeyFirmwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyfirmwareversion)Added [HKDevicePropertyKeyHardwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyhardwareversion)Added [HKDevicePropertyKeyLocalIdentifier](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeylocalidentifier)Added [HKDevicePropertyKeyManufacturer](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeymanufacturer)Added [HKDevicePropertyKeyModel](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeymodel)Added [HKDevicePropertyKeyName](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyname)Added [HKDevicePropertyKeySoftwareVersion](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeysoftwareversion)Added [HKDevicePropertyKeyUDIDeviceIdentifier](https://developer.apple.com/documentation/healthkit/hkdevicepropertykeyudideviceidentifier)

#### HKHealthStore.h

Added [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)Added [HKFitzpatrickSkinTypeObject.skinType](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject/1614174-skintype)Added [-[HKHealthStore deleteObjects:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614163-deleteobjects)Added [-[HKHealthStore deleteObjectsOfType:predicate:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614162-deleteobjectsoftype)Added [-[HKHealthStore earliestPermittedSampleDate]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614166-earliestpermittedsampledate)Added [-[HKHealthStore fitzpatrickSkinTypeWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614161-fitzpatrickskintypewitherror)Added [-[HKHealthStore handleAuthorizationForExtensionWithCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614153-handleauthorizationforextensionw)Added [-[HKHealthStore splitTotalEnergy:startDate:endDate:resultsHandler:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614170-splittotalenergy)Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCopying, NSSecureCoding |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSCopying, NSSecureCoding |

Modified [HKHealthStore](https://developer.apple.com/documentation/healthkit/hkhealthstore)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore addSamples:toWorkout:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614165-addsamples)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addSamples:(NSArray *)samples toWorkout:(HKWorkout *)workout completion:(void (^)(BOOL success, NSError *error))completion ``` |
| To | ``` - (void)addSamples:(NSArray<HKSample *> * _Nonnull)samples toWorkout:(HKWorkout * _Nonnull)workout completion:(void (^ _Nonnull)(BOOL success, NSError * _Nullable error))completion ``` |

Modified [-[HKHealthStore authorizationStatusForType:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614154-authorizationstatusfortype)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore biologicalSexWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614171-biologicalsexwitherror)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore bloodTypeWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614164-bloodtype)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore dateOfBirthWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614160-dateofbirth)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore deleteObject:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614155-delete)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore executeQuery:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614179-execute)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [+[HKHealthStore isHealthDataAvailable]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614180-ishealthdataavailable)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore preferredUnitsForQuantityTypes:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614172-preferredunitsforquantitytypes)

|  | Declaration |
| --- | --- |
| From | ``` - (void)preferredUnitsForQuantityTypes:(NSSet *)quantityTypes completion:(void (^)(NSDictionary *preferredUnits, NSError *error))completion ``` |
| To | ``` - (void)preferredUnitsForQuantityTypes:(NSSet<HKQuantityType *> * _Nonnull)quantityTypes completion:(void (^ _Nonnull)(NSDictionary<HKQuantityType *,HKUnit *> * _Nonnull preferredUnits, NSError * _Nullable error))completion ``` |

Modified [-[HKHealthStore requestAuthorizationToShareTypes:readTypes:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization)

|  | Declaration | App Extension[Available] | App Extension[Message] |
| --- | --- | --- | --- |
| From | ``` - (void)requestAuthorizationToShareTypes:(NSSet *)typesToShare readTypes:(NSSet *)typesToRead completion:(void (^)(BOOL success, NSError *error))completion ``` | no | HealthKit is not supported in extensions |
| To | ``` - (void)requestAuthorizationToShareTypes:(NSSet<HKSampleType *> * _Nullable)typesToShare readTypes:(NSSet<HKObjectType *> * _Nullable)typesToRead completion:(void (^ _Nonnull)(BOOL success, NSError * _Nullable error))completion ``` | -- | -- |

Modified [-[HKHealthStore saveObject:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614168-save)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

Modified [-[HKHealthStore saveObjects:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614176-saveobjects)

|  | Declaration | App Extension[Available] | App Extension[Message] |
| --- | --- | --- | --- |
| From | ``` - (void)saveObjects:(NSArray *)objects withCompletion:(void (^)(BOOL success, NSError *error))completion ``` | no | HealthKit is not supported in extensions |
| To | ``` - (void)saveObjects:(NSArray<HKObject *> * _Nonnull)objects withCompletion:(void (^ _Nonnull)(BOOL success, NSError * _Nullable error))completion ``` | -- | -- |

Modified [-[HKHealthStore stopQuery:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614173-stopquery)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | no | HealthKit is not supported in extensions |
| To | -- | -- |

#### HKMetadata.h

Added [HKMetadataKeyMenstrualCycleStart](https://developer.apple.com/documentation/healthkit/hkmetadatakeymenstrualcyclestart)Added [HKMetadataKeySexualActivityProtectionUsed](https://developer.apple.com/documentation/healthkit/hkmetadatakeysexualactivityprotectionused)

#### HKObject.h

Added [HKObject.device](https://developer.apple.com/documentation/healthkit/hkobject/1615622-device)Added [HKObject.sourceRevision](https://developer.apple.com/documentation/healthkit/hkobject/1615483-sourcerevision)Added [HKPredicateKeyPathDevice](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathdevice)Added [HKPredicateKeyPathSourceRevision](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathsourcerevision)Modified [HKObject.metadata](https://developer.apple.com/documentation/healthkit/hkobject/1615598-metadata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSDictionary *metadata ``` |
| To | ``` @property(readonly, copy, nullable) NSDictionary<NSString *,id> *metadata ``` |

Modified [HKObject.source](https://developer.apple.com/documentation/healthkit/hkobject/1615781-source)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 9.0 |

#### HKQuantitySample.h

Added [+[HKQuantitySample quantitySampleWithType:quantity:startDate:endDate:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615019-init)Modified [+[HKQuantitySample quantitySampleWithType:quantity:startDate:endDate:metadata:]](https://developer.apple.com/documentation/healthkit/hkquantitysample/1615017-quantitysamplewithtype)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)quantitySampleWithType:(HKQuantityType *)quantityType quantity:(HKQuantity *)quantity startDate:(NSDate *)startDate endDate:(NSDate *)endDate metadata:(NSDictionary *)metadata ``` |
| To | ``` + (instancetype _Nonnull)quantitySampleWithType:(HKQuantityType * _Nonnull)quantityType quantity:(HKQuantity * _Nonnull)quantity startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate metadata:(NSDictionary<NSString *,id> * _Nullable)metadata ``` |

#### HKQuery.h

Added [+[HKQuery predicateForObjectsFromDevices:]](https://developer.apple.com/documentation/healthkit/hkquery/1614765-predicateforobjects)Added [+[HKQuery predicateForObjectsFromSourceRevisions:]](https://developer.apple.com/documentation/healthkit/hkquery/1614791-predicateforobjects)Added [+[HKQuery predicateForObjectsWithDeviceProperty:allowedValues:]](https://developer.apple.com/documentation/healthkit/hkquery/1614775-predicateforobjects)Modified [+[HKQuery predicateForObjectsFromSources:]](https://developer.apple.com/documentation/healthkit/hkquery/1614767-predicateforobjectsfromsources)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)predicateForObjectsFromSources:(NSSet *)sources ``` |
| To | ``` + (NSPredicate * _Nonnull)predicateForObjectsFromSources:(NSSet<HKSource *> * _Nonnull)sources ``` |

Modified [+[HKQuery predicateForObjectsWithUUIDs:]](https://developer.apple.com/documentation/healthkit/hkquery/1614785-predicateforobjectswithuuids)

|  | Declaration |
| --- | --- |
| From | ``` + (NSPredicate *)predicateForObjectsWithUUIDs:(NSSet *)UUIDs ``` |
| To | ``` + (NSPredicate * _Nonnull)predicateForObjectsWithUUIDs:(NSSet<NSUUID *> * _Nonnull)UUIDs ``` |

#### HKSampleQuery.h

Modified [-[HKSampleQuery initWithSampleType:predicate:limit:sortDescriptors:resultsHandler:]](https://developer.apple.com/documentation/healthkit/hksamplequery/1615055-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSampleType:(HKSampleType *)sampleType predicate:(NSPredicate *)predicate limit:(NSUInteger)limit sortDescriptors:(NSArray *)sortDescriptors resultsHandler:(void (^)(HKSampleQuery *query, NSArray *results, NSError *error))resultsHandler ``` |
| To | ``` - (instancetype _Nonnull)initWithSampleType:(HKSampleType * _Nonnull)sampleType predicate:(NSPredicate * _Nullable)predicate limit:(NSUInteger)limit sortDescriptors:(NSArray<NSSortDescriptor *> * _Nullable)sortDescriptors resultsHandler:(void (^ _Nonnull)(HKSampleQuery * _Nonnull query, NSArray<__kindof HKSample *> * _Nullable results, NSError * _Nullable error))resultsHandler ``` |

Modified [HKSampleQuery.sortDescriptors](https://developer.apple.com/documentation/healthkit/hksamplequery/1615128-sortdescriptors)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *sortDescriptors ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<NSSortDescriptor *> *sortDescriptors ``` |

#### HKSourceQuery.h

Modified [-[HKSourceQuery initWithSampleType:samplePredicate:completionHandler:]](https://developer.apple.com/documentation/healthkit/hksourcequery/1614367-initwithsampletype)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithSampleType:(HKSampleType *)sampleType samplePredicate:(NSPredicate *)objectPredicate completionHandler:(void (^)(HKSourceQuery *query, NSSet *sources, NSError *error))completionHandler ``` |
| To | ``` - (instancetype _Nonnull)initWithSampleType:(HKSampleType * _Nonnull)sampleType samplePredicate:(NSPredicate * _Nullable)objectPredicate completionHandler:(void (^ _Nonnull)(HKSourceQuery * _Nonnull query, NSSet<HKSource *> * _Nullable sources, NSError * _Nullable error))completionHandler ``` |

#### HKSourceRevision.h (Added)

Added [HKSourceRevision](https://developer.apple.com/documentation/healthkit/hksourcerevision)Added [-[HKSourceRevision initWithSource:version:]](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614799-init)Added [HKSourceRevision.source](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614797-source)Added [HKSourceRevision.version](https://developer.apple.com/documentation/healthkit/hksourcerevision/1614798-version)

#### HKStatistics.h

Modified [HKStatistics.sources](https://developer.apple.com/documentation/healthkit/hkstatistics/1615222-sources)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, strong) NSArray *sources ``` |
| To | ``` @property(readonly, strong, nullable) NSArray<HKSource *> *sources ``` |

#### HKStatisticsCollectionQuery.h

Modified [-[HKStatisticsCollection sources]](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615456-sources)

|  | Declaration |
| --- | --- |
| From | ``` - (NSSet *)sources ``` |
| To | ``` - (NSSet<HKSource *> * _Nonnull)sources ``` |

Modified [-[HKStatisticsCollection statistics]](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/1615550-statistics)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)statistics ``` |
| To | ``` - (NSArray<HKStatistics *> * _Nonnull)statistics ``` |

#### HKTypeIdentifiers.h

Added [HKCategoryTypeIdentifierAppleStandHour](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615539-applestandhour)Added [HKCategoryTypeIdentifierCervicalMucusQuality](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615429-cervicalmucusquality)Added [HKCategoryTypeIdentifierIntermenstrualBleeding](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615418-intermenstrualbleeding)Added [HKCategoryTypeIdentifierMenstrualFlow](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615136-menstrualflow)Added [HKCategoryTypeIdentifierOvulationTestResult](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615252-ovulationtestresult)Added [HKCategoryTypeIdentifierSexualActivity](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifiersexualactivity)Added [HKCharacteristicTypeIdentifierFitzpatrickSkinType](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifierfitzpatrickskintype)Added [HKQuantityTypeIdentifierBasalBodyTemperature](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierbasalbodytemperature)Added [HKQuantityTypeIdentifierDietaryWater](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615313-dietarywater)Added [HKQuantityTypeIdentifierUVExposure](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifieruvexposure)

#### HKUnit.h

Added [+[HKUnit cupImperialUnit]](https://developer.apple.com/documentation/healthkit/hkunit/1615506-cupimperialunit)Added [+[HKUnit cupUSUnit]](https://developer.apple.com/documentation/healthkit/hkunit/1615542-cupusunit)Added [+[HKUnit yardUnit]](https://developer.apple.com/documentation/healthkit/hkunit/1615106-yard)

#### HKWorkout.h

Added [+[HKWorkout workoutWithActivityType:startDate:endDate:duration:totalEnergyBurned:totalDistance:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkout/1615048-init)Added [+[HKWorkout workoutWithActivityType:startDate:endDate:workoutEvents:totalEnergyBurned:totalDistance:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkout/1615713-init)Modified [HKWorkout.workoutEvents](https://developer.apple.com/documentation/healthkit/hkworkout/1615424-workoutevents)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSArray *workoutEvents ``` |
| To | ``` @property(readonly, copy, nullable) NSArray<HKWorkoutEvent *> *workoutEvents ``` |

Modified [+[HKWorkout workoutWithActivityType:startDate:endDate:duration:totalEnergyBurned:totalDistance:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkout/1615739-init)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)workoutWithActivityType:(HKWorkoutActivityType)workoutActivityType startDate:(NSDate *)startDate endDate:(NSDate *)endDate duration:(NSTimeInterval)duration totalEnergyBurned:(HKQuantity *)totalEnergyBurned totalDistance:(HKQuantity *)totalDistance metadata:(NSDictionary *)metadata ``` |
| To | ``` + (instancetype _Nonnull)workoutWithActivityType:(HKWorkoutActivityType)workoutActivityType startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate duration:(NSTimeInterval)duration totalEnergyBurned:(HKQuantity * _Nullable)totalEnergyBurned totalDistance:(HKQuantity * _Nullable)totalDistance metadata:(NSDictionary<NSString *,id> * _Nullable)metadata ``` |

Modified [+[HKWorkout workoutWithActivityType:startDate:endDate:workoutEvents:totalEnergyBurned:totalDistance:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkout/1615212-workoutwithactivitytype)

|  | Declaration |
| --- | --- |
| From | ``` + (instancetype)workoutWithActivityType:(HKWorkoutActivityType)workoutActivityType startDate:(NSDate *)startDate endDate:(NSDate *)endDate workoutEvents:(NSArray *)workoutEvents totalEnergyBurned:(HKQuantity *)totalEnergyBurned totalDistance:(HKQuantity *)totalDistance metadata:(NSDictionary *)metadata ``` |
| To | ``` + (instancetype _Nonnull)workoutWithActivityType:(HKWorkoutActivityType)workoutActivityType startDate:(NSDate * _Nonnull)startDate endDate:(NSDate * _Nonnull)endDate workoutEvents:(NSArray<HKWorkoutEvent *> * _Nullable)workoutEvents totalEnergyBurned:(HKQuantity * _Nullable)totalEnergyBurned totalDistance:(HKQuantity * _Nullable)totalDistance metadata:(NSDictionary<NSString *,id> * _Nullable)metadata ``` |

#### HKWorkoutSession.h (Added)

Added [HKWorkoutSessionLocationType](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype)Added [HKWorkoutSessionState](https://developer.apple.com/documentation/healthkit/hkworkoutsessionstate)

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

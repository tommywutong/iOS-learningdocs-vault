---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/HealthKit.html
archived_at: '2026-07-18T02:54:56.172415Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# HealthKit Changes for Objective-C

### HealthKit

#### HKCDADocumentSample.h (Added)

Added [HKCDADocument](https://developer.apple.com/documentation/healthkit/hkcdadocument)Added [HKCDADocument.authorName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779381-authorname)Added [HKCDADocument.custodianName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779390-custodianname)Added [HKCDADocument.documentData](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779391-documentdata)Added [HKCDADocument.patientName](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779384-patientname)Added [HKCDADocument.title](https://developer.apple.com/documentation/healthkit/hkcdadocument/1779387-title)Added [HKCDADocumentSample](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample)Added [+[HKCDADocumentSample CDADocumentSampleWithData:startDate:endDate:metadata:validationError:]](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/1779395-init)Added [HKCDADocumentSample.document](https://developer.apple.com/documentation/healthkit/hkcdadocumentsample/1779383-document)Added [HKDetailedCDAValidationErrorKey](https://developer.apple.com/documentation/healthkit/hkdetailedcdavalidationerrorkey)Added [HKPredicateKeyPathCDAAuthorName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdaauthorname)Added [HKPredicateKeyPathCDACustodianName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdacustodianname)Added [HKPredicateKeyPathCDAPatientName](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdapatientname)Added [HKPredicateKeyPathCDATitle](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathcdatitle)

#### HKCharacteristicObjects.h (Added)

Added [HKWheelchairUseObject](https://developer.apple.com/documentation/healthkit/hkwheelchairuseobject)Added [HKWheelchairUseObject.wheelchairUse](https://developer.apple.com/documentation/healthkit/hkwheelchairuseobject/1649241-wheelchairuse)Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBiologicalSexObject.biologicalSex](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject/1614157-biologicalsex)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBloodTypeObject.bloodType](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject/1614167-bloodtype)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKFitzpatrickSkinTypeObject.skinType](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject/1614174-skintype)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

#### HKDefines.h

Removed #def HK_CLASS_AVAILABLE_IOSAdded #def HK_AVAILABLE_IOS_ONLYAdded #def HK_CLASS_AVAILABLE_IOS_ONLYAdded [HKCategoryValueSleepAnalysisAwake](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/hkcategoryvaluesleepanalysisawake)Added [HKWheelchairUse](https://developer.apple.com/documentation/healthkit/hkwheelchairuse)Added [HKWheelchairUseNo](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/hkwheelchairuseno)Added [HKWheelchairUseNotSet](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/notset)Added [HKWheelchairUseYes](https://developer.apple.com/documentation/healthkit/hkwheelchairuse/hkwheelchairuseyes)

#### HKDocumentQuery.h (Added)

Added [HKDocumentQuery](https://developer.apple.com/documentation/healthkit/hkdocumentquery)Added [HKDocumentQuery.includeDocumentData](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779564-includedocumentdata)Added [-[HKDocumentQuery initWithDocumentType:predicate:limit:sortDescriptors:includeDocumentData:resultsHandler:]](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779561-initwithdocumenttype)Added [HKDocumentQuery.limit](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779563-limit)Added [HKDocumentQuery.sortDescriptors](https://developer.apple.com/documentation/healthkit/hkdocumentquery/1779560-sortdescriptors)

#### HKDocumentSample.h (Added)

Added [HKDocumentSample](https://developer.apple.com/documentation/healthkit/hkdocumentsample)Added [HKDocumentSample.documentType](https://developer.apple.com/documentation/healthkit/hkdocumentsample/1779250-documenttype)

#### HKHealthStore.h

Added [-[HKHealthStore dateOfBirthComponentsWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648357-dateofbirthcomponentswitherror)Added [-[HKHealthStore startWatchAppWithWorkoutConfiguration:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648358-startwatchappwithworkoutconfigur)Added [-[HKHealthStore wheelchairUseWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1648356-wheelchairuse)Modified [HKBiologicalSexObject](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBiologicalSexObject.biologicalSex](https://developer.apple.com/documentation/healthkit/hkbiologicalsexobject/1614157-biologicalsex)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBloodTypeObject](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKBloodTypeObject.bloodType](https://developer.apple.com/documentation/healthkit/hkbloodtypeobject/1614167-bloodtype)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKFitzpatrickSkinTypeObject](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [HKFitzpatrickSkinTypeObject.skinType](https://developer.apple.com/documentation/healthkit/hkfitzpatrickskintypeobject/1614174-skintype)

|  | Header |
| --- | --- |
| From | HealthKit/HKHealthStore.h |
| To | HealthKit/HKCharacteristicObjects.h |

Modified [-[HKHealthStore dateOfBirthWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614160-dateofbirth)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### HKMetadata.h

Added [HKMetadataKeyLapLength](https://developer.apple.com/documentation/healthkit/hkmetadatakeylaplength)Added [HKMetadataKeySwimmingLocationType](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimminglocationtype)Added [HKMetadataKeySwimmingStrokeStyle](https://developer.apple.com/documentation/healthkit/hkmetadatakeyswimmingstrokestyle)Added [HKMetadataKeyWeatherCondition](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathercondition)Added [HKMetadataKeyWeatherHumidity](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweatherhumidity)Added [HKMetadataKeyWeatherTemperature](https://developer.apple.com/documentation/healthkit/hkmetadatakeyweathertemperature)Added [HKSwimmingStrokeStyle](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle)Added [HKSwimmingStrokeStyleBackstroke](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/backstroke)Added [HKSwimmingStrokeStyleBreaststroke](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylebreaststroke)Added [HKSwimmingStrokeStyleButterfly](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylebutterfly)Added [HKSwimmingStrokeStyleFreestyle](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/freestyle)Added [HKSwimmingStrokeStyleMixed](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestylemixed)Added [HKSwimmingStrokeStyleUnknown](https://developer.apple.com/documentation/healthkit/hkswimmingstrokestyle/hkswimmingstrokestyleunknown)Added [HKWeatherCondition](https://developer.apple.com/documentation/healthkit/hkweathercondition)Added [HKWeatherConditionBlustery](https://developer.apple.com/documentation/healthkit/hkweathercondition/blustery)Added [HKWeatherConditionClear](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionclear)Added [HKWeatherConditionCloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditioncloudy)Added [HKWeatherConditionDrizzle](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiondrizzle)Added [HKWeatherConditionDust](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiondust)Added [HKWeatherConditionFair](https://developer.apple.com/documentation/healthkit/hkweathercondition/fair)Added [HKWeatherConditionFoggy](https://developer.apple.com/documentation/healthkit/hkweathercondition/foggy)Added [HKWeatherConditionFreezingDrizzle](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionfreezingdrizzle)Added [HKWeatherConditionFreezingRain](https://developer.apple.com/documentation/healthkit/hkweathercondition/freezingrain)Added [HKWeatherConditionHail](https://developer.apple.com/documentation/healthkit/hkweathercondition/hail)Added [HKWeatherConditionHaze](https://developer.apple.com/documentation/healthkit/hkweathercondition/haze)Added [HKWeatherConditionHurricane](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionhurricane)Added [HKWeatherConditionMixedRainAndHail](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedrainandhail)Added [HKWeatherConditionMixedRainAndSleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedrainandsleet)Added [HKWeatherConditionMixedRainAndSnow](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedrainandsnow)Added [HKWeatherConditionMixedSnowAndSleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/mixedsnowandsleet)Added [HKWeatherConditionMostlyCloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionmostlycloudy)Added [HKWeatherConditionNone](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionnone)Added [HKWeatherConditionPartlyCloudy](https://developer.apple.com/documentation/healthkit/hkweathercondition/partlycloudy)Added [HKWeatherConditionScatteredShowers](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionscatteredshowers)Added [HKWeatherConditionShowers](https://developer.apple.com/documentation/healthkit/hkweathercondition/showers)Added [HKWeatherConditionSleet](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionsleet)Added [HKWeatherConditionSmoky](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionsmoky)Added [HKWeatherConditionSnow](https://developer.apple.com/documentation/healthkit/hkweathercondition/snow)Added [HKWeatherConditionThunderstorms](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditionthunderstorms)Added [HKWeatherConditionTornado](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiontornado)Added [HKWeatherConditionTropicalStorm](https://developer.apple.com/documentation/healthkit/hkweathercondition/hkweatherconditiontropicalstorm)Added [HKWeatherConditionWindy](https://developer.apple.com/documentation/healthkit/hkweathercondition/windy)Added [HKWorkoutSwimmingLocationType](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype)Added [HKWorkoutSwimmingLocationTypeOpenWater](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/hkworkoutswimminglocationtypeopenwater)Added [HKWorkoutSwimmingLocationTypePool](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/pool)Added [HKWorkoutSwimmingLocationTypeUnknown](https://developer.apple.com/documentation/healthkit/hkworkoutswimminglocationtype/hkworkoutswimminglocationtypeunknown)

#### HKObjectType.h

Added [HKDocumentType](https://developer.apple.com/documentation/healthkit/hkdocumenttype)Added [+[HKObjectType documentTypeForIdentifier:]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1778757-documenttype)Modified [+[HKObjectType categoryTypeForIdentifier:]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615526-categorytypeforidentifier)

|  | Declaration |
| --- | --- |
| From | ``` + (HKCategoryType *)categoryTypeForIdentifier:(NSString *)identifier ``` |
| To | ``` + (HKCategoryType *)categoryTypeForIdentifier:(HKCategoryTypeIdentifier)identifier ``` |

Modified [+[HKObjectType characteristicTypeForIdentifier:]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615558-characteristictype)

|  | Declaration |
| --- | --- |
| From | ``` + (HKCharacteristicType *)characteristicTypeForIdentifier:(NSString *)identifier ``` |
| To | ``` + (HKCharacteristicType *)characteristicTypeForIdentifier:(HKCharacteristicTypeIdentifier)identifier ``` |

Modified [+[HKObjectType correlationTypeForIdentifier:]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615580-correlationtype)

|  | Declaration |
| --- | --- |
| From | ``` + (HKCorrelationType *)correlationTypeForIdentifier:(NSString *)identifier ``` |
| To | ``` + (HKCorrelationType *)correlationTypeForIdentifier:(HKCorrelationTypeIdentifier)identifier ``` |

Modified [+[HKObjectType quantityTypeForIdentifier:]](https://developer.apple.com/documentation/healthkit/hkobjecttype/1615298-quantitytype)

|  | Declaration |
| --- | --- |
| From | ``` + (HKQuantityType *)quantityTypeForIdentifier:(NSString *)identifier ``` |
| To | ``` + (HKQuantityType *)quantityTypeForIdentifier:(HKQuantityTypeIdentifier)identifier ``` |

#### HKQuery.h

Added [+[HKQuery predicateForWorkoutsWithOperatorType:totalSwimmingStrokeCount:]](https://developer.apple.com/documentation/healthkit/hkquery/2344688-predicateforworkoutswithoperator)

#### HKTypeIdentifiers.h

Added [HKCategoryTypeIdentifier](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier)Added [HKCategoryTypeIdentifierMindfulSession](https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifiermindfulsession)Added [HKCharacteristicTypeIdentifier](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier)Added [HKCharacteristicTypeIdentifierWheelchairUse](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier/1648572-wheelchairuse)Added [HKCorrelationTypeIdentifier](https://developer.apple.com/documentation/healthkit/hkcorrelationtypeidentifier)Added [HKDocumentTypeIdentifier](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifier)Added [HKDocumentTypeIdentifierCDA](https://developer.apple.com/documentation/healthkit/hkdocumenttypeidentifiercda)Added [HKQuantityTypeIdentifier](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier)Added [HKQuantityTypeIdentifierDistanceSwimming](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/2344686-distanceswimming)Added [HKQuantityTypeIdentifierDistanceWheelchair](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1771741-distancewheelchair)Added [HKQuantityTypeIdentifierPushCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierpushcount)Added [HKQuantityTypeIdentifierSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifierswimmingstrokecount)

#### HKWorkout.h

Added [HKWorkout.totalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkworkout/2341561-totalswimmingstrokecount)Added [+[HKWorkout workoutWithActivityType:startDate:endDate:workoutEvents:totalEnergyBurned:totalDistance:totalSwimmingStrokeCount:device:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkout/2341569-workoutwithactivitytype)Added [HKWorkoutEvent.metadata](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1649817-metadata)Added [+[HKWorkoutEvent workoutEventWithType:date:metadata:]](https://developer.apple.com/documentation/healthkit/hkworkoutevent/1649819-init)Added [HKPredicateKeyPathWorkoutTotalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathworkouttotalswimmingstrokecount)Added [HKWorkoutActivityTypeBarre](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypebarre)Added [HKWorkoutActivityTypeCoreTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypecoretraining)Added [HKWorkoutActivityTypeCrossCountrySkiing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/crosscountryskiing)Added [HKWorkoutActivityTypeDownhillSkiing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypedownhillskiing)Added [HKWorkoutActivityTypeFlexibility](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/flexibility)Added [HKWorkoutActivityTypeHighIntensityIntervalTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/highintensityintervaltraining)Added [HKWorkoutActivityTypeJumpRope](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypejumprope)Added [HKWorkoutActivityTypeKickboxing](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/kickboxing)Added [HKWorkoutActivityTypePilates](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypepilates)Added [HKWorkoutActivityTypeSnowboarding](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/snowboarding)Added [HKWorkoutActivityTypeStairs](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypestairs)Added [HKWorkoutActivityTypeStepTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/steptraining)Added [HKWorkoutActivityTypeWheelchairRunPace](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypewheelchairrunpace)Added [HKWorkoutActivityTypeWheelchairWalkPace](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/wheelchairwalkpace)Added [HKWorkoutEventTypeLap](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/lap)Added [HKWorkoutEventTypeMarker](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/marker)Added [HKWorkoutEventTypeMotionPaused](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypemotionpaused)Added [HKWorkoutEventTypeMotionResumed](https://developer.apple.com/documentation/healthkit/hkworkouteventtype/hkworkouteventtypemotionresumed)Added [HKWorkoutSortIdentifierTotalSwimmingStrokeCount](https://developer.apple.com/documentation/healthkit/hkworkoutsortidentifiertotalswimmingstrokecount)Modified [HKWorkoutEvent](https://developer.apple.com/documentation/healthkit/hkworkoutevent)

|  | Protocols |
| --- | --- |
| From | NSSecureCoding |
| To | NSCopying, NSSecureCoding |

Modified [HKWorkoutActivityTypeDanceInspiredTraining](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypedanceinspiredtraining)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 10.0 |

#### HKWorkoutSession.h

Added [HKWorkoutConfiguration](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration)Added [HKWorkoutConfiguration.activityType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/1649492-activitytype)Added [HKWorkoutConfiguration.lapLength](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/2342795-laplength)Added [HKWorkoutConfiguration.locationType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/1649491-locationtype)Added [HKWorkoutConfiguration.swimmingLocationType](https://developer.apple.com/documentation/healthkit/hkworkoutconfiguration/2342785-swimminglocationtype)Added [HKWorkoutSessionLocationTypeIndoor](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/indoor)Added [HKWorkoutSessionLocationTypeOutdoor](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/outdoor)Added [HKWorkoutSessionLocationTypeUnknown](https://developer.apple.com/documentation/healthkit/hkworkoutsessionlocationtype/hkworkoutsessionlocationtypeunknown)

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

---
title: iOS 8.2 API Diffs
apple_id: TP40015021
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS82APIDiffs/frameworks/HealthKit.html
archived_at: '2026-07-18T02:56:18.765869Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.2 API Diffs](iOS%208.1%20to%20iOS%208.2%20API%20Differences.md)


# HealthKit Changes

## HealthKit

HKDefines.hAdded [HKBiologicalSexOther](https://developer.apple.com/documentation/healthkit/hkbiologicalsex/hkbiologicalsexother)HKHealthStore.hAdded [-[HKHealthStore preferredUnitsForQuantityTypes:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614172-preferredunitsforquantitytypes)Added HKHealthStore(HKUserPreferences)Added [HKUserPreferencesDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1614169-hkuserpreferencesdidchange)Modified [-[HKHealthStore authorizationStatusForType:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614154-authorizationstatusfortype)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore biologicalSexWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614171-biologicalsexwitherror)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore bloodTypeWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614164-bloodtype)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore dateOfBirthWithError:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614160-dateofbirth)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore deleteObject:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614155-delete)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore executeQuery:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614179-execute)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [+[HKHealthStore isHealthDataAvailable]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614180-ishealthdataavailable)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore requestAuthorizationToShareTypes:readTypes:completion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614152-requestauthorization)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore saveObject:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614168-save)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore saveObjects:withCompletion:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614176-saveobjects)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

Modified [-[HKHealthStore stopQuery:]](https://developer.apple.com/documentation/healthkit/hkhealthstore/1614173-stopquery)

|  | App Extension[Available] | App Extension[Message] |
| --- | --- | --- |
| From | -- | -- |
| To | no | HealthKit is not supported in extensions |

HKUnit.hModified [HKUnit](https://developer.apple.com/documentation/healthkit/hkunit)

|  | Protocols |
| --- | --- |
| From | NSSecureCoding |
| To | NSCopying, NSSecureCoding |

HKWorkout.hAdded [HKWorkoutActivityTypeOther](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/hkworkoutactivitytypeother)

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

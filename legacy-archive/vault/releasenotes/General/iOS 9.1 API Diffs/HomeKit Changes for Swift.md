---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/HomeKit.html
archived_at: '2026-07-18T02:57:08.955990Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# HomeKit Changes for Swift

### HomeKit

Modified [HMAccessory](https://developer.apple.com/documentation/homekit/hmaccessory)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMAccessoryBrowser](https://developer.apple.com/documentation/homekit/hmaccessorybrowser)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMAccessoryCategory](https://developer.apple.com/documentation/homekit/hmaccessorycategory)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMAction](https://developer.apple.com/documentation/homekit/hmaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMActionSet](https://developer.apple.com/documentation/homekit/hmactionset)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMCharacteristic](https://developer.apple.com/documentation/homekit/hmcharacteristic)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMCharacteristicEvent](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMCharacteristicMetadata](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadata)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMCharacteristicValueAirParticulateSize [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairparticulatesize)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueAirQuality [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueairquality)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueCurrentSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluecurrentsecuritysystemstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueDoorState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluedoorstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueHeatingCooling [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvalueheatingcooling)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueLockMechanismLastKnownAction [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismlastknownaction)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueLockMechanismState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluelockmechanismstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValuePositionState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluepositionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueRotationDirection [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluerotationdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueTargetSecuritySystemState [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetargetsecuritysystemstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicValueTemperatureUnit [enum]](https://developer.apple.com/documentation/homekit/hmcharacteristicvaluetemperatureunit)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [HMCharacteristicWriteAction](https://developer.apple.com/documentation/homekit/hmcharacteristicwriteaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMErrorCode [enum]](https://developer.apple.com/documentation/homekit/hmerror/code)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices } extension HMErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension HMErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices } extension HMErrorCode : _BridgedNSError { } extension HMErrorCode : _BridgedNSError { } ``` | -- |

Modified [HMEvent](https://developer.apple.com/documentation/homekit/hmevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMEventTrigger](https://developer.apple.com/documentation/homekit/hmeventtrigger)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMHome](https://developer.apple.com/documentation/homekit/hmhome)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMHomeAccessControl](https://developer.apple.com/documentation/homekit/hmhomeaccesscontrol)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMHomeManager](https://developer.apple.com/documentation/homekit/hmhomemanager)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMLocationEvent](https://developer.apple.com/documentation/homekit/hmlocationevent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMRoom](https://developer.apple.com/documentation/homekit/hmroom)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMService](https://developer.apple.com/documentation/homekit/hmservice)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMServiceGroup](https://developer.apple.com/documentation/homekit/hmservicegroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMTimerTrigger](https://developer.apple.com/documentation/homekit/hmtimertrigger)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMTrigger](https://developer.apple.com/documentation/homekit/hmtrigger)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMUser](https://developer.apple.com/documentation/homekit/hmuser)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [HMZone](https://developer.apple.com/documentation/homekit/hmzone)

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

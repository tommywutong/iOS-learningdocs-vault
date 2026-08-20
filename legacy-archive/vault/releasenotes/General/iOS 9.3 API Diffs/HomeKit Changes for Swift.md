---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/HomeKit.html
archived_at: '2026-07-18T02:57:15.956242Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# HomeKit Changes for Swift

### HomeKit

Added [HMErrorCode.ReferToUserManual](https://developer.apple.com/documentation/homekit/hmerrorcode/hmerrorcoderefertousermanual)Added [HMAccessoryCategoryTypeRangeExtender](https://developer.apple.com/documentation/homekit/hmaccessorycategorytyperangeextender)Added [HMCharacteristicMetadataUnitsLux](https://developer.apple.com/documentation/homekit/hmcharacteristicmetadataunitslux)Added [HMCharacteristicPropertyHidden](https://developer.apple.com/documentation/homekit/hmcharacteristicpropertyhidden)Modified [HMErrorCode [enum]](https://developer.apple.com/documentation/homekit/hmerror/code)

|  | Declaration |
| --- | --- |
| From | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices } extension HMErrorCode : _BridgedNSError { } extension HMErrorCode : _BridgedNSError { } ``` |
| To | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked     case CannotRemoveBuiltinActionSet     case LocationForHomeDisabled     case NotAuthorizedForLocationServices     case ReferToUserManual } extension HMErrorCode : _BridgedNSError { } extension HMErrorCode : _BridgedNSError { } ``` |

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

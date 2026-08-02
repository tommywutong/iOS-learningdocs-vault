---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/HomeKit.html
archived_at: '2026-07-18T02:56:26.099905Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# HomeKit Changes

## HomeKit

Removed HMCharacteristicValueLockMechanism [enum]Removed HMCharacteristicValueLockMechanism.LastKnownActionSecuredRemotelyRemoved HMCharacteristicValueLockMechanism.LastKnownActionSecuredUsingPhysicalMovementExteriorRemoved HMCharacteristicValueLockMechanism.LastKnownActionSecuredUsingPhysicalMovementInteriorRemoved HMCharacteristicValueLockMechanism.LastKnownActionSecuredWithAutomaticSecureTimeoutRemoved HMCharacteristicValueLockMechanism.LastKnownActionSecuredWithKeypadRemoved HMCharacteristicValueLockMechanism.LastKnownActionUnsecuredRemotelyRemoved HMCharacteristicValueLockMechanism.LastKnownActionUnsecuredUsingPhysicalMovementExteriorRemoved HMCharacteristicValueLockMechanism.LastKnownActionUnsecuredUsingPhysicalMovementInteriorRemoved HMCharacteristicValueLockMechanism.LastKnownActionUnsecuredWithKeypadAdded HMCharacteristicValueLockMechanismLastKnownAction [enum]Added HMCharacteristicValueLockMechanismLastKnownAction.SecuredRemotelyAdded HMCharacteristicValueLockMechanismLastKnownAction.SecuredUsingPhysicalMovementAdded HMCharacteristicValueLockMechanismLastKnownAction.SecuredUsingPhysicalMovementExteriorAdded HMCharacteristicValueLockMechanismLastKnownAction.SecuredUsingPhysicalMovementInteriorAdded HMCharacteristicValueLockMechanismLastKnownAction.SecuredWithAutomaticSecureTimeoutAdded HMCharacteristicValueLockMechanismLastKnownAction.SecuredWithKeypadAdded HMCharacteristicValueLockMechanismLastKnownAction.UnsecuredRemotelyAdded HMCharacteristicValueLockMechanismLastKnownAction.UnsecuredUsingPhysicalMovementAdded HMCharacteristicValueLockMechanismLastKnownAction.UnsecuredUsingPhysicalMovementExteriorAdded HMCharacteristicValueLockMechanismLastKnownAction.UnsecuredUsingPhysicalMovementInteriorAdded HMCharacteristicValueLockMechanismLastKnownAction.UnsecuredWithKeypadAdded HMErrorCode.CannotUnblockNonBridgeAccessoryAdded HMErrorCode.DeviceLockedAdded HMCharacteristicMetadataUnitsSecondsModified HMAccessory.delegate

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: HMAccessoryDelegate! ``` |
| To | ``` weak var delegate: HMAccessoryDelegate? ``` |

Modified HMAccessoryBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: HMAccessoryBrowserDelegate! ``` |
| To | ``` weak var delegate: HMAccessoryBrowserDelegate? ``` |

Modified HMAccessoryBrowserDelegate.accessoryBrowser(HMAccessoryBrowser, didFindNewAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser!, didFindNewAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didFindNewAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMAccessoryBrowserDelegate.accessoryBrowser(HMAccessoryBrowser, didRemoveNewAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser!, didRemoveNewAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func accessoryBrowser(_ browser: HMAccessoryBrowser, didRemoveNewAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessory(HMAccessory, didUpdateAssociatedServiceTypeForService: HMService!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory!, didUpdateAssociatedServiceTypeForService service: HMService!) ``` | iOS 8.0 |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateAssociatedServiceTypeForService service: HMService!) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessory(HMAccessory, didUpdateNameForService: HMService!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory!, didUpdateNameForService service: HMService!) ``` | iOS 8.0 |
| To | ``` optional func accessory(_ accessory: HMAccessory, didUpdateNameForService service: HMService!) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessory(HMAccessory, service: HMService!, didUpdateValueForCharacteristic: HMCharacteristic!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessory(_ accessory: HMAccessory!, service service: HMService!, didUpdateValueForCharacteristic characteristic: HMCharacteristic!) ``` | iOS 8.0 |
| To | ``` optional func accessory(_ accessory: HMAccessory, service service: HMService!, didUpdateValueForCharacteristic characteristic: HMCharacteristic!) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessoryDidUpdateName(HMAccessory)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessoryDidUpdateName(_ accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func accessoryDidUpdateName(_ accessory: HMAccessory) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessoryDidUpdateReachability(HMAccessory)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessoryDidUpdateReachability(_ accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func accessoryDidUpdateReachability(_ accessory: HMAccessory) ``` | iOS 8.3 |

Modified HMAccessoryDelegate.accessoryDidUpdateServices(HMAccessory)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func accessoryDidUpdateServices(_ accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func accessoryDidUpdateServices(_ accessory: HMAccessory) ``` | iOS 8.3 |

Modified HMActionSet.actions

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var actions: NSSet! { get } ``` |
| To | ``` var actions: Set<NSObject>! { get } ``` |

Modified HMErrorCode [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement } ``` |
| To | ``` enum HMErrorCode : Int {     case AlreadyExists     case NotFound     case InvalidParameter     case AccessoryNotReachable     case ReadOnlyCharacteristic     case WriteOnlyCharacteristic     case NotificationNotSupported     case OperationTimedOut     case AccessoryPoweredOff     case AccessDenied     case ObjectAssociatedToAnotherHome     case ObjectNotAssociatedToAnyHome     case ObjectAlreadyAssociatedToHome     case AccessoryIsBusy     case OperationInProgress     case AccessoryOutOfResources     case InsufficientPrivileges     case AccessoryPairingFailed     case InvalidDataFormatSpecified     case NilParameter     case UnconfiguredParameter     case InvalidClass     case OperationCancelled     case RoomForHomeCannotBeInZone     case NoActionsInActionSet     case NoRegisteredActionSets     case MissingParameter     case FireDateInPast     case RoomForHomeCannotBeUpdated     case ActionInAnotherActionSet     case ObjectWithSimilarNameExistsInHome     case HomeWithSimilarNameExists     case RenameWithSimilarName     case CannotRemoveNonBridgeAccessory     case NameContainsProhibitedCharacters     case NameDoesNotStartWithValidCharacters     case UserIDNotEmailAddress     case UserDeclinedAddingUser     case UserDeclinedRemovingUser     case UserDeclinedInvite     case UserManagementFailed     case RecurrenceTooSmall     case InvalidValueType     case ValueLowerThanMinimum     case ValueHigherThanMaximum     case StringLongerThanMaximum     case HomeAccessNotAuthorized     case OperationNotSupported     case MaximumObjectLimitReached     case AccessorySentInvalidResponse     case StringShorterThanMinimum     case GenericError     case SecurityFailure     case CommunicationFailure     case MessageAuthenticationFailed     case InvalidMessageSize     case AccessoryDiscoveryFailed     case ClientRequestError     case AccessoryResponseError     case NameDoesNotEndWithValidCharacters     case AccessoryIsBlocked     case InvalidAssociatedServiceType     case ActionSetExecutionFailed     case ActionSetExecutionPartialSuccess     case ActionSetExecutionInProgress     case AccessoryOutOfCompliance     case DataResetFailure     case NotificationAlreadyEnabled     case RecurrenceMustBeOnSpecifiedBoundaries     case DateMustBeOnSpecifiedBoundaries     case CannotActivateTriggerTooFarInFuture     case RecurrenceTooLarge     case ReadWritePartialSuccess     case ReadWriteFailure     case NotSignedIntoiCloud     case KeychainSyncNotEnabled     case CloudDataSyncInProgress     case NetworkUnavailable     case AddAccessoryFailed     case MissingEntitlement     case CannotUnblockNonBridgeAccessory     case DeviceLocked } ``` |

Modified HMHome.delegate

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: HMHomeDelegate! ``` |
| To | ``` weak var delegate: HMHomeDelegate? ``` |

Modified HMHomeDelegate.home(HMHome, didAddAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddActionSet: HMActionSet!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddActionSet actionSet: HMActionSet!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddActionSet actionSet: HMActionSet!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddRoom: HMRoom!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddRoom room: HMRoom!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddRoom: HMRoom!, toZone: HMZone!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddRoom room: HMRoom!, toZone zone: HMZone!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddRoom room: HMRoom!, toZone zone: HMZone!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddService: HMService!, toServiceGroup: HMServiceGroup!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddService service: HMService!, toServiceGroup group: HMServiceGroup!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddService service: HMService!, toServiceGroup group: HMServiceGroup!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddServiceGroup: HMServiceGroup!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddServiceGroup group: HMServiceGroup!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddServiceGroup group: HMServiceGroup!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddTrigger: HMTrigger!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddTrigger trigger: HMTrigger!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddTrigger trigger: HMTrigger!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddUser: HMUser!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddUser user: HMUser!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddUser user: HMUser!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didAddZone: HMZone!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didAddZone zone: HMZone!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didAddZone zone: HMZone!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didEncounterError: NSError!, forAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didEncounterError error: NSError!, forAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didEncounterError error: NSError!, forAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveActionSet: HMActionSet!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveActionSet actionSet: HMActionSet!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveActionSet actionSet: HMActionSet!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveRoom: HMRoom!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveRoom room: HMRoom!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveRoom: HMRoom!, fromZone: HMZone!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveRoom room: HMRoom!, fromZone zone: HMZone!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveRoom room: HMRoom!, fromZone zone: HMZone!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveService: HMService!, fromServiceGroup: HMServiceGroup!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveService service: HMService!, fromServiceGroup group: HMServiceGroup!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveService service: HMService!, fromServiceGroup group: HMServiceGroup!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveServiceGroup: HMServiceGroup!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveServiceGroup group: HMServiceGroup!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveServiceGroup group: HMServiceGroup!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveTrigger: HMTrigger!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveTrigger trigger: HMTrigger!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveTrigger trigger: HMTrigger!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveUser: HMUser!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveUser user: HMUser!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveUser user: HMUser!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didRemoveZone: HMZone!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didRemoveZone zone: HMZone!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didRemoveZone zone: HMZone!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUnblockAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUnblockAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUnblockAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateActionsForActionSet: HMActionSet!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateActionsForActionSet actionSet: HMActionSet!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateActionsForActionSet actionSet: HMActionSet!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateNameForActionSet: HMActionSet!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateNameForActionSet actionSet: HMActionSet!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForActionSet actionSet: HMActionSet!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateNameForRoom: HMRoom!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateNameForRoom room: HMRoom!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForRoom room: HMRoom!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateNameForServiceGroup: HMServiceGroup!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateNameForServiceGroup group: HMServiceGroup!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForServiceGroup group: HMServiceGroup!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateNameForTrigger: HMTrigger!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateNameForTrigger trigger: HMTrigger!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForTrigger trigger: HMTrigger!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateNameForZone: HMZone!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateNameForZone zone: HMZone!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateNameForZone zone: HMZone!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateRoom: HMRoom!, forAccessory: HMAccessory!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateRoom room: HMRoom!, forAccessory accessory: HMAccessory!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateRoom room: HMRoom!, forAccessory accessory: HMAccessory!) ``` | iOS 8.3 |

Modified HMHomeDelegate.home(HMHome, didUpdateTrigger: HMTrigger!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func home(_ home: HMHome!, didUpdateTrigger trigger: HMTrigger!) ``` | iOS 8.0 |
| To | ``` optional func home(_ home: HMHome, didUpdateTrigger trigger: HMTrigger!) ``` | iOS 8.3 |

Modified HMHomeDelegate.homeDidUpdateName(HMHome)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func homeDidUpdateName(_ home: HMHome!) ``` | iOS 8.0 |
| To | ``` optional func homeDidUpdateName(_ home: HMHome) ``` | iOS 8.3 |

Modified HMHomeManager.delegate

|  | Declaration |
| --- | --- |
| From | ``` weak var delegate: HMHomeManagerDelegate! ``` |
| To | ``` weak var delegate: HMHomeManagerDelegate? ``` |

Modified HMHomeManagerDelegate.homeManager(HMHomeManager, didAddHome: HMHome!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager!, didAddHome home: HMHome!) ``` | iOS 8.0 |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didAddHome home: HMHome!) ``` | iOS 8.3 |

Modified HMHomeManagerDelegate.homeManager(HMHomeManager, didRemoveHome: HMHome!)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func homeManager(_ manager: HMHomeManager!, didRemoveHome home: HMHome!) ``` | iOS 8.0 |
| To | ``` optional func homeManager(_ manager: HMHomeManager, didRemoveHome home: HMHome!) ``` | iOS 8.3 |

Modified HMHomeManagerDelegate.homeManagerDidUpdateHomes(HMHomeManager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager!) ``` | iOS 8.0 |
| To | ``` optional func homeManagerDidUpdateHomes(_ manager: HMHomeManager) ``` | iOS 8.3 |

Modified HMHomeManagerDelegate.homeManagerDidUpdatePrimaryHome(HMHomeManager)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager!) ``` | iOS 8.0 |
| To | ``` optional func homeManagerDidUpdatePrimaryHome(_ manager: HMHomeManager) ``` | iOS 8.3 |

Modified HMCharacteristicMetadataFormatArray

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatArray: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatArray: String ``` |

Modified HMCharacteristicMetadataFormatBool

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatBool: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatBool: String ``` |

Modified HMCharacteristicMetadataFormatData

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatData: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatData: String ``` |

Modified HMCharacteristicMetadataFormatDictionary

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatDictionary: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatDictionary: String ``` |

Modified HMCharacteristicMetadataFormatFloat

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatFloat: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatFloat: String ``` |

Modified HMCharacteristicMetadataFormatInt

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatInt: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatInt: String ``` |

Modified HMCharacteristicMetadataFormatString

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatString: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatString: String ``` |

Modified HMCharacteristicMetadataFormatTLV8

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatTLV8: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatTLV8: String ``` |

Modified HMCharacteristicMetadataFormatUInt16

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatUInt16: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatUInt16: String ``` |

Modified HMCharacteristicMetadataFormatUInt32

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatUInt32: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatUInt32: String ``` |

Modified HMCharacteristicMetadataFormatUInt64

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatUInt64: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatUInt64: String ``` |

Modified HMCharacteristicMetadataFormatUInt8

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataFormatUInt8: NSString! ``` |
| To | ``` let HMCharacteristicMetadataFormatUInt8: String ``` |

Modified HMCharacteristicMetadataUnitsArcDegree

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataUnitsArcDegree: NSString! ``` |
| To | ``` let HMCharacteristicMetadataUnitsArcDegree: String ``` |

Modified HMCharacteristicMetadataUnitsCelsius

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataUnitsCelsius: NSString! ``` |
| To | ``` let HMCharacteristicMetadataUnitsCelsius: String ``` |

Modified HMCharacteristicMetadataUnitsFahrenheit

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataUnitsFahrenheit: NSString! ``` |
| To | ``` let HMCharacteristicMetadataUnitsFahrenheit: String ``` |

Modified HMCharacteristicMetadataUnitsPercentage

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicMetadataUnitsPercentage: NSString! ``` |
| To | ``` let HMCharacteristicMetadataUnitsPercentage: String ``` |

Modified HMCharacteristicPropertyReadable

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicPropertyReadable: NSString! ``` |
| To | ``` let HMCharacteristicPropertyReadable: String ``` |

Modified HMCharacteristicPropertySupportsEventNotification

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicPropertySupportsEventNotification: NSString! ``` |
| To | ``` let HMCharacteristicPropertySupportsEventNotification: String ``` |

Modified HMCharacteristicPropertyWritable

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicPropertyWritable: NSString! ``` |
| To | ``` let HMCharacteristicPropertyWritable: String ``` |

Modified HMCharacteristicTypeAdminOnlyAccess

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeAdminOnlyAccess: NSString! ``` |
| To | ``` let HMCharacteristicTypeAdminOnlyAccess: String ``` |

Modified HMCharacteristicTypeAudioFeedback

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeAudioFeedback: NSString! ``` |
| To | ``` let HMCharacteristicTypeAudioFeedback: String ``` |

Modified HMCharacteristicTypeBrightness

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeBrightness: NSString! ``` |
| To | ``` let HMCharacteristicTypeBrightness: String ``` |

Modified HMCharacteristicTypeCoolingThreshold

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCoolingThreshold: NSString! ``` |
| To | ``` let HMCharacteristicTypeCoolingThreshold: String ``` |

Modified HMCharacteristicTypeCurrentDoorState

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCurrentDoorState: NSString! ``` |
| To | ``` let HMCharacteristicTypeCurrentDoorState: String ``` |

Modified HMCharacteristicTypeCurrentHeatingCooling

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCurrentHeatingCooling: NSString! ``` |
| To | ``` let HMCharacteristicTypeCurrentHeatingCooling: String ``` |

Modified HMCharacteristicTypeCurrentLockMechanismState

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCurrentLockMechanismState: NSString! ``` |
| To | ``` let HMCharacteristicTypeCurrentLockMechanismState: String ``` |

Modified HMCharacteristicTypeCurrentRelativeHumidity

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCurrentRelativeHumidity: NSString! ``` |
| To | ``` let HMCharacteristicTypeCurrentRelativeHumidity: String ``` |

Modified HMCharacteristicTypeCurrentTemperature

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeCurrentTemperature: NSString! ``` |
| To | ``` let HMCharacteristicTypeCurrentTemperature: String ``` |

Modified HMCharacteristicTypeHeatingThreshold

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeHeatingThreshold: NSString! ``` |
| To | ``` let HMCharacteristicTypeHeatingThreshold: String ``` |

Modified HMCharacteristicTypeHue

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeHue: NSString! ``` |
| To | ``` let HMCharacteristicTypeHue: String ``` |

Modified HMCharacteristicTypeIdentify

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeIdentify: NSString! ``` |
| To | ``` let HMCharacteristicTypeIdentify: String ``` |

Modified HMCharacteristicTypeLockManagementAutoSecureTimeout

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeLockManagementAutoSecureTimeout: NSString! ``` |
| To | ``` let HMCharacteristicTypeLockManagementAutoSecureTimeout: String ``` |

Modified HMCharacteristicTypeLockManagementControlPoint

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeLockManagementControlPoint: NSString! ``` |
| To | ``` let HMCharacteristicTypeLockManagementControlPoint: String ``` |

Modified HMCharacteristicTypeLockMechanismLastKnownAction

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeLockMechanismLastKnownAction: NSString! ``` |
| To | ``` let HMCharacteristicTypeLockMechanismLastKnownAction: String ``` |

Modified HMCharacteristicTypeLogs

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeLogs: NSString! ``` |
| To | ``` let HMCharacteristicTypeLogs: String ``` |

Modified HMCharacteristicTypeManufacturer

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeManufacturer: NSString! ``` |
| To | ``` let HMCharacteristicTypeManufacturer: String ``` |

Modified HMCharacteristicTypeModel

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeModel: NSString! ``` |
| To | ``` let HMCharacteristicTypeModel: String ``` |

Modified HMCharacteristicTypeMotionDetected

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeMotionDetected: NSString! ``` |
| To | ``` let HMCharacteristicTypeMotionDetected: String ``` |

Modified HMCharacteristicTypeName

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeName: NSString! ``` |
| To | ``` let HMCharacteristicTypeName: String ``` |

Modified HMCharacteristicTypeObstructionDetected

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeObstructionDetected: NSString! ``` |
| To | ``` let HMCharacteristicTypeObstructionDetected: String ``` |

Modified HMCharacteristicTypeOutletInUse

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeOutletInUse: NSString! ``` |
| To | ``` let HMCharacteristicTypeOutletInUse: String ``` |

Modified HMCharacteristicTypePowerState

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypePowerState: NSString! ``` |
| To | ``` let HMCharacteristicTypePowerState: String ``` |

Modified HMCharacteristicTypeRotationDirection

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeRotationDirection: NSString! ``` |
| To | ``` let HMCharacteristicTypeRotationDirection: String ``` |

Modified HMCharacteristicTypeRotationSpeed

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeRotationSpeed: NSString! ``` |
| To | ``` let HMCharacteristicTypeRotationSpeed: String ``` |

Modified HMCharacteristicTypeSaturation

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeSaturation: NSString! ``` |
| To | ``` let HMCharacteristicTypeSaturation: String ``` |

Modified HMCharacteristicTypeSerialNumber

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeSerialNumber: NSString! ``` |
| To | ``` let HMCharacteristicTypeSerialNumber: String ``` |

Modified HMCharacteristicTypeTargetDoorState

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTargetDoorState: NSString! ``` |
| To | ``` let HMCharacteristicTypeTargetDoorState: String ``` |

Modified HMCharacteristicTypeTargetHeatingCooling

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTargetHeatingCooling: NSString! ``` |
| To | ``` let HMCharacteristicTypeTargetHeatingCooling: String ``` |

Modified HMCharacteristicTypeTargetLockMechanismState

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTargetLockMechanismState: NSString! ``` |
| To | ``` let HMCharacteristicTypeTargetLockMechanismState: String ``` |

Modified HMCharacteristicTypeTargetRelativeHumidity

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTargetRelativeHumidity: NSString! ``` |
| To | ``` let HMCharacteristicTypeTargetRelativeHumidity: String ``` |

Modified HMCharacteristicTypeTargetTemperature

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTargetTemperature: NSString! ``` |
| To | ``` let HMCharacteristicTypeTargetTemperature: String ``` |

Modified HMCharacteristicTypeTemperatureUnits

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeTemperatureUnits: NSString! ``` |
| To | ``` let HMCharacteristicTypeTemperatureUnits: String ``` |

Modified HMCharacteristicTypeVersion

|  | Declaration |
| --- | --- |
| From | ``` let HMCharacteristicTypeVersion: NSString! ``` |
| To | ``` let HMCharacteristicTypeVersion: String ``` |

Modified HMErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let HMErrorDomain: NSString! ``` |
| To | ``` let HMErrorDomain: String ``` |

Modified HMServiceTypeAccessoryInformation

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeAccessoryInformation: NSString! ``` |
| To | ``` let HMServiceTypeAccessoryInformation: String ``` |

Modified HMServiceTypeFan

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeFan: NSString! ``` |
| To | ``` let HMServiceTypeFan: String ``` |

Modified HMServiceTypeGarageDoorOpener

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeGarageDoorOpener: NSString! ``` |
| To | ``` let HMServiceTypeGarageDoorOpener: String ``` |

Modified HMServiceTypeLightbulb

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeLightbulb: NSString! ``` |
| To | ``` let HMServiceTypeLightbulb: String ``` |

Modified HMServiceTypeLockManagement

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeLockManagement: NSString! ``` |
| To | ``` let HMServiceTypeLockManagement: String ``` |

Modified HMServiceTypeLockMechanism

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeLockMechanism: NSString! ``` |
| To | ``` let HMServiceTypeLockMechanism: String ``` |

Modified HMServiceTypeOutlet

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeOutlet: NSString! ``` |
| To | ``` let HMServiceTypeOutlet: String ``` |

Modified HMServiceTypeSwitch

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeSwitch: NSString! ``` |
| To | ``` let HMServiceTypeSwitch: String ``` |

Modified HMServiceTypeThermostat

|  | Declaration |
| --- | --- |
| From | ``` let HMServiceTypeThermostat: NSString! ``` |
| To | ``` let HMServiceTypeThermostat: String ``` |

Modified HMUserFailedAccessoriesKey

|  | Declaration |
| --- | --- |
| From | ``` let HMUserFailedAccessoriesKey: NSString! ``` |
| To | ``` let HMUserFailedAccessoriesKey: String ``` |

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

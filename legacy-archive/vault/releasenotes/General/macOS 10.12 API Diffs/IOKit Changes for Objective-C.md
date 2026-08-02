---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/IOKit.html
archived_at: '2026-07-18T02:50:39.620920Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IOKit Changes for Objective-C

### IOKit

#### DV/DVFamily.h (Removed)

Removed AVCCTSFrameStructRemoved AVCCTSFrameStructPtrRemoved AVCTransactionParamsRemoved AVCTransactionParamsPtrRemoved DVAVCTransactionCompleteEventRemoved DVAVCTransactionCompleteEventPtrRemoved DVCancelNotification()Removed DVClientIDRemoved DVCloseDriver()Removed DVConnectionEventRemoved DVConnectionEventPtrRemoved DVCountDevices()Removed DVDeviceIDRemoved DVDeviceRefNumRemoved DVDisableRead()Removed DVDisableWrite()Removed DVDisposeNotification()Removed DVDoAVCTransaction()Removed DVEnableRead()Removed DVEnableWrite()Removed DVEventHeaderRemoved DVEventHeaderPtrRemoved DVEventRecordRemoved DVEventRecordPtrRemoved DVGetDeviceName()Removed DVGetDeviceStandard()Removed DVGetEmptyFrame()Removed DVGetIndDevice()Removed DVIsEnabled()Removed DVIsochCompleteEventRemoved DVIsochCompleteEventPtrRemoved DVNewNotification()Removed DVNotificationIDRemoved DVNotifyMeWhen()Removed DVNotifyProcRemoved DVOpenDriver()Removed DVReadFrame()Removed DVReleaseFrame()Removed DVSetDeviceName()Removed DVSetWriteSignalMode()Removed DVWriteFrame()Removed kAlreadyEnabledErrRemoved kAVCEditAudioInsertRemoved kAVCEditAVInsertRemoved kAVCEditDummyOperandRemoved kAVCEditInPointRemoved kAVCEditOtherModeRemoved kAVCEditOutPointRemoved kAVCEditPreRollAndStandbyRemoved kAVCEditPreRollTimeRemoved kAVCEditPresetOpcodeRemoved kAVCEditSubcodeInsertRemoved kAVCEditSyncPlayRemoved kAVCEditSyncRecordRemoved kAVCEditVideoInsertRemoved kAVCMechaModeDummyOperandRemoved kAVCMechaModeInquiryOpcodeRemoved kAVCMediumEjectRemoved kAVCMediumOpcodeRemoved kAVCMediumTrayCloseRemoved kAVCMediumTrayOpenRemoved kAVCPlay1xRemoved kAVCPlayFast1Removed kAVCPlayFast2Removed kAVCPlayFast3Removed kAVCPlayFast4Removed kAVCPlayFast5Removed kAVCPlayFast6Removed kAVCPlayFastestRemoved kAVCPlayForwardRemoved kAVCPlayForwardPauseRemoved kAVCPlayNextFrameRemoved kAVCPlayOpcodeRemoved kAVCPlayPreviousFrameRemoved kAVCPlayRev1xRemoved kAVCPlayReverseRemoved kAVCPlayReversePauseRemoved kAVCPlayRevFast1Removed kAVCPlayRevFast2Removed kAVCPlayRevFast3Removed kAVCPlayRevFast4Removed kAVCPlayRevFast5Removed kAVCPlayRevFast6Removed kAVCPlayRevFastestRemoved kAVCPlayRevSlow1Removed kAVCPlayRevSlow2Removed kAVCPlayRevSlow3Removed kAVCPlayRevSlow4Removed kAVCPlayRevSlow5Removed kAVCPlayRevSlow6Removed kAVCPlayRevSlowestRemoved kAVCPlaySlow1Removed kAVCPlaySlow2Removed kAVCPlaySlow3Removed kAVCPlaySlow4Removed kAVCPlaySlow5Removed kAVCPlaySlow6Removed kAVCPlaySlowestRemoved kAVCPositionDummyOperandRemoved kAVCPositionTimeCodeOpcodeRemoved kAVCPositionValueInquiryRemoved kAVCRecAudioInsertRemoved kAVCRecAudioInsertPauseRemoved kAVCRecAVInsertRemoved kAVCRecAVInsertPauseRemoved kAVCRecordRemoved kAVCRecordOpcodeRemoved kAVCRecPauseRemoved kAVCRecSpeed32Removed kAVCRecSpeedDummyOperandRemoved kAVCRecSpeedHighSpeedRemoved kAVCRecSpeedLowSpeedRemoved kAVCRecSpeedOpcodeRemoved kAVCRecSpeedStandardRemoved kAVCRecSubcodeInsertRemoved kAVCRecSubcodeInsertPauseRemoved kAVCRecVideoInsertRemoved kAVCRecVideoInsertPauseRemoved kAVCReportInquiryCommandRemoved kAVCSupportInquiryCommandRemoved kAVCWindFastForwardRemoved kAVCWindHighSpeedRewindRemoved kAVCWindOpcodeRemoved kAVCWindRewindRemoved kAVCWindStopRemoved kDVAVCDisabledRemoved kDVAVCEnabledRemoved kDVAVCTransactionCompleteRemoved kDVBadIDErrRemoved kDVDeviceAddedRemoved kDVDeviceBusyErrRemoved KDVDeviceInfoChangedRemoved kDVDeviceRemovedRemoved kDVDisconnectedErrRemoved kDVEveryEventRemoved kDVGlobalEventConnectionIDRemoved kDVInputEventRemoved kDVIsochReadCompleteRemoved kDVIsochReadDisabledRemoved kDVIsochReadEnabledRemoved kDVIsochWriteCompleteRemoved kDVIsochWriteDisabledRemoved kDVIsochWriteEnabledRemoved kDVNoNotificationsErrRemoved kEventSpecificDataSizeRemoved kEveryDVDeviceIDRemoved kEveryDVDeviceRefNumRemoved kInvalidDVConnectionIDRemoved kInvalidDVDeviceEventRemoved kInvalidDVDeviceIDRemoved kInvalidDVDeviceRefNumRemoved kNotEnabledErrRemoved kNTSCStandardRemoved kPALStandardRemoved kUnknownStandardRemoved kUnknownStandardErr

#### graphics/IOGraphicsTypes.h

Added [kIOWSAA_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_accelerated)Added [kIOWSAA_DeferEnd](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_deferend)Added [kIOWSAA_DeferStart](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_deferstart)Added [kIOWSAA_DriverOpen](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_driveropen)Added [kIOWSAA_From_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_from_accelerated)Added [kIOWSAA_Hibernate](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_hibernate)Added [kIOWSAA_Sleep](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_sleep)Added [kIOWSAA_To_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_to_accelerated)Added [kIOWSAA_Transactional](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_transactional)Added [kIOWSAA_Unaccelerated](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_unaccelerated)

#### hid/IOHIDBase.h

Removed [kIOHIDTransactionOptionDefaultOutputValue](https://developer.apple.com/documentation/iokit/kiohidtransactionoptiondefaultoutputvalue)Added [kIOHIDTransactionOptionDefaultOutputValue](https://developer.apple.com/documentation/iokit/kiohidtransactionoptiondefaultoutputvalue)

#### hid/IOHIDKeys.h

Added #def kFnFunctionUsageMapKeyAdded #def kFnKeyboardUsageMapKeyAdded #def kIOHIDBiometricDoubleTapTimeoutKeyAdded #def kIOHIDBiometricTapTrackingEnabledKeyAdded #def kIOHIDBiometricTripleTapTimeoutKeyAdded #def kIOHIDKeyboardCapsLockDelayAdded #def kIOHIDKeyboardEjectDelayAdded #def kIOHIDKeyboardLongPressTimeoutKeyAdded #def kIOHIDKeyboardPressCountDoublePressTimeoutKeyAdded #def kIOHIDKeyboardPressCountTrackingEnabledKeyAdded #def kIOHIDKeyboardPressCountTriplePressTimeoutKeyAdded #def kIOHIDKeyboardPressCountUsagePairsKeyAdded #def kKeyboardUsageMapKeyAdded #def kNumLockKeyboardUsageMapKey

#### hid/IOHIDProperties.h (Added)

Added #def IOHIDProperties_hAdded #def kIOHIDKeyboardCapsLockDelayOverrideAdded #def kIOHIDKeyboardCapsLockDelayOverrideKeyAdded #def kIOHIDMouseAccelerationTypeAdded #def kIOHIDMouseAccelerationTypeKeyAdded #def kIOHIDMouseScrollAccelerationKeyAdded #def kIOHIDPointerAccelerationKeyAdded #def kIOHIDPointerAccelerationTypeKeyAdded #def kIOHIDPointerButtonModeAdded #def kIOHIDPointerButtonModeKeyAdded #def kIOHIDScrollAccelerationKeyAdded #def kIOHIDScrollAccelerationTypeKeyAdded #def kIOHIDServiceEjectDelayKeyAdded #def kIOHIDServiceInitialKeyRepeatDelayKeyAdded #def kIOHIDServiceKeyRepeatDelayKeyAdded #def kIOHIDUserUsageMapKey

#### hid/IOHIDUsageTables.h

Added [kHIDUsage_Game_GamepadFormFitting](https://developer.apple.com/documentation/kernel/1641231-anonymous/khidusage_game_gamepadformfitting)Added [kHIDUsage_GD_AssistiveControl](https://developer.apple.com/documentation/kernel/1641458-anonymous/khidusage_gd_assistivecontrol)Added [kHIDUsage_GD_TabletPCSystemControls](https://developer.apple.com/documentation/iokit/1592534-anonymous/khidusage_gd_tabletpcsystemcontrols)Added [kHIDUsage_LED_Player1](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player1)Added [kHIDUsage_LED_Player2](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player2)Added [kHIDUsage_LED_Player3](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player3)Added [kHIDUsage_LED_Player4](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player4)Added [kHIDUsage_LED_Player5](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player5)Added [kHIDUsage_LED_Player6](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player6)Added [kHIDUsage_LED_Player7](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player7)Added [kHIDUsage_LED_Player8](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player8)Added [kHIDUsage_LED_PlayerIndicator](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_playerindicator)

#### hidsystem/ev_keymap.h

Added #def NX_KEYTYPE_MENU

#### hidsystem/event_status_driver.h

Modified [NXClickTime()](https://developer.apple.com/documentation/iokit/1574526-nxclicktime)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXCloseEventStatus()](https://developer.apple.com/documentation/iokit/1574524-nxcloseeventstatus)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXEventSystemInfo()](https://developer.apple.com/documentation/iokit/1574527-nxeventsysteminfo)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXGetClickSpace()](https://developer.apple.com/documentation/iokit/1574518-nxgetclickspace)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXKeyRepeatInterval()](https://developer.apple.com/documentation/iokit/1574515-nxkeyrepeatinterval)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXKeyRepeatThreshold()](https://developer.apple.com/documentation/iokit/1574514-nxkeyrepeatthreshold)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXOpenEventStatus()](https://developer.apple.com/documentation/iokit/1574517-nxopeneventstatus)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXResetKeyboard()](https://developer.apple.com/documentation/iokit/1574523-nxresetkeyboard)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXResetMouse()](https://developer.apple.com/documentation/iokit/1574520-nxresetmouse)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXSetClickSpace()](https://developer.apple.com/documentation/iokit/1574525-nxsetclickspace)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXSetClickTime()](https://developer.apple.com/documentation/iokit/1574522-nxsetclicktime)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXSetKeyRepeatInterval()](https://developer.apple.com/documentation/iokit/1574519-nxsetkeyrepeatinterval)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [NXSetKeyRepeatThreshold()](https://developer.apple.com/documentation/iokit/1574516-nxsetkeyrepeatthreshold)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### hidsystem/IOHIDEventSystemClient.h (Added)

Added #def IOHIDEventSystemClient_hAdded [IOHIDEventSystemClientCopyProperty()](https://developer.apple.com/documentation/iokit/2269513-iohideventsystemclientcopyproper)Added [IOHIDEventSystemClientCopyServices()](https://developer.apple.com/documentation/iokit/2269511-iohideventsystemclientcopyservic)Added [IOHIDEventSystemClientCreateSimpleClient()](https://developer.apple.com/documentation/iokit/2269514-iohideventsystemclientcreatesimp)Added [IOHIDEventSystemClientGetTypeID()](https://developer.apple.com/documentation/iokit/2269512-iohideventsystemclientgettypeid)Added [IOHIDEventSystemClientRef](https://developer.apple.com/documentation/iokit/iohideventsystemclientref)Added [IOHIDEventSystemClientSetProperty()](https://developer.apple.com/documentation/iokit/2269517-iohideventsystemclientsetpropert)

#### hidsystem/IOHIDLib.h

Removed IOHIDSetCursorBounds()Removed IOHIDSetOnScreenCursorBounds()Modified [IOHIDGetAccelerationWithKey()](https://developer.apple.com/documentation/iokit/1555418-iohidgetaccelerationwithkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDGetButtonEventNum()](https://developer.apple.com/documentation/iokit/1555407-iohidgetbuttoneventnum)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDGetMouseAcceleration()](https://developer.apple.com/documentation/iokit/1555417-iohidgetmouseacceleration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDGetParameter()](https://developer.apple.com/documentation/iokit/1555405-iohidgetparameter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDGetScrollAcceleration()](https://developer.apple.com/documentation/iokit/1555389-iohidgetscrollacceleration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDSetAccelerationWithKey()](https://developer.apple.com/documentation/iokit/1555398-iohidsetaccelerationwithkey)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDSetMouseAcceleration()](https://developer.apple.com/documentation/iokit/1555390-iohidsetmouseacceleration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDSetMouseButtonMode()](https://developer.apple.com/documentation/iokit/1555399-iohidsetmousebuttonmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDSetParameter()](https://developer.apple.com/documentation/iokit/1555394-iohidsetparameter)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [IOHIDSetScrollAcceleration()](https://developer.apple.com/documentation/iokit/1555391-iohidsetscrollacceleration)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### hidsystem/IOHIDParameter.h

Removed #def kIOHIDMouseAccelerationTypeRemoved #def kIOHIDMouseScrollAccelerationKeyRemoved #def kIOHIDPointerAccelerationKeyRemoved #def kIOHIDPointerAccelerationTypeKeyRemoved #def kIOHIDPointerButtonModeRemoved #def kIOHIDScrollAccelerationKeyRemoved #def kIOHIDScrollAccelerationTypeKeyAdded #def kIOHIDKeyboardGlobalModifiersKeyAdded #def kIOHIDMouseClickNotificationAdded #def kIOHIDServiceGlobalModifiersUsageKey

#### hidsystem/IOHIDServiceClient.h (Added)

Added #def IOHIDServiceClient_hAdded [IOHIDServiceClientConformsTo()](https://developer.apple.com/documentation/iokit/2269428-iohidserviceclientconformsto)Added [IOHIDServiceClientCopyProperty()](https://developer.apple.com/documentation/iokit/2269430-iohidserviceclientcopyproperty)Added [IOHIDServiceClientGetRegistryID()](https://developer.apple.com/documentation/iokit/2269426-iohidserviceclientgetregistryid)Added [IOHIDServiceClientGetTypeID()](https://developer.apple.com/documentation/iokit/2269431-iohidserviceclientgettypeid)Added [IOHIDServiceClientRef](https://developer.apple.com/documentation/iokit/iohidserviceclientref)Added [IOHIDServiceClientSetProperty()](https://developer.apple.com/documentation/iokit/2269429-iohidserviceclientsetproperty)

#### hidsystem/IOLLEvent.h

Added #def NX_EVENT_EXTENSION_LOCATION_DEVICE_SCALEDAdded #def NX_EVENT_EXTENSION_LOCATION_INVALIDAdded #def NX_EVENT_EXTENSION_LOCATION_TYPE_FLOATAdded #def NX_EVENT_EXTENSION_MOUSE_DELTA_TYPE_FLOATAdded #def NX_SUBTYPE_ACCESSIBILITYAdded #def NX_SUBTYPE_MENUAdded [NXEventExt](https://developer.apple.com/documentation/iokit/nxeventext)Added [NXEventExtension](https://developer.apple.com/documentation/iokit/nxeventextension)

#### IOBSD.h

Added [#def kIOBSDKey](https://developer.apple.com/documentation/iokit/kiobsdkey)

#### IOKitKeys.h

Added [#def kIOMinimumSaturationByteCountKey](https://developer.apple.com/documentation/iokit/kiominimumsaturationbytecountkey)Added [#def kIOPropertyExistsMatchKey](https://developer.apple.com/documentation/iokit/kiopropertyexistsmatchkey)Added [#def kIORegistryEntryPropertyKeysKey](https://developer.apple.com/documentation/iokit/kioregistryentrypropertykeyskey)Added [#def kIOResourceMatchedKey](https://developer.apple.com/documentation/iokit/kioresourcematchedkey)

#### iokitmig.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### IOReturn.h

Added #def sub_iokit_appleembeddedsleepwakehandler

#### network/IONetworkController.h

Added [kIONetworkFeatureHWTimeStamp](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturehwtimestamp)Added [kIONetworkFeatureSWTimeStamp](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeatureswtimestamp)

#### pwr_mgt/IOPM.h

Added #def kIOPMPSAdapterDetailsVoltage

#### pwr_mgt/IOPMLib.h

Modified [IOAllowPowerChange()](https://developer.apple.com/documentation/iokit/1557064-ioallowpowerchange)

|  | Declaration |
| --- | --- |
| From | ``` IOReturn IOAllowPowerChange (     io_connect_t kernelPort,     long notificationID ); ``` |
| To | ``` IOReturn IOAllowPowerChange (     io_connect_t kernelPort,     intptr_t notificationID ); ``` |

Modified [IOCancelPowerChange()](https://developer.apple.com/documentation/iokit/1557115-iocancelpowerchange)

|  | Declaration |
| --- | --- |
| From | ``` IOReturn IOCancelPowerChange (     io_connect_t kernelPort,     long notificationID ); ``` |
| To | ``` IOReturn IOCancelPowerChange (     io_connect_t kernelPort,     intptr_t notificationID ); ``` |

#### scsi/SCSICmds_INQUIRY_Definitions.h

Added [kINQUIRY_PageB0_PageCode](https://developer.apple.com/documentation/kernel/1643302-anonymous/kinquiry_pageb0_pagecode)Added [kINQUIRY_PageB2_PageCode](https://developer.apple.com/documentation/iokit/1572746-inquiry_page_codes/kinquiry_pageb2_pagecode)Added [SCSICmd_INQUIRY_PageB0_Data](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_pageb0_data)Added [SCSICmd_INQUIRY_PageB2_Data](https://developer.apple.com/documentation/kernel/scsicmd_inquiry_pageb2_data)Added [SCSICmd_INQUIRY_PageB2_Provisioning_Group_Descriptor](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_pageb2_provisioning_group_descriptor)

#### scsi/SCSICommandOperationCodes.h

Added [kSCSICmd_UNMAP](https://developer.apple.com/documentation/kernel/1643419-anonymous/kscsicmd_unmap)Added [kSCSIServiceAction_GET_LBA_STATUS](https://developer.apple.com/documentation/iokit/1778261-anonymous/kscsiserviceaction_get_lba_status)Added [kSCSIServiceAction_REPORT_PROVISIONING_INITIALIZATION_PATTERN](https://developer.apple.com/documentation/kernel/1643413-anonymous/kscsiserviceaction_report_provisioning_initialization_pattern)

#### usb/IOUSBLib.h

Added [IOUSBInterfaceInterface800](https://developer.apple.com/documentation/iokit/iousbinterfaceinterface800)Added #def kIOUSBInterfaceInterfaceID800

#### usb/IOUSBUserClient.h

Added [kUSBInterfaceUserClientSetDeviceIdlePolicy](https://developer.apple.com/documentation/iokit/1575934-anonymous/kusbinterfaceuserclientsetdeviceidlepolicy)Added [kUSBInterfaceUserClientSetPipeIdlePolicy](https://developer.apple.com/documentation/kernel/1646287-anonymous/kusbinterfaceuserclientsetpipeidlepolicy)

#### usb/USB.h

Added [IOUSBDeviceCapabilityBillboard](https://developer.apple.com/documentation/iokit/iousbdevicecapabilitybillboard)Added [IOUSBDeviceCapabilityBillboardAltConfig](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardaltconfig)Added [IOUSBDeviceCapabilityBillboardAltConfigPtr](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardaltconfigptr)Added [IOUSBDeviceCapabilityBillboardPtr](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardptr)Added #def kIOUSBMessageConfigurationSetAdded [kUSBDeviceSpeedSuperPlus](https://developer.apple.com/documentation/iokit/1425357-usbdevicespeed/kusbdevicespeedsuperplus)

#### usb/USBSpec.h

Added [kUSBBillboardAltModeConfigSuccess](https://developer.apple.com/documentation/kernel/1643529-anonymous/kusbbillboardaltmodeconfigsuccess)Added [kUSBBillboardConfigNotAttempted](https://developer.apple.com/documentation/iokit/1643743-anonymous/kusbbillboardconfignotattempted)Added [kUSBBillboardConfigUnsuccessful](https://developer.apple.com/documentation/iokit/1643743-anonymous/kusbbillboardconfigunsuccessful)Added [kUSBBillboardUnspecifiedError](https://developer.apple.com/documentation/kernel/1643529-anonymous/kusbbillboardunspecifiederror)Added [kUSBBillboardVConn1P5Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn1p5watt)Added [kUSBBillboardVConn1Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn1watt)Added [kUSBBillboardVConn2Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn2watt)Added [kUSBBillboardVConn3Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn3watt)Added [kUSBBillboardVConn4Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn4watt)Added [kUSBBillboardVConn5Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn5watt)Added [kUSBBillboardVConn6Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn6watt)Added #def kUSBBillboardVConnNoPowerReqAdded [kUSBBillboardVConnReserved](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconnreserved)Added [kUSBDeviceCapabilityBillboard](https://developer.apple.com/documentation/iokit/1424953-device_capability_types/kusbdevicecapabilitybillboard)

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

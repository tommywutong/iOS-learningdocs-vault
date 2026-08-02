---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/IOKit.html
archived_at: '2026-07-18T02:58:43.459724Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# IOKit Changes

## IOKit

IOATAStorageDefines.hModified [kATAOperationTypeRead](https://developer.apple.com/documentation/kernel/1646149-anonymous/kataoperationtyperead)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypeSMART](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypesmart)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypeFlushCache](https://developer.apple.com/documentation/kernel/1646149-anonymous/kataoperationtypeflushcache)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypePowerManagement](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypepowermanagement)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [ATAOperationType](https://developer.apple.com/documentation/kernel/ataoperationtype)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypeConfiguration](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypeconfiguration)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypeWrite](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypewrite)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

Modified [kATAOperationTypeSMS](https://developer.apple.com/documentation/iokit/1556750-anonymous/kataoperationtypesms)

|  | Architectures |
| --- | --- |
| Old | none? |
| New | ppc,i386,x86_64 |

IODVDTypes.hAdded kDVDKeyClassCSS_CPPM_CPRM (no architecture available)Added kDVDKeyFormatAGID_CPRM (no architecture available)Added kDVDKeyFormatAGID_CSS (no architecture available)Added kDVDKeyFormatAGID_CSS2 (no architecture available)Added kDVDKeyFormatASF (no architecture available)Added kDVDKeyFormatChallengeKey (no architecture available)Added kDVDKeyFormatKey1 (no architecture available)Added kDVDKeyFormatKey2 (no architecture available)Added kDVDKeyFormatRegionState (no architecture available)Added kDVDKeyFormatSetRegion (no architecture available)Added kDVDKeyFormatTitleKey (no architecture available)IOFireWireFamilyCommon.hAdded [DCLCompilerDataType](https://developer.apple.com/documentation/iokit/dclcompilerdatatype)Added [kFWIsochRequireLastContext](https://developer.apple.com/documentation/iokit/iofwisochportoptions/kfwisochrequirelastcontext)IOFireWireLib.hRemoved IOFireWireLibBufferFillIsochPortRefIOI2CInterface.hAdded [kIOI2CBusTypeDisplayPort](https://developer.apple.com/documentation/iokit/1410382-anonymous/kioi2cbustypedisplayport)Added [kIOI2CDisplayPortNativeTransactionType](https://developer.apple.com/documentation/iokit/1410366-anonymous/kioi2cdisplayportnativetransactiontype)IOKitKeys.hAdded [#def kIOUserClientCreatorKey](https://developer.apple.com/documentation/iokit/kiouserclientcreatorkey)IOMacOSVideo.hAdded #def FOUR_CHAR_CODEAdded #def PRAGMA_STRUCT_ALIGNAdded [kVideoBusTypeDisplayPort](https://developer.apple.com/documentation/kernel/1644552-anonymous/kvideobustypedisplayport)Added [kVideoDisplayPortNativeType](https://developer.apple.com/documentation/iokit/1567416-anonymous/kvideodisplayportnativetype)Added [kVideoDisplayPortNativeTypeMask](https://developer.apple.com/documentation/iokit/1567416-anonymous/kvideodisplayportnativetypemask)IONetworkController.hAdded IONetworkController::systemWillShutdown() (no architecture available)Added [kIONetworkFeatureTSOIPv4](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturetsoipv4)Added [kIONetworkFeatureTSOIPv6](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturetsoipv6)IONetworkInterface.hAdded IONetworkInterface::getIfnet() (no architecture available)Added IONetworkInterface::message() (no architecture available)IONetworkMedium.hAdded [kIOMediumEthernet10GBaseCX4](https://developer.apple.com/documentation/iokit/1562954-anonymous/kiomediumethernet10gbasecx4)Added [kIOMediumEthernet10GBaseT](https://developer.apple.com/documentation/iokit/1562954-anonymous/kiomediumethernet10gbaset)IONetworkUserClient.hRemoved IONetworkUserClient::getExternalMethodForIndex() (no architecture available)Removed #def kIONUCGetNetworkDataCapacityFlagsRemoved #def kIONUCGetNetworkDataCapacityInputsRemoved #def kIONUCGetNetworkDataCapacityOutputsRemoved #def kIONUCGetNetworkDataHandleFlagsRemoved #def kIONUCGetNetworkDataHandleInputsRemoved #def kIONUCGetNetworkDataHandleOutputsRemoved #def kIONUCReadNetworkDataFlagsRemoved #def kIONUCReadNetworkDataInputsRemoved #def kIONUCReadNetworkDataOutputsRemoved #def kIONUCResetNetworkDataFlagsRemoved #def kIONUCResetNetworkDataInputsRemoved #def kIONUCResetNetworkDataOutputsRemoved #def kIONUCWriteNetworkDataFlagsRemoved #def kIONUCWriteNetworkDataInput0Removed #def kIONUCWriteNetworkDataInput1Added IONetworkUserClient::externalMethod() (no architecture available)IOPM.hRemoved IOPMRegisterDevice() (no architecture available)Added #def kIOPMBatteryChargeStatusGradientAdded #def kIOPMBatteryChargeStatusTooColdAdded #def kIOPMBatteryChargeStatusTooHotAdded #def kIOPMCPUPowerLimitProcessorCountKeyAdded #def kIOPMCPUPowerLimitProcessorSpeedKeyAdded #def kIOPMCPUPowerLimitSchedulerTimeKeyAdded #def kIOPMCPUPowerLimitsKeyAdded #def kIOPMGraphicsPowerLimitPerformanceKeyAdded #def kIOPMGraphicsPowerLimitsKeyAdded #def kIOPMMessageSystemPowerEventOccurredAdded #def kIOPMPSBatteryChargeStatusKeyAdded #def kIOPMSettingGraphicsSwitchKeyAdded #def kIOPMThermalLevelWarningKeyAdded kIOPMThermalWarningLevelCrisisAdded kIOPMThermalWarningLevelDangerAdded kIOPMThermalWarningLevelNormalIOPMLib.hAdded [IOPMAssertionCreateWithName()](https://developer.apple.com/documentation/iokit/1557134-iopmassertioncreatewithname)Added [#def kIOPMAssertionNameKey](https://developer.apple.com/documentation/iokit/kiopmassertionnamekey)IOPSKeys.hAdded [#def kIOPSBatteryFailureModesKey](https://developer.apple.com/documentation/iokit/kiopsbatteryfailuremodeskey)Added [#def kIOPSBatteryHealthConditionKey](https://developer.apple.com/documentation/iokit/kiopsbatteryhealthconditionkey)Added [#def kIOPSCheckBatteryValue](https://developer.apple.com/documentation/iokit/kiopscheckbatteryvalue)Added [#def kIOPSFailureCellImbalance](https://developer.apple.com/documentation/iokit/kiopsfailurecellimbalance)Added [#def kIOPSFailureChargeFET](https://developer.apple.com/documentation/iokit/kiopsfailurechargefet)Added [#def kIOPSFailureChargeOverCurrent](https://developer.apple.com/documentation/iokit/kiopsfailurechargeovercurrent)Added [#def kIOPSFailureChargeOverTemp](https://developer.apple.com/documentation/iokit/kiopsfailurechargeovertemp)Added [#def kIOPSFailureDataFlushFault](https://developer.apple.com/documentation/iokit/kiopsfailuredataflushfault)Added [#def kIOPSFailureDischargeFET](https://developer.apple.com/documentation/iokit/kiopsfailuredischargefet)Added [#def kIOPSFailureDischargeOverCurrent](https://developer.apple.com/documentation/iokit/kiopsfailuredischargeovercurrent)Added [#def kIOPSFailureDischargeOverTemp](https://developer.apple.com/documentation/iokit/kiopsfailuredischargeovertemp)Added [#def kIOPSFailureExternalInput](https://developer.apple.com/documentation/iokit/kiopsfailureexternalinput)Added [#def kIOPSFailureFuseBlown](https://developer.apple.com/documentation/iokit/kiopsfailurefuseblown)Added [#def kIOPSFailureOpenThermistor](https://developer.apple.com/documentation/iokit/kiopsfailureopenthermistor)Added [#def kIOPSFailurePeriodicAFEComms](https://developer.apple.com/documentation/iokit/kiopsfailureperiodicafecomms)Added [#def kIOPSFailurePermanentAFEComms](https://developer.apple.com/documentation/iokit/kiopsfailurepermanentafecomms)Added [#def kIOPSFailureSafetyOverVoltage](https://developer.apple.com/documentation/iokit/kiopsfailuresafetyovervoltage)Added [#def kIOPSPermanentFailureValue](https://developer.apple.com/documentation/iokit/kiopspermanentfailurevalue)IOPowerSources.hRemoved IOPowerSourceCallbackType (no architecture available)Added [IOPSGetBatteryWarningLevel()](https://developer.apple.com/documentation/iokit/1523851-iopsgetbatterywarninglevel)Added [IOPSLowBatteryWarningLevel](https://developer.apple.com/documentation/iokit/iopslowbatterywarninglevel)Added [kIOPSLowBatteryWarningEarly](https://developer.apple.com/documentation/iokit/iopslowbatterywarninglevel/kiopslowbatterywarningearly)Added [kIOPSLowBatteryWarningFinal](https://developer.apple.com/documentation/iokit/iopslowbatterywarninglevel/kiopslowbatterywarningfinal)Added [kIOPSLowBatteryWarningNone](https://developer.apple.com/documentation/iokit/iopslowbatterywarninglevel/kiopslowbatterywarningnone)Added [#def kIOPSNotifyLowBattery](https://developer.apple.com/documentation/iokit/kiopsnotifylowbattery)IOSCSIMultimediaCommandsDevice.hAdded IOSCSIMultimediaCommandsDevice::setAggressiveness() (no architecture available)IOTypes.hRemoved IOCacheRemoved IOObjectNumberRemoved IO_CacheOffRemoved IO_CopyBackRemoved IO_WriteThroughRemoved kIOMap64BitAdded [IOByteCount32](https://developer.apple.com/documentation/iokit/iobytecount32)Added [IOByteCount64](https://developer.apple.com/documentation/iokit/iobytecount64)Added [IOPhysicalAddress32](https://developer.apple.com/documentation/kernel/iophysicaladdress32)Added [IOPhysicalAddress64](https://developer.apple.com/documentation/kernel/iophysicaladdress64)Added [IOPhysicalLength32](https://developer.apple.com/documentation/iokit/iophysicallength32)Added [IOPhysicalLength64](https://developer.apple.com/documentation/iokit/iophysicallength64)Added [IOPhysicalRange](https://developer.apple.com/documentation/kernel/iophysicalrange)IOUSBLib.hAdded [IOUSBDeviceInterface320](https://developer.apple.com/documentation/iokit/iousbdeviceinterface320)Added [#def kIOUSBDeviceInterfaceID320](https://developer.apple.com/documentation/iokit/kiousbdeviceinterfaceid320)IOUSBUserClient.hAdded [kUSBDeviceUserClientGetDeviceInformation](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientgetdeviceinformation)Added [kUSBDeviceUserClientGetExtraPowerAllocated](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientgetextrapowerallocated)Added [kUSBDeviceUserClientRequestExtraPower](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientrequestextrapower)Added [kUSBDeviceUserClientReturnExtraPower](https://developer.apple.com/documentation/iokit/1575954-anonymous/kusbdeviceuserclientreturnextrapower)SCSICmds_MODE_Definitions.hAdded [kModeSenseSBCDeviceSpecific_DPOFUABit](https://developer.apple.com/documentation/iokit/1555554-device_specific_parameter_bitfie/kmodesensesbcdevicespecific_dpofuabit)Added [kModeSenseSBCDeviceSpecific_DPOFUAMask](https://developer.apple.com/documentation/kernel/1645305-anonymous/kmodesensesbcdevicespecific_dpofuamask)USB.hAdded [LowLatencyUserBufferInfoV3](https://developer.apple.com/documentation/iokit/lowlatencyuserbufferinfov3)Added [USBDeviceInformationBits](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits)Added [USBPhysicalAddress32](https://developer.apple.com/documentation/kernel/usbphysicaladdress32)Added [USBPowerRequestTypes](https://developer.apple.com/documentation/kernel/usbpowerrequesttypes)Added #def kAppleCurrentAvailableAdded #def kAppleCurrentExtraAdded #def kAppleCurrentInSleepAdded #def kAppleExtraPowerAggregateAdded #def kAppleExtraPowerInSleepAdded #def kAppleExtraPowerPerPortAdded #def kAppleInternalUSBDeviceAdded #def kUSBBusIDAdded [kUSBInformationDeviceIsAttachedToRootHubBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisattachedtoroothubbit)Added [kUSBInformationDeviceIsCaptiveBit](https://developer.apple.com/documentation/iokit/usbdeviceinformationbits/kusbinformationdeviceiscaptivebit)Added [kUSBInformationDeviceIsConnectedBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisconnectedbit)Added [kUSBInformationDeviceIsEnabledBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisenabledbit)Added [kUSBInformationDeviceIsInResetBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceisinresetbit)Added [kUSBInformationDeviceIsInternalBit](https://developer.apple.com/documentation/iokit/usbdeviceinformationbits/kusbinformationdeviceisinternalbit)Added [kUSBInformationDeviceIsSuspendedBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceissuspendedbit)Added [kUSBInformationDeviceOvercurrentBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceovercurrentbit)Added [kUSBInformationDevicePortIsInTestModeBit](https://developer.apple.com/documentation/kernel/usbdeviceinformationbits/kusbinformationdeviceportisintestmodebit)Added [kUSBPowerDuringSleep](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerduringsleep)Added [kUSBPowerDuringWake](https://developer.apple.com/documentation/iokit/usbpowerrequesttypes/kusbpowerduringwake)USBSpec.hAdded [kAppleVendorID](https://developer.apple.com/documentation/iokit/1424851-apple_usb_vendor_id/kapplevendorid)Added [kUSBPersonalHealthcareClass](https://developer.apple.com/documentation/iokit/1424988-device_class_codes/kusbpersonalhealthcareclass)Added [kUSBPersonalHealthcareInterfaceClass](https://developer.apple.com/documentation/iokit/1424756-interface_class/kusbpersonalhealthcareinterfaceclass)

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

---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/Kernel.html
archived_at: '2026-07-18T02:51:49.770429Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Kernel Changes

## Kernel

IOKit/bluetooth/Bluetooth.hAdded [BluetoothLEConnectionInterval](https://developer.apple.com/documentation/iobluetooth/bluetoothleconnectioninterval)Added [BluetoothLEConnectionIntervalMax](https://developer.apple.com/documentation/kernel/bluetoothleconnectioninterval/bluetoothleconnectionintervalmax)Added [BluetoothLEConnectionIntervalMin](https://developer.apple.com/documentation/iobluetooth/bluetoothleconnectionintervalmin)Added [kBluetoothL2CAPChannelMagnet](https://developer.apple.com/documentation/kernel/1640028-anonymous/kbluetoothl2capchannelmagnet)IOKit/bluetooth/BluetoothAssignedNumbers.hRemoved kBluetoothSDPUUID16ServiceClassVideoConferencingAdded [kBluetoothSDPUUID16ServiceClassAVRemoteControlController](https://developer.apple.com/documentation/kernel/sdpserviceclasses/kbluetoothsdpuuid16serviceclassavremotecontrolcontroller)IOKit/audio/IOAudioDefines.hAdded #def kIOAudioEngineDisableClockBoundsCheckIOKit/IODataQueue.hModified [IODataQueue](https://developer.apple.com/documentation/kernel/iodataqueue)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::enqueue_tail()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::free()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::getMemoryDescriptor()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::getMetaClass()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::initWithCapacity()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::initWithEntries()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::sendDataAvailableNotification()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::setNotificationPort()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::withCapacity()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified IODataQueue::withEntries()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

IOKit/graphics/IOGraphicsTypes.hAdded [kConnectionVBLMultiplier](https://developer.apple.com/documentation/kernel/1645147-anonymous/kconnectionvblmultiplier)Added [kIOWindowServerActiveAttribute](https://developer.apple.com/documentation/kernel/1645144-anonymous/kiowindowserveractiveattribute)IOKit/pci/IOPCIBridge.hAdded IOPCIBridge::finishMachineState()Added IOPCIBridge::systemPowerChange()IOKit/pwr_mgt/IOPM.hRemoved kIOPMThermalWarningLevelCrisisRemoved kIOPMThermalWarningLevelDangerRemoved kIOPMThermalWarningLevelNormalAdded [kIOPMThermalLevelCritical](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermallevelcritical)Added [kIOPMThermalLevelDanger](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermalleveldanger)Added [kIOPMThermalLevelNormal](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermallevelnormal)Added [kIOPMThermalLevelTrap](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermalleveltrap)Added [kIOPMThermalLevelUnknown](https://developer.apple.com/documentation/iokit/1499874-anonymous/kiopmthermallevelunknown)Added [kIOPMThermalLevelWarning](https://developer.apple.com/documentation/kernel/1645015-anonymous/kiopmthermallevelwarning)Added #def kIOPMThermalWarningLevelCrisisAdded #def kIOPMThermalWarningLevelDangerAdded #def kIOPMThermalWarningLevelNormalIOKit/scsi/IOSCSIBlockCommandsDevice.hAdded #def fDeviceHasNVMETranslationIOKit/IOSharedDataQueue.hAdded IOSharedDataQueue::enqueue()Added IOSharedDataQueue::getQueueSize()Added IOSharedDataQueue::setQueueSize()Added #def DISABLE_DATAQUEUE_WARNINGIOKit/usb/IOUSBControllerV3.hAdded IOUSBControllerV3::GetPMCSR()IOKit/usb/IOUSBHIDDriverPM.h (Removed)Removed IOUSBHIDDriverPMRemoved IOUSBHIDDriverPM::CheckForDeadDevice()Removed IOUSBHIDDriverPM::CheckForPowerSleepers()Removed IOUSBHIDDriverPM::ClearFeatureEndpointHalt()Removed IOUSBHIDDriverPM::EnsureUsability()Removed IOUSBHIDDriverPM::GetHIDDescriptor()Removed IOUSBHIDDriverPM::GetIndexedString()Removed IOUSBHIDDriverPM::GetNumberProperty()Removed IOUSBHIDDriverPM::HandleReport()Removed IOUSBHIDDriverPM::InitializeUSBHIDPowerManagement()Removed IOUSBHIDDriverPM::InterruptReadHandler()Removed IOUSBHIDDriverPM::InterruptReadHandlerEntry()Removed IOUSBHIDDriverPM::IsPortSuspended()Removed IOUSBHIDDriverPM::RaisePowerState()Removed IOUSBHIDDriverPM::RearmInterruptRead()Removed IOUSBHIDDriverPM::ScheduleWork()Removed IOUSBHIDDriverPM::SendDeviceRequest()Removed IOUSBHIDDriverPM::SendDeviceRequestWorker()Removed IOUSBHIDDriverPM::SetIdleMillisecs()Removed IOUSBHIDDriverPM::SetProtocol()Removed IOUSBHIDDriverPM::WorkToDo()Removed IOUSBHIDDriverPM::didTerminate()Removed IOUSBHIDDriverPM::free()Removed IOUSBHIDDriverPM::getMaxReportSize()Removed IOUSBHIDDriverPM::getMetaClass()Removed IOUSBHIDDriverPM::getReport()Removed IOUSBHIDDriverPM::handleStart()Removed IOUSBHIDDriverPM::handleStop()Removed IOUSBHIDDriverPM::init()Removed IOUSBHIDDriverPM::message()Removed IOUSBHIDDriverPM::newCountryCodeNumber()Removed IOUSBHIDDriverPM::newIndexedString()Removed IOUSBHIDDriverPM::newLocationIDNumber()Removed IOUSBHIDDriverPM::newManufacturerString()Removed IOUSBHIDDriverPM::newProductIDNumber()Removed IOUSBHIDDriverPM::newProductString()Removed IOUSBHIDDriverPM::newReportDescriptor()Removed IOUSBHIDDriverPM::newReportIntervalNumber()Removed IOUSBHIDDriverPM::newSerialNumberString()Removed IOUSBHIDDriverPM::newTransportString()Removed IOUSBHIDDriverPM::newVendorIDNumber()Removed IOUSBHIDDriverPM::newVersionNumber()Removed IOUSBHIDDriverPM::powerChangeDone()Removed IOUSBHIDDriverPM::powerStateDidChangeTo()Removed IOUSBHIDDriverPM::powerStateWillChangeTo()Removed IOUSBHIDDriverPM::setPowerState()Removed IOUSBHIDDriverPM::setReport()Removed IOUSBHIDDriverPM::start()Removed IOUSBHIDDriverPM::stop()Removed IOUSBHIDDriverPM::willTerminate()Removed #def HIDMGR2USBREPORTTYPERemoved #def USB2HIDMGRREPORTTYPERemoved #def kHIDStandardDriverRetryCountRemoved #def kHIDStandardRetryCountInMSRemoved #def kMaxHIDReportSizeRemoved #def kUSBHIDIdleTimeRemoved kUSBHIDNumberPowerStatesRemoved kUSBHIDPowerStateLowPowerRemoved kUSBHIDPowerStateOffRemoved kUSBHIDPowerStateOnRemoved kUSBHIDPowerStateRestartRemoved kUSBHIDPowerStateSleepRemoved #def kUSBHIDReportLoggingLevelIOKit/usb/IOUSBMassStorageClass.hAdded IOUSBMassStorageClass::DidWakeFromHibernationOrStandby()IOKit/scsi/SCSICmds_INQUIRY_Definitions.hAdded [kINQUIRY_VERSION_DESCRIPTOR_NVME](https://developer.apple.com/documentation/iokit/1572862-anonymous/kinquiry_version_descriptor_nvme)IOKit/usb/USB.hAdded #def kIOUSBMessageTDMLowBatteryAdded #def kOverrideAllowLowPowerAdded #def kOverrideAttachedToCPUAdded [kUSBTDMLowBatteryType](https://developer.apple.com/documentation/kernel/1646362-anonymous/kusbtdmlowbatterytype)IOKit/usb/USBSpec.hAdded [kUSBBillBoardClass](https://developer.apple.com/documentation/iokit/1424988-device_class_codes/kusbbillboardclass)i386/cpuid.hRemoved #def CPUID_MODEL_HASWELL_SVRAdded #def CPUID_LEAF7_FEATURE_ADXAdded #def CPUID_LEAF7_FEATURE_RDSEEDAdded #def CPUID_LEAF7_FEATURE_SMAPAdded #def CPUID_MODEL_BROADWELLAdded #def CPUID_MODEL_BROADWELL_ULTAdded #def CPUID_MODEL_BROADWELL_ULXAdded #def CPUID_MODEL_BRYSTALWELLAdded #def CPUID_MODEL_HASWELL_EPAdded #def CPUID_VMM_FAMILY_PARALLELSAdded #def CPUID_VMM_ID_PARALLELSkern/hv_support.hRemoved hv_callback_0_tRemoved hv_callback_1_tAdded hv_release_mp_notify()Added hv_set_mp_notify()Added [hv_suspend()](https://developer.apple.com/documentation/kernel/1507114-hv_suspend)Modified [hv_set_callbacks()](https://developer.apple.com/documentation/kernel/1507074-hv_set_callbacks)

|  | Declaration |
| --- | --- |
| From | ``` int hv_set_callbacks (	hv_callbacks_t callbacks); ``` |
| To | ``` kern_return_t hv_set_callbacks (	hv_callbacks_t callbacks); ``` |

Modified [hv_set_traps()](https://developer.apple.com/documentation/kernel/1507088-hv_set_traps)

|  | Declaration |
| --- | --- |
| From | ``` int hv_set_traps (	hv_trap_type_t trap_type,	const hv_trap_t *traps,	unsigned int trap_count); ``` |
| To | ``` kern_return_t hv_set_traps (	hv_trap_type_t trap_type,	const hv_trap_t *traps,	unsigned int trap_count); ``` |

sys/imgact.hAdded #def IMGPF_VFORK_EXECsys/kdebug.hRemoved KD_CALLBACK_KDEBUG_DISABLEDRemoved KD_CALLBACK_KDEBUG_ENABLEDRemoved KD_CALLBACK_SYNC_FLUSHRemoved KD_CALLBACK_TYPEFILTER_CHANGEDRemoved kd_callback_fnRemoved kd_callback_tRemoved kd_callback_typeRemoved kernel_debug_enter()Removed kernel_debug_register_callback()Added #def ARIADNEDBG_CODEAdded #def ATM_GETVALUE_INFOAdded #def ATM_UNREGISTER_INFOAdded #def ATM_VALUE_ADDEDAdded #def ATM_VALUE_DIFF_MAILBOXAdded #def ATM_VALUE_REPLACEDAdded #def ATM_VALUE_UNREGISTEREDAdded #def DBG_ARIADNEAdded #def KDEBUG_ENABLE_SERIALAdded #def SFI_GLOBAL_DEFERAdded #def TRACE_DATA_EXECAdded #def TRACE_DATA_NEWTHREADAdded #def TRACE_INFO_STRINGAdded #def TRACE_LOST_EVENTSAdded #def TRACE_PANICAdded #def TRACE_STRING_EXECAdded #def TRACE_STRING_NEWTHREADAdded #def TRACE_TIMESTAMPSAdded #def TRACE_WRITING_EVENTSsys/kdebugevents.h (Added)Added [kd_event_t](https://developer.apple.com/documentation/kernel/kd_event_t)Added [kd_events](https://developer.apple.com/documentation/kernel/kd_events)mach/machine.hAdded #def CPUFAMILY_INTEL_BROADWELLi386/proc_reg.hAdded #def CR4_SMAPAdded #def MSR_IA32_EVNTSEL2Added #def MSR_IA32_EVNTSEL3Added #def MSR_IA32_PERFCTR3Added #def MSR_IA32_PERFCTR4Added [clac()](https://developer.apple.com/documentation/kernel/1571382-clac)Added [stac()](https://developer.apple.com/documentation/kernel/1571276-stac)sys/syscall.hAdded #def SYS_kdebug_trace64vecLib/vDSP.hAdded [vDSP_sve()](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)Added [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)Added [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)Added [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)Added [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)

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

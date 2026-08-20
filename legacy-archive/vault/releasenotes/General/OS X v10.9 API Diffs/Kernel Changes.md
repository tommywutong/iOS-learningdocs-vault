---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Kernel.html
archived_at: '2026-07-18T02:54:15.018870Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Kernel Changes

## Kernel

AvailabilityMacros.hAdded #def AVAILABLE_MAC_OS_X_VERSION_10_0_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_1_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_2_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_3_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_4_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_5_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_7_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_8_AND_LATER_BUT_DEPRECATED_IN_MAC_OS_X_VERSION_10_9Added #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATERAdded #def AVAILABLE_MAC_OS_X_VERSION_10_9_AND_LATER_BUT_DEPRECATEDAdded #def DEPRECATED_IN_MAC_OS_X_VERSION_10_9_AND_LATERAdded #def DEPRECATED_MSG_ATTRIBUTEAdded #def MAC_OS_X_VERSION_10_9BluetoothAssignedNumbers.hRemoved kBluetoothDeviceClassMajoHealthRemoved kBluetoothDeviceClassMajoToyAdded [kBluetoothDeviceClassMajorHealth](https://developer.apple.com/documentation/kernel/1640534-anonymous/kbluetoothdeviceclassmajorhealth)Added [kBluetoothDeviceClassMajorToy](https://developer.apple.com/documentation/kernel/1640534-anonymous/kbluetoothdeviceclassmajortoy)Added [kBluetoothGAPAppearanceGenericBarcodeScanner](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericbarcodescanner)Added [kBluetoothGAPAppearanceGenericBloodPressure](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancegenericbloodpressure)Added [kBluetoothGAPAppearanceGenericClock](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancegenericclock)Added [kBluetoothGAPAppearanceGenericComputer](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericcomputer)Added [kBluetoothGAPAppearanceGenericCycling](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericcycling)Added [kBluetoothGAPAppearanceGenericDisplay](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancegenericdisplay)Added [kBluetoothGAPAppearanceGenericEyeGlasses](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancegenericeyeglasses)Added [kBluetoothGAPAppearanceGenericGlucoseMeter](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancegenericglucosemeter)Added [kBluetoothGAPAppearanceGenericHeartrateSensor](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancegenericheartratesensor)Added [kBluetoothGAPAppearanceGenericHumanInterfaceDevice](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancegenerichumaninterfacedevice)Added [kBluetoothGAPAppearanceGenericKeyring](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenerickeyring)Added [kBluetoothGAPAppearanceGenericMediaPlayer](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericmediaplayer)Added [kBluetoothGAPAppearanceGenericPhone](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancegenericphone)Added [kBluetoothGAPAppearanceGenericRemoteControl](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericremotecontrol)Added [kBluetoothGAPAppearanceGenericRunningWalkingSensor](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericrunningwalkingsensor)Added [kBluetoothGAPAppearanceGenericTag](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancegenerictag)Added [kBluetoothGAPAppearanceGenericThermometer](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericthermometer)Added [kBluetoothGAPAppearanceGenericWatch](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancegenericwatch)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceBarcodeScanner](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancehumaninterfacedevicebarcodescanner)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceCardReader](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancehumaninterfacedevicecardreader)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceDigitalPen](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancehumaninterfacedevicedigitalpen)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceDigitizerTablet](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancehumaninterfacedevicedigitizertablet)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceGamepad](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancehumaninterfacedevicegamepad)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceJoystick](https://developer.apple.com/documentation/iobluetooth/kbluetoothgapappearancehumaninterfacedevicejoystick)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceKeyboard](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearancehumaninterfacedevicekeyboard)Added [kBluetoothGAPAppearanceHumanInterfaceDeviceMouse](https://developer.apple.com/documentation/kernel/1640542-anonymous/kbluetoothgapappearancehumaninterfacedevicemouse)Added [kBluetoothGAPAppearanceUnknown](https://developer.apple.com/documentation/iobluetooth/1458967-anonymous/kbluetoothgapappearanceunknown)Added [kBluetoothHCIExtendedInquiryResponseDataTypeAppearance](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeappearance)Added [kBluetoothHCIExtendedInquiryResponseDataTypePublicTargetAddress](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypepublictargetaddress)Added [kBluetoothHCIExtendedInquiryResponseDataTypeRandomTargetAddress](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatyperandomtargetaddress)Added [kBluetoothHCIVersionCoreSpecification4_1](https://developer.apple.com/documentation/kernel/bluetoothhciversions/kbluetoothhciversioncorespecification4_1)Added [kBluetoothLMPVersionCoreSpecification4_1](https://developer.apple.com/documentation/kernel/bluetoothlmpversions/kbluetoothlmpversioncorespecification4_1)Added [kBluetoothSDPUUID16MCAPControlChannel](https://developer.apple.com/documentation/kernel/1640486-anonymous/kbluetoothsdpuuid16mcapcontrolchannel)Added [kBluetoothSDPUUID16MCAPDataChannel](https://developer.apple.com/documentation/iobluetooth/1459140-anonymous/kbluetoothsdpuuid16mcapdatachannel)Added [kBluetoothSDPUUID16ServiceClassGlobalNavigationSatelliteSystem](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpuuid16serviceclassglobalnavigationsatellitesystem)Added [kBluetoothSDPUUID16ServiceClassGlobalNavigationSatelliteSystemServer](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpuuid16serviceclassglobalnavigationsatellitesystemserver)Added [kBluetoothSDPUUID16ServiceClassHealthDevice](https://developer.apple.com/documentation/kernel/sdpserviceclasses/kbluetoothsdpuuid16serviceclasshealthdevice)Added [kBluetoothSDPUUID16ServiceClassHealthDeviceSink](https://developer.apple.com/documentation/iobluetooth/sdpserviceclasses/kbluetoothsdpuuid16serviceclasshealthdevicesink)Added [kBluetoothSDPUUID16ServiceClassHealthDeviceSource](https://developer.apple.com/documentation/kernel/sdpserviceclasses/kbluetoothsdpuuid16serviceclasshealthdevicesource)Added [kBluetoothSDPUUID16ServiceClassVideoDistribution](https://developer.apple.com/documentation/iobluetooth/kbluetoothsdpuuid16serviceclassvideodistribution)Added [kBluetoothSDPUUID16ServiceClassVideoSink](https://developer.apple.com/documentation/iobluetooth/sdpserviceclasses/kbluetoothsdpuuid16serviceclassvideosink)Added [kBluetoothSDPUUID16ServiceClassVideoSource](https://developer.apple.com/documentation/iobluetooth/sdpserviceclasses/kbluetoothsdpuuid16serviceclassvideosource)IOAccelTypes.hRemoved kIOAccelKeycolorSurfaceIOAudioDefines.hRemoved #def kIOAudioEngineClientDescriptionRemoved #def kIOAudioEngineClientDescriptionKeyRemoved #def kIOAudioEngineDeviceDescriptionRemoved #def kIOAudioEngineDeviceDescriptionKey_InputDigitalBoostGainRemoved #def kIOAudioEngineDeviceDescriptionKey_PostprocessingInputGainRemoved kIOAudioEngineGeneralClientRemoved kIOAudioEngineIronWoodClientRemoved kIOAudioEngineVoiceClientIOBluetoothHIDDriver.hAdded IOBluetoothHIDDriver::GetCurrentTime()Added IOBluetoothHIDDriver::ReadyToSleepTimerFired()Added IOBluetoothHIDDriver::handleReadyToSleepTimerFired()IODMAController.hAdded IODMAController::setDMAConfig()Added IODMAController::setFIFODepth()Added IODMAController::validDMAConfig()Added IODMAController::validFIFODepth()Modified IODMAController::getFIFODepth()

|  | Declaration |
| --- | --- |
| From | virtual IOByteCount getFIFODepth ( UInt32 dmaIndex); |
| To | virtual IOByteCount getFIFODepth ( UInt32 dmaIndex, IODirection direction); |

Modified IODMAController::notifyDMACommand()

|  | Declaration |
| --- | --- |
| From | virtual void notifyDMACommand ( IODMAEventSource \*dmaES, IODMACommand \*dmaCommand, IOReturn status, IOByteCount actualByteCount); |
| To | virtual void notifyDMACommand ( IODMAEventSource \*dmaES, IODMACommand \*dmaCommand, IOReturn status, IOByteCount actualByteCount, AbsoluteTime timeStamp); |

IODMAEventSource.hAdded IODMAEventSource::free()Added IODMAEventSource::setDMAConfig()Added IODMAEventSource::setFIFODepth()Added IODMAEventSource::validDMAConfig()Added IODMAEventSource::validFIFODepth()Modified IODMAEventSource::getFIFODepth()

|  | Declaration |
| --- | --- |
| From | virtual IOByteCount getFIFODepth ( void); |
| To | virtual IOByteCount getFIFODepth ( IODirection direction); |

Modified IODMAEventSource::notifyDMACommand()

|  | Declaration |
| --- | --- |
| From | virtual void notifyDMACommand ( IODMACommand \*dmaCommand, IOReturn status, IOByteCount actualByteCount); |
| To | virtual void notifyDMACommand ( IODMACommand \*dmaCommand, IOReturn status, IOByteCount actualByteCount, AbsoluteTime timeStamp); |

IODeviceTreeSupport.hRemoved IODTCompareAddressCell64FuncAdded [IODTGetCellCounts()](https://developer.apple.com/documentation/kernel/1442140-iodtgetcellcounts)IOGraphicsTypes.hAdded [kConnectionAudioStreaming](https://developer.apple.com/documentation/iokit/1505380-anonymous/kconnectionaudiostreaming)Added #def kIODisplayEDIDOriginalKeyAdded #def kIOFBHDMIDongleROMKeyIOHIDDescriptorParser.hModified HIDGetButtons()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetButtons ( HIDReportType reportType, UInt32 collection, HIDUsageAndPagePtr usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDGetButtons ( HIDReportType reportType, UInt32 collection, HIDUsageAndPagePtr usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDGetButtonsOnPage()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetButtonsOnPage ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage \*usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDGetButtonsOnPage ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage \*usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDGetReportLength()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetReportLength ( HIDReportType reportType, UInt8 reportID, ByteCount \*reportLength, HIDPreparsedDataRef preparsedDataRef); |
| To | OSStatus HIDGetReportLength ( HIDReportType reportType, UInt8 reportID, IOByteCount \*reportLength, HIDPreparsedDataRef preparsedDataRef); |

Modified HIDGetScaledUsageValue()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetScaledUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 \*usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDGetScaledUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 \*usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDGetUsageValue()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 \*usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDGetUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 \*usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDGetUsageValueArray()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDGetUsageValueArray ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, Byte \*usageValueBuffer, ByteCount usageValueBufferSize, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDGetUsageValueArray ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, UInt8 \*usageValueBuffer, IOByteCount usageValueBufferSize, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDInitReport()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDInitReport ( HIDReportType reportType, UInt8 reportID, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDInitReport ( HIDReportType reportType, UInt8 reportID, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDOpenReportDescriptor()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDOpenReportDescriptor ( void \*hidReportDescriptor, ByteCount descriptorLength, HIDPreparsedDataRef \*preparsedDataRef, UInt32 flags); |
| To | OSStatus HIDOpenReportDescriptor ( void \*hidReportDescriptor, IOByteCount descriptorLength, HIDPreparsedDataRef \*preparsedDataRef, UInt32 flags); |

Modified HIDSetButton()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDSetButton ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDSetButton ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDSetButtons()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDSetButtons ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage \*usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDSetButtons ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage \*usageList, UInt32 \*usageListSize, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDSetScaledUsageValue()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDSetScaledUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDSetScaledUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDSetUsageValue()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDSetUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDSetUsageValue ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, SInt32 usageValue, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

Modified HIDSetUsageValueArray()

|  | Declaration |
| --- | --- |
| From | OSStatus HIDSetUsageValueArray ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, Byte \*usageValueBuffer, ByteCount usageValueBufferLength, HIDPreparsedDataRef preparsedDataRef, void \*report, ByteCount reportLength); |
| To | OSStatus HIDSetUsageValueArray ( HIDReportType reportType, HIDUsage usagePage, UInt32 collection, HIDUsage usage, UInt8 \*usageValueBuffer, IOByteCount usageValueBufferLength, HIDPreparsedDataRef preparsedDataRef, void \*report, IOByteCount reportLength); |

IOHIDDevice.hModified IOHIDDevice::newDeviceUsagePairs()

|  | Declaration |
| --- | --- |
| From | OSArray \* newDeviceUsagePairs ( void); |
| To | virtual OSArray \* newDeviceUsagePairs ( void); |

IOHIDElement.hAdded IOHIDElement::conformsTo()Added IOHIDElement::getScaledFixedValue()Added IOHIDElement::getScaledValue()Added IOHIDElement::setCalibration()IOHIDEventDriver.hAdded IOHIDEventDriver::calibrateAxisToButtonElement()Added IOHIDEventDriver::calibrateDigitizerElement()Added IOHIDEventDriver::calibratePreferredStateElement()Added IOHIDEventDriver::processMultiAxisElement()IOHIDEventService.hAdded IOHIDEventService::dispatchDigitizerEvent()Added IOHIDEventService::dispatchDigitizerEventWithOrientation()Added IOHIDEventService::dispatchDigitizerEventWithPolarOrientation()Added IOHIDEventService::dispatchDigitizerEventWithTiltOrientation()Added IOHIDEventService::dispatchMultiAxisPointerEvent()Added IOHIDEventService::getReportInterval()Added IOHIDEventService::multiAxisTimerCallback()Modified IOHIDEventService::createTransducerData()

|  | Declaration |
| --- | --- |
| From | TransducerData \* createTransducerData ( UInt32 tranducerID); |
| To | TransducerData \* createTransducerData ( UInt32 transducerID); |

Modified IOHIDEventService::dispatchTabletPointerEvent()

|  | Declaration |
| --- | --- |
| From | virtual void dispatchTabletPointerEvent ( AbsoluteTime timeStamp, UInt32 tranducerID, SInt32 x, SInt32 y, SInt32 z, IOGBounds \*bounds, UInt32 buttonState, SInt32 tipPressure, SInt32 tipPressureMin, SInt32 tipPressureMax, SInt32 barrelPressure, SInt32 barrelPressureMin, SInt32 barrelPressureMax, SInt32 tiltX, SInt32 tiltY, UInt32 twist, IOOptionBits options); |
| To | virtual void dispatchTabletPointerEvent ( AbsoluteTime timeStamp, UInt32 transducerID, SInt32 x, SInt32 y, SInt32 z, IOGBounds \*bounds, UInt32 buttonState, SInt32 tipPressure, SInt32 tipPressureMin, SInt32 tipPressureMax, SInt32 barrelPressure, SInt32 barrelPressureMin, SInt32 barrelPressureMax, SInt32 tiltX, SInt32 tiltY, UInt32 twist, IOOptionBits options); |

Modified IOHIDEventService::dispatchTabletProximityEvent()

|  | Declaration |
| --- | --- |
| From | virtual void dispatchTabletProximityEvent ( AbsoluteTime timeStamp, UInt32 tranducerID, bool inRange, bool invert, UInt32 vendorTransducerUniqueID, UInt32 vendorTransducerSerialNumber, IOOptionBits options); |
| To | virtual void dispatchTabletProximityEvent ( AbsoluteTime timeStamp, UInt32 transducerID, bool inRange, bool invert, UInt32 vendorTransducerUniqueID, UInt32 vendorTransducerSerialNumber, IOOptionBits options); |

Modified IOHIDEventService::getTransducerData()

|  | Declaration |
| --- | --- |
| From | TransducerData \* getTransducerData ( UInt32 tranducerID); |
| To | TransducerData \* getTransducerData ( UInt32 transducerID); |

IOHIDKeys.hRemoved [#def kIOHIDDeviceKeyboardLanguageKey](https://developer.apple.com/documentation/iokit/iohidkeys.h_user_space/hid_device_property_keys/kiohiddevicekeyboardlanguagekey)Removed [#def kIOHIDDeviceKeyboardStandardTypeKey](https://developer.apple.com/documentation/iokit/iohidkeys.h_user_space/hid_device_property_keys/kiohiddevicekeyboardstandardtypekey)Added [IOHIDValueOptions](https://developer.apple.com/documentation/kernel/iohidvalueoptions)Added [IOHIDValueScaleType](https://developer.apple.com/documentation/iokit/iohidvaluescaletype)Added #def kIOHIDAltHandlerIdKeyAdded #def kIOHIDBuiltInKeyAdded #def kIOHIDDisplayIntegratedKeyAdded #def kIOHIDKeyboardLanguageKeyAdded #def kIOHIDPowerOnDelayNSKeyAdded #def kIOHIDProductIDArrayKeyAdded #def kIOHIDProductIDMaskKeyAdded #def kIOHIDSampleIntervalKeyAdded [kIOHIDValueOptionsFlagRelativeSimple](https://developer.apple.com/documentation/kernel/1644493-anonymous/kiohidvalueoptionsflagrelativesimple)Added [kIOHIDValueScaleTypeCalibrated](https://developer.apple.com/documentation/iokit/1556676-anonymous/kiohidvaluescaletypecalibrated)Added [kIOHIDValueScaleTypePhysical](https://developer.apple.com/documentation/kernel/1644492-anonymous/kiohidvaluescaletypephysical)IOHIDParameter.hAdded #def kHIDScrollAccelParametricCurvesDebugKeyAdded [kIOHIDActivityDisplayOn](https://developer.apple.com/documentation/kernel/1644785-anonymous/kiohidactivitydisplayon)Added [kIOHIDActivityUserIdle](https://developer.apple.com/documentation/kernel/1644785-anonymous/kiohidactivityuseridle)IOHIDSystem.hRemoved IOHIDSystem::doExtGetToggleState()Removed IOHIDSystem::doExtSetToggleState()Removed IOHIDSystem::extGetModifierLockState()Removed IOHIDSystem::extSetModifierLockState()Removed IOHIDSystem::vblEvent()Removed #def sub_iokit_hidsystemAdded IOHIDSystem::doExtGetStateForSelector()Added IOHIDSystem::doExtSetStateForSelector()Added IOHIDSystem::doProcessNotifications()Added IOHIDSystem::extGetStateForSelector()Added IOHIDSystem::extGetUserHidActivityState()Added IOHIDSystem::extSetStateForSelector()Added IOHIDSystem::getUserHidActivityState()Added IOHIDSystem::getUserHidActivityStateGated()Added IOHIDSystem::hidActivityChecker()Added IOHIDSystem::reportUserHidActivity()Added IOHIDSystem::reportUserHidActivityGated()Added IOHIDSystem::updateHidActivity()Added #def kIOHIDSystemUserHidActivityModified IOHIDSystem::genericNotificationHandler()

|  | Declaration |
| --- | --- |
| From | bool genericNotificationHandler ( void \*target, void \*ref, IOService \*newService, IONotifier \*notifier); |
| To | bool genericNotificationHandler ( void \*ref, IOService \*newService, IONotifier \*notifier); |

Modified IOHIDSystem::relativePointerEventGated()

|  | Declaration |
| --- | --- |
| From | void relativePointerEventGated ( int buttons, int dx, int dy, AbsoluteTime ts, OSObject \*sender); |
| To | void relativePointerEventGated ( int buttons, int dx, int dy, SInt64 ts, OSObject \*sender); |

IOHIDUsageTables.hAdded [kHIDPage_Sensor](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_sensor)Added [kHIDUsage_Csmr_ACAddToCart](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acaddtocart)Added [kHIDUsage_Csmr_ACAllCaps](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acallcaps)Added [kHIDUsage_Csmr_ACAttachComment](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acattachcomment)Added [kHIDUsage_Csmr_ACAttachFile](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acattachfile)Added [kHIDUsage_Csmr_ACBold](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acbold)Added [kHIDUsage_Csmr_ACBulletedList](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acbulletedlist)Added [kHIDUsage_Csmr_ACBuyOrCheckout](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acbuyorcheckout)Added [kHIDUsage_Csmr_ACCancel](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_accancel)Added [kHIDUsage_Csmr_ACCatalog](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_accatalog)Added [kHIDUsage_Csmr_ACClearAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acclearalarm)Added [kHIDUsage_Csmr_ACCollapse](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_accollapse)Added [kHIDUsage_Csmr_ACCollapseAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_accollapseall)Added [kHIDUsage_Csmr_ACDelete](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdelete)Added [kHIDUsage_Csmr_ACDemote](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdemote)Added [kHIDUsage_Csmr_ACDetachComment](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdetachcomment)Added [kHIDUsage_Csmr_ACDistributeH](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdistributeh)Added [kHIDUsage_Csmr_ACDistributeV](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acdistributev)Added [kHIDUsage_Csmr_ACDownload](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acdownload)Added [kHIDUsage_Csmr_ACEdit](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acedit)Added [kHIDUsage_Csmr_ACEditTimeZones](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acedittimezones)Added [kHIDUsage_Csmr_ACExpand](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acexpand)Added [kHIDUsage_Csmr_ACExpandAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acexpandall)Added [kHIDUsage_Csmr_ACFilter](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acfilter)Added [kHIDUsage_Csmr_ACFlipHorizontal](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfliphorizontal)Added [kHIDUsage_Csmr_ACFlipVertical](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acflipvertical)Added [kHIDUsage_Csmr_ACFontColor](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfontcolor)Added [kHIDUsage_Csmr_ACFontSelect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfontselect)Added [kHIDUsage_Csmr_ACFontSize](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acfontsize)Added [kHIDUsage_Csmr_ACForwardMessage](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acforwardmessage)Added [kHIDUsage_Csmr_ACIndentyDecrease](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acindentydecrease)Added [kHIDUsage_Csmr_ACIndentyIncrease](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acindentyincrease)Added [kHIDUsage_Csmr_ACInsertColumn](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertcolumn)Added [kHIDUsage_Csmr_ACInsertFile](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertfile)Added [kHIDUsage_Csmr_ACInsertMode](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertmode)Added [kHIDUsage_Csmr_ACInsertObject](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertobject)Added [kHIDUsage_Csmr_ACInsertPicture](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertpicture)Added [kHIDUsage_Csmr_ACInsertRow](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acinsertrow)Added [kHIDUsage_Csmr_ACInsertSymbol](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertsymbol)Added [kHIDUsage_Csmr_ACItalics](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acitalics)Added [kHIDUsage_Csmr_ACJustifyBlockH](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyblockh)Added [kHIDUsage_Csmr_ACJustifyBlockV](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyblockv)Added [kHIDUsage_Csmr_ACJustifyBottom](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifybottom)Added [kHIDUsage_Csmr_ACJustifyCenterH](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifycenterh)Added [kHIDUsage_Csmr_ACJustifyCenterV](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acjustifycenterv)Added [kHIDUsage_Csmr_ACJustifyLeft](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acjustifyleft)Added [kHIDUsage_Csmr_ACJustifyRight](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyright)Added [kHIDUsage_Csmr_ACJustifyTop](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifytop)Added [kHIDUsage_Csmr_ACLock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aclock)Added [kHIDUsage_Csmr_ACMerge](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acmerge)Added [kHIDUsage_Csmr_ACMirrorHorizontal](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acmirrorhorizontal)Added [kHIDUsage_Csmr_ACMirrorVertical](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acmirrorvertical)Added [kHIDUsage_Csmr_ACNo](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acno)Added [kHIDUsage_Csmr_ACNumberedList](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acnumberedlist)Added [kHIDUsage_Csmr_ACPasteSpecial](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acpastespecial)Added [kHIDUsage_Csmr_ACPrintPreview](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acprintpreview)Added [kHIDUsage_Csmr_ACPromote](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acpromote)Added [kHIDUsage_Csmr_ACProtect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acprotect)Added [kHIDUsage_Csmr_ACRedoOrRepeat](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acredoorrepeat)Added [kHIDUsage_Csmr_ACRename](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acrename)Added [kHIDUsage_Csmr_ACReply](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acreply)Added [kHIDUsage_Csmr_ACReplyAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acreplyall)Added [kHIDUsage_Csmr_ACResetAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acresetalarm)Added [kHIDUsage_Csmr_ACResize](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acresize)Added [kHIDUsage_Csmr_ACRestartNumbering](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acrestartnumbering)Added [kHIDUsage_Csmr_ACRotate](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acrotate)Added [kHIDUsage_Csmr_ACSaveAndClose](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsaveandclose)Added [kHIDUsage_Csmr_ACSelectColumn](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectcolumn)Added [kHIDUsage_Csmr_ACSelectObject](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselectobject)Added [kHIDUsage_Csmr_ACSelectParagraph](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectparagraph)Added [kHIDUsage_Csmr_ACSelectRow](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectrow)Added [kHIDUsage_Csmr_ACSelectSentence](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselectsentence)Added [kHIDUsage_Csmr_ACSelectTable](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselecttable)Added [kHIDUsage_Csmr_ACSelectTimeZone](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselecttimezone)Added [kHIDUsage_Csmr_ACSelectWord](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectword)Added [kHIDUsage_Csmr_ACSend](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsend)Added [kHIDUsage_Csmr_ACSendOrReceive](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsendorreceive)Added [kHIDUsage_Csmr_ACSendTo](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsendto)Added [kHIDUsage_Csmr_ACSetAlarm](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetalarm)Added [kHIDUsage_Csmr_ACSetBorders](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetborders)Added [kHIDUsage_Csmr_ACSetClock](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetclock)Added [kHIDUsage_Csmr_ACSnoozeAlarm](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsnoozealarm)Added [kHIDUsage_Csmr_ACSort](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsort)Added [kHIDUsage_Csmr_ACSortAscending](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsortascending)Added [kHIDUsage_Csmr_ACSortDescending](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsortdescending)Added [kHIDUsage_Csmr_ACSplit](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsplit)Added [kHIDUsage_Csmr_ACStrikethrough](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acstrikethrough)Added [kHIDUsage_Csmr_ACSubscript](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsubscript)Added [kHIDUsage_Csmr_ACSuperscript](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsuperscript)Added [kHIDUsage_Csmr_ACSynchronize](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsynchronize)Added [kHIDUsage_Csmr_ACUnderline](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acunderline)Added [kHIDUsage_Csmr_ACUnlock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acunlock)Added [kHIDUsage_Csmr_ACUnprotect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acunprotect)Added [kHIDUsage_Csmr_ACUpload](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acupload)Added [kHIDUsage_Csmr_ACViewClock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acviewclock)Added [kHIDUsage_Csmr_ACViewComment](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acviewcomment)Added [kHIDUsage_Csmr_ACYes](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acyes)Added [kHIDUsage_Csmr_ALAudioBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alaudiobrowser)Added [kHIDUsage_Csmr_ALAudioPlayer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alaudioplayer)Added [kHIDUsage_Csmr_ALCustomizedCorporateNewsBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alcustomizedcorporatenewsbrowser)Added [kHIDUsage_Csmr_ALDigitalRightsManager](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_aldigitalrightsmanager)Added [kHIDUsage_Csmr_ALDigitalWallet](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aldigitalwallet)Added [kHIDUsage_Csmr_ALEntertainmentContentBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alentertainmentcontentbrowser)Added [kHIDUsage_Csmr_ALImageBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alimagebrowser)Added [kHIDUsage_Csmr_ALInstantMessaging](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alinstantmessaging)Added [kHIDUsage_Csmr_ALMarketMonitorOrFinanceBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_almarketmonitororfinancebrowser)Added [kHIDUsage_Csmr_ALMovieBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_almoviebrowser)Added [kHIDUsage_Csmr_ALOEMFeatureBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aloemfeaturebrowser)Added [kHIDUsage_Csmr_ALOEMHelp](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_aloemhelp)Added [kHIDUsage_Csmr_ALOnlineActivityBrowswer](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alonlineactivitybrowswer)Added [kHIDUsage_Csmr_ALOnlineCommunity](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alonlinecommunity)Added [kHIDUsage_Csmr_ALOnlineShoppingBrowswer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alonlineshoppingbrowswer)Added [kHIDUsage_Csmr_ALResearchOrSearchBrowswer](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alresearchorsearchbrowswer)Added [kHIDUsage_Csmr_ALSmartCardInformationOrHelp](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alsmartcardinformationorhelp)Added [kHIDUsage_Csmr_DuressAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_duressalarm)Added [kHIDUsage_Csmr_GraphicEqualizer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_graphicequalizer)Added [kHIDUsage_Csmr_Headphone](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_headphone)Added [kHIDUsage_Csmr_HoldupAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_holdupalarm)Added [kHIDUsage_Csmr_MedicalAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_medicalalarm)Added [kHIDUsage_Csmr_Microphone](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_microphone)Added [kHIDUsage_Csmr_Motion](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_motion)Added [kHIDUsage_Csmr_Proximity](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_proximity)Added [kHIDUsage_Snsr_Biometric](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric)Added [kHIDUsage_Snsr_Biometric_HumanPresence](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric_humanpresence)Added [kHIDUsage_Snsr_Biometric_HumanProximity](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric_humanproximity)Added [kHIDUsage_Snsr_Biometric_HumanTouch](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_biometric_humantouch)Added [kHIDUsage_Snsr_Electrical](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical)Added [kHIDUsage_Snsr_Electrical_Capacitance](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_capacitance)Added [kHIDUsage_Snsr_Electrical_Current](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_current)Added [kHIDUsage_Snsr_Electrical_Frequency](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_frequency)Added [kHIDUsage_Snsr_Electrical_Inductance](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_inductance)Added [kHIDUsage_Snsr_Electrical_Period](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_period)Added [kHIDUsage_Snsr_Electrical_Potentiometer](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_potentiometer)Added [kHIDUsage_Snsr_Electrical_Power](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_power)Added [kHIDUsage_Snsr_Electrical_Resistance](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_resistance)Added [kHIDUsage_Snsr_Electrical_Voltage](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_voltage)Added [kHIDUsage_Snsr_Environmental](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental)Added [kHIDUsage_Snsr_Environmental_AtmosphericPressure](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_atmosphericpressure)Added [kHIDUsage_Snsr_Environmental_Humidity](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental_humidity)Added [kHIDUsage_Snsr_Environmental_Temperature](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental_temperature)Added [kHIDUsage_Snsr_Environmental_WindDirection](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_winddirection)Added [kHIDUsage_Snsr_Environmental_WindSpeed](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_windspeed)Added [kHIDUsage_Snsr_Event](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event)Added [kHIDUsage_Snsr_Event_SensorEvent](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent)Added [kHIDUsage_Snsr_Event_SensorEvent_ChangeSensitivity](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_changesensitivity)Added [kHIDUsage_Snsr_Event_SensorEvent_ComplexTrigger](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_complextrigger)Added [kHIDUsage_Snsr_Event_SensorEvent_DataUpdated](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_dataupdated)Added [kHIDUsage_Snsr_Event_SensorEvent_FrequencyExceeded](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_frequencyexceeded)Added [kHIDUsage_Snsr_Event_SensorEvent_HighThresholdCrossDown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_highthresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_HighThresholdCrossUp](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_highthresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorEvent_LowThresholdCrossDown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_lowthresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_LowThresholdCrossUp](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_lowthresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorEvent_PeriodExceeded](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_periodexceeded)Added [kHIDUsage_Snsr_Event_SensorEvent_PollResponse](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_pollresponse)Added [kHIDUsage_Snsr_Event_SensorEvent_PropertyChanged](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_propertychanged)Added [kHIDUsage_Snsr_Event_SensorEvent_RangeMaxReached](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_rangemaxreached)Added [kHIDUsage_Snsr_Event_SensorEvent_RangeMinReached](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_rangeminreached)Added [kHIDUsage_Snsr_Event_SensorEvent_StateChanged](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_statechanged)Added [kHIDUsage_Snsr_Event_SensorEvent_Unknown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_unknown)Added [kHIDUsage_Snsr_Event_SensorEvent_ZeroThresholdCrossDown](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_zerothresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_ZeroThresholdCrossUp](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_zerothresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorState](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate)Added [kHIDUsage_Snsr_Event_SensorState_AccessDenied](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_accessdenied)Added [kHIDUsage_Snsr_Event_SensorState_Error](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_error)Added [kHIDUsage_Snsr_Event_SensorState_Initializing](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_initializing)Added [kHIDUsage_Snsr_Event_SensorState_NoData](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorstate_nodata)Added [kHIDUsage_Snsr_Event_SensorState_NotAvailable](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorstate_notavailable)Added [kHIDUsage_Snsr_Event_SensorState_Ready](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_ready)Added [kHIDUsage_Snsr_Event_SensorState_Undefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_undefined)Added [kHIDUsage_Snsr_Light](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light)Added [kHIDUsage_Snsr_Light_AmbientLight](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_light_ambientlight)Added [kHIDUsage_Snsr_Light_ConsumerInfrared](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light_consumerinfrared)Added [kHIDUsage_Snsr_Location](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location)Added [kHIDUsage_Snsr_Location_Broadcast](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_broadcast)Added [kHIDUsage_Snsr_Location_DeadReckoning](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_deadreckoning)Added [kHIDUsage_Snsr_Location_GPS](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_gps)Added [kHIDUsage_Snsr_Location_Lookup](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_lookup)Added [kHIDUsage_Snsr_Location_Other](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_other)Added [kHIDUsage_Snsr_Location_Static](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_static)Added [kHIDUsage_Snsr_Location_Triangulation](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_triangulation)Added [kHIDUsage_Snsr_Mechanical](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical)Added [kHIDUsage_Snsr_Mechanical_BooleanSwitch](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_booleanswitch)Added [kHIDUsage_Snsr_Mechanical_BooleanSwitchArray](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_booleanswitcharray)Added [kHIDUsage_Snsr_Mechanical_Force](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_force)Added [kHIDUsage_Snsr_Mechanical_HallEffectSwitch](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_halleffectswitch)Added [kHIDUsage_Snsr_Mechanical_HapticVibrator](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_hapticvibrator)Added [kHIDUsage_Snsr_Mechanical_MultivalueSwitch](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_multivalueswitch)Added [kHIDUsage_Snsr_Mechanical_Pressure](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_pressure)Added [kHIDUsage_Snsr_Mechanical_Strain](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_strain)Added [kHIDUsage_Snsr_Mechanical_Weight](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_weight)Added [kHIDUsage_Snsr_Modifier_Accuracy](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_accuracy)Added [kHIDUsage_Snsr_Modifier_CalibrationMultiplier](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_calibrationmultiplier)Added [kHIDUsage_Snsr_Modifier_CalibrationOffset](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_calibrationoffset)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityAbsolute](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_changesensitivityabsolute)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityPercentRange](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_changesensitivitypercentrange)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityPercentRelative](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_changesensitivitypercentrelative)Added [kHIDUsage_Snsr_Modifier_FrequencyMax](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_frequencymax)Added [kHIDUsage_Snsr_Modifier_Max](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_max)Added [kHIDUsage_Snsr_Modifier_Min](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_min)Added [kHIDUsage_Snsr_Modifier_None](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_none)Added [kHIDUsage_Snsr_Modifier_PeriodMax](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_periodmax)Added [kHIDUsage_Snsr_Modifier_ReportInterval](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_reportinterval)Added [kHIDUsage_Snsr_Modifier_Resolution](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_resolution)Added [kHIDUsage_Snsr_Modifier_ThresholdHigh](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_thresholdhigh)Added [kHIDUsage_Snsr_Modifier_ThresholdLow](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_thresholdlow)Added [kHIDUsage_Snsr_Modifier_VendorDefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_vendordefined)Added [kHIDUsage_Snsr_Motion](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion)Added [kHIDUsage_Snsr_Motion_Accelerometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer)Added [kHIDUsage_Snsr_Motion_Accelerometer1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer1d)Added [kHIDUsage_Snsr_Motion_Accelerometer2D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_motion_accelerometer2d)Added [kHIDUsage_Snsr_Motion_Accelerometer3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer3d)Added [kHIDUsage_Snsr_Motion_Gyrometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer)Added [kHIDUsage_Snsr_Motion_Gyrometer1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer1d)Added [kHIDUsage_Snsr_Motion_Gyrometer2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer2d)Added [kHIDUsage_Snsr_Motion_Gyrometer3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer3d)Added [kHIDUsage_Snsr_Motion_MotionDetector](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_motion_motiondetector)Added [kHIDUsage_Snsr_Motion_Speedometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_speedometer)Added [kHIDUsage_Snsr_Orientation](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation)Added [kHIDUsage_Snsr_Orientation_Compass1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compass1d)Added [kHIDUsage_Snsr_Orientation_Compass2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compass2d)Added [kHIDUsage_Snsr_Orientation_Compass3D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_compass3d)Added [kHIDUsage_Snsr_Orientation_CompassD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compassd)Added [kHIDUsage_Snsr_Orientation_DeviceOrientation](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_deviceorientation)Added [kHIDUsage_Snsr_Orientation_Distance1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distance1d)Added [kHIDUsage_Snsr_Orientation_Distance2D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_distance2d)Added [kHIDUsage_Snsr_Orientation_Distance3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distance3d)Added [kHIDUsage_Snsr_Orientation_DistanceD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distanced)Added [kHIDUsage_Snsr_Orientation_Inclinometer1D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_inclinometer1d)Added [kHIDUsage_Snsr_Orientation_Inclinometer2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_inclinometer2d)Added [kHIDUsage_Snsr_Orientation_Inclinometer3D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_inclinometer3d)Added [kHIDUsage_Snsr_Orientation_InclinometerD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_inclinometerd)Added [kHIDUsage_Snsr_Other](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other)Added [kHIDUsage_Snsr_Other_Custom](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_custom)Added [kHIDUsage_Snsr_Other_Generic](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_generic)Added [kHIDUsage_Snsr_Other_GenericEnumerator](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_genericenumerator)Added [kHIDUsage_Snsr_Property](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property)Added [kHIDUsage_Snsr_Property_Accuracy](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_accuracy)Added [kHIDUsage_Snsr_Property_ChangeSensitivityAbsolute](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_changesensitivityabsolute)Added [kHIDUsage_Snsr_Property_ChangeSensitivityPercentRange](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_changesensitivitypercentrange)Added [kHIDUsage_Snsr_Property_ChangeSensitivityPercentRelative](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_changesensitivitypercentrelative)Added [kHIDUsage_Snsr_Property_ConnectionType](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype)Added [kHIDUsage_Snsr_Property_ConnectionType_Attached](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype_attached)Added [kHIDUsage_Snsr_Property_ConnectionType_External](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_connectiontype_external)Added [kHIDUsage_Snsr_Property_ConnectionType_Integrated](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype_integrated)Added [kHIDUsage_Snsr_Property_Description](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_description)Added [kHIDUsage_Snsr_Property_DevicePath](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_devicepath)Added [kHIDUsage_Snsr_Property_FirmwareVersion](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_firmwareversion)Added [kHIDUsage_Snsr_Property_FriendlyName](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_friendlyname)Added [kHIDUsage_Snsr_Property_HardwareRevision](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_hardwarerevision)Added [kHIDUsage_Snsr_Property_Manufacturer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_manufacturer)Added [kHIDUsage_Snsr_Property_Maximum](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_maximum)Added [kHIDUsage_Snsr_Property_Minimum](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_minimum)Added [kHIDUsage_Snsr_Property_MinimumReportInterval](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_minimumreportinterval)Added [kHIDUsage_Snsr_Property_Model](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_model)Added [kHIDUsage_Snsr_Property_PersistentUniqueID](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_persistentuniqueid)Added [kHIDUsage_Snsr_Property_PowerState](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate)Added [kHIDUsage_Snsr_Property_PowerState_D0_FullPower](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_d0_fullpower)Added [kHIDUsage_Snsr_Property_PowerState_D1_LowPower](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_d1_lowpower)Added [kHIDUsage_Snsr_Property_PowerState_D2_Standby](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d2_standby)Added [kHIDUsage_Snsr_Property_PowerState_D3_Sleep](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d3_sleep)Added [kHIDUsage_Snsr_Property_PowerState_D4_PowerOff](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d4_poweroff)Added [kHIDUsage_Snsr_Property_PowerState_Undefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_undefined)Added [kHIDUsage_Snsr_Property_ReleaseData](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_releasedata)Added [kHIDUsage_Snsr_Property_ReportInterval](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportinterval)Added [kHIDUsage_Snsr_Property_ReportingState](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate)Added [kHIDUsage_Snsr_Property_ReportingState_AllEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_allevents)Added [kHIDUsage_Snsr_Property_ReportingState_NoEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_noevents)Added [kHIDUsage_Snsr_Property_ReportingState_ThresholdEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_thresholdevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeAllEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_wakeallevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeNoEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_wakenoevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeThresholdEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_wakethresholdevents)Added [kHIDUsage_Snsr_Property_Resolution](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_resolution)Added [kHIDUsage_Snsr_Property_ResponseCurve](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_responsecurve)Added [kHIDUsage_Snsr_Property_SamplingRate](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_samplingrate)Added [kHIDUsage_Snsr_Property_SensorStatus](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_sensorstatus)Added [kHIDUsage_Snsr_Property_SerialNumber](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_serialnumber)Added [kHIDUsage_Snsr_Scanner](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_scanner)Added [kHIDUsage_Snsr_Scanner_Barcode](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_barcode)Added [kHIDUsage_Snsr_Scanner_NFC](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_nfc)Added [kHIDUsage_Snsr_Scanner_RFID](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_rfid)Added [kHIDUsage_Snsr_Sensor](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_sensor)Added [kHIDUsage_Snsr_Time](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_time)Added [kHIDUsage_Snsr_Time_AlarmTimer](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_time_alarmtimer)Added [kHIDUsage_Snsr_Time_RealTimeClock](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_time_realtimeclock)Added [kHIDUsage_Snsr_Undefined](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_undefined)IOHIDUsageTables.hAdded [kHIDPage_Sensor](https://developer.apple.com/documentation/iokit/1591932-anonymous/khidpage_sensor)Added [kHIDUsage_Csmr_ACAddToCart](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acaddtocart)Added [kHIDUsage_Csmr_ACAllCaps](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acallcaps)Added [kHIDUsage_Csmr_ACAttachComment](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acattachcomment)Added [kHIDUsage_Csmr_ACAttachFile](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acattachfile)Added [kHIDUsage_Csmr_ACBold](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acbold)Added [kHIDUsage_Csmr_ACBulletedList](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acbulletedlist)Added [kHIDUsage_Csmr_ACBuyOrCheckout](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acbuyorcheckout)Added [kHIDUsage_Csmr_ACCancel](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_accancel)Added [kHIDUsage_Csmr_ACCatalog](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_accatalog)Added [kHIDUsage_Csmr_ACClearAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acclearalarm)Added [kHIDUsage_Csmr_ACCollapse](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_accollapse)Added [kHIDUsage_Csmr_ACCollapseAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_accollapseall)Added [kHIDUsage_Csmr_ACDelete](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdelete)Added [kHIDUsage_Csmr_ACDemote](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdemote)Added [kHIDUsage_Csmr_ACDetachComment](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdetachcomment)Added [kHIDUsage_Csmr_ACDistributeH](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acdistributeh)Added [kHIDUsage_Csmr_ACDistributeV](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acdistributev)Added [kHIDUsage_Csmr_ACDownload](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acdownload)Added [kHIDUsage_Csmr_ACEdit](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acedit)Added [kHIDUsage_Csmr_ACEditTimeZones](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acedittimezones)Added [kHIDUsage_Csmr_ACExpand](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acexpand)Added [kHIDUsage_Csmr_ACExpandAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acexpandall)Added [kHIDUsage_Csmr_ACFilter](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acfilter)Added [kHIDUsage_Csmr_ACFlipHorizontal](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfliphorizontal)Added [kHIDUsage_Csmr_ACFlipVertical](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acflipvertical)Added [kHIDUsage_Csmr_ACFontColor](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfontcolor)Added [kHIDUsage_Csmr_ACFontSelect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acfontselect)Added [kHIDUsage_Csmr_ACFontSize](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acfontsize)Added [kHIDUsage_Csmr_ACForwardMessage](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acforwardmessage)Added [kHIDUsage_Csmr_ACIndentyDecrease](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acindentydecrease)Added [kHIDUsage_Csmr_ACIndentyIncrease](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acindentyincrease)Added [kHIDUsage_Csmr_ACInsertColumn](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertcolumn)Added [kHIDUsage_Csmr_ACInsertFile](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertfile)Added [kHIDUsage_Csmr_ACInsertMode](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertmode)Added [kHIDUsage_Csmr_ACInsertObject](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertobject)Added [kHIDUsage_Csmr_ACInsertPicture](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertpicture)Added [kHIDUsage_Csmr_ACInsertRow](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acinsertrow)Added [kHIDUsage_Csmr_ACInsertSymbol](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acinsertsymbol)Added [kHIDUsage_Csmr_ACItalics](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acitalics)Added [kHIDUsage_Csmr_ACJustifyBlockH](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyblockh)Added [kHIDUsage_Csmr_ACJustifyBlockV](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyblockv)Added [kHIDUsage_Csmr_ACJustifyBottom](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifybottom)Added [kHIDUsage_Csmr_ACJustifyCenterH](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifycenterh)Added [kHIDUsage_Csmr_ACJustifyCenterV](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acjustifycenterv)Added [kHIDUsage_Csmr_ACJustifyLeft](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acjustifyleft)Added [kHIDUsage_Csmr_ACJustifyRight](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifyright)Added [kHIDUsage_Csmr_ACJustifyTop](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acjustifytop)Added [kHIDUsage_Csmr_ACLock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aclock)Added [kHIDUsage_Csmr_ACMerge](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acmerge)Added [kHIDUsage_Csmr_ACMirrorHorizontal](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acmirrorhorizontal)Added [kHIDUsage_Csmr_ACMirrorVertical](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acmirrorvertical)Added [kHIDUsage_Csmr_ACNo](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acno)Added [kHIDUsage_Csmr_ACNumberedList](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acnumberedlist)Added [kHIDUsage_Csmr_ACPasteSpecial](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acpastespecial)Added [kHIDUsage_Csmr_ACPrintPreview](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acprintpreview)Added [kHIDUsage_Csmr_ACPromote](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acpromote)Added [kHIDUsage_Csmr_ACProtect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acprotect)Added [kHIDUsage_Csmr_ACRedoOrRepeat](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acredoorrepeat)Added [kHIDUsage_Csmr_ACRename](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acrename)Added [kHIDUsage_Csmr_ACReply](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acreply)Added [kHIDUsage_Csmr_ACReplyAll](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acreplyall)Added [kHIDUsage_Csmr_ACResetAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acresetalarm)Added [kHIDUsage_Csmr_ACResize](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acresize)Added [kHIDUsage_Csmr_ACRestartNumbering](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acrestartnumbering)Added [kHIDUsage_Csmr_ACRotate](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acrotate)Added [kHIDUsage_Csmr_ACSaveAndClose](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsaveandclose)Added [kHIDUsage_Csmr_ACSelectColumn](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectcolumn)Added [kHIDUsage_Csmr_ACSelectObject](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselectobject)Added [kHIDUsage_Csmr_ACSelectParagraph](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectparagraph)Added [kHIDUsage_Csmr_ACSelectRow](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectrow)Added [kHIDUsage_Csmr_ACSelectSentence](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselectsentence)Added [kHIDUsage_Csmr_ACSelectTable](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acselecttable)Added [kHIDUsage_Csmr_ACSelectTimeZone](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselecttimezone)Added [kHIDUsage_Csmr_ACSelectWord](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acselectword)Added [kHIDUsage_Csmr_ACSend](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsend)Added [kHIDUsage_Csmr_ACSendOrReceive](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsendorreceive)Added [kHIDUsage_Csmr_ACSendTo](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsendto)Added [kHIDUsage_Csmr_ACSetAlarm](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetalarm)Added [kHIDUsage_Csmr_ACSetBorders](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetborders)Added [kHIDUsage_Csmr_ACSetClock](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsetclock)Added [kHIDUsage_Csmr_ACSnoozeAlarm](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsnoozealarm)Added [kHIDUsage_Csmr_ACSort](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsort)Added [kHIDUsage_Csmr_ACSortAscending](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsortascending)Added [kHIDUsage_Csmr_ACSortDescending](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsortdescending)Added [kHIDUsage_Csmr_ACSplit](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsplit)Added [kHIDUsage_Csmr_ACStrikethrough](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acstrikethrough)Added [kHIDUsage_Csmr_ACSubscript](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsubscript)Added [kHIDUsage_Csmr_ACSuperscript](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acsuperscript)Added [kHIDUsage_Csmr_ACSynchronize](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acsynchronize)Added [kHIDUsage_Csmr_ACUnderline](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acunderline)Added [kHIDUsage_Csmr_ACUnlock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acunlock)Added [kHIDUsage_Csmr_ACUnprotect](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acunprotect)Added [kHIDUsage_Csmr_ACUpload](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acupload)Added [kHIDUsage_Csmr_ACViewClock](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acviewclock)Added [kHIDUsage_Csmr_ACViewComment](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_acviewcomment)Added [kHIDUsage_Csmr_ACYes](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_acyes)Added [kHIDUsage_Csmr_ALAudioBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alaudiobrowser)Added [kHIDUsage_Csmr_ALAudioPlayer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alaudioplayer)Added [kHIDUsage_Csmr_ALCustomizedCorporateNewsBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alcustomizedcorporatenewsbrowser)Added [kHIDUsage_Csmr_ALDigitalRightsManager](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_aldigitalrightsmanager)Added [kHIDUsage_Csmr_ALDigitalWallet](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aldigitalwallet)Added [kHIDUsage_Csmr_ALEntertainmentContentBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alentertainmentcontentbrowser)Added [kHIDUsage_Csmr_ALImageBrowser](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alimagebrowser)Added [kHIDUsage_Csmr_ALInstantMessaging](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alinstantmessaging)Added [kHIDUsage_Csmr_ALMarketMonitorOrFinanceBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_almarketmonitororfinancebrowser)Added [kHIDUsage_Csmr_ALMovieBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_almoviebrowser)Added [kHIDUsage_Csmr_ALOEMFeatureBrowser](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_aloemfeaturebrowser)Added [kHIDUsage_Csmr_ALOEMHelp](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_aloemhelp)Added [kHIDUsage_Csmr_ALOnlineActivityBrowswer](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alonlineactivitybrowswer)Added [kHIDUsage_Csmr_ALOnlineCommunity](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alonlinecommunity)Added [kHIDUsage_Csmr_ALOnlineShoppingBrowswer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_alonlineshoppingbrowswer)Added [kHIDUsage_Csmr_ALResearchOrSearchBrowswer](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alresearchorsearchbrowswer)Added [kHIDUsage_Csmr_ALSmartCardInformationOrHelp](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_alsmartcardinformationorhelp)Added [kHIDUsage_Csmr_DuressAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_duressalarm)Added [kHIDUsage_Csmr_GraphicEqualizer](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_graphicequalizer)Added [kHIDUsage_Csmr_Headphone](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_headphone)Added [kHIDUsage_Csmr_HoldupAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_holdupalarm)Added [kHIDUsage_Csmr_MedicalAlarm](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_medicalalarm)Added [kHIDUsage_Csmr_Microphone](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_microphone)Added [kHIDUsage_Csmr_Motion](https://developer.apple.com/documentation/kernel/1641321-anonymous/khidusage_csmr_motion)Added [kHIDUsage_Csmr_Proximity](https://developer.apple.com/documentation/iokit/1592162-anonymous/khidusage_csmr_proximity)Added [kHIDUsage_Snsr_Biometric](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric)Added [kHIDUsage_Snsr_Biometric_HumanPresence](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric_humanpresence)Added [kHIDUsage_Snsr_Biometric_HumanProximity](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_biometric_humanproximity)Added [kHIDUsage_Snsr_Biometric_HumanTouch](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_biometric_humantouch)Added [kHIDUsage_Snsr_Electrical](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical)Added [kHIDUsage_Snsr_Electrical_Capacitance](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_capacitance)Added [kHIDUsage_Snsr_Electrical_Current](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_current)Added [kHIDUsage_Snsr_Electrical_Frequency](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_frequency)Added [kHIDUsage_Snsr_Electrical_Inductance](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_inductance)Added [kHIDUsage_Snsr_Electrical_Period](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_period)Added [kHIDUsage_Snsr_Electrical_Potentiometer](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_potentiometer)Added [kHIDUsage_Snsr_Electrical_Power](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_power)Added [kHIDUsage_Snsr_Electrical_Resistance](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_electrical_resistance)Added [kHIDUsage_Snsr_Electrical_Voltage](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_electrical_voltage)Added [kHIDUsage_Snsr_Environmental](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental)Added [kHIDUsage_Snsr_Environmental_AtmosphericPressure](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_atmosphericpressure)Added [kHIDUsage_Snsr_Environmental_Humidity](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental_humidity)Added [kHIDUsage_Snsr_Environmental_Temperature](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_environmental_temperature)Added [kHIDUsage_Snsr_Environmental_WindDirection](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_winddirection)Added [kHIDUsage_Snsr_Environmental_WindSpeed](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_environmental_windspeed)Added [kHIDUsage_Snsr_Event](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event)Added [kHIDUsage_Snsr_Event_SensorEvent](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent)Added [kHIDUsage_Snsr_Event_SensorEvent_ChangeSensitivity](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_changesensitivity)Added [kHIDUsage_Snsr_Event_SensorEvent_ComplexTrigger](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_complextrigger)Added [kHIDUsage_Snsr_Event_SensorEvent_DataUpdated](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_dataupdated)Added [kHIDUsage_Snsr_Event_SensorEvent_FrequencyExceeded](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_frequencyexceeded)Added [kHIDUsage_Snsr_Event_SensorEvent_HighThresholdCrossDown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_highthresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_HighThresholdCrossUp](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_highthresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorEvent_LowThresholdCrossDown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_lowthresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_LowThresholdCrossUp](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_lowthresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorEvent_PeriodExceeded](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_periodexceeded)Added [kHIDUsage_Snsr_Event_SensorEvent_PollResponse](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_pollresponse)Added [kHIDUsage_Snsr_Event_SensorEvent_PropertyChanged](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_propertychanged)Added [kHIDUsage_Snsr_Event_SensorEvent_RangeMaxReached](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_rangemaxreached)Added [kHIDUsage_Snsr_Event_SensorEvent_RangeMinReached](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_rangeminreached)Added [kHIDUsage_Snsr_Event_SensorEvent_StateChanged](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_statechanged)Added [kHIDUsage_Snsr_Event_SensorEvent_Unknown](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorevent_unknown)Added [kHIDUsage_Snsr_Event_SensorEvent_ZeroThresholdCrossDown](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_zerothresholdcrossdown)Added [kHIDUsage_Snsr_Event_SensorEvent_ZeroThresholdCrossUp](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorevent_zerothresholdcrossup)Added [kHIDUsage_Snsr_Event_SensorState](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate)Added [kHIDUsage_Snsr_Event_SensorState_AccessDenied](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_accessdenied)Added [kHIDUsage_Snsr_Event_SensorState_Error](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_error)Added [kHIDUsage_Snsr_Event_SensorState_Initializing](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_initializing)Added [kHIDUsage_Snsr_Event_SensorState_NoData](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorstate_nodata)Added [kHIDUsage_Snsr_Event_SensorState_NotAvailable](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_event_sensorstate_notavailable)Added [kHIDUsage_Snsr_Event_SensorState_Ready](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_ready)Added [kHIDUsage_Snsr_Event_SensorState_Undefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_event_sensorstate_undefined)Added [kHIDUsage_Snsr_Light](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light)Added [kHIDUsage_Snsr_Light_AmbientLight](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_light_ambientlight)Added [kHIDUsage_Snsr_Light_ConsumerInfrared](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_light_consumerinfrared)Added [kHIDUsage_Snsr_Location](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location)Added [kHIDUsage_Snsr_Location_Broadcast](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_broadcast)Added [kHIDUsage_Snsr_Location_DeadReckoning](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_deadreckoning)Added [kHIDUsage_Snsr_Location_GPS](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_gps)Added [kHIDUsage_Snsr_Location_Lookup](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_lookup)Added [kHIDUsage_Snsr_Location_Other](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_location_other)Added [kHIDUsage_Snsr_Location_Static](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_static)Added [kHIDUsage_Snsr_Location_Triangulation](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_location_triangulation)Added [kHIDUsage_Snsr_Mechanical](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical)Added [kHIDUsage_Snsr_Mechanical_BooleanSwitch](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_booleanswitch)Added [kHIDUsage_Snsr_Mechanical_BooleanSwitchArray](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_booleanswitcharray)Added [kHIDUsage_Snsr_Mechanical_Force](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_force)Added [kHIDUsage_Snsr_Mechanical_HallEffectSwitch](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_halleffectswitch)Added [kHIDUsage_Snsr_Mechanical_HapticVibrator](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_hapticvibrator)Added [kHIDUsage_Snsr_Mechanical_MultivalueSwitch](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_multivalueswitch)Added [kHIDUsage_Snsr_Mechanical_Pressure](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_pressure)Added [kHIDUsage_Snsr_Mechanical_Strain](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_mechanical_strain)Added [kHIDUsage_Snsr_Mechanical_Weight](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_mechanical_weight)Added [kHIDUsage_Snsr_Modifier_Accuracy](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_accuracy)Added [kHIDUsage_Snsr_Modifier_CalibrationMultiplier](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_calibrationmultiplier)Added [kHIDUsage_Snsr_Modifier_CalibrationOffset](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_calibrationoffset)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityAbsolute](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_changesensitivityabsolute)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityPercentRange](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_changesensitivitypercentrange)Added [kHIDUsage_Snsr_Modifier_ChangeSensitivityPercentRelative](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_changesensitivitypercentrelative)Added [kHIDUsage_Snsr_Modifier_FrequencyMax](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_frequencymax)Added [kHIDUsage_Snsr_Modifier_Max](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_max)Added [kHIDUsage_Snsr_Modifier_Min](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_min)Added [kHIDUsage_Snsr_Modifier_None](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_none)Added [kHIDUsage_Snsr_Modifier_PeriodMax](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_periodmax)Added [kHIDUsage_Snsr_Modifier_ReportInterval](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_reportinterval)Added [kHIDUsage_Snsr_Modifier_Resolution](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_modifier_resolution)Added [kHIDUsage_Snsr_Modifier_ThresholdHigh](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_thresholdhigh)Added [kHIDUsage_Snsr_Modifier_ThresholdLow](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_thresholdlow)Added [kHIDUsage_Snsr_Modifier_VendorDefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_modifier_vendordefined)Added [kHIDUsage_Snsr_Motion](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion)Added [kHIDUsage_Snsr_Motion_Accelerometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer)Added [kHIDUsage_Snsr_Motion_Accelerometer1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer1d)Added [kHIDUsage_Snsr_Motion_Accelerometer2D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_motion_accelerometer2d)Added [kHIDUsage_Snsr_Motion_Accelerometer3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_accelerometer3d)Added [kHIDUsage_Snsr_Motion_Gyrometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer)Added [kHIDUsage_Snsr_Motion_Gyrometer1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer1d)Added [kHIDUsage_Snsr_Motion_Gyrometer2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer2d)Added [kHIDUsage_Snsr_Motion_Gyrometer3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_gyrometer3d)Added [kHIDUsage_Snsr_Motion_MotionDetector](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_motion_motiondetector)Added [kHIDUsage_Snsr_Motion_Speedometer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_motion_speedometer)Added [kHIDUsage_Snsr_Orientation](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation)Added [kHIDUsage_Snsr_Orientation_Compass1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compass1d)Added [kHIDUsage_Snsr_Orientation_Compass2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compass2d)Added [kHIDUsage_Snsr_Orientation_Compass3D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_compass3d)Added [kHIDUsage_Snsr_Orientation_CompassD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_compassd)Added [kHIDUsage_Snsr_Orientation_DeviceOrientation](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_deviceorientation)Added [kHIDUsage_Snsr_Orientation_Distance1D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distance1d)Added [kHIDUsage_Snsr_Orientation_Distance2D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_distance2d)Added [kHIDUsage_Snsr_Orientation_Distance3D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distance3d)Added [kHIDUsage_Snsr_Orientation_DistanceD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_distanced)Added [kHIDUsage_Snsr_Orientation_Inclinometer1D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_inclinometer1d)Added [kHIDUsage_Snsr_Orientation_Inclinometer2D](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_inclinometer2d)Added [kHIDUsage_Snsr_Orientation_Inclinometer3D](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_orientation_inclinometer3d)Added [kHIDUsage_Snsr_Orientation_InclinometerD](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_orientation_inclinometerd)Added [kHIDUsage_Snsr_Other](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other)Added [kHIDUsage_Snsr_Other_Custom](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_custom)Added [kHIDUsage_Snsr_Other_Generic](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_generic)Added [kHIDUsage_Snsr_Other_GenericEnumerator](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_other_genericenumerator)Added [kHIDUsage_Snsr_Property](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property)Added [kHIDUsage_Snsr_Property_Accuracy](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_accuracy)Added [kHIDUsage_Snsr_Property_ChangeSensitivityAbsolute](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_changesensitivityabsolute)Added [kHIDUsage_Snsr_Property_ChangeSensitivityPercentRange](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_changesensitivitypercentrange)Added [kHIDUsage_Snsr_Property_ChangeSensitivityPercentRelative](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_changesensitivitypercentrelative)Added [kHIDUsage_Snsr_Property_ConnectionType](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype)Added [kHIDUsage_Snsr_Property_ConnectionType_Attached](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype_attached)Added [kHIDUsage_Snsr_Property_ConnectionType_External](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_connectiontype_external)Added [kHIDUsage_Snsr_Property_ConnectionType_Integrated](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_connectiontype_integrated)Added [kHIDUsage_Snsr_Property_Description](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_description)Added [kHIDUsage_Snsr_Property_DevicePath](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_devicepath)Added [kHIDUsage_Snsr_Property_FirmwareVersion](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_firmwareversion)Added [kHIDUsage_Snsr_Property_FriendlyName](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_friendlyname)Added [kHIDUsage_Snsr_Property_HardwareRevision](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_hardwarerevision)Added [kHIDUsage_Snsr_Property_Manufacturer](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_manufacturer)Added [kHIDUsage_Snsr_Property_Maximum](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_maximum)Added [kHIDUsage_Snsr_Property_Minimum](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_minimum)Added [kHIDUsage_Snsr_Property_MinimumReportInterval](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_minimumreportinterval)Added [kHIDUsage_Snsr_Property_Model](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_model)Added [kHIDUsage_Snsr_Property_PersistentUniqueID](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_persistentuniqueid)Added [kHIDUsage_Snsr_Property_PowerState](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate)Added [kHIDUsage_Snsr_Property_PowerState_D0_FullPower](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_d0_fullpower)Added [kHIDUsage_Snsr_Property_PowerState_D1_LowPower](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_d1_lowpower)Added [kHIDUsage_Snsr_Property_PowerState_D2_Standby](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d2_standby)Added [kHIDUsage_Snsr_Property_PowerState_D3_Sleep](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d3_sleep)Added [kHIDUsage_Snsr_Property_PowerState_D4_PowerOff](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_powerstate_d4_poweroff)Added [kHIDUsage_Snsr_Property_PowerState_Undefined](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_powerstate_undefined)Added [kHIDUsage_Snsr_Property_ReleaseData](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_releasedata)Added [kHIDUsage_Snsr_Property_ReportInterval](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportinterval)Added [kHIDUsage_Snsr_Property_ReportingState](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate)Added [kHIDUsage_Snsr_Property_ReportingState_AllEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_allevents)Added [kHIDUsage_Snsr_Property_ReportingState_NoEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_noevents)Added [kHIDUsage_Snsr_Property_ReportingState_ThresholdEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_thresholdevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeAllEvents](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_reportingstate_wakeallevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeNoEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_wakenoevents)Added [kHIDUsage_Snsr_Property_ReportingState_WakeThresholdEvents](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_reportingstate_wakethresholdevents)Added [kHIDUsage_Snsr_Property_Resolution](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_resolution)Added [kHIDUsage_Snsr_Property_ResponseCurve](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_property_responsecurve)Added [kHIDUsage_Snsr_Property_SamplingRate](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_samplingrate)Added [kHIDUsage_Snsr_Property_SensorStatus](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_sensorstatus)Added [kHIDUsage_Snsr_Property_SerialNumber](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_property_serialnumber)Added [kHIDUsage_Snsr_Scanner](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_scanner)Added [kHIDUsage_Snsr_Scanner_Barcode](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_barcode)Added [kHIDUsage_Snsr_Scanner_NFC](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_nfc)Added [kHIDUsage_Snsr_Scanner_RFID](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_scanner_rfid)Added [kHIDUsage_Snsr_Sensor](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_sensor)Added [kHIDUsage_Snsr_Time](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_time)Added [kHIDUsage_Snsr_Time_AlarmTimer](https://developer.apple.com/documentation/iokit/1591698-anonymous/khidusage_snsr_time_alarmtimer)Added [kHIDUsage_Snsr_Time_RealTimeClock](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_time_realtimeclock)Added [kHIDUsage_Snsr_Undefined](https://developer.apple.com/documentation/kernel/1641608-anonymous/khidusage_snsr_undefined)IOKitDebug.hAdded kIOAppRespStacksOnAdded kIOPersistentLogAdded [kIOSleepWakeWdogOff](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiosleepwakewdogoff)Added [kIOWaitQuietPanics](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiowaitquietpanics)IOKitKeys.hAdded [#def kIOMaximumPriorityCountKey](https://developer.apple.com/documentation/iokit/kiomaximumprioritycountkey)IOLLEvent.hAdded #def NX_ALPHASHIFT_STATELESS_MASKAdded #def NX_DEVICE_ALPHASHIFT_STATELESS_MASKIOMacOSTypes.hRemoved AddressSpaceIDRemoved KernelProcessIDRemoved UnsignedWidePtrRemoved WidePtrIOMapper.hAdded IOMapper::copyMapperForDeviceWithIndex()IOMemoryDescriptor.hAdded IOMemoryDescriptor::getPageCounts()Added [kIODirectionPrepareNoFault](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectionpreparenofault)Added [kIODirectionPrepareReserved1](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectionpreparereserved1)Added [kIODirectionPrepareToPhys32](https://developer.apple.com/documentation/kernel/1643339-anonymous/kiodirectionpreparetophys32)Added [kIOMemoryPurgeableVolatileBehaviorFifo](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilebehaviorfifo)Added [kIOMemoryPurgeableVolatileBehaviorLifo](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilebehaviorlifo)Added [kIOMemoryPurgeableVolatileGroup0](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup0)Added [kIOMemoryPurgeableVolatileGroup1](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup1)Added [kIOMemoryPurgeableVolatileGroup2](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup2)Added [kIOMemoryPurgeableVolatileGroup3](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup3)Added [kIOMemoryPurgeableVolatileGroup4](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup4)Added [kIOMemoryPurgeableVolatileGroup5](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup5)Added [kIOMemoryPurgeableVolatileGroup6](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup6)Added [kIOMemoryPurgeableVolatileGroup7](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatilegroup7)Added [kIOMemoryPurgeableVolatileOrderingNormal](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatileorderingnormal)Added [kIOMemoryPurgeableVolatileOrderingObsolete](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablevolatileorderingobsolete)IONDRVLibraries.hRemoved [AbsoluteDeltaToDuration()](https://developer.apple.com/documentation/coreservices/1501245-absolutedeltatoduration)Removed [AbsoluteToDuration()](https://developer.apple.com/documentation/coreservices/1501266-absolutetoduration)Removed [AbsoluteToNanoseconds()](https://developer.apple.com/documentation/coreservices/1501246-absolutetonanoseconds)Removed [AddAbsoluteToAbsolute()](https://developer.apple.com/documentation/coreservices/1501267-addabsolutetoabsolute)Removed [AddDurationToAbsolute()](https://developer.apple.com/documentation/coreservices/1501249-adddurationtoabsolute)Removed BlockCopy()Removed BlockMove()Removed BlockMoveData()Removed BlockMoveDataUncached()Removed BlockMoveUncached()Removed BlockZero()Removed BlockZeroUncached()Removed CStrCat()Removed CStrCmp()Removed CStrCopy()Removed CStrLen()Removed CStrNCat()Removed CStrNCmp()Removed CStrNCopy()Removed CStrToPStr()Removed [CompareAndSwap()](https://developer.apple.com/documentation/coreservices/1490575-compareandswap)Removed CreateInterruptSet()Removed CurrentExecutionLevel()Removed DelayFor()Removed DelayForHardware()Removed DelayUntil()Removed DeleteInterruptSet()Removed [DurationToAbsolute()](https://developer.apple.com/documentation/coreservices/1501247-durationtoabsolute)Removed EndianSwap16Bit()Removed EndianSwap32Bit()Removed ExpMgrConfigReadByte()Removed ExpMgrConfigReadLong()Removed ExpMgrConfigReadWord()Removed ExpMgrConfigWriteByte()Removed ExpMgrConfigWriteLong()Removed ExpMgrConfigWriteWord()Removed ExpMgrIOReadByte()Removed ExpMgrIOReadLong()Removed ExpMgrIOReadWord()Removed ExpMgrIOWriteByte()Removed ExpMgrIOWriteLong()Removed ExpMgrIOWriteWord()Removed GetInterruptFunctions()Removed IOCommandIsComplete()Removed ISTPropertyRemoved InstallInterruptFunctions()Removed InterruptDisablerRemoved InterruptEnablerRemoved InterruptHandlerRemoved InterruptMemberNumberRemoved InterruptReturnValueRemoved InterruptSetIDRemoved InterruptSetMemberRemoved InterruptSetOptionsRemoved InterruptSourceStateRemoved [Nanoseconds](https://developer.apple.com/documentation/coreservices/nanoseconds)Removed [NanosecondsToAbsolute()](https://developer.apple.com/documentation/coreservices/1501255-nanosecondstoabsolute)Removed PStrCopy()Removed PStrToCStr()Removed PoolAllocateResident()Removed PoolDeallocate()Removed RegistryCStrEntryCreate()Removed RegistryCStrEntryToPath()Removed RegistryEntryCopy()Removed RegistryEntryDelete()Removed RegistryEntryGetMod()Removed RegistryEntryIterateSet()Removed RegistryEntryMod()Removed RegistryEntryPropertyMod()Removed RegistryEntrySearch()Removed RegistryEntrySetMod()Removed RegistryEntryToPathSize()Removed RegistryPropertyRename()Removed [SubAbsoluteFromAbsolute()](https://developer.apple.com/documentation/coreservices/1501265-subabsolutefromabsolute)Removed SynchronizeIO()Removed SysDebug()Removed SysDebugStr()Removed [UpTime()](https://developer.apple.com/documentation/coreservices/1501237-uptime)Removed VSLSetDisplayConfiguration()Removed VSLWaitOnInterruptService()Removed kFirstMemberNumberRemoved kISTChipInterruptSourceRemoved kISTInputDMAInterruptSourceRemoved kISTOutputDMAInterruptSourceRemoved kISTPropertyMemberCountRemoved #def kISTPropertyNameRemoved kIsrIsCompleteRemoved kIsrIsNotCompleteRemoved kMemberNumberParentRemoved kReturnToParentWhenCompleteRemoved kReturnToParentWhenNotCompleteRemoved kSourceWasDisabledRemoved kSourceWasEnabledIONDRVSupport.hRemoved IONDRVInstallInterruptFunctions()Removed IONDRVInterruptDisablerRemoved IONDRVInterruptEnablerRemoved IONDRVInterruptHandlerRemoved IONDRVInterruptSetMemberRemoved IONDRVUndefinedSymbolHandlerRemoved kIONDRVFirstMemberNumberRemoved kIONDRVISTChipInterruptSourceRemoved kIONDRVISTInputDMAInterruptSourceRemoved kIONDRVISTOutputDMAInterruptSourceRemoved kIONDRVISTPropertyMemberCountRemoved #def kIONDRVISTPropertyNameRemoved kIONDRVIsrIsCompleteRemoved kIONDRVIsrIsNotCompleteRemoved kIONDRVMemberNumberParentRemoved kIONDRVReturnToParentWhenCompleteRemoved kIONDRVReturnToParentWhenNotCompleteIONVRAM.hAdded IODTNVRAM::initNVRAMImage()Added IODTNVRAM::initProxyData()IONetworkController.hAdded [kIONetworkFeatureTransmitCompletionStatus](https://developer.apple.com/documentation/iokit/1551508-network/kionetworkfeaturetransmitcompletionstatus)IONetworkInterface.hAdded IONetworkInterface::notifyDriver()Added [#def kIONetworkNoBSDAttachKey](https://developer.apple.com/documentation/kernel/kionetworknobsdattachkey)IONetworkMedium.hAdded [kIONetworkLinkNoNetworkChange](https://developer.apple.com/documentation/kernel/1645760-anonymous/kionetworklinknonetworkchange)IOPCIBridge.hAdded IOPCIBridge::callPlatformFunction()Added IOPCIBridge::deferredProbe()Added IOPCIBridge::initialPowerStateForDomainState()Added IOPCIBridge::maxCapabilityForDomainState()Added IOPCIBridge::powerStateForDomainState()Added IOPCIBridge::relocate()Added IOPCIBridge::setProperties()Added IOPCIBridge::updateWakeReason()Added [IOPCIMessagedInterruptController](https://developer.apple.com/documentation/kernel/iopcimessagedinterruptcontroller)Modified IOPCIBridge::restoreMachineState()

|  | Declaration |
| --- | --- |
| From | IOReturn restoreMachineState ( IOOptionBits options); |
| To | IOReturn restoreMachineState ( IOOptionBits options, IOPCIDevice \*device); |

Modified IOPCIBridge::setDevicePowerState()

|  | Declaration |
| --- | --- |
| From | virtual IOReturn setDevicePowerState ( IOPCIDevice \*device, unsigned long whatToDo); |
| To | IOReturn setDevicePowerState ( IOPCIDevice \*device, IOOptionBits options, unsigned long prevState, unsigned long newState); |

Modified IOPCIBridge::spaceFromProperties()

|  | Declaration |
| --- | --- |
| From | virtual void spaceFromProperties ( OSDictionary \*propTable, IOPCIAddressSpace \*space); |
| To | void spaceFromProperties ( IORegistryEntry \*regEntry, IOPCIAddressSpace \*space); |

IOPCIDevice.hAdded IOPCIDevice::initialPowerStateForDomainState()Added IOPCIDevice::maxCapabilityForDomainState()Added IOPCIDevice::powerStateForDomainState()Added IOPCIDevice::relocate()Added IOPCIDevice::setLatencyTolerance()Added IOPCIDevice::setPCIPowerState()Added [kIOPCIDevicePausedState](https://developer.apple.com/documentation/kernel/1640322-anonymous/kiopcidevicepausedstate)Added #def kIOPCIExpressCapabilitiesKeyAdded #def kIOPCIExpressSlotCapabilitiesKeyAdded #def kIOPCIExpressSlotStatusKeyAdded [kIOPCILatencySnooped](https://developer.apple.com/documentation/kernel/1640337-anonymous/kiopcilatencysnooped)Added [kIOPCILatencyUnsnooped](https://developer.apple.com/documentation/kernel/1640337-anonymous/kiopcilatencyunsnooped)Added #def kIOPCIPauseCompatibleKeyIOPM.hAdded #def kIOPMBootSessionUUIDKeyAdded [kIOPMDriverAssertionNetworkKeepAliveActiveBit](https://developer.apple.com/documentation/kernel/1645008-anonymous/kiopmdriverassertionnetworkkeepaliveactivebit)Added #def kIOPMDriverAssertionRegistryEntryIDKeyAdded #def kIOPMResetPowerStateOnWakeKeyAdded [kIOPMRootDomainState](https://developer.apple.com/documentation/kernel/1645009-anonymous/kiopmrootdomainstate)IOPMLibDefs.hAdded #def kPMSetDisplayPowerOnAdded #def kPMSleepWakeDebugTrigAdded #def kPMSleepWakeWatchdogEnableIOPMpowerState.hAdded [kIOPMPowerStateVersion2](https://developer.apple.com/documentation/kernel/1646617-anonymous/kiopmpowerstateversion2)IOPlatformExpert.hAdded [PERemoveNVRAMProperty()](https://developer.apple.com/documentation/kernel/1451580-peremovenvramproperty)IOReportTypes.hAdded [IOHistogramReportValues](https://developer.apple.com/documentation/kernel/iohistogramreportvalues)Added #def IOREPORT_MAKEIDAdded [IOReportCategories](https://developer.apple.com/documentation/kernel/ioreportcategories)Added [IOReportChannel](https://developer.apple.com/documentation/kernel/ioreportchannel)Added [IOReportChannelList](https://developer.apple.com/documentation/kernel/ioreportchannellist)Added [IOReportChannelType](https://developer.apple.com/documentation/kernel/ioreportchanneltype)Added [IOReportConfigureAction](https://developer.apple.com/documentation/kernel/ioreportconfigureaction)Added [IOReportElement](https://developer.apple.com/documentation/kernel/ioreportelement)Added [IOReportElementValues](https://developer.apple.com/documentation/kernel/ioreportelementvalues)Added [IOReportFormat](https://developer.apple.com/documentation/kernel/ioreportformat)Added [IOReportInterest](https://developer.apple.com/documentation/kernel/ioreportinterest)Added [IOReportInterestList](https://developer.apple.com/documentation/kernel/ioreportinterestlist)Added [IOReportUpdateAction](https://developer.apple.com/documentation/kernel/ioreportupdateaction)Added [IOSimpleReportValues](https://developer.apple.com/documentation/kernel/iosimplereportvalues)Added [IOStateReportValues](https://developer.apple.com/documentation/kernel/iostatereportvalues)Added #def kIOReportCategoryDebugAdded #def kIOReportCategoryPerformanceAdded #def kIOReportCategoryPeripheralAdded #def kIOReportCategoryPowerAdded #def kIOReportCategoryTrafficAdded [kIOReportCopyChannelData](https://developer.apple.com/documentation/kernel/1645975-anonymous/kioreportcopychanneldata)Added [kIOReportDisable](https://developer.apple.com/documentation/kernel/1645974-anonymous/kioreportdisable)Added [kIOReportEnable](https://developer.apple.com/documentation/kernel/1645974-anonymous/kioreportenable)Added [kIOReportFormatHistogram](https://developer.apple.com/documentation/kernel/1645976-anonymous/kioreportformathistogram)Added [kIOReportFormatSimple](https://developer.apple.com/documentation/kernel/1645976-anonymous/kioreportformatsimple)Added [kIOReportFormatState](https://developer.apple.com/documentation/kernel/1645976-anonymous/kioreportformatstate)Added [kIOReportGetDimensions](https://developer.apple.com/documentation/kernel/1645974-anonymous/kioreportgetdimensions)Added #def kIOReportInvalidCategoryAdded [kIOReportInvalidFormat](https://developer.apple.com/documentation/kernel/1645976-anonymous/kioreportinvalidformat)Added #def kIOReportInvalidIntValueAdded [#def kIOReportInvalidValue](https://developer.apple.com/documentation/kernel/kioreportinvalidvalue)Added [kIOReportNotifyHubOnChange](https://developer.apple.com/documentation/kernel/1645974-anonymous/kioreportnotifyhubonchange)Added [kIOReportTraceChannelData](https://developer.apple.com/documentation/kernel/1645975-anonymous/kioreporttracechanneldata)Added [kIOReportTraceOnChange](https://developer.apple.com/documentation/kernel/1645974-anonymous/kioreporttraceonchange)IOReturn.hAdded #def sub_iokit_audio_videoAdded #def sub_iokit_hidsystemAdded #def sub_iokit_hsicAdded #def sub_iokit_sdioAdded #def sub_iokit_wlanIOSCSIBlockCommandsDevice.hRemoved IOSCSIBlockCommandsDevice::CreateCommandSetObjects()Removed IOSCSIBlockCommandsDevice::ERASE_10()Removed IOSCSIBlockCommandsDevice::ERASE_12()Removed IOSCSIBlockCommandsDevice::FORMAT_UNIT()Removed IOSCSIBlockCommandsDevice::FreeCommandSetObjects()Removed IOSCSIBlockCommandsDevice::GetSCSIBlockCommandObject()Removed IOSCSIBlockCommandsDevice::GetSCSIPrimaryCommandObject()Removed IOSCSIBlockCommandsDevice::LOCK_UNLOCK_CACHE()Removed IOSCSIBlockCommandsDevice::LOCK_UNLOCK_CACHE_16()Removed IOSCSIBlockCommandsDevice::MEDIUM_SCAN()Removed IOSCSIBlockCommandsDevice::PREFETCH()Removed IOSCSIBlockCommandsDevice::PREFETCH_16()Removed IOSCSIBlockCommandsDevice::READ_6()Removed IOSCSIBlockCommandsDevice::READ_DEFECT_DATA_10()Removed IOSCSIBlockCommandsDevice::READ_DEFECT_DATA_12()Removed IOSCSIBlockCommandsDevice::READ_GENERATION()Removed IOSCSIBlockCommandsDevice::READ_LONG()Removed IOSCSIBlockCommandsDevice::READ_LONG_16()Removed IOSCSIBlockCommandsDevice::READ_UPDATED_BLOCK_10()Removed IOSCSIBlockCommandsDevice::REASSIGN_BLOCKS()Removed IOSCSIBlockCommandsDevice::REBUILD()Removed IOSCSIBlockCommandsDevice::REGENERATE()Removed IOSCSIBlockCommandsDevice::REZERO_UNIT()Removed IOSCSIBlockCommandsDevice::SEARCH_DATA_EQUAL_10()Removed IOSCSIBlockCommandsDevice::SEARCH_DATA_HIGH_10()Removed IOSCSIBlockCommandsDevice::SEARCH_DATA_LOW_10()Removed IOSCSIBlockCommandsDevice::SEEK_10()Removed IOSCSIBlockCommandsDevice::SEEK_6()Removed IOSCSIBlockCommandsDevice::SET_LIMITS_10()Removed IOSCSIBlockCommandsDevice::SET_LIMITS_12()Removed IOSCSIBlockCommandsDevice::UPDATE_BLOCK()Removed IOSCSIBlockCommandsDevice::VERIFY_10()Removed IOSCSIBlockCommandsDevice::VERIFY_12()Removed IOSCSIBlockCommandsDevice::VERIFY_16()Removed IOSCSIBlockCommandsDevice::WRITE_6()Removed IOSCSIBlockCommandsDevice::WRITE_AND_VERIFY_10()Removed IOSCSIBlockCommandsDevice::WRITE_AND_VERIFY_12()Removed IOSCSIBlockCommandsDevice::WRITE_AND_VERIFY_16()Removed IOSCSIBlockCommandsDevice::WRITE_LONG()Removed IOSCSIBlockCommandsDevice::WRITE_LONG_16()Removed IOSCSIBlockCommandsDevice::WRITE_SAME()Removed IOSCSIBlockCommandsDevice::WRITE_SAME_16()Removed IOSCSIBlockCommandsDevice::XDREAD()Removed IOSCSIBlockCommandsDevice::XDWRITE()Removed IOSCSIBlockCommandsDevice::XDWRITEREAD_10()Removed IOSCSIBlockCommandsDevice::XDWRITE_EXTENDED()Removed IOSCSIBlockCommandsDevice::XPWRITE()IOSCSIMultimediaCommandsDevice.hRemoved IOSCSIMultimediaCommandsDevice::AudioPause()Removed IOSCSIMultimediaCommandsDevice::AudioPlay()Removed IOSCSIMultimediaCommandsDevice::AudioScan()Removed IOSCSIMultimediaCommandsDevice::AudioStop()Removed IOSCSIMultimediaCommandsDevice::BLANK()Removed IOSCSIMultimediaCommandsDevice::CLOSE_TRACK_SESSION()Removed IOSCSIMultimediaCommandsDevice::CreateCommandSetObjects()Removed IOSCSIMultimediaCommandsDevice::FORMAT_UNIT()Removed IOSCSIMultimediaCommandsDevice::FreeCommandSetObjects()Removed IOSCSIMultimediaCommandsDevice::GetAudioStatus()Removed IOSCSIMultimediaCommandsDevice::GetAudioVolume()Removed IOSCSIMultimediaCommandsDevice::GetSCSIBlockCommandObject()Removed IOSCSIMultimediaCommandsDevice::GetSCSIMultimediaCommandObject()Removed IOSCSIMultimediaCommandsDevice::GetSCSIPrimaryCommandObject()Removed IOSCSIMultimediaCommandsDevice::PAUSE_RESUME()Removed IOSCSIMultimediaCommandsDevice::PLAY_AUDIO_10()Removed IOSCSIMultimediaCommandsDevice::PLAY_AUDIO_12()Removed IOSCSIMultimediaCommandsDevice::PLAY_AUDIO_MSF()Removed IOSCSIMultimediaCommandsDevice::PLAY_CD()Removed IOSCSIMultimediaCommandsDevice::READ_BUFFER_CAPACITY()Removed IOSCSIMultimediaCommandsDevice::READ_HEADER()Removed IOSCSIMultimediaCommandsDevice::READ_MASTER_CUE()Removed IOSCSIMultimediaCommandsDevice::REPAIR_TRACK()Removed IOSCSIMultimediaCommandsDevice::REPORT_KEY()Removed IOSCSIMultimediaCommandsDevice::RESERVE_TRACK()Removed IOSCSIMultimediaCommandsDevice::SCAN()Removed IOSCSIMultimediaCommandsDevice::SEND_CUE_SHEET()Removed IOSCSIMultimediaCommandsDevice::SEND_DVD_STRUCTURE()Removed IOSCSIMultimediaCommandsDevice::SEND_EVENT()Removed IOSCSIMultimediaCommandsDevice::SEND_KEY()Removed IOSCSIMultimediaCommandsDevice::SEND_OPC_INFORMATION()Removed IOSCSIMultimediaCommandsDevice::STOP_PLAY_SCAN()Removed IOSCSIMultimediaCommandsDevice::SetAudioVolume()Added #def fDoNotLockMediaIOSCSIPrimaryCommandsDevice.hRemoved IOSCSIPrimaryCommandsDevice::CHANGE_DEFINITION()Removed IOSCSIPrimaryCommandsDevice::COMPARE()Removed IOSCSIPrimaryCommandsDevice::COPY()Removed IOSCSIPrimaryCommandsDevice::COPY_AND_VERIFY()Removed IOSCSIPrimaryCommandsDevice::CreateCommandSetObjects()Removed IOSCSIPrimaryCommandsDevice::EXTENDED_COPY()Removed IOSCSIPrimaryCommandsDevice::FreeCommandSetObjects()Removed IOSCSIPrimaryCommandsDevice::GetSCSIPrimaryCommandObject()IOSCSIProtocolInterface.hAdded [#def kIOPropertyDoNotPreventMediumRemovalKey](https://developer.apple.com/documentation/kernel/kiopropertydonotpreventmediumremovalkey)IOSCSIReducedBlockCommandsDevice.hRemoved IOSCSIReducedBlockCommandsDevice::CreateCommandSetObjects()Removed IOSCSIReducedBlockCommandsDevice::FreeCommandSetObjects()Removed IOSCSIReducedBlockCommandsDevice::GetSCSIPrimaryCommandObject()Removed IOSCSIReducedBlockCommandsDevice::GetSCSIReducedBlockCommandObject()IOService.hAdded IOService::configureReport()Added IOService::updateReport()IOStorageProtocolCharacteristics.hAdded [#def kIOPropertyPhysicalInterconnectTypePCI](https://developer.apple.com/documentation/kernel/kiopropertyphysicalinterconnecttypepci)IOUSBController.hRemoved IOUSBController::GetInternalHubErrataBits()Added IOUSBController::CheckACPIForPortMapping()Added IOUSBController::IsPortMapped()Added ErrataList64EntryAdded ErrataList64EntryPtrAdded kErrataXHCIEnableAutoComplianceAdded kErrataXHCINoMSIAdded kErrataXHCIPPTMuxingAdded kErrataXHCIPantherPointAdded kErrataXHCIParkRingAdded kErrataXHCISWAssistXHCIIdleAdded kErrataXHCISWBandwidthCheckAdded kErratakUHCIResetAfterBabbleAdded kUSBWatchdogTimeoutMSDuringRestartOffIOUSBControllerV2.hAdded IOUSBControllerV2::UpdateDeviceAddress()Added IOUSBControllerV2::UpdateTopology()IOUSBControllerV3.hRemoved IOUSBControllerV3::GetErrataBits()Added IOUSBControllerV3::CanControllerMuxOverToEHCI()Added IOUSBControllerV3::GetConnectorType()Added IOUSBControllerV3::GetErrata64Bits()Added IOUSBControllerV3::GetInternalHubErrataBits()Added IOUSBControllerV3::GetMinimumIdlePowerState()Added IOUSBControllerV3::PMEHandler()Added #def kACPIInterruptTypeValidAdded #def kGPEACPIStringAdded kMaxEHCIPortsAdded kMaxXHCIPortsModified IOUSBControllerV3::RHCompleteTransaction()

|  | Declaration |
| --- | --- |
| From | void RHCompleteTransaction ( IOUSBRootHubInterruptTransactionPtr outstandingRHTransPtr); |
| To | void RHCompleteTransaction ( IOUSBRootHubInterruptTransactionPtr outstandingRHTransPtr, UInt16 rhStatusChangedBitmap, UInt16 numPorts, bool cancelTimer); |

IOUSBDevice.hRemoved IOUSBDevice::DisplayUserNotificationForDeviceEntry()Added IOUSBDevice::GetDeviceClass()Added IOUSBDevice::GetDeviceSubClass()Added IOUSBDevice::GetLocationID()Modified IOUSBDevice::DisplayUserNotificationForDevice()

|  | Declaration |
| --- | --- |
| From | void DisplayUserNotificationForDevice ( void); |
| To | void DisplayUserNotificationForDevice ( UInt32 notificationType, UInt8 port); |

IOUSBHIDDriver.hRemoved #def kHIDDriverRetryCountAdded #def kHIDStandardDriverRetryCountAdded #def kHIDStandardRetryCountInMSIOUSBHubPolicyMaker.hAdded IOUSBHubPolicyMaker::ProcessUSBNotification()Added IOUSBHubPolicyMaker::stop()IOUSBInterface.hAdded IOUSBInterface::EnableRemoteWake()Added IOUSBInterface::GetInterfaceStatus()Added IOUSBInterface::SetFunctionSuspendFeature()IOUSBUserClient.hAdded [IOUSBNotification](https://developer.apple.com/documentation/kernel/iousbnotification)Added IOUSBNotification::GetAsyncRefPtr()Added IOUSBNotification::GetIOUSBDevice()Added IOUSBNotification::GetIOUSBInterface()Added IOUSBNotification::GetIOUserClient()Added IOUSBNotification::GetNotificationMask()Added IOUSBNotification::SendNotification()Added IOUSBNotification::SetAsyncRef()Added IOUSBNotification::SetIOUSBDevice()Added IOUSBNotification::SetIOUSBInterface()Added IOUSBNotification::SetNotificationMask()Added IOUSBNotification::getMetaClass()Added IOUSBNotification::withUserClient()Added [kUSBDeviceUserClientAcknowledgeNotification](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientacknowledgenotification)Added [kUSBDeviceUserClientRegisterForNotification](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientregisterfornotification)Added [kUSBDeviceUserClientSetConfigurationV2](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientsetconfigurationv2)Added [kUSBDeviceUserClientUnregisterNotification](https://developer.apple.com/documentation/kernel/1646283-anonymous/kusbdeviceuserclientunregisternotification)Added [kUSBInterfaceUserClientAcknowledgeNotification](https://developer.apple.com/documentation/iokit/1575934-anonymous/kusbinterfaceuserclientacknowledgenotification)Added [kUSBInterfaceUserClientRegisterForNotification](https://developer.apple.com/documentation/kernel/1646287-anonymous/kusbinterfaceuserclientregisterfornotification)Added [kUSBInterfaceUserClientUnregisterNotification](https://developer.apple.com/documentation/kernel/1646287-anonymous/kusbinterfaceuserclientunregisternotification)Added [kUSBProcessNotificationAcknowledgeNotification](https://developer.apple.com/documentation/kernel/1646286-anonymous/kusbprocessnotificationacknowledgenotification)Added [kUSBProcessNotificationRegisterNotification](https://developer.apple.com/documentation/kernel/1646286-anonymous/kusbprocessnotificationregisternotification)Added [kUSBProcessNotificationUnregisterNotification](https://developer.apple.com/documentation/kernel/1646286-anonymous/kusbprocessnotificationunregisternotification)IOUserClient.hAdded IOUserClient::sendAsyncResult64WithOptions()Added [kIOUserNotifyOptionCanDrop](https://developer.apple.com/documentation/kernel/1646104-anonymous/kiousernotifyoptioncandrop)MacIOATA.hOSByteOrder.hRemoved #def OS_INLINEOSTypes.hRemoved wideAdded #def ABSOLUTETIME_SCALAR_TYPEModified [OptionBits](https://developer.apple.com/documentation/kernel/optionbits)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [UnsignedWide](https://developer.apple.com/documentation/kernel/unsignedwide)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

OSvKernDSPLib.hAdded [IIRChannel](https://developer.apple.com/documentation/kernel/iirchannel)Added [expf()](https://developer.apple.com/documentation/kernel/1532210-expf)Added [log10f()](https://developer.apple.com/documentation/kernel/1532188-log10f)Added [logf()](https://developer.apple.com/documentation/kernel/1532186-logf)Added [sqrtf()](https://developer.apple.com/documentation/kernel/1532170-sqrtf)Added [vA128Shift()](https://developer.apple.com/documentation/accelerate/1442963-va128shift)Added [vDSP_IIRMonoLeft](https://developer.apple.com/documentation/kernel/1645949-anonymous/vdsp_iirmonoleft)Added [vDSP_IIRMonoRight](https://developer.apple.com/documentation/kernel/1645949-anonymous/vdsp_iirmonoright)Added [vDSP_IIRStereo](https://developer.apple.com/documentation/kernel/1645949-anonymous/vdsp_iirstereo)Added [vDSP_biquad2()](https://developer.apple.com/documentation/kernel/1532195-vdsp_biquad2)Added [vDSP_biquad2_CopyState()](https://developer.apple.com/documentation/kernel/1532220-vdsp_biquad2_copystate)Added [vDSP_biquad2_CreateSetup()](https://developer.apple.com/documentation/kernel/1532224-vdsp_biquad2_createsetup)Added [vDSP_biquad2_DestroySetup()](https://developer.apple.com/documentation/kernel/1532201-vdsp_biquad2_destroysetup)Added [vDSP_biquad2_ResetState()](https://developer.apple.com/documentation/kernel/1532215-vdsp_biquad2_resetstate)Added [vDSP_biquad_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquad_setup)Added [vDSP_int24](https://developer.apple.com/documentation/accelerate/vdsp_int24)Added [vDSP_uint24](https://developer.apple.com/documentation/accelerate/vdsp_uint24)Added [vDSP_vfix16()](https://developer.apple.com/documentation/accelerate/1449992-vdsp_vfix16)Added [vDSP_vfix32()](https://developer.apple.com/documentation/accelerate/1449976-vdsp_vfix32)Added [vDSP_vflt16()](https://developer.apple.com/documentation/accelerate/1450096-vdsp_vflt16)Added [vDSP_vflt24()](https://developer.apple.com/documentation/accelerate/1450529-vdsp_vflt24)Added [vDSP_vflt32()](https://developer.apple.com/documentation/kernel/1532181-vdsp_vflt32)Added [vDSP_vfltu24()](https://developer.apple.com/documentation/accelerate/1450084-vdsp_vfltu24)Added [vDSP_vsmfix24()](https://developer.apple.com/documentation/accelerate/1449670-vdsp_vsmfix24)Added [vDSP_vsmfixu24()](https://developer.apple.com/documentation/kernel/1532178-vdsp_vsmfixu24)Added [vLL128Shift()](https://developer.apple.com/documentation/kernel/1411104-vll128shift)Added [vLR128Shift()](https://developer.apple.com/documentation/kernel/1411111-vlr128shift)Added [vS128Add()](https://developer.apple.com/documentation/accelerate/1442956-vs128add)Added [vS128AddS()](https://developer.apple.com/documentation/accelerate/1442977-vs128adds)Added [vS128Sub()](https://developer.apple.com/documentation/kernel/1411118-vs128sub)Added [vS128SubS()](https://developer.apple.com/documentation/accelerate/1442914-vs128subs)Added [vS64FullMulOdd()](https://developer.apple.com/documentation/kernel/1411122-vs64fullmulodd)Added [vSInt32](https://developer.apple.com/documentation/kernel/vsint32)Added [vU128Add()](https://developer.apple.com/documentation/kernel/1411106-vu128add)Added [vU128AddS()](https://developer.apple.com/documentation/kernel/1411102-vu128adds)Added [vU128Sub()](https://developer.apple.com/documentation/accelerate/1442884-vu128sub)Added [vU128SubS()](https://developer.apple.com/documentation/accelerate/1442931-vu128subs)Added [vU64FullMulOdd()](https://developer.apple.com/documentation/kernel/1411109-vu64fullmulodd)Added [vUInt32](https://developer.apple.com/documentation/kernel/vuint32)Added [vUInt8](https://developer.apple.com/documentation/kernel/vuint8)Added [vvexpf()](https://developer.apple.com/documentation/kernel/1532176-vvexpf)RootDomain.hAdded IOPMrootDomain::configureReport()Added IOPMrootDomain::copyProperty()Added IOPMrootDomain::updateReport()USB.hAdded #def ISROOTHUBAdded [USBNotificationTypes](https://developer.apple.com/documentation/kernel/usbnotificationtypes)Added #def kEHCIIsochMaxBusStallAdded [#def kIOUSBMessageUnsupportedConfiguration](https://developer.apple.com/documentation/iokit/kiousbmessageunsupportedconfiguration)Added [#def kIOUSBTooManyTransactionsPending](https://developer.apple.com/documentation/iokit/kiousbtoomanytransactionspending)Added [kIOUSBVendorIDApple](https://developer.apple.com/documentation/kernel/1646381-anonymous/kiousbvendoridapple)Added #def kOHCIIsochMaxBusStallAdded #def kThunderboltMaxBusStallAdded #def kUHCIIsochMaxBusStallAdded [kUSBNotEnoughPowerNoACNotificationType](https://developer.apple.com/documentation/kernel/1646362-anonymous/kusbnotenoughpowernoacnotificationtype)Added [kUSBNotificationPostForcedResume](https://developer.apple.com/documentation/kernel/usbnotificationtypes/kusbnotificationpostforcedresume)Added [kUSBNotificationPostForcedResumeBit](https://developer.apple.com/documentation/kernel/1646390-anonymous/kusbnotificationpostforcedresumebit)Added [kUSBNotificationPostForcedSuspend](https://developer.apple.com/documentation/kernel/usbnotificationtypes/kusbnotificationpostforcedsuspend)Added [kUSBNotificationPostForcedSuspendBit](https://developer.apple.com/documentation/iokit/1425635-anonymous/kusbnotificationpostforcedsuspendbit)Added [kUSBNotificationPreForcedResume](https://developer.apple.com/documentation/kernel/usbnotificationtypes/kusbnotificationpreforcedresume)Added [kUSBNotificationPreForcedResumeBit](https://developer.apple.com/documentation/iokit/1425635-anonymous/kusbnotificationpreforcedresumebit)Added [kUSBNotificationPreForcedSuspend](https://developer.apple.com/documentation/iokit/usbnotificationtypes/kusbnotificationpreforcedsuspend)Added [kUSBNotificationPreForcedSuspendBit](https://developer.apple.com/documentation/iokit/1425635-anonymous/kusbnotificationpreforcedsuspendbit)Added [kUSBUnsupportedNotificationType](https://developer.apple.com/documentation/iokit/1426344-anonymous/kusbunsupportednotificationtype)Added [kUSBiOSDeviceNotEnoughPowerNotificationType](https://developer.apple.com/documentation/kernel/1646362-anonymous/kusbiosdevicenotenoughpowernotificationtype)Added #def kXHCIIsochMaxBusStallUSBHub.hAdded [kUSBHubOvercurrentMask](https://developer.apple.com/documentation/kernel/1643680-anonymous/kusbhubovercurrentmask)Added [kUSBHubOvercurrentShift](https://developer.apple.com/documentation/kernel/1643680-anonymous/kusbhubovercurrentshift)USBSpec.hAdded [kUSBFunctionRemoteWakeCapableBit](https://developer.apple.com/documentation/iokit/1424754-miscellaneous/kusbfunctionremotewakecapablebit)Added [kUSBFunctionRemoteWakeEnableBit](https://developer.apple.com/documentation/iokit/1424754-miscellaneous/kusbfunctionremotewakeenablebit)Added [kUSBFunctionRemoteWakeupBit](https://developer.apple.com/documentation/kernel/1643523-anonymous/kusbfunctionremotewakeupbit)Added [kUSBLowPowerSuspendStateBit](https://developer.apple.com/documentation/iokit/1424754-miscellaneous/kusblowpowersuspendstatebit)WKdm_new.hAdded #def ALL_ONES_MASKAdded #def BITS_PER_BYTEAdded #def BITS_PER_WORDAdded #def BYTES_PER_WORDAdded #def DEBUG_PRINT_1Added #def DEBUG_PRINT_2Added #def DICTIONARY_SIZEAdded DictionaryElementAdded #def EMIT_BYTEAdded #def EMIT_WORDAdded #def EXACT_TAGAdded #def FOUR_BITS_PACKING_MASKAdded #def FULL_WORD_AREA_STARTAdded #def HASH_LOOKUP_TABLE_CONTENTSAdded #def HASH_TO_DICT_BYTE_OFFSETAdded #def HEADER_SIZE_IN_WORDSAdded #def HIGH_BITSAdded #def LOW_BITSAdded #def LOW_BITS_AREA_ENDAdded #def LOW_BITS_AREA_STARTAdded #def LOW_BITS_MASKAdded #def MISS_TAGAdded #def NUM_LOW_BITSAdded #def PAGE_SIZE_IN_BYTESAdded #def PAGE_SIZE_IN_WORDSAdded #def PARTIAL_TAGAdded #def PRELOAD_DICTIONARYAdded #def QPOS_AREA_ENDAdded #def QPOS_AREA_STARTAdded #def RECORD_EXACTAdded #def RECORD_MISSAdded #def RECORD_PARTIALAdded #def RECORD_ZEROAdded #def SET_LOW_BITS_AREA_ENDAdded #def SET_LOW_BITS_AREA_STARTAdded #def SET_QPOS_AREA_STARTAdded #def TAGS_AREA_ENDAdded #def TAGS_AREA_OFFSETAdded #def TAGS_AREA_SIZEAdded #def TAGS_AREA_STARTAdded #def TEN_LOW_BITS_MASKAdded #def TWENTY_TWO_HIGH_BITS_MASKAdded #def TWO_BITS_PACKING_MASKAdded [WK_word](https://developer.apple.com/documentation/kernel/wk_word)Added #def WKdm_SCRATCH_BUF_SIZEAdded [WKdm_compress_new()](https://developer.apple.com/documentation/kernel/1473458-wkdm_compress_new)Added [WKdm_decompress_new()](https://developer.apple.com/documentation/kernel/1473454-wkdm_decompress_new)Added #def ZERO_TAGAdded hashLookupTable___offsetof.h_blkcnt_t.hModified [blkcnt_t](https://developer.apple.com/documentation/kernel/blkcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_blkcnt_t.h |

_blksize_t.hModified [blksize_t](https://developer.apple.com/documentation/kernel/blksize_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_blksize_t.h |

_clock_t.hModified [clock_t](https://developer.apple.com/documentation/kernel/clock_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_clock_t.h |

_ct_rune_t.hAdded [ct_rune_t](https://developer.apple.com/documentation/kernel/ct_rune_t)_dev_t.hModified [dev_t](https://developer.apple.com/documentation/kernel/dev_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_dev_t.h |

_errno_t.hModified [errno_t](https://developer.apple.com/documentation/kernel/errno_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_errno_t.h |

_fd_clr.hModified #def FD_CLR

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_clr.h |

_fd_copy.hModified #def FD_COPY

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_copy.h |

_fd_def.hModified [fd_set](https://developer.apple.com/documentation/kernel/fd_set)

|  | Header |
| --- | --- |
| From | Kernel/sys/_structs.h |
| To | Kernel/sys/_types/_fd_def.h |

_fd_isset.hModified #def FD_ISSET

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_isset.h |

_fd_set.hModified #def FD_SET

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_set.h |

_fd_setsize.hModified #def FD_SETSIZE

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_setsize.h |

_fd_zero.hModified #def FD_ZERO

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_zero.h |

_filesec_t.hAdded [filesec_t](https://developer.apple.com/documentation/kernel/filesec_t)_fsblkcnt_t.hModified [fsblkcnt_t](https://developer.apple.com/documentation/kernel/fsblkcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fsblkcnt_t.h |

_fsfilcnt_t.hModified [fsfilcnt_t](https://developer.apple.com/documentation/kernel/fsfilcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fsfilcnt_t.h |

_gid_t.hAdded [gid_t](https://developer.apple.com/documentation/kernel/gid_t)_guid_t.hModified #def KAUTH_GUID_SIZE

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_guid_t.h |

Modified [guid_t](https://developer.apple.com/documentation/kernel/guid_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_guid_t.h |

_id_t.hAdded [id_t](https://developer.apple.com/documentation/kernel/id_t)_in_addr_t.hAdded [in_addr_t](https://developer.apple.com/documentation/kernel/in_addr_t)_in_port_t.hAdded [in_port_t](https://developer.apple.com/documentation/kernel/in_port_t)_ino64_t.hModified [ino64_t](https://developer.apple.com/documentation/kernel/ino64_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_ino64_t.h |

_ino_t.hModified [ino_t](https://developer.apple.com/documentation/kernel/ino_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_ino_t.h |

_int16_t.hModified [int16_t](https://developer.apple.com/documentation/kernel/int16_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int16_t.h |

_int32_t.hModified [int32_t](https://developer.apple.com/documentation/kernel/int32_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int32_t.h |

_int64_t.hModified [int64_t](https://developer.apple.com/documentation/kernel/int64_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int64_t.h |

_int8_t.hModified [int8_t](https://developer.apple.com/documentation/kernel/int8_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int8_t.h |

_intptr_t.hModified [intptr_t](https://developer.apple.com/documentation/kernel/intptr_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_intptr_t.h |

_iovec_t.hAdded [iovec](https://developer.apple.com/documentation/kernel/iovec)_key_t.hAdded [key_t](https://developer.apple.com/documentation/kernel/key_t)_mach_port_t.h_mbstate_t.hAdded [mbstate_t](https://developer.apple.com/documentation/kernel/mbstate_t)_mcontext.h_mcontext.hModified #def I386_MCONTEXT_SIZE

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext32](https://developer.apple.com/documentation/kernel/mcontext32)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext64](https://developer.apple.com/documentation/kernel/mcontext64)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_avx32](https://developer.apple.com/documentation/kernel/mcontext_avx32)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_avx64](https://developer.apple.com/documentation/kernel/mcontext_avx64)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_t](https://developer.apple.com/documentation/kernel/mcontext_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

_mode_t.hAdded [mode_t](https://developer.apple.com/documentation/kernel/mode_t)_nlink_t.hModified [nlink_t](https://developer.apple.com/documentation/kernel/nlink_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_nlink_t.h |

_null.hAdded #def NULL_o_dsync.hModified #def O_DSYNC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_o_dsync.h |

_o_sync.hModified #def O_SYNC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_o_sync.h |

_off_t.hAdded [off_t](https://developer.apple.com/documentation/kernel/off_t)_os_inline.hAdded #def OS_INLINE_pid_t.hAdded [pid_t](https://developer.apple.com/documentation/kernel/pid_t)_posix_vdisable.h_pthread_attr_t.hModified pthread_attr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_attr_t.h |

_pthread_cond_t.hModified pthread_cond_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_cond_t.h |

_pthread_condattr_t.hModified pthread_condattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_condattr_t.h |

_pthread_key_t.hModified pthread_key_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_key_t.h |

_pthread_mutex_t.hModified pthread_mutex_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_mutex_t.h |

_pthread_mutexattr_t.hModified pthread_mutexattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_mutexattr_t.h |

_pthread_once_t.hModified pthread_once_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_once_t.h |

_pthread_rwlock_t.hModified pthread_rwlock_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_rwlock_t.h |

_pthread_rwlockattr_t.hModified pthread_rwlockattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_rwlockattr_t.h |

_pthread_t.hModified pthread_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_t.h |

_ptrdiff_t.hAdded [ptrdiff_t](https://developer.apple.com/documentation/kernel/ptrdiff_t)_rsize_t.hAdded [rsize_t](https://developer.apple.com/documentation/kernel/rsize_t)_rune_t.hAdded [rune_t](https://developer.apple.com/documentation/kernel/rune_t)_s_ifmt.hModified #def S_IEXEC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFBLK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFCHR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFDIR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFIFO

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFLNK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFMT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFREG

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFSOCK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFWHT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IREAD

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IROTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXG

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXO

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXU

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISGID

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISTXT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISUID

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISVTX

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWOTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWRITE

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXOTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

_sa_family_t.hAdded [sa_family_t](https://developer.apple.com/documentation/kernel/sa_family_t)_seek_set.hAdded #def SEEK_CURAdded #def SEEK_ENDAdded #def SEEK_SET_sigaltstack.hAdded [stack_t](https://developer.apple.com/documentation/kernel/stack_t)_sigset_t.hAdded [sigset_t](https://developer.apple.com/documentation/kernel/sigset_t)_size_t.hAdded [size_t](https://developer.apple.com/documentation/kernel/size_t)_socklen_t.hModified [socklen_t](https://developer.apple.com/documentation/kernel/socklen_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/socket.h |
| To | Kernel/sys/_types/_socklen_t.h |

_ssize_t.hAdded [ssize_t](https://developer.apple.com/documentation/kernel/ssize_t)_structs.hModified #def I386_MCONTEXT_SIZE

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext32](https://developer.apple.com/documentation/kernel/mcontext32)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext64](https://developer.apple.com/documentation/kernel/mcontext64)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_avx32](https://developer.apple.com/documentation/kernel/mcontext_avx32)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_avx64](https://developer.apple.com/documentation/kernel/mcontext_avx64)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

Modified [mcontext_t](https://developer.apple.com/documentation/kernel/mcontext_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/_structs.h |
| To | Kernel/i386/_mcontext.h |

_structs.hModified [fd_set](https://developer.apple.com/documentation/kernel/fd_set)

|  | Header |
| --- | --- |
| From | Kernel/sys/_structs.h |
| To | Kernel/sys/_types/_fd_def.h |

_suseconds_t.hModified [suseconds_t](https://developer.apple.com/documentation/kernel/suseconds_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_suseconds_t.h |

_time_t.hAdded [time_t](https://developer.apple.com/documentation/kernel/time_t)_timespec.hAdded [timespec](https://developer.apple.com/documentation/kernel/timespec)_timeval.hAdded [timeval](https://developer.apple.com/documentation/kernel/timeval)_timeval32.hAdded [timeval32](https://developer.apple.com/documentation/kernel/timeval32)_ucontext.hAdded [ucontext_t](https://developer.apple.com/documentation/kernel/ucontext_t)_ucontext64.h_uid_t.hAdded [uid_t](https://developer.apple.com/documentation/kernel/uid_t)_uintptr_t.hModified [uintptr_t](https://developer.apple.com/documentation/kernel/uintptr_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_uintptr_t.h |

_useconds_t.hModified [useconds_t](https://developer.apple.com/documentation/kernel/useconds_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_useconds_t.h |

_user32_itimerval.hAdded [user32_itimerval](https://developer.apple.com/documentation/kernel/user32_itimerval)_user32_timespec.hAdded [user32_timespec](https://developer.apple.com/documentation/kernel/user32_timespec)_user32_timeval.hAdded [user32_timeval](https://developer.apple.com/documentation/kernel/user32_timeval)_user64_itimerval.hAdded [user64_itimerval](https://developer.apple.com/documentation/kernel/user64_itimerval)_user64_timespec.hAdded [user64_timespec](https://developer.apple.com/documentation/kernel/user64_timespec)_user64_timeval.hAdded [user64_timeval](https://developer.apple.com/documentation/kernel/user64_timeval)_user_timespec.hAdded [user_timespec](https://developer.apple.com/documentation/kernel/user_timespec)_user_timeval.hAdded [user_timeval](https://developer.apple.com/documentation/kernel/user_timeval)_uuid_t.hModified [uuid_t](https://developer.apple.com/documentation/kernel/uuid_t)

|  | Header |
| --- | --- |
| From | Kernel/uuid/uuid.h |
| To | Kernel/sys/_types/_uuid_t.h |

_va_list.hAdded [va_list](https://developer.apple.com/documentation/kernel/va_list)_wchar_t.h_wint_t.hAdded [wint_t](https://developer.apple.com/documentation/kernel/wint_t)boot.hAdded #def kBootArgsFlagBlackbpf.hAdded #def BIOCSETFNRAdded #def DLT_A429Added #def DLT_A653_ICMAdded #def DLT_AIRONET_HEADERAdded #def DLT_AOSAdded #def DLT_ARCNET_LINUXAdded #def DLT_AURORAAdded #def DLT_AX25_KISSAdded #def DLT_BACNET_MS_TPAdded #def DLT_BLUETOOTH_HCI_H4Added #def DLT_BLUETOOTH_HCI_H4_WITH_PHDRAdded #def DLT_CAN20BAdded #def DLT_CAN_SOCKETCANAdded #def DLT_CISCO_IOSAdded #def DLT_C_HDLC_WITH_DIRAdded #def DLT_DBUSAdded #def DLT_DECTAdded #def DLT_DOCSISAdded #def DLT_DVB_CIAdded #def DLT_ECONETAdded #def DLT_ENCAdded #def DLT_ERFAdded #def DLT_ERF_ETHAdded #def DLT_ERF_POSAdded #def DLT_FC_2Added #def DLT_FC_2_WITH_FRAME_DELIMSAdded #def DLT_FLEXRAYAdded #def DLT_FRELAYAdded #def DLT_FRELAY_WITH_DIRAdded #def DLT_GCOM_SERIALAdded #def DLT_GCOM_T1E1Added #def DLT_GPF_FAdded #def DLT_GPF_TAdded #def DLT_GPRS_LLCAdded #def DLT_GSMTAP_ABISAdded #def DLT_GSMTAP_UMAdded #def DLT_HHDLCAdded #def DLT_IBM_SNAdded #def DLT_IBM_SPAdded #def DLT_IEEE802_15_4Added #def DLT_IEEE802_15_4_LINUXAdded #def DLT_IEEE802_15_4_NOFCSAdded #def DLT_IEEE802_15_4_NONASK_PHYAdded #def DLT_IEEE802_16_MAC_CPSAdded #def DLT_IEEE802_16_MAC_CPS_RADIOAdded #def DLT_IPFILTERAdded #def DLT_IPMBAdded #def DLT_IPMB_LINUXAdded #def DLT_IPNETAdded #def DLT_IPOIBAdded #def DLT_IPV4Added #def DLT_IPV6Added #def DLT_IP_OVER_FCAdded #def DLT_JUNIPER_ATM1Added #def DLT_JUNIPER_ATM2Added #def DLT_JUNIPER_ATM_CEMICAdded #def DLT_JUNIPER_CHDLCAdded #def DLT_JUNIPER_ESAdded #def DLT_JUNIPER_ETHERAdded #def DLT_JUNIPER_FIBRECHANNELAdded #def DLT_JUNIPER_FRELAYAdded #def DLT_JUNIPER_GGSNAdded #def DLT_JUNIPER_ISMAdded #def DLT_JUNIPER_MFRAdded #def DLT_JUNIPER_MLFRAdded #def DLT_JUNIPER_MLPPPAdded #def DLT_JUNIPER_MONITORAdded #def DLT_JUNIPER_PIC_PEERAdded #def DLT_JUNIPER_PPPAdded #def DLT_JUNIPER_PPPOEAdded #def DLT_JUNIPER_PPPOE_ATMAdded #def DLT_JUNIPER_SERVICESAdded #def DLT_JUNIPER_SRX_E2EAdded #def DLT_JUNIPER_STAdded #def DLT_JUNIPER_VPAdded #def DLT_JUNIPER_VSAdded #def DLT_LAPB_WITH_DIRAdded #def DLT_LAPDAdded #def DLT_LINAdded #def DLT_LINUX_EVDEVAdded #def DLT_LINUX_IRDAAdded #def DLT_LINUX_LAPDAdded #def DLT_LINUX_PPP_WITHDIRECTIONAdded #def DLT_LTALKAdded #def DLT_MATCHING_MAXAdded #def DLT_MATCHING_MINAdded #def DLT_MFRAdded #def DLT_MOSTAdded #def DLT_MPEG_2_TSAdded #def DLT_MPLSAdded #def DLT_MTP2Added #def DLT_MTP2_WITH_PHDRAdded #def DLT_MTP3Added #def DLT_MUX27010Added #def DLT_NETANALYZERAdded #def DLT_NETANALYZER_TRANSPARENTAdded #def DLT_NFC_LLCPAdded #def DLT_NFLOGAdded #def DLT_NG40Added #def DLT_PCI_EXPAdded #def DLT_PPIAdded #def DLT_PPP_ETHERAdded #def DLT_PPP_PPPDAdded #def DLT_PPP_WITH_DIRAdded #def DLT_PPP_WITH_DIRECTIONAdded #def DLT_PRISM_HEADERAdded #def DLT_RAIF1Added #def DLT_RIOAdded #def DLT_SCCPAdded #def DLT_SITAAdded #def DLT_STANAG_5066_D_PDUAdded #def DLT_SUNATMAdded #def DLT_SYMANTEC_FIREWALLAdded #def DLT_TZSPAdded #def DLT_USBAdded #def DLT_USB_LINUXAdded #def DLT_USB_LINUX_MMAPPEDAdded #def DLT_USER0Added #def DLT_USER1Added #def DLT_USER10Added #def DLT_USER11Added #def DLT_USER12Added #def DLT_USER13Added #def DLT_USER14Added #def DLT_USER15Added #def DLT_USER2Added #def DLT_USER3Added #def DLT_USER4Added #def DLT_USER5Added #def DLT_USER6Added #def DLT_USER7Added #def DLT_USER8Added #def DLT_USER9Added #def DLT_WIHARTAdded #def DLT_X2E_SERIALAdded #def DLT_X2E_XORAYAcall_entry.hclock.hAdded [clock_get_calendar_absolute_and_microtime()](https://developer.apple.com/documentation/kernel/1416697-clock_get_calendar_absolute_and_)conf.hRemoved #def D_TRACKCLOSERemoved #def D_TYPEMASKcpuid.hRemoved #def CPUID_FEATURE_xAPICRemoved cpuid_get_info()Added #def CPUID_FEATURE_FMAAdded #def CPUID_FEATURE_x2APICAdded #def CPUID_LEAF7_FEATURE_AVX2Added #def CPUID_LEAF7_FEATURE_BMI1Added #def CPUID_LEAF7_FEATURE_BMI2Added #def CPUID_LEAF7_FEATURE_HLEAdded #def CPUID_LEAF7_FEATURE_INVPCIDAdded #def CPUID_LEAF7_FEATURE_RTMAdded #def CPUID_LEAF7_FEATURE_TSCOFFAdded #def CPUID_MODEL_HASWELLAdded #def CPUID_MODEL_HASWELL_SVRAdded #def CPUID_MODEL_HASWELL_ULTdebug.hAdded [STACKSHOT_GET_BOOT_PROFILE](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_get_boot_profile)Added [STACKSHOT_GET_MICROSTACKSHOT](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_get_microstackshot)Added [STACKSHOT_GLOBAL_MICROSTACKSHOT_DISABLE](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_global_microstackshot_disable)Added [STACKSHOT_GLOBAL_MICROSTACKSHOT_ENABLE](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_global_microstackshot_enable)Added #def STACKSHOT_MICRO_SNAPSHOT_MAGICAdded STACKSHOT_SAVE_KERNEL_FRAMES_ONLYAdded [STACKSHOT_SAVE_KEXT_LOADINFO](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_save_kext_loadinfo)Added [STACKSHOT_SET_MICROSTACKSHOT_MARK](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_set_microstackshot_mark)Added [dyld_uuid_info_32](https://developer.apple.com/documentation/kernel/dyld_uuid_info_32)Added [dyld_uuid_info_64](https://developer.apple.com/documentation/kernel/dyld_uuid_info_64)Added [generic_snapshot_flags](https://developer.apple.com/documentation/kernel/generic_snapshot_flags)Added [kInterruptRecord](https://developer.apple.com/documentation/kernel/micro_snapshot_flags/kinterruptrecord)Added [kStacksPCOnly](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kstackspconly)Added [kTaskDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskdarwinbg)Added [kTaskExtDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskextdarwinbg)Added [kTaskIsBoosted](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisboosted)Added [kTaskIsForeground](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisforeground)Added [kTaskIsSuppressed](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskissuppressed)Added [kTaskIsTimerThrottled](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskistimerthrottled)Added [kTaskRsrcFlagged](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskrsrcflagged)Added [kTaskVisNonvisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisnonvisible)Added [kTaskVisVisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisvisible)Added [kThreadDarwinBG](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreaddarwinbg)Added [kTimerArmingRecord](https://developer.apple.com/documentation/kernel/micro_snapshot_flags/ktimerarmingrecord)Added [kUserMode](https://developer.apple.com/documentation/kernel/micro_snapshot_flags/kusermode)Added [micro_snapshot](https://developer.apple.com/documentation/kernel/micro_snapshot)Added [micro_snapshot_flags](https://developer.apple.com/documentation/kernel/micro_snapshot_flags)Added [stack_snapshot_frame32](https://developer.apple.com/documentation/kernel/stack_snapshot_frame32)Added [stack_snapshot_frame64](https://developer.apple.com/documentation/kernel/stack_snapshot_frame64)Added [task_snapshot_flags](https://developer.apple.com/documentation/kernel/task_snapshot_flags)Added [thread_snapshot_flags](https://developer.apple.com/documentation/kernel/thread_snapshot_flags)disk.hAdded #def DKIOCGETMAXPRIORITYCOUNTev_keymap.hAdded #def NX_MODIFIERKEY_ALPHALOCK_STATELESSAdded #def NX_MODIFIERKEY_LAST_KEYevent.hRemoved #def NOTE_RESOURCEENDAdded #def NOTE_BACKGROUNDAdded #def NOTE_CRITICALAdded #def NOTE_EXIT_CSERRORAdded #def NOTE_EXIT_DECRYPTFAILAdded #def NOTE_EXIT_DETAILAdded #def NOTE_EXIT_DETAIL_MASKAdded #def NOTE_EXIT_MEMORYAdded #def NOTE_LEEWAYAdded [eNoteExitReparentedDeprecated](https://developer.apple.com/documentation/kernel/1639039-anonymous/enoteexitreparenteddeprecated)Added [eNoteReapDeprecated](https://developer.apple.com/documentation/kernel/1639028-anonymous/enotereapdeprecated)exception_types.hAdded #def EXC_GUARDAdded #def EXC_MASK_GUARDfcntl.hRemoved #def F_MARKDEPENDENCYRemoved #def F_READBOOTSTRAPRemoved #def F_WRITEBOOTSTRAPRemoved #def SEEK_CURRemoved #def SEEK_ENDRemoved #def SEEK_SETAdded #def F_FINDSIGSAdded #def F_SETLKWTIMEOUTAdded #def O_CLOFORKAdded [flocktimeout](https://developer.apple.com/documentation/kernel/flocktimeout)Modified #def O_DSYNC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_o_dsync.h |

Modified #def O_SYNC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_o_sync.h |

Modified #def S_IEXEC

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFBLK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFCHR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFDIR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFIFO

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFLNK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFMT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFREG

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFSOCK

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IFWHT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IREAD

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IROTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXG

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXO

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IRWXU

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISGID

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISTXT

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISUID

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_ISVTX

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWOTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWRITE

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IWUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXGRP

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXOTH

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

Modified #def S_IXUSR

|  | Header |
| --- | --- |
| From | Kernel/sys/fcntl.h |
| To | Kernel/sys/_types/_s_ifmt.h |

hfs_format.hRemoved [ConstHFSUniStr255Param](https://developer.apple.com/documentation/kernel/consthfsunistr255param)Removed [HFSUniStr255](https://developer.apple.com/documentation/kernel/hfsunistr255)hfs_unistr.hAdded [ConstHFSUniStr255Param](https://developer.apple.com/documentation/kernel/consthfsunistr255param)Added [HFSUniStr255](https://developer.apple.com/documentation/kernel/hfsunistr255)host_info.hAdded #def HOST_EXPIRED_TASK_INFOAdded #def HOST_VM_INFO64_REV0_COUNTAdded #def HOST_VM_INFO64_REV1_COUNTAdded #def HOST_VM_PURGABLEAdded #def HOST_VM_PURGABLE_COUNTAdded [host_purgable_info_data_t](https://developer.apple.com/documentation/kernel/host_purgable_info_data_t)Added [host_purgable_info_t](https://developer.apple.com/documentation/kernel/host_purgable_info_t)host_special_ports.hAdded #def HOST_TELEMETRY_PORTAdded #def host_get_telemetry_portAdded #def host_set_telemetry_portif.hAdded #def IFCAP_AVAdded #def IFCAP_HWCSUMAdded #def IFCAP_JUMBO_MTUAdded #def IFCAP_LROAdded #def IFCAP_RXCSUMAdded #def IFCAP_TSOAdded #def IFCAP_TSO4Added #def IFCAP_TSO6Added #def IFCAP_TXCSUMAdded #def IFCAP_TXSTATUSAdded #def IFCAP_VALIDAdded #def IFCAP_VLAN_HWTAGGINGAdded #def IFCAP_VLAN_MTUAdded #def IFF_ALLMULTIAdded #def IFF_ALTPHYSAdded #def IFF_BROADCASTAdded #def IFF_DEBUGAdded #def IFF_LINK0Added #def IFF_LINK1Added #def IFF_LINK2Added #def IFF_LOOPBACKAdded #def IFF_MULTICASTAdded #def IFF_NOARPAdded #def IFF_NOTRAILERSAdded #def IFF_OACTIVEAdded #def IFF_POINTOPOINTAdded #def IFF_PROMISCAdded #def IFF_RUNNINGAdded #def IFF_SIMPLEXAdded #def IFF_UPAdded #def IFLR_PREFIXAdded #def IFNET_SLOWHZAdded #def IFQ_MAXLENAdded #def IFSTATMAXAdded #def IF_NAMESIZEAdded #def IF_WAKE_ON_MAGIC_PACKETAdded #def KEV_DL_ADDMULTIAdded #def KEV_DL_DELMULTIAdded #def KEV_DL_IFCAP_CHANGEDAdded #def KEV_DL_IFDELEGATE_CHANGEDAdded #def KEV_DL_IF_ATTACHEDAdded #def KEV_DL_IF_DETACHEDAdded #def KEV_DL_IF_DETACHINGAdded #def KEV_DL_IF_IDLE_ROUTE_REFCNTAdded #def KEV_DL_ISSUESAdded #def KEV_DL_LINK_ADDRESS_CHANGEDAdded #def KEV_DL_LINK_OFFAdded #def KEV_DL_LINK_ONAdded #def KEV_DL_LINK_QUALITY_METRIC_CHANGEDAdded #def KEV_DL_MASTER_ELECTEDAdded #def KEV_DL_NODE_ABSENCEAdded #def KEV_DL_NODE_PRESENCEAdded #def KEV_DL_PROTO_ATTACHEDAdded #def KEV_DL_PROTO_DETACHEDAdded #def KEV_DL_SIFFLAGSAdded #def KEV_DL_SIFGENERICAdded #def KEV_DL_SIFMEDIAAdded #def KEV_DL_SIFMETRICSAdded #def KEV_DL_SIFMTUAdded #def KEV_DL_SIFPHYSAdded #def KEV_DL_SUBCLASSAdded #def KEV_DL_WAKEFLAGS_CHANGEDAdded [if_clonereq](https://developer.apple.com/documentation/kernel/if_clonereq)Added if_laddrreqAdded [if_msghdr](https://developer.apple.com/documentation/kernel/if_msghdr)Added [if_msghdr2](https://developer.apple.com/documentation/kernel/if_msghdr2)Added [ifa_msghdr](https://developer.apple.com/documentation/kernel/ifa_msghdr)Added [ifaliasreq](https://developer.apple.com/documentation/kernel/ifaliasreq)Added [ifdevmtu](https://developer.apple.com/documentation/kernel/ifdevmtu)Added [ifdrv](https://developer.apple.com/documentation/kernel/ifdrv)Added [ifkpi](https://developer.apple.com/documentation/kernel/ifkpi)Added [ifma_msghdr](https://developer.apple.com/documentation/kernel/ifma_msghdr)Added [ifma_msghdr2](https://developer.apple.com/documentation/kernel/ifma_msghdr2)Added #def ifr_addrAdded #def ifr_broadaddrAdded #def ifr_curcapAdded #def ifr_dataAdded #def ifr_devmtuAdded #def ifr_dstaddrAdded #def ifr_flagsAdded #def ifr_intvalAdded #def ifr_kpiAdded #def ifr_mediaAdded #def ifr_metricAdded #def ifr_mtuAdded #def ifr_physAdded #def ifr_reqcapAdded #def ifr_route_refcntAdded #def ifr_wake_flagsAdded [ifreq](https://developer.apple.com/documentation/kernel/ifreq)Added [ifstat](https://developer.apple.com/documentation/kernel/ifstat)Added [kev_dl_proto_data](https://developer.apple.com/documentation/kernel/kev_dl_proto_data)Added [rslvmulti_req](https://developer.apple.com/documentation/kernel/rslvmulti_req)if_arp.hAdded [arpstat](https://developer.apple.com/documentation/kernel/arpstat)if_media.hAdded #def IFM_WAKESAMENETif_types.hAdded #def IFT_PKTAPif_utun.hAdded #def UTUN_CONTROL_NAMEAdded #def UTUN_FLAGS_NO_INPUTAdded #def UTUN_FLAGS_NO_OUTPUTAdded #def UTUN_OPT_EXT_IFDATA_STATSAdded #def UTUN_OPT_FLAGSAdded #def UTUN_OPT_IFNAMEAdded #def UTUN_OPT_INC_IFDATA_STATS_INAdded #def UTUN_OPT_INC_IFDATA_STATS_OUTAdded #def UTUN_OPT_SET_DELEGATE_INTERFACEAdded [utun_stats_param](https://developer.apple.com/documentation/kernel/utun_stats_param)if_utun_crypto.hif_utun_crypto_ipsec.hin.hRemoved [in_addr_t](https://developer.apple.com/documentation/kernel/in_addr_t)Removed [in_port_t](https://developer.apple.com/documentation/kernel/in_port_t)Added [inet_aton()](https://developer.apple.com/documentation/kernel/1475455-inet_aton)Added inet_ntoa()Added inet_ntoa_r()Added inet_pton()ipc.hRemoved [gid_t](https://developer.apple.com/documentation/kernel/gid_t)Removed [key_t](https://developer.apple.com/documentation/kernel/key_t)Removed [mode_t](https://developer.apple.com/documentation/kernel/mode_t)Removed [uid_t](https://developer.apple.com/documentation/kernel/uid_t)ipcomp.hAdded #def IPCOMP_CPI_NEGOTIATE_MINAdded #def IPCOMP_DEFLATEAdded #def IPCOMP_LZSAdded #def IPCOMP_MAXAdded #def IPCOMP_OUIAdded [ipcomp](https://developer.apple.com/documentation/kernel/ipcomp)ipsec.hAdded #def IPSEC_DIR_ANYAdded #def IPSEC_DIR_INBOUNDAdded #def IPSEC_DIR_INVALIDAdded #def IPSEC_DIR_MAXAdded #def IPSEC_DIR_OUTBOUNDAdded #def IPSEC_LEVEL_DEFAULTAdded #def IPSEC_LEVEL_REQUIREAdded #def IPSEC_LEVEL_UNIQUEAdded #def IPSEC_LEVEL_USEAdded #def IPSEC_MANUAL_REQID_MAXAdded #def IPSEC_MODE_ANYAdded #def IPSEC_MODE_TRANSPORTAdded #def IPSEC_MODE_TUNNELAdded #def IPSEC_POLICY_BYPASSAdded #def IPSEC_POLICY_DISCARDAdded #def IPSEC_POLICY_ENTRUSTAdded #def IPSEC_POLICY_GENERATEAdded #def IPSEC_POLICY_IPSECAdded #def IPSEC_POLICY_NONEAdded #def IPSEC_PORT_ANYAdded #def IPSEC_PROTO_ANYAdded #def IPSEC_REPLAYWSIZEAdded #def IPSEC_ULPROTO_ANYAdded [ipsecstat](https://developer.apple.com/documentation/kernel/ipsecstat)kdebug.hRemoved #def MACH_SCHED_LPA_BROKENAdded #def BSD_MEMSTAT_CLEAR_ERRORSAdded #def BSD_MEMSTAT_FREEZEAdded #def BSD_MEMSTAT_IDLE_DEMOTEAdded #def BSD_MEMSTAT_JETSAMAdded #def BSD_MEMSTAT_JETSAM_HIWATAdded #def BSD_MEMSTAT_LATENCY_COALESCEAdded #def BSD_MEMSTAT_SCANAdded #def BSD_MEMSTAT_UPDATEAdded #def DBG_ACFSAdded #def DBG_APP_AUDIOAdded #def DBG_BSD_MEMSTATAdded #def DBG_COMPRESSOR_FAULTAdded #def DBG_COMPRESSOR_SWAPIN_FAULTAdded #def DBG_DRVSPIAdded #def DBG_HFS_UPDATE_ACCTIMEAdded #def DBG_HFS_UPDATE_CHGTIMEAdded #def DBG_HFS_UPDATE_DATEADDEDAdded #def DBG_HFS_UPDATE_FORCEAdded #def DBG_HFS_UPDATE_MODIFIEDAdded #def DBG_HFS_UPDATE_MODTIMEAdded #def DBG_IMPORTANCEAdded #def DBG_IOTHUNDERBOLTAdded #def DBG_MACH_STACKSHOTAdded #def DBG_MACH_VM_PRESSUREAdded #def DBG_THROTTLEAdded #def DKIO_TIER_MASKAdded #def DKIO_TIER_SHIFTAdded #def IMPORTANCE_CODEAdded #def IMP_ASSERTIONAdded #def IMP_BOOSTAdded #def IMP_BOOSTEDAdded #def IMP_DROPAdded #def IMP_EXTERNAdded #def IMP_HOLDAdded #def IMP_MSGAdded #def IMP_MSG_DELVAdded #def IMP_MSG_SENDAdded #def IMP_TASK_APPTYPEAdded #def IMP_TASK_SUPPRESSIONAdded #def IMP_UNBOOSTEDAdded #def IMP_UPDATEAdded #def IMP_UPDATE_TASK_CREATEAdded #def IMP_WATCHPORTAdded #def IO_THROTTLE_DISABLEAdded KD_CALLBACK_KDEBUG_DISABLEDAdded KD_CALLBACK_KDEBUG_ENABLEDAdded KD_CALLBACK_SYNC_FLUSHAdded KD_CALLBACK_TYPEFILTER_CHANGEDAdded #def MACH_CPU_THROTTLE_DISABLEAdded #def MACH_DEEP_IDLEAdded #def MACH_RW_DEMOTEAdded #def MACH_RW_PROMOTEAdded #def MACH_SCHED_CHOOSE_PROCESSORAdded #def MACH_SCHED_DECAY_PRIORITYAdded #def MACH_TASK_RESUMEAdded #def MACH_TASK_SUSPENDAdded #def MICROSTACKSHOT_GATHERAdded #def MICROSTACKSHOT_RECORDAdded #def OPEN_THROTTLE_WINDOWAdded #def PMAP__FLUSH_DELAYED_TLBSAdded #def PMAP__FLUSH_KERN_TLBSAdded #def PMAP__QUERY_RESIDENTAdded #def PMAP__REUSABLEAdded #def PROCESS_THROTTLEDAdded kd_callback_fnAdded kd_callback_tAdded kd_callback_typeAdded kernel_debug_enter()Added kernel_debug_register_callback()kern_event.hAdded #def KEV_ANY_CLASSAdded #def KEV_ANY_SUBCLASSAdded #def KEV_ANY_VENDORAdded [#def KEV_APPLESHARE_CLASS](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2bkbieyrktjbaverk7ingecu2t)Added [#def KEV_FIREWALL_CLASS](https://developer.apple.com/documentation/kernel/kev_firewall_class)Added [#def KEV_IEEE80211_CLASS](https://developer.apple.com/documentation/kernel/kev_ieee80211_class)Added [#def KEV_IOKIT_CLASS](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2jj5fusvc7ingecu2t)Added [#def KEV_MSG_HEADER_SIZE](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2nkndv6scfifcekus7knevuri)Added [#def KEV_NETWORK_CLASS](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2oivkfot2sjnpugtcbknjq)Added #def KEV_RECVSPACEAdded #def KEV_SNDSPACEAdded [#def KEV_SYSTEM_CLASS](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2tlfjvirknl5buyqktkm)Added [#def KEV_VENDOR_APPLE](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2wivheit2sl5avaucmiu)Added [#def KEV_VENDOR_CODE_MAX_STR_LEN](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpjncvmx2wivheit2sl5bu6rcfl5gucwc7knkfex2mivha)Added [#def N_KEV_VECTORS](https://developer.apple.com/documentation/kernel/n_kev_vectors)Added [#def SIOCGKEVFILT](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpkneu6q2hjncvmrsjjrka)Added [#def SIOCGKEVID](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpkneu6q2hjncvmske)Added [#def SIOCGKEVVENDOR](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpkneu6q2hjncvmvsfjzce6uq)Added [#def SIOCSKEVFILT](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3nmfrxe3zpkneu6q2tjncvmrsjjrka)Added #def SYS_KERN_EVENT_HAdded [kern_event_msg](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts623fojxf6zlwmvxhix3nontq)Added [kev_d_vectors](https://developer.apple.com/documentation/kernel/kev_d_vectors)Added [kev_msg](https://developer.apple.com/documentation/kernel/kev_msg)Added [kev_msg_post()](https://developer.apple.com/documentation/kernel/1446953-kev_msg_post)Added [kev_request](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts623fozpxezlrovsxg5a)Added [kev_vendor_code](../../../documentation/Darwin/Miscellaneous%20User%20Space%20API%20Reference/CompositePage-83.md#apple-f4xwc4dqnrsv64tfmyxwgl3umfts623fozpxmzlomrxxex3dn5sgk)Added [kev_vendor_code_find()](https://developer.apple.com/documentation/kernel/1446965-kev_vendor_code_find)kern_memorystatus.hRemoved kMemorystatusFlagsActiveRemoved kMemorystatusFlagsDirtyRemoved kMemorystatusFlagsFrontmostRemoved kMemorystatusFlagsFrozenRemoved kMemorystatusFlagsKilledRemoved kMemorystatusFlagsKilledHiwatRemoved kMemorystatusFlagsKilledSwapRemoved kMemorystatusFlagsKilledVMRemoved kMemorystatusFlagsKilledVnodesRemoved kMemorystatusFlagsSupportsIdleExitRemoved kMemorystatusFlagsSuspForDiagnosisRemoved kMemorystatusFlagsThawedAdded #def DEFERRED_IDLE_EXIT_TIME_SECSAdded #def JETSAM_PRIORITY_AUDIO_AND_ACCESSORYAdded #def JETSAM_PRIORITY_BACKGROUNDAdded #def JETSAM_PRIORITY_BACKGROUND_OPPORTUNISTICAdded #def JETSAM_PRIORITY_CONDUCTORAdded #def JETSAM_PRIORITY_CRITICALAdded #def JETSAM_PRIORITY_DEFAULTAdded #def JETSAM_PRIORITY_EXECUTIVEAdded #def JETSAM_PRIORITY_FOREGROUNDAdded #def JETSAM_PRIORITY_FOREGROUND_SUPPORTAdded #def JETSAM_PRIORITY_HOMEAdded #def JETSAM_PRIORITY_IDLEAdded #def JETSAM_PRIORITY_IDLE_DEFERREDAdded #def JETSAM_PRIORITY_IMPORTANTAdded #def JETSAM_PRIORITY_MAILAdded #def JETSAM_PRIORITY_MAXAdded #def JETSAM_PRIORITY_PHONEAdded #def JETSAM_PRIORITY_REVISIONAdded #def JETSAM_PRIORITY_TELEPHONYAdded #def JETSAM_PRIORITY_UI_SUPPORTAdded #def KEV_MEMORYSTATUS_SUBCLASSAdded #def MEMORYSTATUS_BUFFERSIZE_MAXAdded #def MEMORYSTATUS_CMD_GET_JETSAM_SNAPSHOTAdded #def MEMORYSTATUS_CMD_GET_PRESSURE_STATUSAdded #def MEMORYSTATUS_CMD_GET_PRIORITY_LISTAdded #def MEMORYSTATUS_CMD_SET_JETSAM_HIGH_WATER_MARKAdded #def MEMORYSTATUS_CMD_SET_PRIORITY_PROPERTIESAdded #def kMaxSnapshotEntriesAdded #def kMemorystatusDirtyAdded kMemorystatusFreezeNoteAdded #def kMemorystatusFrozenAdded kMemorystatusKilledAdded kMemorystatusKilledDiagnosticAdded kMemorystatusKilledHiwatAdded kMemorystatusKilledIdleExitAdded kMemorystatusKilledPerProcessLimitAdded kMemorystatusKilledVMAdded kMemorystatusKilledVMPageShortageAdded kMemorystatusKilledVMThrashingAdded kMemorystatusKilledVnodesAdded kMemorystatusLevelAnyAdded kMemorystatusLevelCriticalAdded kMemorystatusLevelNormalAdded kMemorystatusLevelNoteAdded kMemorystatusLevelUrgentAdded kMemorystatusLevelWarningAdded kMemorystatusPressureNoteAdded kMemorystatusSnapshotNoteAdded #def kMemorystatusSupportsIdleExitAdded #def kMemorystatusSuspendedAdded #def kMemorystatusTrackedAdded #def kMemorystatusWasThawedAdded memorystatus_freeze_entry_tAdded memorystatus_jetsam_snapshot_entry_tAdded memorystatus_jetsam_snapshot_tAdded memorystatus_kernel_stats_tAdded memorystatus_priority_entry_tAdded memorystatus_priority_properties_tkern_types.hAdded #def TIMEOUT_URGENCY_FIRST_AVAILAdded #def TIMEOUT_URGENCY_LEEWAYAdded #def TIMEOUT_URGENCY_MASKAdded #def TIMEOUT_URGENCY_SYS_BACKGROUNDAdded #def TIMEOUT_URGENCY_SYS_CRITICALAdded #def TIMEOUT_URGENCY_SYS_NORMALAdded #def TIMEOUT_URGENCY_USER_BACKGROUNDAdded #def TIMEOUT_URGENCY_USER_CRITICALAdded #def TIMEOUT_URGENCY_USER_MASKAdded #def TIMEOUT_URGENCY_USER_NORMALAdded [wait_timeout_urgency_t](https://developer.apple.com/documentation/kernel/wait_timeout_urgency_t)kernel_types.hModified #def KAUTH_GUID_SIZE

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_guid_t.h |

Modified [errno_t](https://developer.apple.com/documentation/kernel/errno_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_errno_t.h |

Modified [guid_t](https://developer.apple.com/documentation/kernel/guid_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/kernel_types.h |
| To | Kernel/sys/_types/_guid_t.h |

kpc.hkpi_interface.hRemoved [sa_family_t](https://developer.apple.com/documentation/kernel/sa_family_t)Added [IFNET_TX_STATUS](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_tx_status)libkern.hRemoved locc()Removed rindex()Added [memchr()](https://developer.apple.com/documentation/kernel/1441105-memchr)Modified [strsep()](https://developer.apple.com/documentation/kernel/1441093-strsep)

|  | Declaration |
| --- | --- |
| From | char \* strsep ( char \*\*stringp, const char \*delim); |
| To | char \* strsep ( char \*\*, const char \*); |

loader.hAdded #def LC_ENCRYPTION_INFO_64Added [encryption_info_command_64](https://developer.apple.com/documentation/kernel/encryption_info_command_64)mach_port.hAdded [mach_port_construct()](https://developer.apple.com/documentation/kernel/1578687-mach_port_construct)Added [mach_port_destruct()](https://developer.apple.com/documentation/kernel/1578881-mach_port_destruct)Added [mach_port_guard()](https://developer.apple.com/documentation/kernel/1578772-mach_port_guard)Added [mach_port_peek()](https://developer.apple.com/documentation/kernel/1578839-mach_port_peek)Added [mach_port_unguard()](https://developer.apple.com/documentation/kernel/1578951-mach_port_unguard)mach_types.hAdded [task_suspension_token_t](https://developer.apple.com/documentation/kernel/task_suspension_token_t)machine.hAdded #def CPUFAMILY_ARM_12Added #def CPUFAMILY_ARM_SWIFTAdded #def CPUFAMILY_INTEL_HASWELLAdded #def CPU_SUBTYPE_ARM_V6MAdded #def CPU_SUBTYPE_ARM_V7EMAdded #def CPU_SUBTYPE_ARM_V7MAdded #def CPU_SUBTYPE_ARM_V7Smachine_kpc.hmachine_kpc.hAdded #def CONFIGURABLE_ACTIONIDAdded #def CONFIGURABLE_RELOADAdded #def CONFIGURABLE_SHADOWAdded #def FIXED_ACTIONIDAdded #def FIXED_RELOADAdded #def FIXED_SHADOWAdded #def KPC_MAX_COUNTERSAdded #def KPC_X86_64_FIXED_CONFIGSAdded [kpc_config_t](https://developer.apple.com/documentation/kernel/kpc_config_t)memory_object_types.hAdded #def MAP_MEM_USE_DATA_ADDRAdded #def MAP_MEM_VM_COPYAdded #def MAP_MEM_VM_SHAREAdded #def UPL_IGNORE_VALID_PAGE_CHECKAdded #def UPL_NOZEROFILLIOAdded #def UPL_REQUEST_NO_FAULTmessage.hAdded #def MACH_MSGH_BITS_IMPHOLDASRTAdded #def MACH_MSGH_BITS_RAISEIMPAdded #def MACH_RCV_LARGE_IDENTITYAdded #def MACH_SEND_IMPORTANCEAdded #def MACH_SEND_NOIMPORTANCEAdded [mach_msg_trailer_info_t](https://developer.apple.com/documentation/kernel/mach_msg_trailer_info_t)mman.hRemoved [mode_t](https://developer.apple.com/documentation/kernel/mode_t)Removed [off_t](https://developer.apple.com/documentation/kernel/off_t)Removed [size_t](https://developer.apple.com/documentation/kernel/size_t)mount.hRemoved #def VQ_FLAG0800Added #def VFS_CTL_SERVERINFOAdded #def VFS_TBLVNOP_NOUPDATEID_RENAMEAdded #def VQ_SERVEREVENTAdded [vfs_server](https://developer.apple.com/documentation/kernel/vfs_server)msg.hRemoved [pid_t](https://developer.apple.com/documentation/kernel/pid_t)Removed [size_t](https://developer.apple.com/documentation/kernel/size_t)Removed [ssize_t](https://developer.apple.com/documentation/kernel/ssize_t)Removed [time_t](https://developer.apple.com/documentation/kernel/time_t)param.hRemoved #def NULLpfkeyv2.hAdded #def SADB_X_EXT_ADDR_RANGE_DST_ENDAdded #def SADB_X_EXT_ADDR_RANGE_DST_STARTAdded #def SADB_X_EXT_ADDR_RANGE_SRC_ENDAdded #def SADB_X_EXT_ADDR_RANGE_SRC_STARTAdded #def SADB_X_EXT_IPSECIFAdded #def SADB_X_SPDDISABLEAdded #def SADB_X_SPDENABLEport.hAdded #def GUARD_TYPE_MACH_PORTAdded #def MACH_PORT_IMPORTANCE_RECEIVERAdded #def MACH_PORT_INFO_EXTAdded #def MACH_PORT_INFO_EXT_COUNTAdded #def MACH_PORT_STATUS_FLAG_GUARDEDAdded #def MACH_PORT_STATUS_FLAG_IMP_DONATIONAdded #def MACH_PORT_STATUS_FLAG_REVIVEAdded #def MACH_PORT_STATUS_FLAG_STRICT_GUARDAdded #def MACH_PORT_STATUS_FLAG_TASKPTRAdded #def MACH_PORT_STATUS_FLAG_TEMPOWNERAdded #def MACH_PORT_TEMPOWNERAdded #def MPO_CONTEXT_AS_GUARDAdded #def MPO_IMPORTANCE_RECEIVERAdded #def MPO_INSERT_SEND_RIGHTAdded #def MPO_QLIMITAdded #def MPO_STRICTAdded #def MPO_TEMPOWNERAdded [kGUARD_EXC_DESTROY](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes/kguard_exc_destroy)Added [kGUARD_EXC_INCORRECT_GUARD](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes/kguard_exc_incorrect_guard)Added [kGUARD_EXC_MOD_REFS](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes/kguard_exc_mod_refs)Added [kGUARD_EXC_SET_CONTEXT](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes/kguard_exc_set_context)Added [kGUARD_EXC_UNGUARDED](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes/kguard_exc_unguarded)Added [mach_port_guard_exception_codes](https://developer.apple.com/documentation/kernel/mach_port_guard_exception_codes)Added [mach_port_info_ext_t](https://developer.apple.com/documentation/kernel/mach_port_info_ext_t)Added [mach_port_options_ptr_t](https://developer.apple.com/documentation/kernel/mach_port_options_ptr_t)Added [mach_port_options_t](https://developer.apple.com/documentation/kernel/mach_port_options_t)proc_reg.hRemoved #def MSR_IA32_ENERGY_PERFORMANCE_BIASRemoved #def MSR_IA32_PACKAGE_ENERY_STATUSRemoved #def MSR_IA32_PACKAGE_POWER_SKU_UNITRemoved #def MSR_IA32_PRIMARY_PLANE_ENERY_STATUSRemoved #def MSR_IA32_SECONDARY_PLANE_ENERY_STATUSRemoved #def MSR_PMG_CST_CONFIG_CONTROLRemoved get_cr3()Removed set_cr3()Added #def MSR_IA32_APERFAdded #def MSR_IA32_CORE_C3_RESIDENCYAdded #def MSR_IA32_CORE_C6_RESIDENCYAdded #def MSR_IA32_CORE_C7_RESIDENCYAdded #def MSR_IA32_DDR_ENERGY_STATUSAdded #def MSR_IA32_GT_PERF_LIMIT_REASONSAdded #def MSR_IA32_IA_PERF_LIMIT_REASONSAdded #def MSR_IA32_LLC_FLUSHED_RESIDENCY_TIMERAdded #def MSR_IA32_MPERFAdded #def MSR_IA32_PERF_FIXED_CTR0Added #def MSR_IA32_PERF_FIXED_CTR_CTRLAdded #def MSR_IA32_PERF_GLOBAL_CTRLAdded #def MSR_IA32_PERF_GLOBAL_OVF_CTRLAdded #def MSR_IA32_PERF_GLOBAL_STATUSAdded #def MSR_IA32_PKG_C10_RESIDENCYAdded #def MSR_IA32_PKG_C2_RESIDENCYAdded #def MSR_IA32_PKG_C3_RESIDENCYAdded #def MSR_IA32_PKG_C6_RESIDENCYAdded #def MSR_IA32_PKG_C7_RESIDENCYAdded #def MSR_IA32_PKG_C8_RESIDENCYAdded #def MSR_IA32_PKG_C9_RESIDENCYAdded #def MSR_IA32_PKG_ENERGY_STATUSAdded #def MSR_IA32_PKG_POWER_SKU_UNITAdded #def MSR_IA32_PP0_ENERGY_STATUSAdded #def MSR_IA32_PP1_ENERGY_STATUSAdded #def MSR_IA32_RING_PERF_STATUSAdded [rdpmc64()](https://developer.apple.com/documentation/kernel/1571261-rdpmc64)Modified [get_cr3_base()](https://developer.apple.com/documentation/kernel/1571286-get_cr3_base)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

Modified [set_cr3_composed()](https://developer.apple.com/documentation/kernel/1571401-set_cr3_composed)

|  | Architectures |
| --- | --- |
| From | x86_64 |
| To | i386,x86_64 |

resource.hAdded #def CPUMON_MAKE_FATALAdded #def IOPOL_APPLICATIONAdded #def IOPOL_IMPORTANTAdded #def IOPOL_SCOPE_DARWIN_BGAdded #def IOPOL_STANDARDAdded #def RLIMIT_CPU_USAGE_MONITORAdded #def RLIMIT_WAKEUPS_MONITORAdded #def RUSAGE_INFO_CURRENTAdded #def RUSAGE_INFO_V0Added #def RUSAGE_INFO_V1Added #def RUSAGE_INFO_V2Added #def WAKEMON_DISABLEAdded #def WAKEMON_ENABLEAdded #def WAKEMON_GET_PARAMSAdded #def WAKEMON_MAKE_FATALAdded #def WAKEMON_SET_DEFAULTSAdded [proc_rlimit_control_wakeupmon](https://developer.apple.com/documentation/kernel/proc_rlimit_control_wakeupmon)Added [rusage_info_child](https://developer.apple.com/documentation/kernel/rusage_info_child)Added rusage_info_diskiobytesAdded [rusage_info_t](https://developer.apple.com/documentation/kernel/rusage_info_t)Added [rusage_info_v0](https://developer.apple.com/documentation/kernel/rusage_info_v0)Added [rusage_info_v1](https://developer.apple.com/documentation/kernel/rusage_info_v1)Added [rusage_info_v2](https://developer.apple.com/documentation/kernel/rusage_info_v2)Added [rusage_superset](https://developer.apple.com/documentation/kernel/rusage_superset)route.hRemoved route_cbAdded #def RTF_BITSAdded #def RTF_NOIFREFsched_prim.hAdded [assert_wait_deadline_with_leeway()](https://developer.apple.com/documentation/kernel/1524380-assert_wait_deadline_with_leeway)Added [assert_wait_timeout_with_leeway()](https://developer.apple.com/documentation/kernel/1524381-assert_wait_timeout_with_leeway)sdt.hAdded #def DTRACE_BOOSTAdded #def DTRACE_BOOST1Added #def DTRACE_BOOST2Added #def DTRACE_BOOST3Added #def DTRACE_BOOST4Added #def DTRACE_BOOST5Added #def DTRACE_BOOST6Added #def DTRACE_FSINFOAdded #def DTRACE_FSINFO_IOAdded #def DTRACE_MPTCPAdded #def DTRACE_MPTCP1Added #def DTRACE_MPTCP2Added #def DTRACE_MPTCP3Added #def DTRACE_MPTCP4Added #def DTRACE_MPTCP5Added #def DTRACE_MPTCP6Added #def DTRACE_MPTCP7select.hRemoved [sigset_t](https://developer.apple.com/documentation/kernel/sigset_t)sem.hRemoved [pid_t](https://developer.apple.com/documentation/kernel/pid_t)Removed [size_t](https://developer.apple.com/documentation/kernel/size_t)Removed [time_t](https://developer.apple.com/documentation/kernel/time_t)shm.hRemoved [pid_t](https://developer.apple.com/documentation/kernel/pid_t)Removed [size_t](https://developer.apple.com/documentation/kernel/size_t)Removed [time_t](https://developer.apple.com/documentation/kernel/time_t)signal.hRemoved [sigset_t](https://developer.apple.com/documentation/kernel/sigset_t)socket.hRemoved #def SO_RESTRICTIONSRemoved #def SO_RESTRICT_DENYINRemoved #def SO_RESTRICT_DENYOUTRemoved #def SO_RESTRICT_DENYSETRemoved [iovec](https://developer.apple.com/documentation/kernel/iovec)Removed [sa_family_t](https://developer.apple.com/documentation/kernel/sa_family_t)Modified [socklen_t](https://developer.apple.com/documentation/kernel/socklen_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/socket.h |
| To | Kernel/sys/_types/_socklen_t.h |

socketvar.hRemoved #def SS_ASYNCRemoved #def SS_CANTRCVMORERemoved #def SS_CANTSENDMORERemoved #def SS_COMPRemoved #def SS_DEFUNCTRemoved #def SS_DRAININGRemoved #def SS_INCOMPRemoved #def SS_ISCONFIRMINGRemoved #def SS_ISCONNECTEDRemoved #def SS_ISCONNECTINGRemoved #def SS_ISDISCONNECTEDRemoved #def SS_ISDISCONNECTINGRemoved #def SS_NBIORemoved #def SS_NOFDREFRemoved #def SS_PRIVRemoved #def SS_RCVATMARKRemoved [so_gen_t](https://developer.apple.com/documentation/kernel/so_gen_t)Removed [xsockbuf](https://developer.apple.com/documentation/kernel/xsockbuf)Removed [xsocket](https://developer.apple.com/documentation/kernel/xsocket)Removed [xsocket64](https://developer.apple.com/documentation/kernel/xsocket64)stdint.hAdded #def INT16_CAdded #def INT32_CAdded #def INT64_CAdded #def INT8_CAdded #def INTMAX_CAdded #def RSIZE_MAXAdded #def SIG_ATOMIC_MAXAdded #def SIG_ATOMIC_MINAdded #def UINT16_CAdded #def UINT32_CAdded #def UINT64_CAdded #def UINT8_CAdded #def UINTMAX_CAdded #def WCHAR_MINAdded #def WINT_MAXAdded #def WINT_MINstring.hAdded [strnstr()](https://developer.apple.com/documentation/kernel/1579346-strnstr)syscall.hRemoved #def SYS_ATPgetreqRemoved #def SYS_ATPgetrspRemoved #def SYS_ATPsndreqRemoved #def SYS_ATPsndrspRemoved #def SYS_ATgetmsgRemoved #def SYS_ATputmsgRemoved #def SYS_ATsocketRemoved #def SYS_pid_hibernateRemoved #def SYS_pid_shutdown_socketsAdded #def SYS_change_fdguard_npAdded #def SYS_connectxAdded #def SYS_disconnectxAdded #def SYS_guarded_close_npAdded #def SYS_guarded_kqueue_npAdded #def SYS_guarded_open_npAdded #def SYS_memorystatus_controlAdded #def SYS_memorystatus_get_levelAdded #def SYS_peeloffAdded #def SYS_proc_rlimit_controlAdded #def SYS_proc_uuid_policyAdded #def SYS_socket_delegateAdded #def SYS_system_overrideAdded #def SYS_telemetryAdded #def SYS_vfs_purgesystm.hRemoved throttle_legacy_process_decr()Removed throttle_legacy_process_incr()task.hAdded [task_suspension_token_deallocate()](https://developer.apple.com/documentation/kernel/1574411-task_suspension_token_deallocate)task.hAdded [task_purgable_info()](https://developer.apple.com/documentation/kernel/1538155-task_purgable_info)Added [task_resume2()](https://developer.apple.com/documentation/kernel/1537653-task_resume2)Added [task_set_phys_footprint_limit()](https://developer.apple.com/documentation/kernel/1538131-task_set_phys_footprint_limit)Added [task_suspend2()](https://developer.apple.com/documentation/kernel/1538207-task_suspend2)task_info.hAdded #def TASK_POWER_INFOAdded #def TASK_POWER_INFO_COUNTAdded #def TASK_VM_INFOAdded #def TASK_VM_INFO_COUNTAdded #def TASK_VM_INFO_PURGEABLEAdded [task_power_info_data_t](https://developer.apple.com/documentation/kernel/task_power_info_data_t)Added [task_power_info_t](https://developer.apple.com/documentation/kernel/task_power_info_t)Added [task_purgable_info_t](https://developer.apple.com/documentation/kernel/task_purgable_info_t)Added [task_vm_info_data_t](https://developer.apple.com/documentation/kernel/task_vm_info_data_t)Added [task_vm_info_t](https://developer.apple.com/documentation/kernel/task_vm_info_t)task_policy.hAdded #def LATENCY_QOS_LAUNCH_DEFAULT_TIERAdded [LATENCY_QOS_TIER_0](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_0)Added [LATENCY_QOS_TIER_1](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_1)Added [LATENCY_QOS_TIER_2](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_2)Added [LATENCY_QOS_TIER_3](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_3)Added [LATENCY_QOS_TIER_4](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_4)Added [LATENCY_QOS_TIER_5](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_5)Added [LATENCY_QOS_TIER_UNSPECIFIED](https://developer.apple.com/documentation/kernel/task_latency_qos/latency_qos_tier_unspecified)Added #def PROC_FLAG_ADAPTIVEAdded #def PROC_FLAG_ADAPTIVE_IMPORTANTAdded #def PROC_FLAG_DARWINBGAdded #def PROC_FLAG_EXT_DARWINBGAdded #def PROC_FLAG_IMPORTANCE_DONORAdded #def PROC_FLAG_IOS_APPLEDAEMONAdded #def PROC_FLAG_IOS_APPLICATIONAdded #def PROC_FLAG_IOS_IMPPROMOTIONAdded #def PROC_FLAG_SUPPRESSEDAdded #def TASK_BASE_QOS_POLICYAdded #def TASK_OVERRIDE_QOS_POLICYAdded #def TASK_POLICY_STATEAdded #def TASK_QOS_POLICY_COUNTAdded #def TASK_SUPPRESSION_POLICYAdded #def THROUGHPUT_QOS_LAUNCH_DEFAULT_TIERAdded [THROUGHPUT_QOS_TIER_0](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_0)Added [THROUGHPUT_QOS_TIER_1](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_1)Added [THROUGHPUT_QOS_TIER_2](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_2)Added [THROUGHPUT_QOS_TIER_3](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_3)Added [THROUGHPUT_QOS_TIER_4](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_4)Added [THROUGHPUT_QOS_TIER_5](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_5)Added [THROUGHPUT_QOS_TIER_UNSPECIFIED](https://developer.apple.com/documentation/kernel/task_throughput_qos/throughput_qos_tier_unspecified)Added [task_latency_qos](https://developer.apple.com/documentation/kernel/task_latency_qos)Added [task_latency_qos_t](https://developer.apple.com/documentation/kernel/task_latency_qos_t)Added [task_qos_policy_t](https://developer.apple.com/documentation/kernel/task_qos_policy_t)Added [task_role](https://developer.apple.com/documentation/kernel/task_role)Added [task_throughput_qos](https://developer.apple.com/documentation/kernel/task_throughput_qos)Added [task_throughput_qos_t](https://developer.apple.com/documentation/kernel/task_throughput_qos_t)tcp.hRemoved #def TCP_MINMSSOVERLOADAdded #def TCP_KEEPCNTAdded #def TCP_KEEPINTVLAdded #def TCP_SENDMOREACKStelemetry.hAdded #def TELEMETRY_CMD_TIMER_EVENTAdded bootprofile_gather()Added bootprofile_init()Added compute_telemetry()Added telemetry_ast()Added telemetry_gather()Added telemetry_global_ctl()Added telemetry_init()Added telemetry_mark_curthread()Added telemetry_needs_recordAdded telemetry_task_ctl()Added telemetry_task_ctl_locked()Added telemetry_timer_event()telemetry_notification_server.hAdded #def subsystem_to_name_map_telemetry_notificationAdded [telemetry_notification()](https://developer.apple.com/documentation/kernel/1543673-telemetry_notification)Added #def telemetry_notification_MSG_COUNTAdded [telemetry_notification_server()](https://developer.apple.com/documentation/kernel/1543703-telemetry_notification_server)Added [telemetry_notification_server_routine()](https://developer.apple.com/documentation/kernel/1543688-telemetry_notification_server_ro)Added [telemetry_notification_subsystem](https://developer.apple.com/documentation/kernel/telemetry_notification_subsystem-3gl)Added [telemetry_notification_subsystem](https://developer.apple.com/documentation/kernel/telemetry_notification_subsystem)thread_status.hAdded #def THREAD_STATE_FLAVOR_LIST_10_9thread_status.hRemoved x86_seg_load_fault32Added #def x86_AVX_STATEAdded #def x86_AVX_STATE_COUNTAdded [x86_avx_state_t](https://developer.apple.com/documentation/kernel/x86_avx_state_t)time.hAdded [microtime_with_abstime()](https://developer.apple.com/documentation/kernel/1391782-microtime_with_abstime)timer_call.htypes.hRemoved [gid_t](https://developer.apple.com/documentation/kernel/gid_t)Removed [id_t](https://developer.apple.com/documentation/kernel/id_t)Removed [in_addr_t](https://developer.apple.com/documentation/kernel/in_addr_t)Removed [in_port_t](https://developer.apple.com/documentation/kernel/in_port_t)Removed [key_t](https://developer.apple.com/documentation/kernel/key_t)Removed [mode_t](https://developer.apple.com/documentation/kernel/mode_t)Removed [off_t](https://developer.apple.com/documentation/kernel/off_t)Removed [pid_t](https://developer.apple.com/documentation/kernel/pid_t)Removed [size_t](https://developer.apple.com/documentation/kernel/size_t)Removed [ssize_t](https://developer.apple.com/documentation/kernel/ssize_t)Removed [time_t](https://developer.apple.com/documentation/kernel/time_t)Removed [uid_t](https://developer.apple.com/documentation/kernel/uid_t)Modified #def FD_CLR

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_clr.h |

Modified #def FD_COPY

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_copy.h |

Modified #def FD_ISSET

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_isset.h |

Modified #def FD_SET

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_set.h |

Modified #def FD_SETSIZE

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_setsize.h |

Modified #def FD_ZERO

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fd_zero.h |

Modified [blkcnt_t](https://developer.apple.com/documentation/kernel/blkcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_blkcnt_t.h |

Modified [blksize_t](https://developer.apple.com/documentation/kernel/blksize_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_blksize_t.h |

Modified [clock_t](https://developer.apple.com/documentation/kernel/clock_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_clock_t.h |

Modified [dev_t](https://developer.apple.com/documentation/kernel/dev_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_dev_t.h |

Modified [fsblkcnt_t](https://developer.apple.com/documentation/kernel/fsblkcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fsblkcnt_t.h |

Modified [fsfilcnt_t](https://developer.apple.com/documentation/kernel/fsfilcnt_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_fsfilcnt_t.h |

Modified [ino64_t](https://developer.apple.com/documentation/kernel/ino64_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_ino64_t.h |

Modified [ino_t](https://developer.apple.com/documentation/kernel/ino_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_ino_t.h |

Modified [nlink_t](https://developer.apple.com/documentation/kernel/nlink_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_nlink_t.h |

Modified pthread_attr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_attr_t.h |

Modified pthread_cond_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_cond_t.h |

Modified pthread_condattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_condattr_t.h |

Modified pthread_key_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_key_t.h |

Modified pthread_mutex_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_mutex_t.h |

Modified pthread_mutexattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_mutexattr_t.h |

Modified pthread_once_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_once_t.h |

Modified pthread_rwlock_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_rwlock_t.h |

Modified pthread_rwlockattr_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_rwlockattr_t.h |

Modified pthread_t

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_pthread_t.h |

Modified [suseconds_t](https://developer.apple.com/documentation/kernel/suseconds_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_suseconds_t.h |

Modified [useconds_t](https://developer.apple.com/documentation/kernel/useconds_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/types.h |
| To | Kernel/sys/_types/_useconds_t.h |

types.hModified [int16_t](https://developer.apple.com/documentation/kernel/int16_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int16_t.h |

Modified [int32_t](https://developer.apple.com/documentation/kernel/int32_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int32_t.h |

Modified [int64_t](https://developer.apple.com/documentation/kernel/int64_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int64_t.h |

Modified [int8_t](https://developer.apple.com/documentation/kernel/int8_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_int8_t.h |

Modified [intptr_t](https://developer.apple.com/documentation/kernel/intptr_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_intptr_t.h |

Modified [uintptr_t](https://developer.apple.com/documentation/kernel/uintptr_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_uintptr_t.h |

ubc.hAdded #def UBC_INVALIDATEAdded #def UBC_PUSHALLAdded #def UBC_PUSHDIRTYAdded #def UBC_SYNCAdded [advisory_read()](https://developer.apple.com/documentation/kernel/1463716-advisory_read)Added [advisory_read_ext()](https://developer.apple.com/documentation/kernel/1463707-advisory_read_ext)Added [cluster_bp()](https://developer.apple.com/documentation/kernel/1463769-cluster_bp)Added [cluster_bp_ext()](https://developer.apple.com/documentation/kernel/1463742-cluster_bp_ext)Added [cluster_copy_ubc_data()](https://developer.apple.com/documentation/kernel/1463730-cluster_copy_ubc_data)Added [cluster_copy_upl_data()](https://developer.apple.com/documentation/kernel/1463719-cluster_copy_upl_data)Added [cluster_pagein()](https://developer.apple.com/documentation/kernel/1463765-cluster_pagein)Added [cluster_pagein_ext()](https://developer.apple.com/documentation/kernel/1463709-cluster_pagein_ext)Added [cluster_pageout()](https://developer.apple.com/documentation/kernel/1463710-cluster_pageout)Added [cluster_pageout_ext()](https://developer.apple.com/documentation/kernel/1463750-cluster_pageout_ext)Added [cluster_push()](https://developer.apple.com/documentation/kernel/1463738-cluster_push)Added [cluster_push_ext()](https://developer.apple.com/documentation/kernel/1463714-cluster_push_ext)Added [cluster_read()](https://developer.apple.com/documentation/kernel/1463724-cluster_read)Added [cluster_read_ext()](https://developer.apple.com/documentation/kernel/1463712-cluster_read_ext)Added [cluster_write()](https://developer.apple.com/documentation/kernel/1463767-cluster_write)Added [cluster_write_ext()](https://developer.apple.com/documentation/kernel/1463756-cluster_write_ext)Added [cluster_zero()](https://developer.apple.com/documentation/kernel/1463752-cluster_zero)Added [is_file_clean()](https://developer.apple.com/documentation/kernel/1463775-is_file_clean)Added [ubc_blktooff()](https://developer.apple.com/documentation/kernel/1463720-ubc_blktooff)Added [ubc_create_upl()](https://developer.apple.com/documentation/kernel/1463758-ubc_create_upl)Added [ubc_getcred()](https://developer.apple.com/documentation/kernel/1463771-ubc_getcred)Added [ubc_getsize()](https://developer.apple.com/documentation/kernel/1463713-ubc_getsize)Added [ubc_msync()](https://developer.apple.com/documentation/kernel/1463717-ubc_msync)Added [ubc_offtoblk()](https://developer.apple.com/documentation/kernel/1463760-ubc_offtoblk)Added [ubc_page_op()](https://developer.apple.com/documentation/kernel/1463700-ubc_page_op)Added [ubc_pages_resident()](https://developer.apple.com/documentation/kernel/1463777-ubc_pages_resident)Added [ubc_range_op()](https://developer.apple.com/documentation/kernel/1463728-ubc_range_op)Added [ubc_setsize()](https://developer.apple.com/documentation/kernel/1463764-ubc_setsize)Added [ubc_setthreadcred()](https://developer.apple.com/documentation/kernel/1463732-ubc_setthreadcred)Added ubc_sync_range()Added [ubc_upl_abort()](https://developer.apple.com/documentation/kernel/1463754-ubc_upl_abort)Added [ubc_upl_abort_range()](https://developer.apple.com/documentation/kernel/1463762-ubc_upl_abort_range)Added [ubc_upl_commit()](https://developer.apple.com/documentation/kernel/1463702-ubc_upl_commit)Added [ubc_upl_commit_range()](https://developer.apple.com/documentation/kernel/1463734-ubc_upl_commit_range)Added [ubc_upl_map()](https://developer.apple.com/documentation/kernel/1463744-ubc_upl_map)Added [ubc_upl_maxbufsize()](https://developer.apple.com/documentation/kernel/1463748-ubc_upl_maxbufsize)Added [ubc_upl_pageinfo()](https://developer.apple.com/documentation/kernel/1463704-ubc_upl_pageinfo)Added [ubc_upl_range_needed()](https://developer.apple.com/documentation/kernel/1463746-ubc_upl_range_needed)Added [ubc_upl_unmap()](https://developer.apple.com/documentation/kernel/1463778-ubc_upl_unmap)ucred.hRemoved is_suser()Removed is_suser1()uio.hRemoved [iovec](https://developer.apple.com/documentation/kernel/iovec)un.hRemoved [sa_family_t](https://developer.apple.com/documentation/kernel/sa_family_t)Added #def LOCAL_PEEREPIDAdded #def LOCAL_PEEREUUIDAdded #def LOCAL_PEERUUIDuuid.hModified [uuid_t](https://developer.apple.com/documentation/kernel/uuid_t)

|  | Header |
| --- | --- |
| From | Kernel/uuid/uuid.h |
| To | Kernel/sys/_types/_uuid_t.h |

vDSP.hAdded [COMPLEX](https://developer.apple.com/documentation/kernel/complex)Added [COMPLEX_SPLIT](https://developer.apple.com/documentation/kernel/complex_split)Added [DOUBLE_COMPLEX](https://developer.apple.com/documentation/kernel/double_complex)Added [DOUBLE_COMPLEX_SPLIT](https://developer.apple.com/documentation/kernel/double_complex_split)Added [DSPComplex](https://developer.apple.com/documentation/accelerate/dspcomplex)Added [DSPDoubleComplex](https://developer.apple.com/documentation/kernel/dspdoublecomplex)Added [DSPDoubleSplitComplex](https://developer.apple.com/documentation/accelerate/dspdoublesplitcomplex)Added [DSPSplitComplex](https://developer.apple.com/documentation/kernel/dspsplitcomplex)Added [FFTDirection](https://developer.apple.com/documentation/accelerate/fftdirection)Added [FFTRadix](https://developer.apple.com/documentation/kernel/fftradix)Added [FFTSetup](https://developer.apple.com/documentation/kernel/fftsetup)Added [FFTSetupD](https://developer.apple.com/documentation/kernel/fftsetupd)Added [FFT_FORWARD](https://developer.apple.com/documentation/kernel/1645050-anonymous/fft_forward)Added [FFT_INVERSE](https://developer.apple.com/documentation/kernel/1645050-anonymous/fft_inverse)Added [FFT_RADIX2](https://developer.apple.com/documentation/kernel/1645053-anonymous/fft_radix2)Added [FFT_RADIX3](https://developer.apple.com/documentation/kernel/1645053-anonymous/fft_radix3)Added [FFT_RADIX5](https://developer.apple.com/documentation/kernel/1645053-anonymous/fft_radix5)Added #def USE_NON_APPLE_STANDARD_DATATYPESAdded [kFFTDirection_Forward](https://developer.apple.com/documentation/kernel/1645049-anonymous/kfftdirection_forward)Added [kFFTDirection_Inverse](https://developer.apple.com/documentation/kernel/1645049-anonymous/kfftdirection_inverse)Added [kFFTRadix2](https://developer.apple.com/documentation/kernel/1645051-anonymous/kfftradix2)Added [kFFTRadix3](https://developer.apple.com/documentation/kernel/1645051-anonymous/kfftradix3)Added [kFFTRadix5](https://developer.apple.com/documentation/kernel/1645051-anonymous/kfftradix5)Added [vDSP_HALF_WINDOW](https://developer.apple.com/documentation/accelerate/vdsp_half_window)Added [vDSP_HANN_DENORM](https://developer.apple.com/documentation/accelerate/vdsp_hann_denorm)Added [vDSP_HANN_NORM](https://developer.apple.com/documentation/kernel/1645052-anonymous/vdsp_hann_norm)Added [vDSP_Length](https://developer.apple.com/documentation/accelerate/vdsp_length)Added [vDSP_Stride](https://developer.apple.com/documentation/kernel/vdsp_stride)Added [#def vDSP_Version0](https://developer.apple.com/documentation/accelerate/vdsp_version0)Added [#def vDSP_Version1](https://developer.apple.com/documentation/accelerate/vdsp_version1)Added [vDSP_biquad_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquad_setup)Added [vDSP_biquad_SetupD](https://developer.apple.com/documentation/kernel/vdsp_biquad_setupd)Added [vDSP_biquadm_Setup](https://developer.apple.com/documentation/kernel/vdsp_biquadm_setup)Added [vDSP_create_fftsetup()](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)Added [vDSP_ctoz()](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)Added [vDSP_destroy_fftsetup()](https://developer.apple.com/documentation/accelerate/1450396-vdsp_destroy_fftsetup)Added [vDSP_fft_zrip()](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)Added [vDSP_int24](https://developer.apple.com/documentation/accelerate/vdsp_int24)Added [vDSP_uint24](https://developer.apple.com/documentation/accelerate/vdsp_uint24)Added [vDSP_vadd()](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)Added [vDSP_vclip()](https://developer.apple.com/documentation/accelerate/1450071-vdsp_vclip)Added [vDSP_vclr()](https://developer.apple.com/documentation/accelerate/1450402-vdsp_vclr)Added [vDSP_vdbcon()](https://developer.apple.com/documentation/accelerate/1450241-vdsp_vdbcon)Added [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)Added [vDSP_ztoc()](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)Added [vDSP_zvabs()](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)vecLib.hvm_purgable.hAdded #def VM_PURGABLE_NO_AGINGAdded #def VM_PURGABLE_NO_AGING_MASKAdded #def VM_PURGABLE_NO_AGING_SHIFTvm_region.hAdded #def VM_REGION_SUBMAP_INFO_V0_COUNT_64Added #def VM_REGION_SUBMAP_INFO_V0_SIZEAdded #def VM_REGION_SUBMAP_INFO_V1_COUNT_64Added #def VM_REGION_SUBMAP_INFO_V1_SIZEvm_statistics.hAdded #def VM_FLAGS_RETURN_DATA_ADDRAdded #def VM_MEMORY_ACCELERATEAdded #def VM_MEMORY_COREDATAAdded #def VM_MEMORY_COREDATA_OBJECTIDSAdded #def VM_MEMORY_COREUIAdded #def VM_MEMORY_LIBDISPATCHAdded #def VM_MEMORY_MALLOC_NANOAdded #def VM_MEMORY_OS_ALLOC_ONCEAdded [vm_purgeable_info_t](https://developer.apple.com/documentation/kernel/vm_purgeable_info_t)Added [vm_purgeable_stat_t](https://developer.apple.com/documentation/kernel/vm_purgeable_stat_t)vnode.hAdded #def IO_SWAP_DISPATCHwait.hRemoved [id_t](https://developer.apple.com/documentation/kernel/id_t)Removed [pid_t](https://developer.apple.com/documentation/kernel/pid_t)

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

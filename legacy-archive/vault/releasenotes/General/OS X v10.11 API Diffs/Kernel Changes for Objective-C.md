---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/Kernel.html
archived_at: '2026-07-18T02:53:08.388684Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Kernel Changes for Objective-C

### Kernel

#### atm/atm_types.h

Added #def ATM_ACTION_GETSUBAIDAdded #def ATM_ACTION_REGISTERAdded [atm_guard_t](https://developer.apple.com/documentation/kernel/atm_guard_t)Added #def ATM_TRACE_DISABLE

#### corpses/task_corpse.h (Added)

Added #def CRASHINFO_ITEM_DATA_PTRAdded #def CRASHINFO_ITEM_FOREACHAdded #def CRASHINFO_ITEM_NEXT_HEADERAdded #def CRASHINFO_ITEM_SIZEAdded #def CRASHINFO_ITEM_TYPEAdded #def TASK_CRASHINFO_ARGSLENAdded #def TASK_CRASHINFO_BEGINAdded #def TASK_CRASHINFO_BSDINFOWITHUNIQIDAdded #def TASK_CRASHINFO_CPUTYPEAdded #def TASK_CRASHINFO_CRASHED_THREADIDAdded #def TASK_CRASHINFO_DIRTY_FLAGSAdded #def TASK_CRASHINFO_ENDAdded #def TASK_CRASHINFO_EXCEPTION_CODESAdded #def TASK_CRASHINFO_EXTMODINFOAdded #def TASK_CRASHINFO_GIDAdded [task_crashinfo_item_t](https://developer.apple.com/documentation/kernel/task_crashinfo_item_t)Added #def TASK_CRASHINFO_PIDAdded #def TASK_CRASHINFO_PPIDAdded #def TASK_CRASHINFO_PROC_ARGCAdded #def TASK_CRASHINFO_PROC_CSFLAGSAdded #def TASK_CRASHINFO_PROC_FLAGSAdded #def TASK_CRASHINFO_PROC_NAMEAdded #def TASK_CRASHINFO_PROC_PATHAdded #def TASK_CRASHINFO_PROC_STARTTIMEAdded #def TASK_CRASHINFO_PROC_STATUSAdded #def TASK_CRASHINFO_RESPONSIBLE_PIDAdded #def TASK_CRASHINFO_RUSAGEAdded #def TASK_CRASHINFO_RUSAGE_INFOAdded #def TASK_CRASHINFO_STRING_DESCAdded #def TASK_CRASHINFO_TASKDYLD_INFOAdded #def TASK_CRASHINFO_UIDAdded #def TASK_CRASHINFO_UINT32_DESCAdded #def TASK_CRASHINFO_UINT64_DESCAdded #def TASK_CRASHINFO_USERSTACKAdded #def TASK_CRASHINFO_UUIDAdded #def TASK_CRASHINFO_WORKQUEUEINFO

#### device/device_types.h

Added [io_string_inband_t](https://developer.apple.com/documentation/kernel/io_string_inband_t)

#### hfs/hfs_format.h

Added [kHFSAutoCandidateBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsautocandidatebit)Added [kHFSAutoCandidateMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsautocandidatemask)Added [kHFSDoNotFastDevPinBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsdonotfastdevpinbit)Added [kHFSDoNotFastDevPinMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsdonotfastdevpinmask)Added [kHFSFastDevCandidateBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevcandidatebit)Added [kHFSFastDevCandidateMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevcandidatemask)Added [kHFSFastDevPinnedBit](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevpinnedbit)Added [kHFSFastDevPinnedMask](https://developer.apple.com/documentation/kernel/1646114-anonymous/khfsfastdevpinnedmask)

#### i386/proc_reg.h

Added #def MSR_IA32_VMX_EPT_VPID_CAP_AD_SHIFT

#### IOKit/bluetooth/Bluetooth.h

Added [BluetoothHCICurrentInquiryAccessCodesForWrite](https://developer.apple.com/documentation/kernel/bluetoothhcicurrentinquiryaccesscodesforwrite)Added [BluetoothLESecurityManagerKeypressNotificationType](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype)Added [kBluetoothHCICommandDeleteReservedLTADDR](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommanddeletereservedltaddr)Added [kBluetoothHCICommandEnhancedAcceptSynchronousConnectionRequest](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandenhancedacceptsynchronousconnectionrequest)Added [kBluetoothHCICommandEnhancedSetupSynchronousConnection](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandenhancedsetupsynchronousconnection)Added [kBluetoothHCICommandGetMWSTransportLayerConfiguration](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandgetmwstransportlayerconfiguration)Added [kBluetoothHCICommandLEAddDeviceToResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleadddevicetoresolvinglist)Added [kBluetoothHCICommandLEClearResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleclearresolvinglist)Added [kBluetoothHCICommandLEGenerateDHKey](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlegeneratedhkey)Added [kBluetoothHCICommandLEReadLocalP256PublicKey](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadlocalp256publickey)Added [kBluetoothHCICommandLEReadLocalResolvableAddress](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadlocalresolvableaddress)Added [kBluetoothHCICommandLEReadMaximumDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadmaximumdatalength)Added [kBluetoothHCICommandLEReadPeerResolvableAddress](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadpeerresolvableaddress)Added [kBluetoothHCICommandLEReadResolvingListSize](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadresolvinglistsize)Added [kBluetoothHCICommandLEReadSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadsuggesteddefaultdatalength)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestNegativeReply](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleremoteconnectionparameterrequestnegativereply)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandleremoteconnectionparameterrequestreply)Added [kBluetoothHCICommandLERemoveDeviceFromResolvingList](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleremovedevicefromresolvinglist)Added [kBluetoothHCICommandLESetAddressResolutionEnable](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetaddressresolutionenable)Added [kBluetoothHCICommandLESetDataLength](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetdatalength)Added [kBluetoothHCICommandLESetResolvablePrivateAddressTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetresolvableprivateaddresstimeout)Added [kBluetoothHCICommandLEWriteSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlewritesuggesteddefaultdatalength)Added [kBluetoothHCICommandReadAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadauthenticatedpayloadtimeout)Added [kBluetoothHCICommandReadDataBlockSize](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreaddatablocksize)Added [kBluetoothHCICommandReadExtendedInquiryLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadextendedinquirylength)Added [kBluetoothHCICommandReadExtendedPageTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadextendedpagetimeout)Added [kBluetoothHCICommandReadLocalOOBExtendedData](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlocaloobextendeddata)Added [kBluetoothHCICommandReadLocalSupportedCodecs](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadlocalsupportedcodecs)Added [kBluetoothHCICommandReadSecureConnectionsHostSupport](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadsecureconnectionshostsupport)Added [kBluetoothHCICommandReadSynchronizationTrainParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadsynchronizationtrainparameters)Added [kBluetoothHCICommandReceiveSynchronizationTrain](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreceivesynchronizationtrain)Added [kBluetoothHCICommandRemoteOOBExtendedDataRequestReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandremoteoobextendeddatarequestreply)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcast](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcast)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastData](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcastdata)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastReceive](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcastreceive)Added [kBluetoothHCICommandSetExternalFrameConfiguration](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetexternalframeconfiguration)Added [kBluetoothHCICommandSetMWSChannelParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwschannelparameters)Added [kBluetoothHCICommandSetMWSPATTERNConfiguration](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwspatternconfiguration)Added [kBluetoothHCICommandSetMWSScanFrequencyTable](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwsscanfrequencytable)Added [kBluetoothHCICommandSetMWSSignaling](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwssignaling)Added [kBluetoothHCICommandSetMWSTransportLayer](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwstransportlayer)Added [kBluetoothHCICommandSetReservedLTADDR](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetreservedltaddr)Added [kBluetoothHCICommandSetTriggeredClockCapture](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsettriggeredclockcapture)Added [kBluetoothHCICommandStartSynchronizationTrain](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandstartsynchronizationtrain)Added [kBluetoothHCICommandTruncatedPage](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpage)Added [kBluetoothHCICommandTruncatedPageCancel](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpagecancel)Added [kBluetoothHCICommandWriteAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwriteauthenticatedpayloadtimeout)Added [kBluetoothHCICommandWriteExtendedInquiryLength](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwriteextendedinquirylength)Added [kBluetoothHCICommandWriteExtendedPageTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwriteextendedpagetimeout)Added [kBluetoothHCICommandWriteSecureConnectionsHostSupport](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritesecureconnectionshostsupport)Added [kBluetoothHCICommandWriteSynchronizationTrainParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritesynchronizationtrainparameters)Added [kBluetoothLESecurityManagerLinkKey](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeydistributionformat/kbluetoothlesecuritymanagerlinkkey)Added [kBluetoothLESecurityManagerNotificationTypePasskeyCleared](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeycleared)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitEntered](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeydigitentered)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitErased](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeydigiterased)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryCompleted](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeyentrycompleted)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryStarted](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeyentrystarted)Added [kBluetoothLESecurityManagerNotificationTypeReservedEnd](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypereservedend)Added [kBluetoothLESecurityManagerNotificationTypeReservedStart](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypereservedstart)Added [kBluetoothLESecurityManagerReasonCodeBREDRPairingInProgress](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreasoncodebredrpairinginprogress)Added [kBluetoothLESecurityManagerReasonCodeCrossTransportKeyDerivationGenerationNotAllowed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodecrosstransportkeyderivationgenerationnotallowed)Added [kMaximumNumberOfInquiryAccessCodes](https://developer.apple.com/documentation/iobluetooth/1489444-anonymous/kmaximumnumberofinquiryaccesscodes)

#### IOKit/bluetooth/BluetoothAssignedNumbers.h

Added [kBluetoothL2CAPPSMAVCTP_Browsing](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2cappsmavctp_browsing)

#### IOKit/hid/IOHIDKeys.h

Added #def kIOHIDBatchIntervalKeyAdded #def kIOHIDSystemButtonPressedDuringDarkBootAdded #def kIOHIDUniqueIDKey

#### IOKit/hidevent/IOHIDEventDriver.h

Removed IOHIDEventDriver::calibrateDigitizerElement()Removed IOHIDEventDriver::calibratePreferredStateElement()Added IOHIDEventDriver::calibrateCenteredPreferredStateElement()Added IOHIDEventDriver::calibrateJustifiedPreferredStateElement()Added IOHIDEventDriver::checkGameControllerElement()Added IOHIDEventDriver::handleGameControllerReport()Added IOHIDEventDriver::parseGameControllerElement()Added IOHIDEventDriver::parseLEDElement()Added IOHIDEventDriver::processGameControllerElements()Added IOHIDEventDriver::setGameControllerProperties()Added IOHIDEventDriver::setLEDProperties()

#### IOKit/hidsystem/IOHIDSystem.h

Removed [IOFixedPoint64](https://developer.apple.com/documentation/kernel/iofixedpoint64)Removed [IOHIDEvent](https://developer.apple.com/documentation/kernel/iohidevent)Removed [IOHIDKeyboardDevice](https://developer.apple.com/documentation/kernel/iohidkeyboarddevice)Removed [IOHIDPointingDevice](https://developer.apple.com/documentation/kernel/iohidpointingdevice)Removed [IOHIDSystem](https://developer.apple.com/documentation/kernel/iohidsystem)Removed IOHIDSystem::absolutePointerEvent()Removed IOHIDSystem::absolutePointerEventGated()Removed IOHIDSystem::addConsumedKey()Removed IOHIDSystem::animateWaitCursor()Removed IOHIDSystem::attach()Removed IOHIDSystem::attachDefaultEventSources()Removed IOHIDSystem::changeCursor()Removed IOHIDSystem::createFilteredParamPropertiesForService()Removed IOHIDSystem::createParameters()Removed IOHIDSystem::createShmem()Removed IOHIDSystem::createShmemGated()Removed IOHIDSystem::detach()Removed IOHIDSystem::detachEventSources()Removed IOHIDSystem::disableContinuousCursor()Removed IOHIDSystem::dispatchEvent()Removed IOHIDSystem::doAbsolutePointerEvent()Removed IOHIDSystem::doCreateShmem()Removed IOHIDSystem::doEvClose()Removed IOHIDSystem::doExtGetButtonEventNum()Removed IOHIDSystem::doExtGetStateForSelector()Removed IOHIDSystem::doExtPostEvent()Removed IOHIDSystem::doExtSetMouseLocation()Removed IOHIDSystem::doExtSetStateForSelector()Removed IOHIDSystem::doKeyboardEvent()Removed IOHIDSystem::doKeyboardSpecialEvent()Removed IOHIDSystem::doKickEventConsumer()Removed IOHIDSystem::doNewUserClient()Removed IOHIDSystem::doProcessKeyboardEQ()Removed IOHIDSystem::doProcessNotifications()Removed IOHIDSystem::doProximityEvent()Removed IOHIDSystem::doRegisterEventQueue()Removed IOHIDSystem::doRegisterScreen()Removed IOHIDSystem::doRelativePointerEvent()Removed IOHIDSystem::doScrollWheelEvent()Removed IOHIDSystem::doSetContinuousCursorEnable()Removed IOHIDSystem::doSetCursorEnable()Removed IOHIDSystem::doSetDisplayBounds()Removed IOHIDSystem::doSetEventPort()Removed IOHIDSystem::doSetEventsEnablePost()Removed IOHIDSystem::doSetEventsEnablePre()Removed IOHIDSystem::doSetParamPropertiesPost()Removed IOHIDSystem::doSetParamPropertiesPre()Removed IOHIDSystem::doSpecialKeyMsg()Removed IOHIDSystem::doTabletEvent()Removed IOHIDSystem::doUnregisterEventQueue()Removed IOHIDSystem::doUnregisterScreen()Removed IOHIDSystem::doUpdateEventFlags()Removed IOHIDSystem::enableContinuousCursor()Removed IOHIDSystem::evClose()Removed IOHIDSystem::evCloseGated()Removed IOHIDSystem::evDispatch()Removed IOHIDSystem::eventFlags()Removed IOHIDSystem::evOpen()Removed IOHIDSystem::evSpecialKeyMsg()Removed IOHIDSystem::extGetButtonEventNum()Removed IOHIDSystem::extGetButtonEventNumGated()Removed IOHIDSystem::extGetStateForSelector()Removed IOHIDSystem::extGetUserHidActivityState()Removed IOHIDSystem::extPostEvent()Removed IOHIDSystem::extPostEventGated()Removed IOHIDSystem::extRegisterVirtualDisplay()Removed IOHIDSystem::extSetBounds()Removed IOHIDSystem::extSetMouseLocation()Removed IOHIDSystem::extSetMouseLocationGated()Removed IOHIDSystem::extSetStateForSelector()Removed IOHIDSystem::extSetVirtualDisplayBounds()Removed IOHIDSystem::extUnregisterVirtualDisplay()Removed IOHIDSystem::free()Removed IOHIDSystem::genericNotificationHandler()Removed IOHIDSystem::getCapsLockState()Removed IOHIDSystem::getMetaClass()Removed IOHIDSystem::getNumLockState()Removed IOHIDSystem::getSubtypeForSender()Removed IOHIDSystem::getUniqueEventNum()Removed IOHIDSystem::getUserHidActivityState()Removed IOHIDSystem::getUserHidActivityStateGated()Removed IOHIDSystem::getWorkLoop()Removed IOHIDSystem::handlePublishNotification()Removed IOHIDSystem::handleTerminateNotification()Removed IOHIDSystem::hidActivityChecker()Removed IOHIDSystem::hideCursor()Removed IOHIDSystem::hideWaitCursor()Removed IOHIDSystem::init()Removed IOHIDSystem::initShmem()Removed IOHIDSystem::instance()Removed IOHIDSystem::keyboardEvent()Removed IOHIDSystem::keyboardEventGated()Removed IOHIDSystem::keyboardSpecialEvent()Removed IOHIDSystem::keyboardSpecialEventGated()Removed IOHIDSystem::kickEventConsumer()Removed IOHIDSystem::makeInt32ArrayParamProperty()Removed IOHIDSystem::makeNumberParamProperty()Removed IOHIDSystem::message()Removed IOHIDSystem::moveCursor()Removed IOHIDSystem::newUserClient()Removed IOHIDSystem::newUserClientGated()Removed IOHIDSystem::periodicEvents()Removed IOHIDSystem::pointToScreen()Removed IOHIDSystem::postEvent()Removed IOHIDSystem::powerStateDidChangeTo()Removed IOHIDSystem::powerStateHandler()Removed IOHIDSystem::probe()Removed IOHIDSystem::processKeyboardEQ()Removed IOHIDSystem::proximityEvent()Removed IOHIDSystem::proximityEventGated()Removed IOHIDSystem::registerEventQueue()Removed IOHIDSystem::registerEventQueueGated()Removed IOHIDSystem::registerEventSource()Removed IOHIDSystem::registerScreen()Removed IOHIDSystem::registerScreenGated()Removed IOHIDSystem::relativePointerEvent()Removed IOHIDSystem::relativePointerEventGated()Removed IOHIDSystem::removeConsumedKey()Removed IOHIDSystem::reportUserHidActivity()Removed IOHIDSystem::reportUserHidActivityGated()Removed IOHIDSystem::resetCursor()Removed IOHIDSystem::scaleLocationToCurrentScreen()Removed IOHIDSystem::scheduleNextPeriodicEvent()Removed IOHIDSystem::scrollWheelEvent()Removed IOHIDSystem::scrollWheelEventGated()Removed IOHIDSystem::sendStackShotMessage()Removed IOHIDSystem::setCapsLockState()Removed IOHIDSystem::setContinuousCursorEnable()Removed IOHIDSystem::setContinuousCursorEnableGated()Removed IOHIDSystem::setCursorEnable()Removed IOHIDSystem::setCursorEnableGated()Removed IOHIDSystem::setCursorPosition()Removed IOHIDSystem::setDisplayBoundsGated()Removed IOHIDSystem::setDisplaySleepDrivenByPM()Removed IOHIDSystem::setEventPort()Removed IOHIDSystem::setEventPortGated()Removed IOHIDSystem::setEventsEnable()Removed IOHIDSystem::setEventsEnablePostGated()Removed IOHIDSystem::setEventsEnablePreGated()Removed IOHIDSystem::setNumLockState()Removed IOHIDSystem::setParamProperties()Removed IOHIDSystem::setParamPropertiesPostGated()Removed IOHIDSystem::setParamPropertiesPreGated()Removed IOHIDSystem::setProperties()Removed IOHIDSystem::setSpecialKeyPort()Removed IOHIDSystem::setStackShotPort()Removed IOHIDSystem::showCursor()Removed IOHIDSystem::showWaitCursor()Removed IOHIDSystem::specialKeyPort()Removed IOHIDSystem::start()Removed IOHIDSystem::startCursor()Removed IOHIDSystem::tabletEvent()Removed IOHIDSystem::tabletEventGated()Removed IOHIDSystem::unregisterEventQueue()Removed IOHIDSystem::unregisterEventQueueGated()Removed IOHIDSystem::unregisterScreen()Removed IOHIDSystem::unregisterScreenGated()Removed IOHIDSystem::updateEventFlags()Removed IOHIDSystem::updateEventFlagsGated()Removed IOHIDSystem::updateHidActivity()Removed IOHIDSystem::updateMouseEventForSender()Removed IOHIDSystem::updateMouseMoveEventForSender()Removed IOHIDSystem::updateScrollEventForSender()Removed IOHIDSystem::workspaceBounds()Removed #def kIOHIDSystem508MouseClickMessageRemoved #def kIOHIDSystem508SpecialKeyDownMessageRemoved #def kIOHIDSystemActivityTickleRemoved #def kIOHIDSystemDeviceSeizeRequestMessageRemoved #def kIOHIDSystemUserHidActivity

#### IOKit/hidsystem/IOHIKeyboard.h

Removed IOHIKeyboard::attachToChild()Removed IOHIKeyboard::detachFromChild()Removed IOHIKeyboard::newUserClient()Removed IOHIKeyboard::newUserClientGated()Removed IOHIKeyboard::postSecureKey()

#### IOKit/IODataQueue.h

Removed IODataQueue::enqueue_tail()Added IODataQueue::enqueue()

#### IOKit/IODeviceTreeSupport.h

Added [gIODTTargetTypeKey](https://developer.apple.com/documentation/kernel/giodttargettypekey)

#### IOKit/IODMACommand.h

Added [IOBufferMemoryDescriptor](https://developer.apple.com/documentation/kernel/iobuffermemorydescriptor)Added IODMACommand::createCopyBuffer()Added IODMACommand::getAlignmentInternalSegments()Added IODMACommand::getAlignmentLength()Added IODMACommand::getIOMemoryDescriptor()Added IODMACommand::initWithRefCon()Added IODMACommand::setSpecification()Added IODMACommand::withRefCon()Added [kIODMAMapOptionBypassed](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptionbypassed)Added [kIODMAMapOptionIterateOnly](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptioniterateonly)Added [kIODMAMapOptionMapped](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptionmapped)Added [kIODMAMapOptionNoCacheStore](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptionnocachestore)Added [kIODMAMapOptionNonCoherent](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptionnoncoherent)Added [kIODMAMapOptionOnChip](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptiononchip)Added [kIODMAMapOptionTypeMask](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptiontypemask)Added [kIODMAMapOptionUnmapped](https://developer.apple.com/documentation/kernel/1645905-anonymous/kiodmamapoptionunmapped)

#### IOKit/IODMAController.h

Added IODMAController::setFrameSize()

#### IOKit/IODMAEventSource.h

Added IODMAEventSource::setFrameSize()

#### IOKit/IOInterruptAccounting.h

Added #def kInterruptAccountingGroupName

#### IOKit/IOKitDebug.h

Removed kOSTraceObjectAllocAdded [IOKitDiagnosticsParameters](https://developer.apple.com/documentation/kernel/iokitdiagnosticsparameters)Added [IOTrackingCallSiteInfo](https://developer.apple.com/documentation/kernel/iotrackingcallsiteinfo)Added [kIOKextSpinDump](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiokextspindump)Added #def kIOKitDiagnosticsClientClassNameAdded [kIOKitDiagnosticsClientType](https://developer.apple.com/documentation/kernel/1644086-anonymous/kiokitdiagnosticsclienttype)Added #def kIOMallocTrackingNameAdded #def kIOMapTrackingNameAdded [kIOTracking](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiotracking)Added [kIOTrackingBoot](https://developer.apple.com/documentation/kernel/1644087-anonymous/kiotrackingboot)Added [kIOTrackingCallSiteBTs](https://developer.apple.com/documentation/kernel/1644081-anonymous/kiotrackingcallsitebts)Added [kIOTrackingExcludeNames](https://developer.apple.com/documentation/kernel/1644084-anonymous/kiotrackingexcludenames)Added [kIOTrackingGetTracking](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackinggettracking)Added [kIOTrackingInvalid](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackinginvalid)Added [kIOTrackingLeaks](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackingleaks)Added kIOTrackingPrintTrackingAdded [kIOTrackingResetTracking](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackingresettracking)Added [kIOTrackingSetMinCaptureSize](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackingsetmincapturesize)Added [kIOTrackingStartCapture](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackingstartcapture)Added [kIOTrackingStopCapture](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackingstopcapture)Added #def kIOWireTrackingNameModified IOKitDiagnostics::updateOffset()

|  | Declaration |
| --- | --- |
| From | ``` void updateOffset (     OSDictionary *dict,     UInt32 value,     const char *name ); ``` |
| To | ``` void updateOffset (     OSDictionary *dict,     UInt64 value,     const char *name ); ``` |

#### IOKit/IOKitDiagnosticsUserClient.h (Added)

Added [IOKitDiagnosticsClient](https://developer.apple.com/documentation/kernel/iokitdiagnosticsclient)Added IOKitDiagnosticsClient::clientClose()Added IOKitDiagnosticsClient::externalMethod()Added IOKitDiagnosticsClient::getMetaClass()Added IOKitDiagnosticsClient::setProperties()Added IOKitDiagnosticsClient::withTask()

#### IOKit/IOLib.h

Added [IOSleepWithLeeway()](https://developer.apple.com/documentation/kernel/1575303-iosleepwithleeway)

#### IOKit/IOMapper.h

Removed IOMapper::allocTable()Removed IOMapper::FreeARTTable()Removed IOMapper::getBypassMask()Removed IOMapper::iovmAlloc()Removed IOMapper::iovmAllocDMACommand()Removed IOMapper::iovmFree()Removed IOMapper::iovmFreeDMACommand()Removed IOMapper::mapAddr()Removed IOMapper::NewARTTable()Removed IOFreePhysical()Removed IOMallocPhysical()Removed IOMapperInsertPPNPages()Removed IOMapperInsertUPLPages()Added IOMapper::getPageSize()Added IOMapper::iovmUnmapMemory()Added IOMapper::mapToPhysicalAddress()Modified IOMapper::iovmInsert()

|  | Declaration |
| --- | --- |
| From | ``` virtual void iovmInsert (     ppnum_t addr,     IOItemCount offset,     ppnum_t page ); ``` |
| To | ``` virtual IOReturn iovmInsert (     uint32_t options,     uint64_t mapAddress,     uint64_t offset,     uint64_t physicalAddress,     uint64_t length ); ``` |

Modified IOMapper::iovmMapMemory()

|  | Declaration |
| --- | --- |
| From | ``` virtual ppnum_t iovmMapMemory (     OSObject *memory,     ppnum_t offsetPage,     ppnum_t pageCount,     uint32_t options,     upl_page_info_t *pageList,     const IODMAMapSpecification *mapSpecification ); ``` |
| To | ``` virtual IOReturn iovmMapMemory (     IOMemoryDescriptor *memory,     uint64_t descriptorOffset,     uint64_t length,     uint32_t mapOptions,     const IODMAMapSpecification *mapSpecification,     IODMACommand *dmaCommand,     const IODMAMapPageList *pageList,     uint64_t *mapAddress,     uint64_t *mapLength ); ``` |

#### IOKit/IOMemoryDescriptor.h

Added [IODMACommand](https://developer.apple.com/documentation/kernel/iodmacommand)Added [IODMAMapPageList](https://developer.apple.com/documentation/kernel/iodmamappagelist)Added [kIODMAMapFixedAddress](https://developer.apple.com/documentation/kernel/1643343-anonymous/kiodmamapfixedaddress)Added [kIODMAMapPageListFullyOccupied](https://developer.apple.com/documentation/kernel/1643343-anonymous/kiodmamappagelistfullyoccupied)Added [kIODMAMapReadAccess](https://developer.apple.com/documentation/kernel/1643343-anonymous/kiodmamapreadaccess)

#### IOKit/IOMultiMemoryDescriptor.h

Added IOMultiMemoryDescriptor::doMap()Added IOMultiMemoryDescriptor::getPageCounts()Added IOMultiMemoryDescriptor::setPurgeable()Added #def IOMULTIMEMORYDESCRIPTOR_SUPPORTS_GETPAGECOUNTS

#### IOKit/IONVRAM.h

Added IODTNVRAM::syncInternal()

#### IOKit/IOPlatformExpert.h

Added IOPlatformExpertDevice::newUserClient()Added [gIOPlatformPanicActionKey](https://developer.apple.com/documentation/kernel/gioplatformpanicactionkey)Added [PEWriteNVRAMBooleanProperty()](https://developer.apple.com/documentation/kernel/1451625-pewritenvrambooleanproperty)

#### IOKit/IOReportMacros.h

Added #def HISTREPORT_BUFSIZEAdded #def HISTREPORT_GETCHIDAdded #def HISTREPORT_GETCHTYPEAdded #def HISTREPORT_INITAdded #def HISTREPORT_TALLYVALUEAdded #def HISTREPORT_UPDATEPREPAdded #def HISTREPORT_UPDATERESAdded [IOHistReportInfo](https://developer.apple.com/documentation/kernel/iohistreportinfo)

#### IOKit/IOReturn.h

Added #def sub_iokit_basebandAdded #def sub_iokit_HDAAdded #def sub_iokit_platformAdded #def sub_iokit_usbaudio

#### IOKit/IOSubMemoryDescriptor.h

Added IOSubMemoryDescriptor::getPageCounts()

#### IOKit/IOTimeStamp.h

Added #def IOSERVICE_DETACHAdded #def IOSERVICE_TERM_SCHED_PHASE2Added #def IOSERVICE_TERM_SET_INACTIVEAdded #def IOSERVICE_TERM_START_PHASE2Added #def IOSERVICE_TERM_TRY_PHASE2Added #def IOSERVICE_TERM_UC_DEFER

#### IOKit/IOTypes.h

Added [kIOMapOverwrite](https://developer.apple.com/documentation/iokit/kiomapoverwrite)

#### IOKit/network/IONetworkInterface.h

Added IONetworkInterface::configureOutputStartDelay()

#### IOKit/network/IONetworkMedium.h

Added [kIOMediumEthernet2500BaseT](https://developer.apple.com/documentation/kernel/1645756-anonymous/kiomediumethernet2500baset)Added [kIOMediumEthernet5000BaseT](https://developer.apple.com/documentation/kernel/1645756-anonymous/kiomediumethernet5000baset)

#### IOKit/nvram/IONVRAMController.h

Removed IONVRAMController::start()Added IONVRAMController::registerService()

#### IOKit/pci/IOPCIDevice.h

Added IOPCIDevice::copyAERErrorDescriptionForBit()Added [kIOPCIConfigShadowPermanent](https://developer.apple.com/documentation/kernel/1640338-anonymous/kiopciconfigshadowpermanent)Added [kIOPCICorrectableErrorBitAdvisoryNonFatal](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitadvisorynonfatal)Added [kIOPCICorrectableErrorBitBadDLLP](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitbaddllp)Added [kIOPCICorrectableErrorBitBadTLP](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitbadtlp)Added [kIOPCICorrectableErrorBitCorrectedInternal](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitcorrectedinternal)Added [kIOPCICorrectableErrorBitHeaderLogOverflow](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitheaderlogoverflow)Added [kIOPCICorrectableErrorBitReceiver](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitreceiver)Added [kIOPCICorrectableErrorBitReplayNumRollover](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitreplaynumrollover)Added [kIOPCICorrectableErrorBitReplayTimerTimeout](https://developer.apple.com/documentation/kernel/1640348-anonymous/kiopcicorrectableerrorbitreplaytimertimeout)Added #def kIOPCIDeviceDeviceTreeEntryKeyAdded [kIOPCIUncorrectableErrorBitACSViolation](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitacsviolation)Added [kIOPCIUncorrectableErrorBitAtomicOpEgressBlocked](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitatomicopegressblocked)Added [kIOPCIUncorrectableErrorBitCompleterAbort](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitcompleterabort)Added [kIOPCIUncorrectableErrorBitCompletionTimeout](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitcompletiontimeout)Added [kIOPCIUncorrectableErrorBitDataLinkProtocol](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitdatalinkprotocol)Added [kIOPCIUncorrectableErrorBitECRC](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitecrc)Added [kIOPCIUncorrectableErrorBitFlowControlProtocol](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitflowcontrolprotocol)Added [kIOPCIUncorrectableErrorBitInternal](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitinternal)Added [kIOPCIUncorrectableErrorBitMalformedTLP](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitmalformedtlp)Added [kIOPCIUncorrectableErrorBitMCBlockedTLP](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitmcblockedtlp)Added [kIOPCIUncorrectableErrorBitPoisonedTLP](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitpoisonedtlp)Added [kIOPCIUncorrectableErrorBitReceiverOverflow](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitreceiveroverflow)Added [kIOPCIUncorrectableErrorBitSurpriseDown](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitsurprisedown)Added [kIOPCIUncorrectableErrorBitTLPPrefixBlocked](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbittlpprefixblocked)Added [kIOPCIUncorrectableErrorBitUnexpectedCompletion](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitunexpectedcompletion)Added [kIOPCIUncorrectableErrorBitUnsupportedRequest](https://developer.apple.com/documentation/kernel/1640328-anonymous/kiopciuncorrectableerrorbitunsupportedrequest)

#### IOKit/pwr_mgt/RootDomain.h

Added IOPMrootDomain::configureReportGated()Added IOPMrootDomain::updateReportGated()

#### IOKit/scsi/IOSCSIPrimaryCommandsDevice.h

Added IOSCSIPrimaryCommandsDevice::ClampPowerState()Added IOSCSIPrimaryCommandsDevice::ReleasePowerStateClamp()Added #def fNumCommandsExecuting

#### IOKit/scsi/SCSICmds_INQUIRY_Definitions.h

Added [SCSICmd_INQUIRY_Page00_Header_SPC_16](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_page00_header_spc_16)Added [SCSICmd_INQUIRY_Page80_Header_SPC_16](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_page80_header_spc_16)

#### IOKit/storage/IOApplePartitionScheme.h

Removed IOApplePartitionScheme::attachMediaObjectToDeviceTree()Removed IOApplePartitionScheme::detachMediaObjectFromDeviceTree()

#### IOKit/storage/IOBlockStorageDevice.h

Removed IOBlockStorageDevice::doSyncReadWrite()Removed IOBlockStorageDevice::reportMaxReadTransfer()Removed IOBlockStorageDevice::reportMaxWriteTransfer()Added IOBlockStorageDevice::doSynchronize()Modified IOBlockStorageDevice::doAsyncReadWrite()

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` virtual IOReturn doAsyncReadWrite (     IOMemoryDescriptor *buffer,     UInt32 block,     UInt32 nblks,     IOStorageCompletion completion ); ``` | OS X 10.6 |
| To | ``` virtual IOReturn doAsyncReadWrite (     IOMemoryDescriptor *buffer,     UInt64 block,     UInt64 nblks,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` | -- |

Modified IOBlockStorageDevice::doDiscard()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDevice::doLockUnlockMedia()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDevice::doSynchronizeCache()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified IOBlockStorageDevice::doUnmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn doUnmap (     IOBlockStorageDeviceExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn doUnmap (     IOBlockStorageDeviceExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

Modified IOBlockStorageDevice::reportLockability()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDevice::reportPollRequirements()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

#### IOKit/storage/IOBlockStorageDriver.h

Removed IOBlockStorageDriver::synchronizeCache()Added IOBlockStorageDriver::synchronize()Modified IOBlockStorageDriver::breakUpRequest()

|  | Declaration |
| --- | --- |
| From | ``` virtual void breakUpRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion,     IOBlockStorageDriver::Context *context ); ``` |
| To | ``` virtual void breakUpRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     IOStorageCompletion *completion,     IOBlockStorageDriver::Context *context ); ``` |

Modified IOBlockStorageDriver::constrainByteCount()

|  | Deprecation | Removal |
| --- | --- | --- |
| From | -- | OS X 10.7 |
| To | OS X 10.11 | OS X 10.11 |

Modified IOBlockStorageDriver::deblockRequest()

|  | Declaration |
| --- | --- |
| From | ``` virtual void deblockRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion,     IOBlockStorageDriver::Context *context ); ``` |
| To | ``` virtual void deblockRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     IOStorageCompletion *completion,     IOBlockStorageDriver::Context *context ); ``` |

Modified IOBlockStorageDriver::executeRequest()

|  | Declaration |
| --- | --- |
| From | ``` virtual void executeRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion,     IOBlockStorageDriver::Context *context ); ``` |
| To | ``` virtual void executeRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     IOStorageCompletion *completion,     IOBlockStorageDriver::Context *context ); ``` |

Modified IOBlockStorageDriver::handleYield()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::isMediaPollExpensive()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::isMediaPollRequired()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::lockMedia()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::pollMedia()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::prepareRequest()

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` virtual void prepareRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion ); ``` | OS X 10.6 |
| To | ``` virtual void prepareRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` | -- |

Modified IOBlockStorageDriver::schedulePoller()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::unmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

Modified IOBlockStorageDriver::unschedulePoller()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOBlockStorageDriver::yield()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

#### IOKit/storage/IOCDBlockStorageDevice.h

Removed IOCDBlockStorageDevice::audioPause()Removed IOCDBlockStorageDevice::audioPlay()Removed IOCDBlockStorageDevice::audioScan()Removed IOCDBlockStorageDevice::audioStop()Removed IOCDBlockStorageDevice::getAudioStatus()Removed IOCDBlockStorageDevice::getAudioVolume()Removed IOCDBlockStorageDevice::setAudioVolume()

#### IOKit/storage/IOCDBlockStorageDriver.h

Removed IOCDBlockStorageDriver::audioPause()Removed IOCDBlockStorageDriver::audioPlay()Removed IOCDBlockStorageDriver::audioScan()Removed IOCDBlockStorageDriver::audioStop()Removed IOCDBlockStorageDriver::getAudioStatus()Removed IOCDBlockStorageDriver::getAudioVolume()Removed IOCDBlockStorageDriver::setAudioVolume()Modified IOCDBlockStorageDriver::executeRequest()

|  | Declaration |
| --- | --- |
| From | ``` virtual void executeRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion,     IOBlockStorageDriver::Context *context ); ``` |
| To | ``` virtual void executeRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     IOStorageCompletion *completion,     IOBlockStorageDriver::Context *context ); ``` |

Modified IOCDBlockStorageDriver::prepareRequest()

|  | Declaration |
| --- | --- |
| From | ``` virtual void prepareRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageCompletion completion ); ``` |
| To | ``` virtual void prepareRequest (     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` |

Modified IOCDBlockStorageDriver::readCD()

|  | Declaration |
| --- | --- |
| From | ``` virtual void readCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageCompletion completion ); ``` |
| To | ``` virtual void readCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` |

Modified IOCDBlockStorageDriver::writeCD()

|  | Declaration |
| --- | --- |
| From | ``` virtual void writeCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageCompletion completion ); ``` |
| To | ``` virtual void writeCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` |

#### IOKit/storage/IOCDMedia.h

Modified IOCDMedia::readCD()

|  | Declaration |
| --- | --- |
| From | ``` virtual void readCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageCompletion completion ); ``` |
| To | ``` virtual void readCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` |

Modified IOCDMedia::writeCD()

|  | Declaration |
| --- | --- |
| From | ``` virtual void writeCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageCompletion completion ); ``` |
| To | ``` virtual void writeCD (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     CDSectorArea sectorArea,     CDSectorType sectorType,     IOStorageAttributes *attributes,     IOStorageCompletion *completion ); ``` |

#### IOKit/storage/IOFDiskPartitionScheme.h

Removed IOFDiskPartitionScheme::attachMediaObjectToDeviceTree()Removed IOFDiskPartitionScheme::detachMediaObjectFromDeviceTree()

#### IOKit/storage/IOFilterScheme.h

Removed IOFilterScheme::synchronizeCache()Added IOFilterScheme::synchronize()Modified IOFilterScheme::unmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

#### IOKit/storage/IOGUIDPartitionScheme.h

Removed IOGUIDPartitionScheme::attachMediaObjectToDeviceTree()Removed IOGUIDPartitionScheme::detachMediaObjectFromDeviceTree()

#### IOKit/storage/IOMedia.h

Removed IOMedia::synchronizeCache()Added IOMedia::synchronize()Modified IOMedia::init()

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` virtual bool init (     UInt64 base,     UInt64 size,     UInt64 preferredBlockSize,     bool isEjectable,     bool isWhole,     bool isWritable,     const char *contentHint,     OSDictionary *properties ); ``` | OS X 10.6 |
| To | ``` virtual bool init (     UInt64 base,     UInt64 size,     UInt64 preferredBlockSize,     IOMediaAttributeMask attributes,     bool isWhole,     bool isWritable,     const char *contentHint,     OSDictionary *properties ); ``` | -- |

Modified IOMedia::unmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

#### IOKit/storage/IOMediaBSDClient.h

Removed IOMediaBSDClient::getAnchors()Removed IOMediaBSDClient::getMinor()Removed IOMediaBSDClient::getMinors()

#### IOKit/storage/IOPartitionScheme.h

Removed IOPartitionScheme::synchronizeCache()Added IOPartitionScheme::synchronize()Modified IOPartitionScheme::attachMediaObjectToDeviceTree()

|  | Declaration |
| --- | --- |
| From | ``` virtual bool attachMediaObjectToDeviceTree (     IOMedia *media,     IOOptionBits options ); ``` |
| To | ``` virtual bool attachMediaObjectToDeviceTree (     IOMedia *media ); ``` |

Modified IOPartitionScheme::detachMediaObjectFromDeviceTree()

|  | Declaration |
| --- | --- |
| From | ``` virtual void detachMediaObjectFromDeviceTree (     IOMedia *media,     IOOptionBits options ); ``` |
| To | ``` virtual void detachMediaObjectFromDeviceTree (     IOMedia *media ); ``` |

Modified IOPartitionScheme::unmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

#### IOKit/storage/IOStorage.h

Removed IOStorage::init()Added IOStorage::attach()Added IOStorage::synchronize()Added [IOStorageSynchronizeOptions](https://developer.apple.com/documentation/kernel/iostoragesynchronizeoptions)Added [IOStorageUnmapOptions](https://developer.apple.com/documentation/kernel/iostorageunmapoptions)Added #def kIOStorageFeatureBarrierAdded [kIOStorageSynchronizeOptionBarrier](https://developer.apple.com/documentation/kernel/1644753-anonymous/kiostoragesynchronizeoptionbarrier)Added [kIOStorageSynchronizeOptionNone](https://developer.apple.com/documentation/kernel/1644753-anonymous/kiostoragesynchronizeoptionnone)Added [kIOStorageSynchronizeOptionReserved](https://developer.apple.com/documentation/kernel/1644753-anonymous/kiostoragesynchronizeoptionreserved)Added [kIOStorageUnmapOptionReserved](https://developer.apple.com/documentation/kernel/1644750-anonymous/kiostorageunmapoptionreserved)Modified IOStorage::discard()

|  | Removal |
| --- | --- |
| From | OS X 10.7 |
| To | OS X 10.11 |

Modified IOStorage::read()

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` virtual void read (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion ); ``` | OS X 10.6 |
| To | ``` virtual IOReturn read (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     UInt64 *actualByteCount ); ``` | -- |

Modified IOStorage::synchronizeCache()

|  | Deprecation | Removal |
| --- | --- | --- |
| From | -- | OS X 10.7 |
| To | OS X 10.11 | OS X 10.11 |

Modified IOStorage::unmap()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     UInt32 options ); ``` |
| To | ``` virtual IOReturn unmap (     IOService *client,     IOStorageExtent *extents,     UInt32 extentsCount,     IOStorageUnmapOptions options ); ``` |

Modified IOStorage::write()

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` virtual void write (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageCompletion completion ); ``` | OS X 10.6 |
| To | ``` virtual IOReturn write (     IOService *client,     UInt64 byteStart,     IOMemoryDescriptor *buffer,     IOStorageAttributes *attributes,     UInt64 *actualByteCount ); ``` | -- |

#### IOKit/usb/IOUFIStorageServices.h

Removed IOUFIStorageServicesRemoved IOUFIStorageServices::AsyncReadWriteComplete()Removed IOUFIStorageServices::attach()Removed IOUFIStorageServices::detach()Removed IOUFIStorageServices::doAsyncReadWrite()Removed IOUFIStorageServices::doEjectMedia()Removed IOUFIStorageServices::doFormatMedia()Removed IOUFIStorageServices::doGetFormatCapacities()Removed IOUFIStorageServices::doSynchronizeCache()Removed IOUFIStorageServices::doSyncReadWrite()Removed IOUFIStorageServices::getAdditionalDeviceInfoString()Removed IOUFIStorageServices::getMetaClass()Removed IOUFIStorageServices::getProductString()Removed IOUFIStorageServices::getRevisionString()Removed IOUFIStorageServices::getVendorString()Removed IOUFIStorageServices::getWriteCacheState()Removed IOUFIStorageServices::message()Removed IOUFIStorageServices::reportBlockSize()Removed IOUFIStorageServices::reportEjectability()Removed IOUFIStorageServices::reportMaxValidBlock()Removed IOUFIStorageServices::reportMediaState()Removed IOUFIStorageServices::reportRemovability()Removed IOUFIStorageServices::reportWriteProtection()Removed IOUFIStorageServices::setWriteCacheState()

#### IOKit/usb/IOUSBBus.h (Removed)

Removed IOUSBBusRemoved IOUSBBus::getMetaClass()

#### IOKit/usb/IOUSBCommand.h (Removed)

Removed IOUSBCommandRemoved IOUSBCommand::free()Removed IOUSBCommand::GetAddress()Removed IOUSBCommand::GetBuffer()Removed IOUSBCommand::GetBufferMemoryDescriptor()Removed IOUSBCommand::GetBufferRounding()Removed IOUSBCommand::GetBufferUSBCommand()Removed IOUSBCommand::GetClientCompletion()Removed IOUSBCommand::GetCompletionTimeout()Removed IOUSBCommand::GetDataRemaining()Removed IOUSBCommand::GetDblBufLength()Removed IOUSBCommand::GetDirection()Removed IOUSBCommand::GetDisjointCompletion()Removed IOUSBCommand::GetDMACommand()Removed IOUSBCommand::GetEndpoint()Removed IOUSBCommand::GetFinalTransferInTransaction()Removed IOUSBCommand::GetIsSyncTransfer()Removed IOUSBCommand::GetMasterUSBCommand()Removed IOUSBCommand::getMetaClass()Removed IOUSBCommand::GetMultiTransferTransaction()Removed IOUSBCommand::GetNoDataTimeout()Removed IOUSBCommand::GetOrigBuffer()Removed IOUSBCommand::GetReqCount()Removed IOUSBCommand::GetRequest()Removed IOUSBCommand::GetRequestMemoryDescriptor()Removed IOUSBCommand::GetSelector()Removed IOUSBCommand::GetStage()Removed IOUSBCommand::GetStatus()Removed IOUSBCommand::GetStreamID()Removed IOUSBCommand::GetTimeStamp()Removed IOUSBCommand::GetType()Removed IOUSBCommand::GetUIMScratch()Removed IOUSBCommand::GetUIMScratch64()Removed IOUSBCommand::GetUseTimeStamp()Removed IOUSBCommand::GetUSLCompletion()Removed IOUSBCommand::init()Removed IOUSBCommand::NewCommand()Removed IOUSBCommand::SetAddress()Removed IOUSBCommand::SetBT()Removed IOUSBCommand::SetBuffer()Removed IOUSBCommand::SetBufferMemoryDescriptor()Removed IOUSBCommand::SetBufferRounding()Removed IOUSBCommand::SetBufferUSBCommand()Removed IOUSBCommand::SetClientCompletion()Removed IOUSBCommand::SetCompletionTimeout()Removed IOUSBCommand::SetDataRemaining()Removed IOUSBCommand::SetDblBufLength()Removed IOUSBCommand::SetDirection()Removed IOUSBCommand::SetDisjointCompletion()Removed IOUSBCommand::SetDMACommand()Removed IOUSBCommand::SetEndpoint()Removed IOUSBCommand::SetFinalTransferInTransaction()Removed IOUSBCommand::SetIsSyncTransfer()Removed IOUSBCommand::SetMultiTransferTransaction()Removed IOUSBCommand::SetNoDataTimeout()Removed IOUSBCommand::SetOrigBuffer()Removed IOUSBCommand::SetReqCount()Removed IOUSBCommand::SetRequest()Removed IOUSBCommand::SetRequestMemoryDescriptor()Removed IOUSBCommand::SetSelector()Removed IOUSBCommand::SetStage()Removed IOUSBCommand::SetStatus()Removed IOUSBCommand::SetStreamID()Removed IOUSBCommand::SetTimeStamp()Removed IOUSBCommand::SetType()Removed IOUSBCommand::SetUIMScratch()Removed IOUSBCommand::SetUIMScratch64()Removed IOUSBCommand::SetUseTimeStamp()Removed IOUSBCommand::SetUSLCompletion()Removed IOUSBCommandPoolRemoved IOUSBCommandPool::gatedGetCommand()Removed IOUSBCommandPool::gatedReturnCommand()Removed IOUSBCommandPool::getMetaClass()Removed IOUSBCommandPool::withWorkLoop()Removed IOUSBIsocCommandRemoved IOUSBIsocCommand::free()Removed IOUSBIsocCommand::GetAddress()Removed IOUSBIsocCommand::GetBuffer()Removed IOUSBIsocCommand::GetCompletion()Removed IOUSBIsocCommand::GetDirection()Removed IOUSBIsocCommand::GetDMACommand()Removed IOUSBIsocCommand::GetEndpoint()Removed IOUSBIsocCommand::GetFrameList()Removed IOUSBIsocCommand::GetIsRosettaClient()Removed IOUSBIsocCommand::GetIsSyncTransfer()Removed IOUSBIsocCommand::GetLowLatency()Removed IOUSBIsocCommand::getMetaClass()Removed IOUSBIsocCommand::GetNumFrames()Removed IOUSBIsocCommand::GetSelector()Removed IOUSBIsocCommand::GetStartFrame()Removed IOUSBIsocCommand::GetStatus()Removed IOUSBIsocCommand::GetTimeStamp()Removed IOUSBIsocCommand::GetUIMScratch()Removed IOUSBIsocCommand::GetUpdateFrequency()Removed IOUSBIsocCommand::GetUseTimeStamp()Removed IOUSBIsocCommand::GetUSLCompletion()Removed IOUSBIsocCommand::init()Removed IOUSBIsocCommand::NewCommand()Removed IOUSBIsocCommand::SetAddress()Removed IOUSBIsocCommand::SetBuffer()Removed IOUSBIsocCommand::SetCompletion()Removed IOUSBIsocCommand::SetDirection()Removed IOUSBIsocCommand::SetDMACommand()Removed IOUSBIsocCommand::SetEndpoint()Removed IOUSBIsocCommand::SetFrameList()Removed IOUSBIsocCommand::SetIsSyncTransfer()Removed IOUSBIsocCommand::SetLowLatency()Removed IOUSBIsocCommand::SetNumFrames()Removed IOUSBIsocCommand::SetRosettaClient()Removed IOUSBIsocCommand::SetSelector()Removed IOUSBIsocCommand::SetStartFrame()Removed IOUSBIsocCommand::SetStatus()Removed IOUSBIsocCommand::SetTimeStamp()Removed IOUSBIsocCommand::SetUIMScratch()Removed IOUSBIsocCommand::SetUpdateFrequency()Removed IOUSBIsocCommand::SetUseTimeStamp()Removed IOUSBIsocCommand::SetUSLCompletion()Removed CREATE_EPRemoved DELETE_EPRemoved DEVICE_REQUESTRemoved DEVICE_REQUEST_BUFFERCOMMANDRemoved DEVICE_REQUEST_DESCRemoved INVALID_SELECTORRemoved #def kUSBCommandScratch64BuffersRemoved #def kUSBCommandScratchBuffersRemoved READRemoved usbCommandRemoved WRITE

#### IOKit/usb/IOUSBCompositeDriver.h (Removed)

Removed [IOUSBCompositeDriver](https://developer.apple.com/documentation/kernel/iousbcompositedriver)Removed IOUSBCompositeDriver::CompositeDriverInterestHandler()Removed IOUSBCompositeDriver::ConfigureDevice()Removed IOUSBCompositeDriver::ConfigureDevicePowerManagement()Removed IOUSBCompositeDriver::didTerminate()Removed IOUSBCompositeDriver::FindConfigIndexFromPowerRequirements()Removed IOUSBCompositeDriver::FindConfigIndexFromPreferredConfiguration()Removed IOUSBCompositeDriver::FindConfigIndexFromPreferredInterface()Removed IOUSBCompositeDriver::FindPreferredConfiguration()Removed IOUSBCompositeDriver::free()Removed IOUSBCompositeDriver::GetConfigbmAttributes()Removed IOUSBCompositeDriver::GetConfigDescriptor()Removed IOUSBCompositeDriver::GetConfigValue()Removed IOUSBCompositeDriver::GetExpectingClose()Removed IOUSBCompositeDriver::getMetaClass()Removed IOUSBCompositeDriver::GetNotifier()Removed IOUSBCompositeDriver::init()Removed IOUSBCompositeDriver::message()Removed IOUSBCompositeDriver::ReConfigureDevice()Removed IOUSBCompositeDriver::SetConfiguration()Removed IOUSBCompositeDriver::start()Removed IOUSBCompositeDriver::willTerminate()

#### IOKit/usb/IOUSBController.h (Removed)

Removed AppleUSBHubPortRemoved [IOMemoryDescriptor](https://developer.apple.com/documentation/kernel/iomemorydescriptor)Removed [IOUSBController](https://developer.apple.com/documentation/kernel/iousbcontroller)Removed IOUSBController::AbortPipe()Removed IOUSBController::AcquireDeviceZero()Removed IOUSBController::BulkPacketHandler()Removed IOUSBController::BulkTransaction()Removed IOUSBController::calculateACPIDepth()Removed IOUSBController::calculateUSBDepth()Removed IOUSBController::CheckACPIForPortMapping()Removed IOUSBController::CheckACPIUPCTable()Removed IOUSBController::CheckACPIUPCTableForInternalHubErrataBits()Removed IOUSBController::CheckACPIUPCTableForMuxedMethods()Removed IOUSBController::CheckForDisjointDescriptor()Removed IOUSBController::ClearPipeStall()Removed IOUSBController::ClearRootHubFeature()Removed IOUSBController::ClearRootHubPortFeature()Removed IOUSBController::ClosePipe()Removed IOUSBController::Complete()Removed IOUSBController::CompleteWithTimeStamp()Removed IOUSBController::ConfigureDeviceZero()Removed IOUSBController::ControlPacketHandler()Removed IOUSBController::ControlTransaction()Removed IOUSBController::CopyACPIDevice()Removed IOUSBController::CreateDevice()Removed IOUSBController::CreateRootHubDevice()Removed IOUSBController::DeviceRequest()Removed IOUSBController::didTerminate()Removed IOUSBController::DoAbortEP()Removed IOUSBController::DoClearEPStall()Removed IOUSBController::DoControlTransfer()Removed IOUSBController::DoCreateEP()Removed IOUSBController::DoDeleteEP()Removed IOUSBController::DoIOTransfer()Removed IOUSBController::DoIsocTransfer()Removed IOUSBController::DoLowLatencyIsocTransfer()Removed IOUSBController::DumpUSBACPI()Removed IOUSBController::ExpressCardPort()Removed IOUSBController::finalize()Removed IOUSBController::free()Removed IOUSBController::FreeCommand()Removed IOUSBController::GetBandwidthAvailable()Removed IOUSBController::GetCommandGate()Removed IOUSBController::GetControllerSpeed()Removed IOUSBController::GetDeviceZeroDescriptor()Removed IOUSBController::GetErrataBits()Removed IOUSBController::GetFrameNumber()Removed IOUSBController::GetFrameNumber32()Removed IOUSBController::getMetaClass()Removed IOUSBController::GetNewAddress()Removed IOUSBController::getNubResources()Removed IOUSBController::GetRootHubConfDescriptor()Removed IOUSBController::GetRootHubDescriptor()Removed IOUSBController::GetRootHubDeviceDescriptor()Removed IOUSBController::GetRootHubPortState()Removed IOUSBController::GetRootHubPortStatus()Removed IOUSBController::GetRootHubStatus()Removed IOUSBController::GetRootHubStringDescriptor()Removed IOUSBController::getWorkLoop()Removed IOUSBController::HasExpressCard()Removed IOUSBController::IncreaseCommandPool()Removed IOUSBController::IncreaseIsocCommandPool()Removed IOUSBController::init()Removed IOUSBController::InterruptPacketHandler()Removed IOUSBController::InterruptTransaction()Removed IOUSBController::IsControllerMuxed()Removed IOUSBController::IsocCompletionHandler()Removed IOUSBController::IsocIO()Removed IOUSBController::IsocTransaction()Removed IOUSBController::IsPortInternal()Removed IOUSBController::IsPortMapped()Removed IOUSBController::IsPortMuxed()Removed IOUSBController::LowLatencyIsocCompletionHandler()Removed IOUSBController::LowLatencyIsocTransaction()Removed IOUSBController::MakeDevice()Removed IOUSBController::MakeHubDevice()Removed IOUSBController::message()Removed IOUSBController::OpenPipe()Removed IOUSBController::ParsePCILocation()Removed IOUSBController::PolledRead()Removed IOUSBController::PollInterrupts()Removed IOUSBController::ProtectedDevZeroLock()Removed IOUSBController::Read()Removed IOUSBController::ReleaseDeviceZero()Removed IOUSBController::ResetPipe()Removed IOUSBController::ReturnUSBCommand()Removed IOUSBController::SetDeviceZeroAddress()Removed IOUSBController::SetHubAddress()Removed IOUSBController::SetRootHubDescriptor()Removed IOUSBController::SetRootHubFeature()Removed IOUSBController::SetRootHubPortFeature()Removed IOUSBController::start()Removed IOUSBController::stop()Removed IOUSBController::TerminatePCCard()Removed IOUSBController::UIMAbortEndpoint()Removed IOUSBController::UIMCheckForTimeouts()Removed IOUSBController::UIMClearEndpointStall()Removed IOUSBController::UIMCreateBulkEndpoint()Removed IOUSBController::UIMCreateBulkTransfer()Removed IOUSBController::UIMCreateControlEndpoint()Removed IOUSBController::UIMCreateControlTransfer()Removed IOUSBController::UIMCreateInterruptEndpoint()Removed IOUSBController::UIMCreateInterruptTransfer()Removed IOUSBController::UIMCreateIsochEndpoint()Removed IOUSBController::UIMCreateIsochTransfer()Removed IOUSBController::UIMDeleteEndpoint()Removed IOUSBController::UIMFinalize()Removed IOUSBController::UIMInitialize()Removed IOUSBController::UIMRootHubStatusChange()Removed IOUSBController::ValueOfHexDigit()Removed IOUSBController::WaitForReleaseDeviceZero()Removed IOUSBController::WatchdogTimer()Removed IOUSBController::Write()Removed IOUSBController_ExtraCurrentIOLockClassRemoved [IOUSBHubDevice](https://developer.apple.com/documentation/kernel/iousbhubdevice)Removed [IOUSBLog](https://developer.apple.com/documentation/kernel/iousblog)Removed IOUSBRootHubDeviceRemoved ErrataList64EntryRemoved ErrataList64EntryPtrRemoved ErrataListEntryRemoved ErrataListEntryPtrRemoved IOUSBSyncCompletion()Removed IOUSBSyncIsoCompletion()Removed kErrataAgereEHCIAsyncSchedRemoved kErrataCMDDisableTestModeRemoved kErrataDisableOvercurrentRemoved kErrataDisablePCIeLinkOnSleepRemoved kErrataDontUseCompanionControllerRemoved kErrataEHCIUseRLvalueRemoved kErrataICH6PowerSequencingRemoved kErrataICH7ISTBufferRemoved kErrataIgnoreRootHubPowerClearFeatureRemoved kErratakUHCIResetAfterBabbleRemoved kErrataLSHSOptiRemoved kErrataLucentSuspendResumeRemoved kErrataMCP79IgnoreDisconnectRemoved kErrataMissingPortChangeIntRemoved kErrataNECIncompleteWriteRemoved kErrataNECOHCIIsochWraparoundRemoved kErrataNeedsOvercurrentDebounceRemoved kErrataNeedsPortPowerOffRemoved kErrataNeedsWatchdogTimerRemoved kErrataNoCSonSplitIsochRemoved kErrataOHCINoGlobalSuspendOnSleepRemoved kErrataOnlySinglePageTransfersRemoved kErrataRetryBufferUnderrunsRemoved kErrataSupportsPortResumeEnableRemoved kErrataUHCISupportsOvercurrentRemoved kErrataUHCISupportsResumeDetectOnConnectRemoved kErrataUse32bitEHCIRemoved kErrataXHCIEnableAutoComplianceRemoved kErrataXHCINoMSIRemoved kErrataXHCIPantherPointRemoved kErrataXHCIParkRingRemoved kErrataXHCIPPTMuxingRemoved kErrataXHCISWAssistXHCIIdleRemoved kErrataXHCISWBandwidthCheckRemoved kPCIPMRegBlock_BSERemoved kPCIPMRegBlockCapIDRemoved kPCIPMRegBlockDataRemoved kPCIPMRegBlockNextRemoved kPCIPMRegBlockPMCRemoved kPCIPMRegBlockPMCSRRemoved kUSBWatchdogTimeoutMSRemoved kUSBWatchdogTimeoutMSDuringRestartOffRemoved SleepCurrentPerModelRemoved SleepCurrentPerModelPtrModified [IOUSBDevice](https://developer.apple.com/documentation/kernel/iousbdevice)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBController.h |
| To | Kernel/IOKit/usb/IOUSBUserClient.h |

#### IOKit/usb/IOUSBControllerListElement.h (Removed)

Removed IOUSBControllerIsochEndpointRemoved IOUSBControllerIsochEndpoint::getMetaClass()Removed IOUSBControllerIsochEndpoint::init()Removed IOUSBControllerIsochListElementRemoved IOUSBControllerIsochListElement::Deallocate()Removed IOUSBControllerIsochListElement::getMetaClass()Removed IOUSBControllerIsochListElement::GetPhysicalAddrWithType()Removed IOUSBControllerIsochListElement::GetPhysicalLink()Removed IOUSBControllerIsochListElement::print()Removed IOUSBControllerIsochListElement::SetPhysicalLink()Removed IOUSBControllerIsochListElement::UpdateFrameList()Removed IOUSBControllerListElementRemoved IOUSBControllerListElement::getMetaClass()Removed IOUSBControllerListElement::GetPhysicalAddrWithType()Removed IOUSBControllerListElement::GetPhysicalLink()Removed IOUSBControllerListElement::print()Removed IOUSBControllerListElement::SetPhysicalLink()Removed [IOUSBControllerV2](https://developer.apple.com/documentation/kernel/iousbcontrollerv2)

#### IOKit/usb/IOUSBControllerV2.h (Removed)

Removed [IOUSBControllerV2](https://developer.apple.com/documentation/kernel/iousbcontrollerv2)Removed IOUSBControllerV2::AddHSHub()Removed IOUSBControllerV2::AllocateIsochEP()Removed IOUSBControllerV2::ClearTT()Removed IOUSBControllerV2::clearTTHandler()Removed IOUSBControllerV2::ConfigureDeviceZero()Removed IOUSBControllerV2::CreateDevice()Removed IOUSBControllerV2::CreateIsochronousEndpoint()Removed IOUSBControllerV2::DeallocateIsochEP()Removed IOUSBControllerV2::DoCreateEP()Removed IOUSBControllerV2::DOHSHubMaintenance()Removed IOUSBControllerV2::DOSetTestMode()Removed IOUSBControllerV2::FindIsochronousEndpoint()Removed IOUSBControllerV2::free()Removed IOUSBControllerV2::GatedGetTDfromDoneQueue()Removed IOUSBControllerV2::GetFrameNumberWithTime()Removed IOUSBControllerV2::GetLowLatencyOptionsAndPhysicalMask()Removed IOUSBControllerV2::getMetaClass()Removed IOUSBControllerV2::GetMicroFrameNumber()Removed IOUSBControllerV2::GetNewDMACommand()Removed IOUSBControllerV2::GetTDfromDeferredQueue()Removed IOUSBControllerV2::GetTDfromDoneQueue()Removed IOUSBControllerV2::GetTDfromToDoList()Removed IOUSBControllerV2::init()Removed IOUSBControllerV2::OpenPipe()Removed IOUSBControllerV2::OpenSSPipe()Removed IOUSBControllerV2::PutTDonDeferredQueue()Removed IOUSBControllerV2::PutTDonDoneQueue()Removed IOUSBControllerV2::PutTDonToDoList()Removed IOUSBControllerV2::ReadStream()Removed IOUSBControllerV2::ReadV2()Removed IOUSBControllerV2::RemoveHSHub()Removed IOUSBControllerV2::ReturnIsochDoneQueue()Removed IOUSBControllerV2::ReturnIsochDoneQueueEntry()Removed IOUSBControllerV2::SetTestMode()Removed IOUSBControllerV2::start()Removed IOUSBControllerV2::UIMCreateBulkEndpoint()Removed IOUSBControllerV2::UIMCreateControlEndpoint()Removed IOUSBControllerV2::UIMCreateInterruptEndpoint()Removed IOUSBControllerV2::UIMCreateIsochEndpoint()Removed IOUSBControllerV2::UIMHubMaintenance()Removed IOUSBControllerV2::UIMSetTestMode()Removed IOUSBControllerV2::UpdateDeviceAddress()Removed IOUSBControllerV2::UpdateTopology()Removed IOUSBControllerV2::WriteStream()Removed #def kLowLatencyUSB32bitPhysicalMaskRemoved #def kLowLatencyUSB64bitPhysicalMaskRemoved #def kLowLatencyUSBDefaultOptionBits

#### IOKit/usb/IOUSBControllerV3.h (Removed)

Removed [IOUSBControllerV3](https://developer.apple.com/documentation/kernel/iousbcontrollerv3)Removed IOUSBControllerV3::AbortPipe()Removed IOUSBControllerV3::AcquireDeviceZero()Removed IOUSBControllerV3::AddHSHub()Removed IOUSBControllerV3::AllocateExtraRootHubPortPower()Removed IOUSBControllerV3::AllocatePowerStateArray()Removed IOUSBControllerV3::CanControllerMuxOverToEHCI()Removed IOUSBControllerV3::ChangeExternalDeviceCount()Removed IOUSBControllerV3::CheckForEHCIController()Removed IOUSBControllerV3::CheckForRootHubChanges()Removed IOUSBControllerV3::CheckPMAssertions()Removed IOUSBControllerV3::CheckPowerModeBeforeGatedCall()Removed IOUSBControllerV3::ClearPipeStall()Removed IOUSBControllerV3::ClosePipe()Removed IOUSBControllerV3::ControllerDoze()Removed IOUSBControllerV3::ControllerOff()Removed IOUSBControllerV3::ControllerOn()Removed IOUSBControllerV3::ControllerRestart()Removed IOUSBControllerV3::ControllerSleep()Removed IOUSBControllerV3::CreateStreams()Removed IOUSBControllerV3::DeviceRequest()Removed IOUSBControllerV3::didTerminate()Removed IOUSBControllerV3::DoAbortStream()Removed IOUSBControllerV3::DoCreateStreams()Removed IOUSBControllerV3::DoEnableAddressEndpoints()Removed IOUSBControllerV3::DoEnableAllEndpoints()Removed IOUSBControllerV3::DoGetActualDeviceAddress()Removed IOUSBControllerV3::DoNotPowerOffPortsOnStop()Removed IOUSBControllerV3::DozeController()Removed IOUSBControllerV3::EnableAddressEndpoints()Removed IOUSBControllerV3::EnableAllEndpoints()Removed IOUSBControllerV3::EnableBusMastering()Removed IOUSBControllerV3::EnableInterruptsFromController()Removed IOUSBControllerV3::EnsureUsability()Removed IOUSBControllerV3::FixupNECControllerConfigRegisters()Removed IOUSBControllerV3::free()Removed IOUSBControllerV3::GatedPowerChange()Removed IOUSBControllerV3::GetActualDeviceAddress()Removed IOUSBControllerV3::GetBandwidthAvailableForDevice()Removed IOUSBControllerV3::GetConnectorType()Removed IOUSBControllerV3::GetErrata64Bits()Removed IOUSBControllerV3::GetInternalHubErrataBits()Removed IOUSBControllerV3::getMetaClass()Removed IOUSBControllerV3::GetMinimumIdlePowerState()Removed IOUSBControllerV3::GetPMCSR()Removed IOUSBControllerV3::GetRootHub3Descriptor()Removed IOUSBControllerV3::GetRootHubBOSDescriptor()Removed IOUSBControllerV3::GetRootHubPortErrorCount()Removed IOUSBControllerV3::GetRootHubPowerExitLatencies()Removed IOUSBControllerV3::HandlePowerChange()Removed IOUSBControllerV3::init()Removed IOUSBControllerV3::InitForPM()Removed IOUSBControllerV3::initialPowerStateForDomainState()Removed IOUSBControllerV3::IsControllerAvailable()Removed IOUSBControllerV3::IsocIO()Removed IOUSBControllerV3::maxCapabilityForDomainState()Removed IOUSBControllerV3::OpenPipe()Removed IOUSBControllerV3::PMEHandler()Removed IOUSBControllerV3::powerChangeDone()Removed IOUSBControllerV3::powerStateDidChangeTo()Removed IOUSBControllerV3::powerStateWillChangeTo()Removed IOUSBControllerV3::Read()Removed IOUSBControllerV3::ReadV2()Removed IOUSBControllerV3::ReleaseDeviceZero()Removed IOUSBControllerV3::RemoveHSHub()Removed IOUSBControllerV3::ResetControllerState()Removed IOUSBControllerV3::ResetPipe()Removed IOUSBControllerV3::RestartControllerFromReset()Removed IOUSBControllerV3::RestoreControllerStateFromSleep()Removed IOUSBControllerV3::ReturnExtraRootHubPortPower()Removed IOUSBControllerV3::RHAbortTransaction()Removed IOUSBControllerV3::RHCompleteTransaction()Removed IOUSBControllerV3::RHQueueTransaction()Removed IOUSBControllerV3::RootHubAbortInterruptRead()Removed IOUSBControllerV3::RootHubQueueInterruptRead()Removed IOUSBControllerV3::RootHubStartTimer()Removed IOUSBControllerV3::RootHubStartTimer32()Removed IOUSBControllerV3::RootHubStopTimer()Removed IOUSBControllerV3::RootHubTimerFired()Removed IOUSBControllerV3::SaveControllerStateForSleep()Removed IOUSBControllerV3::setPowerState()Removed IOUSBControllerV3::SetTestMode()Removed IOUSBControllerV3::start()Removed IOUSBControllerV3::stop()Removed IOUSBControllerV3::systemWillShutdown()Removed IOUSBControllerV3::UIMAbortStream()Removed IOUSBControllerV3::UIMCreateSSBulkEndpoint()Removed IOUSBControllerV3::UIMCreateSSInterruptEndpoint()Removed IOUSBControllerV3::UIMCreateSSIsochEndpoint()Removed IOUSBControllerV3::UIMCreateStreams()Removed IOUSBControllerV3::UIMDeviceToBeReset()Removed IOUSBControllerV3::UIMEnableAddressEndpoints()Removed IOUSBControllerV3::UIMEnableAllEndpoints()Removed IOUSBControllerV3::UIMGetActualDeviceAddress()Removed IOUSBControllerV3::UIMMaxSupportedStream()Removed IOUSBControllerV3::UpdateThunderboltExtraCurrentiVars()Removed IOUSBControllerV3::WaitForPCIPauseToFinish()Removed IOUSBControllerV3::WakeControllerFromDoze()Removed IOUSBControllerV3::WakeUpCheckPowerModeThreadsGated()Removed IOUSBControllerV3::willTerminate()Removed IOUSBControllerV3::Write()Removed IOUSBRootHubInterruptTransactionRemoved IOUSBRootHubInterruptTransactionPtrRemoved kCheckPowerModeOptionsUserSpaceRequestMaskRemoved #def kIOThunderboltAppleDisplay2011DMIDRemoved #def kIOThunderboltAppleDVIDRemoved #def kIOThunderboltTunnelEndpointDeviceMIDPropertyRemoved #def kIOThunderboltTunnelEndpointDeviceVIDPropertyRemoved kIOUSBMaxRootHubTransactionsRemoved kMaxEHCIPortsRemoved kMaxTransactionsDuringPCIPauseRemoved kMaxXHCIPortsRemoved kUSBBusStateResetRemoved kUSBBusStateRunningRemoved kUSBBusStateSuspendedRemoved kUSBNumberBusPowerStatesRemoved kUSBPowerStateLowPowerRemoved kUSBPowerStateOffRemoved kUSBPowerStateOnRemoved kUSBPowerStateRestartRemoved kUSBPowerStateSleepRemoved #def kUSBPowerStateStableModified #def kACPIInterruptTypeValid

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBControllerV3.h |
| To | Kernel/IOKit/usb/IOUSBHostFamily.h |

Modified #def kGPEACPIString

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBControllerV3.h |
| To | Kernel/IOKit/usb/IOUSBHostFamily.h |

#### IOKit/usb/IOUSBDevice.h (Removed)

Removed [IOUSBController](https://developer.apple.com/documentation/kernel/iousbcontroller)Removed [IOUSBControllerV2](https://developer.apple.com/documentation/kernel/iousbcontrollerv2)Removed [IOUSBControllerV3](https://developer.apple.com/documentation/kernel/iousbcontrollerv3)Removed [IOUSBDevice](https://developer.apple.com/documentation/kernel/iousbdevice)Removed IOUSBDevice::ChangeGetConfigLock()Removed IOUSBDevice::CreateInterfaceIterator()Removed IOUSBDevice::DeviceRequest()Removed IOUSBDevice::DisplayNotEnoughPowerNotice()Removed IOUSBDevice::DisplayUserNotification()Removed IOUSBDevice::DisplayUserNotificationForDevice()Removed IOUSBDevice::DoLocationOverrideAndModelMatch()Removed IOUSBDevice::DoMessageClients()Removed IOUSBDevice::DoMessageClientsEntry()Removed IOUSBDevice::finalize()Removed IOUSBDevice::FindConfig()Removed IOUSBDevice::FindNextDescriptor()Removed IOUSBDevice::FindNextInterface()Removed IOUSBDevice::FindNextInterfaceDescriptor()Removed IOUSBDevice::free()Removed IOUSBDevice::GetAddress()Removed IOUSBDevice::GetbcdUSB()Removed IOUSBDevice::GetBus()Removed IOUSBDevice::GetBusPowerAvailable()Removed IOUSBDevice::GetChildLocationID()Removed IOUSBDevice::GetConfigDescriptor()Removed IOUSBDevice::GetConfiguration()Removed IOUSBDevice::GetConfigurationDescriptor()Removed IOUSBDevice::GetDeviceClass()Removed IOUSBDevice::GetDeviceDescriptor()Removed IOUSBDevice::GetDeviceInformation()Removed IOUSBDevice::GetDevicePowerParent()Removed IOUSBDevice::GetDeviceRelease()Removed IOUSBDevice::GetDeviceStatus()Removed IOUSBDevice::GetDeviceSubClass()Removed IOUSBDevice::GetExtraPowerAllocated()Removed IOUSBDevice::GetFullConfigurationDescriptor()Removed IOUSBDevice::GetHubParent()Removed IOUSBDevice::GetInterface()Removed IOUSBDevice::GetInterfacePowerParent()Removed IOUSBDevice::GetIsochDelay()Removed IOUSBDevice::GetLocationID()Removed IOUSBDevice::GetManufacturerStringIndex()Removed IOUSBDevice::GetMaxPacketSize()Removed IOUSBDevice::getMetaClass()Removed IOUSBDevice::GetNumConfigurations()Removed IOUSBDevice::GetPipeZero()Removed IOUSBDevice::GetProductID()Removed IOUSBDevice::GetProductStringIndex()Removed IOUSBDevice::GetProtocol()Removed IOUSBDevice::GetSerialNumberStringIndex()Removed IOUSBDevice::GetSpeed()Removed IOUSBDevice::GetStringDescriptor()Removed IOUSBDevice::GetVendorID()Removed IOUSBDevice::handleClose()Removed IOUSBDevice::handleIsOpen()Removed IOUSBDevice::handleOpen()Removed IOUSBDevice::init()Removed IOUSBDevice::IsDeviceInternal()Removed IOUSBDevice::joinPMtree()Removed IOUSBDevice::MakePipe()Removed IOUSBDevice::matchPropertyTable()Removed IOUSBDevice::message()Removed IOUSBDevice::NewDevice()Removed IOUSBDevice::OpenOrCloseAllInterfacePipes()Removed IOUSBDevice::ProcessPortReEnumerate()Removed IOUSBDevice::ProcessPortReEnumerateEntry()Removed IOUSBDevice::ProcessPortReset()Removed IOUSBDevice::ProcessPortResetEntry()Removed IOUSBDevice::ReEnumerateDevice()Removed IOUSBDevice::RegisterInterfaces()Removed IOUSBDevice::ReleaseGetConfigLock()Removed IOUSBDevice::RequestExtraPower()Removed IOUSBDevice::requestTerminate()Removed IOUSBDevice::ResetDevice()Removed IOUSBDevice::ReturnExtraPower()Removed IOUSBDevice::SetAddress()Removed IOUSBDevice::SetBusPowerAvailable()Removed IOUSBDevice::SetConfiguration()Removed IOUSBDevice::SetFeature()Removed IOUSBDevice::SetHubParent()Removed IOUSBDevice::SetIsochDelay()Removed IOUSBDevice::SetPort()Removed IOUSBDevice::SetProperties()Removed IOUSBDevice::SimpleUnicodeToUTF8()Removed IOUSBDevice::start()Removed IOUSBDevice::stop()Removed IOUSBDevice::SuspendDevice()Removed IOUSBDevice::SwapUniWords()Removed IOUSBDevice::TakeGetConfigLock()Removed IOUSBDevice::terminate()Removed IOUSBDevice::TerminateInterfaces()Removed IOUSBDevice::TrimStringDescriptor()Removed IOUSBHubPolicyMakerModified [IOUSBInterface](https://developer.apple.com/documentation/kernel/iousbinterface)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBUserClient.h |

Modified #def kAllowConfigValueOfZero

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBHostDevice.h |

Modified #def kAllowNumConfigsOfZero

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBHostDevice.h |

#### IOKit/usb/IOUSBHIDDriver.h (Removed)

Removed [IOUSBHIDDriver](https://developer.apple.com/documentation/kernel/iousbhiddriver)Removed IOUSBHIDDriver::AbortAndSuspend()Removed IOUSBHIDDriver::ChangeOutstandingIO()Removed IOUSBHIDDriver::CheckForDeadDevice()Removed IOUSBHIDDriver::CheckForDeadDeviceEntry()Removed IOUSBHIDDriver::ClaimPendingRead()Removed IOUSBHIDDriver::ClearFeatureEndpointHalt()Removed IOUSBHIDDriver::ClearFeatureEndpointHaltEntry()Removed IOUSBHIDDriver::DecrementOutstandingIO()Removed IOUSBHIDDriver::didTerminate()Removed IOUSBHIDDriver::free()Removed IOUSBHIDDriver::GetHexChar()Removed IOUSBHIDDriver::GetHIDDescriptor()Removed IOUSBHIDDriver::GetIndexedString()Removed IOUSBHIDDriver::getMaxReportSize()Removed IOUSBHIDDriver::getMetaClass()Removed IOUSBHIDDriver::GetReport()Removed IOUSBHIDDriver::getReport()Removed IOUSBHIDDriver::HandleReport()Removed IOUSBHIDDriver::HandleReportEntry()Removed IOUSBHIDDriver::handleStart()Removed IOUSBHIDDriver::handleStop()Removed IOUSBHIDDriver::IncrementOutstandingIO()Removed IOUSBHIDDriver::init()Removed IOUSBHIDDriver::InitializeUSBHIDPowerManagement()Removed IOUSBHIDDriver::InterruptReadHandler()Removed IOUSBHIDDriver::InterruptReadHandlerEntry()Removed IOUSBHIDDriver::InterruptReadHandlerWithTimeStampEntry()Removed IOUSBHIDDriver::IsPortSuspended()Removed IOUSBHIDDriver::LogMemReport()Removed IOUSBHIDDriver::maxCapabilityForDomainState()Removed IOUSBHIDDriver::message()Removed IOUSBHIDDriver::newCountryCodeNumber()Removed IOUSBHIDDriver::newIndexedString()Removed IOUSBHIDDriver::newLocationIDNumber()Removed IOUSBHIDDriver::newManufacturerString()Removed IOUSBHIDDriver::newProductIDNumber()Removed IOUSBHIDDriver::newProductString()Removed IOUSBHIDDriver::newReportDescriptor()Removed IOUSBHIDDriver::newReportIntervalNumber()Removed IOUSBHIDDriver::newSerialNumberString()Removed IOUSBHIDDriver::newTransportString()Removed IOUSBHIDDriver::newVendorIDNumber()Removed IOUSBHIDDriver::newVersionNumber()Removed IOUSBHIDDriver::powerChangeDone()Removed IOUSBHIDDriver::powerStateDidChangeTo()Removed IOUSBHIDDriver::powerStateWillChangeTo()Removed IOUSBHIDDriver::processPacket()Removed IOUSBHIDDriver::RearmInterruptRead()Removed IOUSBHIDDriver::SetIdleMillisecs()Removed IOUSBHIDDriver::setPowerState()Removed IOUSBHIDDriver::SetProtocol()Removed IOUSBHIDDriver::SetReport()Removed IOUSBHIDDriver::setReport()Removed IOUSBHIDDriver::start()Removed IOUSBHIDDriver::StartFinalProcessing()Removed IOUSBHIDDriver::stop()Removed IOUSBHIDDriver::SuspendPort()Removed IOUSBHIDDriver::SuspendPortTimer()Removed IOUSBHIDDriver::willTerminate()Removed #def HIDMGR2USBREPORTTYPERemoved #def kHIDStandardDriverRetryCountRemoved #def kHIDStandardRetryCountInMSRemoved #def kMaxHIDReportSizeRemoved kUSBHIDNumberPowerStatesRemoved kUSBHIDPowerStateLowPowerRemoved kUSBHIDPowerStateOffRemoved kUSBHIDPowerStateOnRemoved kUSBHIDPowerStateRestartRemoved kUSBHIDPowerStateSleepRemoved #def USB2HIDMGRREPORTTYPEModified #def ENABLE_HIDREPORT_LOGGING

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBHIDDriver.h |
| To | Kernel/IOKit/usb/IOUSBHostHIDDevice.h |

Modified #def kUSBHIDReportLoggingLevel

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBHIDDriver.h |
| To | Kernel/IOKit/usb/IOUSBHostHIDDevice.h |

#### IOKit/usb/IOUSBHostDevice.h (Added)

Added [AppleUSBHostController](https://developer.apple.com/documentation/kernel/appleusbhostcontroller)Added AppleUSBHostDescriptorCacheAdded [AppleUSBHostDeviceIdler](https://developer.apple.com/documentation/kernel/appleusbhostdeviceidler)Added [AppleUSBHostPort](https://developer.apple.com/documentation/kernel/appleusbhostport)Added [AppleUSBHostRequestCompleter](https://developer.apple.com/documentation/kernel/appleusbhostrequestcompleter)Added [AppleUSBHostResources](https://developer.apple.com/documentation/kernel/appleusbhostresources)Added AppleUSBHostSynchronousRequestCompleterAdded [IOUSBHostDevice](https://developer.apple.com/documentation/kernel/iousbhostdevice)Added IOUSBHostDevice::abortDeviceRequests()Added IOUSBHostDevice::abortDeviceRequestsGated()Added IOUSBHostDevice::addPowerChild()Added IOUSBHostDevice::addPowerChildGated()Added IOUSBHostDevice::addPowerChildThreadCall()Added IOUSBHostDevice::allocateDownstreamBusCurrent()Added IOUSBHostDevice::allocateDownstreamBusCurrentGated()Added IOUSBHostDevice::attach()Added IOUSBHostDevice::cacheDescriptor()Added IOUSBHostDevice::cacheDescriptorGated()Added IOUSBHostDevice::close()Added IOUSBHostDevice::closeGated()Added IOUSBHostDevice::compareProperty()Added IOUSBHostDevice::createIOBuffer()Added IOUSBHostDevice::createPipe()Added IOUSBHostDevice::createPipeGated()Added IOUSBHostDevice::deviceRequest()Added IOUSBHostDevice::forcePower()Added IOUSBHostDevice::forcePowerGated()Added IOUSBHostDevice::free()Added IOUSBHostDevice::getAddress()Added IOUSBHostDevice::getCapabilityDescriptors()Added IOUSBHostDevice::getConfigurationDescriptor()Added IOUSBHostDevice::getConfigurationDescriptorWithValue()Added IOUSBHostDevice::getDescriptor()Added IOUSBHostDevice::getDescriptorGated()Added IOUSBHostDevice::getDeviceDescriptor()Added IOUSBHostDevice::getFrameNumber()Added IOUSBHostDevice::getMetaClass()Added IOUSBHostDevice::getPortStatus()Added IOUSBHostDevice::getSpeed()Added IOUSBHostDevice::getStringDescriptor()Added IOUSBHostDevice::handleClose()Added IOUSBHostDevice::handleIsOpen()Added IOUSBHostDevice::handleOpen()Added IOUSBHostDevice::idleAssertion()Added IOUSBHostDevice::initialPowerStateForDomainState()Added IOUSBHostDevice::initWithController()Added IOUSBHostDevice::internalDeviceRequest()Added IOUSBHostDevice::internalDeviceRequestGated()Added IOUSBHostDevice::matchPropertyTable()Added IOUSBHostDevice::message()Added IOUSBHostDevice::open()Added IOUSBHostDevice::openGated()Added IOUSBHostDevice::PMstop()Added IOUSBHostDevice::pmStopThreadCall()Added IOUSBHostDevice::powerChangeDone()Added IOUSBHostDevice::powerStateDidChangeTo()Added IOUSBHostDevice::powerStateDidChangeToGated()Added IOUSBHostDevice::powerStateWillChangeTo()Added IOUSBHostDevice::powerStateWillChangeToGated()Added IOUSBHostDevice::registerPowerService()Added IOUSBHostDevice::removePowerChild()Added IOUSBHostDevice::reset()Added IOUSBHostDevice::setConfiguration()Added IOUSBHostDevice::setConfigurationGated()Added IOUSBHostDevice::setPowerState()Added IOUSBHostDevice::setPowerStateGated()Added IOUSBHostDevice::start()Added IOUSBHostDevice::stop()Added IOUSBHostDevice::stringFromReturn()Added IOUSBHostDevice::terminate()Added IOUSBHostDevice::terminateGated()Added IOUSBHostDevice::updateIdlePolicy()Added IOUSBHostDevice::updateIdlePolicyAsync()Added IOUSBHostDevice::updateIdlePolicyGated()Added IOUSBHostDevice::withController()Added [IOUSBHostInterface](https://developer.apple.com/documentation/kernel/iousbhostinterface)Added #def IOUSBHostFamily_IOUSBHostDevice_hAdded #def kUSBHostDeviceForceSuspendModified #def kAllowConfigValueOfZero

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBHostDevice.h |

Modified #def kAllowNumConfigsOfZero

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBHostDevice.h |

#### IOKit/usb/IOUSBHostFamily.h (Added)

Added #def iokit_usb_codemaskAdded #def iokit_usbhost_errAdded #def iokit_usbhost_groupAdded #def iokit_usbhost_msgAdded #def iokit_usblegacy_err_msgAdded #def iokit_usblegacy_groupAdded #def IOUSBHostFamily_IOUSBHostFamily_hAdded #def kACPIDevicePathKeyAdded #def kAppleCurrentExtraAdded #def kAppleCurrentExtraInSleepAdded #def kAppleExternalConnectorBitmapAdded #def kAppleMaxPortCurrentAdded #def kAppleMaxPortCurrentInSleepAdded [kEndpointDirectionIn](https://developer.apple.com/documentation/kernel/tendpointdirection/kendpointdirectionin)Added [kEndpointDirectionOut](https://developer.apple.com/documentation/kernel/tendpointdirection/kendpointdirectionout)Added [kEndpointDirectionUnknown](https://developer.apple.com/documentation/kernel/tendpointdirection/kendpointdirectionunknown)Added [kEndpointTypeBulk](https://developer.apple.com/documentation/kernel/tendpointtype/kendpointtypebulk)Added [kEndpointTypeControl](https://developer.apple.com/documentation/kernel/tendpointtype/kendpointtypecontrol)Added [kEndpointTypeInterrupt](https://developer.apple.com/documentation/kernel/tendpointtype/kendpointtypeinterrupt)Added [kEndpointTypeIsochronous](https://developer.apple.com/documentation/kernel/tendpointtype/kendpointtypeisochronous)Added #def kGetBehaviorACPIMethodAdded #def kRDYForGPIOTestAdded #def kReconfiguredCountAdded [kRequestDirectionIn](https://developer.apple.com/documentation/kernel/tdevicerequestdirection/krequestdirectionin)Added [kRequestDirectionOut](https://developer.apple.com/documentation/kernel/tdevicerequestdirection/krequestdirectionout)Added [kRequestRecipientDevice](https://developer.apple.com/documentation/kernel/tdevicerequestrecipient/krequestrecipientdevice)Added [kRequestRecipientEndpoint](https://developer.apple.com/documentation/kernel/tdevicerequestrecipient/krequestrecipientendpoint)Added [kRequestRecipientInterface](https://developer.apple.com/documentation/kernel/tdevicerequestrecipient/krequestrecipientinterface)Added [kRequestRecipientOther](https://developer.apple.com/documentation/kernel/tdevicerequestrecipient/krequestrecipientother)Added [kRequestTypeClass](https://developer.apple.com/documentation/kernel/tdevicerequesttype/krequesttypeclass)Added [kRequestTypeStandard](https://developer.apple.com/documentation/kernel/tdevicerequesttype/krequesttypestandard)Added [kRequestTypeVendor](https://developer.apple.com/documentation/kernel/tdevicerequesttype/krequesttypevendor)Added #def kSDControllerCaptiveUSB3ReaderKeyAdded #def kSDControllerGPIOPowerACPIMethodAdded #def kSDControllerGPIOResetACPIMethodAdded #def kSDControllerGPIOResetPropertyKeyAdded #def kSDPortConnectionBehaviorACPIMethodAdded [#def kUSBExpressCardCantWake](https://developer.apple.com/documentation/iokit/kusbexpresscardcantwake)Added #def kUSBHostACPIPropertyMultiplexorAdded #def kUSBHostACPIPropertyXHCICompanionAdded [kUSBHostClassRequestCompletionTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostclassrequestcompletiontimeout)Added [kUSBHostClassRequestNoDataTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostclassrequestnodatatimeout)Added [kUSBHostConnectionSpeedCount](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedcount)Added [kUSBHostConnectionSpeedFull](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedfull)Added [kUSBHostConnectionSpeedHigh](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedhigh)Added [kUSBHostConnectionSpeedLow](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedlow)Added [kUSBHostConnectionSpeedSuper](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedsuper)Added [kUSBHostConnectorTypeA](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypea)Added [kUSBHostConnectorTypeExpressCard](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeexpresscard)Added [kUSBHostConnectorTypeMiniAB](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeminiab)Added [kUSBHostConnectorTypeProprietary](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeproprietary)Added [kUSBHostConnectorTypeUnknown](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeunknown)Added [kUSBHostConnectorTypeUSB3A](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusb3a)Added [kUSBHostConnectorTypeUSB3B](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusb3b)Added [kUSBHostConnectorTypeUSB3MicroAB](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusb3microab)Added [kUSBHostConnectorTypeUSB3MicroB](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusb3microb)Added [kUSBHostConnectorTypeUSB3PowerB](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusb3powerb)Added #def kUSBHostControllerPropertyCompanionAdded #def kUSBHostControllerPropertyDebugErrorAdded #def kUSBHostControllerPropertyFullSpeedCompanionAdded #def kUSBHostControllerPropertyHighSpeedCompanionAdded #def kUSBHostControllerPropertyIsochronousRequiresContiguousAdded #def kUSBHostControllerPropertyLowSpeedCompanionAdded #def kUSBHostControllerPropertyMuxEnabledAdded #def kUSBHostControllerPropertySleepSupportedAdded #def kUSBHostControllerPropertySuperSpeedCompanionAdded [kUSBHostDefaultControlCompletionTimeoutMS](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostdefaultcontrolcompletiontimeoutms)Added [kUSBHostDefaultControlNoDataTimeoutMS](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostdefaultcontrolnodatatimeoutms)Added #def kUSBHostDevicePropertyConfigurationCurrentOverrideAdded #def kUSBHostDevicePropertyConfigurationDescriptorOverrideAdded #def kUSBHostDevicePropertyContainerIDAdded #def kUSBHostDevicePropertyCurrentConfigurationAdded #def kUSBHostDevicePropertyFailedRequestedPowerAdded #def kUSBHostDevicePropertyPreferredConfigurationAdded #def kUSBHostDevicePropertyRemoteWakeOverrideAdded #def kUSBHostDevicePropertyResetDurationOverrideAdded #def kUSBHostDevicePropertyResumeRecoveryTimeAdded #def kUSBHostDevicePropertySerialNumberStringAdded #def kUSBHostDevicePropertyVendorStringAdded [kUSBHostHubClass](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhosthubclass)Added #def kUSBHostHubPropertyIdlePolicyAdded #def kUSBHostHubPropertyPortSequenceDelayAdded #def kUSBHostHubPropertyPowerSupplyAdded #def kUSBHostHubPropertyStartupDelayAdded #def kUSBHostInterfacePropertyAlternateSettingAdded #def kUSBHostMatchingPropertyConfigurationValueAdded #def kUSBHostMatchingPropertyDeviceClassAdded #def kUSBHostMatchingPropertyDeviceProtocolAdded #def kUSBHostMatchingPropertyDeviceReleaseNumberAdded #def kUSBHostMatchingPropertyDeviceSubClassAdded #def kUSBHostMatchingPropertyInterfaceClassAdded #def kUSBHostMatchingPropertyInterfaceNumberAdded #def kUSBHostMatchingPropertyInterfaceProtocolAdded #def kUSBHostMatchingPropertyInterfaceSubClassAdded #def kUSBHostMatchingPropertyPortTypeAdded #def kUSBHostMatchingPropertyProductIDAdded #def kUSBHostMatchingPropertyProductIDArrayAdded #def kUSBHostMatchingPropertyProductIDMaskAdded #def kUSBHostMatchingPropertySpeedAdded #def kUSBHostMatchingPropertyVendorIDAdded [kUSBHostMaxCountFullSpeedIsochronous](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhostmaxcountfullspeedisochronous)Added [kUSBHostMaxDevices](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhostmaxdevices)Added [kUSBHostMaxPipes](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhostmaxpipes)Added #def kUSBHostMessageConfigurationSetAdded #def kUSBHostMessageDeviceConnectedAdded #def kUSBHostMessageDeviceCountExceededAdded #def kUSBHostMessageDeviceDisconnectedAdded #def kUSBHostMessageDeviceResumeAdded #def kUSBHostMessageDeviceSuspendAdded #def kUSBHostMessageEndpointCountExceededAdded #def kUSBHostMessageHubCountExceededAdded #def kUSBHostMessageNotEnoughPowerAdded #def kUSBHostMessageOvercurrentConditionAdded #def kUSBHostMessagePortsCreatedAdded #def kUSBHostMessageRemoteWakeAdded #def kUSBHostMessageRenegotiateCurrentAdded #def kUSBHostMessageTDMLowBatteryAdded #def kUSBHostMessageUnsupportedConfigurationAdded #def kUSBHostMessageUpdateIdlePolicyAdded [kUSBHostPortConnectable](https://developer.apple.com/documentation/kernel/tusbhostportconnectable/kusbhostportconnectable)Added [kUSBHostPortConnectionSpeedCount](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedcount)Added [kUSBHostPortConnectionSpeedFull](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedfull)Added [kUSBHostPortConnectionSpeedHigh](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedhigh)Added [kUSBHostPortConnectionSpeedLow](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedlow)Added [kUSBHostPortConnectionSpeedNone](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeednone)Added [kUSBHostPortConnectionSpeedSuper](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedsuper)Added [kUSBHostPortNotConnectable](https://developer.apple.com/documentation/kernel/tusbhostportconnectable/kusbhostportnotconnectable)Added #def kUSBHostPortPropertyBusCurrentAllocationAdded #def kUSBHostPortPropertyBusCurrentSleepAllocationAdded #def kUSBHostPortPropertyCardReaderAdded #def kUSBHostPortPropertyCompanionIndexAdded #def kUSBHostPortPropertyConnectableAdded #def kUSBHostPortPropertyConnectorTypeAdded #def kUSBHostPortPropertyExternalDevicePowerControllerAdded #def kUSBHostPortPropertyExternalDeviceResetControllerAdded #def kUSBHostPortPropertyMuxAdded #def kUSBHostPortPropertyOffsetAdded #def kUSBHostPortPropertyPortNumberAdded #def kUSBHostPortPropertyRemovableAdded #def kUSBHostPortPropertySimulateInterruptAdded #def kUSBHostPortPropertyTestModeAdded [kUSBHostPortStatusConnectedSpeedFull](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedfull)Added [kUSBHostPortStatusConnectedSpeedHigh](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedhigh)Added [kUSBHostPortStatusConnectedSpeedLow](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedlow)Added [kUSBHostPortStatusConnectedSpeedMask](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedmask)Added [kUSBHostPortStatusConnectedSpeedNone](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeednone)Added [kUSBHostPortStatusConnectedSpeedPhase](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedphase)Added [kUSBHostPortStatusConnectedSpeedSuper](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedsuper)Added [kUSBHostPortStatusEnabled](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusenabled)Added [kUSBHostPortStatusOvercurrent](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusovercurrent)Added [kUSBHostPortStatusPortTypeAccessory](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypeaccessory)Added [kUSBHostPortStatusPortTypeCaptive](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypecaptive)Added [kUSBHostPortStatusPortTypeInternal](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypeinternal)Added [kUSBHostPortStatusPortTypeMask](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypemask)Added [kUSBHostPortStatusPortTypePhase](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypephase)Added [kUSBHostPortStatusPortTypeReserved](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypereserved)Added [kUSBHostPortStatusPortTypeStandard](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusporttypestandard)Added [kUSBHostPortStatusResetting](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusresetting)Added [kUSBHostPortStatusSuspended](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatussuspended)Added [kUSBHostPortStatusTestMode](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatustestmode)Added [kUSBHostPortTypeAccessory](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypeaccessory)Added [kUSBHostPortTypeCaptive](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypecaptive)Added [kUSBHostPortTypeCount](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypecount)Added [kUSBHostPortTypeInternal](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypeinternal)Added [kUSBHostPortTypeStandard](https://developer.apple.com/documentation/kernel/tusbhostporttype/kusbhostporttypestandard)Added #def kUSBHostPropertyDataToggleResetOverrideAdded #def kUSBHostPropertyDebugOptionsAdded #def kUSBHostPropertyFailedRemoteWakeAdded #def kUSBHostPropertyLocationIDAdded #def kUSBHostPropertySleepPortCurrentLimitAdded #def kUSBHostPropertySleepPowerSupplyAdded #def kUSBHostPropertyWakePortCurrentLimitAdded #def kUSBHostPropertyWakePowerSupplyAdded #def kUSBHostReturnNoPowerAdded #def kUSBHostReturnPipeStalledAdded [kUSBHostSetAddressTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostsetaddresstimeout)Added [kUSBHostStandardRequestCompletionTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhoststandardrequestcompletiontimeout)Added [kUSBHostStandardRequestNoDataTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhoststandardrequestnodatatimeout)Added [kUSBHostStandardRequestSimpleCompletionTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhoststandardrequestsimplecompletiontimeout)Added [kUSBHostVendorIDAppleComputer](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhostvendoridapplecomputer)Added [kUSBHostVendorRequestCompletionTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostvendorrequestcompletiontimeout)Added [kUSBHostVendorRequestNoDataTimeout](https://developer.apple.com/documentation/kernel/1645795-anonymous/kusbhostvendorrequestnodatatimeout)Added [kUSBHostVendorSpecificClass](https://developer.apple.com/documentation/kernel/1645794-anonymous/kusbhostvendorspecificclass)Added #def kUSBPlatformPropertiesAdded [makeDeviceRequestbmRequestType()](https://developer.apple.com/documentation/kernel/1579500-makedevicerequestbmrequesttype)Added [tDeviceRequestDirection](https://developer.apple.com/documentation/kernel/tdevicerequestdirection)Added [tDeviceRequestRecipient](https://developer.apple.com/documentation/kernel/tdevicerequestrecipient)Added [tDeviceRequestType](https://developer.apple.com/documentation/kernel/tdevicerequesttype)Added [tEndpointDirection](https://developer.apple.com/documentation/kernel/tendpointdirection)Added [tEndpointType](https://developer.apple.com/documentation/kernel/tendpointtype)Added [tUSBHostConnectionSpeed](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed)Added [tUSBHostConnectorType](https://developer.apple.com/documentation/kernel/tusbhostconnectortype)Added [tUSBHostDeviceAddress](https://developer.apple.com/documentation/kernel/tusbhostdeviceaddress)Added [tUSBHostPortConnectable](https://developer.apple.com/documentation/kernel/tusbhostportconnectable)Added [tUSBHostPortStatus](https://developer.apple.com/documentation/kernel/tusbhostportstatus)Added [tUSBHostPortType](https://developer.apple.com/documentation/kernel/tusbhostporttype)Modified #def kACPIInterruptTypeValid

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBControllerV3.h |
| To | Kernel/IOKit/usb/IOUSBHostFamily.h |

Modified #def kGPEACPIString

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBControllerV3.h |
| To | Kernel/IOKit/usb/IOUSBHostFamily.h |

#### IOKit/usb/IOUSBHostHIDDevice.h (Added)

Added IOUSBHostHIDDeviceAdded IOUSBHostHIDDevice::free()Added IOUSBHostHIDDevice::getHidDescriptor()Added IOUSBHostHIDDevice::getHidDescriptorGated()Added IOUSBHostHIDDevice::getMaxReportSize()Added IOUSBHostHIDDevice::getMetaClass()Added IOUSBHostHIDDevice::getReport()Added IOUSBHostHIDDevice::getStringAtIndex()Added IOUSBHostHIDDevice::handleStart()Added IOUSBHostHIDDevice::interruptReadComplete()Added IOUSBHostHIDDevice::interruptRetry()Added IOUSBHostHIDDevice::newCountryCodeNumber()Added IOUSBHostHIDDevice::newIndexedString()Added IOUSBHostHIDDevice::newLocationIDNumber()Added IOUSBHostHIDDevice::newManufacturerString()Added IOUSBHostHIDDevice::newProductIDNumber()Added IOUSBHostHIDDevice::newProductString()Added IOUSBHostHIDDevice::newReportDescriptor()Added IOUSBHostHIDDevice::newSerialNumberString()Added IOUSBHostHIDDevice::newTransportString()Added IOUSBHostHIDDevice::newVendorIDNumber()Added IOUSBHostHIDDevice::newVersionNumber()Added IOUSBHostHIDDevice::readInterruptPipeAsync()Added IOUSBHostHIDDevice::readInterruptPipeAsyncGated()Added IOUSBHostHIDDevice::SetIdleMillisecs()Added IOUSBHostHIDDevice::setProtocol()Added IOUSBHostHIDDevice::setReport()Added IOUSBHostHIDDevice::setReportComplete()Added IOUSBHostHIDDevice::start()Added IOUSBHostHIDDevice::stop()Added IOUSBHostHIDDevice::willTerminate()Added IOUSBHostHIDDevice::zlpWriteComplete()Added #def HID_MGR_2_USB_REPORT_TYPEAdded IOUSBHostHIDDescriptorAdded IOUSBHostHIDReportDescriptorAdded [kHIDBootProtocolValue](https://developer.apple.com/documentation/kernel/1643535-anonymous/khidbootprotocolvalue)Added #def kHIDDriverRetryCountAdded [kHIDKeyboardInterfaceProtocol](https://developer.apple.com/documentation/kernel/1643508-anonymous/khidkeyboardinterfaceprotocol)Added [kHIDMouseInterfaceProtocol](https://developer.apple.com/documentation/kernel/1643508-anonymous/khidmouseinterfaceprotocol)Added [kHIDNoInterfaceProtocol](https://developer.apple.com/documentation/kernel/1643508-anonymous/khidnointerfaceprotocol)Added [kHIDReportProtocolValue](https://developer.apple.com/documentation/kernel/1643535-anonymous/khidreportprotocolvalue)Added [kHIDRqGetIdle](https://developer.apple.com/documentation/iokit/1424744-hid_requests/khidrqgetidle)Added [kHIDRqGetProtocol](https://developer.apple.com/documentation/kernel/1643521-anonymous/khidrqgetprotocol)Added [kHIDRqGetReport](https://developer.apple.com/documentation/iokit/1424744-hid_requests/khidrqgetreport)Added [kHIDRqSetIdle](https://developer.apple.com/documentation/kernel/1643521-anonymous/khidrqsetidle)Added [kHIDRqSetProtocol](https://developer.apple.com/documentation/kernel/1643521-anonymous/khidrqsetprotocol)Added [kHIDRqSetReport](https://developer.apple.com/documentation/kernel/1643521-anonymous/khidrqsetreport)Added [kHIDRtFeatureReport](https://developer.apple.com/documentation/kernel/1643519-anonymous/khidrtfeaturereport)Added [kHIDRtInputReport](https://developer.apple.com/documentation/kernel/1643519-anonymous/khidrtinputreport)Added [kHIDRtOutputReport](https://developer.apple.com/documentation/kernel/1643519-anonymous/khidrtoutputreport)Added kInterruptRetriesAdded #def kUSBHID_DeviceIdleTimeoutAdded #def kUSBHID_IoIdleTimeoutAdded [kUSBHIDBootInterfaceSubClass](https://developer.apple.com/documentation/kernel/1643510-anonymous/kusbhidbootinterfacesubclass)Added [kUSBHIDClass](https://developer.apple.com/documentation/kernel/1643512-anonymous/kusbhidclass)Added [kUSBHIDDesc](https://developer.apple.com/documentation/kernel/1643537-anonymous/kusbhiddesc)Added [kUSBHIDInterfaceClass](https://developer.apple.com/documentation/iokit/1424756-interface_class/kusbhidinterfaceclass)Added [kUSBReportDesc](https://developer.apple.com/documentation/iokit/1424957-usb_descriptors/kusbreportdesc)Added [kUSBVendorSpecificProtocol](https://developer.apple.com/documentation/kernel/1643508-anonymous/kusbvendorspecificprotocol)Added #def USB_2_HID_MGR_REPORT_TYPEModified #def ENABLE_HIDREPORT_LOGGING

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBHIDDriver.h |
| To | Kernel/IOKit/usb/IOUSBHostHIDDevice.h |

Modified #def kUSBHIDReportLoggingLevel

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBHIDDriver.h |
| To | Kernel/IOKit/usb/IOUSBHostHIDDevice.h |

#### IOKit/usb/IOUSBHostInterface.h (Added)

Added [IOUSBHostInterface](https://developer.apple.com/documentation/kernel/iousbhostinterface)Added IOUSBHostInterface::abortDeviceRequests()Added IOUSBHostInterface::attach()Added IOUSBHostInterface::close()Added IOUSBHostInterface::closeGated()Added IOUSBHostInterface::closePipes()Added IOUSBHostInterface::closePipesGated()Added IOUSBHostInterface::compareProperty()Added IOUSBHostInterface::copyPipe()Added IOUSBHostInterface::copyPipeGated()Added IOUSBHostInterface::createIOBuffer()Added IOUSBHostInterface::deviceRequest()Added IOUSBHostInterface::free()Added IOUSBHostInterface::getConfigurationDescriptor()Added IOUSBHostInterface::getDevice()Added IOUSBHostInterface::getFrameNumber()Added IOUSBHostInterface::getIdlePolicy()Added IOUSBHostInterface::getInterfaceDescriptor()Added IOUSBHostInterface::getInterfaceDescriptorGated()Added IOUSBHostInterface::getMetaClass()Added IOUSBHostInterface::getPortStatus()Added IOUSBHostInterface::getStringDescriptor()Added IOUSBHostInterface::initWithDescriptors()Added IOUSBHostInterface::matchPropertyTable()Added IOUSBHostInterface::message()Added IOUSBHostInterface::open()Added IOUSBHostInterface::openGated()Added IOUSBHostInterface::pipeLockLock()Added IOUSBHostInterface::pipeLockUnlock()Added IOUSBHostInterface::selectAlternateSetting()Added IOUSBHostInterface::selectAlternateSettingGated()Added IOUSBHostInterface::setIdlePolicy()Added IOUSBHostInterface::start()Added IOUSBHostInterface::stop()Added IOUSBHostInterface::stringFromReturn()Added IOUSBHostInterface::terminate()Added IOUSBHostInterface::updateMatchingProperties()Added IOUSBHostInterface::withDescriptors()Added #def IOUSBHostFamily_IOUSBHostInterface_h

#### IOKit/usb/IOUSBHostIOSource.h (Added)

Added [AppleUSBHostController](https://developer.apple.com/documentation/kernel/appleusbhostcontroller)Added AppleUSBHostRequestPoolAdded [IOUSBHostDevice](https://developer.apple.com/documentation/kernel/iousbhostdevice)Added [IOUSBHostIOSource](https://developer.apple.com/documentation/kernel/iousbhostiosource)Added IOUSBHostIOSource::abort()Added IOUSBHostIOSource::abortGated()Added IOUSBHostIOSource::close()Added IOUSBHostIOSource::closeGated()Added IOUSBHostIOSource::free()Added IOUSBHostIOSource::getMetaClass()Added IOUSBHostIOSource::getState()Added IOUSBHostIOSource::getStateGated()Added IOUSBHostIOSource::initWithOwners()Added IOUSBHostIOSource::io()Added IOUSBHostIOSource::ioGated()Added IOUSBHostIOSource::synchronousCompletion()Added IOUSBHostIOSource::synchronousIsochronousCompletion()Added IOUSBHostIOSource::timerCompletion()Added [IOUSBHostCompletion](https://developer.apple.com/documentation/kernel/iousbhostcompletion)Added [IOUSBHostCompletionAction](https://developer.apple.com/documentation/kernel/iousbhostcompletionaction)Added #def IOUSBHostFamily_IOUSBHostIOSource_hAdded [IOUSBHostIsochronousCompletion](https://developer.apple.com/documentation/kernel/iousbhostisochronouscompletion)Added [IOUSBHostIsochronousCompletionAction](https://developer.apple.com/documentation/kernel/iousbhostisochronouscompletionaction)Added [IOUSBHostIsochronousFrame](https://developer.apple.com/documentation/kernel/iousbhostisochronousframe)

#### IOKit/usb/IOUSBHostPipe.h (Added)

Added [AppleUSBHostController](https://developer.apple.com/documentation/kernel/appleusbhostcontroller)Added [IOUSBHostInterface](https://developer.apple.com/documentation/kernel/iousbhostinterface)Added [IOUSBHostPipe](https://developer.apple.com/documentation/kernel/iousbhostpipe)Added IOUSBHostPipe::abort()Added IOUSBHostPipe::abortGated()Added IOUSBHostPipe::adjustPipe()Added IOUSBHostPipe::adjustPipeGated()Added IOUSBHostPipe::clearStall()Added IOUSBHostPipe::clearStallGated()Added IOUSBHostPipe::closeGated()Added IOUSBHostPipe::controlRequest()Added IOUSBHostPipe::controlRequestGated()Added IOUSBHostPipe::copyStream()Added IOUSBHostPipe::copyStreamGated()Added IOUSBHostPipe::disableStreams()Added IOUSBHostPipe::disableStreamsGated()Added IOUSBHostPipe::enableStreams()Added IOUSBHostPipe::enableStreamsGated()Added IOUSBHostPipe::free()Added IOUSBHostPipe::getDeviceAddress()Added IOUSBHostPipe::getEndpointDescriptor()Added IOUSBHostPipe::getIdlePolicy()Added IOUSBHostPipe::getIdlePolicyGated()Added IOUSBHostPipe::getMetaClass()Added IOUSBHostPipe::getSpeed()Added IOUSBHostPipe::getSuperSpeedEndpointCompanionDescriptor()Added IOUSBHostPipe::initWithDescriptorsAndOwners()Added IOUSBHostPipe::io()Added IOUSBHostPipe::isochronousIoGated()Added IOUSBHostPipe::rawBufferControlRequestCompletion()Added IOUSBHostPipe::setIdlePolicy()Added IOUSBHostPipe::setIdlePolicyGated()Added IOUSBHostPipe::withDescriptorsAndOwners()Added #def IOUSBHostFamily_IOUSBHostPipe_h

#### IOKit/usb/IOUSBHostStream.h (Added)

Added [IOUSBHostPipe](https://developer.apple.com/documentation/kernel/iousbhostpipe)Added [IOUSBHostStream](https://developer.apple.com/documentation/kernel/iousbhoststream)Added IOUSBHostStream::abort()Added IOUSBHostStream::abortGated()Added IOUSBHostStream::closeGated()Added IOUSBHostStream::free()Added IOUSBHostStream::getMetaClass()Added IOUSBHostStream::getPipe()Added IOUSBHostStream::getStreamID()Added IOUSBHostStream::initWithOwnersAndStreamID()Added IOUSBHostStream::io()Added IOUSBHostStream::withOwnersAndStreamID()Added #def IOUSBHostFamily_IOUSBHostStream_h

#### IOKit/usb/IOUSBHubDevice.h (Removed)

Removed [IOUSBHubDevice](https://developer.apple.com/documentation/kernel/iousbhubdevice)Removed IOUSBHubDevice::free()Removed IOUSBHubDevice::GetHubCharacteristics()Removed IOUSBHubDevice::GetMaxProvidedPower()Removed IOUSBHubDevice::getMetaClass()Removed IOUSBHubDevice::GetPolicyMaker()Removed IOUSBHubDevice::GetSleepCurrent()Removed IOUSBHubDevice::GetTotalSleepCurrent()Removed IOUSBHubDevice::init()Removed IOUSBHubDevice::InitializeCharacteristics()Removed IOUSBHubDevice::InitializeExtraPower()Removed IOUSBHubDevice::NewHubDevice()Removed IOUSBHubDevice::RequestExtraPower()Removed IOUSBHubDevice::RequestExtraWakePowerGated()Removed IOUSBHubDevice::RequestProvidedPower()Removed IOUSBHubDevice::RequestSleepPower()Removed IOUSBHubDevice::RequestSleepPowerGated()Removed IOUSBHubDevice::ReturnExtraPower()Removed IOUSBHubDevice::ReturnExtraWakePowerGated()Removed IOUSBHubDevice::ReturnSleepPower()Removed IOUSBHubDevice::ReturnSleepPowerGated()Removed IOUSBHubDevice::SendExtraPowerMessage()Removed IOUSBHubDevice::SetHubCharacteristics()Removed IOUSBHubDevice::SetPolicyMaker()Removed IOUSBHubDevice::SetSleepCurrent()Removed IOUSBHubDevice::SetTotalSleepCurrent()Removed IOUSBHubDevice::start()Removed IOUSBHubDevice::stop()Removed IOUSBHubDevice::UpdateUnconnectedExternalPorts()Removed IOUSBHubDevice::UpdateUnconnectedExternalPortsGated()Removed IOUSBHubPolicyMakerRemoved kIOUSBHubDeviceCanSleepRemoved kIOUSBHubDeviceIsOnHighSpeedBusRemoved kIOUSBHubDeviceIsOnSuperSpeedBusRemoved kIOUSBHubDeviceIsRootHub

#### IOKit/usb/IOUSBHubPolicyMaker.h (Removed)

Removed IOUSBHubPolicyMakerRemoved IOUSBHubPolicyMaker::AllocateExtraPower()Removed IOUSBHubPolicyMaker::ConfigureHubDriver()Removed IOUSBHubPolicyMaker::EnsureUsability()Removed IOUSBHubPolicyMaker::GetExtraPortPower()Removed IOUSBHubPolicyMaker::getMetaClass()Removed IOUSBHubPolicyMaker::GetMinimumIdlePowerState()Removed IOUSBHubPolicyMaker::GetPortInformation()Removed IOUSBHubPolicyMaker::GetPowerExitLatencies()Removed IOUSBHubPolicyMaker::HubPowerChange()Removed IOUSBHubPolicyMaker::maxCapabilityForDomainState()Removed IOUSBHubPolicyMaker::powerChangeDone()Removed IOUSBHubPolicyMaker::powerStateDidChangeTo()Removed IOUSBHubPolicyMaker::powerStateForDomainState()Removed IOUSBHubPolicyMaker::powerStateWillChangeTo()Removed IOUSBHubPolicyMaker::ProcessUSBNotification()Removed IOUSBHubPolicyMaker::ReEnumeratePort()Removed IOUSBHubPolicyMaker::RequestExtraPower()Removed IOUSBHubPolicyMaker::ResetPort()Removed IOUSBHubPolicyMaker::ReturnExtraPortPower()Removed IOUSBHubPolicyMaker::ReturnExtraPower()Removed IOUSBHubPolicyMaker::setPowerState()Removed IOUSBHubPolicyMaker::start()Removed IOUSBHubPolicyMaker::stop()Removed IOUSBHubPolicyMaker::SuspendPort()Removed IOUSBHubExitLatenciesRemoved IOUSBHubExitLatencyStatesRemoved kHubResumeRecoveryTimeRemoved #def kIOUSBHubExitLatenciesVersionRemoved #def kIOUSBHubExitLatencyMaxRemoved kIOUSBHubNumberPowerStatesRemoved kIOUSBHubPowerStateLowPowerRemoved kIOUSBHubPowerStateOffRemoved kIOUSBHubPowerStateOnRemoved kIOUSBHubPowerStateRestartRemoved kIOUSBHubPowerStateSleepRemoved #def kIOUSBHubPowerStateStableRemoved kPortResumeRecoveryTime

#### IOKit/usb/IOUSBInterface.h (Removed)

Removed [IOUSBInterface](https://developer.apple.com/documentation/kernel/iousbinterface)Removed IOUSBInterface::AbortPipesGated()Removed IOUSBInterface::CalculateFullMaxPacketSize()Removed IOUSBInterface::CallSuperClose()Removed IOUSBInterface::CallSuperOpen()Removed IOUSBInterface::close()Removed IOUSBInterface::ClosePipes()Removed IOUSBInterface::ClosePipesGated()Removed IOUSBInterface::CreatePipes()Removed IOUSBInterface::DeviceRequest()Removed IOUSBInterface::EnableRemoteWake()Removed IOUSBInterface::finalize()Removed IOUSBInterface::FindNextAltInterface()Removed IOUSBInterface::FindNextAssociatedDescriptor()Removed IOUSBInterface::FindNextPipe()Removed IOUSBInterface::FindNextPipeGated()Removed IOUSBInterface::free()Removed IOUSBInterface::GetAlternateSetting()Removed IOUSBInterface::GetConfigValue()Removed IOUSBInterface::GetDevice()Removed IOUSBInterface::GetEndpointProperties()Removed IOUSBInterface::GetEndpointPropertiesV3()Removed IOUSBInterface::GetInterfaceClass()Removed IOUSBInterface::GetInterfaceNumber()Removed IOUSBInterface::GetInterfaceProtocol()Removed IOUSBInterface::GetInterfaceStatus()Removed IOUSBInterface::GetInterfaceStringIndex()Removed IOUSBInterface::GetInterfaceSubClass()Removed IOUSBInterface::getMetaClass()Removed IOUSBInterface::GetNumEndpoints()Removed IOUSBInterface::GetPipeObj()Removed IOUSBInterface::GetPipeObjGated()Removed IOUSBInterface::handleClose()Removed IOUSBInterface::handleIsOpen()Removed IOUSBInterface::handleOpen()Removed IOUSBInterface::hex2char()Removed IOUSBInterface::init()Removed IOUSBInterface::joinPMtree()Removed IOUSBInterface::matchPropertyTable()Removed IOUSBInterface::message()Removed IOUSBInterface::open()Removed IOUSBInterface::RecreateStreams()Removed IOUSBInterface::RecreateStreamsGated()Removed IOUSBInterface::RememberStreams()Removed IOUSBInterface::RememberStreamsGated()Removed IOUSBInterface::ReopenPipes()Removed IOUSBInterface::ReopenPipesGated()Removed IOUSBInterface::ResetPipes()Removed IOUSBInterface::SetAlternateInterface()Removed IOUSBInterface::SetFunctionSuspendFeature()Removed IOUSBInterface::SetProperties()Removed IOUSBInterface::start()Removed IOUSBInterface::stop()Removed IOUSBInterface::terminate()Removed IOUSBInterface::UnlinkPipes()Removed IOUSBInterface::withDescriptors()

#### IOKit/usb/IOUSBMassStorageClass.h

Removed IOUSBMassStorageClassRemoved IOUSBMassStorageClass::AbortCurrentSCSITask()Removed IOUSBMassStorageClass::AbortSCSICommand()Removed IOUSBMassStorageClass::AbortSCSICommandForBulkOnlyProtocol()Removed IOUSBMassStorageClass::AbortSCSICommandForCBIProtocol()Removed IOUSBMassStorageClass::AcceptSCSITask()Removed IOUSBMassStorageClass::BeginProvidedServices()Removed IOUSBMassStorageClass::BulkDeviceResetDevice()Removed IOUSBMassStorageClass::BulkOnlyExecuteCommandCompletion()Removed IOUSBMassStorageClass::BulkOnlyReceiveCSWPacket()Removed IOUSBMassStorageClass::BulkOnlySendCBWPacket()Removed IOUSBMassStorageClass::BulkOnlyTransferData()Removed IOUSBMassStorageClass::BulkOnlyUSBCompletionAction()Removed IOUSBMassStorageClass::CBIClearFeatureEndpointStall()Removed IOUSBMassStorageClass::CBIGetStatusEndpointStatus()Removed IOUSBMassStorageClass::CBIProtocolCommandCompletion()Removed IOUSBMassStorageClass::CBIProtocolReadInterrupt()Removed IOUSBMassStorageClass::CBIProtocolTransferData()Removed IOUSBMassStorageClass::CBIProtocolUSBCompletionAction()Removed IOUSBMassStorageClass::CheckDeferredTermination()Removed IOUSBMassStorageClass::ClearFeatureEndpointStall()Removed IOUSBMassStorageClass::ClearPipeStall()Removed IOUSBMassStorageClass::CompleteSCSICommand()Removed IOUSBMassStorageClass::DeviceRecoveryCompletionAction()Removed IOUSBMassStorageClass::didTerminate()Removed IOUSBMassStorageClass::DidWakeFromHibernationOrStandby()Removed IOUSBMassStorageClass::EndProvidedServices()Removed IOUSBMassStorageClass::FinishDeviceRecovery()Removed IOUSBMassStorageClass::free()Removed IOUSBMassStorageClass::GatedCompleteSCSICommand()Removed IOUSBMassStorageClass::GatedWaitForReset()Removed IOUSBMassStorageClass::GatedWaitForTaskAbort()Removed IOUSBMassStorageClass::GetBulkInPipe()Removed IOUSBMassStorageClass::GetBulkOnlyRequestBlock()Removed IOUSBMassStorageClass::GetBulkOutPipe()Removed IOUSBMassStorageClass::GetCBIRequestBlock()Removed IOUSBMassStorageClass::GetControlPipe()Removed IOUSBMassStorageClass::GetInterfaceProtocol()Removed IOUSBMassStorageClass::GetInterfaceReference()Removed IOUSBMassStorageClass::GetInterfaceSubclass()Removed IOUSBMassStorageClass::GetInterruptPipe()Removed IOUSBMassStorageClass::GetMaxLogicalUnitNumber()Removed IOUSBMassStorageClass::getMetaClass()Removed IOUSBMassStorageClass::GetNextBulkOnlyCommandTag()Removed IOUSBMassStorageClass::GetStatusEndpointStatus()Removed IOUSBMassStorageClass::handleClose()Removed IOUSBMassStorageClass::handleIsOpen()Removed IOUSBMassStorageClass::handleOpen()Removed IOUSBMassStorageClass::HandlePowerOn()Removed IOUSBMassStorageClass::HandleProtocolServiceFeature()Removed IOUSBMassStorageClass::init()Removed IOUSBMassStorageClass::IsPhysicalInterconnectLocationInternal()Removed IOUSBMassStorageClass::IsProtocolServiceSupported()Removed IOUSBMassStorageClass::message()Removed IOUSBMassStorageClass::ReleaseBulkOnlyRequestBlock()Removed IOUSBMassStorageClass::ReleaseCBIRequestBlock()Removed IOUSBMassStorageClass::ResetDeviceNow()Removed IOUSBMassStorageClass::sAbortCurrentSCSITask()Removed IOUSBMassStorageClass::SendSCSICommand()Removed IOUSBMassStorageClass::SendSCSICommandForBulkOnlyProtocol()Removed IOUSBMassStorageClass::SendSCSICommandForCBIProtocol()Removed IOUSBMassStorageClass::SetInterfaceReference()Removed IOUSBMassStorageClass::SetMaxLogicalUnitNumber()Removed IOUSBMassStorageClass::sResetDevice()Removed IOUSBMassStorageClass::start()Removed IOUSBMassStorageClass::StartDeviceRecovery()Removed IOUSBMassStorageClass::stop()Removed IOUSBMassStorageClass::SuspendPort()Removed IOUSBMassStorageClass::sWaitForReset()Removed IOUSBMassStorageClass::sWaitForTaskAbort()Removed IOUSBMassStorageClass::systemWillShutdown()Removed IOUSBMassStorageClass::willTerminate()Removed BulkOnlyRequestBlockRemoved CBIRequestBlockRemoved #def fAbortCurrentSCSITaskInProgressRemoved #def fAutonomousSpinDownWorkAroundRemoved #def fBlockOnResetThreadRemoved #def fBulkOnlyCBWMemoryDescriptorRemoved #def fBulkOnlyCSWMemoryDescriptorRemoved #def fCBIMemoryDescriptorRemoved #def fClearStallInProgressRemoved #def fClientsRemoved #def fConsecutiveResetCountRemoved #def fDeviceAttachedRemoved #def fKnownCSWTagMismatchIssuesRemoved #def fPortIsSuspendedRemoved #def fPortSuspendResumeForPMEnabledRemoved #def fPostDeviceResetCoolDownIntervalRemoved #def fPotentiallyStalledPipeRemoved #def fRequiredMaxBusStallRemoved #def fRequiresResetOnResumeRemoved #def fResetInProgressRemoved #def fResetStatusRemoved #def fSuspendOnRebootRemoved #def fTerminatingRemoved #def fTerminationDeferredRemoved #def fUseUSBResetNotBOResetRemoved #def fWaitingForReconfigurationMessageRemoved #def kIOPropertyIOUnitKeyRemoved #def kIOUSBKnownCSWTagIssuesRemoved #def kIOUSBMassStorageCharacteristicsRemoved #def kIOUSBMassStorageDoNotMatchRemoved #def kIOUSBMassStorageDoNotOperateRemoved #def kIOUSBMassStorageEnableSuspendResumePMRemoved #def kIOUSBMassStorageMaxLogicalUnitNumberRemoved #def kIOUSBMassStoragePostResetCoolDownRemoved #def kIOUSBMassStoragePreferredProtocolRemoved #def kIOUSBMassStoragePreferredSubclassRemoved kIOUSBMassStorageReconfigurationTimeoutMSRemoved #def kIOUSBMassStorageResetOnResumeRemoved #def kIOUSBMassStorageSuspendOnRebootRemoved #def kIOUSBMassStorageUseStandardUSBResetRemoved kUSBDAddressLengthRemoved StorageBulkOnlyCBWRemoved StorageBulkOnlyCSWRemoved #def UNUSED

#### IOKit/usb/IOUSBMassStorageUFISubclass.h

Removed IOUSBMassStorageUFIDeviceRemoved IOUSBMassStorageUFIDevice::AsyncReadWrite()Removed IOUSBMassStorageUFIDevice::AsyncReadWriteComplete()Removed IOUSBMassStorageUFIDevice::ClearNotReadyStatus()Removed IOUSBMassStorageUFIDevice::CreateStorageServiceNub()Removed IOUSBMassStorageUFIDevice::DetermineDeviceCharacteristics()Removed IOUSBMassStorageUFIDevice::DetermineMediaPresence()Removed IOUSBMassStorageUFIDevice::DetermineMediumCapacity()Removed IOUSBMassStorageUFIDevice::DetermineMediumWriteProtectState()Removed IOUSBMassStorageUFIDevice::DisablePolling()Removed IOUSBMassStorageUFIDevice::EjectTheMedium()Removed IOUSBMassStorageUFIDevice::EnablePolling()Removed IOUSBMassStorageUFIDevice::FORMAT_UNIT()Removed IOUSBMassStorageUFIDevice::FormatMedium()Removed IOUSBMassStorageUFIDevice::GetDeviceCharacteristicsDictionary()Removed IOUSBMassStorageUFIDevice::GetFormatCapacities()Removed IOUSBMassStorageUFIDevice::GetInitialPowerState()Removed IOUSBMassStorageUFIDevice::getMetaClass()Removed IOUSBMassStorageUFIDevice::GetNumberOfPowerStateTransitions()Removed IOUSBMassStorageUFIDevice::GetProductString()Removed IOUSBMassStorageUFIDevice::GetProtocolCharacteristicsDictionary()Removed IOUSBMassStorageUFIDevice::GetRevisionString()Removed IOUSBMassStorageUFIDevice::GetVendorString()Removed IOUSBMassStorageUFIDevice::HandleCheckPowerState()Removed IOUSBMassStorageUFIDevice::HandlePowerChange()Removed IOUSBMassStorageUFIDevice::InitializeDeviceSupport()Removed IOUSBMassStorageUFIDevice::InitializePowerManagement()Removed IOUSBMassStorageUFIDevice::INQUIRY()Removed IOUSBMassStorageUFIDevice::IsParameterValid()Removed IOUSBMassStorageUFIDevice::IssueRead()Removed IOUSBMassStorageUFIDevice::IssueWrite()Removed IOUSBMassStorageUFIDevice::MODE_SELECT_10()Removed IOUSBMassStorageUFIDevice::MODE_SENSE_10()Removed IOUSBMassStorageUFIDevice::PollForMediaRemoval()Removed IOUSBMassStorageUFIDevice::PollForNewMedia()Removed IOUSBMassStorageUFIDevice::PREVENT_ALLOW_MEDIUM_REMOVAL()Removed IOUSBMassStorageUFIDevice::ProcessPoll()Removed IOUSBMassStorageUFIDevice::READ_10()Removed IOUSBMassStorageUFIDevice::READ_12()Removed IOUSBMassStorageUFIDevice::READ_CAPACITY()Removed IOUSBMassStorageUFIDevice::READ_FORMAT_CAPACITIES()Removed IOUSBMassStorageUFIDevice::ReportDeviceMaxBlocksReadTransfer()Removed IOUSBMassStorageUFIDevice::ReportDeviceMaxBlocksWriteTransfer()Removed IOUSBMassStorageUFIDevice::ReportMediumBlockSize()Removed IOUSBMassStorageUFIDevice::ReportMediumTotalBlockCount()Removed IOUSBMassStorageUFIDevice::ReportMediumWriteProtection()Removed IOUSBMassStorageUFIDevice::REQUEST_SENSE()Removed IOUSBMassStorageUFIDevice::ResetMediumCharacteristics()Removed IOUSBMassStorageUFIDevice::ResumeDeviceSupport()Removed IOUSBMassStorageUFIDevice::REZERO_UNIT()Removed IOUSBMassStorageUFIDevice::SEEK()Removed IOUSBMassStorageUFIDevice::SEND_DIAGNOSTICS()Removed IOUSBMassStorageUFIDevice::SetMediumCharacteristics()Removed IOUSBMassStorageUFIDevice::sProcessPoll()Removed IOUSBMassStorageUFIDevice::START_STOP_UNIT()Removed IOUSBMassStorageUFIDevice::StartDeviceSupport()Removed IOUSBMassStorageUFIDevice::StopDeviceSupport()Removed IOUSBMassStorageUFIDevice::SuspendDeviceSupport()Removed IOUSBMassStorageUFIDevice::SyncReadWrite()Removed IOUSBMassStorageUFIDevice::TerminateDeviceSupport()Removed IOUSBMassStorageUFIDevice::TEST_UNIT_READY()Removed IOUSBMassStorageUFIDevice::TicklePowerManager()Removed IOUSBMassStorageUFIDevice::VERIFY()Removed IOUSBMassStorageUFIDevice::WRITE_10()Removed IOUSBMassStorageUFIDevice::WRITE_12()Removed IOUSBMassStorageUFIDevice::WRITE_AND_VERIFY()Removed IOUSBMassStorageUFISubclassRemoved IOUSBMassStorageUFISubclass::BeginProvidedServices()Removed IOUSBMassStorageUFISubclass::EndProvidedServices()Removed IOUSBMassStorageUFISubclass::getMetaClass()

#### IOKit/usb/IOUSBNub.h (Removed)

Removed [IOUSBController](https://developer.apple.com/documentation/kernel/iousbcontroller)Removed IOUSBNubRemoved IOUSBNub::getMetaClass()Removed IOUSBNub::initialize()Removed IOUSBNub::IsWildCardMatch()Removed IOUSBNub::USBCompareProperty()Removed IOUSBNub::USBComparePropertyInArray()Removed IOUSBNub::USBComparePropertyInArrayWithMask()Removed IOUSBNub::USBComparePropertyWithMask()Removed [IOUSBPipe](https://developer.apple.com/documentation/kernel/iousbpipe)Removed gUSBConfigurationValueRemoved gUSBDeviceClassRemoved gUSBDeviceProtocolRemoved gUSBDeviceReleaseNumberRemoved gUSBDeviceSubClassRemoved gUSBInterfaceClassRemoved gUSBInterfaceNumberRemoved gUSBInterfaceProtocolRemoved gUSBInterfaceSubClassRemoved gUSBProductIDRemoved gUSBProductIDMaskRemoved gUSBVendorIDRemoved printConfigDescriptor()Removed printDescriptor()Removed printDeviceDescriptor()Removed printEndpointDescriptor()Removed printInterfaceDescriptor()

#### IOKit/usb/IOUSBPipe.h (Removed)

Removed [IOUSBInterface](https://developer.apple.com/documentation/kernel/iousbinterface)Removed [IOUSBPipe](https://developer.apple.com/documentation/kernel/iousbpipe)Removed IOUSBPipe::Abort()Removed IOUSBPipe::ClearPipeStall()Removed IOUSBPipe::ClearStall()Removed IOUSBPipe::ClosePipe()Removed IOUSBPipe::ControlRequest()Removed IOUSBPipe::free()Removed IOUSBPipe::GetAddress()Removed IOUSBPipe::GetDirection()Removed IOUSBPipe::GetEndpoint()Removed IOUSBPipe::GetEndpointDescriptor()Removed IOUSBPipe::GetEndpointNumber()Removed IOUSBPipe::GetInterval()Removed IOUSBPipe::GetMaxPacketSize()Removed IOUSBPipe::getMetaClass()Removed IOUSBPipe::GetPipeStatus()Removed IOUSBPipe::GetStatus()Removed IOUSBPipe::GetSyncType()Removed IOUSBPipe::GetType()Removed IOUSBPipe::GetUsageType()Removed IOUSBPipe::InitToEndpoint()Removed IOUSBPipe::Read()Removed IOUSBPipe::Reset()Removed IOUSBPipe::SetPipePolicy()Removed IOUSBPipe::ToEndpoint()Removed IOUSBPipe::Write()Removed #def kAppleUSBSSIsocContinuousFrame

#### IOKit/usb/IOUSBPipeV2.h (Removed)

Removed [IOUSBPipeV2](https://developer.apple.com/documentation/kernel/iousbpipev2)Removed IOUSBPipeV2::Abort()Removed IOUSBPipeV2::CreateStreams()Removed IOUSBPipeV2::GetBytesPerInterval()Removed IOUSBPipeV2::GetConfiguredStreams()Removed IOUSBPipeV2::GetMaxBurst()Removed IOUSBPipeV2::getMetaClass()Removed IOUSBPipeV2::GetMult()Removed IOUSBPipeV2::GetSuperSpeedEndpointCompanionDescriptor()Removed IOUSBPipeV2::InitToEndpoint()Removed IOUSBPipeV2::Read()Removed IOUSBPipeV2::SetPipePolicy()Removed IOUSBPipeV2::SupportsStreams()Removed IOUSBPipeV2::ToEndpoint()Removed IOUSBPipeV2::Write()

#### IOKit/usb/IOUSBRootHubDevice.h (Removed)

Removed IOUSBRootHubDeviceRemoved IOUSBRootHubDevice::DeviceRequest()Removed IOUSBRootHubDevice::DeviceRequestWorker()Removed IOUSBRootHubDevice::free()Removed IOUSBRootHubDevice::GatedDeviceRequest()Removed IOUSBRootHubDevice::GetDeviceInformation()Removed IOUSBRootHubDevice::getMetaClass()Removed IOUSBRootHubDevice::GetSleepCurrent()Removed IOUSBRootHubDevice::init()Removed IOUSBRootHubDevice::InitializeCharacteristics()Removed IOUSBRootHubDevice::InitializeExtraPower()Removed IOUSBRootHubDevice::IsRootHub()Removed IOUSBRootHubDevice::NewRootHubDevice()Removed IOUSBRootHubDevice::RequestExtraPower()Removed IOUSBRootHubDevice::RequestExtraWakePower()Removed IOUSBRootHubDevice::RequestSleepPower()Removed IOUSBRootHubDevice::ReturnExtraPower()Removed IOUSBRootHubDevice::ReturnExtraWakePower()Removed IOUSBRootHubDevice::ReturnSleepPower()Removed IOUSBRootHubDevice::SendExtraPowerMessage()Removed IOUSBRootHubDevice::SetSleepCurrent()Removed IOUSBRootHubDevice::start()Removed IOUSBRootHubDevice::stop()Removed RHCommandHeaderRemoved RHCommandHeaderPtr

#### IOKit/usb/IOUSBUserClient.h

Removed IOUSBUserClientInitRemoved IOUSBUserClientInit::MergeDictionaryIntoDictionary()Removed IOUSBUserClientInit::MergeDictionaryIntoProvider()Removed kIOUSBLibInterfaceUserClientV3NumCommandsAdded [IOUSBUserClientLegacy](https://developer.apple.com/documentation/kernel/iousbuserclientlegacy)Added IOUSBUserClientLegacy::clientClose()Added IOUSBUserClientLegacy::close()Added IOUSBUserClientLegacy::closeGated()Added IOUSBUserClientLegacy::free()Added IOUSBUserClientLegacy::GetConfigDescriptor()Added IOUSBUserClientLegacy::GetController()Added IOUSBUserClientLegacy::GetDevice()Added IOUSBUserClientLegacy::GetFrameNumber()Added IOUSBUserClientLegacy::GetFrameNumberWithTime()Added IOUSBUserClientLegacy::GetMicroFrameNumber()Added IOUSBUserClientLegacy::initWithTask()Added IOUSBUserClientLegacy::isAuthorized()Added IOUSBUserClientLegacy::open()Added IOUSBUserClientLegacy::openGated()Added IOUSBUserClientLegacy::requestCompletion()Added IOUSBUserClientLegacy::setAsyncPort()Added IOUSBUserClientLegacy::stop()Added IOUSBUserClientLegacy::terminate()Modified [IOUSBDevice](https://developer.apple.com/documentation/kernel/iousbdevice)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBController.h |
| To | Kernel/IOKit/usb/IOUSBUserClient.h |

Modified [IOUSBInterface](https://developer.apple.com/documentation/kernel/iousbinterface)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/usb/IOUSBDevice.h |
| To | Kernel/IOKit/usb/IOUSBUserClient.h |

Modified IOUSBUserClientLegacy::getMetaClass()

|  | Introduction | Removal |
| --- | --- | --- |
| From | OS X 10.6 | OS X 10.7 |
| To | OS X 10.11 | -- |

Modified IOUSBUserClientLegacy::start()

|  | Introduction | Removal |
| --- | --- | --- |
| From | OS X 10.6 | OS X 10.7 |
| To | OS X 10.11 | -- |

#### IOKit/usb/IOUSBWorkLoop.h (Removed)

Removed IOUSBWorkLoopRemoved IOUSBWorkLoop::CloseGate()Removed IOUSBWorkLoop::closeGate()Removed IOUSBWorkLoop::free()Removed IOUSBWorkLoop::getMetaClass()Removed IOUSBWorkLoop::init()Removed IOUSBWorkLoop::OpenGate()Removed IOUSBWorkLoop::sleep()Removed IOUSBWorkLoop::SleepWithTimeout()Removed IOUSBWorkLoop::tryCloseGate()Removed IOUSBWorkLoop::wake()Removed IOUSBWorkLoop::Wakeup()Removed IOUSBWorkLoop::workLoop()

#### IOKit/usb/StandardUSB.h (Added)

Added #def HostToUSB16Added #def HostToUSB32Added #def HostToUSB64Added #def IOUSBHostFamily_StandardUSB_hAdded #def StandardUSBBitAdded #def StandardUSBBitRangeAdded #def StandardUSBBitRange64Added #def StandardUSBBitRangePhaseAdded #def USBToHost16Added #def USBToHost32Added #def USBToHost64

#### IOKit/usb/USB.h

Added #def kIOUSBMessageLegacyReEnumerateDeviceAdded #def kIOUSBMessageLegacyResetDeviceAdded #def kIOUSBMessageLegacySuspendDevice

#### kern/clock.h

Added [mach_absolutetime_asleep](https://developer.apple.com/documentation/kernel/mach_absolutetime_asleep)Added [mach_absolutetime_last_sleep](https://developer.apple.com/documentation/kernel/mach_absolutetime_last_sleep)

#### kern/debug.h

Added [io_stats_snapshot](https://developer.apple.com/documentation/kernel/io_stats_snapshot)Added [kGlobalForcedIdle](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kglobalforcedidle)Added kThreadDecompressedBTAdded [kThreadFaultedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadfaultedbt)Added [kThreadTruncatedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadtruncatedbt)Added STACKSHOT_ENABLE_FAULTINGAdded #def STACKSHOT_KCCONTAINER_TASKAdded #def STACKSHOT_KCCONTAINER_THREADAdded [STACKSHOT_KCDATA_FORMAT](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_kcdata_format)Added #def STACKSHOT_KCTYPE_BOOTARGSAdded #def STACKSHOT_KCTYPE_GLOBAL_MEM_STATSAdded #def STACKSHOT_KCTYPE_IOSTATSAdded #def STACKSHOT_KCTYPE_JETSAM_LEVELAdded #def STACKSHOT_KCTYPE_KERN_PAGE_SIZEAdded #def STACKSHOT_KCTYPE_KERN_STACKFRAMEAdded #def STACKSHOT_KCTYPE_KERN_STACKFRAME64Added #def STACKSHOT_KCTYPE_OSVERSIONAdded #def STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFOAdded #def STACKSHOT_KCTYPE_TASK_SNAPSHOTAdded #def STACKSHOT_KCTYPE_THREAD_NAMEAdded #def STACKSHOT_KCTYPE_THREAD_SNAPSHOTAdded #def STACKSHOT_KCTYPE_USER_STACKFRAMEAdded #def STACKSHOT_KCTYPE_USER_STACKFRAME64Added [STACKSHOT_RETRIEVE_EXISTING_BUFFER](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_retrieve_existing_buffer)Added [STACKSHOT_SAVE_IN_KERNEL_BUFFER](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_save_in_kernel_buffer)Added #def STASKSHOT_KCTYPE_DONATING_PIDSAdded [task_snapshot_v2](https://developer.apple.com/documentation/kernel/task_snapshot_v2)Added [thread_snapshot_v2](https://developer.apple.com/documentation/kernel/thread_snapshot_v2)

#### kern/energy_perf.h

Added #def GPU_BUSY_VALIDAdded #def GPU_CYCLE_COUNT_VALIDAdded [gpu_fceiling_cb_register()](https://developer.apple.com/documentation/kernel/1478505-gpu_fceiling_cb_register)Added #def GPU_MISC_VALIDAdded #def GPU_NCMDS_VALIDAdded #def GPU_NOUTSTANDING_VALIDAdded [gpu_set_fceiling_t](https://developer.apple.com/documentation/kernel/gpu_set_fceiling_t)Added [gpu_submission_telemetry()](https://developer.apple.com/documentation/kernel/1478498-gpu_submission_telemetry)

#### kern/hv_support.h

Removed hv_release_mp_notify()Removed hv_set_mp_notify()

#### kern/kern_cdata.h (Added)

Added [KC_ST_CHAR](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_char)Added [KC_ST_INT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int16)Added [KC_ST_INT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int32)Added [KC_ST_INT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int64)Added [KC_ST_INT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int8)Added [KC_ST_UINT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint16)Added [KC_ST_UINT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint32)Added [KC_ST_UINT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint64)Added [KC_ST_UINT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint8)Added #def KCDATA_BUFFER_BEGIN_CRASHINFOAdded #def KCDATA_BUFFER_BEGIN_STACKSHOTAdded #def KCDATA_CONTAINER_IDAdded #def KCDATA_DESC_MAXLENAdded #def KCDATA_ITEM_ARRAY_GET_EL_COUNTAdded #def KCDATA_ITEM_ARRAY_GET_EL_SIZEAdded #def KCDATA_ITEM_ARRAY_GET_EL_TYPEAdded KCDATA_ITEM_FIND_TYPE()Added #def KCDATA_ITEM_FLAGSAdded #def KCDATA_ITEM_FOREACHAdded #def KCDATA_ITEM_HEADER_SIZEAdded #def KCDATA_ITEM_NEXT_HEADERAdded #def KCDATA_ITEM_SIZEAdded [kcdata_item_t](https://developer.apple.com/documentation/kernel/kcdata_item_t)Added #def KCDATA_ITEM_TYPEAdded [kcdata_subtype_descriptor_t](https://developer.apple.com/documentation/kernel/kcdata_subtype_descriptor_t)Added #def KCDATA_TYPE_ARRAYAdded #def KCDATA_TYPE_BINDATA_DESCAdded #def KCDATA_TYPE_BUFFER_ENDAdded #def KCDATA_TYPE_CONTAINER_BEGINAdded #def KCDATA_TYPE_CONTAINER_ENDAdded [kcdata_type_definition](https://developer.apple.com/documentation/kernel/kcdata_type_definition)Added #def KCDATA_TYPE_INT32_DESCAdded #def KCDATA_TYPE_INT64_DESCAdded #def KCDATA_TYPE_INVALIDAdded #def KCDATA_TYPE_LIBRARY_LOADINFOAdded #def KCDATA_TYPE_LIBRARY_LOADINFO64Added #def KCDATA_TYPE_MACH_ABSOLUTE_TIMEAdded #def KCDATA_TYPE_STRING_DESCAdded #def KCDATA_TYPE_TIMEBASEAdded #def KCDATA_TYPE_TIMEVALAdded #def KCDATA_TYPE_TYPEDEFINTIONAdded #def KCDATA_TYPE_UINT32_DESCAdded #def KCDATA_TYPE_UINT64_DESCAdded #def KCDATA_TYPE_USECS_SINCE_EPOCHAdded [kcs_get_elem_count()](https://developer.apple.com/documentation/kernel/1588393-kcs_get_elem_count)Added [kcs_get_elem_size()](https://developer.apple.com/documentation/kernel/1588402-kcs_get_elem_size)Added [kcs_set_elem_size()](https://developer.apple.com/documentation/kernel/1588385-kcs_set_elem_size)Added #def KCS_SUBTYPE_FLAGS_ARRAYAdded #def KCS_SUBTYPE_FLAGS_NONEAdded #def KCS_SUBTYPE_PACK_SIZEAdded [kctype_subtype_t](https://developer.apple.com/documentation/kernel/kctype_subtype_t)

#### kern/kern_types.h

Added #def TIMEOUT_NO_LEEWAYAdded #def TIMEOUT_WAIT_FOREVER

#### kern/kpc.h

Added #def CONFIGURABLE_RELOAD_CPUAdded #def CONFIGURABLE_SHADOW_CPUAdded #def FIXED_RELOAD_CPUAdded #def FIXED_SHADOW_CPUAdded [kpc_actionid](https://developer.apple.com/documentation/kernel/kpc_actionid)Added #def KPC_ALL_CPUSAdded [kpc_arch_init()](https://developer.apple.com/documentation/kernel/1572346-kpc_arch_init)Added #def KPC_CLASS_CONFIGURABLEAdded #def KPC_CLASS_CONFIGURABLE_MASKAdded #def KPC_CLASS_FIXEDAdded #def KPC_CLASS_FIXED_MASKAdded #def KPC_CLASS_POWERAdded #def KPC_CLASS_POWER_MASKAdded #def KPC_CLASS_RAWPMUAdded #def KPC_CLASS_RAWPMU_MASKAdded [kpc_common_init()](https://developer.apple.com/documentation/kernel/1572407-kpc_common_init)Added [kpc_config_remote](https://developer.apple.com/documentation/kernel/kpc_config_remote)Added [kpc_configurable_config_count()](https://developer.apple.com/documentation/kernel/1572369-kpc_configurable_config_count)Added [kpc_configurable_count()](https://developer.apple.com/documentation/kernel/1572402-kpc_configurable_count)Added [kpc_configurable_max()](https://developer.apple.com/documentation/kernel/1572351-kpc_configurable_max)Added [kpc_controls_counter()](https://developer.apple.com/documentation/kernel/1572431-kpc_controls_counter)Added [kpc_controls_fixed_counters()](https://developer.apple.com/documentation/kernel/1572385-kpc_controls_fixed_counters)Added [kpc_counterbuf_alloc()](https://developer.apple.com/documentation/kernel/1572340-kpc_counterbuf_alloc)Added [kpc_counterbuf_free()](https://developer.apple.com/documentation/kernel/1572361-kpc_counterbuf_free)Added [kpc_disable_whitelist()](https://developer.apple.com/documentation/kernel/1572389-kpc_disable_whitelist)Added [kpc_driver](https://developer.apple.com/documentation/kernel/kpc_driver)Added [kpc_fixed_config_count()](https://developer.apple.com/documentation/kernel/1572325-kpc_fixed_config_count)Added [kpc_fixed_count()](https://developer.apple.com/documentation/kernel/1572322-kpc_fixed_count)Added [kpc_fixed_max()](https://developer.apple.com/documentation/kernel/1572415-kpc_fixed_max)Added [kpc_force_all_ctrs()](https://developer.apple.com/documentation/kernel/1572429-kpc_force_all_ctrs)Added [kpc_force_all_ctrs_arch()](https://developer.apple.com/documentation/kernel/1572433-kpc_force_all_ctrs_arch)Added [kpc_get_actionid()](https://developer.apple.com/documentation/kernel/1572427-kpc_get_actionid)Added [kpc_get_all_cpus_counters()](https://developer.apple.com/documentation/kernel/1572398-kpc_get_all_cpus_counters)Added [kpc_get_classes()](https://developer.apple.com/documentation/kernel/1572364-kpc_get_classes)Added [kpc_get_config()](https://developer.apple.com/documentation/kernel/1572417-kpc_get_config)Added [kpc_get_config_count()](https://developer.apple.com/documentation/kernel/1572387-kpc_get_config_count)Added [kpc_get_configurable_config()](https://developer.apple.com/documentation/kernel/1572423-kpc_get_configurable_config)Added [kpc_get_configurable_counters()](https://developer.apple.com/documentation/kernel/1572334-kpc_get_configurable_counters)Added [kpc_get_configurable_pmc_mask()](https://developer.apple.com/documentation/kernel/1572341-kpc_get_configurable_pmc_mask)Added [kpc_get_counter_count()](https://developer.apple.com/documentation/kernel/1572416-kpc_get_counter_count)Added [kpc_get_counters_remote](https://developer.apple.com/documentation/kernel/kpc_get_counters_remote)Added [kpc_get_cpu_counters()](https://developer.apple.com/documentation/kernel/1572419-kpc_get_cpu_counters)Added [kpc_get_curcpu_counters()](https://developer.apple.com/documentation/kernel/1572335-kpc_get_curcpu_counters)Added [kpc_get_curthread_counters()](https://developer.apple.com/documentation/kernel/1572391-kpc_get_curthread_counters)Added [kpc_get_fixed_config()](https://developer.apple.com/documentation/kernel/1572376-kpc_get_fixed_config)Added [kpc_get_fixed_counters()](https://developer.apple.com/documentation/kernel/1572343-kpc_get_fixed_counters)Added [kpc_get_force_all_ctrs()](https://developer.apple.com/documentation/kernel/1572336-kpc_get_force_all_ctrs)Added [kpc_get_period()](https://developer.apple.com/documentation/kernel/1572422-kpc_get_period)Added [kpc_get_pmu_version()](https://developer.apple.com/documentation/kernel/1572386-kpc_get_pmu_version)Added [kpc_get_rawpmu_config()](https://developer.apple.com/documentation/kernel/1572412-kpc_get_rawpmu_config)Added [kpc_get_running()](https://developer.apple.com/documentation/kernel/1572420-kpc_get_running)Added [kpc_get_shadow_counters()](https://developer.apple.com/documentation/kernel/1572328-kpc_get_shadow_counters)Added [kpc_get_thread_counting()](https://developer.apple.com/documentation/kernel/1572344-kpc_get_thread_counting)Added [kpc_get_whitelist_disabled()](https://developer.apple.com/documentation/kernel/1572377-kpc_get_whitelist_disabled)Added [kpc_idle()](https://developer.apple.com/documentation/kernel/1572405-kpc_idle)Added [kpc_idle_exit()](https://developer.apple.com/documentation/kernel/1572370-kpc_idle_exit)Added [kpc_init()](https://developer.apple.com/documentation/kernel/1572384-kpc_init)Added [kpc_is_running_configurable()](https://developer.apple.com/documentation/kernel/1572390-kpc_is_running_configurable)Added [kpc_is_running_fixed()](https://developer.apple.com/documentation/kernel/1572434-kpc_is_running_fixed)Added [kpc_multiple_clients()](https://developer.apple.com/documentation/kernel/1572342-kpc_multiple_clients)Added [kpc_pm_handler_t](https://developer.apple.com/documentation/kernel/kpc_pm_handler_t)Added #def KPC_PMU_ARM_APPLEAdded #def KPC_PMU_ARM_V2Added #def KPC_PMU_ERRORAdded #def KPC_PMU_INTEL_V2Added #def KPC_PMU_INTEL_V3Added [kpc_popcount()](https://developer.apple.com/documentation/kernel/1572350-kpc_popcount)Added [kpc_rawpmu_config_count()](https://developer.apple.com/documentation/kernel/1572404-kpc_rawpmu_config_count)Added [kpc_register_cpu()](https://developer.apple.com/documentation/kernel/1572424-kpc_register_cpu)Added [kpc_register_pm_handler()](https://developer.apple.com/documentation/kernel/1572430-kpc_register_pm_handler)Added [kpc_release_pm_counters()](https://developer.apple.com/documentation/kernel/1572327-kpc_release_pm_counters)Added [kpc_reserve_pm_counters()](https://developer.apple.com/documentation/kernel/1572395-kpc_reserve_pm_counters)Added [kpc_running_remote](https://developer.apple.com/documentation/kernel/kpc_running_remote)Added [kpc_sample_kperf()](https://developer.apple.com/documentation/kernel/1572393-kpc_sample_kperf)Added [kpc_set_actionid()](https://developer.apple.com/documentation/kernel/1572379-kpc_set_actionid)Added [kpc_set_config()](https://developer.apple.com/documentation/kernel/1572437-kpc_set_config)Added [kpc_set_config_arch()](https://developer.apple.com/documentation/kernel/1572396-kpc_set_config_arch)Added [kpc_set_period()](https://developer.apple.com/documentation/kernel/1572418-kpc_set_period)Added [kpc_set_period_arch()](https://developer.apple.com/documentation/kernel/1572380-kpc_set_period_arch)Added [kpc_set_running()](https://developer.apple.com/documentation/kernel/1572411-kpc_set_running)Added [kpc_set_running_arch()](https://developer.apple.com/documentation/kernel/1572368-kpc_set_running_arch)Added [kpc_set_sw_inc()](https://developer.apple.com/documentation/kernel/1572355-kpc_set_sw_inc)Added [kpc_set_thread_counting()](https://developer.apple.com/documentation/kernel/1572378-kpc_set_thread_counting)Added kpc_switch_context()Added [kpc_thread_ast_handler()](https://developer.apple.com/documentation/kernel/1572357-kpc_thread_ast_handler)Added [kpc_thread_create()](https://developer.apple.com/documentation/kernel/1572348-kpc_thread_create)Added [kpc_thread_destroy()](https://developer.apple.com/documentation/kernel/1572383-kpc_thread_destroy)Added [kpc_thread_init()](https://developer.apple.com/documentation/kernel/1572333-kpc_thread_init)Added [kpc_threads_counting](https://developer.apple.com/documentation/kernel/kpc_threads_counting)Modified #def CONFIGURABLE_ACTIONID

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def CONFIGURABLE_RELOAD

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def CONFIGURABLE_SHADOW

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_ACTIONID

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_RELOAD

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_SHADOW

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

#### kern/queue.h

Added [movqueue()](https://developer.apple.com/documentation/kernel/1567118-movqueue)Added #def qe_elementAdded #def qe_foreachAdded #def qe_foreach_elementAdded #def qe_foreach_element_safeAdded #def qe_foreach_safeAdded #def queue_chain_initAdded #def queue_head_initAdded [re_queue_head()](https://developer.apple.com/documentation/kernel/1567135-re_queue_head)Added [re_queue_tail()](https://developer.apple.com/documentation/kernel/1567146-re_queue_tail)

#### libkern/c++/OSMetaClass.h

Added #def APPLE_KEXT_COMPATIBILITY_OVERRIDEAdded #def APPLE_KEXT_OVERRIDE

#### libkern/c++/OSString.h

Removed OSString::withStringOfLength()

#### libkern/OSKextLib.h

Added [OSKextGrabPgoData()](https://developer.apple.com/documentation/kernel/1508333-oskextgrabpgodata)

#### mach-o/loader.h

Added #def LC_LINKER_OPTIMIZATION_HINTAdded #def LC_LINKER_OPTIONAdded #def LC_VERSION_MIN_WATCHOSAdded [linker_option_command](https://developer.apple.com/documentation/kernel/linker_option_command)Added #def MH_APP_EXTENSION_SAFE

#### mach-o/nlist.h

Added #def N_ALT_ENTRY

#### mach/exception_types.h

Added #def EXC_CORPSE_NOTIFYAdded #def EXC_MASK_CORPSE_NOTIFY

#### mach/host_info.h

Added #def HOST_DEBUG_INFO_INTERNAL

#### mach/host_special_ports.h

Added #def HOST_CONTAINERD_PORTAdded #def host_get_container_portAdded #def host_get_sysdiagnose_portAdded #def host_set_container_portAdded #def host_set_sysdiagnose_portAdded #def HOST_SYSDIAGNOSE_PORTAdded #def HOST_XPC_EXCEPTION_PORT

#### mach/mach_host.h

Added [host_set_atm_diagnostic_flag()](https://developer.apple.com/documentation/kernel/1502446-host_set_atm_diagnostic_flag)Added [mach_memory_info()](https://developer.apple.com/documentation/kernel/1502832-mach_memory_info)

#### mach/machine.h

Added #def CPUFAMILY_ARM_TYPHOON

#### mach/machine/sdt.h

Added #def DTRACE_VM5

#### mach/memory_object_types.h

Added #def MAP_MEM_4K_DATA_ADDRAdded [upl_control_flags_t](https://developer.apple.com/documentation/kernel/upl_control_flags_t)Added #def UPL_MEMORY_TAGAdded #def UPL_MEMORY_TAG_MAKEAdded #def UPL_MEMORY_TAG_MASKAdded #def UPL_MEMORY_TAG_SHIFT

#### mach/sysdiagnose_notification_server.h (Added)

Added [receive_sysdiagnose_notification()](https://developer.apple.com/documentation/kernel/1412350-receive_sysdiagnose_notification)Added [receive_sysdiagnose_notification_subsystem](https://developer.apple.com/documentation/kernel/receive_sysdiagnose_notification_subsystem-382)Added [receive_sysdiagnose_notification_subsystem](https://developer.apple.com/documentation/kernel/receive_sysdiagnose_notification_subsystem)Added #def subsystem_to_name_map_sysdiagnose_notificationAdded #def sysdiagnose_notification_MSG_COUNTAdded [sysdiagnose_notification_server()](https://developer.apple.com/documentation/kernel/1412344-sysdiagnose_notification_server)Added [sysdiagnose_notification_server_routine()](https://developer.apple.com/documentation/kernel/1412346-sysdiagnose_notification_server_)

#### mach/task_info.h

Added #def TASK_DEBUG_INFO_INTERNALAdded #def TASK_FLAGS_INFOAdded #def TASK_FLAGS_INFO_COUNTAdded [task_flags_info_data_t](https://developer.apple.com/documentation/kernel/task_flags_info_data_t)Added [task_flags_info_t](https://developer.apple.com/documentation/kernel/task_flags_info_t)Added #def TASK_VM_INFO_PURGEABLE_ACCOUNTAdded #def TASK_VM_INFO_REV0_COUNTAdded #def TF_LP64

#### mach/thread_info.h

Added #def MAXTHREADNAMESIZEAdded #def TH_FLAGS_GLOBAL_FORCED_IDLEAdded #def THREAD_DEBUG_INFO_INTERNALAdded #def THREAD_EXTENDED_INFOAdded #def THREAD_EXTENDED_INFO_COUNTAdded [thread_extended_info_data_t](https://developer.apple.com/documentation/kernel/thread_extended_info_data_t)Added [thread_extended_info_t](https://developer.apple.com/documentation/kernel/thread_extended_info_t)

#### mach/vm_behavior.h

Added #def VM_BEHAVIOR_PAGEOUT

#### mach/vm_prot.h

Added #def VM_PROT_MEMORY_TAGAdded #def VM_PROT_MEMORY_TAG_MAKEAdded #def VM_PROT_MEMORY_TAG_MASKAdded #def VM_PROT_MEMORY_TAG_SHIFT

#### mach/vm_statistics.h

Added #def VM_FLAGS_RESILIENT_CODESIGNAdded #def VM_FLAGS_RESILIENT_MEDIAAdded #def VM_FLAGS_RETURN_4K_DATA_ADDRAdded #def VM_MEMORY_ASLAdded #def VM_MEMORY_CORPSEINFOAdded #def VM_MEMORY_RAWCAMERAAdded #def VM_PAGE_QUERY_PAGE_CS_NX

#### mach_debug/mach_debug_types.h

Added [mach_core_fileheader](https://developer.apple.com/documentation/kernel/mach_core_fileheader)Added #def MACH_CORE_FILEHEADER_SIGNATURE

#### mach_debug/zone_info.h

Added [mach_memory_info_array_t](https://developer.apple.com/documentation/kernel/mach_memory_info_array_t)Added [mach_memory_info_t](https://developer.apple.com/documentation/kernel/mach_memory_info_t)

#### net/if.h

Added #def KEV_DL_RRC_STATE_CHANGED

#### net/if_media.h

Added #def IFM_2500_TAdded #def IFM_5000_T

#### net/pfkeyv2.h

Added #def SADB_EXT_MIGRATE_ADDRESS_DSTAdded #def SADB_EXT_MIGRATE_ADDRESS_SRCAdded #def SADB_MIGRATEAdded #def SADB_X_EALG_AES_GCMAdded #def SADB_X_EXT_MIGRATE_IPSECIF

#### netinet/in.h

Removed inet_ntoa()Removed inet_ntoa_r()Removed inet_pton()

#### netinet/tcp.h

Added #def TCP_CONNECTION_INFOAdded [tcp_connection_info](https://developer.apple.com/documentation/kernel/tcp_connection_info)Added #def TCP_FASTOPENAdded #def TCPCI_FLAG_LOSSRECOVERYAdded #def TCPCI_FLAG_REORDERING_DETECTEDAdded #def TCPCI_OPT_ECNAdded #def TCPCI_OPT_SACKAdded #def TCPCI_OPT_TIMESTAMPSAdded #def TCPCI_OPT_WSCALEAdded #def TCPOLEN_FASTOPEN_REQAdded #def TCPOPT_FASTOPEN

#### netinet6/scope6_var.h (Added)

Added #def SCOPE6_ID_MAX

#### pexpert/i386/boot.h

Removed #def kBootArgsFlagCSRPendingConfigAdded #def kBootArgsFlagCSRConfigModeAdded #def kBootArgsFlagInstallUI

#### pexpert/pexpert.h

Added [gPlatformECID](https://developer.apple.com/documentation/kernel/gplatformecid)Added [PE_cpu_signal_cancel()](https://developer.apple.com/documentation/kernel/1553700-pe_cpu_signal_cancel)Added [PE_cpu_signal_deferred()](https://developer.apple.com/documentation/kernel/1553622-pe_cpu_signal_deferred)Added [PE_i_can_has_debugger()](https://developer.apple.com/documentation/kernel/1553651-pe_i_can_has_debugger)

#### security/mac.h

Added #def SECURITY_MAC_CHECK_ENFORCEAdded #def SECURITY_MAC_CTLFLAGS

#### security/mac_internal.h

Added #def MAC_BOOLEANAdded #def MAC_CHECKAdded mac_check_structmac_consistent()Added mac_context_check_enforce()Added mac_context_set_enforce()Added mac_cred_label_externalize()Added mac_cred_label_internalize()Added mac_device_enforceAdded mac_error_select()Added mac_externalize()Added #def MAC_EXTERNALIZEAdded #def MAC_EXTERNALIZE_AUDITAdded #def MAC_GRANTAdded mac_internalize()Added #def MAC_INTERNALIZEAdded mac_label_destroy()Added mac_label_elementAdded mac_label_element_listAdded mac_label_element_list_tAdded mac_label_init()Added mac_label_listenerAdded mac_label_listeners_tAdded mac_label_vnodesAdded mac_labelzone_alloc()Added mac_labelzone_free()Added mac_labelzone_init()Added mac_lateAdded #def mac_mbuf_to_labelAdded #def MAC_PERFORMAdded mac_pipe_enforceAdded mac_pipe_label_externalize()Added mac_pipe_label_internalize()Added mac_policy_addto_labellist()Added mac_policy_listAdded mac_policy_list_busy()Added mac_policy_list_conditional_busy()Added mac_policy_list_elementAdded mac_policy_list_tAdded mac_policy_list_unbusy()Added mac_policy_removefrom_labellist()Added mac_posixsem_enforceAdded mac_posixshm_enforceAdded mac_proc_check_enforce()Added mac_proc_enforceAdded mac_socket_enforceAdded mac_static_label_element_listAdded mac_system_enforceAdded mac_sysvmsg_enforceAdded mac_sysvsem_enforceAdded mac_sysvshm_enforceAdded mac_vm_enforceAdded mac_vnode_enforceAdded mac_vnode_label_externalize()Added mac_vnode_label_internalize()Added sysctl__security_childrenAdded sysctl__security_mac_children

#### security/mac_mach_internal.h

Removed mac_thread_get_threadlabel()Removed mac_thread_get_uthreadlabel()

#### security/mac_policy.h

Added [OSObject](https://developer.apple.com/documentation/kernel/osobject)Added [io_object_t](https://developer.apple.com/documentation/kernel/io_object_t)Added #def LABEL_TO_SLOTAdded #def MAC_AUDIT_DATA_LIMITAdded #def MAC_AUDIT_DEFAULTAdded #def MAC_AUDIT_NOAdded mac_audit_text()Added #def MAC_AUDIT_YESAdded #def mac_get_mpcAdded mac_label_get()Added mac_label_set()Added #def MAC_NOWAITAdded mac_policy_confAdded mac_policy_handle_tAdded mac_policy_opsAdded #def MAC_POLICY_OPS_VERSIONAdded mac_policy_register()Added #def MAC_POLICY_SETAdded mac_policy_unregister()Added mac_vnop_getxattr()Added mac_vnop_removexattr()Added mac_vnop_setxattr()Added #def MAC_WAITOKAdded #def MPC_LOADTIME_BASE_POLICYAdded #def MPC_LOADTIME_FLAG_LABELMBUFSAdded #def MPC_LOADTIME_FLAG_NOTLATEAdded #def MPC_LOADTIME_FLAG_UNLOADOKAdded #def MPC_RUNTIME_FLAG_REGISTEREDAdded #def mpc_tAdded mpo_audit_check_postselect_tAdded mpo_audit_check_preselect_tAdded mpo_bpfdesc_check_receive_tAdded mpo_bpfdesc_label_associate_tAdded mpo_bpfdesc_label_destroy_tAdded mpo_bpfdesc_label_init_tAdded mpo_cred_check_label_update_execve_tAdded mpo_cred_check_label_update_tAdded mpo_cred_check_visible_tAdded mpo_cred_label_associate_fork_tAdded mpo_cred_label_associate_kernel_tAdded mpo_cred_label_associate_tAdded mpo_cred_label_associate_user_tAdded mpo_cred_label_destroy_tAdded mpo_cred_label_externalize_audit_tAdded mpo_cred_label_externalize_tAdded mpo_cred_label_init_tAdded mpo_cred_label_internalize_tAdded mpo_cred_label_update_execve_tAdded mpo_cred_label_update_tAdded mpo_devfs_label_associate_device_tAdded mpo_devfs_label_associate_directory_tAdded mpo_devfs_label_copy_tAdded mpo_devfs_label_destroy_tAdded mpo_devfs_label_init_tAdded mpo_devfs_label_update_tAdded mpo_file_check_change_offset_tAdded mpo_file_check_create_tAdded mpo_file_check_dup_tAdded mpo_file_check_fcntl_tAdded mpo_file_check_get_offset_tAdded mpo_file_check_get_tAdded mpo_file_check_inherit_tAdded mpo_file_check_ioctl_tAdded mpo_file_check_lock_tAdded mpo_file_check_mmap_downgrade_tAdded mpo_file_check_mmap_tAdded mpo_file_check_receive_tAdded mpo_file_check_set_tAdded mpo_file_label_associate_tAdded mpo_file_label_destroy_tAdded mpo_file_label_init_tAdded mpo_ifnet_check_label_update_tAdded mpo_ifnet_check_transmit_tAdded mpo_ifnet_label_associate_tAdded mpo_ifnet_label_copy_tAdded mpo_ifnet_label_destroy_tAdded mpo_ifnet_label_externalize_tAdded mpo_ifnet_label_init_tAdded mpo_ifnet_label_internalize_tAdded mpo_ifnet_label_recycle_tAdded mpo_ifnet_label_update_tAdded mpo_inpcb_check_deliver_tAdded mpo_inpcb_label_associate_tAdded mpo_inpcb_label_destroy_tAdded mpo_inpcb_label_init_tAdded mpo_inpcb_label_recycle_tAdded mpo_inpcb_label_update_tAdded mpo_iokit_check_device_tAdded mpo_iokit_check_filter_properties_tAdded mpo_iokit_check_get_property_tAdded mpo_iokit_check_hid_control_tAdded mpo_iokit_check_nvram_delete_tAdded mpo_iokit_check_nvram_get_tAdded mpo_iokit_check_nvram_set_tAdded mpo_iokit_check_open_tAdded mpo_iokit_check_set_properties_tAdded mpo_ipq_label_associate_tAdded mpo_ipq_label_compare_tAdded mpo_ipq_label_destroy_tAdded mpo_ipq_label_init_tAdded mpo_ipq_label_update_tAdded mpo_kext_check_load_tAdded mpo_kext_check_query_tAdded mpo_kext_check_unload_tAdded mpo_mbuf_label_associate_bpfdesc_tAdded mpo_mbuf_label_associate_ifnet_tAdded mpo_mbuf_label_associate_inpcb_tAdded mpo_mbuf_label_associate_ipq_tAdded mpo_mbuf_label_associate_linklayer_tAdded mpo_mbuf_label_associate_multicast_encap_tAdded mpo_mbuf_label_associate_netlayer_tAdded mpo_mbuf_label_associate_socket_tAdded mpo_mbuf_label_copy_tAdded mpo_mbuf_label_destroy_tAdded mpo_mbuf_label_init_tAdded mpo_mount_check_fsctl_tAdded mpo_mount_check_getattr_tAdded mpo_mount_check_label_update_tAdded mpo_mount_check_mount_tAdded mpo_mount_check_remount_tAdded mpo_mount_check_setattr_tAdded mpo_mount_check_stat_tAdded mpo_mount_check_umount_tAdded mpo_mount_label_associate_tAdded mpo_mount_label_destroy_tAdded mpo_mount_label_externalize_tAdded mpo_mount_label_init_tAdded mpo_mount_label_internalize_tAdded mpo_netinet_fragment_tAdded mpo_netinet_icmp_reply_tAdded mpo_netinet_tcp_reply_tAdded mpo_pipe_check_ioctl_tAdded mpo_pipe_check_kqfilter_tAdded mpo_pipe_check_label_update_tAdded mpo_pipe_check_read_tAdded mpo_pipe_check_select_tAdded mpo_pipe_check_stat_tAdded mpo_pipe_check_write_tAdded mpo_pipe_label_associate_tAdded mpo_pipe_label_copy_tAdded mpo_pipe_label_destroy_tAdded mpo_pipe_label_externalize_tAdded mpo_pipe_label_init_tAdded mpo_pipe_label_internalize_tAdded mpo_pipe_label_update_tAdded mpo_policy_destroy_tAdded mpo_policy_init_tAdded mpo_policy_initbsd_tAdded mpo_policy_syscall_tAdded mpo_posixsem_check_create_tAdded mpo_posixsem_check_open_tAdded mpo_posixsem_check_post_tAdded mpo_posixsem_check_unlink_tAdded mpo_posixsem_check_wait_tAdded mpo_posixsem_label_associate_tAdded mpo_posixsem_label_destroy_tAdded mpo_posixsem_label_init_tAdded mpo_posixshm_check_create_tAdded mpo_posixshm_check_mmap_tAdded mpo_posixshm_check_open_tAdded mpo_posixshm_check_stat_tAdded mpo_posixshm_check_truncate_tAdded mpo_posixshm_check_unlink_tAdded mpo_posixshm_label_associate_tAdded mpo_posixshm_label_destroy_tAdded mpo_posixshm_label_init_tAdded mpo_priv_check_tAdded mpo_priv_grant_tAdded mpo_proc_check_cpumon_tAdded mpo_proc_check_debug_tAdded mpo_proc_check_expose_task_tAdded mpo_proc_check_fork_tAdded mpo_proc_check_get_task_name_tAdded mpo_proc_check_get_task_tAdded mpo_proc_check_getaudit_tAdded mpo_proc_check_getauid_tAdded mpo_proc_check_getlcid_tAdded mpo_proc_check_inherit_ipc_ports_tAdded mpo_proc_check_ledger_tAdded mpo_proc_check_map_anon_tAdded mpo_proc_check_mprotect_tAdded mpo_proc_check_proc_info_tAdded mpo_proc_check_run_cs_invalid_tAdded mpo_proc_check_sched_tAdded mpo_proc_check_set_host_exception_port_tAdded mpo_proc_check_set_host_special_port_tAdded mpo_proc_check_setaudit_tAdded mpo_proc_check_setauid_tAdded mpo_proc_check_setlcid_tAdded mpo_proc_check_signal_tAdded mpo_proc_check_suspend_resume_tAdded mpo_proc_check_wait_tAdded mpo_proc_label_destroy_tAdded mpo_proc_label_init_tAdded mpo_pty_notify_close_tAdded mpo_pty_notify_grant_tAdded mpo_reserved_hook_tAdded mpo_socket_check_accept_tAdded mpo_socket_check_accepted_tAdded mpo_socket_check_bind_tAdded mpo_socket_check_connect_tAdded mpo_socket_check_create_tAdded mpo_socket_check_deliver_tAdded mpo_socket_check_getsockopt_tAdded mpo_socket_check_kqfilter_tAdded mpo_socket_check_label_update_tAdded mpo_socket_check_listen_tAdded mpo_socket_check_receive_tAdded mpo_socket_check_received_tAdded mpo_socket_check_select_tAdded mpo_socket_check_send_tAdded mpo_socket_check_setsockopt_tAdded mpo_socket_check_stat_tAdded mpo_socket_label_associate_accept_tAdded mpo_socket_label_associate_tAdded mpo_socket_label_copy_tAdded mpo_socket_label_destroy_tAdded mpo_socket_label_externalize_tAdded mpo_socket_label_init_tAdded mpo_socket_label_internalize_tAdded mpo_socket_label_update_tAdded mpo_socketpeer_label_associate_mbuf_tAdded mpo_socketpeer_label_associate_socket_tAdded mpo_socketpeer_label_destroy_tAdded mpo_socketpeer_label_externalize_tAdded mpo_socketpeer_label_init_tAdded mpo_system_check_acct_tAdded mpo_system_check_audit_tAdded mpo_system_check_auditctl_tAdded mpo_system_check_auditon_tAdded mpo_system_check_chud_tAdded mpo_system_check_host_priv_tAdded mpo_system_check_info_tAdded mpo_system_check_kas_info_tAdded mpo_system_check_nfsd_tAdded mpo_system_check_reboot_tAdded mpo_system_check_settime_tAdded mpo_system_check_swapoff_tAdded mpo_system_check_swapon_tAdded mpo_system_check_sysctlbyname_tAdded mpo_sysvmsg_label_associate_tAdded mpo_sysvmsg_label_destroy_tAdded mpo_sysvmsg_label_init_tAdded mpo_sysvmsg_label_recycle_tAdded mpo_sysvmsq_check_enqueue_tAdded mpo_sysvmsq_check_msgrcv_tAdded mpo_sysvmsq_check_msgrmid_tAdded mpo_sysvmsq_check_msqctl_tAdded mpo_sysvmsq_check_msqget_tAdded mpo_sysvmsq_check_msqrcv_tAdded mpo_sysvmsq_check_msqsnd_tAdded mpo_sysvmsq_label_associate_tAdded mpo_sysvmsq_label_destroy_tAdded mpo_sysvmsq_label_init_tAdded mpo_sysvmsq_label_recycle_tAdded mpo_sysvsem_check_semctl_tAdded mpo_sysvsem_check_semget_tAdded mpo_sysvsem_check_semop_tAdded mpo_sysvsem_label_associate_tAdded mpo_sysvsem_label_destroy_tAdded mpo_sysvsem_label_init_tAdded mpo_sysvsem_label_recycle_tAdded mpo_sysvshm_check_shmat_tAdded mpo_sysvshm_check_shmctl_tAdded mpo_sysvshm_check_shmdt_tAdded mpo_sysvshm_check_shmget_tAdded mpo_sysvshm_label_associate_tAdded mpo_sysvshm_label_destroy_tAdded mpo_sysvshm_label_init_tAdded mpo_sysvshm_label_recycle_tAdded mpo_thread_userret_tAdded mpo_vnode_check_access_tAdded mpo_vnode_check_chdir_tAdded mpo_vnode_check_chroot_tAdded mpo_vnode_check_create_tAdded mpo_vnode_check_deleteextattr_tAdded mpo_vnode_check_exchangedata_tAdded mpo_vnode_check_exec_tAdded mpo_vnode_check_fsgetpath_tAdded mpo_vnode_check_getattrlist_tAdded mpo_vnode_check_getextattr_tAdded mpo_vnode_check_ioctl_tAdded mpo_vnode_check_kqfilter_tAdded mpo_vnode_check_label_update_tAdded mpo_vnode_check_link_tAdded mpo_vnode_check_listextattr_tAdded mpo_vnode_check_lookup_tAdded mpo_vnode_check_open_tAdded mpo_vnode_check_read_tAdded mpo_vnode_check_readdir_tAdded mpo_vnode_check_readlink_tAdded mpo_vnode_check_rename_from_tAdded mpo_vnode_check_rename_tAdded mpo_vnode_check_rename_to_tAdded mpo_vnode_check_revoke_tAdded mpo_vnode_check_searchfs_tAdded mpo_vnode_check_select_tAdded mpo_vnode_check_setattrlist_tAdded mpo_vnode_check_setextattr_tAdded mpo_vnode_check_setflags_tAdded mpo_vnode_check_setmode_tAdded mpo_vnode_check_setowner_tAdded mpo_vnode_check_setutimes_tAdded mpo_vnode_check_signature_tAdded mpo_vnode_check_stat_tAdded mpo_vnode_check_truncate_tAdded mpo_vnode_check_uipc_bind_tAdded mpo_vnode_check_uipc_connect_tAdded mpo_vnode_check_unlink_tAdded mpo_vnode_check_write_tAdded mpo_vnode_find_sigs_tAdded mpo_vnode_label_associate_devfs_tAdded mpo_vnode_label_associate_extattr_tAdded mpo_vnode_label_associate_file_tAdded mpo_vnode_label_associate_pipe_tAdded mpo_vnode_label_associate_posixsem_tAdded mpo_vnode_label_associate_posixshm_tAdded mpo_vnode_label_associate_singlelabel_tAdded mpo_vnode_label_associate_socket_tAdded mpo_vnode_label_copy_tAdded mpo_vnode_label_destroy_tAdded mpo_vnode_label_externalize_audit_tAdded mpo_vnode_label_externalize_tAdded mpo_vnode_label_init_tAdded mpo_vnode_label_internalize_tAdded mpo_vnode_label_recycle_tAdded mpo_vnode_label_store_tAdded mpo_vnode_label_update_extattr_tAdded mpo_vnode_label_update_tAdded mpo_vnode_notify_create_tAdded mpo_vnode_notify_link_tAdded mpo_vnode_notify_open_tAdded mpo_vnode_notify_rename_tAdded #def POLICY_VER

#### sys/_types/_timeval64.h (Added)

Added [timeval64](https://developer.apple.com/documentation/kernel/timeval64)

#### sys/disk.h

Removed #def DKIOCGETBLOCKCOUNT32Added #def DK_CORESTORAGE_ENABLE_HOTFILESAdded [dk_corestorage_info_t](https://developer.apple.com/documentation/kernel/dk_corestorage_info_t)Added #def DK_CORESTORAGE_PIN_YOUR_METADATAAdded #def DK_CORESTORAGE_PIN_YOUR_SWAPFILEAdded #def DK_FEATURE_BARRIERAdded #def DK_SYNCHRONIZE_OPTION_BARRIERAdded [dk_synchronize_t](https://developer.apple.com/documentation/kernel/dk_synchronize_t)Added #def DKIOCCORESTORAGEAdded #def DKIOCSYNCHRONIZE

#### sys/event.h

Added #def EV_DISPATCH2Added #def EV_UDATA_SPECIFICAdded #def KEVENT_FLAG_ERROR_EVENTSAdded #def KEVENT_FLAG_IMMEDIATEAdded #def KEVENT_FLAG_NONE

#### sys/fcntl.h

Added #def F_ADDFILESIGS_FOR_DYLD_SIMAdded #def F_ADDFILESIGS_RETURNAdded #def F_BARRIERFSYNCAdded #def F_OFD_LOCKAdded #def FUNENCRYPTEDAdded #def O_DP_GETRAWUNENCRYPTED

#### sys/kauth.h

Added #def fsec_aceAdded #def fsec_entrycountAdded #def fsec_flagsAdded groupmember()Added #def KAUTH_ACE_ALARMAdded #def KAUTH_ACE_AUDITAdded #def KAUTH_ACE_DENYAdded #def KAUTH_ACE_DIRECTORY_INHERITAdded #def KAUTH_ACE_FAILUREAdded #def KAUTH_ACE_FILE_INHERITAdded #def KAUTH_ACE_GENERIC_ALLAdded #def KAUTH_ACE_GENERIC_EXECUTEAdded #def KAUTH_ACE_GENERIC_READAdded #def KAUTH_ACE_GENERIC_WRITEAdded #def KAUTH_ACE_INHERIT_CONTROL_FLAGSAdded #def KAUTH_ACE_INHERITEDAdded #def KAUTH_ACE_KINDMASKAdded #def KAUTH_ACE_LIMIT_INHERITAdded #def KAUTH_ACE_ONLY_INHERITAdded #def KAUTH_ACE_PERMITAdded kauth_ace_rights_tAdded #def KAUTH_ACE_SUCCESSAdded kauth_acl_alloc()Added #def KAUTH_ACL_COPYSIZEAdded #def KAUTH_ACL_DEFER_INHERITAdded kauth_acl_eval_tAdded #def KAUTH_ACL_FLAGS_PRIVATEAdded kauth_acl_free()Added #def KAUTH_ACL_MAX_ENTRIESAdded #def KAUTH_ACL_NO_INHERITAdded #def KAUTH_ACL_SIZEAdded [kauth_action_t](https://developer.apple.com/documentation/kernel/kauth_action_t)Added #def KAUTH_AEVAL_IN_GROUPAdded #def KAUTH_AEVAL_IN_GROUP_UNKNOWNAdded #def KAUTH_AEVAL_IS_OWNERAdded kauth_authorize_action()Added kauth_authorize_allow()Added kauth_authorize_fileop()Added kauth_authorize_process()Added kauth_cache_sizesAdded #def KAUTH_CLEAR_CACHESAdded kauth_cred_create()Added kauth_cred_find()Added kauth_cred_get()Added kauth_cred_get_with_ref()Added kauth_cred_getgid()Added kauth_cred_getguid()Added kauth_cred_getntsid()Added kauth_cred_getrgid()Added kauth_cred_getruid()Added kauth_cred_getsvgid()Added kauth_cred_getsvuid()Added kauth_cred_getuid()Added kauth_cred_gid2guid()Added kauth_cred_gid2ntsid()Added kauth_cred_grnam2guid()Added kauth_cred_guid2gid()Added kauth_cred_guid2grnam()Added kauth_cred_guid2ntsid()Added kauth_cred_guid2pwnam()Added kauth_cred_guid2uid()Added kauth_cred_ismember_gid()Added kauth_cred_ismember_guid()Added kauth_cred_issuser()Added kauth_cred_label_update()Added kauth_cred_ntsid2gid()Added kauth_cred_ntsid2guid()Added kauth_cred_ntsid2uid()Added kauth_cred_proc_ref()Added kauth_cred_pwnam2guid()Added kauth_cred_ref()Added kauth_cred_rele()Added kauth_cred_uid2guid()Added kauth_cred_uid2ntsid()Added kauth_cred_unref()Added #def KAUTH_DEBUGAdded kauth_deregister_scope()Added #def KAUTH_ENDIAN_DISKAdded #def KAUTH_ENDIAN_HOSTAdded #def KAUTH_EXTLOOKUP_BADRQAdded #def KAUTH_EXTLOOKUP_DEREGISTERAdded #def KAUTH_EXTLOOKUP_FAILUREAdded #def KAUTH_EXTLOOKUP_FATALAdded #def KAUTH_EXTLOOKUP_INPROGAdded #def KAUTH_EXTLOOKUP_ISMEMBERAdded #def KAUTH_EXTLOOKUP_REGISTERAdded #def KAUTH_EXTLOOKUP_RESULTAdded #def KAUTH_EXTLOOKUP_SUCCESSAdded #def KAUTH_EXTLOOKUP_VALID_GGUIDAdded #def KAUTH_EXTLOOKUP_VALID_GIDAdded #def KAUTH_EXTLOOKUP_VALID_GRNAMAdded #def KAUTH_EXTLOOKUP_VALID_GSIDAdded #def KAUTH_EXTLOOKUP_VALID_MEMBERSHIPAdded #def KAUTH_EXTLOOKUP_VALID_PWNAMAdded #def KAUTH_EXTLOOKUP_VALID_SUPGRPSAdded #def KAUTH_EXTLOOKUP_VALID_UGUIDAdded #def KAUTH_EXTLOOKUP_VALID_UIDAdded #def KAUTH_EXTLOOKUP_VALID_USIDAdded #def KAUTH_EXTLOOKUP_WANT_GGUIDAdded #def KAUTH_EXTLOOKUP_WANT_GIDAdded #def KAUTH_EXTLOOKUP_WANT_GRNAMAdded #def KAUTH_EXTLOOKUP_WANT_GSIDAdded #def KAUTH_EXTLOOKUP_WANT_MEMBERSHIPAdded #def KAUTH_EXTLOOKUP_WANT_PWNAMAdded #def KAUTH_EXTLOOKUP_WANT_SUPGRPSAdded #def KAUTH_EXTLOOKUP_WANT_UGUIDAdded #def KAUTH_EXTLOOKUP_WANT_UIDAdded #def KAUTH_EXTLOOKUP_WANT_USIDAdded #def KAUTH_EXTLOOKUP_WORKERAdded #def KAUTH_FILEOP_CLOSEAdded #def KAUTH_FILEOP_CLOSE_MODIFIEDAdded #def KAUTH_FILEOP_DELETEAdded #def KAUTH_FILEOP_EXCHANGEAdded #def KAUTH_FILEOP_EXECAdded #def KAUTH_FILEOP_LINKAdded #def KAUTH_FILEOP_OPENAdded #def KAUTH_FILEOP_RENAMEAdded kauth_filesec_alloc()Added #def KAUTH_FILESEC_COPYSIZEAdded #def KAUTH_FILESEC_COUNTAdded #def KAUTH_FILESEC_DEFER_INHERITAdded #def KAUTH_FILESEC_FLAGS_PRIVATEAdded kauth_filesec_free()Added #def KAUTH_FILESEC_MAGICAdded #def KAUTH_FILESEC_NO_INHERITAdded #def KAUTH_FILESEC_NOACLAdded #def KAUTH_FILESEC_NONEAdded #def KAUTH_FILESEC_SIZEAdded #def KAUTH_FILESEC_VALIDAdded #def KAUTH_FILESEC_WANTEDAdded #def KAUTH_FILESEC_XATTRAdded #def KAUTH_GENERIC_ISSUSERAdded #def KAUTH_GET_CACHE_SIZESAdded kauth_getgid()Added kauth_getruid()Added kauth_getuid()Added #def KAUTH_GID_NONEAdded kauth_guid_equal()Added kauth_identity_extlookupAdded #def KAUTH_INVALIDATE_CACHED_RIGHTSAdded kauth_lck_grpAdded kauth_listen_scope()Added kauth_listener_tAdded #def KAUTH_NTSID_HDRSIZEAdded #def KAUTH_NTSID_MAX_AUTHORITIESAdded #def KAUTH_NTSID_SIZEAdded kauth_null_guidAdded kauth_proc_label_update()Added #def KAUTH_PROCESS_CANSIGNALAdded #def KAUTH_PROCESS_CANTRACEAdded kauth_register_scope()Added #def KAUTH_RESULT_ALLOWAdded #def KAUTH_RESULT_DEFERAdded #def KAUTH_RESULT_DENYAdded kauth_scope_callback_tAdded #def KAUTH_SCOPE_FILEOPAdded #def KAUTH_SCOPE_GENERICAdded #def KAUTH_SCOPE_PROCESSAdded kauth_scope_tAdded #def KAUTH_SCOPE_VNODEAdded #def KAUTH_SET_CACHE_SIZESAdded #def KAUTH_UID_NONEAdded kauth_unlisten_scope()Added #def KAUTH_VNODE_ACCESSAdded #def KAUTH_VNODE_ADD_FILEAdded #def KAUTH_VNODE_ADD_SUBDIRECTORYAdded #def KAUTH_VNODE_APPEND_DATAAdded #def KAUTH_VNODE_CHANGE_OWNERAdded #def KAUTH_VNODE_CHECKIMMUTABLEAdded #def KAUTH_VNODE_DELETEAdded #def KAUTH_VNODE_DELETE_CHILDAdded #def KAUTH_VNODE_EXECUTEAdded #def KAUTH_VNODE_GENERIC_ALL_BITSAdded #def KAUTH_VNODE_GENERIC_EXECUTE_BITSAdded #def KAUTH_VNODE_GENERIC_READ_BITSAdded #def KAUTH_VNODE_GENERIC_WRITE_BITSAdded #def KAUTH_VNODE_LINKTARGETAdded #def KAUTH_VNODE_LIST_DIRECTORYAdded #def KAUTH_VNODE_NOIMMUTABLEAdded #def KAUTH_VNODE_READ_ATTRIBUTESAdded #def KAUTH_VNODE_READ_DATAAdded #def KAUTH_VNODE_READ_EXTATTRIBUTESAdded #def KAUTH_VNODE_READ_SECURITYAdded #def KAUTH_VNODE_SEARCHAdded #def KAUTH_VNODE_SEARCHBYANYONEAdded #def KAUTH_VNODE_SYNCHRONIZEAdded #def KAUTH_VNODE_TAKE_OWNERSHIPAdded #def KAUTH_VNODE_WRITE_ATTRIBUTESAdded #def KAUTH_VNODE_WRITE_DATAAdded #def KAUTH_VNODE_WRITE_EXTATTRIBUTESAdded #def KAUTH_VNODE_WRITE_RIGHTSAdded #def KAUTH_VNODE_WRITE_SECURITYAdded ntsid_tAdded posix_cred_access()Added posix_cred_create()Added posix_cred_get()Added posix_cred_label()Added #def VFS_DEBUG

#### sys/kdebug.h

Removed #def ATM_MIN_LINK_LISTRemoved kernel_debug_string()Removed #def MACH_FAIRSHARE_ENTERRemoved #def MACH_FAIRSHARE_EXITRemoved #def MACH_SCHED_DECAY_PRIORITYAdded #def ATM_LINK_LIST_TRIMAdded #def COREDUETDBG_CODEAdded #def DAEMONDBG_CODEAdded #def DBG_APP_APPKITAdded #def DBG_APP_SIGPOSTAdded #def DBG_DAEMONAdded #def DBG_DAEMON_COREDUETAdded #def DBG_ENERGYTRACEAdded #def DBG_HFS_UPDATE_MINORAdded #def DBG_HFS_UPDATE_SKIPPEDAdded #def DBG_MACH_CLOCKAdded #def DBG_MACH_SYSDIAGNOSEAdded #def ENTR_KDASSOCIATEAdded #def ENTR_KDTRACEAdded #def ENTR_SHOULDTRACEAdded #def KDBG_CLASS_MASKAdded #def KDBG_CLASS_MAXAdded #def KDBG_CLASS_OFFSETAdded #def KDBG_CODE_MASKAdded #def KDBG_CODE_MAXAdded #def KDBG_CODE_OFFSETAdded #def KDBG_CSC_MASKAdded #def KDBG_CSC_OFFSETAdded #def KDBG_EVENTIDAdded #def KDBG_EVENTID_MASKAdded #def KDBG_EXTRACT_CLASSAdded #def KDBG_EXTRACT_CODEAdded #def KDBG_EXTRACT_CSCAdded #def KDBG_EXTRACT_SUBCLASSAdded #def KDBG_SUBCLASS_MASKAdded #def KDBG_SUBCLASS_MAXAdded #def KDBG_SUBCLASS_OFFSETAdded #def kEnTrActKernKQWaitAdded #def kEnTrActKernPollAdded #def kEnTrActKernSelectAdded #def kEnTrActKernSocketAdded #def kEnTrActKernSockReadAdded #def kEnTrActKernSockWriteAdded #def kEnTrCompKernelAdded #def kEnTrEvUnblockedAdded #def kEnTrFlagNonBlockingAdded #def kEnTrFlagNoWorkAdded #def kEnTrModAssociateAdded #def MACH_EPOCH_CHANGEAdded #def MACH_REMOTE_CANCEL_ASTAdded #def MACH_REMOTE_DEFERRED_ASTAdded #def MACH_SCHED_CHANGE_PRIORITYAdded #def MACH_SCHED_UPDATE_REC_CORESAdded #def MACH_STACK_WAITAdded #def MACH_THREAD_BINDAdded #def MACH_WAITQ_DEMOTEAdded #def MACH_WAITQ_PROMOTEAdded #def PMAP__FLUSH_EPTAdded #def SYSDIAGNOSE_NOTIFY_USERAdded #def TRACE_STRING_GLOBAL

#### sys/lctx.h (Removed)

Removed #def LCID_CREATERemoved #def LCID_PROC_SELFRemoved #def LCID_REMOVE

#### sys/mman.h

Added #def MADV_PAGEOUTAdded #def MAP_ANONYMOUSAdded #def MAP_RESILIENT_CODESIGNAdded #def MAP_RESILIENT_MEDIA

#### sys/proc.h

Added [proc_chrooted()](https://developer.apple.com/documentation/kernel/1488999-proc_chrooted)

#### sys/sbuf.h

Added sbufAdded #def SBUF_AUTOEXTENDAdded sbuf_bcat()Added sbuf_bcopyin()Added sbuf_bcpy()Added sbuf_cat()Added sbuf_clear()Added sbuf_copyin()Added sbuf_cpy()Added sbuf_data()Added sbuf_delete()Added sbuf_done()Added #def SBUF_DYNAMICAdded #def SBUF_DYNSTRUCTAdded sbuf_finish()Added #def SBUF_FINISHEDAdded #def SBUF_FIXEDLENAdded sbuf_len()Added sbuf_new()Added sbuf_overflowed()Added #def SBUF_OVERFLOWEDAdded sbuf_printf()Added sbuf_putc()Added sbuf_setpos()Added sbuf_trim()Added sbuf_uionew()Added #def SBUF_USRFLAGMSKAdded sbuf_vprintf()

#### sys/socket.h

Added #def CONNECT_DATA_IDEMPOTENTAdded #def CONNECT_RESUME_ON_READ_WRITEAdded [sa_endpoints_t](https://developer.apple.com/documentation/kernel/sa_endpoints_t)Added #def SAE_ASSOCID_ALLAdded #def SAE_ASSOCID_ANYAdded [sae_associd_t](https://developer.apple.com/documentation/kernel/sae_associd_t)Added #def SAE_CONNID_ALLAdded #def SAE_CONNID_ANYAdded [sae_connid_t](https://developer.apple.com/documentation/kernel/sae_connid_t)

#### sys/socketvar.h

Added [so_gen_t](https://developer.apple.com/documentation/kernel/so_gen_t)Added [xsockbuf](https://developer.apple.com/documentation/kernel/xsockbuf)Added [xsocket](https://developer.apple.com/documentation/kernel/xsocket)Added [xsocket64](https://developer.apple.com/documentation/kernel/xsocket64)

#### sys/stat.h

Added #def SF_NOUNLINKAdded #def SF_SUPPORTED

#### sys/syscall.h

Removed #def SYS___mac_get_lcidRemoved #def SYS___mac_get_lctxRemoved #def SYS___mac_set_lctxRemoved #def SYS_getlcidRemoved #def SYS_setlcidAdded #def SYS_grab_pgo_dataAdded #def SYS_kdebug_trace_stringAdded #def SYS_kevent_qosAdded #def SYS_microstackshotAdded #def SYS_netagent_triggerAdded #def SYS_stack_snapshot_with_configAdded #def SYS_work_interval_ctl

#### sys/systm.h

Modified [throttle_info_disable_throttle()](https://developer.apple.com/documentation/kernel/1519606-throttle_info_disable_throttle)

|  | Declaration |
| --- | --- |
| From | ``` void throttle_info_disable_throttle (     int devno ); ``` |
| To | ``` void throttle_info_disable_throttle (     int devno,     boolean_t isfusion ); ``` |

#### sys/ubc.h

Added [cl_direct_read_lock_t](https://developer.apple.com/documentation/kernel/cl_direct_read_lock_t)Added [cluster_lock_direct_read()](https://developer.apple.com/documentation/kernel/1463706-cluster_lock_direct_read)Added [cluster_unlock_direct_read()](https://developer.apple.com/documentation/kernel/1463731-cluster_unlock_direct_read)Added [mach_to_bsd_errno()](https://developer.apple.com/documentation/kernel/1463711-mach_to_bsd_errno)

#### sys/vnode.h

Added #def IO_EVTONLYAdded [vfs_get_notify_attributes()](https://developer.apple.com/documentation/kernel/1562277-vfs_get_notify_attributes)Added [vnode_clearautocandidate()](https://developer.apple.com/documentation/kernel/1562373-vnode_clearautocandidate)Added [vnode_clearfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562403-vnode_clearfastdevicecandidate)Added [vnode_isautocandidate()](https://developer.apple.com/documentation/kernel/1562339-vnode_isautocandidate)Added [vnode_isfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562391-vnode_isfastdevicecandidate)Added #def VNODE_LOOKUP_CROSSMOUNTNOWAITAdded [vnode_notify()](https://developer.apple.com/documentation/kernel/1562393-vnode_notify)Added #def VNODE_REMOVE_NO_AUDIT_PATHAdded [vnode_setautocandidate()](https://developer.apple.com/documentation/kernel/1562116-vnode_setautocandidate)Added [vnode_setfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562221-vnode_setfastdevicecandidate)

#### vecLib/vDSP.h

Added [vDSP_biquadm_SetActiveFilters()](https://developer.apple.com/documentation/kernel/1579973-vdsp_biquadm_setactivefilters)Added [vDSP_biquadm_SetCoefficientsDouble()](https://developer.apple.com/documentation/accelerate/1450453-vdsp_biquadm_setcoefficientsdoub)Added [vDSP_biquadm_SetCoefficientsSingle()](https://developer.apple.com/documentation/accelerate/1450128-vdsp_biquadm_setcoefficientssing)Added [vDSP_biquadm_SetTargetsDouble()](https://developer.apple.com/documentation/kernel/1580010-vdsp_biquadm_settargetsdouble)Added [vDSP_biquadm_SetTargetsSingle()](https://developer.apple.com/documentation/accelerate/1450077-vdsp_biquadm_settargetssingle)Modified [vDSP_biquadm()](https://developer.apple.com/documentation/accelerate/1450603-vdsp_biquadm)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm (     vDSP_biquadm_Setup __vDSP_Setup,     const float **__vDSP_X,     vDSP_Stride __vDSP_IX,     float **__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquadm (     vDSP_biquadm_Setup _Nonnull __Setup,     const float * _Nonnull * _Nonnull __X,     vDSP_Stride __IX,     float * _Nonnull * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_CopyState()](https://developer.apple.com/documentation/kernel/1579980-vdsp_biquadm_copystate)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_CopyState (     vDSP_biquadm_Setup __vDSP_dest,     const struct vDSP_biquadm_SetupStruct *__vDSP_src ); ``` |
| To | ``` void vDSP_biquadm_CopyState (     vDSP_biquadm_Setup _Nonnull __dest,     const struct vDSP_biquadm_SetupStruct * _Nonnull __src ); ``` |

Modified [vDSP_biquadm_CopyStateD()](https://developer.apple.com/documentation/kernel/1580000-vdsp_biquadm_copystated)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_CopyStateD (     vDSP_biquadm_SetupD __vDSP_dest,     const struct vDSP_biquadm_SetupStructD *__vDSP_src ); ``` |
| To | ``` void vDSP_biquadm_CopyStateD (     vDSP_biquadm_SetupD _Nonnull __dest,     const struct vDSP_biquadm_SetupStructD * _Nonnull __src ); ``` |

Modified [vDSP_biquadm_CreateSetup()](https://developer.apple.com/documentation/kernel/1579945-vdsp_biquadm_createsetup)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquadm_Setup vDSP_biquadm_CreateSetup (     const double *__vDSP_coeffs,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` vDSP_biquadm_Setup _Nullable vDSP_biquadm_CreateSetup (     const double * _Nonnull __coeffs,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_CreateSetupD()](https://developer.apple.com/documentation/accelerate/1449719-vdsp_biquadm_createsetupd)

|  | Declaration |
| --- | --- |
| From | ``` vDSP_biquadm_SetupD vDSP_biquadm_CreateSetupD (     const double *__vDSP_coeffs,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N ); ``` |
| To | ``` vDSP_biquadm_SetupD _Nullable vDSP_biquadm_CreateSetupD (     const double * _Nonnull __coeffs,     vDSP_Length __M,     vDSP_Length __N ); ``` |

Modified [vDSP_biquadm_DestroySetup()](https://developer.apple.com/documentation/kernel/1579970-vdsp_biquadm_destroysetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_DestroySetup (     vDSP_biquadm_Setup __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_DestroySetup (     vDSP_biquadm_Setup _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_DestroySetupD()](https://developer.apple.com/documentation/accelerate/1450779-vdsp_biquadm_destroysetupd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_DestroySetupD (     vDSP_biquadm_SetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_DestroySetupD (     vDSP_biquadm_SetupD _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_ResetState()](https://developer.apple.com/documentation/accelerate/1449898-vdsp_biquadm_resetstate)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_ResetState (     vDSP_biquadm_Setup __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_ResetState (     vDSP_biquadm_Setup _Nonnull __setup ); ``` |

Modified [vDSP_biquadm_ResetStateD()](https://developer.apple.com/documentation/kernel/1579935-vdsp_biquadm_resetstated)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadm_ResetStateD (     vDSP_biquadm_SetupD __vDSP_setup ); ``` |
| To | ``` void vDSP_biquadm_ResetStateD (     vDSP_biquadm_SetupD _Nonnull __setup ); ``` |

Modified [vDSP_biquadmD()](https://developer.apple.com/documentation/accelerate/1450102-vdsp_biquadmd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_biquadmD (     vDSP_biquadm_SetupD __vDSP_Setup,     const double **__vDSP_X,     vDSP_Stride __vDSP_IX,     double **__vDSP_Y,     vDSP_Stride __vDSP_IY,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_biquadmD (     vDSP_biquadm_SetupD _Nonnull __Setup,     const double * _Nonnull * _Nonnull __X,     vDSP_Stride __IX,     double * _Nonnull * _Nonnull __Y,     vDSP_Stride __IY,     vDSP_Length __N ); ``` |

Modified [vDSP_conv()](https://developer.apple.com/documentation/kernel/1532184-vdsp_conv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_conv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_F,     vDSP_Stride __vDSP_IF,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_conv (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __F,     vDSP_Stride __IF,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_create_fftsetup()](https://developer.apple.com/documentation/kernel/1580009-vdsp_create_fftsetup)

|  | Declaration |
| --- | --- |
| From | ``` FFTSetup vDSP_create_fftsetup (     vDSP_Length __vDSP_Log2n,     FFTRadix __vDSP_Radix ); ``` |
| To | ``` FFTSetup _Nullable vDSP_create_fftsetup (     vDSP_Length __Log2n,     FFTRadix __Radix ); ``` |

Modified [vDSP_ctoz()](https://developer.apple.com/documentation/kernel/1579975-vdsp_ctoz)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ctoz (     const DSPComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     const DSPSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ctoz (     const DSPComplex * _Nonnull __C,     vDSP_Stride __IC,     const DSPSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     vDSP_Length __N ); ``` |

Modified [vDSP_deq22()](https://developer.apple.com/documentation/kernel/1532225-vdsp_deq22)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_deq22 (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_deq22 (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_destroy_fftsetup()](https://developer.apple.com/documentation/accelerate/1450396-vdsp_destroy_fftsetup)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_destroy_fftsetup (     FFTSetup __vDSP_setup ); ``` |
| To | ``` void vDSP_destroy_fftsetup (     FFTSetup _Nullable __setup ); ``` |

Modified [vDSP_fft_zrip()](https://developer.apple.com/documentation/kernel/1579997-vdsp_fft_zrip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_fft_zrip (     FFTSetup __vDSP_Setup,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_Log2N,     FFTDirection __vDSP_Direction ); ``` |
| To | ``` void vDSP_fft_zrip (     FFTSetup _Nonnull __Setup,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __Log2N,     FFTDirection __Direction ); ``` |

Modified [vDSP_maxmgv()](https://developer.apple.com/documentation/kernel/1532187-vdsp_maxmgv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxmgv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxmgv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_maxv()](https://developer.apple.com/documentation/kernel/1580003-vdsp_maxv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_maxv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_maxv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_minv()](https://developer.apple.com/documentation/accelerate/1450267-vdsp_minv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_minv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_minv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_rmsqv()](https://developer.apple.com/documentation/accelerate/1450655-vdsp_rmsqv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_rmsqv (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_rmsqv (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svdiv()](https://developer.apple.com/documentation/accelerate/1450412-vdsp_svdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svdiv (     const float *__vDSP_A,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svdiv (     const float * _Nonnull __A,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_sve()](https://developer.apple.com/documentation/kernel/1579937-vdsp_sve)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sve (     const float *__vDSP_A,     vDSP_Stride __vDSP_I,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sve (     const float * _Nonnull __A,     vDSP_Stride __I,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_sve_svesq()](https://developer.apple.com/documentation/kernel/1579989-vdsp_sve_svesq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_sve_svesq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_Sum,     float *__vDSP_SumOfSquares,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_sve_svesq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __Sum,     float * _Nonnull __SumOfSquares,     vDSP_Length __N ); ``` |

Modified [vDSP_svesq()](https://developer.apple.com/documentation/accelerate/1450392-vdsp_svesq)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svesq (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svesq (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_svs()](https://developer.apple.com/documentation/kernel/1532174-vdsp_svs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_svs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_svs (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Length __N ); ``` |

Modified [vDSP_vabs()](https://developer.apple.com/documentation/kernel/1532216-vdsp_vabs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vabs (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vabs (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vadd()](https://developer.apple.com/documentation/kernel/1532191-vdsp_vadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vadd (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vadd (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vclip()](https://developer.apple.com/documentation/accelerate/1450071-vdsp_vclip)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclip (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     const float *__vDSP_C,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclip (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     const float * _Nonnull __C,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vclr()](https://developer.apple.com/documentation/accelerate/1450402-vdsp_vclr)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vclr (     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vclr (     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vdbcon()](https://developer.apple.com/documentation/accelerate/1450241-vdsp_vdbcon)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdbcon (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     unsigned int __vDSP_F ); ``` |
| To | ``` void vDSP_vdbcon (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     unsigned int __F ); ``` |

Modified [vDSP_vdiv()](https://developer.apple.com/documentation/accelerate/1450243-vdsp_vdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vdiv (     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vdiv (     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfill (     const float *__vDSP_A,     float *__vDSP_C,     vDSP_Stride __vDSP_IA,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vfill (     const float * _Nonnull __A,     float * _Nonnull __C,     vDSP_Stride __IA,     vDSP_Length __N ); ``` |

Modified [vDSP_vma()](https://developer.apple.com/documentation/kernel/1532193-vdsp_vma)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vma (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_C,     vDSP_Stride __vDSP_IC,     float *__vDSP_D,     vDSP_Stride __vDSP_ID,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vma (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __C,     vDSP_Stride __IC,     float * _Nonnull __D,     vDSP_Stride __ID,     vDSP_Length __N ); ``` |

Modified [vDSP_vmax()](https://developer.apple.com/documentation/kernel/1579953-vdsp_vmax)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmax (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmax (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmaxmg()](https://developer.apple.com/documentation/accelerate/1450295-vdsp_vmaxmg)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmaxmg (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmaxmg (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vmul()](https://developer.apple.com/documentation/accelerate/1450344-vdsp_vmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vmul (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vmul (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     vDSP_Stride __IB,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsadd()](https://developer.apple.com/documentation/kernel/1579993-vdsp_vsadd)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsadd (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsadd (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsmul()](https://developer.apple.com/documentation/kernel/1532223-vdsp_vsmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsmul (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     const float *__vDSP_B,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsmul (     const float * _Nonnull __A,     vDSP_Stride __IA,     const float * _Nonnull __B,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vsub()](https://developer.apple.com/documentation/accelerate/1449900-vdsp_vsub)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vsub (     const float *__vDSP_B,     vDSP_Stride __vDSP_IB,     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_vsub (     const float * _Nonnull __B,     vDSP_Stride __IB,     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_vswmax()](https://developer.apple.com/documentation/kernel/1579990-vdsp_vswmax)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vswmax (     const float *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_WindowLength ); ``` |
| To | ``` void vDSP_vswmax (     const float * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     vDSP_Length __WindowLength ); ``` |

Modified [vDSP_zmmul()](https://developer.apple.com/documentation/accelerate/1449712-vdsp_zmmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zmmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_M,     vDSP_Length __vDSP_N,     vDSP_Length __vDSP_P ); ``` |
| To | ``` void vDSP_zmmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __M,     vDSP_Length __N,     vDSP_Length __P ); ``` |

Modified [vDSP_ztoc()](https://developer.apple.com/documentation/kernel/1579934-vdsp_ztoc)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_ztoc (     const DSPSplitComplex *__vDSP_Z,     vDSP_Stride __vDSP_IZ,     DSPComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_ztoc (     const DSPSplitComplex * _Nonnull __Z,     vDSP_Stride __IZ,     DSPComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvabs()](https://developer.apple.com/documentation/kernel/1579998-vdsp_zvabs)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvabs (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     float *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvabs (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     float * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvdiv()](https://developer.apple.com/documentation/accelerate/1449769-vdsp_zvdiv)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvdiv (     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvdiv (     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmov()](https://developer.apple.com/documentation/kernel/1579979-vdsp_zvmov)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmov (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N ); ``` |
| To | ``` void vDSP_zvmov (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

Modified [vDSP_zvmul()](https://developer.apple.com/documentation/kernel/1579954-vdsp_zvmul)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_zvmul (     const DSPSplitComplex *__vDSP_A,     vDSP_Stride __vDSP_IA,     const DSPSplitComplex *__vDSP_B,     vDSP_Stride __vDSP_IB,     const DSPSplitComplex *__vDSP_C,     vDSP_Stride __vDSP_IC,     vDSP_Length __vDSP_N,     int __vDSP_Conjugate ); ``` |
| To | ``` void vDSP_zvmul (     const DSPSplitComplex * _Nonnull __A,     vDSP_Stride __IA,     const DSPSplitComplex * _Nonnull __B,     vDSP_Stride __IB,     const DSPSplitComplex * _Nonnull __C,     vDSP_Stride __IC,     vDSP_Length __N,     int __Conjugate ); ``` |

#### vecLib/vForce.h

Modified [vvexpf()](https://developer.apple.com/documentation/kernel/1532176-vvexpf)

|  | Declaration |
| --- | --- |
| From | ``` void vvexpf (     float *,     const float *,     const int * ); ``` |
| To | ``` void vvexpf (     float * _Nonnull,     const float * _Nonnull,     const int * _Nonnull ); ``` |

#### vm/vm_kern.h

Added [vm_kernel_addrperm_ext](https://developer.apple.com/documentation/kernel/vm_kernel_addrperm_ext)Added [vm_kernel_addrperm_external()](https://developer.apple.com/documentation/kernel/1401818-vm_kernel_addrperm_external)Added [vm_kernel_unslide_or_perm_external()](https://developer.apple.com/documentation/kernel/1401816-vm_kernel_unslide_or_perm_extern)

#### vm/WKdm_new.h

Modified [WKdm_compress_new()](https://developer.apple.com/documentation/kernel/1473458-wkdm_compress_new)

|  | Declaration |
| --- | --- |
| From | ``` int WKdm_compress_new (     WK_word *src_buf,     WK_word *dest_buf,     WK_word *scratch,     unsigned int limit ); ``` |
| To | ``` int WKdm_compress_new (     const WK_word *src_buf,     WK_word *dest_buf,     WK_word *scratch,     unsigned int limit ); ``` |

#### x86_64/machine_kpc.h

Modified #def CONFIGURABLE_ACTIONID

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def CONFIGURABLE_RELOAD

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def CONFIGURABLE_SHADOW

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_ACTIONID

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_RELOAD

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

Modified #def FIXED_SHADOW

|  | Removal | Header |
| --- | --- | --- |
| From | -- | Kernel/x86_64/machine_kpc.h |
| To | OS X 10.11 | Kernel/kern/kpc.h |

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

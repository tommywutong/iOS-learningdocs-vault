---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Kernel.html
archived_at: '2026-07-18T02:50:40.146559Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Kernel Changes for Objective-C

### Kernel

#### atm/atm_types.h

Added #def ATM_ENABLE_LEGACY_LOGGINGAdded #def ATM_TRACE_OFF

#### corpses/task_corpse.h

Modified #def TASK_CRASHINFO_ARGSLEN

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_BEGIN

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_BSDINFOWITHUNIQID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_CPUTYPE

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_CRASHED_THREADID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_DIRTY_FLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_END

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_EXCEPTION_CODES

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_EXTMODINFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_GID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PPID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_ARGC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_CSFLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_FLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_NAME

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_PATH

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_STARTTIME

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_STATUS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RESPONSIBLE_PID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RUSAGE

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RUSAGE_INFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_STRING_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_TASKDYLD_INFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UINT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UINT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_USERSTACK

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UUID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_WORKQUEUEINFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

#### default_pager/default_pager_object.h (Removed)

Removed default_pager_add_file()Removed default_pager_backing_store_create()Removed default_pager_backing_store_delete()Removed default_pager_backing_store_info()Removed default_pager_info()Removed default_pager_info_64()Removed default_pager_object_create()Removed #def default_pager_object_MSG_COUNTRemoved default_pager_object_pages()Removed default_pager_objects()Removed default_pager_triggers()Removed #def subsystem_to_name_map_default_pager_object

#### default_pager/default_pager_types.h

Removed #def BACKING_STORE_BASIC_INFORemoved #def BACKING_STORE_BASIC_INFO_COUNTRemoved backing_store_basic_info_tRemoved backing_store_flavor_tRemoved backing_store_info_tRemoved #def DEFAULT_PAGER_BACKING_STORE_MAXPRIRemoved default_pager_info_64_tRemoved default_pager_info_tRemoved default_pager_object_array_tRemoved default_pager_object_tRemoved default_pager_page_array_tRemoved default_pager_page_tRemoved default_pager_tRemoved #def DPI_ENCRYPTEDRemoved vnode_ptr_t

#### gssd/gssd_mach.h

Added [mach_gss_init_sec_context_v3()](https://developer.apple.com/documentation/kernel/1642105-mach_gss_init_sec_context_v3)Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### gssd/gssd_mach_types.h

Added [gssd_etype_list](https://developer.apple.com/documentation/kernel/gssd_etype_list)Added #def GSSD_LUCID_CONTEXT

#### hfs/hfs_encodings.h

Added [hfs_getconverter()](https://developer.apple.com/documentation/kernel/1646506-hfs_getconverter)Added [hfs_getencodingbias()](https://developer.apple.com/documentation/kernel/1646508-hfs_getencodingbias)Added [hfs_pickencoding()](https://developer.apple.com/documentation/kernel/1646509-hfs_pickencoding)Added [hfs_relconverter()](https://developer.apple.com/documentation/kernel/1646505-hfs_relconverter)Added [hfs_setencodingbias()](https://developer.apple.com/documentation/kernel/1646502-hfs_setencodingbias)Added [mac_roman_to_unicode()](https://developer.apple.com/documentation/kernel/1646513-mac_roman_to_unicode)Added [mac_roman_to_utf8()](https://developer.apple.com/documentation/kernel/1646507-mac_roman_to_utf8)Added [unicode_to_mac_roman()](https://developer.apple.com/documentation/kernel/1646503-unicode_to_mac_roman)Added [utf8_to_mac_roman()](https://developer.apple.com/documentation/kernel/1646504-utf8_to_mac_roman)Modified #def CTL_HFS_NAMES

|  | Header |
| --- | --- |
| From | hfs/hfs_encodings.h |
| To | Kernel/hfs/hfs_encodings.h |

Modified hfs_addconverter()

|  | Header |
| --- | --- |
| From | hfs/hfs_encodings.h |
| To | Kernel/hfs/hfs_encodings.h |

Modified hfs_remconverter()

|  | Header |
| --- | --- |
| From | hfs/hfs_encodings.h |
| To | Kernel/hfs/hfs_encodings.h |

Modified [hfs_to_unicode_func_t](https://developer.apple.com/documentation/kernel/hfs_to_unicode_func_t)

|  | Header |
| --- | --- |
| From | hfs/hfs_encodings.h |
| To | Kernel/hfs/hfs_encodings.h |

Modified [unicode_to_hfs_func_t](https://developer.apple.com/documentation/kernel/unicode_to_hfs_func_t)

|  | Header |
| --- | --- |
| From | hfs/hfs_encodings.h |
| To | Kernel/hfs/hfs_encodings.h |

#### hfs/hfs_mount.h

Removed #def HFS_ENCODINGHINTRemoved #def HFS_GET_JOURNAL_INFORemoved #def HFS_SET_PKG_EXTENSIONS

#### i386/cpuid.h

Removed #def CPUID_MODEL_MEROMRemoved #def CPUID_MODEL_YONAH

#### i386/proc_reg.h

Added #def HV_VMX_EPTP_ENABLE_AD_FLAGSAdded #def HV_VMX_EPTP_MEMORY_TYPE_UCAdded #def HV_VMX_EPTP_MEMORY_TYPE_WBAdded #def HV_VMX_EPTP_WALK_LENGTH

#### i386/types.h

Modified [u_int16_t](https://developer.apple.com/documentation/kernel/u_int16_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int16_t.h |

Modified [u_int32_t](https://developer.apple.com/documentation/kernel/u_int32_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int32_t.h |

Modified [u_int64_t](https://developer.apple.com/documentation/kernel/u_int64_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int64_t.h |

Modified [u_int8_t](https://developer.apple.com/documentation/kernel/u_int8_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int8_t.h |

#### IOKit/acpi/IOACPITypes.h

Added #def kIOACPIInterruptTypeValid

#### IOKit/audio/IOAudioEngineUserClient.h

Added #def kDriverHelper_DriverHostEntitlement

#### IOKit/bluetooth/Bluetooth.h

Added [BluetoothEnhancedSynchronousConnectionInfo](https://developer.apple.com/documentation/iobluetooth/bluetoothenhancedsynchronousconnectioninfo)Added [BluetoothHCIEnhancedAcceptSynchronousConnectionRequestParams](https://developer.apple.com/documentation/iobluetooth/bluetoothhcienhancedacceptsynchronousconnectionrequestparams)Added [BluetoothHCIEnhancedSetupSynchronousConnectionParams](https://developer.apple.com/documentation/kernel/bluetoothhcienhancedsetupsynchronousconnectionparams)Added [BluetoothHCIEventLEReadRemoteUsedFeaturesCompleteResults](https://developer.apple.com/documentation/iobluetooth/bluetoothhcieventlereadremoteusedfeaturescompleteresults)Added [BluetoothHCIInputBandwidth](https://developer.apple.com/documentation/kernel/bluetoothhciinputbandwidth)Added [BluetoothHCIInputCodedDataSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputcodeddatasize)Added [BluetoothHCIInputCodingFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputcodingformat)Added [BluetoothHCIInputDataPath](https://developer.apple.com/documentation/kernel/bluetoothhciinputdatapath)Added [BluetoothHCIInputPCMDataFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputpcmdataformat)Added [BluetoothHCIInputPCMSamplePayloadMSBPosition](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputpcmsamplepayloadmsbposition)Added [BluetoothHCIInputTransportUnitSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhciinputtransportunitsize)Added [BluetoothHCILESupportedFeatures](https://developer.apple.com/documentation/iobluetooth/bluetoothhcilesupportedfeatures)Added [BluetoothHCILEUsedFeatures](https://developer.apple.com/documentation/iobluetooth/bluetoothhcileusedfeatures)Added [BluetoothHCIOutputBandwidth](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputbandwidth)Added [BluetoothHCIOutputCodedDataSize](https://developer.apple.com/documentation/kernel/bluetoothhcioutputcodeddatasize)Added [BluetoothHCIOutputCodingFormat](https://developer.apple.com/documentation/kernel/bluetoothhcioutputcodingformat)Added [BluetoothHCIOutputDataPath](https://developer.apple.com/documentation/kernel/bluetoothhcioutputdatapath)Added [BluetoothHCIOutputPCMDataFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputpcmdataformat)Added [BluetoothHCIOutputPCMSamplePayloadMSBPosition](https://developer.apple.com/documentation/iobluetooth/bluetoothhcioutputpcmsamplepayloadmsbposition)Added [BluetoothHCIOutputTransportUnitSize](https://developer.apple.com/documentation/kernel/bluetoothhcioutputtransportunitsize)Added [BluetoothHCIReceiveCodecFrameSize](https://developer.apple.com/documentation/kernel/bluetoothhcireceivecodecframesize)Added [BluetoothHCIReceiveCodingFormat](https://developer.apple.com/documentation/iobluetooth/bluetoothhcireceivecodingformat)Added [BluetoothHCITransmitCodecFrameSize](https://developer.apple.com/documentation/iobluetooth/bluetoothhcitransmitcodecframesize)Added [BluetoothHCITransmitCodingFormat](https://developer.apple.com/documentation/kernel/bluetoothhcitransmitcodingformat)Added [BluetoothL2CAPSegmentationAndReassembly](https://developer.apple.com/documentation/kernel/bluetoothl2capsegmentationandreassembly)Added [BluetoothL2CAPSupervisoryFuctionType](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capsupervisoryfuctiontype)Added [BluetoothLEFeatureBits](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits)Added [kBluetoothHCIErrorCoarseClockAdjustmentRejected](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcierrorcoarseclockadjustmentrejected)Added [kBluetoothHCISubEventLEDataLengthChange](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventledatalengthchange)Added [kBluetoothHCISubEventLEDirectAdvertisingReport](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventledirectadvertisingreport)Added [kBluetoothHCISubEventLEEnhancedConnectionComplete](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventleenhancedconnectioncomplete)Added [kBluetoothHCISubEventLEGenerateDHKeyComplete](https://developer.apple.com/documentation/kernel/1639977-anonymous/kbluetoothhcisubeventlegeneratedhkeycomplete)Added [kBluetoothHCISubEventLEReadLocalP256PublicKeyComplete](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcisubeventlereadlocalp256publickeycomplete)Added [kBluetoothHCISubEventLERemoteConnectionParameterRequest](https://developer.apple.com/documentation/iobluetooth/1490041-anonymous/kbluetoothhcisubeventleremoteconnectionparameterrequest)Added [kBluetoothL2CAPConnectionResultRefusedInvalidSourceCID](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedinvalidsourcecid)Added [kBluetoothL2CAPConnectionResultRefusedReserved](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedreserved)Added [kBluetoothL2CAPConnectionResultRefusedSourceCIDAlreadyAllocated](https://developer.apple.com/documentation/kernel/bluetoothl2capconnectionresult/kbluetoothl2capconnectionresultrefusedsourcecidalreadyallocated)Added [kBluetoothL2CAPMTULowEnergyMax](https://developer.apple.com/documentation/iobluetooth/1489801-anonymous/kbluetoothl2capmtulowenergymax)Added [kBluetoothL2CAPSegmentationAndReassemblyContinuationOfSDU](https://developer.apple.com/documentation/iobluetooth/bluetoothl2capsegmentationandreassembly/kbluetoothl2capsegmentationandreassemblycontinuationofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyEndOfSDU](https://developer.apple.com/documentation/kernel/bluetoothl2capsegmentationandreassembly/kbluetoothl2capsegmentationandreassemblyendofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyStartOfSDU](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsegmentationandreassemblystartofsdu)Added [kBluetoothL2CAPSegmentationAndReassemblyUnsegmentedSDU](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsegmentationandreassemblyunsegmentedsdu)Added [kBluetoothL2CAPSupervisoryFuctionTypeReceiverNotReady](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereceivernotready)Added [kBluetoothL2CAPSupervisoryFuctionTypeReceiverReady](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereceiverready)Added [kBluetoothL2CAPSupervisoryFuctionTypeReject](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypereject)Added [kBluetoothL2CAPSupervisoryFuctionTypeSelectiveReject](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2capsupervisoryfuctiontypeselectivereject)Added [kBluetoothLEFeatureConnectionParamsRequestProcedure](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureconnectionparamsrequestprocedure)Added [kBluetoothLEFeatureExtendedRejectIndication](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureextendedrejectindication)Added [kBluetoothLEFeatureExtendedScannerFilterPolicies](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureextendedscannerfilterpolicies)Added [kBluetoothLEFeatureLEDataPacketLengthExtension](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureledatapacketlengthextension)Added [kBluetoothLEFeatureLEEncryption](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureleencryption)Added [kBluetoothLEFeatureLEPing](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeatureleping)Added [kBluetoothLEFeatureLLPrivacy](https://developer.apple.com/documentation/kernel/bluetoothlefeaturebits/kbluetoothlefeaturellprivacy)Added [kBluetoothLEFeatureSlaveInitiatedFeaturesExchange](https://developer.apple.com/documentation/iobluetooth/bluetoothlefeaturebits/kbluetoothlefeatureslaveinitiatedfeaturesexchange)Added [kBluetoothLEMaxTXOctetsDefault](https://developer.apple.com/documentation/iobluetooth/kbluetoothlemaxtxoctetsdefault)Added [kBluetoothLEMaxTXOctetsMax](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxoctetsmax)Added [kBluetoothLEMaxTXOctetsMin](https://developer.apple.com/documentation/iobluetooth/kbluetoothlemaxtxoctetsmin)Added [kBluetoothLEMaxTXTimeDefault](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimedefault)Added [kBluetoothLEMaxTXTimeMax](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimemax)Added [kBluetoothLEMaxTXTimeMin](https://developer.apple.com/documentation/iobluetooth/1643068-anonymous/kbluetoothlemaxtxtimemin)Added [kBluetoothLETXOctetsDefault](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxoctetsdefault)Added [kBluetoothLETXOctetsMax](https://developer.apple.com/documentation/kernel/1639933-anonymous/kbluetoothletxoctetsmax)Added [kBluetoothLETXOctetsMin](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxoctetsmin)Added [kBluetoothLETXTimeDefault](https://developer.apple.com/documentation/kernel/1639933-anonymous/kbluetoothletxtimedefault)Added [kBluetoothLETXTimeMax](https://developer.apple.com/documentation/iobluetooth/kbluetoothletxtimemax)Added [kBluetoothLETXTimeMin](https://developer.apple.com/documentation/iobluetooth/1642841-anonymous/kbluetoothletxtimemin)

#### IOKit/bluetooth/BluetoothAssignedNumbers.h

Added [kBluetoothHCIExtendedInquiryResponseDataType3DInformationData](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatype3dinformationdata)Added [kBluetoothHCIExtendedInquiryResponseDataTypeAdvertisingInterval](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeadvertisinginterval)Added [kBluetoothHCIExtendedInquiryResponseDataTypeLEBluetoothDeviceAddress](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypelebluetoothdeviceaddress)Added [kBluetoothHCIExtendedInquiryResponseDataTypeLERole](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypelerole)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsConfirmationValue](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecureconnectionsconfirmationvalue)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSecureConnectionsRandomValue](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesecureconnectionsrandomvalue)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceData128BitUUID](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicedata128bituuid)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceData32BitUUID](https://developer.apple.com/documentation/iobluetooth/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypeservicedata32bituuid)Added [kBluetoothHCIExtendedInquiryResponseDataTypeServiceSolicitation32BitUUIDs](https://developer.apple.com/documentation/iobluetooth/kbluetoothhciextendedinquiryresponsedatatypeservicesolicitation32bituuids)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingHash](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesimplepairinghash)Added [kBluetoothHCIExtendedInquiryResponseDataTypeSimplePairingRandomizer](https://developer.apple.com/documentation/kernel/bluetoothhciextendedinquiryresponsedatatypes/kbluetoothhciextendedinquiryresponsedatatypesimplepairingrandomizer)Added [kBluetoothL2CAPPSMAACP](https://developer.apple.com/documentation/kernel/1640540-anonymous/kbluetoothl2cappsmaacp)

#### IOKit/graphics/IOFramebuffer.h

Added #def IOFRAMEBUFFER_REVAdded [kIOFBNotifyWSAAEnterDefer](https://developer.apple.com/documentation/kernel/1638125-anonymous/kiofbnotifywsaaenterdefer)Added [kIOFBNotifyWSAAExitDefer](https://developer.apple.com/documentation/kernel/1638125-anonymous/kiofbnotifywsaaexitdefer)

#### IOKit/graphics/IOGraphicsTypes.h

Added [kIOWSAA_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_accelerated)Added [kIOWSAA_DeferEnd](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_deferend)Added [kIOWSAA_DeferStart](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_deferstart)Added [kIOWSAA_DriverOpen](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_driveropen)Added [kIOWSAA_From_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_from_accelerated)Added [kIOWSAA_Hibernate](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_hibernate)Added [kIOWSAA_Sleep](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_sleep)Added [kIOWSAA_To_Accelerated](https://developer.apple.com/documentation/kernel/1645117-anonymous/kiowsaa_to_accelerated)Added [kIOWSAA_Transactional](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_transactional)Added [kIOWSAA_Unaccelerated](https://developer.apple.com/documentation/iokit/1645069-anonymous/kiowsaa_unaccelerated)

#### IOKit/hid/IOHIDKeys.h

Added #def kFnFunctionUsageMapKeyAdded #def kFnKeyboardUsageMapKeyAdded #def kIOHIDBiometricDoubleTapTimeoutKeyAdded #def kIOHIDBiometricTapTrackingEnabledKeyAdded #def kIOHIDBiometricTripleTapTimeoutKeyAdded #def kIOHIDKeyboardCapsLockDelayAdded #def kIOHIDKeyboardEjectDelayAdded #def kIOHIDKeyboardLongPressTimeoutKeyAdded #def kIOHIDKeyboardPressCountDoublePressTimeoutKeyAdded #def kIOHIDKeyboardPressCountTrackingEnabledKeyAdded #def kIOHIDKeyboardPressCountTriplePressTimeoutKeyAdded #def kIOHIDKeyboardPressCountUsagePairsKeyAdded #def kKeyboardUsageMapKeyAdded #def kNumLockKeyboardUsageMapKey

#### IOKit/hid/IOHIDProperties.h (Added)

Added #def IOHIDProperties_hAdded #def kIOHIDKeyboardCapsLockDelayOverrideAdded #def kIOHIDKeyboardCapsLockDelayOverrideKeyAdded #def kIOHIDMouseAccelerationTypeAdded #def kIOHIDMouseAccelerationTypeKeyAdded #def kIOHIDMouseScrollAccelerationKeyAdded #def kIOHIDPointerAccelerationKeyAdded #def kIOHIDPointerAccelerationTypeKeyAdded #def kIOHIDPointerButtonModeAdded #def kIOHIDPointerButtonModeKeyAdded #def kIOHIDScrollAccelerationKeyAdded #def kIOHIDScrollAccelerationTypeKeyAdded #def kIOHIDServiceEjectDelayKeyAdded #def kIOHIDServiceInitialKeyRepeatDelayKeyAdded #def kIOHIDServiceKeyRepeatDelayKeyAdded #def kIOHIDUserUsageMapKey

#### IOKit/hid/IOHIDUsageTables.h

Added [kHIDUsage_Game_GamepadFormFitting](https://developer.apple.com/documentation/kernel/1641231-anonymous/khidusage_game_gamepadformfitting)Added [kHIDUsage_GD_AssistiveControl](https://developer.apple.com/documentation/kernel/1641458-anonymous/khidusage_gd_assistivecontrol)Added [kHIDUsage_GD_TabletPCSystemControls](https://developer.apple.com/documentation/iokit/1592534-anonymous/khidusage_gd_tabletpcsystemcontrols)Added [kHIDUsage_LED_Player1](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player1)Added [kHIDUsage_LED_Player2](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player2)Added [kHIDUsage_LED_Player3](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player3)Added [kHIDUsage_LED_Player4](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player4)Added [kHIDUsage_LED_Player5](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player5)Added [kHIDUsage_LED_Player6](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player6)Added [kHIDUsage_LED_Player7](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player7)Added [kHIDUsage_LED_Player8](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player8)Added [kHIDUsage_LED_PlayerIndicator](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_playerindicator)

#### IOKit/hidevent/IOHIDEventDriver.h

Removed [DigitizerTransducer](https://developer.apple.com/documentation/kernel/digitizertransducer)Removed [EventElementCollection](https://developer.apple.com/documentation/kernel/eventelementcollection)Removed [IOHIDEventDriver](https://developer.apple.com/documentation/kernel/iohideventdriver)Removed IOHIDEventDriver::calibrateCenteredPreferredStateElement()Removed IOHIDEventDriver::calibrateJustifiedPreferredStateElement()Removed IOHIDEventDriver::checkGameControllerElement()Removed IOHIDEventDriver::checkMultiAxisElement()Removed IOHIDEventDriver::didTerminate()Removed IOHIDEventDriver::free()Removed IOHIDEventDriver::getCountryCode()Removed IOHIDEventDriver::getElementValue()Removed IOHIDEventDriver::getLocationID()Removed IOHIDEventDriver::getManufacturer()Removed IOHIDEventDriver::getMetaClass()Removed IOHIDEventDriver::getProduct()Removed IOHIDEventDriver::getProductID()Removed IOHIDEventDriver::getReportElements()Removed IOHIDEventDriver::getSerialNumber()Removed IOHIDEventDriver::getTransport()Removed IOHIDEventDriver::getVendorID()Removed IOHIDEventDriver::getVendorIDSource()Removed IOHIDEventDriver::getVersion()Removed IOHIDEventDriver::handleBootPointingReport()Removed IOHIDEventDriver::handleDigitizerReport()Removed IOHIDEventDriver::handleDigitizerTransducerReport()Removed IOHIDEventDriver::handleGameControllerReport()Removed IOHIDEventDriver::handleInterruptReport()Removed IOHIDEventDriver::handleKeboardReport()Removed IOHIDEventDriver::handleMultiAxisPointerReport()Removed IOHIDEventDriver::handleRelativeReport()Removed IOHIDEventDriver::handleScrollReport()Removed IOHIDEventDriver::handleStart()Removed IOHIDEventDriver::handleStop()Removed IOHIDEventDriver::handleUnicodeGestureCandidateReport()Removed IOHIDEventDriver::handleUnicodeGestureReport()Removed IOHIDEventDriver::handleUnicodeLegacyReport()Removed IOHIDEventDriver::handleUnicodeReport()Removed IOHIDEventDriver::init()Removed IOHIDEventDriver::parseDigitizerElement()Removed IOHIDEventDriver::parseDigitizerTransducerElement()Removed IOHIDEventDriver::parseElements()Removed IOHIDEventDriver::parseGameControllerElement()Removed IOHIDEventDriver::parseGestureUnicodeElement()Removed IOHIDEventDriver::parseKeyboardElement()Removed IOHIDEventDriver::parseLEDElement()Removed IOHIDEventDriver::parseLegacyUnicodeElement()Removed IOHIDEventDriver::parseMultiAxisElement()Removed IOHIDEventDriver::parseRelativeElement()Removed IOHIDEventDriver::parseScrollElement()Removed IOHIDEventDriver::parseUnicodeElement()Removed IOHIDEventDriver::processDigitizerElements()Removed IOHIDEventDriver::processGameControllerElements()Removed IOHIDEventDriver::processMultiAxisElements()Removed IOHIDEventDriver::processUnicodeElements()Removed IOHIDEventDriver::serializeCharacterGestureState()Removed IOHIDEventDriver::setDigitizerProperties()Removed IOHIDEventDriver::setElementValue()Removed IOHIDEventDriver::setGameControllerProperties()Removed IOHIDEventDriver::setKeyboardProperties()Removed IOHIDEventDriver::setLEDProperties()Removed IOHIDEventDriver::setMultiAxisProperties()Removed IOHIDEventDriver::setProperties()Removed IOHIDEventDriver::setRelativeProperties()Removed IOHIDEventDriver::setScrollProperties()Removed IOHIDEventDriver::setUnicodeProperties()Modified [IOHIDEvent](https://developer.apple.com/documentation/kernel/iohidevent)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/hidevent/IOHIDEventDriver.h |
| To | Kernel/IOKit/hidsystem/IOHIDSystem.h |

#### IOKit/hidevent/IOHIDEventService.h

Removed [IOHIDConsumer](https://developer.apple.com/documentation/kernel/iohidconsumer)Removed [IOHIDEventService](https://developer.apple.com/documentation/kernel/iohideventservice)Removed IOHIDEventService::calculateCapsLockDelay()Removed IOHIDEventService::calculateStandardType()Removed IOHIDEventService::capsTimerCallback()Removed IOHIDEventService::determineResolution()Removed IOHIDEventService::dispatchAbsolutePointerEvent()Removed IOHIDEventService::dispatchDigitizerEvent()Removed IOHIDEventService::dispatchDigitizerEventWithOrientation()Removed IOHIDEventService::dispatchDigitizerEventWithPolarOrientation()Removed IOHIDEventService::dispatchDigitizerEventWithTiltOrientation()Removed IOHIDEventService::dispatchKeyboardEvent()Removed IOHIDEventService::dispatchMultiAxisPointerEvent()Removed IOHIDEventService::dispatchRelativePointerEvent()Removed IOHIDEventService::dispatchScrollWheelEvent()Removed IOHIDEventService::dispatchTabletPointerEvent()Removed IOHIDEventService::dispatchTabletProximityEvent()Removed IOHIDEventService::dispatchUnicodeEvent()Removed IOHIDEventService::ejectTimerCallback()Removed IOHIDEventService::free()Removed IOHIDEventService::getCountryCode()Removed IOHIDEventService::getDeviceUsagePairs()Removed IOHIDEventService::getElementValue()Removed IOHIDEventService::getLocationID()Removed IOHIDEventService::getManufacturer()Removed IOHIDEventService::getMetaClass()Removed IOHIDEventService::getProduct()Removed IOHIDEventService::getProductID()Removed IOHIDEventService::getReportElements()Removed IOHIDEventService::getReportInterval()Removed IOHIDEventService::getSerialNumber()Removed IOHIDEventService::getTransport()Removed IOHIDEventService::getVendorID()Removed IOHIDEventService::getVendorIDSource()Removed IOHIDEventService::getVersion()Removed IOHIDEventService::handleClose()Removed IOHIDEventService::handleIsOpen()Removed IOHIDEventService::handleOpen()Removed IOHIDEventService::handleStart()Removed IOHIDEventService::handleStop()Removed IOHIDEventService::init()Removed IOHIDEventService::matchPropertyTable()Removed IOHIDEventService::multiAxisTimerCallback()Removed IOHIDEventService::newConsumerShim()Removed IOHIDEventService::newKeyboardShim()Removed IOHIDEventService::newPointingShim()Removed IOHIDEventService::parseSupportedElements()Removed IOHIDEventService::processTabletElement()Removed IOHIDEventService::readyForReports()Removed IOHIDEventService::setElementValue()Removed IOHIDEventService::setProperties()Removed IOHIDEventService::setSystemProperties()Removed IOHIDEventService::start()Removed IOHIDEventService::stop()Removed [IOHIDKeyboard](https://developer.apple.com/documentation/kernel/iohidkeyboard)Removed [IOHIDPointing](https://developer.apple.com/documentation/kernel/iohidpointing)Removed [kHIDDispatchOptionDeliveryNotificationForce](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptiondeliverynotificationforce)Removed [kHIDDispatchOptionDeliveryNotificationSuppress](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptiondeliverynotificationsuppress)Removed [kHIDDispatchOptionKeyboardNoRepeat](https://developer.apple.com/documentation/kernel/2765597-anonymous/khiddispatchoptionkeyboardnorepeat)Removed [kHIDDispatchOptionPhaseAny](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphaseany)Removed [kHIDDispatchOptionPhaseBegan](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphasebegan)Removed [kHIDDispatchOptionPhaseCanceled](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphasecanceled)Removed [kHIDDispatchOptionPhaseChanged](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphasechanged)Removed [kHIDDispatchOptionPhaseEnded](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphaseended)Removed [kHIDDispatchOptionPhaseMayBegin](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionphasemaybegin)Removed [kHIDDispatchOptionPointerAbsolutToRelative](https://developer.apple.com/documentation/kernel/2765607-anonymous/khiddispatchoptionpointerabsoluttorelative)Removed [kHIDDispatchOptionPointerAffixToScreen](https://developer.apple.com/documentation/kernel/2765607-anonymous/khiddispatchoptionpointeraffixtoscreen)Removed [kHIDDispatchOptionPointerDisplayIntegrated](https://developer.apple.com/documentation/kernel/2765607-anonymous/khiddispatchoptionpointerdisplayintegrated)Removed [kHIDDispatchOptionPointerNoAcceleration](https://developer.apple.com/documentation/kernel/2765607-anonymous/khiddispatchoptionpointernoacceleration)Removed [kHIDDispatchOptionScrollMomentumAny](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionscrollmomentumany)Removed [kHIDDispatchOptionScrollMomentumContinue](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionscrollmomentumcontinue)Removed [kHIDDispatchOptionScrollMomentumEnd](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionscrollmomentumend)Removed [kHIDDispatchOptionScrollMomentumStart](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionscrollmomentumstart)Removed [kHIDDispatchOptionScrollNoAcceleration](https://developer.apple.com/documentation/kernel/2765584-anonymous/khiddispatchoptionscrollnoacceleration)

#### IOKit/hidsystem/ev_keymap.h

Added #def NX_KEYTYPE_MENU

#### IOKit/hidsystem/IOHIDParameter.h

Removed #def kIOHIDMouseAccelerationTypeRemoved #def kIOHIDMouseScrollAccelerationKeyRemoved #def kIOHIDPointerAccelerationKeyRemoved #def kIOHIDPointerAccelerationTypeKeyRemoved #def kIOHIDPointerButtonModeRemoved #def kIOHIDScrollAccelerationKeyRemoved #def kIOHIDScrollAccelerationTypeKeyAdded #def kIOHIDKeyboardGlobalModifiersKeyAdded #def kIOHIDMouseClickNotificationAdded #def kIOHIDServiceGlobalModifiersUsageKey

#### IOKit/hidsystem/IOHIDSystem.h

Added [IOFixedPoint64](https://developer.apple.com/documentation/kernel/iofixedpoint64)Added [IOHIDKeyboardDevice](https://developer.apple.com/documentation/kernel/iohidkeyboarddevice)Added [IOHIDPointingDevice](https://developer.apple.com/documentation/kernel/iohidpointingdevice)Added [IOHIDSystem](https://developer.apple.com/documentation/kernel/iohidsystem)Added IOHIDSystem::animateWaitCursor()Added IOHIDSystem::attach()Added IOHIDSystem::changeCursor()Added IOHIDSystem::createFilteredParamPropertiesForService()Added IOHIDSystem::createParameters()Added IOHIDSystem::createShmem()Added IOHIDSystem::createShmemGated()Added IOHIDSystem::detach()Added IOHIDSystem::disableContinuousCursor()Added IOHIDSystem::dispatchEvent()Added IOHIDSystem::doCreateShmem()Added IOHIDSystem::doEvClose()Added IOHIDSystem::doExtGetButtonEventNum()Added IOHIDSystem::doExtGetStateForSelector()Added IOHIDSystem::doExtPostEvent()Added IOHIDSystem::doExtSetMouseLocation()Added IOHIDSystem::doExtSetStateForSelector()Added IOHIDSystem::doKeyboardEvent()Added IOHIDSystem::doKeyboardSpecialEvent()Added IOHIDSystem::doNewUserClient()Added IOHIDSystem::doProcessKeyboardEQ()Added IOHIDSystem::doProcessNotifications()Added IOHIDSystem::doRegisterEventQueue()Added IOHIDSystem::doRegisterScreen()Added IOHIDSystem::doSetContinuousCursorEnable()Added IOHIDSystem::doSetCursorEnable()Added IOHIDSystem::doSetDisplayBounds()Added IOHIDSystem::doSetParamPropertiesPost()Added IOHIDSystem::doSetParamPropertiesPre()Added IOHIDSystem::doUnregisterEventQueue()Added IOHIDSystem::doUnregisterScreen()Added IOHIDSystem::doUpdateEventFlags()Added IOHIDSystem::enableContinuousCursor()Added IOHIDSystem::evClose()Added IOHIDSystem::evCloseGated()Added IOHIDSystem::evDispatch()Added IOHIDSystem::eventFlags()Added IOHIDSystem::evOpen()Added IOHIDSystem::extGetButtonEventNum()Added IOHIDSystem::extGetButtonEventNumGated()Added IOHIDSystem::extGetStateForSelector()Added IOHIDSystem::extGetUserHidActivityState()Added IOHIDSystem::extPostEvent()Added IOHIDSystem::extPostEventGated()Added IOHIDSystem::extRegisterVirtualDisplay()Added IOHIDSystem::extSetBounds()Added IOHIDSystem::extSetMouseLocation()Added IOHIDSystem::extSetMouseLocationGated()Added IOHIDSystem::extSetOnScreenBounds()Added IOHIDSystem::extSetStateForSelector()Added IOHIDSystem::extSetVirtualDisplayBounds()Added IOHIDSystem::extUnregisterVirtualDisplay()Added IOHIDSystem::free()Added IOHIDSystem::genericNotificationHandler()Added IOHIDSystem::getMetaClass()Added IOHIDSystem::getUserHidActivityState()Added IOHIDSystem::getUserHidActivityStateGated()Added IOHIDSystem::getWorkLoop()Added IOHIDSystem::handlePublishNotification()Added IOHIDSystem::hidActivityChecker()Added IOHIDSystem::hideCursor()Added IOHIDSystem::hideWaitCursor()Added IOHIDSystem::init()Added IOHIDSystem::initShmem()Added IOHIDSystem::instance()Added IOHIDSystem::keyboardEvent()Added IOHIDSystem::keyboardEventGated()Added IOHIDSystem::keyboardSpecialEvent()Added IOHIDSystem::keyboardSpecialEventGated()Added IOHIDSystem::makeInt32ArrayParamProperty()Added IOHIDSystem::makeNumberParamProperty()Added IOHIDSystem::message()Added IOHIDSystem::moveCursor()Added IOHIDSystem::newUserClient()Added IOHIDSystem::newUserClientGated()Added IOHIDSystem::periodicEvents()Added IOHIDSystem::pointToScreen()Added IOHIDSystem::postEvent()Added IOHIDSystem::powerStateDidChangeTo()Added IOHIDSystem::probe()Added IOHIDSystem::processKeyboardEQ()Added IOHIDSystem::registerEventQueue()Added IOHIDSystem::registerEventQueueGated()Added IOHIDSystem::registerEventSource()Added IOHIDSystem::registerScreen()Added IOHIDSystem::registerScreenGated()Added IOHIDSystem::reportUserHidActivity()Added IOHIDSystem::reportUserHidActivityGated()Added IOHIDSystem::resetCursor()Added IOHIDSystem::scheduleNextPeriodicEvent()Added IOHIDSystem::setBounds()Added IOHIDSystem::setContinuousCursorEnable()Added IOHIDSystem::setContinuousCursorEnableGated()Added IOHIDSystem::setCursorEnable()Added IOHIDSystem::setCursorEnableGated()Added IOHIDSystem::setCursorPosition()Added IOHIDSystem::setDisplayBoundsGated()Added IOHIDSystem::setEventsEnable()Added IOHIDSystem::setParamProperties()Added IOHIDSystem::setParamPropertiesPostGated()Added IOHIDSystem::setParamPropertiesPreGated()Added IOHIDSystem::setProperties()Added IOHIDSystem::showCursor()Added IOHIDSystem::showWaitCursor()Added IOHIDSystem::start()Added IOHIDSystem::startCursor()Added IOHIDSystem::unregisterEventQueue()Added IOHIDSystem::unregisterEventQueueGated()Added IOHIDSystem::unregisterScreen()Added IOHIDSystem::unregisterScreenGated()Added IOHIDSystem::updateEventFlags()Added IOHIDSystem::updateEventFlagsGated()Added IOHIDSystem::updateHidActivity()Added IOHIDSystem::updateParamPropertiesGated()Added IOHIDSystem::workspaceBounds()Added #def kIOHIDSystem508MouseClickMessageAdded #def kIOHIDSystem508SpecialKeyDownMessageAdded #def kIOHIDSystemActivityTickleAdded #def kIOHIDSystemDeviceSeizeRequestMessageAdded #def kIOHIDSystemUserHidActivityModified [IOHIDEvent](https://developer.apple.com/documentation/kernel/iohidevent)

|  | Header |
| --- | --- |
| From | Kernel/IOKit/hidevent/IOHIDEventDriver.h |
| To | Kernel/IOKit/hidsystem/IOHIDSystem.h |

#### IOKit/hidsystem/IOHIDUsageTables.h

Added [kHIDUsage_Game_GamepadFormFitting](https://developer.apple.com/documentation/kernel/1641231-anonymous/khidusage_game_gamepadformfitting)Added [kHIDUsage_GD_AssistiveControl](https://developer.apple.com/documentation/kernel/1641458-anonymous/khidusage_gd_assistivecontrol)Added [kHIDUsage_GD_TabletPCSystemControls](https://developer.apple.com/documentation/iokit/1592534-anonymous/khidusage_gd_tabletpcsystemcontrols)Added [kHIDUsage_LED_Player1](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player1)Added [kHIDUsage_LED_Player2](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player2)Added [kHIDUsage_LED_Player3](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player3)Added [kHIDUsage_LED_Player4](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player4)Added [kHIDUsage_LED_Player5](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player5)Added [kHIDUsage_LED_Player6](https://developer.apple.com/documentation/iokit/1592166-anonymous/khidusage_led_player6)Added [kHIDUsage_LED_Player7](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player7)Added [kHIDUsage_LED_Player8](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_player8)Added [kHIDUsage_LED_PlayerIndicator](https://developer.apple.com/documentation/kernel/1641289-anonymous/khidusage_led_playerindicator)

#### IOKit/hidsystem/IOHIDWorkLoop.h (Added)

Added [IOHIDWorkLoop](https://developer.apple.com/documentation/kernel/iohidworkloop)Added IOHIDWorkLoop::free()Added IOHIDWorkLoop::getMetaClass()Added IOHIDWorkLoop::init()Added IOHIDWorkLoop::workLoop()

#### IOKit/hidsystem/IOHIKeyboardMapper.h

Removed IOHIKeyboardMapper::createParamDicts()Removed IOHIKeyboardMapper::f12EjectFilterKey()Removed IOHIKeyboardMapper::modifierSwapFilterKey()Removed IOHIKeyboardMapper::performF12Eject()Removed IOHIKeyboardMapper::slowKeysFilterKey()Removed IOHIKeyboardMapper::slowKeysPostProcess()Removed IOHIKeyboardMapper::stickyKeysAllocToggleInfo()Removed IOHIKeyboardMapper::stickyKeysCleanup()Removed IOHIKeyboardMapper::stickyKeysFilterKey()Removed IOHIKeyboardMapper::stickyKeysfree()Removed IOHIKeyboardMapper::stickyKeysFreeToggleInfo()Removed IOHIKeyboardMapper::stickyKeysinit()Removed IOHIKeyboardMapper::stickyKeysModifierKey()Removed IOHIKeyboardMapper::stickyKeysModifierToggleCheck()Removed IOHIKeyboardMapper::stickyKeysMouseUp()Removed IOHIKeyboardMapper::stickyKeysNonModifierKey()Removed IOHIKeyboardMapper::stickyKeysSetFnState()

#### IOKit/hidsystem/IOLLEvent.h

Added #def NX_EVENT_EXTENSION_LOCATION_DEVICE_SCALEDAdded #def NX_EVENT_EXTENSION_LOCATION_INVALIDAdded #def NX_EVENT_EXTENSION_LOCATION_TYPE_FLOATAdded #def NX_EVENT_EXTENSION_MOUSE_DELTA_TYPE_FLOATAdded #def NX_SUBTYPE_ACCESSIBILITYAdded #def NX_SUBTYPE_MENUAdded [NXEventExt](https://developer.apple.com/documentation/iokit/nxeventext)Added [NXEventExtension](https://developer.apple.com/documentation/iokit/nxeventextension)

#### IOKit/IOBSD.h

Added [#def kIOBSDKey](https://developer.apple.com/documentation/iokit/kiobsdkey)

#### IOKit/IODataQueue.h

Removed IODataQueue::enqueue()Added IODataQueue::enqueue_tail()

#### IOKit/IOKernelReportStructs.h

Added #def kIOReportUnit_GiBAdded #def kIOReportUnit_MiBAdded #def kIOReportUnit_TiB

#### IOKit/IOKitDebug.h

Removed kIOTrackingPrintTrackingAdded [kIOTrackingGetMappings](https://developer.apple.com/documentation/kernel/1644082-anonymous/kiotrackinggetmappings)

#### IOKit/IOKitKeys.h

Added [#def kIOMinimumSaturationByteCountKey](https://developer.apple.com/documentation/iokit/kiominimumsaturationbytecountkey)Added [#def kIOPropertyExistsMatchKey](https://developer.apple.com/documentation/iokit/kiopropertyexistsmatchkey)Added [#def kIORegistryEntryPropertyKeysKey](https://developer.apple.com/documentation/iokit/kioregistryentrypropertykeyskey)Added [#def kIOResourceMatchedKey](https://developer.apple.com/documentation/iokit/kioresourcematchedkey)

#### IOKit/IOMemoryDescriptor.h

Added #def IOMEMORYUSERESERVEDEFINEDAdded [kIOMemoryPurgeableFaultOnAccess](https://developer.apple.com/documentation/kernel/1643335-anonymous/kiomemorypurgeablefaultonaccess)Added [kIOMemoryUseReserve](https://developer.apple.com/documentation/kernel/1643338-anonymous/kiomemoryusereserve)

#### IOKit/IORegistryEntry.h

Added [gIORegistryEntryPropertyKeysKey](https://developer.apple.com/documentation/kernel/gioregistryentrypropertykeyskey)

#### IOKit/IOReturn.h

Added #def sub_iokit_appleembeddedsleepwakehandler

#### IOKit/IOService.h

Added [gIOBSDKey](https://developer.apple.com/documentation/kernel/giobsdkey)Added [gIOBSDMajorKey](https://developer.apple.com/documentation/kernel/giobsdmajorkey)Added [gIOBSDMinorKey](https://developer.apple.com/documentation/kernel/giobsdminorkey)Added [gIOBSDNameKey](https://developer.apple.com/documentation/kernel/giobsdnamekey)Added [gIOBSDUnitKey](https://developer.apple.com/documentation/kernel/giobsdunitkey)Added [gIOResourceMatchedKey](https://developer.apple.com/documentation/kernel/gioresourcematchedkey)Modified IOService::setIdleTimerPeriod()

|  | Declaration |
| --- | --- |
| From | ``` virtual IOReturn setIdleTimerPeriod (     unsigned long ); ``` |
| To | ``` virtual IOReturn setIdleTimerPeriod (     unsigned long period ); ``` |

#### IOKit/IOWorkLoop.h

Added IOWorkLoop::setMaximumLockTime()

#### IOKit/network/IONetworkController.h

Added [kIONetworkFeatureHWTimeStamp](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeaturehwtimestamp)Added [kIONetworkFeatureSWTimeStamp](https://developer.apple.com/documentation/kernel/1646638-anonymous/kionetworkfeatureswtimestamp)

#### IOKit/pci/IOPCIBridge.h

Modified IOPCIBridge::restoreTunnelState()

|  | Declaration |
| --- | --- |
| From | ``` IOReturn restoreTunnelState (     IOPCIDevice *root,     IOOptionBits options ); ``` |
| To | ``` IOReturn restoreTunnelState (     IOPCIDevice *rootDevice,     IOOptionBits options,     bool *didTunnelController ); ``` |

#### IOKit/pwr_mgt/IOPM.h

Added #def kIOPMPSAdapterDetailsVoltage

#### IOKit/scsi/IOBDServices.h

Modified IOBDServices::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/scsi/IOBlockStorageServices.h

Added IOBlockStorageServices::doGetProvisionStatus()Added IOBlockStorageServices::doUnmap()

#### IOKit/scsi/IODVDServices.h

Modified IODVDServices::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/scsi/IOSCSIBlockCommandsDevice.h

Added IOSCSIBlockCommandsDevice::GET_LBA_STATUS()Added IOSCSIBlockCommandsDevice::GetDeviceUnmapCharacteristics()Added IOSCSIBlockCommandsDevice::GetProvisionStatus()Added IOSCSIBlockCommandsDevice::IssueUnmap()Added IOSCSIBlockCommandsDevice::IsUnmapAllowed()Added IOSCSIBlockCommandsDevice::IsUseWriteSame()Added IOSCSIBlockCommandsDevice::LogicalBlockProvisioningUnmapSupport()Added IOSCSIBlockCommandsDevice::REPORT_PROVISIONING_INITIALIZATION_PATTERN()Added IOSCSIBlockCommandsDevice::ReportProvisioningInitializationPattern()Added IOSCSIBlockCommandsDevice::Unmap()Added IOSCSIBlockCommandsDevice::UNMAP()Added IOSCSIBlockCommandsDevice::UnmapTruncateAndAccumulate()Added IOSCSIBlockCommandsDevice::UnmapTryExtentCoalesce()Added IOSCSIBlockCommandsDevice::UpdateLBAProvisionStatus()Added IOSCSIBlockCommandsDevice::WRITE_SAME_10()Added IOSCSIBlockCommandsDevice::WRITE_SAME_16()Added IOSCSIBlockCommandsDevice::WriteSame()Added IOSCSIBlockCommandsDevice::WriteSameUnmap()Added #def fLBPRZAdded #def fMaximumUnmapBlockDescriptorCountAdded #def fMaximumUnmapLBACountAdded #def fMaximumWriteSameLengthAdded #def fUnmapAllowedAdded #def fUseWriteSameModified IOSCSIBlockCommandsDevice::READ_16()

|  | Declaration |
| --- | --- |
| From | ``` bool READ_16 (     SCSITaskIdentifier request,     IOMemoryDescriptor *dataBuffer,     UInt32 blockSize,     SCSICmdField3Bit RDPROTECT,     SCSICmdField1Bit DPO,     SCSICmdField1Bit FUA,     SCSICmdField1Bit FUA_NV,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte TRANSFER_LENGTH,     SCSICmdField5Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |
| To | ``` bool READ_16 (     SCSITaskIdentifier request,     IOMemoryDescriptor *dataBuffer,     UInt32 blockSize,     SCSICmdField3Bit RDPROTECT,     SCSICmdField1Bit DPO,     SCSICmdField1Bit FUA,     SCSICmdField1Bit FUA_NV,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte TRANSFER_LENGTH,     SCSICmdField6Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |

Modified IOSCSIBlockCommandsDevice::SYNCRONIZE_CACHE_16()

|  | Declaration |
| --- | --- |
| From | ``` bool SYNCRONIZE_CACHE_16 (     SCSITaskIdentifier request,     SCSICmdField1Bit SYNC_NV,     SCSICmdField1Bit IMMED,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte NUMBER_OF_BLOCKS,     SCSICmdField5Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |
| To | ``` bool SYNCRONIZE_CACHE_16 (     SCSITaskIdentifier request,     SCSICmdField1Bit SYNC_NV,     SCSICmdField1Bit IMMED,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte NUMBER_OF_BLOCKS,     SCSICmdField6Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |

Modified IOSCSIBlockCommandsDevice::WRITE_16()

|  | Declaration |
| --- | --- |
| From | ``` bool WRITE_16 (     SCSITaskIdentifier request,     IOMemoryDescriptor *dataBuffer,     UInt32 blockSize,     SCSICmdField3Bit WRPROTECT,     SCSICmdField1Bit DPO,     SCSICmdField1Bit FUA,     SCSICmdField1Bit FUA_NV,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte TRANSFER_LENGTH,     SCSICmdField5Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |
| To | ``` bool WRITE_16 (     SCSITaskIdentifier request,     IOMemoryDescriptor *dataBuffer,     UInt32 blockSize,     SCSICmdField3Bit WRPROTECT,     SCSICmdField1Bit DPO,     SCSICmdField1Bit FUA,     SCSICmdField1Bit FUA_NV,     SCSICmdField8Byte LOGICAL_BLOCK_ADDRESS,     SCSICmdField4Byte TRANSFER_LENGTH,     SCSICmdField6Bit GROUP_NUMBER,     SCSICmdField1Byte CONTROL ); ``` |

#### IOKit/scsi/IOSCSIMultimediaCommandsDevice.h

Added IOSCSIMultimediaCommandsDevice::REPORT_KEY_V3()Modified IOSCSIMultimediaCommandsDevice::REPORT_KEY_V2()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified IOSCSIMultimediaCommandsDevice::ReportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/scsi/SCSICmds_INQUIRY_Definitions.h

Added [kINQUIRY_PageB0_PageCode](https://developer.apple.com/documentation/kernel/1643302-anonymous/kinquiry_pageb0_pagecode)Added [kINQUIRY_PageB2_PageCode](https://developer.apple.com/documentation/iokit/1572746-inquiry_page_codes/kinquiry_pageb2_pagecode)Added [SCSICmd_INQUIRY_PageB0_Data](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_pageb0_data)Added [SCSICmd_INQUIRY_PageB2_Data](https://developer.apple.com/documentation/kernel/scsicmd_inquiry_pageb2_data)Added [SCSICmd_INQUIRY_PageB2_Provisioning_Group_Descriptor](https://developer.apple.com/documentation/iokit/scsicmd_inquiry_pageb2_provisioning_group_descriptor)

#### IOKit/scsi/SCSICommandOperationCodes.h

Added [kSCSICmd_UNMAP](https://developer.apple.com/documentation/kernel/1643419-anonymous/kscsicmd_unmap)Added [kSCSIServiceAction_GET_LBA_STATUS](https://developer.apple.com/documentation/iokit/1778261-anonymous/kscsiserviceaction_get_lba_status)Added [kSCSIServiceAction_REPORT_PROVISIONING_INITIALIZATION_PATTERN](https://developer.apple.com/documentation/kernel/1643413-anonymous/kscsiserviceaction_report_provisioning_initialization_pattern)

#### IOKit/skywalk/IOSkywalkSupport.h (Added)

Added [IOMemoryDescriptor](https://developer.apple.com/documentation/kernel/iomemorydescriptor)Added [IOMemoryMap](https://developer.apple.com/documentation/kernel/iomemorymap)Added IOSKMemoryArrayCreate()Added IOSKMemoryArrayRefAdded IOSKMemoryBufferCreate()Added IOSKMemoryBufferRefAdded IOSKMemoryBufferSpecAdded IOSKMemoryDescriptorAdded IOSKMemoryDestroy()Added IOSKMemoryDiscard()Added IOSKMemoryGetIOMD()Added IOSKMemoryMapDestroy()Added IOSKMemoryMapRefAdded IOSKMemoryMapToTask()Added IOSKMemoryReclaim()Added IOSKMemoryRefAdded sk_verbose

#### IOKit/storage/IOBDMedia.h

Modified IOBDMedia::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/storage/IOBlockStorageDevice.h

Added IOBlockStorageDevice::doGetProvisionStatus()Added [IOBlockStorageProvisionDeviceExtent](https://developer.apple.com/documentation/kernel/ioblockstorageprovisiondeviceextent)

#### IOKit/storage/IOBlockStorageDriver.h

Added IOBlockStorageDriver::getProvisionStatus()

#### IOKit/storage/IODVDBlockStorageDevice.h

Modified IODVDBlockStorageDevice::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/storage/IODVDBlockStorageDriver.h

Modified IODVDBlockStorageDriver::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/storage/IODVDMedia.h

Modified IODVDMedia::reportKey()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### IOKit/storage/IOFilterScheme.h

Added IOFilterScheme::getProvisionStatus()

#### IOKit/storage/IOMedia.h

Added IOMedia::getProvisionStatus()

#### IOKit/storage/IOPartitionScheme.h

Added IOPartitionScheme::getProvisionStatus()

#### IOKit/storage/IOStorage.h

Added IOStorage::getProvisionStatus()Added [IOStorageGetProvisionStatusOptions](https://developer.apple.com/documentation/kernel/iostoragegetprovisionstatusoptions)Added [IOStorageProvisionExtent](https://developer.apple.com/documentation/kernel/iostorageprovisionextent)Added [kIOStorageProvisionTypeAnchored](https://developer.apple.com/documentation/kernel/1644744-anonymous/kiostorageprovisiontypeanchored)Added [kIOStorageProvisionTypeDeallocated](https://developer.apple.com/documentation/kernel/1644744-anonymous/kiostorageprovisiontypedeallocated)Added [kIOStorageProvisionTypeMapped](https://developer.apple.com/documentation/kernel/1644744-anonymous/kiostorageprovisiontypemapped)

#### IOKit/usb/IOUSBHostDevice.h

Added [IOSimpleReporter](https://developer.apple.com/documentation/kernel/iosimplereporter)Added [IOStateReporter](https://developer.apple.com/documentation/kernel/iostatereporter)Added IOUSBHostDevice::configureReport()Added IOUSBHostDevice::setProperties()Added IOUSBHostDevice::setProperty()Added IOUSBHostDevice::updateReport()Modified IOUSBHostDevice::stringFromReturn()

|  | Declaration |
| --- | --- |
| From | ``` virtual const char * stringFromReturn (     IOReturn rtn ); ``` |
| To | ``` virtual const char * stringFromReturn (     IOReturn code ); ``` |

#### IOKit/usb/IOUSBHostFamily.h

Removed #def kUSBHostControllerPropertyDebugErrorAdded #def kUSBHostBillboardDevicePropertyAdditionalFailureInfoAdded #def kUSBHostBillboardDevicePropertyAddtionalInfoURLAdded #def kUSBHostBillboardDevicePropertyAddtionalInfoURLIndexAdded #def kUSBHostBillboardDevicePropertyAlternateModeAdded #def kUSBHostBillboardDevicePropertyAlternateModeStringAdded #def kUSBHostBillboardDevicePropertyAlternateModeStringIndexAdded #def kUSBHostBillboardDevicePropertyBcdVersionAdded #def kUSBHostBillboardDevicePropertyConfiguredAdded #def kUSBHostBillboardDevicePropertyNumberOfAlternateModesAdded #def kUSBHostBillboardDevicePropertyPreferredAlternateModeAdded #def kUSBHostBillboardDevicePropertySVIDAdded #def kUSBHostBillboardDevicePropertyVCONNPowerAdded [kUSBHostConnectionSpeedSuperPlus](https://developer.apple.com/documentation/kernel/1645785-anonymous/kusbhostconnectionspeedsuperplus)Added [kUSBHostConnectorTypeUSBTypeC](https://developer.apple.com/documentation/kernel/tusbhostconnectortype/kusbhostconnectortypeusbtypec)Added #def kUSBHostControllerPropertyCompanionControllerNameAdded #def kUSBHostControllerPropertyCompanionPresentAdded #def kUSBHostControllerPropertyRevisionAdded #def kUSBHostDevicePropertyDescriptorOverrideAdded #def kUSBHostMessageNonInterruptIsochFrameAdded [kUSBHostPortConnectionSpeedSuperPlus](https://developer.apple.com/documentation/kernel/tusbhostconnectionspeed/kusbhostportconnectionspeedsuperplus)Added #def kUSBHostPortPropertyCompanionPortNumberAdded #def kUSBHostPortPropertyCompanionPresentAdded #def kUSBHostPortPropertyOvercurrentAdded #def kUSBHostPortPropertyUsbCPortNumberAdded [kUSBHostPortStatusConnectedSpeedSuperPlus](https://developer.apple.com/documentation/kernel/tusbhostportstatus/kusbhostportstatusconnectedspeedsuperplus)Added #def kUSBTypeCCableDetectACPIMethodAdded kUSBTypeCCableTypeErrorAdded [kUSBTypeCCableTypeNone](https://developer.apple.com/documentation/kernel/tusbctypecabletype/kusbtypeccabletypenone)Added [kUSBTypeCCableTypeUSB](https://developer.apple.com/documentation/kernel/tusbctypecabletype/kusbtypeccabletypeusb)Added [tUSBCTypeCableType](https://developer.apple.com/documentation/kernel/tusbctypecabletype)

#### IOKit/usb/IOUSBHostHIDDevice.h

Added IOUSBHostHIDDevice::setProperty()Added #def kUSBHostHIDDevicePropertyIdlePolicy

#### IOKit/usb/IOUSBHostInterface.h

Added [IOSimpleReporter](https://developer.apple.com/documentation/kernel/iosimplereporter)Added IOUSBHostInterface::configureReport()Added IOUSBHostInterface::updateReport()Modified IOUSBHostInterface::stringFromReturn()

|  | Declaration |
| --- | --- |
| From | ``` virtual const char * stringFromReturn (     IOReturn rtn ); ``` |
| To | ``` virtual const char * stringFromReturn (     IOReturn code ); ``` |

#### IOKit/usb/IOUSBHostPipe.h

Added IOUSBHostPipe::adjustPipeGatedV2()Added IOUSBHostPipe::getDescriptors()

#### IOKit/usb/IOUSBUserClient.h

Added [kUSBInterfaceUserClientSetDeviceIdlePolicy](https://developer.apple.com/documentation/iokit/1575934-anonymous/kusbinterfaceuserclientsetdeviceidlepolicy)Added [kUSBInterfaceUserClientSetPipeIdlePolicy](https://developer.apple.com/documentation/kernel/1646287-anonymous/kusbinterfaceuserclientsetpipeidlepolicy)

#### IOKit/usb/USB.h

Added [IOUSBDeviceCapabilityBillboard](https://developer.apple.com/documentation/iokit/iousbdevicecapabilitybillboard)Added [IOUSBDeviceCapabilityBillboardAltConfig](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardaltconfig)Added [IOUSBDeviceCapabilityBillboardAltConfigPtr](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardaltconfigptr)Added [IOUSBDeviceCapabilityBillboardPtr](https://developer.apple.com/documentation/kernel/iousbdevicecapabilitybillboardptr)Added #def kIOUSBMessageConfigurationSetAdded [kUSBDeviceSpeedSuperPlus](https://developer.apple.com/documentation/iokit/1425357-usbdevicespeed/kusbdevicespeedsuperplus)

#### IOKit/usb/USBSpec.h

Added [kUSBBillboardAltModeConfigSuccess](https://developer.apple.com/documentation/kernel/1643529-anonymous/kusbbillboardaltmodeconfigsuccess)Added [kUSBBillboardConfigNotAttempted](https://developer.apple.com/documentation/iokit/1643743-anonymous/kusbbillboardconfignotattempted)Added [kUSBBillboardConfigUnsuccessful](https://developer.apple.com/documentation/iokit/1643743-anonymous/kusbbillboardconfigunsuccessful)Added [kUSBBillboardUnspecifiedError](https://developer.apple.com/documentation/kernel/1643529-anonymous/kusbbillboardunspecifiederror)Added [kUSBBillboardVConn1P5Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn1p5watt)Added [kUSBBillboardVConn1Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn1watt)Added [kUSBBillboardVConn2Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn2watt)Added [kUSBBillboardVConn3Watt](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconn3watt)Added [kUSBBillboardVConn4Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn4watt)Added [kUSBBillboardVConn5Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn5watt)Added [kUSBBillboardVConn6Watt](https://developer.apple.com/documentation/iokit/1643726-anonymous/kusbbillboardvconn6watt)Added #def kUSBBillboardVConnNoPowerReqAdded [kUSBBillboardVConnReserved](https://developer.apple.com/documentation/kernel/1643501-anonymous/kusbbillboardvconnreserved)Added [kUSBDeviceCapabilityBillboard](https://developer.apple.com/documentation/iokit/1424953-device_capability_types/kusbdevicecapabilitybillboard)

#### kern/assert.h

Removed #def assert_staticAdded #def APPLE_KEXT_ASSERTIONSAdded [kext_assertions_enable](https://developer.apple.com/documentation/kernel/kext_assertions_enable)

#### kern/backtrace.h (Added)

Added [backtrace()](https://developer.apple.com/documentation/kernel/1644760-backtrace)Added [backtrace_frame()](https://developer.apple.com/documentation/kernel/2202279-backtrace_frame)Added [backtrace_interrupted()](https://developer.apple.com/documentation/kernel/2202278-backtrace_interrupted)Added [backtrace_thread_user()](https://developer.apple.com/documentation/kernel/2202281-backtrace_thread_user)Added [backtrace_user()](https://developer.apple.com/documentation/kernel/2202280-backtrace_user)

#### kern/clock.h

Added [absolutetime_to_continuoustime()](https://developer.apple.com/documentation/kernel/1645327-absolutetime_to_continuoustime)Added [clock_continuoustime_interval_to_deadline()](https://developer.apple.com/documentation/kernel/1645325-clock_continuoustime_interval_to)Added [continuoustime_to_absolutetime()](https://developer.apple.com/documentation/kernel/1645326-continuoustime_to_absolutetime)

#### kern/debug.h

Removed kThreadDecompressedBTRemoved STACKSHOT_ENABLE_FAULTINGRemoved STACKSHOT_GET_WINDOWED_MICROSTACKSHOTSRemoved STACKSHOT_SAVE_KERNEL_FRAMES_ONLYRemoved STACKSHOT_WINDOWED_MICROSTACKSHOTS_DISABLERemoved STACKSHOT_WINDOWED_MICROSTACKSHOTS_ENABLERemoved #def STASKSHOT_KCTYPE_DONATING_PIDSAdded [kIORecord](https://developer.apple.com/documentation/kernel/micro_snapshot_flags/kiorecord)Added [STACKSHOT_ACTIVE_KERNEL_THREADS_ONLY](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_active_kernel_threads_only)Added [STACKSHOT_COLLECT_DELTA_SNAPSHOT](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_collect_delta_snapshot)Added [STACKSHOT_ENABLE_BT_FAULTING](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_enable_bt_faulting)Added [STACKSHOT_ENABLE_UUID_FAULTING](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_enable_uuid_faulting)Added [STACKSHOT_FROM_PANIC](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_from_panic)Added [STACKSHOT_NO_IO_STATS](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_no_io_stats)Added STACKSHOT_TAILSPINAdded [STACKSHOT_TRYLOCK](https://developer.apple.com/documentation/kernel/1644204-anonymous/stackshot_trylock)Modified [dyld_uuid_info_32](https://developer.apple.com/documentation/kernel/dyld_uuid_info_32)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [dyld_uuid_info_64](https://developer.apple.com/documentation/kernel/dyld_uuid_info_64)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [io_stats_snapshot](https://developer.apple.com/documentation/kernel/io_stats_snapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kFrozen](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kfrozen)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kGlobalForcedIdle](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kglobalforcedidle)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kHasDispatchSerial](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/khasdispatchserial)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kPidSuspended](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kpidsuspended)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kStacksPCOnly](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kstackspconly)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskdarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskExtDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskextdarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsBoosted](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisboosted)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsForeground](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisforeground)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisimpdonor)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsLiveImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisliveimpdonor)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsSuppressed](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskissuppressed)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsTimerThrottled](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskistimerthrottled)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskRsrcFlagged](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskrsrcflagged)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskVisNonvisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisnonvisible)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskVisVisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisvisible)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTerminatedSnapshot](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kterminatedsnapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadDarwinBG](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreaddarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadFaultedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadfaultedbt)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadIOPassive](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadiopassive)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadSuspended](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadsuspended)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadTruncatedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadtruncatedbt)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [mem_and_io_snapshot](https://developer.apple.com/documentation/kernel/mem_and_io_snapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [stack_snapshot_frame32](https://developer.apple.com/documentation/kernel/stack_snapshot_frame32)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [stack_snapshot_frame64](https://developer.apple.com/documentation/kernel/stack_snapshot_frame64)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_IO_NUM_PRIORITIES

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCCONTAINER_TASK

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCCONTAINER_THREAD

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_BOOTARGS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_GLOBAL_MEM_STATS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_IOSTATS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_JETSAM_LEVEL

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_PAGE_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_STACKFRAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_STACKFRAME64

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_OSVERSION

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_TASK_SNAPSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_THREAD_NAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_THREAD_SNAPSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_USER_STACKFRAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_USER_STACKFRAME64

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_MAX_THREAD_NAME_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [task_snapshot_flags](https://developer.apple.com/documentation/kernel/task_snapshot_flags)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [task_snapshot_v2](https://developer.apple.com/documentation/kernel/task_snapshot_v2)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [thread_snapshot_flags](https://developer.apple.com/documentation/kernel/thread_snapshot_flags)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [thread_snapshot_v2](https://developer.apple.com/documentation/kernel/thread_snapshot_v2)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

#### kern/exc_resource.h

Added #def EXC_RESOURCE_IO_DECODE_INTERVALAdded #def EXC_RESOURCE_IO_DECODE_LIMITAdded #def EXC_RESOURCE_IO_ENCODE_INTERVALAdded #def EXC_RESOURCE_IO_ENCODE_LIMITAdded #def EXC_RESOURCE_IO_ENCODE_OBSERVEDAdded #def EXC_RESOURCE_IO_OBSERVEDAdded #def FLAVOR_IO_LOGICAL_WRITESAdded #def FLAVOR_IO_PHYSICAL_WRITESAdded #def RESOURCE_TYPE_IO

#### kern/kcdata.h (Added)

Added [codesigning_exit_reason_info](https://developer.apple.com/documentation/kernel/codesigning_exit_reason_info)Added [dyld_uuid_info_64_v2](https://developer.apple.com/documentation/kernel/dyld_uuid_info_64_v2)Added #def EXIT_REASON_CODESIG_PATH_MAXAdded #def EXIT_REASON_CODESIGNING_INFOAdded #def EXIT_REASON_PAYLOAD_MAX_LENAdded #def EXIT_REASON_SNAPSHOTAdded [exit_reason_snapshot](https://developer.apple.com/documentation/kernel/exit_reason_snapshot)Added #def EXIT_REASON_USER_DESCAdded #def EXIT_REASON_USER_DESC_MAX_LENAdded #def EXIT_REASON_USER_PAYLOADAdded #def KCDATA_ALIGNMENT_SIZEAdded #def KCDATA_BUFFER_BEGIN_DELTA_STACKSHOTAdded #def KCDATA_BUFFER_BEGIN_OS_REASONAdded #def KCDATA_BUFFER_BEGIN_XNUPOST_CONFIGAdded [kcdata_calc_padding()](https://developer.apple.com/documentation/kernel/1644354-kcdata_calc_padding)Added [kcdata_flags_get_padding()](https://developer.apple.com/documentation/kernel/1644444-kcdata_flags_get_padding)Added #def KCDATA_FLAGS_STRUCT_HAS_PADDINGAdded #def KCDATA_FLAGS_STRUCT_PADDING_MASKAdded [kcdata_invalid_iter](https://developer.apple.com/documentation/kernel/kcdata_invalid_iter)Added [kcdata_iter()](https://developer.apple.com/documentation/kernel/1644413-kcdata_iter)Added [kcdata_iter_array_elem_count()](https://developer.apple.com/documentation/kernel/1644336-kcdata_iter_array_elem_count)Added [kcdata_iter_array_elem_size()](https://developer.apple.com/documentation/kernel/1644411-kcdata_iter_array_elem_size)Added [kcdata_iter_array_elem_type()](https://developer.apple.com/documentation/kernel/1644333-kcdata_iter_array_elem_type)Added [kcdata_iter_array_size_switch()](https://developer.apple.com/documentation/kernel/1644352-kcdata_iter_array_size_switch)Added [kcdata_iter_array_valid()](https://developer.apple.com/documentation/kernel/1644409-kcdata_iter_array_valid)Added [kcdata_iter_container_id()](https://developer.apple.com/documentation/kernel/1644447-kcdata_iter_container_id)Added [kcdata_iter_container_type()](https://developer.apple.com/documentation/kernel/1644401-kcdata_iter_container_type)Added [kcdata_iter_container_valid()](https://developer.apple.com/documentation/kernel/1644455-kcdata_iter_container_valid)Added [kcdata_iter_data_with_desc_valid()](https://developer.apple.com/documentation/kernel/1644445-kcdata_iter_data_with_desc_valid)Added [kcdata_iter_find_type()](https://developer.apple.com/documentation/kernel/1644421-kcdata_iter_find_type)Added [kcdata_iter_flags()](https://developer.apple.com/documentation/kernel/1644383-kcdata_iter_flags)Added #def KCDATA_ITER_FOREACHAdded #def KCDATA_ITER_FOREACH_FAILEDAdded [kcdata_iter_get_data_with_desc()](https://developer.apple.com/documentation/kernel/1644414-kcdata_iter_get_data_with_desc)Added [kcdata_iter_is_legacy_item()](https://developer.apple.com/documentation/kernel/1644404-kcdata_iter_is_legacy_item)Added [kcdata_iter_next()](https://developer.apple.com/documentation/kernel/1644423-kcdata_iter_next)Added [kcdata_iter_payload()](https://developer.apple.com/documentation/kernel/1644368-kcdata_iter_payload)Added [kcdata_iter_size()](https://developer.apple.com/documentation/kernel/1644412-kcdata_iter_size)Added [kcdata_iter_string()](https://developer.apple.com/documentation/kernel/1644356-kcdata_iter_string)Added [kcdata_iter_t](https://developer.apple.com/documentation/kernel/kcdata_iter_t)Added [kcdata_iter_type()](https://developer.apple.com/documentation/kernel/1644351-kcdata_iter_type)Added [kcdata_iter_unsafe()](https://developer.apple.com/documentation/kernel/1644335-kcdata_iter_unsafe)Added [kcdata_iter_valid()](https://developer.apple.com/documentation/kernel/1644360-kcdata_iter_valid)Added #def KCDATA_TYPE_ARRAY_PAD0Added #def KCDATA_TYPE_ARRAY_PAD1Added #def KCDATA_TYPE_ARRAY_PAD2Added #def KCDATA_TYPE_ARRAY_PAD3Added #def KCDATA_TYPE_ARRAY_PAD4Added #def KCDATA_TYPE_ARRAY_PAD5Added #def KCDATA_TYPE_ARRAY_PAD6Added #def KCDATA_TYPE_ARRAY_PAD7Added #def KCDATA_TYPE_ARRAY_PAD8Added #def KCDATA_TYPE_ARRAY_PAD9Added #def KCDATA_TYPE_ARRAY_PADaAdded #def KCDATA_TYPE_ARRAY_PADbAdded #def KCDATA_TYPE_ARRAY_PADcAdded #def KCDATA_TYPE_ARRAY_PADdAdded #def KCDATA_TYPE_ARRAY_PADeAdded #def KCDATA_TYPE_ARRAY_PADfAdded #def KCDATA_TYPE_NESTED_KCDATAAdded #def KCDATA_TYPE_PIDAdded #def KCDATA_TYPE_PROCNAMEAdded #def KCS_SUBTYPE_FLAGS_MERGEAdded #def KCS_SUBTYPE_FLAGS_STRUCTAdded [kTaskIsDirty](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisdirty)Added [kTaskSharedRegionInfoUnavailable](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktasksharedregioninfounavailable)Added [kTaskUUIDInfoFaultedIn](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskuuidinfofaultedin)Added [kTaskUUIDInfoMissing](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskuuidinfomissing)Added [kTaskUUIDInfoTriedFault](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskuuidinfotriedfault)Added [kTaskWqExceededConstrainedThreadLimit](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskwqexceededconstrainedthreadlimit)Added [kTaskWqExceededTotalThreadLimit](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskwqexceededtotalthreadlimit)Added [kTaskWqFlagsAvailable](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskwqflagsavailable)Added [kThreadIdleWorker](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadidleworker)Added [kThreadOnCore](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadoncore)Added [kThreadTriedFaultBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadtriedfaultbt)Added #def SS_TH_IDLEAdded #def SS_TH_RUNAdded #def SS_TH_SUSPAdded #def SS_TH_TERMINATEAdded #def SS_TH_TERMINATE2Added #def SS_TH_UNINTAdded #def SS_TH_WAITAdded [stackshot_cpu_times](https://developer.apple.com/documentation/kernel/stackshot_cpu_times)Added [stackshot_duration](https://developer.apple.com/documentation/kernel/stackshot_duration)Added [stackshot_fault_stats](https://developer.apple.com/documentation/kernel/stackshot_fault_stats)Added #def STACKSHOT_KCTYPE_CPU_TIMESAdded #def STACKSHOT_KCTYPE_DELTA_SINCE_TIMESTAMPAdded #def STACKSHOT_KCTYPE_DONATING_PIDSAdded #def STACKSHOT_KCTYPE_KERN_STACKLRAdded #def STACKSHOT_KCTYPE_KERN_STACKLR64Added #def STACKSHOT_KCTYPE_KERNELCACHE_LOADINFOAdded #def STACKSHOT_KCTYPE_NONRUNNABLE_TASKSAdded #def STACKSHOT_KCTYPE_NONRUNNABLE_TIDSAdded #def STACKSHOT_KCTYPE_STACKSHOT_DURATIONAdded #def STACKSHOT_KCTYPE_STACKSHOT_FAULT_STATSAdded #def STACKSHOT_KCTYPE_TASK_DELTA_SNAPSHOTAdded #def STACKSHOT_KCTYPE_THREAD_DELTA_SNAPSHOTAdded #def STACKSHOT_KCTYPE_USER_STACKLRAdded #def STACKSHOT_KCTYPE_USER_STACKLR64Added #def TASK_CRASHINFO_COALITION_IDAdded #def TASK_CRASHINFO_MEMORY_LIMITAdded #def TASK_CRASHINFO_UDATA_PTRSAdded [task_delta_snapshot_v2](https://developer.apple.com/documentation/kernel/task_delta_snapshot_v2)Added [thread_delta_snapshot_v2](https://developer.apple.com/documentation/kernel/thread_delta_snapshot_v2)Added [thread_snapshot_v3](https://developer.apple.com/documentation/kernel/thread_snapshot_v3)Added [user32_dyld_uuid_info](https://developer.apple.com/documentation/kernel/user32_dyld_uuid_info)Added [user64_dyld_uuid_info](https://developer.apple.com/documentation/kernel/user64_dyld_uuid_info)Added #def XNUPOST_KCTYPE_TESTCONFIGModified [dyld_uuid_info_32](https://developer.apple.com/documentation/kernel/dyld_uuid_info_32)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [dyld_uuid_info_64](https://developer.apple.com/documentation/kernel/dyld_uuid_info_64)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [io_stats_snapshot](https://developer.apple.com/documentation/kernel/io_stats_snapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_CHAR](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_char)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int16)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int32)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int64)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int8)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint16)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint32)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint64)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint8)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_BUFFER_BEGIN_CRASHINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_BUFFER_BEGIN_STACKSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_DESC_MAXLEN

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_item_t](https://developer.apple.com/documentation/kernel/kcdata_item_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_subtype_descriptor_t](https://developer.apple.com/documentation/kernel/kcdata_subtype_descriptor_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_ARRAY

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_BINDATA_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_BUFFER_END

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_CONTAINER_BEGIN

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_CONTAINER_END

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_type_definition](https://developer.apple.com/documentation/kernel/kcdata_type_definition)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INVALID

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_LIBRARY_LOADINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_LIBRARY_LOADINFO64

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_MACH_ABSOLUTE_TIME

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_STRING_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TIMEBASE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TIMEVAL

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TYPEDEFINTION

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_UINT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_UINT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_USECS_SINCE_EPOCH

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_get_elem_count()](https://developer.apple.com/documentation/kernel/1588393-kcs_get_elem_count)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_get_elem_size()](https://developer.apple.com/documentation/kernel/1588402-kcs_get_elem_size)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_set_elem_size()](https://developer.apple.com/documentation/kernel/1588385-kcs_set_elem_size)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` kern_return_t kcs_set_elem_size (     kcdata_subtype_descriptor_t d,     uint32_t size,     uint32_t count ); ``` | Kernel/kern/kern_cdata.h |
| To | ``` int kcs_set_elem_size (     kcdata_subtype_descriptor_t d,     uint32_t size,     uint32_t count ); ``` | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_FLAGS_ARRAY

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_FLAGS_NONE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_PACK_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kctype_subtype_t](https://developer.apple.com/documentation/kernel/kctype_subtype_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kFrozen](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kfrozen)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kGlobalForcedIdle](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kglobalforcedidle)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kHasDispatchSerial](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/khasdispatchserial)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kPidSuspended](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kpidsuspended)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kStacksPCOnly](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kstackspconly)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskdarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskExtDarwinBG](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskextdarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsBoosted](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisboosted)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsForeground](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisforeground)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisimpdonor)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsLiveImpDonor](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskisliveimpdonor)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsSuppressed](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskissuppressed)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskIsTimerThrottled](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskistimerthrottled)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskRsrcFlagged](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskrsrcflagged)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskVisNonvisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisnonvisible)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTaskVisVisible](https://developer.apple.com/documentation/kernel/task_snapshot_flags/ktaskvisvisible)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kTerminatedSnapshot](https://developer.apple.com/documentation/kernel/task_snapshot_flags/kterminatedsnapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadDarwinBG](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreaddarwinbg)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadFaultedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadfaultedbt)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadIOPassive](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadiopassive)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadSuspended](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadsuspended)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [kThreadTruncatedBT](https://developer.apple.com/documentation/kernel/thread_snapshot_flags/kthreadtruncatedbt)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [mem_and_io_snapshot](https://developer.apple.com/documentation/kernel/mem_and_io_snapshot)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [stack_snapshot_frame32](https://developer.apple.com/documentation/kernel/stack_snapshot_frame32)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [stack_snapshot_frame64](https://developer.apple.com/documentation/kernel/stack_snapshot_frame64)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_IO_NUM_PRIORITIES

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCCONTAINER_TASK

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCCONTAINER_THREAD

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_BOOTARGS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_GLOBAL_MEM_STATS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_IOSTATS

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_JETSAM_LEVEL

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_PAGE_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_STACKFRAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_KERN_STACKFRAME64

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_OSVERSION

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_SHAREDCACHE_LOADINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_TASK_SNAPSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_THREAD_NAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_THREAD_SNAPSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_USER_STACKFRAME

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_KCTYPE_USER_STACKFRAME64

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def STACKSHOT_MAX_THREAD_NAME_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_ARGSLEN

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_BEGIN

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_BSDINFOWITHUNIQID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_CPUTYPE

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_CRASHED_THREADID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_DIRTY_FLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_END

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_EXCEPTION_CODES

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_EXTMODINFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_GID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PPID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_ARGC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_CSFLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_FLAGS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_NAME

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_PATH

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_STARTTIME

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_PROC_STATUS

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RESPONSIBLE_PID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RUSAGE

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_RUSAGE_INFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_STRING_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_TASKDYLD_INFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UINT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UINT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_USERSTACK

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_UUID

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified #def TASK_CRASHINFO_WORKQUEUEINFO

|  | Header |
| --- | --- |
| From | Kernel/corpses/task_corpse.h |
| To | Kernel/kern/kcdata.h |

Modified [task_snapshot_flags](https://developer.apple.com/documentation/kernel/task_snapshot_flags)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [task_snapshot_v2](https://developer.apple.com/documentation/kernel/task_snapshot_v2)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [thread_snapshot_flags](https://developer.apple.com/documentation/kernel/thread_snapshot_flags)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

Modified [thread_snapshot_v2](https://developer.apple.com/documentation/kernel/thread_snapshot_v2)

|  | Header |
| --- | --- |
| From | Kernel/kern/debug.h |
| To | Kernel/kern/kcdata.h |

#### kern/kern_cdata.h

Removed KCDATA_ITEM_FIND_TYPE()Added [kcdata_descriptor_t](https://developer.apple.com/documentation/kernel/kcdata_descriptor_t)Added [kcdata_estimate_required_buffer_size()](https://developer.apple.com/documentation/kernel/2097077-kcdata_estimate_required_buffer_)Added #def kcdata_get_container_typeAdded #def kcdata_get_data_with_descAdded [kcdata_get_memory_addr()](https://developer.apple.com/documentation/kernel/2097078-kcdata_get_memory_addr)Added [kcdata_get_memory_addr_for_array()](https://developer.apple.com/documentation/kernel/2097076-kcdata_get_memory_addr_for_array)Added #def KCDATA_ITEM_DATA_PTRAdded #def KCDATA_ITEM_FIND_TYPEAdded #def KCDATA_ITEM_ITERAdded [kcdata_memcpy()](https://developer.apple.com/documentation/kernel/2097081-kcdata_memcpy)Added [kcdata_memory_get_used_bytes()](https://developer.apple.com/documentation/kernel/2097079-kcdata_memory_get_used_bytes)Modified [KC_ST_CHAR](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_char)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int16)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int32)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int64)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_INT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_int8)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT16](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint16)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT32](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint32)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT64](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint64)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [KC_ST_UINT8](https://developer.apple.com/documentation/kernel/kctype_subtype_t/kc_st_uint8)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_BUFFER_BEGIN_CRASHINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_BUFFER_BEGIN_STACKSHOT

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_DESC_MAXLEN

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_item_t](https://developer.apple.com/documentation/kernel/kcdata_item_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_subtype_descriptor_t](https://developer.apple.com/documentation/kernel/kcdata_subtype_descriptor_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_ARRAY

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_BINDATA_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_BUFFER_END

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_CONTAINER_BEGIN

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_CONTAINER_END

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcdata_type_definition](https://developer.apple.com/documentation/kernel/kcdata_type_definition)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_INVALID

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_LIBRARY_LOADINFO

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_LIBRARY_LOADINFO64

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_MACH_ABSOLUTE_TIME

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_STRING_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TIMEBASE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TIMEVAL

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_TYPEDEFINTION

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_UINT32_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_UINT64_DESC

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCDATA_TYPE_USECS_SINCE_EPOCH

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_get_elem_count()](https://developer.apple.com/documentation/kernel/1588393-kcs_get_elem_count)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_get_elem_size()](https://developer.apple.com/documentation/kernel/1588402-kcs_get_elem_size)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kcs_set_elem_size()](https://developer.apple.com/documentation/kernel/1588385-kcs_set_elem_size)

|  | Declaration | Header |
| --- | --- | --- |
| From | ``` kern_return_t kcs_set_elem_size (     kcdata_subtype_descriptor_t d,     uint32_t size,     uint32_t count ); ``` | Kernel/kern/kern_cdata.h |
| To | ``` int kcs_set_elem_size (     kcdata_subtype_descriptor_t d,     uint32_t size,     uint32_t count ); ``` | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_FLAGS_ARRAY

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_FLAGS_NONE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified #def KCS_SUBTYPE_PACK_SIZE

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

Modified [kctype_subtype_t](https://developer.apple.com/documentation/kernel/kctype_subtype_t)

|  | Header |
| --- | --- |
| From | Kernel/kern/kern_cdata.h |
| To | Kernel/kern/kcdata.h |

#### kern/kpc.h

Removed kpc_switch_context()Added #def KERN_KPC_HAdded [kpc_unregister_cpu()](https://developer.apple.com/documentation/kernel/1645398-kpc_unregister_cpu)

#### kern/ledger.h

Added #def LEDGER_MAX_CMD

#### kern/locks.h

Added #def LCK_ASSERT_NOTOWNEDAdded #def LCK_ASSERT_OWNEDAdded #def LCK_MTX_ASSERTAdded #def LCK_MTX_ASSERT_DEBUG

#### kern/sched_prim.h

Removed thread_wakeup_prim_internal()Added [thread_wakeup_thread()](https://developer.apple.com/documentation/kernel/1646218-thread_wakeup_thread)

#### kern/task.h

Added #def TF_NONE

#### kern/telemetry.h

Removed compute_telemetry_windowed()Removed telemetry_disable_window()Removed telemetry_enable_window()Removed telemetry_gather_windowed()Removed telemetry_window_enabledAdded bootprofile_get()Modified telemetry_ast()

|  | Declaration |
| --- | --- |
| From | ``` void telemetry_ast (     thread_t,     boolean_t interrupted_userspace,     boolean_t is_windowed ); ``` |
| To | ``` void telemetry_ast (     thread_t,     boolean_t interrupted_userspace,     boolean_t io_telemetry ); ``` |

#### kextd/kextd_mach.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### libkern/c++/OSMetaClass.h

Added #def APPLE_KEXT_ALIGN_CONTAINERS

#### libkern/c++/OSSerialize.h

Added [OSArray](https://developer.apple.com/documentation/kernel/osarray)

#### libkern/c++/OSString.h

Removed OSString::initWithStringOfLength()

#### libkern/libkern.h

Added [crc16()](https://developer.apple.com/documentation/kernel/1643494-crc16)Modified [clz()](https://developer.apple.com/documentation/kernel/1441034-clz)

|  | Declaration |
| --- | --- |
| From | ``` unsigned int clz (     unsigned int num ); ``` |
| To | ``` int clz (     unsigned int num ); ``` |

#### libkern/machine/OSByteOrder.h

Modified #def OS_INLINE

|  | Header |
| --- | --- |
| From | Kernel/libkern/machine/OSByteOrder.h |
| To | Kernel/os/base.h |

#### libkern/OSKextLib.h

Added [OSKextResetPgoCounters()](https://developer.apple.com/documentation/kernel/1646298-oskextresetpgocounters)Added [OSKextResetPgoCountersLock()](https://developer.apple.com/documentation/kernel/1646299-oskextresetpgocounterslock)Added [OSKextResetPgoCountersUnlock()](https://developer.apple.com/documentation/kernel/1646297-oskextresetpgocountersunlock)

#### lockd/lockd_mach.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach-o/loader.h

Added #def LC_VERSION_MIN_TVOS

#### mach/audit_triggers_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/clock.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/coalition_notification_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/dyld_kernel.h (Added)

Added [dyld_kernel_image_info_array_t](https://developer.apple.com/documentation/kernel/dyld_kernel_image_info_array_t)Added [dyld_kernel_image_info_t](https://developer.apple.com/documentation/kernel/dyld_kernel_image_info_t)Added [dyld_kernel_process_info_t](https://developer.apple.com/documentation/kernel/dyld_kernel_process_info_t)

#### mach/host_info.h

Added #def HOST_CAN_HAS_DEBUGGERAdded #def HOST_CAN_HAS_DEBUGGER_COUNTAdded [host_can_has_debugger_info_data_t](https://developer.apple.com/documentation/kernel/host_can_has_debugger_info_data_t)Added [host_can_has_debugger_info_t](https://developer.apple.com/documentation/kernel/host_can_has_debugger_info_t)

#### mach/host_notify.h

Added #def HOST_CALENDAR_SET_REPLYIDAdded #def HOST_NOTIFY_CALENDAR_SET

#### mach/host_special_ports.h

Added #def host_get_ktrace_background_portAdded #def host_get_node_portAdded #def HOST_KTRACE_BACKGROUND_PORTAdded #def HOST_NODE_PORTAdded #def HOST_RESOURCE_NOTIFY_PORTAdded #def host_set_ktrace_background_portAdded #def host_set_node_port

#### mach/ktrace_background.h (Added)

Added #def ktrace_background_MSG_COUNTAdded [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added [send_ktrace_background_available()](https://developer.apple.com/documentation/kernel/1645220-send_ktrace_background_available)Added #def subsystem_to_name_map_ktrace_backgroundAdded #def USING_MIG_STRNCPY_ZEROFILL

#### mach/mach_time.h

Added [mach_continuous_approximate_time()](https://developer.apple.com/documentation/kernel/1646198-mach_continuous_approximate_time)Added [mach_continuous_time()](https://developer.apple.com/documentation/kernel/1646199-mach_continuous_time)

#### mach/mach_vm.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/mach_voucher.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/mach_voucher_attr_control.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/mach_voucher_types.h

Added #def MACH_ACTIVITY_ID_COUNT_MAXAdded #def MACH_VOUCHER_ATTR_KEY_PTHPRIORITYAdded #def MACH_VOUCHER_ATTR_MAX_RAW_RECIPE_ARRAY_SIZEAdded #def MACH_VOUCHER_TRAP_STACK_LIMIT

#### mach/machine.h

Removed #def CPUFAMILY_INTEL_6_14Removed #def CPUFAMILY_INTEL_6_15Removed #def CPUFAMILY_INTEL_CORERemoved #def CPUFAMILY_INTEL_CORE2Removed #def CPUFAMILY_INTEL_MEROMRemoved #def CPUFAMILY_INTEL_YONAHAdded #def CPUFAMILY_ARM_HURRICANE

#### mach/machine/sdt.h

Added #def DTRACE_MEMORYSTATUS2Added #def DTRACE_MEMORYSTATUS3Added #def DTRACE_MEMORYSTATUS6Added #def DTRACE_PHYSLAT3Added #def DTRACE_PROBEAdded #def DTRACE_PROBE1Added #def DTRACE_PROBE10Added #def DTRACE_PROBE2Added #def DTRACE_PROBE3Added #def DTRACE_PROBE4Added #def DTRACE_PROBE5Added #def DTRACE_PROBE6Added #def DTRACE_PROBE7Added #def DTRACE_PROBE8Added #def DTRACE_PROBE9Added #def DTRACE_TMR4Added #def DTRACE_TMR5Added #def DTRACE_TMR6Added #def DTRACE_TMR7Added #def DTRACE_VM6

#### mach/memory_object_control.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/memory_object_default_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/memory_object_server.h (Removed)

Removed memory_object_data_initialize()Removed memory_object_data_reclaim()Removed memory_object_data_request()Removed memory_object_data_return()Removed memory_object_data_unlock()Removed memory_object_init()Removed memory_object_last_unmap()Removed memory_object_map()Removed #def memory_object_MSG_COUNTRemoved memory_object_server()Removed memory_object_server_routine()Removed memory_object_subsystemRemoved memory_object_subsystemRemoved memory_object_synchronize()Removed memory_object_terminate()Removed #def subsystem_to_name_map_memory_object

#### mach/memory_object_types.h

Added #def MAP_MEM_GRAB_SECLUDED

#### mach/message.h

Added [mach_msg_priority_t](https://developer.apple.com/documentation/kernel/mach_msg_priority_t)Added #def MACH_MSG_PRIORITY_UNSPECIFIEDAdded #def MACH_SEND_OVERRIDE

#### mach/mig.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)

#### mach/sysdiagnose_notification_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/task.h

Added [task_generate_corpse()](https://developer.apple.com/documentation/kernel/1646547-task_generate_corpse)Added [task_get_dyld_image_infos()](https://developer.apple.com/documentation/kernel/1646553-task_get_dyld_image_infos)Added [task_map_corpse_info()](https://developer.apple.com/documentation/kernel/1646533-task_map_corpse_info)Added [task_map_corpse_info_64()](https://developer.apple.com/documentation/kernel/1911639-task_map_corpse_info_64)Added [task_register_dyld_get_process_state()](https://developer.apple.com/documentation/kernel/1646549-task_register_dyld_get_process_s)Added [task_register_dyld_image_infos()](https://developer.apple.com/documentation/kernel/1646550-task_register_dyld_image_infos)Added [task_register_dyld_set_dyld_state()](https://developer.apple.com/documentation/kernel/1646572-task_register_dyld_set_dyld_stat)Added [task_register_dyld_shared_cache_image_info()](https://developer.apple.com/documentation/kernel/1646581-task_register_dyld_shared_cache_)Added [task_unregister_dyld_image_infos()](https://developer.apple.com/documentation/kernel/1646587-task_unregister_dyld_image_infos)

#### mach/task_access.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/task_access_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/task_info.h

Added #def TASK_VM_INFO_REV1_COUNTAdded #def TASK_VM_INFO_REV2_COUNT

#### mach/task_special_ports.h

Added #def TASK_RESOURCE_NOTIFY_PORT

#### mach/telemetry_notification_server.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/thread_policy.h

Added #def THREAD_BACKGROUND_POLICY_DARWIN_BG

#### mach/upl.h

Added [mig_strncpy_zerofill()](https://developer.apple.com/documentation/kernel/1645207-mig_strncpy_zerofill)Added #def USING_MIG_STRNCPY_ZEROFILL

#### mach/vm_param.h

Added [mach_vm_round_page_overflow()](https://developer.apple.com/documentation/kernel/1643689-mach_vm_round_page_overflow)Added #def round_page_overflow

#### mach/vm_prot.h

Added #def VM_PROT_EXECUTE_ONLYAdded #def VM_PROT_STRIP_READ

#### mach/vm_statistics.h

Added #def VM_FLAGS_RANDOM_ADDRAdded #def VM_MEMORY_COREGRAPHICS_XALLOCAdded #def VM_MEMORY_DHMMAdded #def VM_MEMORY_SCENEKITAdded #def VM_MEMORY_SKYWALKAdded #def VM_MEMORY_SWIFT_METADATAAdded #def VM_MEMORY_SWIFT_RUNTIME

#### net/ethernet.h

Added #def ETHERTYPE_PTP

#### net/if.h

Added #def IFCAP_HW_TIMESTAMPAdded #def IFCAP_SKYWALKAdded #def IFCAP_SW_TIMESTAMPModified #def KEV_DL_ADDMULTI

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_AWDL_RESTRICTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_AWDL_UNRESTRICTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_DELMULTI

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_ATTACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_DETACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_DETACHING

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_IDLE_ROUTE_REFCNT

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IFCAP_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IFDELEGATE_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_ISSUES

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_ADDRESS_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_OFF

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_ON

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_QUALITY_METRIC_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_MASTER_ELECTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_NODE_ABSENCE

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_NODE_PRESENCE

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_PROTO_ATTACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_PROTO_DETACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_RRC_STATE_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFFLAGS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFGENERIC

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMEDIA

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMETRICS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMTU

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFPHYS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SUBCLASS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_WAKEFLAGS_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

#### net/if_utun.h

Added #def UTUN_FLAGS_ENABLE_PROC_UUIDAdded #def UTUN_OPT_ENABLE_CHANNELAdded #def UTUN_OPT_GET_CHANNEL_UUID

#### net/kpi_interface.h

Added [IFNET_HW_TIMESTAMP](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_hw_timestamp)Added [IFNET_SW_TIMESTAMP](https://developer.apple.com/documentation/kernel/1644631-anonymous/ifnet_sw_timestamp)Modified [ifnet_llbroadcast_copy_bytes()](https://developer.apple.com/documentation/kernel/1525030-ifnet_llbroadcast_copy_bytes)

|  | Declaration |
| --- | --- |
| From | ``` errno_t ifnet_llbroadcast_copy_bytes (     ifnet_t interface,     void *addr,     size_t bufferlen,     size_t *addr_len ); ``` |
| To | ``` errno_t ifnet_llbroadcast_copy_bytes (     ifnet_t interface,     void *addr,     size_t bufferlen,     size_t *out_len ); ``` |

#### net/net_kev.h (Added)

Added #def KEV_DL_QOS_MODE_CHANGEDAdded #def KEV_INET6_ADDR_DELETEDAdded #def KEV_INET6_CHANGED_ADDRAdded #def KEV_INET6_DEFROUTERAdded #def KEV_INET6_NEW_LL_ADDRAdded #def KEV_INET6_NEW_RTADV_ADDRAdded #def KEV_INET6_NEW_USER_ADDRAdded #def KEV_INET6_SUBCLASSAdded #def KEV_INET_ADDR_DELETEDAdded #def KEV_INET_ARPCOLLISIONAdded #def KEV_INET_ARPRTRALIVEAdded #def KEV_INET_ARPRTRFAILUREAdded #def KEV_INET_CHANGED_ADDRAdded #def KEV_INET_NEW_ADDRAdded #def KEV_INET_PORTINUSEAdded #def KEV_INET_SIFBRDADDRAdded #def KEV_INET_SIFDSTADDRAdded #def KEV_INET_SIFNETMASKAdded #def KEV_INET_SUBCLASSModified #def KEV_DL_ADDMULTI

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_AWDL_RESTRICTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_AWDL_UNRESTRICTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_DELMULTI

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_ATTACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_DETACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_DETACHING

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IF_IDLE_ROUTE_REFCNT

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IFCAP_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_IFDELEGATE_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_ISSUES

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_ADDRESS_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_OFF

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_ON

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_LINK_QUALITY_METRIC_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_MASTER_ELECTED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_NODE_ABSENCE

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_NODE_PRESENCE

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_PROTO_ATTACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_PROTO_DETACHED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_RRC_STATE_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFFLAGS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFGENERIC

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMEDIA

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMETRICS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFMTU

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SIFPHYS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_SUBCLASS

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

Modified #def KEV_DL_WAKEFLAGS_CHANGED

|  | Header |
| --- | --- |
| From | Kernel/net/if.h |
| To | Kernel/net/net_kev.h |

#### netinet/ip.h

Added #def IPTOS_DSCP_SHIFT

#### os/base.h (Added)

Added #def OS_ALIGNEDAdded #def OS_ALWAYS_INLINEAdded #def OS_ASSUME_NONNULL_BEGINAdded #def OS_ASSUME_NONNULL_ENDAdded [os_block_t](https://developer.apple.com/documentation/os/os_block_t)Added #def OS_COLDAdded #def os_compiler_barrierAdded #def OS_COMPILER_CAN_ASSUMEAdded #def OS_CONCATAdded #def OS_CONSTAdded #def OS_ENUMAdded #def OS_EXPECTAdded #def OS_EXPORTAdded #def OS_FORMAT_PRINTFAdded [os_function_t](https://developer.apple.com/documentation/os/os_function_t)Added #def os_is_compile_time_constantAdded #def OS_MALLOCAdded #def OS_NOESCAPEAdded #def OS_NOINLINEAdded #def OS_NONNULL1Added #def OS_NONNULL10Added #def OS_NONNULL11Added #def OS_NONNULL12Added #def OS_NONNULL13Added #def OS_NONNULL14Added #def OS_NONNULL15Added #def OS_NONNULL2Added #def OS_NONNULL3Added #def OS_NONNULL4Added #def OS_NONNULL5Added #def OS_NONNULL6Added #def OS_NONNULL7Added #def OS_NONNULL8Added #def OS_NONNULL9Added #def OS_NONNULL_ALLAdded #def OS_NORETURNAdded #def OS_NOT_TAIL_CALLEDAdded #def OS_NOTHROWAdded #def OS_OVERLOADABLEAdded #def os_prevent_tail_call_optimizationAdded #def OS_PUREAdded #def OS_REFINED_FOR_SWIFTAdded #def OS_SENTINELAdded #def OS_STRINGIFYAdded #def OS_SWIFT_NAMEAdded #def OS_SWIFT_UNAVAILABLEAdded #def OS_TRANSPARENT_UNIONAdded #def OS_UNUSEDAdded #def OS_USEDAdded #def OS_WARN_RESULTAdded #def OS_WEAKAdded #def OS_WEAK_IMPORTModified #def OS_INLINE

|  | Header |
| --- | --- |
| From | Kernel/libkern/machine/OSByteOrder.h |
| To | Kernel/os/base.h |

#### os/log.h (Added)

Added [OS_os_log](https://developer.apple.com/documentation/kernel/os_os_log)Added [#def os_log](https://developer.apple.com/documentation/os/os_log)Added [os_log_create()](https://developer.apple.com/documentation/os/oslog/1643744-init)Added [#def os_log_debug](https://developer.apple.com/documentation/os/os_log_debug)Added [os_log_debug_enabled()](https://developer.apple.com/documentation/kernel/1643808-os_log_debug_enabled)Added [#def OS_LOG_DEFAULT](https://developer.apple.com/documentation/os/os_log_default)Added [#def OS_LOG_DISABLED](https://developer.apple.com/documentation/os/os_log_disabled)Added [#def os_log_error](https://developer.apple.com/documentation/os/os_log_error)Added [#def os_log_fault](https://developer.apple.com/documentation/os/os_log_fault)Added [#def os_log_info](https://developer.apple.com/documentation/os/os_log_info)Added [os_log_info_enabled()](https://developer.apple.com/documentation/kernel/1643817-os_log_info_enabled)Added #def OS_LOG_NOTAILCALLAdded #def OS_LOG_NOTAILCALL_MARKERAdded #def os_log_sensitive_debugAdded [os_log_t](https://developer.apple.com/documentation/kernel/os_log_t)Added [OS_LOG_TYPE_DEBUG](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_debug)Added [OS_LOG_TYPE_DEFAULT](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_default)Added [OS_LOG_TYPE_ERROR](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_error)Added [OS_LOG_TYPE_FAULT](https://developer.apple.com/documentation/kernel/os_log_type_t/os_log_type_fault)Added [OS_LOG_TYPE_INFO](https://developer.apple.com/documentation/os/os_log_type_t/os_log_type_info)Added [os_log_type_t](https://developer.apple.com/documentation/os/os_log_type_t)Added [#def os_log_with_type](https://developer.apple.com/documentation/os/os_log_with_type)

#### os/object.h (Added)

Added #def fastpathAdded #def OS_OBJC_INDEPENDENT_CLASSAdded #def OS_OBJECT_BRIDGEAdded #def OS_OBJECT_CLASSAdded #def OS_OBJECT_CONSUMEDAdded #def OS_OBJECT_DECLAdded #def OS_OBJECT_DECL_IMPLAdded #def OS_OBJECT_DECL_SUBCLASSAdded #def OS_OBJECT_GLOBAL_OBJECTAdded #def OS_OBJECT_HAVE_OBJC_SUPPORTAdded #def OS_OBJECT_RETURNS_RETAINEDAdded #def OS_OBJECT_USE_OBJCAdded #def OS_OBJECT_USE_OBJC_RETAIN_RELEASEAdded [os_release()](https://developer.apple.com/documentation/kernel/1646596-os_release)Added #def os_releaseAdded [os_retain()](https://developer.apple.com/documentation/os/1524246-os_retain)Added #def os_retainAdded #def OS_WARN_RESULT_NEEDS_RELEASEAdded #def slowpath

#### os/overflow.h

Added #def os_add_and_mul_overflowAdded #def os_mul_and_add_overflow

#### pexpert/i386/boot.h

Added [Boot_VideoV1](https://developer.apple.com/documentation/kernel/boot_videov1)

#### pexpert/pexpert.h

Added [gPlatformMemoryID](https://developer.apple.com/documentation/kernel/gplatformmemoryid)

#### security/mac_policy.h

Added mac_file_getxattr()Added mac_file_removexattr()Added mac_file_setxattr()Added mpo_exc_action_check_exception_send_tAdded mpo_exc_action_label_associate_tAdded mpo_exc_action_label_copy_tAdded mpo_exc_action_label_destroy_tAdded mpo_exc_action_label_init_tAdded mpo_exc_action_label_update_tAdded mpo_file_check_library_validation_tAdded mpo_mount_check_snapshot_create_tAdded mpo_mount_check_snapshot_delete_tAdded mpo_proc_check_get_cs_info_tAdded mpo_proc_check_set_cs_info_tAdded mpo_vnode_check_clone_tAdded mpo_vnode_check_setacl_tAdded mpo_vnode_notify_deleteextattr_tAdded mpo_vnode_notify_setacl_tAdded mpo_vnode_notify_setattrlist_tAdded mpo_vnode_notify_setextattr_tAdded mpo_vnode_notify_setflags_tAdded mpo_vnode_notify_setmode_tAdded mpo_vnode_notify_setowner_tAdded mpo_vnode_notify_setutimes_tAdded mpo_vnode_notify_truncate_t

#### sys/_types/_fsobj_id_t.h (Added)

Modified [fsobj_id_t](https://developer.apple.com/documentation/kernel/fsobj_id_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/attr.h |
| To | Kernel/sys/_types/_fsobj_id_t.h |

#### sys/_types/_os_inline.h

Removed #def OS_INLINE

#### sys/_types/_u_int16_t.h (Added)

Modified [u_int16_t](https://developer.apple.com/documentation/kernel/u_int16_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int16_t.h |

#### sys/_types/_u_int32_t.h (Added)

Modified [u_int32_t](https://developer.apple.com/documentation/kernel/u_int32_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int32_t.h |

#### sys/_types/_u_int64_t.h (Added)

Modified [u_int64_t](https://developer.apple.com/documentation/kernel/u_int64_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int64_t.h |

#### sys/_types/_u_int8_t.h (Added)

Modified [u_int8_t](https://developer.apple.com/documentation/kernel/u_int8_t)

|  | Header |
| --- | --- |
| From | Kernel/i386/types.h |
| To | Kernel/sys/_types/_u_int8_t.h |

#### sys/attr.h

Added #def VOL_CAP_FMT_DIR_HARDLINKSAdded #def VOL_CAP_FMT_DOCUMENT_IDAdded #def VOL_CAP_FMT_WRITE_GENERATION_COUNTAdded #def VOL_CAP_INT_CLONEAdded #def VOL_CAP_INT_RENAME_EXCLAdded #def VOL_CAP_INT_RENAME_SWAPModified [fsobj_id_t](https://developer.apple.com/documentation/kernel/fsobj_id_t)

|  | Header |
| --- | --- |
| From | Kernel/sys/attr.h |
| To | Kernel/sys/_types/_fsobj_id_t.h |

#### sys/buf.h

Modified [buf_alloc()](https://developer.apple.com/documentation/kernel/1561906-buf_alloc)

|  | Declaration |
| --- | --- |
| From | ``` buf_t buf_alloc (     vnode_t ); ``` |
| To | ``` buf_t buf_alloc (     vnode_t vp ); ``` |

Modified [buf_attr()](https://developer.apple.com/documentation/kernel/1561894-buf_attr)

|  | Declaration |
| --- | --- |
| From | ``` bufattr_t buf_attr (     buf_t ); ``` |
| To | ``` bufattr_t buf_attr (     buf_t bp ); ``` |

Modified [buf_bawrite()](https://developer.apple.com/documentation/kernel/1561823-buf_bawrite)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_bawrite (     buf_t ); ``` |
| To | ``` errno_t buf_bawrite (     buf_t bp ); ``` |

Modified [buf_bdwrite()](https://developer.apple.com/documentation/kernel/1561858-buf_bdwrite)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_bdwrite (     buf_t ); ``` |
| To | ``` errno_t buf_bdwrite (     buf_t bp ); ``` |

Modified [buf_biodone()](https://developer.apple.com/documentation/kernel/1561914-buf_biodone)

|  | Declaration |
| --- | --- |
| From | ``` void buf_biodone (     buf_t ); ``` |
| To | ``` void buf_biodone (     buf_t bp ); ``` |

Modified [buf_biowait()](https://developer.apple.com/documentation/kernel/1561908-buf_biowait)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_biowait (     buf_t ); ``` |
| To | ``` errno_t buf_biowait (     buf_t bp ); ``` |

Modified [buf_blkno()](https://developer.apple.com/documentation/kernel/1561926-buf_blkno)

|  | Declaration |
| --- | --- |
| From | ``` daddr64_t buf_blkno (     buf_t ); ``` |
| To | ``` daddr64_t buf_blkno (     buf_t bp ); ``` |

Modified [buf_bread()](https://developer.apple.com/documentation/kernel/1561851-buf_bread)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_bread (     vnode_t,     daddr64_t,     int,     kauth_cred_t,     buf_t * ); ``` |
| To | ``` errno_t buf_bread (     vnode_t vp,     daddr64_t blkno,     int size,     kauth_cred_t cred,     buf_t *bpp ); ``` |

Modified [buf_breadn()](https://developer.apple.com/documentation/kernel/1561873-buf_breadn)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_breadn (     vnode_t,     daddr64_t,     int,     daddr64_t *,     int *,     int,     kauth_cred_t,     buf_t * ); ``` |
| To | ``` errno_t buf_breadn (     vnode_t vp,     daddr64_t blkno,     int size,     daddr64_t *rablks,     int *rasizes,     int nrablks,     kauth_cred_t cred,     buf_t *bpp ); ``` |

Modified [buf_brelse()](https://developer.apple.com/documentation/kernel/1561897-buf_brelse)

|  | Declaration |
| --- | --- |
| From | ``` void buf_brelse (     buf_t ); ``` |
| To | ``` void buf_brelse (     buf_t bp ); ``` |

Modified [buf_bwrite()](https://developer.apple.com/documentation/kernel/1561886-buf_bwrite)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_bwrite (     buf_t ); ``` |
| To | ``` errno_t buf_bwrite (     buf_t bp ); ``` |

Modified [buf_callback()](https://developer.apple.com/documentation/kernel/1561902-buf_callback)

|  | Declaration |
| --- | --- |
| From | ``` void * buf_callback (     buf_t ); ``` |
| To | ``` void * buf_callback (     buf_t bp ); ``` |

Modified [buf_clear()](https://developer.apple.com/documentation/kernel/1561901-buf_clear)

|  | Declaration |
| --- | --- |
| From | ``` void buf_clear (     buf_t ); ``` |
| To | ``` void buf_clear (     buf_t bp ); ``` |

Modified [buf_clear_redundancy_flags()](https://developer.apple.com/documentation/kernel/1561898-buf_clear_redundancy_flags)

|  | Declaration |
| --- | --- |
| From | ``` void buf_clear_redundancy_flags (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_clear_redundancy_flags (     buf_t bp,     uint32_t flags ); ``` |

Modified [buf_clearflags()](https://developer.apple.com/documentation/kernel/1561837-buf_clearflags)

|  | Declaration |
| --- | --- |
| From | ``` void buf_clearflags (     buf_t,     int32_t ); ``` |
| To | ``` void buf_clearflags (     buf_t bp,     int32_t flags ); ``` |

Modified [buf_clone()](https://developer.apple.com/documentation/kernel/1561867-buf_clone)

|  | Declaration |
| --- | --- |
| From | ``` buf_t buf_clone (     buf_t,     int,     int,     void (*)(buf_t, void *),     void * ); ``` |
| To | ``` buf_t buf_clone (     buf_t bp,     int io_offset,     int io_size,     void (*iodone)(buf_t, void *),     void *arg ); ``` |

Modified [buf_count()](https://developer.apple.com/documentation/kernel/1561820-buf_count)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_count (     buf_t ); ``` |
| To | ``` uint32_t buf_count (     buf_t bp ); ``` |

Modified [buf_dataptr()](https://developer.apple.com/documentation/kernel/1561881-buf_dataptr)

|  | Declaration |
| --- | --- |
| From | ``` uintptr_t buf_dataptr (     buf_t ); ``` |
| To | ``` uintptr_t buf_dataptr (     buf_t bp ); ``` |

Modified [buf_device()](https://developer.apple.com/documentation/kernel/1561922-buf_device)

|  | Declaration |
| --- | --- |
| From | ``` dev_t buf_device (     buf_t ); ``` |
| To | ``` dev_t buf_device (     buf_t bp ); ``` |

Modified [buf_dirtyend()](https://developer.apple.com/documentation/kernel/1561850-buf_dirtyend)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_dirtyend (     buf_t ); ``` |
| To | ``` uint32_t buf_dirtyend (     buf_t bp ); ``` |

Modified [buf_dirtyoff()](https://developer.apple.com/documentation/kernel/1561923-buf_dirtyoff)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_dirtyoff (     buf_t ); ``` |
| To | ``` uint32_t buf_dirtyoff (     buf_t bp ); ``` |

Modified [buf_drvdata()](https://developer.apple.com/documentation/kernel/1561866-buf_drvdata)

|  | Declaration |
| --- | --- |
| From | ``` void * buf_drvdata (     buf_t ); ``` |
| To | ``` void * buf_drvdata (     buf_t bp ); ``` |

Modified [buf_error()](https://developer.apple.com/documentation/kernel/1561818-buf_error)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_error (     buf_t ); ``` |
| To | ``` errno_t buf_error (     buf_t bp ); ``` |

Modified [buf_flags()](https://developer.apple.com/documentation/kernel/1561844-buf_flags)

|  | Declaration |
| --- | --- |
| From | ``` int32_t buf_flags (     buf_t ); ``` |
| To | ``` int32_t buf_flags (     buf_t bp ); ``` |

Modified [buf_flushdirtyblks()](https://developer.apple.com/documentation/kernel/1561822-buf_flushdirtyblks)

|  | Declaration |
| --- | --- |
| From | ``` void buf_flushdirtyblks (     vnode_t,     int,     int,     const char * ); ``` |
| To | ``` void buf_flushdirtyblks (     vnode_t vp,     int wait,     int flags,     const char *msg ); ``` |

Modified [buf_free()](https://developer.apple.com/documentation/kernel/1561907-buf_free)

|  | Declaration |
| --- | --- |
| From | ``` void buf_free (     buf_t ); ``` |
| To | ``` void buf_free (     buf_t bp ); ``` |

Modified [buf_fromcache()](https://developer.apple.com/documentation/kernel/1561933-buf_fromcache)

|  | Declaration |
| --- | --- |
| From | ``` int buf_fromcache (     buf_t ); ``` |
| To | ``` int buf_fromcache (     buf_t bp ); ``` |

Modified [buf_fsprivate()](https://developer.apple.com/documentation/kernel/1561929-buf_fsprivate)

|  | Declaration |
| --- | --- |
| From | ``` void * buf_fsprivate (     buf_t ); ``` |
| To | ``` void * buf_fsprivate (     buf_t bp ); ``` |

Modified [buf_fua()](https://developer.apple.com/documentation/kernel/1561842-buf_fua)

|  | Declaration |
| --- | --- |
| From | ``` int buf_fua (     buf_t ); ``` |
| To | ``` int buf_fua (     buf_t bp ); ``` |

Modified [buf_getblk()](https://developer.apple.com/documentation/kernel/1561932-buf_getblk)

|  | Declaration |
| --- | --- |
| From | ``` buf_t buf_getblk (     vnode_t,     daddr64_t,     int,     int,     int,     int ); ``` |
| To | ``` buf_t buf_getblk (     vnode_t vp,     daddr64_t blkno,     int size,     int slpflag,     int slptimeo,     int operation ); ``` |

Modified [buf_geteblk()](https://developer.apple.com/documentation/kernel/1561862-buf_geteblk)

|  | Declaration |
| --- | --- |
| From | ``` buf_t buf_geteblk (     int ); ``` |
| To | ``` buf_t buf_geteblk (     int size ); ``` |

Modified [buf_invalblkno()](https://developer.apple.com/documentation/kernel/1561843-buf_invalblkno)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_invalblkno (     vnode_t,     daddr64_t,     int ); ``` |
| To | ``` errno_t buf_invalblkno (     vnode_t vp,     daddr64_t lblkno,     int flags ); ``` |

Modified [buf_invalidateblks()](https://developer.apple.com/documentation/kernel/1561910-buf_invalidateblks)

|  | Declaration |
| --- | --- |
| From | ``` int buf_invalidateblks (     vnode_t,     int,     int,     int ); ``` |
| To | ``` int buf_invalidateblks (     vnode_t vp,     int flags,     int slpflag,     int slptimeo ); ``` |

Modified [buf_iterate()](https://developer.apple.com/documentation/kernel/1561857-buf_iterate)

|  | Declaration |
| --- | --- |
| From | ``` void buf_iterate (     vnode_t,     int (*)(buf_t, void *),     int,     void * ); ``` |
| To | ``` void buf_iterate (     vnode_t vp,     int (*callout)(buf_t, void *),     int flags,     void *arg ); ``` |

Modified [buf_lblkno()](https://developer.apple.com/documentation/kernel/1561825-buf_lblkno)

|  | Declaration |
| --- | --- |
| From | ``` daddr64_t buf_lblkno (     buf_t ); ``` |
| To | ``` daddr64_t buf_lblkno (     buf_t bp ); ``` |

Modified [buf_map()](https://developer.apple.com/documentation/kernel/1561890-buf_map)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_map (     buf_t,     caddr_t * ); ``` |
| To | ``` errno_t buf_map (     buf_t bp,     caddr_t *io_addr ); ``` |

Modified [buf_markaged()](https://developer.apple.com/documentation/kernel/1561845-buf_markaged)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markaged (     buf_t ); ``` |
| To | ``` void buf_markaged (     buf_t bp ); ``` |

Modified [buf_markdelayed()](https://developer.apple.com/documentation/kernel/1561911-buf_markdelayed)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markdelayed (     buf_t ); ``` |
| To | ``` void buf_markdelayed (     buf_t bp ); ``` |

Modified [buf_markeintr()](https://developer.apple.com/documentation/kernel/1561892-buf_markeintr)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markeintr (     buf_t ); ``` |
| To | ``` void buf_markeintr (     buf_t bp ); ``` |

Modified [buf_markfua()](https://developer.apple.com/documentation/kernel/1561841-buf_markfua)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markfua (     buf_t ); ``` |
| To | ``` void buf_markfua (     buf_t bp ); ``` |

Modified [buf_markinvalid()](https://developer.apple.com/documentation/kernel/1561863-buf_markinvalid)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markinvalid (     buf_t ); ``` |
| To | ``` void buf_markinvalid (     buf_t bp ); ``` |

Modified [buf_markstatic()](https://developer.apple.com/documentation/kernel/1561839-buf_markstatic)

|  | Declaration |
| --- | --- |
| From | ``` void buf_markstatic (     buf_t ); ``` |
| To | ``` void buf_markstatic (     buf_t bp ); ``` |

Modified [buf_meta_bread()](https://developer.apple.com/documentation/kernel/1561871-buf_meta_bread)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_meta_bread (     vnode_t,     daddr64_t,     int,     kauth_cred_t,     buf_t * ); ``` |
| To | ``` errno_t buf_meta_bread (     vnode_t vp,     daddr64_t blkno,     int size,     kauth_cred_t cred,     buf_t *bpp ); ``` |

Modified [buf_meta_breadn()](https://developer.apple.com/documentation/kernel/1561821-buf_meta_breadn)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_meta_breadn (     vnode_t,     daddr64_t,     int,     daddr64_t *,     int *,     int,     kauth_cred_t,     buf_t * ); ``` |
| To | ``` errno_t buf_meta_breadn (     vnode_t vp,     daddr64_t blkno,     int size,     daddr64_t *rablks,     int *rasizes,     int nrablks,     kauth_cred_t cred,     buf_t *bpp ); ``` |

Modified [buf_proc()](https://developer.apple.com/documentation/kernel/1561855-buf_proc)

|  | Declaration |
| --- | --- |
| From | ``` proc_t buf_proc (     buf_t ); ``` |
| To | ``` proc_t buf_proc (     buf_t bp ); ``` |

Modified [buf_rcred()](https://developer.apple.com/documentation/kernel/1561836-buf_rcred)

|  | Declaration |
| --- | --- |
| From | ``` kauth_cred_t buf_rcred (     buf_t ); ``` |
| To | ``` kauth_cred_t buf_rcred (     buf_t bp ); ``` |

Modified [buf_redundancy_flags()](https://developer.apple.com/documentation/kernel/1561872-buf_redundancy_flags)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_redundancy_flags (     buf_t ); ``` |
| To | ``` uint32_t buf_redundancy_flags (     buf_t bp ); ``` |

Modified [buf_reset()](https://developer.apple.com/documentation/kernel/1561928-buf_reset)

|  | Declaration |
| --- | --- |
| From | ``` void buf_reset (     buf_t,     int32_t ); ``` |
| To | ``` void buf_reset (     buf_t bp,     int32_t flags ); ``` |

Modified [buf_resid()](https://developer.apple.com/documentation/kernel/1561835-buf_resid)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_resid (     buf_t ); ``` |
| To | ``` uint32_t buf_resid (     buf_t bp ); ``` |

Modified [buf_set_redundancy_flags()](https://developer.apple.com/documentation/kernel/1561865-buf_set_redundancy_flags)

|  | Declaration |
| --- | --- |
| From | ``` void buf_set_redundancy_flags (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_set_redundancy_flags (     buf_t bp,     uint32_t flags ); ``` |

Modified [buf_setblkno()](https://developer.apple.com/documentation/kernel/1561888-buf_setblkno)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setblkno (     buf_t,     daddr64_t ); ``` |
| To | ``` void buf_setblkno (     buf_t bp,     daddr64_t blkno ); ``` |

Modified [buf_setcallback()](https://developer.apple.com/documentation/kernel/1561885-buf_setcallback)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_setcallback (     buf_t,     void (*)(buf_t, void *),     void * ); ``` |
| To | ``` errno_t buf_setcallback (     buf_t bp,     void (*callback)(buf_t, void *),     void *transaction ); ``` |

Modified [buf_setcount()](https://developer.apple.com/documentation/kernel/1561852-buf_setcount)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setcount (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_setcount (     buf_t bp,     uint32_t bcount ); ``` |

Modified [buf_setdataptr()](https://developer.apple.com/documentation/kernel/1561861-buf_setdataptr)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setdataptr (     buf_t,     uintptr_t ); ``` |
| To | ``` void buf_setdataptr (     buf_t bp,     uintptr_t data ); ``` |

Modified [buf_setdevice()](https://developer.apple.com/documentation/kernel/1561859-buf_setdevice)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_setdevice (     buf_t,     vnode_t ); ``` |
| To | ``` errno_t buf_setdevice (     buf_t bp,     vnode_t vp ); ``` |

Modified [buf_setdirtyend()](https://developer.apple.com/documentation/kernel/1561826-buf_setdirtyend)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setdirtyend (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_setdirtyend (     buf_t bp,     uint32_t ); ``` |

Modified [buf_setdirtyoff()](https://developer.apple.com/documentation/kernel/1561924-buf_setdirtyoff)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setdirtyoff (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_setdirtyoff (     buf_t bp,     uint32_t ); ``` |

Modified [buf_setdrvdata()](https://developer.apple.com/documentation/kernel/1561880-buf_setdrvdata)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setdrvdata (     buf_t,     void * ); ``` |
| To | ``` void buf_setdrvdata (     buf_t bp,     void *drvdata ); ``` |

Modified [buf_seterror()](https://developer.apple.com/documentation/kernel/1561934-buf_seterror)

|  | Declaration |
| --- | --- |
| From | ``` void buf_seterror (     buf_t,     errno_t ); ``` |
| To | ``` void buf_seterror (     buf_t bp,     errno_t ); ``` |

Modified [buf_setflags()](https://developer.apple.com/documentation/kernel/1561931-buf_setflags)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setflags (     buf_t,     int32_t ); ``` |
| To | ``` void buf_setflags (     buf_t bp,     int32_t flags ); ``` |

Modified [buf_setfsprivate()](https://developer.apple.com/documentation/kernel/1561927-buf_setfsprivate)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setfsprivate (     buf_t,     void * ); ``` |
| To | ``` void buf_setfsprivate (     buf_t bp,     void *fsprivate ); ``` |

Modified [buf_setlblkno()](https://developer.apple.com/documentation/kernel/1561900-buf_setlblkno)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setlblkno (     buf_t,     daddr64_t ); ``` |
| To | ``` void buf_setlblkno (     buf_t bp,     daddr64_t lblkno ); ``` |

Modified [buf_setresid()](https://developer.apple.com/documentation/kernel/1561849-buf_setresid)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setresid (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_setresid (     buf_t bp,     uint32_t resid ); ``` |

Modified [buf_setsize()](https://developer.apple.com/documentation/kernel/1561921-buf_setsize)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setsize (     buf_t,     uint32_t ); ``` |
| To | ``` void buf_setsize (     buf_t bp,     uint32_t ); ``` |

Modified [buf_setupl()](https://developer.apple.com/documentation/kernel/1561846-buf_setupl)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_setupl (     buf_t,     upl_t,     uint32_t ); ``` |
| To | ``` errno_t buf_setupl (     buf_t bp,     upl_t upl,     uint32_t offset ); ``` |

Modified [buf_setvnode()](https://developer.apple.com/documentation/kernel/1561833-buf_setvnode)

|  | Declaration |
| --- | --- |
| From | ``` void buf_setvnode (     buf_t,     vnode_t ); ``` |
| To | ``` void buf_setvnode (     buf_t bp,     vnode_t vp ); ``` |

Modified [buf_size()](https://developer.apple.com/documentation/kernel/1561917-buf_size)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_size (     buf_t ); ``` |
| To | ``` uint32_t buf_size (     buf_t bp ); ``` |

Modified [buf_static()](https://developer.apple.com/documentation/kernel/1561912-buf_static)

|  | Declaration |
| --- | --- |
| From | ``` int buf_static (     buf_t ); ``` |
| To | ``` int buf_static (     buf_t bp ); ``` |

Modified [buf_strategy()](https://developer.apple.com/documentation/kernel/1561893-buf_strategy)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_strategy (     vnode_t,     void * ); ``` |
| To | ``` errno_t buf_strategy (     vnode_t devvp,     void *ap ); ``` |

Modified [buf_unmap()](https://developer.apple.com/documentation/kernel/1561876-buf_unmap)

|  | Declaration |
| --- | --- |
| From | ``` errno_t buf_unmap (     buf_t ); ``` |
| To | ``` errno_t buf_unmap (     buf_t bp ); ``` |

Modified [buf_upl()](https://developer.apple.com/documentation/kernel/1561918-buf_upl)

|  | Declaration |
| --- | --- |
| From | ``` void * buf_upl (     buf_t ); ``` |
| To | ``` void * buf_upl (     buf_t bp ); ``` |

Modified [buf_uploffset()](https://developer.apple.com/documentation/kernel/1561860-buf_uploffset)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t buf_uploffset (     buf_t ); ``` |
| To | ``` uint32_t buf_uploffset (     buf_t bp ); ``` |

Modified [buf_valid()](https://developer.apple.com/documentation/kernel/1561915-buf_valid)

|  | Declaration |
| --- | --- |
| From | ``` int buf_valid (     buf_t ); ``` |
| To | ``` int buf_valid (     buf_t bp ); ``` |

Modified [buf_vnode()](https://developer.apple.com/documentation/kernel/1561919-buf_vnode)

|  | Declaration |
| --- | --- |
| From | ``` vnode_t buf_vnode (     buf_t ); ``` |
| To | ``` vnode_t buf_vnode (     buf_t bp ); ``` |

Modified [buf_wcred()](https://developer.apple.com/documentation/kernel/1561896-buf_wcred)

|  | Declaration |
| --- | --- |
| From | ``` kauth_cred_t buf_wcred (     buf_t ); ``` |
| To | ``` kauth_cred_t buf_wcred (     buf_t bp ); ``` |

Modified [physio()](https://developer.apple.com/documentation/kernel/1561895-physio)

|  | Declaration |
| --- | --- |
| From | ``` int physio (     void (*)(buf_t),     buf_t,     dev_t,     int,     u_int (*)(buf_t),     struct uio *,     int ); ``` |
| To | ``` int physio (     void (*f_strategy)(buf_t),     buf_t bp,     dev_t dev,     int flags,     u_int (*f_minphys)(buf_t),     struct uio *uio,     int blocksize ); ``` |

#### sys/disk.h

Added [dk_provision_extent_t](https://developer.apple.com/documentation/kernel/dk_provision_extent_t)Added [dk_provision_status_t](https://developer.apple.com/documentation/kernel/dk_provision_status_t)Added #def DK_PROVISION_TYPE_ANCHOREDAdded #def DK_PROVISION_TYPE_DEALLOCATEDAdded #def DK_PROVISION_TYPE_MAPPEDAdded #def DKIOCGETIOMINSATURATIONBYTECOUNTAdded #def DKIOCGETPROVISIONSTATUS

#### sys/event.h

Added #def EV_VANISHEDAdded #def EVFILT_EXCEPTAdded #def NOTE_FUNLOCKAdded #def NOTE_MACH_CONTINUOUS_TIMEAdded #def NOTE_OOB

#### sys/fcntl.h

Added #def F_CHECK_LVAdded [fchecklv_t](https://developer.apple.com/documentation/kernel/fchecklv_t)Added [user32_fchecklv_t](https://developer.apple.com/documentation/kernel/user32_fchecklv_t)Added [user_fchecklv_t](https://developer.apple.com/documentation/kernel/user_fchecklv_t)

#### sys/kauth.h

Added kauth_cred_dsnode2nfs4domain()Added kauth_cred_nfs4domain2dsnode()

#### sys/kdebug.h

Removed #def DBG_APP_SIGPOSTRemoved #def DBG_DYLD_STRINGAdded #def BSD_PROC_EXECAdded #def BSD_PROC_EXITREASON_COMMITAdded #def BSD_PROC_EXITREASON_CREATEAdded #def DBG_APFSAdded #def DBG_APP_DFRAdded #def DBG_APP_SIGNPOSTAdded #def DBG_APP_SYSTEMUIAdded #def DBG_BSD_KDEBUG_TESTAdded #def DBG_DISPATCHAdded #def DBG_DRVWLAN_802_11Added #def DBG_DYLD_UUIDAdded #def DBG_DYLD_UUID_MAP_32_AAdded #def DBG_DYLD_UUID_MAP_32_BAdded #def DBG_DYLD_UUID_MAP_32_CAdded #def DBG_DYLD_UUID_MAP_AAdded #def DBG_DYLD_UUID_MAP_BAdded #def DBG_DYLD_UUID_SHARED_CACHE_32_AAdded #def DBG_DYLD_UUID_SHARED_CACHE_32_BAdded #def DBG_DYLD_UUID_SHARED_CACHE_32_CAdded #def DBG_DYLD_UUID_SHARED_CACHE_AAdded #def DBG_DYLD_UUID_SHARED_CACHE_BAdded #def DBG_DYLD_UUID_UNMAP_32_AAdded #def DBG_DYLD_UUID_UNMAP_32_BAdded #def DBG_DYLD_UUID_UNMAP_32_CAdded #def DBG_DYLD_UUID_UNMAP_AAdded #def DBG_DYLD_UUID_UNMAP_BAdded #def DBG_MACH_RESOURCEAdded #def DBG_MACH_SIGNPOSTAdded #def DBG_MACH_WORKINGSETAdded #def DBG_SMBAdded #def DBG_UMALLOCAdded #def DBG_UMALLOC_EXTERNALAdded #def DBG_UMALLOC_INTERNALAdded #def KDBG_CSC_MAXAdded #def KDBG_FUNC_MASKAdded #def KDBG_IMPROBABLEAdded #def KDEBUG_COMMPAGE_ENABLE_TRACEAdded #def KDEBUG_COMMPAGE_ENABLE_TYPEFILTERAdded #def KERNEL_DEBUG_CONSTANT_DEBUGAdded #def KERNEL_DEBUG_CONSTANT_FILTEREDAdded #def KERNEL_DEBUG_CONSTANT_RELEASEAdded [kernel_debug_filtered()](https://developer.apple.com/documentation/kernel/2123006-kernel_debug_filtered)Added #def MACH_IPC_KMSG_INFOAdded #def MACH_IPC_KMSG_LINKAdded #def RMON_CPUUSAGE_RESUMEDAdded #def RMON_CPUUSAGE_SUSPENDEDAdded #def RMON_CPUUSAGE_VIOLATEDAdded #def RMON_CPUUSAGE_VIOLATED_K32AAdded #def RMON_CPUUSAGE_VIOLATED_K32BAdded #def RMON_CPUWAKES_VIOLATEDAdded #def RMON_CPUWAKES_VIOLATED_K32AAdded #def RMON_CPUWAKES_VIOLATED_K32BAdded #def RMON_DISABLE_CPUUSAGE_MONITORAdded #def RMON_DISABLE_CPUWAKES_MONITORAdded #def RMON_DISABLE_IO_MONITORAdded #def RMON_ENABLE_CPUUSAGE_MONITORAdded #def RMON_ENABLE_CPUWAKES_MONITORAdded #def RMON_ENABLE_IO_MONITORAdded #def RMON_LOGWRITES_VIOLATEDAdded #def RMON_LOGWRITES_VIOLATED_K32AAdded #def RMON_LOGWRITES_VIOLATED_K32BAdded #def RMON_PHYSWRITES_VIOLATEDAdded #def TRACE_DATA_THREAD_TERMINATE_PIDAdded #def TRACE_STRING_PROC_EXITAdded #def TRACE_STRING_THREADNAMEAdded #def TRACE_STRING_THREADNAME_PREV

#### sys/kpi_socketfilter.h

Modified [sflt_attach()](https://developer.apple.com/documentation/kernel/1433214-sflt_attach)

|  | Declaration |
| --- | --- |
| From | ``` errno_t sflt_attach (     socket_t so,     sflt_handle ); ``` |
| To | ``` errno_t sflt_attach (     socket_t socket,     sflt_handle handle ); ``` |

Modified [sflt_detach()](https://developer.apple.com/documentation/kernel/1433247-sflt_detach)

|  | Declaration |
| --- | --- |
| From | ``` errno_t sflt_detach (     socket_t so,     sflt_handle ); ``` |
| To | ``` errno_t sflt_detach (     socket_t socket,     sflt_handle handle ); ``` |

#### sys/malloc.h

Removed #def M_HFSMNT

#### sys/mount.h

Added [fs_snapshot_mount_args](https://developer.apple.com/documentation/kernel/fs_snapshot_mount_args)Added [fs_snapshot_revert_args](https://developer.apple.com/documentation/kernel/fs_snapshot_revert_args)Added #def VFS_IOATTR_FLAGS_SWAPPIN_SUPPORTEDAdded #def VFS_TBLCANMOUNTROOTAdded #def VFS_TBLVNOP_SECLUDE_RENAMEAdded #def VFSCTL_MOUNT_SNAPSHOTAdded #def VFSCTL_REVERT_SNAPSHOTAdded #def VFSIOC_MOUNT_SNAPSHOTAdded #def VFSIOC_REVERT_SNAPSHOTModified [vfs_64bitready()](https://developer.apple.com/documentation/kernel/1523312-vfs_64bitready)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_64bitready (     mount_t ); ``` |
| To | ``` int vfs_64bitready (     mount_t mp ); ``` |

Modified [vfs_authcache_ttl()](https://developer.apple.com/documentation/kernel/1523180-vfs_authcache_ttl)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_authcache_ttl (     mount_t ); ``` |
| To | ``` int vfs_authcache_ttl (     mount_t mp ); ``` |

Modified [vfs_authopaque()](https://developer.apple.com/documentation/kernel/1523276-vfs_authopaque)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_authopaque (     mount_t ); ``` |
| To | ``` int vfs_authopaque (     mount_t mp ); ``` |

Modified [vfs_authopaqueaccess()](https://developer.apple.com/documentation/kernel/1523247-vfs_authopaqueaccess)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_authopaqueaccess (     mount_t ); ``` |
| To | ``` int vfs_authopaqueaccess (     mount_t mp ); ``` |

Modified [vfs_busy()](https://developer.apple.com/documentation/kernel/1523389-vfs_busy)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_busy (     mount_t,     int ); ``` |
| To | ``` int vfs_busy (     mount_t mp,     int flags ); ``` |

Modified [vfs_clearauthcache_ttl()](https://developer.apple.com/documentation/kernel/1523469-vfs_clearauthcache_ttl)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_clearauthcache_ttl (     mount_t ); ``` |
| To | ``` void vfs_clearauthcache_ttl (     mount_t mp ); ``` |

Modified [vfs_clearauthopaque()](https://developer.apple.com/documentation/kernel/1523223-vfs_clearauthopaque)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_clearauthopaque (     mount_t ); ``` |
| To | ``` void vfs_clearauthopaque (     mount_t mp ); ``` |

Modified [vfs_clearauthopaqueaccess()](https://developer.apple.com/documentation/kernel/1523231-vfs_clearauthopaqueaccess)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_clearauthopaqueaccess (     mount_t ); ``` |
| To | ``` void vfs_clearauthopaqueaccess (     mount_t mp ); ``` |

Modified [vfs_clearextendedsecurity()](https://developer.apple.com/documentation/kernel/1523368-vfs_clearextendedsecurity)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_clearextendedsecurity (     mount_t ); ``` |
| To | ``` void vfs_clearextendedsecurity (     mount_t mp ); ``` |

Modified [vfs_clearflags()](https://developer.apple.com/documentation/kernel/1523299-vfs_clearflags)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_clearflags (     mount_t,     uint64_t ); ``` |
| To | ``` void vfs_clearflags (     mount_t mp,     uint64_t flags ); ``` |

Modified [vfs_devblocksize()](https://developer.apple.com/documentation/kernel/1523172-vfs_devblocksize)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_devblocksize (     mount_t ); ``` |
| To | ``` int vfs_devblocksize (     mount_t mp ); ``` |

Modified [vfs_event_signal()](https://developer.apple.com/documentation/kernel/1523107-vfs_event_signal)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_event_signal (     fsid_t *,     u_int32_t,     intptr_t ); ``` |
| To | ``` void vfs_event_signal (     fsid_t *fsid,     u_int32_t event,     intptr_t data ); ``` |

Modified [vfs_flags()](https://developer.apple.com/documentation/kernel/1523261-vfs_flags)

|  | Declaration |
| --- | --- |
| From | ``` uint64_t vfs_flags (     mount_t ); ``` |
| To | ``` uint64_t vfs_flags (     mount_t mp ); ``` |

Modified [vfs_fsadd()](https://developer.apple.com/documentation/kernel/1523490-vfs_fsadd)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_fsadd (     struct vfs_fsentry *,     vfstable_t * ); ``` |
| To | ``` int vfs_fsadd (     struct vfs_fsentry *vfe,     vfstable_t *handle ); ``` |

Modified [vfs_fsprivate()](https://developer.apple.com/documentation/kernel/1523301-vfs_fsprivate)

|  | Declaration |
| --- | --- |
| From | ``` void * vfs_fsprivate (     mount_t ); ``` |
| To | ``` void * vfs_fsprivate (     mount_t mp ); ``` |

Modified [vfs_fsremove()](https://developer.apple.com/documentation/kernel/1523194-vfs_fsremove)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_fsremove (     vfstable_t ); ``` |
| To | ``` int vfs_fsremove (     vfstable_t handle ); ``` |

Modified [vfs_getnewfsid()](https://developer.apple.com/documentation/kernel/1523259-vfs_getnewfsid)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_getnewfsid (     struct mount * ); ``` |
| To | ``` void vfs_getnewfsid (     struct mount *mp ); ``` |

Modified [vfs_getvfs()](https://developer.apple.com/documentation/kernel/1523465-vfs_getvfs)

|  | Declaration |
| --- | --- |
| From | ``` mount_t vfs_getvfs (     fsid_t * ); ``` |
| To | ``` mount_t vfs_getvfs (     fsid_t *fsid ); ``` |

Modified [vfs_init_io_attributes()](https://developer.apple.com/documentation/kernel/1523109-vfs_init_io_attributes)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_init_io_attributes (     vnode_t,     mount_t ); ``` |
| To | ``` int vfs_init_io_attributes (     vnode_t devvp,     mount_t mp ); ``` |

Modified [vfs_ioattr()](https://developer.apple.com/documentation/kernel/1523411-vfs_ioattr)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_ioattr (     mount_t,     struct vfsioattr * ); ``` |
| To | ``` void vfs_ioattr (     mount_t mp,     struct vfsioattr *ioattrp ); ``` |

Modified [vfs_isforce()](https://developer.apple.com/documentation/kernel/1523525-vfs_isforce)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_isforce (     mount_t ); ``` |
| To | ``` int vfs_isforce (     mount_t mp ); ``` |

Modified [vfs_isrdonly()](https://developer.apple.com/documentation/kernel/1523242-vfs_isrdonly)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_isrdonly (     mount_t ); ``` |
| To | ``` int vfs_isrdonly (     mount_t mp ); ``` |

Modified [vfs_isrdwr()](https://developer.apple.com/documentation/kernel/1523454-vfs_isrdwr)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_isrdwr (     mount_t ); ``` |
| To | ``` int vfs_isrdwr (     mount_t mp ); ``` |

Modified [vfs_isreload()](https://developer.apple.com/documentation/kernel/1523537-vfs_isreload)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_isreload (     mount_t ); ``` |
| To | ``` int vfs_isreload (     mount_t mp ); ``` |

Modified [vfs_issynchronous()](https://developer.apple.com/documentation/kernel/1523327-vfs_issynchronous)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_issynchronous (     mount_t ); ``` |
| To | ``` int vfs_issynchronous (     mount_t mp ); ``` |

Modified [vfs_isupdate()](https://developer.apple.com/documentation/kernel/1523536-vfs_isupdate)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_isupdate (     mount_t ); ``` |
| To | ``` int vfs_isupdate (     mount_t mp ); ``` |

Modified [vfs_iswriteupgrade()](https://developer.apple.com/documentation/kernel/1523486-vfs_iswriteupgrade)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_iswriteupgrade (     mount_t ); ``` |
| To | ``` int vfs_iswriteupgrade (     mount_t mp ); ``` |

Modified [vfs_iterate()](https://developer.apple.com/documentation/kernel/1523233-vfs_iterate)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_iterate (     int,     int (*)(struct mount *, void *),     void * ); ``` |
| To | ``` int vfs_iterate (     int flags,     int (*callout)(struct mount *, void *),     void *arg ); ``` |

Modified [vfs_maxsymlen()](https://developer.apple.com/documentation/kernel/1523507-vfs_maxsymlen)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t vfs_maxsymlen (     mount_t ); ``` |
| To | ``` uint32_t vfs_maxsymlen (     mount_t mp ); ``` |

Modified [vfs_mountedon()](https://developer.apple.com/documentation/kernel/1523197-vfs_mountedon)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_mountedon (     struct vnode * ); ``` |
| To | ``` int vfs_mountedon (     struct vnode *vp ); ``` |

Modified [vfs_name()](https://developer.apple.com/documentation/kernel/1523128-vfs_name)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_name (     mount_t,     char * ); ``` |
| To | ``` void vfs_name (     mount_t mp,     char *buffer ); ``` |

Modified [vfs_setauthcache_ttl()](https://developer.apple.com/documentation/kernel/1523286-vfs_setauthcache_ttl)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setauthcache_ttl (     mount_t,     int ); ``` |
| To | ``` void vfs_setauthcache_ttl (     mount_t mp,     int ttl ); ``` |

Modified [vfs_setauthopaque()](https://developer.apple.com/documentation/kernel/1523440-vfs_setauthopaque)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setauthopaque (     mount_t ); ``` |
| To | ``` void vfs_setauthopaque (     mount_t mp ); ``` |

Modified [vfs_setauthopaqueaccess()](https://developer.apple.com/documentation/kernel/1523218-vfs_setauthopaqueaccess)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setauthopaqueaccess (     mount_t ); ``` |
| To | ``` void vfs_setauthopaqueaccess (     mount_t mp ); ``` |

Modified [vfs_setextendedsecurity()](https://developer.apple.com/documentation/kernel/1523360-vfs_setextendedsecurity)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setextendedsecurity (     mount_t ); ``` |
| To | ``` void vfs_setextendedsecurity (     mount_t mp ); ``` |

Modified [vfs_setflags()](https://developer.apple.com/documentation/kernel/1523521-vfs_setflags)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setflags (     mount_t,     uint64_t ); ``` |
| To | ``` void vfs_setflags (     mount_t mp,     uint64_t flags ); ``` |

Modified [vfs_setfsprivate()](https://developer.apple.com/documentation/kernel/1523413-vfs_setfsprivate)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setfsprivate (     mount_t,     void *mntdata ); ``` |
| To | ``` void vfs_setfsprivate (     mount_t mp,     void *mntdata ); ``` |

Modified [vfs_setioattr()](https://developer.apple.com/documentation/kernel/1523458-vfs_setioattr)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setioattr (     mount_t,     struct vfsioattr * ); ``` |
| To | ``` void vfs_setioattr (     mount_t mp,     struct vfsioattr *ioattrp ); ``` |

Modified [vfs_setlocklocal()](https://developer.apple.com/documentation/kernel/1523104-vfs_setlocklocal)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setlocklocal (     mount_t ); ``` |
| To | ``` void vfs_setlocklocal (     mount_t mp ); ``` |

Modified [vfs_setmaxsymlen()](https://developer.apple.com/documentation/kernel/1523316-vfs_setmaxsymlen)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_setmaxsymlen (     mount_t,     uint32_t ); ``` |
| To | ``` void vfs_setmaxsymlen (     mount_t mp,     uint32_t symlen ); ``` |

Modified [vfs_statfs()](https://developer.apple.com/documentation/kernel/1523098-vfs_statfs)

|  | Declaration |
| --- | --- |
| From | ``` struct vfsstatfs * vfs_statfs (     mount_t ); ``` |
| To | ``` struct vfsstatfs * vfs_statfs (     mount_t mp ); ``` |

Modified [vfs_typenum()](https://developer.apple.com/documentation/kernel/1523418-vfs_typenum)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_typenum (     mount_t ); ``` |
| To | ``` int vfs_typenum (     mount_t mp ); ``` |

Modified [vfs_unbusy()](https://developer.apple.com/documentation/kernel/1523451-vfs_unbusy)

|  | Declaration |
| --- | --- |
| From | ``` void vfs_unbusy (     mount_t ); ``` |
| To | ``` void vfs_unbusy (     mount_t mp ); ``` |

Modified [vfs_unmountbyfsid()](https://developer.apple.com/documentation/kernel/1523503-vfs_unmountbyfsid)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_unmountbyfsid (     fsid_t *,     int,     vfs_context_t ); ``` |
| To | ``` int vfs_unmountbyfsid (     fsid_t *fsid,     int flags,     vfs_context_t ctx ); ``` |

Modified [vfs_update_vfsstat()](https://developer.apple.com/documentation/kernel/1523278-vfs_update_vfsstat)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_update_vfsstat (     mount_t,     vfs_context_t,     int eventtype ); ``` |
| To | ``` int vfs_update_vfsstat (     mount_t mp,     vfs_context_t ctx,     int eventtype ); ``` |

#### sys/proc.h

Modified [proc_pgrpid()](https://developer.apple.com/documentation/kernel/1488969-proc_pgrpid)

|  | Declaration |
| --- | --- |
| From | ``` pid_t proc_pgrpid (     proc_t ); ``` |
| To | ``` pid_t proc_pgrpid (     proc_t p ); ``` |

#### sys/socket.h

Added #def NET_SERVICE_TYPE_AVAdded #def NET_SERVICE_TYPE_BEAdded #def NET_SERVICE_TYPE_BKAdded #def NET_SERVICE_TYPE_OAMAdded #def NET_SERVICE_TYPE_RDAdded #def NET_SERVICE_TYPE_RVAdded #def NET_SERVICE_TYPE_SIGAdded #def NET_SERVICE_TYPE_VIAdded #def NET_SERVICE_TYPE_VOAdded #def NETSVC_MRKNG_LVL_L2Added #def NETSVC_MRKNG_LVL_L3L2_ALLAdded #def NETSVC_MRKNG_LVL_L3L2_BKAdded #def NETSVC_MRKNG_UNKNOWNAdded #def SO_NET_SERVICE_TYPEAdded #def SO_NETSVC_MARKING_LEVEL

#### sys/syscall.h

Removed #def SYS_chudRemoved #def SYS_rename_extRemoved #def SYS_stack_snapshotAdded #def SYS___channel_get_infoAdded #def SYS___channel_get_optAdded #def SYS___channel_openAdded #def SYS___channel_set_optAdded #def SYS___channel_syncAdded #def SYS___nexus_createAdded #def SYS___nexus_deregisterAdded #def SYS___nexus_destroyAdded #def SYS___nexus_get_optAdded #def SYS___nexus_openAdded #def SYS___nexus_registerAdded #def SYS___nexus_set_optAdded #def SYS_abort_with_payloadAdded #def SYS_clonefileatAdded #def SYS_fclonefileatAdded #def SYS_fs_snapshotAdded #def SYS_getentropyAdded #def SYS_invalidAdded #def SYS_kdebug_typefilterAdded #def SYS_necp_client_actionAdded #def SYS_necp_openAdded #def SYS_renameatx_npAdded #def SYS_terminate_with_payloadAdded #def SYS_ulock_waitAdded #def SYS_ulock_wake

#### sys/sysctl.h

Modified [sysctl_register_fixed()](https://developer.apple.com/documentation/kernel/1404259-sysctl_register_fixed)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### sys/vnode.h

Added #def VA_64BITOBJIDSAdded [VT_APFS](https://developer.apple.com/documentation/kernel/vtagtype/vt_apfs)Modified [vfs_attr_pack()](https://developer.apple.com/documentation/kernel/1562242-vfs_attr_pack)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vfs_attr_pack (     vnode_t,     uio_t,     struct attrlist *,     uint64_t,     struct vnode_attr *,     void *,     vfs_context_t ); ``` |
| To | ``` errno_t vfs_attr_pack (     vnode_t vp,     uio_t uio,     struct attrlist *alp,     uint64_t options,     struct vnode_attr *vap,     void *fndesc,     vfs_context_t ctx ); ``` |

Modified [vfs_context_create()](https://developer.apple.com/documentation/kernel/1562360-vfs_context_create)

|  | Declaration |
| --- | --- |
| From | ``` vfs_context_t vfs_context_create (     vfs_context_t ); ``` |
| To | ``` vfs_context_t vfs_context_create (     vfs_context_t ctx ); ``` |

Modified [vfs_context_is64bit()](https://developer.apple.com/documentation/kernel/1562122-vfs_context_is64bit)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_context_is64bit (     vfs_context_t ); ``` |
| To | ``` int vfs_context_is64bit (     vfs_context_t ctx ); ``` |

Modified [vfs_context_issignal()](https://developer.apple.com/documentation/kernel/1562448-vfs_context_issignal)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_context_issignal (     vfs_context_t,     sigset_t ); ``` |
| To | ``` int vfs_context_issignal (     vfs_context_t ctx,     sigset_t mask ); ``` |

Modified [vfs_context_pid()](https://developer.apple.com/documentation/kernel/1562461-vfs_context_pid)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_context_pid (     vfs_context_t ); ``` |
| To | ``` int vfs_context_pid (     vfs_context_t ctx ); ``` |

Modified [vfs_context_proc()](https://developer.apple.com/documentation/kernel/1562390-vfs_context_proc)

|  | Declaration |
| --- | --- |
| From | ``` proc_t vfs_context_proc (     vfs_context_t ); ``` |
| To | ``` proc_t vfs_context_proc (     vfs_context_t ctx ); ``` |

Modified [vfs_context_rele()](https://developer.apple.com/documentation/kernel/1562367-vfs_context_rele)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_context_rele (     vfs_context_t ); ``` |
| To | ``` int vfs_context_rele (     vfs_context_t ctx ); ``` |

Modified [vfs_context_suser()](https://developer.apple.com/documentation/kernel/1562261-vfs_context_suser)

|  | Declaration |
| --- | --- |
| From | ``` int vfs_context_suser (     vfs_context_t ); ``` |
| To | ``` int vfs_context_suser (     vfs_context_t ctx ); ``` |

Modified [vfs_context_ucred()](https://developer.apple.com/documentation/kernel/1562308-vfs_context_ucred)

|  | Declaration |
| --- | --- |
| From | ``` kauth_cred_t vfs_context_ucred (     vfs_context_t ); ``` |
| To | ``` kauth_cred_t vfs_context_ucred (     vfs_context_t ctx ); ``` |

Modified [vfs_setup_vattr_from_attrlist()](https://developer.apple.com/documentation/kernel/1562135-vfs_setup_vattr_from_attrlist)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vfs_setup_vattr_from_attrlist (     struct attrlist *,     struct vnode_attr *,     enum vtype,     ssize_t *,     vfs_context_t ); ``` |
| To | ``` errno_t vfs_setup_vattr_from_attrlist (     struct attrlist *alp,     struct vnode_attr *vap,     enum vtype obj_vtype,     ssize_t *attr_fixed_sizep,     vfs_context_t ctx ); ``` |

Modified [vn_rdwr()](https://developer.apple.com/documentation/kernel/1562098-vn_rdwr)

|  | Declaration |
| --- | --- |
| From | ``` int vn_rdwr (     enum uio_rw,     vnode_t,     caddr_t,     int,     off_t,     enum uio_seg,     int,     kauth_cred_t,     int *,     proc_t ); ``` |
| To | ``` int vn_rdwr (     enum uio_rw rw,     struct vnode *vp,     caddr_t base,     int len,     off_t offset,     enum uio_seg segflg,     int ioflg,     kauth_cred_t cred,     int *aresid,     proc_t p ); ``` |

Modified [vn_revoke()](https://developer.apple.com/documentation/kernel/1562348-vn_revoke)

|  | Declaration |
| --- | --- |
| From | ``` int vn_revoke (     vnode_t vp,     int flags,     vfs_context_t ); ``` |
| To | ``` int vn_revoke (     vnode_t vp,     int flags,     vfs_context_t ctx ); ``` |

Modified [vnode_addfsref()](https://developer.apple.com/documentation/kernel/1562216-vnode_addfsref)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_addfsref (     vnode_t ); ``` |
| To | ``` int vnode_addfsref (     vnode_t vp ); ``` |

Modified [vnode_authattr()](https://developer.apple.com/documentation/kernel/1562106-vnode_authattr)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_authattr (     vnode_t,     struct vnode_attr *,     kauth_action_t *,     vfs_context_t ); ``` |
| To | ``` int vnode_authattr (     vnode_t vp,     struct vnode_attr *vap,     kauth_action_t *actionp,     vfs_context_t ctx ); ``` |

Modified [vnode_authattr_new()](https://developer.apple.com/documentation/kernel/1562184-vnode_authattr_new)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_authattr_new (     vnode_t,     struct vnode_attr *,     int,     vfs_context_t ); ``` |
| To | ``` int vnode_authattr_new (     vnode_t dvp,     struct vnode_attr *vap,     int noauth,     vfs_context_t ctx ); ``` |

Modified [vnode_authorize()](https://developer.apple.com/documentation/kernel/1562084-vnode_authorize)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_authorize (     vnode_t,     vnode_t,     kauth_action_t,     vfs_context_t ); ``` |
| To | ``` int vnode_authorize (     vnode_t vp,     vnode_t dvp,     kauth_action_t action,     vfs_context_t ctx ); ``` |

Modified [vnode_clearautocandidate()](https://developer.apple.com/documentation/kernel/1562373-vnode_clearautocandidate)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearautocandidate (     vnode_t ); ``` |
| To | ``` void vnode_clearautocandidate (     vnode_t vp ); ``` |

Modified [vnode_cleardirty()](https://developer.apple.com/documentation/kernel/1562294-vnode_cleardirty)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_cleardirty (     vnode_t ); ``` |
| To | ``` int vnode_cleardirty (     vnode_t vp ); ``` |

Modified [vnode_clearfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562403-vnode_clearfastdevicecandidate)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearfastdevicecandidate (     vnode_t ); ``` |
| To | ``` void vnode_clearfastdevicecandidate (     vnode_t vp ); ``` |

Modified [vnode_clearfsnode()](https://developer.apple.com/documentation/kernel/1562353-vnode_clearfsnode)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearfsnode (     vnode_t ); ``` |
| To | ``` void vnode_clearfsnode (     vnode_t vp ); ``` |

Modified [vnode_clearmountedon()](https://developer.apple.com/documentation/kernel/1562415-vnode_clearmountedon)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearmountedon (     vnode_t ); ``` |
| To | ``` void vnode_clearmountedon (     vnode_t vp ); ``` |

Modified [vnode_clearnocache()](https://developer.apple.com/documentation/kernel/1562430-vnode_clearnocache)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearnocache (     vnode_t ); ``` |
| To | ``` void vnode_clearnocache (     vnode_t vp ); ``` |

Modified [vnode_clearnoreadahead()](https://developer.apple.com/documentation/kernel/1562228-vnode_clearnoreadahead)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_clearnoreadahead (     vnode_t ); ``` |
| To | ``` void vnode_clearnoreadahead (     vnode_t vp ); ``` |

Modified [vnode_close()](https://developer.apple.com/documentation/kernel/1562091-vnode_close)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vnode_close (     vnode_t,     int,     vfs_context_t ); ``` |
| To | ``` errno_t vnode_close (     vnode_t vp,     int flags,     vfs_context_t ctx ); ``` |

Modified [vnode_create()](https://developer.apple.com/documentation/kernel/1562117-vnode_create)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vnode_create (     uint32_t,     uint32_t,     void *,     vnode_t * ); ``` |
| To | ``` errno_t vnode_create (     uint32_t flavor,     uint32_t size,     void *data,     vnode_t *vpp ); ``` |

Modified [vnode_fsnode()](https://developer.apple.com/documentation/kernel/1562316-vnode_fsnode)

|  | Declaration |
| --- | --- |
| From | ``` void * vnode_fsnode (     vnode_t ); ``` |
| To | ``` void * vnode_fsnode (     vnode_t vp ); ``` |

Modified [vnode_getwithref()](https://developer.apple.com/documentation/kernel/1562306-vnode_getwithref)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_getwithref (     vnode_t ); ``` |
| To | ``` int vnode_getwithref (     vnode_t vp ); ``` |

Modified [vnode_hascleanblks()](https://developer.apple.com/documentation/kernel/1562371-vnode_hascleanblks)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_hascleanblks (     vnode_t ); ``` |
| To | ``` int vnode_hascleanblks (     vnode_t vp ); ``` |

Modified [vnode_hasdirtyblks()](https://developer.apple.com/documentation/kernel/1562463-vnode_hasdirtyblks)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_hasdirtyblks (     vnode_t ); ``` |
| To | ``` int vnode_hasdirtyblks (     vnode_t vp ); ``` |

Modified [vnode_isautocandidate()](https://developer.apple.com/documentation/kernel/1562339-vnode_isautocandidate)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isautocandidate (     vnode_t ); ``` |
| To | ``` int vnode_isautocandidate (     vnode_t vp ); ``` |

Modified [vnode_isblk()](https://developer.apple.com/documentation/kernel/1562233-vnode_isblk)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isblk (     vnode_t ); ``` |
| To | ``` int vnode_isblk (     vnode_t vp ); ``` |

Modified [vnode_ischr()](https://developer.apple.com/documentation/kernel/1562401-vnode_ischr)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_ischr (     vnode_t ); ``` |
| To | ``` int vnode_ischr (     vnode_t vp ); ``` |

Modified [vnode_isdir()](https://developer.apple.com/documentation/kernel/1562276-vnode_isdir)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isdir (     vnode_t ); ``` |
| To | ``` int vnode_isdir (     vnode_t vp ); ``` |

Modified [vnode_isdirty()](https://developer.apple.com/documentation/kernel/1562357-vnode_isdirty)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isdirty (     vnode_t ); ``` |
| To | ``` int vnode_isdirty (     vnode_t vp ); ``` |

Modified [vnode_isfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562391-vnode_isfastdevicecandidate)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isfastdevicecandidate (     vnode_t ); ``` |
| To | ``` int vnode_isfastdevicecandidate (     vnode_t vp ); ``` |

Modified [vnode_isfifo()](https://developer.apple.com/documentation/kernel/1562153-vnode_isfifo)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isfifo (     vnode_t ); ``` |
| To | ``` int vnode_isfifo (     vnode_t vp ); ``` |

Modified [vnode_isinuse()](https://developer.apple.com/documentation/kernel/1562179-vnode_isinuse)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isinuse (     vnode_t,     int ); ``` |
| To | ``` int vnode_isinuse (     vnode_t vp,     int refcnt ); ``` |

Modified [vnode_islnk()](https://developer.apple.com/documentation/kernel/1562202-vnode_islnk)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_islnk (     vnode_t ); ``` |
| To | ``` int vnode_islnk (     vnode_t vp ); ``` |

Modified [vnode_ismount()](https://developer.apple.com/documentation/kernel/1562400-vnode_ismount)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_ismount (     vnode_t ); ``` |
| To | ``` int vnode_ismount (     vnode_t vp ); ``` |

Modified [vnode_ismountedon()](https://developer.apple.com/documentation/kernel/1562452-vnode_ismountedon)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_ismountedon (     vnode_t ); ``` |
| To | ``` int vnode_ismountedon (     vnode_t vp ); ``` |

Modified [vnode_isnamedstream()](https://developer.apple.com/documentation/kernel/1562161-vnode_isnamedstream)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isnamedstream (     vnode_t ); ``` |
| To | ``` int vnode_isnamedstream (     vnode_t vp ); ``` |

Modified [vnode_isnocache()](https://developer.apple.com/documentation/kernel/1562192-vnode_isnocache)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isnocache (     vnode_t ); ``` |
| To | ``` int vnode_isnocache (     vnode_t vp ); ``` |

Modified [vnode_isnoreadahead()](https://developer.apple.com/documentation/kernel/1562307-vnode_isnoreadahead)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isnoreadahead (     vnode_t ); ``` |
| To | ``` int vnode_isnoreadahead (     vnode_t vp ); ``` |

Modified [vnode_israge()](https://developer.apple.com/documentation/kernel/1562229-vnode_israge)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_israge (     vnode_t ); ``` |
| To | ``` int vnode_israge (     vnode_t vp ); ``` |

Modified [vnode_isrecycled()](https://developer.apple.com/documentation/kernel/1562214-vnode_isrecycled)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isrecycled (     vnode_t ); ``` |
| To | ``` int vnode_isrecycled (     vnode_t vp ); ``` |

Modified [vnode_isreg()](https://developer.apple.com/documentation/kernel/1562441-vnode_isreg)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isreg (     vnode_t ); ``` |
| To | ``` int vnode_isreg (     vnode_t vp ); ``` |

Modified [vnode_issystem()](https://developer.apple.com/documentation/kernel/1562350-vnode_issystem)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_issystem (     vnode_t ); ``` |
| To | ``` int vnode_issystem (     vnode_t vp ); ``` |

Modified [vnode_isvroot()](https://developer.apple.com/documentation/kernel/1562236-vnode_isvroot)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_isvroot (     vnode_t ); ``` |
| To | ``` int vnode_isvroot (     vnode_t vp ); ``` |

Modified [vnode_iterate()](https://developer.apple.com/documentation/kernel/1562464-vnode_iterate)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_iterate (     struct mount *,     int,     int (*)(struct vnode *, void *),     void * ); ``` |
| To | ``` int vnode_iterate (     struct mount *mp,     int flags,     int (*callout)(struct vnode *, void *),     void *arg ); ``` |

Modified [vnode_lookup()](https://developer.apple.com/documentation/kernel/1562245-vnode_lookup)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vnode_lookup (     const char *,     int,     vnode_t *,     vfs_context_t ); ``` |
| To | ``` errno_t vnode_lookup (     const char *path,     int flags,     vnode_t *vpp,     vfs_context_t ctx ); ``` |

Modified [vnode_mount()](https://developer.apple.com/documentation/kernel/1562358-vnode_mount)

|  | Declaration |
| --- | --- |
| From | ``` mount_t vnode_mount (     vnode_t ); ``` |
| To | ``` mount_t vnode_mount (     vnode_t vp ); ``` |

Modified [vnode_needssnapshots()](https://developer.apple.com/documentation/kernel/1562160-vnode_needssnapshots)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_needssnapshots (     vnode_t ); ``` |
| To | ``` int vnode_needssnapshots (     vnode_t vp ); ``` |

Modified [vnode_notify()](https://developer.apple.com/documentation/kernel/1562393-vnode_notify)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_notify (     vnode_t,     uint32_t,     struct vnode_attr * ); ``` |
| To | ``` int vnode_notify (     vnode_t vp,     uint32_t events,     struct vnode_attr *vap ); ``` |

Modified [vnode_open()](https://developer.apple.com/documentation/kernel/1562149-vnode_open)

|  | Declaration |
| --- | --- |
| From | ``` errno_t vnode_open (     const char *,     int,     int,     int,     vnode_t *,     vfs_context_t ); ``` |
| To | ``` errno_t vnode_open (     const char *path,     int fmode,     int cmode,     int flags,     vnode_t *vpp,     vfs_context_t ctx ); ``` |

Modified [vnode_put()](https://developer.apple.com/documentation/kernel/1562280-vnode_put)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_put (     vnode_t ); ``` |
| To | ``` int vnode_put (     vnode_t vp ); ``` |

Modified [vnode_recycle()](https://developer.apple.com/documentation/kernel/1562237-vnode_recycle)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_recycle (     vnode_t ); ``` |
| To | ``` int vnode_recycle (     vnode_t vp ); ``` |

Modified [vnode_ref()](https://developer.apple.com/documentation/kernel/1562240-vnode_ref)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_ref (     vnode_t ); ``` |
| To | ``` int vnode_ref (     vnode_t vp ); ``` |

Modified [vnode_rele()](https://developer.apple.com/documentation/kernel/1562121-vnode_rele)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_rele (     vnode_t ); ``` |
| To | ``` void vnode_rele (     vnode_t vp ); ``` |

Modified [vnode_removefsref()](https://developer.apple.com/documentation/kernel/1562210-vnode_removefsref)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_removefsref (     vnode_t ); ``` |
| To | ``` int vnode_removefsref (     vnode_t vp ); ``` |

Modified [vnode_setautocandidate()](https://developer.apple.com/documentation/kernel/1562116-vnode_setautocandidate)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_setautocandidate (     vnode_t ); ``` |
| To | ``` void vnode_setautocandidate (     vnode_t vp ); ``` |

Modified [vnode_setdirty()](https://developer.apple.com/documentation/kernel/1562289-vnode_setdirty)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_setdirty (     vnode_t ); ``` |
| To | ``` int vnode_setdirty (     vnode_t vp ); ``` |

Modified [vnode_setfastdevicecandidate()](https://developer.apple.com/documentation/kernel/1562221-vnode_setfastdevicecandidate)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_setfastdevicecandidate (     vnode_t ); ``` |
| To | ``` void vnode_setfastdevicecandidate (     vnode_t vp ); ``` |

Modified [vnode_setmountedon()](https://developer.apple.com/documentation/kernel/1562370-vnode_setmountedon)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_setmountedon (     vnode_t ); ``` |
| To | ``` void vnode_setmountedon (     vnode_t vp ); ``` |

Modified [vnode_setnocache()](https://developer.apple.com/documentation/kernel/1562318-vnode_setnocache)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_setnocache (     vnode_t ); ``` |
| To | ``` void vnode_setnocache (     vnode_t vp ); ``` |

Modified [vnode_setnoreadahead()](https://developer.apple.com/documentation/kernel/1562123-vnode_setnoreadahead)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_setnoreadahead (     vnode_t ); ``` |
| To | ``` void vnode_setnoreadahead (     vnode_t vp ); ``` |

Modified [vnode_settag()](https://developer.apple.com/documentation/kernel/1562288-vnode_settag)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_settag (     vnode_t,     int ); ``` |
| To | ``` void vnode_settag (     vnode_t vp,     int tag ); ``` |

Modified [vnode_specrdev()](https://developer.apple.com/documentation/kernel/1562443-vnode_specrdev)

|  | Declaration |
| --- | --- |
| From | ``` dev_t vnode_specrdev (     vnode_t ); ``` |
| To | ``` dev_t vnode_specrdev (     vnode_t vp ); ``` |

Modified [vnode_startwrite()](https://developer.apple.com/documentation/kernel/1562369-vnode_startwrite)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_startwrite (     vnode_t ); ``` |
| To | ``` void vnode_startwrite (     vnode_t vp ); ``` |

Modified [vnode_tag()](https://developer.apple.com/documentation/kernel/1562337-vnode_tag)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_tag (     vnode_t ); ``` |
| To | ``` int vnode_tag (     vnode_t vp ); ``` |

Modified [vnode_vfs64bitready()](https://developer.apple.com/documentation/kernel/1562169-vnode_vfs64bitready)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_vfs64bitready (     vnode_t ); ``` |
| To | ``` int vnode_vfs64bitready (     vnode_t vp ); ``` |

Modified [vnode_vfsisrdonly()](https://developer.apple.com/documentation/kernel/1562081-vnode_vfsisrdonly)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_vfsisrdonly (     vnode_t ); ``` |
| To | ``` int vnode_vfsisrdonly (     vnode_t vp ); ``` |

Modified [vnode_vfsmaxsymlen()](https://developer.apple.com/documentation/kernel/1562159-vnode_vfsmaxsymlen)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t vnode_vfsmaxsymlen (     vnode_t ); ``` |
| To | ``` uint32_t vnode_vfsmaxsymlen (     vnode_t vp ); ``` |

Modified [vnode_vfsname()](https://developer.apple.com/documentation/kernel/1562467-vnode_vfsname)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_vfsname (     vnode_t,     char * ); ``` |
| To | ``` void vnode_vfsname (     vnode_t vp,     char *buf ); ``` |

Modified [vnode_vfstypenum()](https://developer.apple.com/documentation/kernel/1562295-vnode_vfstypenum)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_vfstypenum (     vnode_t ); ``` |
| To | ``` int vnode_vfstypenum (     vnode_t vp ); ``` |

Modified [vnode_vid()](https://developer.apple.com/documentation/kernel/1562119-vnode_vid)

|  | Declaration |
| --- | --- |
| From | ``` uint32_t vnode_vid (     vnode_t ); ``` |
| To | ``` uint32_t vnode_vid (     vnode_t vp ); ``` |

Modified [vnode_vtype()](https://developer.apple.com/documentation/kernel/1562175-vnode_vtype)

|  | Declaration |
| --- | --- |
| From | ``` enum vtype vnode_vtype (     vnode_t ); ``` |
| To | ``` enum vtype vnode_vtype (     vnode_t vp ); ``` |

Modified [vnode_waitforwrites()](https://developer.apple.com/documentation/kernel/1562434-vnode_waitforwrites)

|  | Declaration |
| --- | --- |
| From | ``` int vnode_waitforwrites (     vnode_t,     int,     int,     int,     const char * ); ``` |
| To | ``` int vnode_waitforwrites (     vnode_t vp,     int output_target,     int slpflag,     int slptimeout,     const char *msg ); ``` |

Modified [vnode_writedone()](https://developer.apple.com/documentation/kernel/1562375-vnode_writedone)

|  | Declaration |
| --- | --- |
| From | ``` void vnode_writedone (     vnode_t ); ``` |
| To | ``` void vnode_writedone (     vnode_t vp ); ``` |

#### sys/vnode_if.h

Added [VFS_RENAME_EXCL](https://developer.apple.com/documentation/kernel/1646220-anonymous/vfs_rename_excl)Added [VFS_RENAME_FLAGS_MASK](https://developer.apple.com/documentation/kernel/1646220-anonymous/vfs_rename_flags_mask)Added [vfs_rename_flags_t](https://developer.apple.com/documentation/kernel/vfs_rename_flags_t)Added [VFS_RENAME_SECLUDE](https://developer.apple.com/documentation/kernel/1646220-anonymous/vfs_rename_seclude)Added [VFS_RENAME_SWAP](https://developer.apple.com/documentation/kernel/1646220-anonymous/vfs_rename_swap)Added [vnop_clonefile_args](https://developer.apple.com/documentation/kernel/vnop_clonefile_args)Added [vnop_clonefile_desc](https://developer.apple.com/documentation/kernel/vnop_clonefile_desc)Added [vnop_renamex_args](https://developer.apple.com/documentation/kernel/vnop_renamex_args)Added [vnop_renamex_desc](https://developer.apple.com/documentation/kernel/vnop_renamex_desc)Modified [VNOP_BWRITE()](https://developer.apple.com/documentation/kernel/1585961-vnop_bwrite)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_BWRITE (     buf_t ); ``` |
| To | ``` errno_t VNOP_BWRITE (     buf_t bp ); ``` |

Modified [VNOP_FSYNC()](https://developer.apple.com/documentation/kernel/1586212-vnop_fsync)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_FSYNC (     vnode_t,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_FSYNC (     vnode_t vp,     int waitfor,     vfs_context_t ctx ); ``` |

Modified [VNOP_GETXATTR()](https://developer.apple.com/documentation/kernel/1586289-vnop_getxattr)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_GETXATTR (     vnode_t,     const char *,     uio_t,     size_t *,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_GETXATTR (     vnode_t vp,     const char *name,     uio_t uio,     size_t *size,     int options,     vfs_context_t ctx ); ``` |

Modified [VNOP_IOCTL()](https://developer.apple.com/documentation/kernel/1586258-vnop_ioctl)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_IOCTL (     vnode_t,     u_long,     caddr_t,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_IOCTL (     vnode_t vp,     u_long command,     caddr_t data,     int fflag,     vfs_context_t ctx ); ``` |

Modified [VNOP_READ()](https://developer.apple.com/documentation/kernel/1586326-vnop_read)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_READ (     vnode_t,     struct uio *,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_READ (     vnode_t vp,     struct uio *uio,     int,     vfs_context_t ctx ); ``` |

Modified [VNOP_SETXATTR()](https://developer.apple.com/documentation/kernel/1586200-vnop_setxattr)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_SETXATTR (     vnode_t,     const char *,     uio_t,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_SETXATTR (     vnode_t vp,     const char *name,     uio_t uio,     int options,     vfs_context_t ctx ); ``` |

Modified [VNOP_WRITE()](https://developer.apple.com/documentation/kernel/1586129-vnop_write)

|  | Declaration |
| --- | --- |
| From | ``` errno_t VNOP_WRITE (     vnode_t,     struct uio *,     int,     vfs_context_t ); ``` |
| To | ``` errno_t VNOP_WRITE (     vnode_t vp,     struct uio *uio,     int ioflag,     vfs_context_t ctx ); ``` |

#### uuid/uuid.h

Added [UUID_NULL](https://developer.apple.com/documentation/kernel/uuid_null)

#### vecLib/vDSP.h

Added #def vDSP_ENUMModified [vDSP_vfill()](https://developer.apple.com/documentation/kernel/1579967-vdsp_vfill)

|  | Declaration |
| --- | --- |
| From | ``` void vDSP_vfill (     const float *__A,     float *__C,     vDSP_Stride __IA,     vDSP_Length __N ); ``` |
| To | ``` void vDSP_vfill (     const float *__A,     float *__C,     vDSP_Stride __IC,     vDSP_Length __N ); ``` |

#### vm/WKdm_new.h

Removed #def WKdm_SCRATCH_BUF_SIZEAdded #def WKdm_SCRATCH_BUF_SIZE_INTERNAL

#### voucher/ipc_pthread_priority_types.h (Added)

Added [ipc_pthread_priority_value_t](https://developer.apple.com/documentation/kernel/ipc_pthread_priority_value_t)Added #def MACH_VOUCHER_ATTR_PTHPRIORITY_CREATEAdded #def MACH_VOUCHER_ATTR_PTHPRIORITY_NULLAdded #def MACH_VOUCHER_PTHPRIORITY_CONTENT_SIZE

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

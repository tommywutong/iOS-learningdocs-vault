---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/IOBluetooth.html
archived_at: '2026-07-18T02:53:07.658411Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# IOBluetooth Changes for Objective-C

### IOBluetooth

#### Bluetooth.h

Added [BluetoothHCICurrentInquiryAccessCodesForWrite](https://developer.apple.com/documentation/kernel/bluetoothhcicurrentinquiryaccesscodesforwrite)Added [BluetoothLESecurityManagerKeypressNotificationType](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype)Added [kBluetoothHCICommandDeleteReservedLTADDR](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommanddeletereservedltaddr)Added [kBluetoothHCICommandEnhancedAcceptSynchronousConnectionRequest](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandenhancedacceptsynchronousconnectionrequest)Added [kBluetoothHCICommandEnhancedSetupSynchronousConnection](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandenhancedsetupsynchronousconnection)Added [kBluetoothHCICommandGetMWSTransportLayerConfiguration](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandgetmwstransportlayerconfiguration)Added [kBluetoothHCICommandLEAddDeviceToResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleadddevicetoresolvinglist)Added [kBluetoothHCICommandLEClearResolvingList](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleclearresolvinglist)Added [kBluetoothHCICommandLEGenerateDHKey](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlegeneratedhkey)Added [kBluetoothHCICommandLEReadLocalP256PublicKey](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadlocalp256publickey)Added [kBluetoothHCICommandLEReadLocalResolvableAddress](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadlocalresolvableaddress)Added [kBluetoothHCICommandLEReadMaximumDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadmaximumdatalength)Added [kBluetoothHCICommandLEReadPeerResolvableAddress](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlereadpeerresolvableaddress)Added [kBluetoothHCICommandLEReadResolvingListSize](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlereadresolvinglistsize)Added [kBluetoothHCICommandLEReadSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlereadsuggesteddefaultdatalength)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestNegativeReply](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandleremoteconnectionparameterrequestnegativereply)Added [kBluetoothHCICommandLERemoteConnectionParameterRequestReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandleremoteconnectionparameterrequestreply)Added [kBluetoothHCICommandLERemoveDeviceFromResolvingList](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandleremovedevicefromresolvinglist)Added [kBluetoothHCICommandLESetAddressResolutionEnable](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandlesetaddressresolutionenable)Added [kBluetoothHCICommandLESetDataLength](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetdatalength)Added [kBluetoothHCICommandLESetResolvablePrivateAddressTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandlesetresolvableprivateaddresstimeout)Added [kBluetoothHCICommandLEWriteSuggestedDefaultDataLength](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandlewritesuggesteddefaultdatalength)Added [kBluetoothHCICommandReadAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadauthenticatedpayloadtimeout)Added [kBluetoothHCICommandReadDataBlockSize](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreaddatablocksize)Added [kBluetoothHCICommandReadExtendedInquiryLength](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadextendedinquirylength)Added [kBluetoothHCICommandReadExtendedPageTimeout](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadextendedpagetimeout)Added [kBluetoothHCICommandReadLocalOOBExtendedData](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandreadlocaloobextendeddata)Added [kBluetoothHCICommandReadLocalSupportedCodecs](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadlocalsupportedcodecs)Added [kBluetoothHCICommandReadSecureConnectionsHostSupport](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadsecureconnectionshostsupport)Added [kBluetoothHCICommandReadSynchronizationTrainParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandreadsynchronizationtrainparameters)Added [kBluetoothHCICommandReceiveSynchronizationTrain](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreceivesynchronizationtrain)Added [kBluetoothHCICommandRemoteOOBExtendedDataRequestReply](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandremoteoobextendeddatarequestreply)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcast](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcast)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastData](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcastdata)Added [kBluetoothHCICommandSetConnectionlessSlaveBroadcastReceive](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandsetconnectionlessslavebroadcastreceive)Added [kBluetoothHCICommandSetExternalFrameConfiguration](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetexternalframeconfiguration)Added [kBluetoothHCICommandSetMWSChannelParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwschannelparameters)Added [kBluetoothHCICommandSetMWSPATTERNConfiguration](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwspatternconfiguration)Added [kBluetoothHCICommandSetMWSScanFrequencyTable](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwsscanfrequencytable)Added [kBluetoothHCICommandSetMWSSignaling](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwssignaling)Added [kBluetoothHCICommandSetMWSTransportLayer](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetmwstransportlayer)Added [kBluetoothHCICommandSetReservedLTADDR](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandsetreservedltaddr)Added [kBluetoothHCICommandSetTriggeredClockCapture](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandsettriggeredclockcapture)Added [kBluetoothHCICommandStartSynchronizationTrain](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandstartsynchronizationtrain)Added [kBluetoothHCICommandTruncatedPage](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpage)Added [kBluetoothHCICommandTruncatedPageCancel](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandtruncatedpagecancel)Added [kBluetoothHCICommandWriteAuthenticatedPayloadTimeout](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcicommandwriteauthenticatedpayloadtimeout)Added [kBluetoothHCICommandWriteExtendedInquiryLength](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwriteextendedinquirylength)Added [kBluetoothHCICommandWriteExtendedPageTimeout](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwriteextendedpagetimeout)Added [kBluetoothHCICommandWriteSecureConnectionsHostSupport](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritesecureconnectionshostsupport)Added [kBluetoothHCICommandWriteSynchronizationTrainParameters](https://developer.apple.com/documentation/kernel/1640155-anonymous/kbluetoothhcicommandwritesynchronizationtrainparameters)Added [kBluetoothLESecurityManagerLinkKey](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeydistributionformat/kbluetoothlesecuritymanagerlinkkey)Added [kBluetoothLESecurityManagerNotificationTypePasskeyCleared](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeycleared)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitEntered](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeydigitentered)Added [kBluetoothLESecurityManagerNotificationTypePasskeyDigitErased](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeydigiterased)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryCompleted](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeyentrycompleted)Added [kBluetoothLESecurityManagerNotificationTypePasskeyEntryStarted](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypepasskeyentrystarted)Added [kBluetoothLESecurityManagerNotificationTypeReservedEnd](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypereservedend)Added [kBluetoothLESecurityManagerNotificationTypeReservedStart](https://developer.apple.com/documentation/kernel/bluetoothlesecuritymanagerkeypressnotificationtype/kbluetoothlesecuritymanagernotificationtypereservedstart)Added [kBluetoothLESecurityManagerReasonCodeBREDRPairingInProgress](https://developer.apple.com/documentation/iobluetooth/kbluetoothlesecuritymanagerreasoncodebredrpairinginprogress)Added [kBluetoothLESecurityManagerReasonCodeCrossTransportKeyDerivationGenerationNotAllowed](https://developer.apple.com/documentation/iobluetooth/bluetoothlesecuritymanagerpairingfailedreasoncode/kbluetoothlesecuritymanagerreasoncodecrosstransportkeyderivationgenerationnotallowed)Added [kMaximumNumberOfInquiryAccessCodes](https://developer.apple.com/documentation/iobluetooth/1489444-anonymous/kmaximumnumberofinquiryaccesscodes)

#### BluetoothAssignedNumbers.h

Added [kBluetoothL2CAPPSMAVCTP_Browsing](https://developer.apple.com/documentation/iobluetooth/kbluetoothl2cappsmavctp_browsing)

#### IOBluetoothUtilities.h

Removed [IOBluetoothLaunchHandsFreeAgent()](https://developer.apple.com/documentation/iobluetooth/iobluetoothutilities.h/1811195-iobluetoothlaunchhandsfreeagent)

#### objc/IOBluetoothHandsFree.h

Removed -[IOBluetoothDevice isHandsFreeAudioGateway]Removed -[IOBluetoothDevice isHandsFreeDevice]Added [IOBluetoothDevice.handsFreeAudioGateway](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427806-ishandsfreeaudiogateway)Added [IOBluetoothDevice.handsFreeDevice](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/1427742-handsfreedevice)

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

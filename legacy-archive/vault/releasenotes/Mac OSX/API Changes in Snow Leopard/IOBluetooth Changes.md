---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/IOBluetooth.html
archived_at: '2026-07-18T02:58:43.418075Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# IOBluetooth Changes

## IOBluetooth

Bluetooth.hRemoved BluetoothHCIRequestNotificationInfo (no architecture available)Removed kBluetoothHCICommandIOCapabilityResponse (no architecture available)Added [BluetoothHCIEventReadExtendedFeaturesResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventreadextendedfeaturesresults) (no architecture available)Added [BluetoothHCIEventReadRemoteExtendedFeaturesResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventreadremoteextendedfeaturesresults) (no architecture available)Added [BluetoothHCIEventSimplePairingCompleteResults](https://developer.apple.com/documentation/kernel/bluetoothhcieventsimplepairingcompleteresults) (no architecture available)Added [BluetoothHCIExtendedFeaturesInfo](https://developer.apple.com/documentation/kernel/bluetoothhciextendedfeaturesinfo) (no architecture available)Added [BluetoothHCIPageNumber](https://developer.apple.com/documentation/iobluetooth/bluetoothhcipagenumber) (no architecture available)Added [BluetoothNumericValue](https://developer.apple.com/documentation/iobluetooth/bluetoothnumericvalue) (no architecture available)Added [BluetoothUserConfirmationRequest](https://developer.apple.com/documentation/iobluetooth/bluetoothuserconfirmationrequest) (no architecture available)Added [kBluetoothFeature3SlotEnhancedDataRateeSCOPackets](https://developer.apple.com/documentation/iobluetooth/kbluetoothfeature3slotenhanceddatarateescopackets) (no architecture available)Added [kBluetoothFeaturePowerControlRequests](https://developer.apple.com/documentation/kernel/bluetoothfeaturebits/kbluetoothfeaturepowercontrolrequests) (no architecture available)Added [kBluetoothFeatureSimpleSecurePairingHostMode](https://developer.apple.com/documentation/iobluetooth/bluetoothfeaturebits/kbluetoothfeaturesimplesecurepairinghostmode) (no architecture available)Added [kBluetoothFeatureSniffSubrating](https://developer.apple.com/documentation/kernel/bluetoothfeaturebits/kbluetoothfeaturesniffsubrating) (no architecture available)Added [kBluetoothHCICommandIOCapabilityRequestReply](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandiocapabilityrequestreply) (no architecture available)Added [kBluetoothHCICommandReadRemoteExtendedFeatures](https://developer.apple.com/documentation/iobluetooth/1489732-anonymous/kbluetoothhcicommandreadremoteextendedfeatures) (no architecture available)Added [#def kBluetoothHCIEventMaskIOCapabilityRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskiocapabilityrequestevent)Added [#def kBluetoothHCIEventMaskIOCapabilityRequestReplyEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskiocapabilityrequestreplyevent)Added [#def kBluetoothHCIEventMaskKeypressNotificationEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskkeypressnotificationevent)Added [#def kBluetoothHCIEventMaskRemoteOOBDataRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskremoteoobdatarequestevent)Added [#def kBluetoothHCIEventMaskSimplePairingCompleteEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmasksimplepairingcompleteevent)Added [#def kBluetoothHCIEventMaskUserConfirmationRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserconfirmationrequestevent)Added [#def kBluetoothHCIEventMaskUserPasskeyNotificationEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserpasskeynotificationevent)Added [#def kBluetoothHCIEventMaskUserPasskeyRequestEvent](https://developer.apple.com/documentation/iobluetooth/kbluetoothhcieventmaskuserpasskeyrequestevent)BluetoothAssignedNumbers.hAdded [kBluetoothSDPAttributeIdentifierHIDVirtualCable](https://developer.apple.com/documentation/kernel/sdpattributeidentifiercodes/kbluetoothsdpattributeidentifierhidvirtualcable)IOBluetoothSDPServiceRecord.hAdded [-[IOBluetoothSDPServiceRecord initWithServiceDictionary:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1431493-init) (no architecture available)Added [+[IOBluetoothSDPServiceRecord withServiceDictionary:device:]](https://developer.apple.com/documentation/iobluetooth/iobluetoothsdpservicerecord/1435073-withservicedictionary) (no architecture available)IOBluetoothUserLib.hAdded #def BLUETOOTH_VERSION_2_1Added #def BLUETOOTH_VERSION_2_1_0Added #def BLUETOOTH_VERSION_2_1_1Added [IOBluetoothIgnoreHIDDevice()](https://developer.apple.com/documentation/iobluetooth/1433141-iobluetoothignorehiddevice) (no architecture available)Added [IOBluetoothRemoveIgnoredHIDDevice()](https://developer.apple.com/documentation/iobluetooth/1429363-iobluetoothremoveignoredhiddevic) (no architecture available)OBEX.hAdded [OBEXOpCodeSessionValues](https://developer.apple.com/documentation/iobluetooth/obex.h/obexopcodesessionvalues) (no architecture available)Added [OBEXSessionParameterTags](https://developer.apple.com/documentation/iobluetooth/obex.h/obexsessionparametertags) (no architecture available)Added [kOBEXForbiddenError](https://developer.apple.com/documentation/iobluetooth/obexerrorcodes/kobexforbiddenerror) (no architecture available)Added [kOBEXHeaderIDOBEX13CreatorID](https://developer.apple.com/documentation/iobluetooth/kobexheaderidobex13creatorid) (no architecture available)Added [kOBEXHeaderIDOBEX13ObjectClass](https://developer.apple.com/documentation/iobluetooth/kobexheaderidobex13objectclass) (no architecture available)Added [kOBEXHeaderIDOBEX13SessionParameters](https://developer.apple.com/documentation/iobluetooth/kobexheaderidobex13sessionparameters) (no architecture available)Added [kOBEXHeaderIDOBEX13SessionSequenceNumber](https://developer.apple.com/documentation/iobluetooth/obexheaderidentifiers/kobexheaderidobex13sessionsequencenumber) (no architecture available)Added [kOBEXHeaderIDOBEX13WANUUID](https://developer.apple.com/documentation/iobluetooth/kobexheaderidobex13wanuuid) (no architecture available)Added [kOBEXOpCodeCloseSession](https://developer.apple.com/documentation/iobluetooth/obexopcodesessionvalues/kobexopcodeclosesession) (no architecture available)Added [kOBEXOpCodeCreateSession](https://developer.apple.com/documentation/iobluetooth/obexopcodesessionvalues/kobexopcodecreatesession) (no architecture available)Added [kOBEXOpCodeResumeSession](https://developer.apple.com/documentation/iobluetooth/kobexopcoderesumesession) (no architecture available)Added [kOBEXOpCodeSetTimeout](https://developer.apple.com/documentation/iobluetooth/kobexopcodesettimeout) (no architecture available)Added [kOBEXOpCodeSuspendSession](https://developer.apple.com/documentation/iobluetooth/obexopcodesessionvalues/kobexopcodesuspendsession) (no architecture available)Added [kOBEXSessionParameterTagDeviceAddress](https://developer.apple.com/documentation/iobluetooth/obexsessionparametertags/kobexsessionparametertagdeviceaddress) (no architecture available)Added [kOBEXSessionParameterTagNextSequenceNumber](https://developer.apple.com/documentation/iobluetooth/kobexsessionparametertagnextsequencenumber) (no architecture available)Added [kOBEXSessionParameterTagNonce](https://developer.apple.com/documentation/iobluetooth/kobexsessionparametertagnonce) (no architecture available)Added [kOBEXSessionParameterTagSessionID](https://developer.apple.com/documentation/iobluetooth/obexsessionparametertags/kobexsessionparametertagsessionid) (no architecture available)Added [kOBEXSessionParameterTagSessionOpcode](https://developer.apple.com/documentation/iobluetooth/kobexsessionparametertagsessionopcode) (no architecture available)Added [kOBEXSessionParameterTagTimeout](https://developer.apple.com/documentation/iobluetooth/kobexsessionparametertagtimeout) (no architecture available)

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

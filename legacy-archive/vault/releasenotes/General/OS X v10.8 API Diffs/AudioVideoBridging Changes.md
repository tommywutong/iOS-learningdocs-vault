---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/AudioVideoBridging.html
archived_at: '2026-07-18T02:53:56.826274Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# AudioVideoBridging Changes

## AudioVideoBridging

AVB17221ACMPInterface.hAdded AVB17221ACMPClientAdded -[AVB17221ACMPClient ACMPDidReceiveCommand:onInterface:]Added -[AVB17221ACMPClient ACMPDidReceiveResponse:onInterface:]Added AVB17221ACMPInterfaceAdded +[AVB17221ACMPInterface ACMPInterfaceWithInterface:]Added +[AVB17221ACMPInterface ACMPInterfaceWithInterfaceNamed:]Added AVB17221ACMPInterface.multicastDestinationAddressAdded -[AVB17221ACMPInterface removeHandlerForGUID:]Added -[AVB17221ACMPInterface sendACMPCommandMessage:completionHandler:]Added -[AVB17221ACMPInterface sendACMPResponseMessage:error:]Added -[AVB17221ACMPInterface setHandler:forGUID:]Added AVB17221ACMPInterfaceCompletionAVB17221ACMPMessage.hAdded AVB17221ACMPMessageAdded AVB17221ACMPMessage.connectionCountAdded AVB17221ACMPMessage.controllerGUIDAdded AVB17221ACMPMessage.destinationMACAdded AVB17221ACMPMessage.flagsAdded AVB17221ACMPMessage.listenerGUIDAdded AVB17221ACMPMessage.listenerUniqueIDAdded AVB17221ACMPMessage.messageTypeAdded AVB17221ACMPMessage.sequenceIDAdded AVB17221ACMPMessage.sourceMACAdded AVB17221ACMPMessage.statusAdded AVB17221ACMPMessage.streamIDAdded AVB17221ACMPMessage.talkerGUIDAdded AVB17221ACMPMessage.talkerUniqueIDAVB17221AECPInterface.hAdded AVB17221AECPClientAdded -[AVB17221AECPClient AECPDidReceiveCommand:onInterface:]Added -[AVB17221AECPClient AECPDidReceiveResponse:onInterface:]Added AVB17221AECPInterfaceAdded +[AVB17221AECPInterface AECPInterfaceWithInterface:]Added +[AVB17221AECPInterface AECPInterfaceWithInterfaceNamed:]Added -[AVB17221AECPInterface removeHandlerForGUID:]Added -[AVB17221AECPInterface sendCommand:toMACAddress:completionHandler:]Added -[AVB17221AECPInterface sendResponse:toMACAddress:error:]Added -[AVB17221AECPInterface setHandler:forGUID:]Added AVB17221AECPInterfaceCompletionAVB17221AECPMessage.hAdded AVB17221AECPAEMMessageAdded +[AVB17221AECPAEMMessage commandMessage]Added AVB17221AECPAEMMessage.commandSpecificDataAdded AVB17221AECPAEMMessage.commandTypeAdded +[AVB17221AECPAEMMessage responseMessage]Added AVB17221AECPAEMMessage.unsolicitedAdded AVB17221AECPAVCMessageAdded AVB17221AECPAVCMessage.commandResponseAdded AVB17221AECPAddressAccessMessageAdded +[AVB17221AECPAddressAccessMessage commandMessage]Added +[AVB17221AECPAddressAccessMessage responseMessage]Added AVB17221AECPAddressAccessMessage.tlvsAdded AVB17221AECPAddressAccessTLVAdded AVB17221AECPAddressAccessTLV.addressAdded AVB17221AECPAddressAccessTLV.memoryDataAdded AVB17221AECPAddressAccessTLV.modeAdded AVB17221AECPMessageAdded AVB17221AECPMessage.controllerGUIDAdded AVB17221AECPMessage.messageTypeAdded AVB17221AECPMessage.sequenceIDAdded AVB17221AECPMessage.sourceMACAdded AVB17221AECPMessage.statusAdded AVB17221AECPMessage.targetGUIDAdded AVB17221AECPVendorMessageAdded AVB17221AECPVendorMessage.protocolIDAdded AVB17221AECPVendorMessage.protocolSpecificDataAVB17221Entity.hAdded AVB17221EntityAdded AVB17221Entity.asGrandmasterIDAdded AVB17221Entity.associationIDAdded AVB17221Entity.availableIndexAdded AVB17221Entity.controllerCapabilitiesAdded AVB17221Entity.entityCapabilitiesAdded AVB17221Entity.entityDiscoveryAdded AVB17221Entity.guidAdded AVB17221Entity.listenerCapabilitiesAdded AVB17221Entity.listenerStreamSinksAdded AVB17221Entity.localEntityAdded AVB17221Entity.macAddressesAdded AVB17221Entity.modelIDAdded AVB17221Entity.talkerCapabilitiesAdded AVB17221Entity.talkerStreamSourcesAdded AVB17221Entity.timeToLiveAdded AVB17221Entity.vendorIDAVB17221EntityDiscovery.hAdded AVB17221EntityDiscoveryAdded -[AVB17221EntityDiscovery addLocalEntity:error:]Added -[AVB17221EntityDiscovery changeEntityWithGUID:toNewASGrandmasterID:error:]Added -[AVB17221EntityDiscovery discoverEntities]Added -[AVB17221EntityDiscovery discoverEntity:]Added AVB17221EntityDiscovery.discoveryDelegateAdded -[AVB17221EntityDiscovery initWithInterfaceName:]Added AVB17221EntityDiscovery.interfaceAdded AVB17221EntityDiscovery.interfaceNameAdded -[AVB17221EntityDiscovery primeIterators]Added -[AVB17221EntityDiscovery removeLocalEntity:error:]AVB17221EntityDiscoveryDelegate.hAdded AVB17221EntityDiscoveryDelegateAdded -[AVB17221EntityDiscoveryDelegate didAddLocalEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didAddRemoteEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didRediscoverLocalEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didRediscoverRemoteEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didRemoveLocalEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didRemoveRemoteEntity:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didUpdateLocalEntity:changedProperties:on17221EntityDiscovery:]Added -[AVB17221EntityDiscoveryDelegate didUpdateRemoteEntity:changedProperties:on17221EntityDiscovery:]Added AVB17221EntityPropertyChangedAdded AVB17221EntityPropertyChangedASGrandmasterIDAdded AVB17221EntityPropertyChangedAssociationIDAdded AVB17221EntityPropertyChangedAvailableIndexAdded AVB17221EntityPropertyChangedControllerCapabilitiesAdded AVB17221EntityPropertyChangedEntityCapabilitiesAdded AVB17221EntityPropertyChangedEntityTypeAdded AVB17221EntityPropertyChangedGUIDAdded AVB17221EntityPropertyChangedListenerCapabilitiesAdded AVB17221EntityPropertyChangedListenerStreamSinksAdded AVB17221EntityPropertyChangedMACAddressAdded AVB17221EntityPropertyChangedModelIDAdded AVB17221EntityPropertyChangedTalkerCapabilitiesAdded AVB17221EntityPropertyChangedTalkerStreamSourcesAdded AVB17221EntityPropertyChangedTimeToLiveAdded AVB17221EntityPropertyChangedVendorIDAdded NA (no architecture available)Added #def kAVB17221EntityPropertyChangedCanChangeMaskAdded #def kAVB17221EntityPropertyChangedShouldntChangeMaskAVB1722ControlInterface.hAdded AVB1722ControlInterfaceAdded -[AVB1722ControlInterface initWithService:onInterface:]Added -[AVB1722ControlInterface initWithService:onInterfaceNamed:]Added AVB1722ControlInterface.interfaceAdded AVB1722ControlInterface.interfaceNameAVBConstants.hAdded AVBErrorDomainAdded #def AVBMACAddressSizeAdded #def AudioVideoBridging_AVBConstants_hAdded NS_ENUM()Added NS_ENUM_AVAILABLE()Added NS_OPTIONS()AVBEthernetInterface.hAdded AVBEthernetInterfaceAVBInterface.hAdded AVBInterfaceAdded AVBInterface.acmpAdded AVBInterface.aecpAdded AVBInterface.entityDiscoveryAdded -[AVBInterface initWithInterfaceName:]Added AVBInterface.interfaceNameAdded +[AVBInterface isAVBCapableInterfaceNamed:]Added +[AVBInterface isAVBEnabledOnInterfaceNamed:]Added +[AVBInterface macAddressForInterfaceNamed:]Added +[AVBInterface myGUID]Added +[AVBInterface supportedInterfaces]AVBMACAddress.hAdded AVBMACAddressAdded AVBMACAddress.bytesAdded AVBMACAddress.dataRepresentationAdded -[AVBMACAddress initWithBytes:]Added AVBMACAddress.multicastAdded AVBMACAddress.stringRepresentationAudioVideoBridging.hAdded #def AudioVideoBridging_H

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

---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/AudioVideoBridging.html
archived_at: '2026-07-18T02:52:56.015663Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# AudioVideoBridging Changes for Objective-C

### AudioVideoBridging

#### AVB17221ACMPInterface.h

Modified -[AVB17221ACMPClient ACMPDidReceiveCommand:onInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)ACMPDidReceiveCommand:(AVB17221ACMPMessage *)message onInterface:(AVB17221ACMPInterface *)anInterface ``` |
| To | ``` - (BOOL)ACMPDidReceiveCommand:(AVB17221ACMPMessage * _Nonnull)message onInterface:(AVB17221ACMPInterface * _Nonnull)anInterface ``` |

Modified -[AVB17221ACMPClient ACMPDidReceiveResponse:onInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)ACMPDidReceiveResponse:(AVB17221ACMPMessage *)message onInterface:(AVB17221ACMPInterface *)anInterface ``` |
| To | ``` - (BOOL)ACMPDidReceiveResponse:(AVB17221ACMPMessage * _Nonnull)message onInterface:(AVB17221ACMPInterface * _Nonnull)anInterface ``` |

Modified +[AVB17221ACMPInterface ACMPInterfaceWithInterface:]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221ACMPInterface *)ACMPInterfaceWithInterface:(AVBInterface *)anInterface ``` |
| To | ``` + (AVB17221ACMPInterface * _Nonnull)ACMPInterfaceWithInterface:(AVBInterface * _Nonnull)anInterface ``` |

Modified +[AVB17221ACMPInterface ACMPInterfaceWithInterfaceNamed:]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221ACMPInterface *)ACMPInterfaceWithInterfaceNamed:(NSString *)anInterfaceName ``` |
| To | ``` + (AVB17221ACMPInterface * _Nonnull)ACMPInterfaceWithInterfaceNamed:(NSString * _Nonnull)anInterfaceName ``` |

Modified AVB17221ACMPInterface.multicastDestinationAddress

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) AVBMACAddress *multicastDestinationAddress ``` |
| To | ``` @property(readonly, copy, nonnull) AVBMACAddress *multicastDestinationAddress ``` |

Modified -[AVB17221ACMPInterface sendACMPCommandMessage:completionHandler:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendACMPCommandMessage:(AVB17221ACMPMessage *)message completionHandler:(AVB17221ACMPInterfaceCompletion)completionHandler ``` |
| To | ``` - (BOOL)sendACMPCommandMessage:(AVB17221ACMPMessage * _Nonnull)message completionHandler:(AVB17221ACMPInterfaceCompletion _Nonnull)completionHandler ``` |

Modified -[AVB17221ACMPInterface sendACMPResponseMessage:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendACMPResponseMessage:(AVB17221ACMPMessage *)message error:(NSError **)error ``` |
| To | ``` - (BOOL)sendACMPResponseMessage:(AVB17221ACMPMessage * _Nonnull)message error:(NSError * _Nullable * _Nullable)error ``` |

Modified -[AVB17221ACMPInterface setHandler:forEntityID:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setHandler:(id<AVB17221ACMPClient>)handler forEntityID:(uint64_t)targetEntityID ``` |
| To | ``` - (BOOL)setHandler:(id<AVB17221ACMPClient> _Nonnull)handler forEntityID:(uint64_t)targetEntityID ``` |

Modified -[AVB17221ACMPInterface setHandler:forGUID:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setHandler:(id<AVB17221ACMPClient>)handler forGUID:(uint64_t)targetGUID ``` |
| To | ``` - (BOOL)setHandler:(id<AVB17221ACMPClient> _Nonnull)handler forGUID:(uint64_t)targetGUID ``` |

#### AVB17221ACMPMessage.h

Modified AVB17221ACMPMessage.destinationMAC

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) AVBMACAddress *destinationMAC ``` |
| To | ``` @property(copy, nullable) AVBMACAddress *destinationMAC ``` |

Modified AVB17221ACMPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) AVBMACAddress *sourceMAC ``` |
| To | ``` @property(copy, nullable) AVBMACAddress *sourceMAC ``` |

#### AVB17221AECPInterface.h

Added -[AVB17221AECPInterface removeCommandHandlerForEntityID:]Added -[AVB17221AECPInterface removeResponseHandlerForControllerEntityID:]Added -[AVB17221AECPInterface setCommandHandler:forEntityID:]Added -[AVB17221AECPInterface setResponseHandler:forControllerEntityID:]Modified -[AVB17221AECPClient AECPDidReceiveCommand:onInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)AECPDidReceiveCommand:(AVB17221AECPMessage *)message onInterface:(AVB17221AECPInterface *)anInterface ``` |
| To | ``` - (BOOL)AECPDidReceiveCommand:(AVB17221AECPMessage * _Nonnull)message onInterface:(AVB17221AECPInterface * _Nonnull)anInterface ``` |

Modified -[AVB17221AECPClient AECPDidReceiveResponse:onInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)AECPDidReceiveResponse:(AVB17221AECPMessage *)message onInterface:(AVB17221AECPInterface *)anInterface ``` |
| To | ``` - (BOOL)AECPDidReceiveResponse:(AVB17221AECPMessage * _Nonnull)message onInterface:(AVB17221AECPInterface * _Nonnull)anInterface ``` |

Modified +[AVB17221AECPInterface AECPInterfaceWithInterface:]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPInterface *)AECPInterfaceWithInterface:(AVBInterface *)anInterface ``` |
| To | ``` + (AVB17221AECPInterface * _Nullable)AECPInterfaceWithInterface:(AVBInterface * _Nonnull)anInterface ``` |

Modified +[AVB17221AECPInterface AECPInterfaceWithInterfaceNamed:]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPInterface *)AECPInterfaceWithInterfaceNamed:(NSString *)anInterfaceName ``` |
| To | ``` + (AVB17221AECPInterface * _Nullable)AECPInterfaceWithInterfaceNamed:(NSString * _Nonnull)anInterfaceName ``` |

Modified -[AVB17221AECPInterface removeHandlerForEntityID:]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

Modified -[AVB17221AECPInterface sendCommand:toMACAddress:completionHandler:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendCommand:(AVB17221AECPMessage *)message toMACAddress:(AVBMACAddress *)destMAC completionHandler:(AVB17221AECPInterfaceCompletion)completionHandler ``` |
| To | ``` - (BOOL)sendCommand:(AVB17221AECPMessage * _Nonnull)message toMACAddress:(AVBMACAddress * _Nonnull)destMAC completionHandler:(AVB17221AECPInterfaceCompletion _Nonnull)completionHandler ``` |

Modified -[AVB17221AECPInterface sendResponse:toMACAddress:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendResponse:(AVB17221AECPMessage *)message toMACAddress:(AVBMACAddress *)destMAC error:(NSError **)error ``` |
| To | ``` - (BOOL)sendResponse:(AVB17221AECPMessage * _Nonnull)message toMACAddress:(AVBMACAddress * _Nonnull)destMAC error:(NSError * _Nullable * _Nullable)error ``` |

Modified -[AVB17221AECPInterface setHandler:forEntityID:]

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (BOOL)setHandler:(id<AVB17221AECPClient>)handler forEntityID:(uint64_t)targetEntityID ``` | -- |
| To | ``` - (BOOL)setHandler:(id<AVB17221AECPClient> _Nonnull)handler forEntityID:(uint64_t)targetEntityID ``` | OS X 10.11 |

Modified -[AVB17221AECPInterface setHandler:forGUID:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)setHandler:(id<AVB17221AECPClient>)handler forGUID:(uint64_t)targetGUID ``` |
| To | ``` - (BOOL)setHandler:(id<AVB17221AECPClient> _Nonnull)handler forGUID:(uint64_t)targetGUID ``` |

#### AVB17221AECPMessage.h

Modified +[AVB17221AECPAddressAccessMessage commandMessage]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPAddressAccessMessage *)commandMessage ``` |
| To | ``` + (AVB17221AECPAddressAccessMessage * _Nonnull)commandMessage ``` |

Modified +[AVB17221AECPAddressAccessMessage responseMessage]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPAddressAccessMessage *)responseMessage ``` |
| To | ``` + (AVB17221AECPAddressAccessMessage * _Nonnull)responseMessage ``` |

Modified AVB17221AECPAddressAccessMessage.tlvs

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *tlvs ``` |
| To | ``` @property(copy, nullable) NSArray<AVB17221AECPAddressAccessTLV *> *tlvs ``` |

Modified AVB17221AECPAddressAccessTLV.memoryData

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *memoryData ``` |
| To | ``` @property(copy, nullable) NSData *memoryData ``` |

Modified +[AVB17221AECPAEMMessage commandMessage]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPAEMMessage *)commandMessage ``` |
| To | ``` + (AVB17221AECPAEMMessage * _Nonnull)commandMessage ``` |

Modified AVB17221AECPAEMMessage.commandSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *commandSpecificData ``` |
| To | ``` @property(copy, nullable) NSData *commandSpecificData ``` |

Modified +[AVB17221AECPAEMMessage responseMessage]

|  | Declaration |
| --- | --- |
| From | ``` + (AVB17221AECPAEMMessage *)responseMessage ``` |
| To | ``` + (AVB17221AECPAEMMessage * _Nonnull)responseMessage ``` |

Modified AVB17221AECPAVCMessage.commandResponse

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *commandResponse ``` |
| To | ``` @property(copy, nullable) NSData *commandResponse ``` |

Modified AVB17221AECPMessage.sourceMAC

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) AVBMACAddress *sourceMAC ``` |
| To | ``` @property(copy, nonnull) AVBMACAddress *sourceMAC ``` |

Modified AVB17221AECPVendorMessage.protocolSpecificData

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *protocolSpecificData ``` |
| To | ``` @property(copy, nullable) NSData *protocolSpecificData ``` |

#### AVB17221Entity.h

Modified AVB17221Entity.entityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) AVB17221EntityDiscovery *entityDiscovery ``` |
| To | ``` @property(assign, nullable) AVB17221EntityDiscovery *entityDiscovery ``` |

Modified AVB17221Entity.macAddresses

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *macAddresses ``` |
| To | ``` @property(copy, nonnull) NSArray<AVBMACAddress *> *macAddresses ``` |

#### AVB17221EntityDiscovery.h

Modified -[AVB17221EntityDiscovery addLocalEntity:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)addLocalEntity:(AVB17221Entity *)anEntity error:(NSError **)error ``` |
| To | ``` - (BOOL)addLocalEntity:(AVB17221Entity * _Nonnull)anEntity error:(NSError * _Nullable * _Nullable)error ``` |

Modified -[AVB17221EntityDiscovery changeEntityWithEntityID:toNewGPTPGrandmasterID:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)changeEntityWithEntityID:(uint64_t)entityID toNewGPTPGrandmasterID:(uint64_t)gPTPGrandmasterID error:(NSError **)error ``` |
| To | ``` - (BOOL)changeEntityWithEntityID:(uint64_t)entityID toNewGPTPGrandmasterID:(uint64_t)gPTPGrandmasterID error:(NSError * _Nullable * _Nullable)error ``` |

Modified -[AVB17221EntityDiscovery changeEntityWithGUID:toNewASGrandmasterID:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)changeEntityWithGUID:(uint64_t)entityGUID toNewASGrandmasterID:(uint64_t)asGrandmasterID error:(NSError **)error ``` |
| To | ``` - (BOOL)changeEntityWithGUID:(uint64_t)entityGUID toNewASGrandmasterID:(uint64_t)asGrandmasterID error:(NSError * _Nullable * _Nullable)error ``` |

Modified AVB17221EntityDiscovery.discoveryDelegate

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id<AVB17221EntityDiscoveryDelegate> discoveryDelegate ``` |
| To | ``` @property(assign, nullable) id<AVB17221EntityDiscoveryDelegate> discoveryDelegate ``` |

Modified -[AVB17221EntityDiscovery initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype _Nonnull)initWithInterfaceName:(NSString * _Nonnull)anInterfaceName ``` |

Modified AVB17221EntityDiscovery.interface

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) AVBInterface *interface ``` |
| To | ``` @property(readonly, assign, nullable) AVBInterface *interface ``` |

Modified AVB17221EntityDiscovery.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *interfaceName ``` |
| To | ``` @property(copy, nonnull) NSString *interfaceName ``` |

Modified -[AVB17221EntityDiscovery removeLocalEntity:error:]

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)removeLocalEntity:(uint64_t)guid error:(NSError **)error ``` |
| To | ``` - (BOOL)removeLocalEntity:(uint64_t)guid error:(NSError * _Nullable * _Nullable)error ``` |

#### AVB17221EntityDiscoveryDelegate.h

Modified -[AVB17221EntityDiscoveryDelegate didAddLocalEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didAddLocalEntity:(AVB17221Entity *)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didAddLocalEntity:(AVB17221Entity * _Nonnull)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didAddRemoteEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didAddRemoteEntity:(AVB17221Entity *)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didAddRemoteEntity:(AVB17221Entity * _Nonnull)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didRediscoverLocalEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRediscoverLocalEntity:(AVB17221Entity *)entity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didRediscoverLocalEntity:(AVB17221Entity * _Nonnull)entity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didRediscoverRemoteEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRediscoverRemoteEntity:(AVB17221Entity *)entity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didRediscoverRemoteEntity:(AVB17221Entity * _Nonnull)entity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didRemoveLocalEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRemoveLocalEntity:(AVB17221Entity *)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didRemoveLocalEntity:(AVB17221Entity * _Nonnull)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didRemoveRemoteEntity:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRemoveRemoteEntity:(AVB17221Entity *)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didRemoveRemoteEntity:(AVB17221Entity * _Nonnull)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didUpdateLocalEntity:changedProperties:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didUpdateLocalEntity:(AVB17221Entity *)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didUpdateLocalEntity:(AVB17221Entity * _Nonnull)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

Modified -[AVB17221EntityDiscoveryDelegate didUpdateRemoteEntity:changedProperties:on17221EntityDiscovery:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didUpdateRemoteEntity:(AVB17221Entity *)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery ``` |
| To | ``` - (void)didUpdateRemoteEntity:(AVB17221Entity * _Nonnull)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery * _Nonnull)entityDiscovery ``` |

#### AVB1722ControlInterface.h

Removed -[AVB1722ControlInterface initWithService:onInterface:]Removed -[AVB1722ControlInterface initWithService:onInterfaceNamed:]Added -[AVB1722ControlInterface initWithInterface:]Modified -[AVB1722ControlInterface initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype _Nullable)initWithInterfaceName:(NSString * _Nonnull)anInterfaceName ``` |

Modified AVB1722ControlInterface.interface

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign) AVBInterface *interface ``` |
| To | ``` @property(readonly, assign, nullable) AVBInterface *interface ``` |

Modified AVB1722ControlInterface.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *interfaceName ``` |
| To | ``` @property(readonly, copy, nonnull) NSString *interfaceName ``` |

#### AVBCentralManager.h

Modified -[AVBCentralManager didAddInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didAddInterface:(AVBInterface *)interface ``` |
| To | ``` - (void)didAddInterface:(AVBInterface * _Nonnull)interface ``` |

Modified -[AVBCentralManager didRemoveInterface:]

|  | Declaration |
| --- | --- |
| From | ``` - (void)didRemoveInterface:(AVBInterface *)interface ``` |
| To | ``` - (void)didRemoveInterface:(AVBInterface * _Nonnull)interface ``` |

#### AVBConstants.h

Added AVB17221AECPStatusStreamIsRunningAdded #def AVB_LEGACY_OBJC_RUNTIMEAdded #def AVB_MODERN_OBJC_RUNTIME

#### AVBInterface.h

Modified AVBInterface.acmp

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) AVB17221ACMPInterface *acmp ``` |
| To | ``` @property(retain, readonly, nullable) AVB17221ACMPInterface *acmp ``` |

Modified AVBInterface.aecp

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) AVB17221AECPInterface *aecp ``` |
| To | ``` @property(retain, readonly, nullable) AVB17221AECPInterface *aecp ``` |

Modified AVBInterface.entityDiscovery

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, readonly) AVB17221EntityDiscovery *entityDiscovery ``` |
| To | ``` @property(retain, readonly, nullable) AVB17221EntityDiscovery *entityDiscovery ``` |

Modified -[AVBInterface initWithInterfaceName:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithInterfaceName:(NSString *)anInterfaceName ``` |
| To | ``` - (instancetype _Nullable)initWithInterfaceName:(NSString * _Nonnull)anInterfaceName ``` |

Modified AVBInterface.interfaceName

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly) NSString *interfaceName ``` |
| To | ``` @property(copy, readonly, nonnull) NSString *interfaceName ``` |

Modified +[AVBInterface isAVBCapableInterfaceNamed:]

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)isAVBCapableInterfaceNamed:(NSString *)anInterfaceName ``` |
| To | ``` + (BOOL)isAVBCapableInterfaceNamed:(NSString * _Nonnull)anInterfaceName ``` |

Modified +[AVBInterface isAVBEnabledOnInterfaceNamed:]

|  | Declaration |
| --- | --- |
| From | ``` + (BOOL)isAVBEnabledOnInterfaceNamed:(NSString *)anInterfaceName ``` |
| To | ``` + (BOOL)isAVBEnabledOnInterfaceNamed:(NSString * _Nonnull)anInterfaceName ``` |

Modified +[AVBInterface macAddressForInterfaceNamed:]

|  | Declaration |
| --- | --- |
| From | ``` + (AVBMACAddress *)macAddressForInterfaceNamed:(NSString *)anInterfaceName ``` |
| To | ``` + (AVBMACAddress * _Nullable)macAddressForInterfaceNamed:(NSString * _Nonnull)anInterfaceName ``` |

Modified +[AVBInterface myGUID]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified +[AVBInterface supportedInterfaces]

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)supportedInterfaces ``` |
| To | ``` + (NSArray<NSString *> * _Nullable)supportedInterfaces ``` |

#### AVBMACAddress.h

Modified AVBMACAddress.bytes

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, readonly) const uint8_t *bytes ``` |
| To | ``` @property(assign, readonly, nonnull) const uint8_t *bytes ``` |

Modified AVBMACAddress.dataRepresentation

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSData *dataRepresentation ``` |
| To | ``` @property(copy, nonnull) NSData *dataRepresentation ``` |

Modified -[AVBMACAddress initWithBytes:]

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithBytes:(uint8_t *)bytes ``` |
| To | ``` - (instancetype _Nonnull)initWithBytes:(const uint8_t * _Nonnull)bytes ``` |

Modified AVBMACAddress.stringRepresentation

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *stringRepresentation ``` |
| To | ``` @property(copy, nonnull) NSString *stringRepresentation ``` |

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

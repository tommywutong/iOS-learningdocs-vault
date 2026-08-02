---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/AVBNetworkBrowser_ANBAVDECCEntity_m.html
archived_at: '2026-07-26T19:54:13.870415Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-ANBEUI64Transformer.h.md)[Previous](AVBNetworkBrowser-ANBAVDECCEntity.h.md)

# AVBNetworkBrowser/ANBAVDECCEntity.m

```objc
/*

     File: ANBAVDECCEntity.m
 Abstract: Implementation for a class which maintains the state and information for an IEEE Std. 1722.1-2013 AVDECC Entity. It uses AVDECC AECP AEM Commmands and Responses to read the information from the Entity.
  Version: 1.0

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
 Inc. ("Apple") in consideration of your agreement to the following
 terms, and your use, installation, modification or redistribution of
 this Apple software constitutes acceptance of these terms.  If you do
 not agree with these terms, please do not use, install, modify or
 redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software.
 Neither the name, trademarks, service marks or logos of Apple Inc. may
 be used to endorse or promote products derived from the Apple Software
 without specific prior written permission from Apple.  Except as
 expressly stated in this notice, no other rights or licenses, express or
 implied, are granted by Apple herein, including but not limited to any
 patent rights that may be infringed by your derivative works or by other
 works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import "ANBAVDECCEntity.h"

#import "AVBTypes.h"

#import "ANBAppDelegate.h"

//The maximum number of AECP commands that may be inflight to this Entity at once
#define INFLIGHT_LIMIT  8

//524 (max) - 12 (sizeof address access common header) - 10 (sizeof address access tlv header)
#define MAX_SEGMENT_LENGTH  502

@interface ANBAVDECCEntity ()
{
    uint16_t _currentConfiguration;
    dispatch_queue_t _aecpQueue;
    dispatch_semaphore_t _aecpLimiter;
    BOOL _hasInterface;
    uint16_t _interfaceIndex;
    BOOL _hasLocale;
    uint16_t _localeIndex;
    uint16_t _localeBaseStrings;

    uint16_t _localeCount;
    NSMutableDictionary *_possibleLocales;

    uint16_t _vendorStringsOffset;
    uint8_t _vendorStringIndex;
    uint16_t _modelStringsOffset;
    uint8_t _modelStringIndex;
}

@end

@implementation ANBAVDECCEntity

- (id)initWithADPEntity:(AVB17221Entity *)adpEntity onInterface:(AVBInterface *)interface
{
    self = [super init];
    if(self)
    {
        self.adpEntity = adpEntity;
        self.interface = interface;

        //Create the dispatch queue and semaphore for limiting the number of AECP commands sent to the device
        //By using a serial dispatch queue and a semaphore we can queue up a number of AECP commands and then
        //let the semaphore limit how many are inflight at once. INFLIGHT_LIMIT is currently set at 8 which is
        //a number that most devices seem to be able to handle.
        _aecpQueue = dispatch_queue_create([[NSString stringWithFormat:@"%@.0x%016llx", [self className], adpEntity.entityID] UTF8String], 0);
        _aecpLimiter = dispatch_semaphore_create(INFLIGHT_LIMIT);

        //Use some placeholder images in case the entity doesn't have any or we can't read them.
        self.vendorLogo = [NSImage imageNamed:NSImageNameNetwork];
        self.entityLogo = [NSImage imageNamed:NSImageNameAdvanced];
    }
    return self;
}

- (void)parseEntity
{
    //The process of parsing the entity happens recursively through the tree of descriptors as it is parsed
    //We start of with the Entity descriptor
    [self readEntityDescriptor];
}

//Read an AEM ENTITY descriptor from the Entity
- (void)readEntityDescriptor
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //Construct the read descriptor command
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = 0;
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeEntity);
    readDescriptorCommand.descriptor_index = 0;

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMEntityDescriptorFields)))
                    {
                        AVB17221AEMEntityDescriptorFields *descriptor = (AVB17221AEMEntityDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        NSUInteger length = strnlen((const char *)descriptor->entity_name, AVB17221AEMNameLength);
                        NSString *entityName = [[NSString alloc] initWithBytes:descriptor->entity_name length:length encoding:NSUTF8StringEncoding];

                        _vendorStringsOffset = OSSwapBigToHostInt16(descriptor->vendor_name_string);
                        _vendorStringIndex = _vendorStringsOffset & 0x07;
                        _vendorStringsOffset = _vendorStringsOffset >> 3;

                        _modelStringsOffset = OSSwapBigToHostInt16(descriptor->model_name_string);
                        _modelStringIndex = _modelStringsOffset & 0x07;
                        _modelStringsOffset = _modelStringsOffset >> 3;

                        length = strnlen((const char *)descriptor->firmware_version, AVB17221AEMNameLength);
                        NSString *firmwareVersion = [[NSString alloc] initWithBytes:descriptor->firmware_version length:length encoding:NSUTF8StringEncoding];

                        length = strnlen((const char *)descriptor->group_name, AVB17221AEMNameLength);
                        NSString *groupName = [[NSString alloc] initWithBytes:descriptor->group_name length:length encoding:NSUTF8StringEncoding];

                        length = strnlen((const char *)descriptor->serial_number, AVB17221AEMNameLength);
                        NSString *serialNumber = [[NSString alloc] initWithBytes:descriptor->serial_number length:length encoding:NSUTF8StringEncoding];

                        //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                        dispatch_async(dispatch_get_main_queue(), ^{
                            self.entityName = entityName;
                            self.firmwareVersion = firmwareVersion;
                            self.groupName = groupName;
                            self.serialNumber = serialNumber;
                        });

                        _currentConfiguration = OSSwapBigToHostInt16(descriptor->current_configuration);

                        //If the ADP entity info includes the interface index of the AVB Interface than go and directly read that now (no need to parse everything to find it)
                        if(self.adpEntity.entityCapabilities & AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValid)
                        {
                            [self readInterfaceDescriptor:self.adpEntity.interfaceIndex inConfiguration:_currentConfiguration];
                        }

                        //Read the configuration descriptor and pull out more info
                        [self readConfigurationDescriptor:_currentConfiguration];
                    }
                }
                else
                {
                    NSLog(@"readEntityDescriptor Failed to read descriptor type 0x%04hx from entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeEntity, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readEntityDescriptor Failed to read descriptor type 0x%04hx from entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeEntity, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Read an AEM CONFIGURATION descriptor from the Entity
- (void)readConfigurationDescriptor:(uint16_t)configurationIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //Construct the read decriptor command
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = OSSwapHostToBigConstInt16(0);
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeConfiguration);
    readDescriptorCommand.descriptor_index = OSSwapHostToBigInt16(configurationIndex);

    //Construct the AECP AEM Command Message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1. This is a 2 stage check because it is variable length
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMConfigurationDescriptorFields)))
                    {
                        AVB17221AEMConfigurationDescriptorFields *descriptor = (AVB17221AEMConfigurationDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        uint16_t count = OSSwapBigToHostInt16(descriptor->descriptor_counts_count);

                        //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                        if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMConfigurationDescriptorFields) + (count * sizeof(AVB17221AEMDescriptorCountsCount))))
                        {
                            AVB17221AEMDescriptorCountsCount *descriptorCounts = (AVB17221AEMDescriptorCountsCount *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMConfigurationDescriptorFields));

                            uint16_t index;
                            for(index = 0; index < count; index++)
                            {
                                AVB17221AEMDescriptorType descriptorType = OSSwapBigToHostInt16(descriptorCounts[index].descriptor_type);
                                uint16_t descriptorCount = OSSwapBigToHostInt16(descriptorCounts[index].count);
                                uint16_t descriptorIndex;

                                switch(descriptorType)
                                {
                                    case AVB17221AEMDescriptorTypeAVBInterface:
                                        if(self.adpEntity.entityCapabilities & AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValid)
                                        {
                                            //We have already executed the read so no need to do anything
                                        }
                                        else
                                        {
                                            //We don't know which one it is so we have to read all of them
                                            for(descriptorIndex = 0; descriptorIndex < descriptorCount; descriptorIndex++)
                                            {
                                                [self readInterfaceDescriptor:descriptorIndex inConfiguration:configurationIndex];
                                            }
                                        }
                                        break;
                                    case AVB17221AEMDescriptorTypeMemoryObject:
                                        //Read all of the memory object descriptors looking for the manufacturer and entity images
                                        for(descriptorIndex = 0; descriptorIndex < descriptorCount; descriptorIndex++)
                                        {
                                            [self readMemoryObjectDescriptor:descriptorIndex inConfiguration:configurationIndex];
                                        }
                                        break;

                                    case AVB17221AEMDescriptorTypeLocale:
                                        //Look for the locales so we can get the localized strings
                                        if(1 == descriptorCount)
                                        {
                                            //There is only one locale so the choice is easy. Go ahead and read it
                                            _hasLocale = YES;
                                            _localeIndex = 0;
                                            [self readLocaleDescriptor:_localeIndex inConfiguration:configurationIndex];
                                        }
                                        else
                                        {
                                            //Loop through all of the Locale descriptors building up a list of locale identifiers
                                            //When it reaches the end it will find the best one compared with the users languages
                                            _localeCount = descriptorCount;
                                            _possibleLocales = [NSMutableDictionary dictionary];
                                            for(descriptorIndex = 0; descriptorIndex < descriptorCount; descriptorIndex++)
                                            {
                                                [self readLocaleDescriptor:descriptorIndex inConfiguration:configurationIndex];
                                            }
                                        }
                                        break;
                                    default:
                                        //Don't do anything with it
                                        break;
                                }
                            }
                        }
                    }
                }
                else
                {
                    NSLog(@"readConfigurationDescriptor: Failed to read descriptor type 0x%04hx id 0x%04hxfrom entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeConfiguration, configurationIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readConfigurationDescriptor: Failed to read descriptor type 0x%04hx id 0x%04hxfrom entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeConfiguration, configurationIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Read an AEM AVB_INTERFACE descriptor from the Entity
- (void)readInterfaceDescriptor:(uint16_t)interfaceIndex inConfiguration:(uint16_t)configurationIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //Construct the read descriptor command
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = OSSwapHostToBigInt16(configurationIndex);
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeAVBInterface);
    readDescriptorCommand.descriptor_index = OSSwapHostToBigInt16(interfaceIndex);

    //Construct the AECP AEM Command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMAVBInterfaceDescriptorFields)))
                    {
                        AVB17221AEMAVBInterfaceDescriptorFields *descriptor = (AVB17221AEMAVBInterfaceDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        BOOL thisIsIt = NO;

                        //If the ADP entity info includes the interface index and we just read that interface then this is it
                        if(self.adpEntity.entityCapabilities & AVB17221ADPEntityCapabilitiesAEMInterfaceIndexValid)
                        {
                            if(self.adpEntity.interfaceIndex == interfaceIndex)
                            {
                                thisIsIt = YES;
                            }
                        }
                        else
                        {
                            //if this is the interface with the same MAC address as where we have been sending messages then this is it
                            AVBMACAddress *firstMac = self.adpEntity.macAddresses.firstObject;

                            if(firstMac && 0 == bcmp(firstMac.bytes, descriptor->mac_address, AVBMACAddressSize))
                            {
                                thisIsIt = YES;
                            }
                        }

                        //If this is it then pull out the info
                        if(thisIsIt)
                        {
                            uint64_t clockIdentity = OSSwapBigToHostInt64(descriptor->clock_identity);
                            uint16_t portNumber = OSSwapBigToHostInt16(descriptor->port_number);

                            //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                            dispatch_async(dispatch_get_main_queue(), ^{
                                self.clockIdentity = clockIdentity;
                                self.portNumber = portNumber;
                            });

                            _hasInterface = YES;
                            _interfaceIndex = interfaceIndex;

                            [self getGPTPPathForInterfaceIndex:interfaceIndex];
                            [self getAVBInfoForInterfaceIndex:interfaceIndex];
                        }
                    }
                }
                else
                {
                    NSLog(@"readInterfaceDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeAVBInterface, interfaceIndex, configurationIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readInterfaceDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeAVBInterface, interfaceIndex, configurationIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Read an AEM MEMORY_OBJCT descriptor from the Entity
- (void)readMemoryObjectDescriptor:(uint16_t)memoryObjectIndex inConfiguration:(uint16_t)configurationIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //If the ADP entity info includes the interface index
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = OSSwapHostToBigInt16(configurationIndex);
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeMemoryObject);
    readDescriptorCommand.descriptor_index = OSSwapHostToBigInt16(memoryObjectIndex);

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMMemoryObjectDescriptorFields)))
                    {
                        AVB17221AEMMemoryObjectDescriptorFields *descriptor = (AVB17221AEMMemoryObjectDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        AVB17221AEMMemoryObjectType memoryObjectType = OSSwapBigToHostInt16(descriptor->memory_object_type);

                        uint64_t address = OSSwapBigToHostInt64(descriptor->start_address);
                        uint64_t length = OSSwapBigToHostInt64(descriptor->length);

                        if(AVB17221AEMMemoryObjectTypeManufacturerPNG == memoryObjectType || AVB17221AEMMemoryObjectTypeManufacturerSVG == memoryObjectType)
                        {
                            [self addressAccessReadAtAddress:address ofLength:length appendToData:[NSMutableData data] withCompletion:^(NSData *data) {
                                //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                                dispatch_async(dispatch_get_main_queue(), ^{
                                    self.vendorLogo = [[NSImage alloc] initWithData:data];
                                });
                            }];
                        }
                        else if(AVB17221AEMMemoryObjectTypeEntityPNG == memoryObjectType || AVB17221AEMMemoryObjectTypeEntitySVG == memoryObjectType)
                        {
                            [self addressAccessReadAtAddress:address ofLength:length appendToData:[NSMutableData data] withCompletion:^(NSData *data) {
                                //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                                dispatch_async(dispatch_get_main_queue(), ^{
                                    self.entityLogo = [[NSImage alloc] initWithData:data];
                                });
                            }];
                        }
                    }
                }
                else
                {
                    NSLog(@"readMemoryObjectDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeMemoryObject, memoryObjectIndex, configurationIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readMemoryObjectDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeMemoryObject, memoryObjectIndex, configurationIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Read an AEM LOCALE descriptor from the Entity
- (void)readLocaleDescriptor:(uint16_t)localeIndex inConfiguration:(uint16_t)configurationIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //If the ADP entity info includes the interface index
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = OSSwapHostToBigInt16(configurationIndex);
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeLocale);
    readDescriptorCommand.descriptor_index = OSSwapHostToBigInt16(localeIndex);

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMLocaleDescriptorFields)))
                    {
                        AVB17221AEMLocaleDescriptorFields *descriptor = (AVB17221AEMLocaleDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        //If we have identified the right locale (and this is it)
                        if(_hasLocale && localeIndex == _localeIndex)
                        {
                            //Get the base strings entry and then read the strings descriptor(s) to get the vendor and model name strings
                            _localeBaseStrings = OSSwapBigToHostInt16(descriptor->base_strings);

                            [self readStringsDescriptor:_localeBaseStrings+_vendorStringsOffset inConfiguration:configurationIndex];

                            //If the vendor and model name strings are in different STRINGS descriptors then read the second one
                            if(_vendorStringsOffset != _modelStringsOffset)
                            {
                                [self readStringsDescriptor:_localeBaseStrings+_modelStringsOffset inConfiguration:configurationIndex];
                            }
                        }
                        //If we haven't identified the locale yet, add this ones identifier to the list and process (if the last one)
                        else if(!_hasLocale)
                        {
                            NSUInteger length = strnlen((const char *)descriptor->locale_identifier, AVB17221AEMNameLength);
                            NSString *localeIdentifier = [[NSString alloc] initWithBytes:descriptor->locale_identifier length:length encoding:NSUTF8StringEncoding];
                            dispatch_async(_aecpQueue, ^{
                                [_possibleLocales setObject:[NSNumber numberWithUnsignedShort:localeIndex] forKey:localeIdentifier];

                                //Did we just insert the last one?
                                if(_localeCount == _possibleLocales.count)
                                {
                                    //Yes so look up which one we should use
                                    NSArray *userLanguages = [NSLocale preferredLanguages];

                                    if(userLanguages.count > 0)
                                    {
                                        //Do we have an exact match for the first language?
                                        if([_possibleLocales objectForKey:[userLanguages objectAtIndex:0]])
                                        {
                                            //Yes use it
                                            _hasLocale = YES;
                                            _localeIndex = [[_possibleLocales objectForKey:[userLanguages objectAtIndex:0]] unsignedShortValue];

                                            //Now that we have the known one re-read it so we will go through the other path and read the strings.
                                            [self readLocaleDescriptor:_localeIndex inConfiguration:configurationIndex];
                                        }
                                        else
                                        {
                                            //No so we have to find the best option
                                            for(NSString *language in userLanguages)
                                            {
                                                if([_possibleLocales objectForKey:language])
                                                {
                                                    //Yes use it
                                                    _hasLocale = YES;
                                                    _localeIndex = [[_possibleLocales objectForKey:language] unsignedShortValue];

                                                    //Now that we have the known one re-read it so we will go through the other path and read the strings.
                                                    [self readLocaleDescriptor:_localeIndex inConfiguration:configurationIndex];

                                                    break;
                                                }
                                            }

                                            if(!_hasLocale)
                                            {
                                                //We didn't find an exact match, this should go through and find the best match between the two (which may be a language match plus or minus a region)

                                                //Use the first one for now
                                                _hasLocale = YES;
                                                _localeIndex = 0;
                                                [self readLocaleDescriptor:_localeIndex inConfiguration:configurationIndex];
                                            }
                                        }
                                    }
                                }
                            });
                        }
                    }
                }
                else
                {
                    NSLog(@"readLocaleDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeLocale, localeIndex, configurationIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readLocaleDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeLocale, localeIndex, configurationIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Read an AEM STRINGS descriptor from the Entity
- (void)readStringsDescriptor:(uint16_t)stringsIndex inConfiguration:(uint16_t)configurationIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //If the ADP entity info includes the interface index
    AVB17221AEMCommandReadDescriptorFields readDescriptorCommand;

    bzero(&readDescriptorCommand, sizeof(AVB17221AEMCommandReadDescriptorFields));

    readDescriptorCommand.configuration = OSSwapHostToBigInt16(configurationIndex);
    readDescriptorCommand.descriptor_type = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeStrings);
    readDescriptorCommand.descriptor_index = OSSwapHostToBigInt16(stringsIndex);

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeReadDescriptor;

    message.commandSpecificData = [NSData dataWithBytes:&readDescriptorCommand length:sizeof(AVB17221AEMCommandReadDescriptorFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned descriptor is long enough then parse out the info. We allow it to be longer so that it will work with future versions of 1722.1
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseReadDescriptorFields) + sizeof(AVB17221AEMStringsDescriptorFields)))
                    {
                        AVB17221AEMStringsDescriptorFields *descriptor = (AVB17221AEMStringsDescriptorFields *)(payload + sizeof(AVB17221AEMResponseReadDescriptorFields));

                        //Is this the descriptor with the vendor name string?
                        if(stringsIndex == (_localeBaseStrings + _vendorStringsOffset))
                        {
                            //Yes so read the right string entry and set the property
                            uint8_t *stringBase = descriptor->string0 + (_vendorStringIndex * AVB17221AEMNameLength);

                            NSUInteger length = strnlen((const char *)stringBase, AVB17221AEMNameLength);
                            NSString *vendorName = [[NSString alloc] initWithBytes:stringBase length:length encoding:NSUTF8StringEncoding];

                            //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                            dispatch_async(dispatch_get_main_queue(), ^{
                                self.vendorName = vendorName;
                            });
                        }

                        //Is this the descriptor with the model name string?
                        if(stringsIndex == (_localeBaseStrings + _modelStringsOffset))
                        {
                            //Yes so read the right string entry and set the property
                            uint8_t *stringBase = descriptor->string0 + (_modelStringIndex * AVB17221AEMNameLength);

                            NSUInteger length = strnlen((const char *)stringBase, AVB17221AEMNameLength);
                            NSString *modelName = [[NSString alloc] initWithBytes:stringBase length:length encoding:NSUTF8StringEncoding];
                            //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                            dispatch_async(dispatch_get_main_queue(), ^{
                                self.modelName = modelName;
                            });
                        }
                    }
                }
                else
                {
                    NSLog(@"readStringsDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with message status 0x%02hhx\n", (uint16_t)AVB17221AEMDescriptorTypeStrings, stringsIndex, configurationIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"readStringsDescriptor:inConfiguration: Failed to read descriptor type 0x%04hx id 0x%04hx config 0x%04hx from entity 0x%016llx with error 0x%08x\n", (uint16_t)AVB17221AEMDescriptorTypeStrings, stringsIndex, configurationIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Send the GET_AS_PATH AECP AEM Command to the entity to get the IEEE 802.1AS (gPTP) path
- (void)getGPTPPathForInterfaceIndex:(uint16_t)interfaceIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //Construct the get as path command
    AVB17221AEMGetASPathFields asPathCommand;

    bzero(&asPathCommand, sizeof(AVB17221AEMGetASPathFields));

    asPathCommand.count = 0;
    asPathCommand.descriptor_index = OSSwapHostToBigInt16(interfaceIndex);

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeGetASPath;

    message.commandSpecificData = [NSData dataWithBytes:&asPathCommand length:sizeof(AVB17221AEMGetASPathFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned response is long enough then parse out the info.                  if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMGetASPathFields)))
                    {
                        AVB17221AEMGetASPathFields *asPathResponse = (AVB17221AEMGetASPathFields *)payload;

                        uint16_t count = OSSwapBigToHostInt16(asPathResponse->count);

                        //The response is variable length so make sure that it is long enough for what it says that it contains
                        if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMGetASPathFields) + (count * sizeof(uint64_t))))
                        {
                            uint64_t *path = (uint64_t *)(payload + sizeof(AVB17221AEMGetASPathFields));

                            NSMutableArray *gPTPPath = [NSMutableArray array];

                            for(uint16_t index = 0; index < count; index++)
                            {
                                [gPTPPath addObject:[NSNumber numberWithUnsignedLongLong:OSSwapBigToHostInt64(path[index])]];
                            }

                            //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                            dispatch_async(dispatch_get_main_queue(), ^{
                                self.gPTPPath = gPTPPath;
                            });
                        }
                    }
                }
                else
                {
                    NSLog(@"getGPTPPathForInterfaceIndex: Failed to execute for index 0x%04hx of entity 0x%016llx with message status 0x%02hhx\n", interfaceIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"getGPTPPathForInterfaceIndex: Failed to execute for index 0x%04hx of entity 0x%016llx with error 0x%08x\n", interfaceIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Send the GET_AVB_INFO AECP AEM Command to the Entity to get AVB info for the interface
- (void)getAVBInfoForInterfaceIndex:(uint16_t)interfaceIndex
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    //Construct the get avb info command
    AVB17221AEMCommandGetAVBInfoFields avbInfoCommand;

    bzero(&avbInfoCommand, sizeof(AVB17221AEMCommandGetAVBInfoFields));

    avbInfoCommand.descriptor_type  = OSSwapHostToBigConstInt16(AVB17221AEMDescriptorTypeAVBInterface);
    avbInfoCommand.descriptor_index = OSSwapHostToBigInt16(interfaceIndex);

    //Create the AECP AEM command message
    AVB17221AECPAEMMessage *message = [AVB17221AECPAEMMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;
    message.commandType = AVB17221AEMCommandTypeGetAVBInfo;

    message.commandSpecificData = [NSData dataWithBytes:&avbInfoCommand length:sizeof(AVB17221AEMCommandGetAVBInfoFields)];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AEM Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == (IOReturn)error.code)
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAEMMessage *aemMessage = (AVB17221AECPAEMMessage *)response;
                    uint8_t *payload = (uint8_t *)[aemMessage.commandSpecificData bytes];

                    //If the returned response is long enough then parse out the info.
                    if(aemMessage.commandSpecificData.length >= (sizeof(AVB17221AEMResponseGetAVBInfoFields)))
                    {
                        AVB17221AEMResponseGetAVBInfoFields *avbInfoResponse = (AVB17221AEMResponseGetAVBInfoFields *)payload;

                        uint64_t grandmasterID = OSSwapBigToHostInt64(avbInfoResponse->gptp_grandmaster_id);

                        //Property updates must be performed on the main thread since they update the UI through Cocoa Bindings
                        dispatch_async(dispatch_get_main_queue(), ^{
                            self.gPTPGrandMaster = grandmasterID;
                        });
                    }
                }
                else
                {
                    NSLog(@"getAVBInfoForInterfaceIndex: Failed to execute for index 0x%04hx of entity 0x%016llx with message status 0x%02hhx\n", interfaceIndex, self.adpEntity.entityID, (uint8_t)response.status);
                }
            }
            else
            {
                NSLog(@"getAVBInfoForInterfaceIndex: Failed to execute for index 0x%04hx of entity 0x%016llx with error 0x%08x\n", interfaceIndex, self.adpEntity.entityID, (uint32_t)error.code);
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

typedef void (^memoryCompletion)(NSData *data);

//This method uses the AECP AA protocol to read the contents of a memory object from the Entity
//It recusively calls itself to read the block of memory segment by segment until it is done
- (void)addressAccessReadAtAddress:(uint64_t)address ofLength:(uint64_t)length appendToData:(NSMutableData *)data withCompletion:(memoryCompletion)completion
{
    ANBAppDelegate *delegate = (ANBAppDelegate *)[NSApp delegate];

    uint64_t segmentLength = (length > MAX_SEGMENT_LENGTH) ? MAX_SEGMENT_LENGTH : length;

    //Create the AECP AA command message
    AVB17221AECPAddressAccessMessage *message = [AVB17221AECPAddressAccessMessage commandMessage];

    message.targetEntityID = self.adpEntity.entityID;
    message.status = AVB17221AECPStatusSuccess;
    message.controllerEntityID = delegate.controllerEntityID;

    //Create the AECP AA read TLV with the appropriate info for this segment
    AVB17221AECPAddressAccessTLV *tlv = [[AVB17221AECPAddressAccessTLV alloc] init];

    tlv.mode = AVB17221AECPAddressAccessTLVModeRead;
    tlv.address = address;
    NSMutableData *readData = [NSMutableData data];
    [readData setLength:segmentLength];
    tlv.memoryData = readData;

    message.tlvs = @[tlv];

    //Dispatch async to the AECP serialization and limiting queue
    dispatch_async(_aecpQueue, ^{
        //Take a semaphore count so that we will limit the inflight
        dispatch_semaphore_wait(_aecpLimiter, DISPATCH_TIME_FOREVER);

        //Send the AECP AA Command message to the entity. The response is handled in the completion handler block
        if(![self.interface.aecp sendCommand:message toMACAddress:self.adpEntity.macAddresses.firstObject completionHandler:^(NSError *error, AVB17221AECPMessage *response){
            if(kIOReturnSuccess == [error code])
            {
                if(AVB17221AECPStatusSuccess == response.status)
                {
                    AVB17221AECPAddressAccessMessage *aaResponse = (AVB17221AECPAddressAccessMessage *)response;

                    if(1 == aaResponse.tlvs.count)
                    {
                        AVB17221AECPAddressAccessTLV *tlv = [aaResponse.tlvs objectAtIndex:0];

                        uint64_t nextLength = length - segmentLength;
                        uint64_t nextAddress = address + segmentLength;

                        [data appendData:tlv.memoryData];

                        //if we have reached the end call the completion handler otherwise read the next segment
                        if(0 == nextLength)
                        {
                            completion(data);
                        }
                        else
                        {
                            [self addressAccessReadAtAddress:nextAddress ofLength:nextLength appendToData:data withCompletion:completion];
                        }
                    }
                }
                else
                {
                    //Errored out, drop the whole transaction and don't call completion
                }
            }
            else
            {
                //Errored out, drop the whole transaction and don't call completion
            }
            dispatch_semaphore_signal(_aecpLimiter);
        }])
        {
            //An error occured trying to send the message (completion handler won't fire) so clean up the limit
            dispatch_semaphore_signal(_aecpLimiter);
        }
    });
}

//Called from the UI refresh button (via buttons target binding) to refresh the gPTP and AVB info from the device (does not reparse descriptors)
- (void)refreshInfo
{
    if(_hasInterface)
    {
        [self getGPTPPathForInterfaceIndex:_interfaceIndex];
        [self getAVBInfoForInterfaceIndex:_interfaceIndex];
    }
}

@end
```

[Next](AVBNetworkBrowser-ANBEUI64Transformer.h.md)[Previous](AVBNetworkBrowser-ANBAVDECCEntity.h.md)


---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/AVBNetworkBrowser_AVBTypes_h.html
archived_at: '2026-07-26T19:54:13.956845Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-main.m.md)[Previous](AVBNetworkBrowser-ANBWindowController.m.md)

# AVBNetworkBrowser/AVBTypes.h

```c
/*

     File: AVBTypes.h
 Abstract: Constants and Types for the IEEE Std. 1722.1-2013 descriptors and commands.
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

#ifndef AVBNetworkBrowser_AVBTypes_h
#define AVBNetworkBrowser_AVBTypes_h

#define AVB17221AEMNameLength 64

typedef NS_ENUM(uint16_t, AVB17221AEMDescriptorType)
{
    AVB17221AEMDescriptorTypeEntity                 = 0x0000,
    AVB17221AEMDescriptorTypeConfiguration          = 0x0001,
    AVB17221AEMDescriptorTypeAudioUnit              = 0x0002,
    AVB17221AEMDescriptorTypeVideoUnit              = 0x0003,
    AVB17221AEMDescriptorTypeSensorUnit             = 0x0004,
    AVB17221AEMDescriptorTypeStreamInput            = 0x0005,
    AVB17221AEMDescriptorTypeStreamOutput           = 0x0006,
    AVB17221AEMDescriptorTypeJackInput              = 0x0007,
    AVB17221AEMDescriptorTypeJackOutput             = 0x0008,
    AVB17221AEMDescriptorTypeAVBInterface           = 0x0009,
    AVB17221AEMDescriptorTypeClockSource            = 0x000a,
    AVB17221AEMDescriptorTypeMemoryObject           = 0x000b,
    AVB17221AEMDescriptorTypeLocale                 = 0x000c,
    AVB17221AEMDescriptorTypeStrings                = 0x000d,
    AVB17221AEMDescriptorTypeStreamPortInput        = 0x000e,
    AVB17221AEMDescriptorTypeStreamPortOutput       = 0x000f,
    AVB17221AEMDescriptorTypeExternalPortInput      = 0x0010,
    AVB17221AEMDescriptorTypeExternalPortOutput     = 0x0011,
    AVB17221AEMDescriptorTypeInternalPortInput      = 0x0012,
    AVB17221AEMDescriptorTypeInternalPortOutput     = 0x0013,
    AVB17221AEMDescriptorTypeAudioCluster           = 0x0014,
    AVB17221AEMDescriptorTypeVideoCluster           = 0x0015,
    AVB17221AEMDescriptorTypeSensorCluster          = 0x0016,
    AVB17221AEMDescriptorTypeAudioMap               = 0x0017,
    AVB17221AEMDescriptorTypeVideoMap               = 0x0018,
    AVB17221AEMDescriptorTypeSensorMap              = 0x0019,
    AVB17221AEMDescriptorTypeControl                = 0x001a,
    AVB17221AEMDescriptorTypeSignalSelector         = 0x001b,
    AVB17221AEMDescriptorTypeMixer                  = 0x001c,
    AVB17221AEMDescriptorTypeMatrix                 = 0x001d,
    AVB17221AEMDescriptorTypeMatrixSignal           = 0x001e,
    AVB17221AEMDescriptorTypeSignalSplitter         = 0x001f,
    AVB17221AEMDescriptorTypeSignalCombiner         = 0x0020,
    AVB17221AEMDescriptorTypeSignalDemultiplexer    = 0x0021,
    AVB17221AEMDescriptorTypeSignalMultiplexer      = 0x0022,
    AVB17221AEMDescriptorTypeSignalTranscoder       = 0x0023,
    AVB17221AEMDescriptorTypeClockDomain            = 0x0024,
    AVB17221AEMDescriptorTypeControlBlock           = 0x0025,
    AVB17221AEMDescriptorTypeInvalid                = 0xffff,
};

typedef NS_ENUM(uint16_t, AVB17221AEMMemoryObjectType)
{
    AVB17221AEMMemoryObjectTypeFirmwareImage        = 0x0000,
    AVB17221AEMMemoryObjectTypeVendorSpecific       = 0x0001,
    AVB17221AEMMemoryObjectTypeCrashDump            = 0x0002,
    AVB17221AEMMemoryObjectTypeLog                  = 0x0003,
    AVB17221AEMMemoryObjectTypeAutostartSettings    = 0x0004,
    AVB17221AEMMemoryObjectTypeSnapshotSettings     = 0x0005,
    AVB17221AEMMemoryObjectTypeManufacturerSVG      = 0x0006,
    AVB17221AEMMemoryObjectTypeEntitySVG            = 0x0007,
    AVB17221AEMMemoryObjectTypeGenericSVG           = 0x0008,
    AVB17221AEMMemoryObjectTypeManufacturerPNG      = 0x0009,
    AVB17221AEMMemoryObjectTypeEntityPNG            = 0x000a,
    AVB17221AEMMemoryObjectTypeGenericPNG           = 0x000b,
    AVB17221AEMMemoryObjectTypeManufacturerDAE      = 0x000c,
    AVB17221AEMMemoryObjectTypeEntityDAE            = 0x000d,
    AVB17221AEMMemoryObjectTypeGenericDAE           = 0x000e,
};

#pragma mark Commands

typedef struct
{
    uint16_t configuration;
    uint16_t reserved;
    uint16_t descriptor_type;
    uint16_t descriptor_index;
} __attribute__((__packed__)) AVB17221AEMCommandReadDescriptorFields;

typedef struct
{
    uint16_t configuration;
    uint16_t reserved;
} __attribute__((__packed__)) AVB17221AEMResponseReadDescriptorFields;

typedef struct
{
    uint16_t descriptor_index;
    uint16_t count;
} __attribute__((__packed__)) AVB17221AEMGetASPathFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
} __attribute__((__packed__)) AVB17221AEMCommandGetAVBInfoFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint64_t gptp_grandmaster_id;
    uint32_t propagation_delay;
    uint8_t gptp_domain_number;
    uint8_t flags;
    uint16_t msrp_mappings_count;
} __attribute__((__packed__)) AVB17221AEMResponseGetAVBInfoFields;

#pragma mark Descriptors

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint64_t entity_id;
    uint64_t entity_model_id;
    uint32_t entity_capabilities;
    uint16_t talker_stream_sources;
    uint16_t talker_capabilities;
    uint16_t listener_stream_sinks;
    uint16_t listener_capabilities;
    uint32_t controller_capabilities;
    uint32_t available_index;
    uint64_t association_id;
    uint8_t entity_name[AVB17221AEMNameLength];
    uint16_t vendor_name_string;
    uint16_t model_name_string;
    uint8_t firmware_version[AVB17221AEMNameLength];
    uint8_t group_name[AVB17221AEMNameLength];
    uint8_t serial_number[AVB17221AEMNameLength];
    uint16_t configurations_count;
    uint16_t current_configuration;
} __attribute__((__packed__)) AVB17221AEMEntityDescriptorFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint8_t object_name[AVB17221AEMNameLength];
    uint16_t localized_description;
    uint16_t descriptor_counts_count;
    uint16_t descriptor_counts_offset;
} __attribute__((__packed__)) AVB17221AEMConfigurationDescriptorFields;

#define AVB17221AEMConfigurationDescriptorCountsOffset  (sizeof(AVB17221AEMConfigurationDescriptorFields))

typedef struct
{
    uint16_t descriptor_type;
    uint16_t count;
} __attribute__((__packed__)) AVB17221AEMDescriptorCountsCount;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint8_t object_name[AVB17221AEMNameLength];
    uint16_t localized_description;
    uint8_t mac_address[AVBMACAddressSize];
    uint16_t interface_flags;
    uint64_t clock_identity;
    uint8_t priority1;
    uint8_t clock_class;
    uint16_t offset_scaled_log_variance;
    uint8_t clock_accuracy;
    uint8_t priority2;
    uint8_t domain_number;
    int8_t log_sync_interval;
    int8_t log_announce_interval;
    int8_t log_pdelay_interval;
    uint16_t port_number;
} __attribute__((__packed__)) AVB17221AEMAVBInterfaceDescriptorFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint8_t locale_identifier[AVB17221AEMNameLength];
    uint16_t number_of_strings;
    uint16_t base_strings;
} __attribute__((__packed__)) AVB17221AEMLocaleDescriptorFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint8_t string0[AVB17221AEMNameLength];
    uint8_t string1[AVB17221AEMNameLength];
    uint8_t string2[AVB17221AEMNameLength];
    uint8_t string3[AVB17221AEMNameLength];
    uint8_t string4[AVB17221AEMNameLength];
    uint8_t string5[AVB17221AEMNameLength];
    uint8_t string6[AVB17221AEMNameLength];
} __attribute__((__packed__)) AVB17221AEMStringsDescriptorFields;

typedef struct
{
    uint16_t descriptor_type;
    uint16_t descriptor_index;
    uint8_t object_name[AVB17221AEMNameLength];
    uint16_t localized_description;
    uint16_t memory_object_type;
    uint16_t target_descriptor_type;
    uint16_t target_descriptor_index;
    uint64_t start_address;
    uint64_t maximum_length;
    uint64_t length;
} __attribute__((__packed__)) AVB17221AEMMemoryObjectDescriptorFields;

#endif
```

[Next](AVBNetworkBrowser-main.m.md)[Previous](AVBNetworkBrowser-ANBWindowController.m.md)


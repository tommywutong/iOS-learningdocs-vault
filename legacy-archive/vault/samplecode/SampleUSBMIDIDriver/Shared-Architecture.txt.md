---
title: SampleUSBMIDIDriver
apple_id: DTS40008412
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreMIDI
published: '2009-03-18'
source_url: https://developer.apple.com/library/archive/samplecode/SampleUSBMIDIDriver/Listings/Shared_Architecture_txt.html
archived_at: '2026-07-18T03:23:05.858788Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleUSBMIDIDriver](SampleUSBMIDIDriver.md)


[Next](Shared-IOServiceClient.cpp.md)[Previous](SampleUSBMIDI.h.md)

# Shared/Architecture.txt

```
Class hierarchies
-----------------

MIDIDriver
    USBMIDIDriverBase
        USBVendorMIDIDriver
            CompanyA_USBMIDIDriver
            CompanyB_USBMIDIDriver
            etc.
        USBMIDIClassDriver
    SerialMIDIDriverBase *
        StandardSerialMIDIDriver
        CompanyC_SerialMIDIDriver
        CompanyD_SerialMIDIDriver
        etc.

MIDIDriverDevice  (was: InterfaceState)
    USBMIDIDevice
    SerialMIDIDevice *

IOServiceManager
    USBDeviceManager
        USBMIDIDeviceManager
    USBInterfaceManager
        USBMIDIClassInterfaceManager
    SerialDeviceManager *

* doesn't exist yet

Vendor-specific drivers not supplied by Apple.



Object ownership hierarchy
--------------------------
USBVendorMIDIDriver
    USBMIDIDeviceManager
        array of USBMIDIDevice

with ALL vendor-specific overrides implemented in the driver class
although the device may also be subclassed in special cases
```

[Next](Shared-IOServiceClient.cpp.md)[Previous](SampleUSBMIDI.h.md)


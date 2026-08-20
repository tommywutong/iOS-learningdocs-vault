---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/04_Matching/MS_Matching.html
archived_at: '2026-07-15T07:31:32.805817Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Mass Storage Device Driver Programming Guide](Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md)


[Next](Developing%20a%20Universal%20Binary.md)[Previous](Mass%20Storage%20Device%20Compliance.md)

# Mass Storage Driver Matching and Loading

Before a mass storage device can be used, the I/O Kit must find and load several drivers for it. In the transport driver layer, the required drivers are a protocol services driver and a logical unit driver. The only required driver in the device services layer is the generic block storage driver but if there is media present in the device, there may be partition and filter-scheme drivers, as well. Like all I/O Kit drivers, these drivers must declare what devices they are suited to drive by placing device-specific or device type-specific information in special dictionaries called personalities. In a process called driver matching, the I/O Kit compares this information to values reported by the device to find the most suitable driver.

This chapter first describes the driver matching process in general and then focuses on the matching semantics of the protocol services drivers, the logical unit drivers, and the optional filter-scheme drivers.

The I/O Kit finds and loads device drivers in a three-stage matching process that excludes unsuitable drivers from the pool of candidates until one or more eligible drivers are left. The most eligible of the remaining drivers is then given the first opportunity to drive the device.

This process makes use of matching dictionaries that are in every driver’s information property list. Each dictionary, consisting of XML key-value pairs, specifies a personality of the driver, which declares its suitability for a particular device or device type. A driver may have more than one personality if it can drive different devices or device types.

This section presents a brief overview of driver personalities and matching (for a more in-depth description of these topics, see _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.) The subsequent sections, [Protocol Services Driver Matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskjjjeuera), [Logical Unit Driver Matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskgjbdeery), and [Filter-Scheme Driver Matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbegskcifbuosa) describe how this process is implemented by specific mass storage drivers.

Every device driver must declare one or more personalities that define the types of devices it can support. These personalities are in the form of XML dictionaries contained in the information property list (`Info.plist` file) in the driver’s kernel extension (KEXT) bundle.

Each entry in the matching dictionary is made up of a key-value pair in which the XML tags `<key>` and `</key>` enclose the key and the associated value is enclosed by XML tags that indicate its data type.

At minimum, all driver personalities contain the following two keys:

- The `IOClass` key declares the name of the class the I/O Kit instantiates when probing. For example,

```
<key>IOClass</key>
<string>IOATAPIProtocolTransport</string>
```

  tells the I/O Kit to instantiate the `IOATAPIProtocolTransport` driver when probing the device for this personality.
- The `IOProviderClass` key declares the name of the nub class a driver personality attaches to. For example,

```
<key>IOProviderClass</key>
<string>IOFireWireSBP2LUN</string>
```

  tells the I/O Kit that this driver personality attaches to an `IOFireWireSBP2LUN` nub.

  The provider class defines the family-specific matching keys used in the passive matching step, described in [Driver Matching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskdjfbeiqy).

Most driver personalities also contain the `IOProbeScore` key, which declares the initial probe score for a personality. For example,

```
<key>IOProbeScore</key>
<integer>5000</integer>
```

declares a base probe score of 5000, which can be increased or decreased during the matching process, reflecting the driver’s suitability for the device.

Driver matching occurs when a device is discovered. Each candidate driver has a probe score that reflects how well suited it is to drive the device. During the matching process, the family can increase the probe score with each property match. The driver with the highest probe score is given the first opportunity to drive the device.

The driver matching process consists of three phases:

1. In the class matching phase, the I/O Kit eliminates drivers of the wrong class. For example, the I/O Kit eliminates drivers that descend from a SCSI class when searching for a USB driver.
2. In the passive matching phase, the I/O Kit examines the personality of the driver for family-specific properties. In the SCSI Architecture Model family, the more matching properties found, the higher the driver’s probe score. For example, a driver that matches on both vendor name and product name has a higher probe score than a driver that matches only on vendor name. The Storage family, on the other hand, does not influence a driver’s probe score during matching.

   Often this step is sufficient to determine if a driver is suitable for a device. If there is no family-specific matching, however, the next step is automatically invoked.
3. In the active matching phase, the candidate driver is allowed to communicate with the device and verify that it can drive it. The I/O Kit loads the drivers remaining after the passive matching phase and each driver’s `probe` function is called with reference to the device it is being matched against. The `probe` method can examine the device in any way it chooses, as long as it leaves the device in the same state in which it was found.

   For example, a vendor may use certain bits of a property value to signify the presence of a particular device component. A logical unit driver for that device can implement a `probe` method that examines those bits to determine if the component is indeed present.

   Depending on the results of the probe, the driver increases or decreases its probe score to indicate its suitability to drive the device.

The I/O Kit chooses the driver with the highest probe score and starts it. If the driver starts successfully, any remaining driver candidates are discarded. If it is not successful, the driver with the next highest probe score is started and the process continues until a successful driver is found.

When probing, a driver can perform a detailed examination of the device, including, if necessary, memory allocations, but it must leave the device in the same state in which it found it. If a driver starts successfully, it can reuse the memory it allocated in its `probe` method but if it is unsuccessful, it must be sure to deallocate the memory in its `free` method.

When a driver starts, it should call its superclass’s `start` method before doing anything else. If the superclass’s `start` method succeeds, the driver can then perform its initializations or allocations. Because a driver may not be able to perform initializations or allocations safely after it starts, it should perform such tasks in its `start` method. If the driver is unable to complete its tasks, it can notify the I/O Kit and the driver with the next highest probe score starts.

During the building of the mass storage driver stack, objects in the physical interconnect layer discover a mass storage device and publish a nub representing it in the I/O Registry. The I/O Kit finds a protocol services driver by performing driver matching on this nub.

The protocol services drivers rely on matching semantics that are specific to the family of the bus they communicate with. The following sections describe the matching properties and process for each Apple-provided protocol services driver.

As described in [Construction of a Mass Storage Driver Stack](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvbeur2gjjeuuqi), the protocol services driver for a FireWire SBP-2 mass storage device must match on the `IOFireWireSBP2LUN` nub published by the `IOFireWireTarget` object in the physical interconnect layer. The `IOFireWireSBP2LUN` object contains the following seven keys:

- `Command_Set`
- `Command_Set_Spec_ID`
- `Vendor_ID`
- `Command_Set_Revision`
- `IOUnit`
- `Firmware_Revision`
- `Device_Type`

The `IOFireWireTarget` object scans the device’s configuration ROM and fills in the values for these keys. If the device doesn’t declare one or more of these properties in its configuration ROM, the `IOFireWireSPB2LUN` publishes the corresponding key with a zero value.

To match on the `IOFireWireSBP2LUN`, the `IOFireWireSerialBusProtocolTransport` driver personality includes the keys shown in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskki5deera).

__Listing 3-1__  The IOFireWireSerialBusProtocolTransport driver personality dictionary

```
<dict>
    <!-- CFBundleIdentifier denotes the name of the driver in
     -- reverse DNS notation. -->
    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOFireWireSerialBusProtocolTransport</string>

    <!-- Command_Set refers to the organization responsible
     -- for the definition of the command set. -->
    <key>Command_Set</key>
    <integer>66776</integer>

    <!-- Command_Set_Spec_ID specifies the commands
     -- understood by the device. -->
    <key>Command_Set_Spec_ID</key>
    <integer>24734</integer>

    <!-- The name of the class the I/O Kit instantiates
     -- when probing. -->
    <key>IOClass</key>
    <string>IOFireWireSerialBusProtocolTransport</string>

    <!-- The initial probe score for this personality. -->
    <key>IOProbeScore</key>
    <integer>4096</integer>

    <!-- The provider class is the name of the nub class this
     -- driver personality attaches to. -->
    <key>IOProviderClass</key>
    <string>IOFireWireSBP2LUN</string>

    <!-- The next two keys describe which
     -- bus the device is on and whether it is
     -- internal or external.-->
    <key>Physical Interconnect</key>
    <string>FireWire</string>

    <key>Physical Interconnect Location</key>
    <string>External</string>
</dict>
```

A subclass of the `IOFireWireSerialBusProtocolTransport` driver can use more of the seven keys in the `IOFireWireSBP2LUN` object to more narrowly define the device it is suited to drive. It can also examine the property values in its `probe` method to further determine its suitability. For example, a vendor can use some of the bits in a property value to declare the presence of a device component. A driver that needs to determine the presence of this component can examine those bits in its `probe` method. [Listing 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskfiffesqy) shows how this can be done for a subclass of the `IOFireWireSerialBusProtocolTransport` driver.

__Listing 3-2__  Example FireWire protocol services driver probe method


```swift
// This example probe method tests the Firmware_Revision value.
IOService *com_MySoftwareCompany_driver_MyFWProtocolLayerDriver::probe(
                IOService *provider, SInt32 *score )
{
    IOFireWireSBP2LUN *fwSBP2LUN = NULL;
    OSObject *firmwareObject;
    IOService *returnValue = 0;

    // Override probe method inherited from IOFireWireSBP2LUN.
    // Incorporate additional matching based on bits within
    // firmware revision data.

    // Allow superclass first chance at probe
    if ( !IOFireWireSerialBusProtocolTransport::probe( provider, score ) )
        goto ErrorExit;

    fwSBP2LUN = OSDynamicCast( IOFireWireSBP2LUN, provider );
    if ( fwSBP2LUN == NULL )
        goto ErrorExit;

    // Get key from registry that IOFireWireSBP2LUN published
    firmwareObject = provider->getProperty( "Firmware_Revision" );
    if ( firmwareObject )
    {
        OSNumber *firmwareNumberObject;
        UInt32 firmwareValue = 0;

        // Translate the Firmware_Revision property
        // into an OSNumber value for inspection.
        firmwareNumberObject = OSDynamicCast( OSNumber, firmwareObject );
        if ( firmwareNumberObject )
        {
            firmwareValue = firmwareNumberObject->unsigned32BitValue( );
        }

        // Check bits 8 through 23 of the Firmware_Revision value by
        // comparing them with the constants kMyConstant1 and
        // kMyConstant2.
        // These constants represent identification codes and
        // would be defined earlier in the driver's code.
        if ( ( ( ( firmwareValue >> 8 ) & 0x000FFF ) == kMyConstant1 )
        ||
         ( ( ( firmwareValue >> 8 ) & 0x000FFF ) == kMyConstant2 ) )
        {
            IOLog( "%s: Device component detected\n", getName( ) );
            returnValue = this;
        }
    }
ErrorExit:
    return returnValue;
}
```


When a USB mass storage class device is discovered, the USB family abstracts the contents of the device descriptor into an I/O Kit nub object called `IOUSBDevice`. The device descriptor includes information such as the device’s class and subclass, vendor and product numbers, and the number of configurations.

Because USB mass storage class devices are defined as composite class devices, the `AppleUSBComposite` driver matches against the `IOUSBDevice` nub object and sets the first configuration in the device. This causes the USB family to abstract each interface descriptor in the configuration into an `IOUSBInterface` nub object. The `IOUSBMassStorageClass` driver then matches on the mass storage class-compliant interface nub objects.

The Apple-provided `IOUSBMassStorageClass` driver contains six personalities that correspond to the six mass storage subclasses. Each subclass represents the type of command block set the device’s interfaces use. If the device is compliant with the USB mass storage class specification, its interface descriptor contains its subclass and protocol in the `bInterfaceSubClass` and `bInterfaceProtocol` fields, respectively.

The subclass code in the `bInterfaceSubClass` field refers to one of the subclasses listed in [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskhiveeeqi). These codes denote industry-standard specifications that describe the command block definitions used by the interfaces of USB mass storage class devices. They do _not_ refer to specific device types since most USB mass storage class devices can choose to comply with any command block specification.

__Table 3-1__  USB mass storage class subclasses

| Subclass code | Command block specification | Typical usage |
| 0x01 | Reduced Block Commands (RBC) | Flash device, other mass storage class devices |
| 0x02 | SFF8020I | CD-ROM device, other mass storage devices |
| 0x03 | QIC-157 | Tape device |
| 0x04 | UFI | Floppy disk device |
| 0x05 | SFF8070I | Floppy disk device, other mass storage devices |
| 0x06 | SCSI transparent command set | Any device that complies with a SCSI-defined command set |

The `bInterfaceProtocol` field in the interface descriptor denotes the transport protocol the interface uses. The `IOUSBMassStorageClass` driver supports the interface protocols shown in [Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeschifbugry).

__Table 3-2__  USB mass storage class protocols

| Protocol code | Protocol implementation |
| 0x0 | Control/Bulk/Interrupt protocol _with_ command completion interrupt |
| 0x01 | Control/Bulk/Interrupt protocol _without_ command completion interrupt |
| 0x50 | Bulk-only transport |

If the device is mass storage class compliant, one of the `IOUSBMassStorageClass` driver’s personalities matches on the device’s interface subclass. [Listing 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskhijceqsi) shows the first personality in the `IOUSBMassStorageClass` driver’s personality dictionary.

__Listing 3-3__  One of the IOUSBMassStorageClass driver’s personalities

```
<dict>
    <!-- CFBundleIdentifier denotes the name of the driver in
     -- reverse DNS notation. -->
    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOUSBMassStorageClass</string>

    <!-- IOUSBMassStorageClass is the name of the class the I/O Kit
     -- instantiates. -->
    <key>IOClass</key>
    <string>IOUSBMassStorageClass</string>

    <!-- IOUSBInterface is the name of the nub class this
     -- personality attaches to. -->
    <key>IOProviderClass</key>
    <string>IOUSBInterface</string>

    <!-- The next two keys describe which bus
     -- the device is on and whether it is internal
     -- or external.-->
    <key>Physical Interconnect</key>
    <string>USB</string>
    <key>Physical Interconnect Location</key>
    <string>External</string>

    <!-- The interface class this driver matches on.-->
    <key>bInterfaceClass</key>
    <integer>8</integer>

    <!-- Interface subclass 1 refers to the Reduced Block Commands
     -- subclass.-->
    <key>bInterfaceSubClass</key>
    <integer>1</integer>
```


Occasionally, a device is compliant with the USB mass storage specification but declares its device class to be vendor specific instead of mass storage. In this case, you need to induce the I/O Kit to load the `IOUSBMassStorageClass` driver for your device even though the driver matches on only mass storage class interfaces.

You do this by creating a KEXT that consists solely of an information property list that contains a personality for your device. Like any vendor-specific interface driver, this KEXT matches on the configuration value, interface number, and vendor and product numbers the `IOUSBInterface` nub supplies. Unlike most vendor-specific drivers, however, this KEXT sets its `IOClass` key to `IOUSBMassStorageClass` and includes a dictionary named “USB Mass Storage Characteristics” containing the subclass and protocol information that reflects how the device should be treated. The `IOUSBMassStorageClass` driver then uses those keys to determine the subclass and protocol of the device instead of relying on the information supplied by the device.

[Listing 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskjivceoqi) shows the personality for a device that complies with the USB mass storage class specification but belongs to the vendor-specific class.

__Listing 3-4__  Partial listing of an Info.plist file for a vendor-specific device


```
<dict>
    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOUSBMassStorageClass</string>

    <!-- IOUSBMassStorageClass is the name of the class the
     -- I/O Kit instantiates when probing. -->
    <key>IOClass</key>
    <string>IOUSBMassStorageClass</string>

    <!-- IOUSBInterface is the name of the nub class
    < -- the driver attaches to. -->
    <key>IOProviderClass</key>
    <string>IOUSBInterface</string>

    <!-- The following two keys describe
     -- which bus the device is on and whether it
     -- is internal or external. -->
    <key>Physical Interconnect</key>
    <string>USB</string
    <key>Physical Interconnect Location</key>
    <string>External</string>

    <key>USB Mass Storage Characteristics</key>
    <dict>
        <!-- The bInterfaceProtocol value is Control/Bulk/Interrupt
         -- with command completion interrupt. -->
        <key>Preferred Protocol</key>
        <integer>1</integer>
        <!-- The bInterfaceSubclass value is SFF8070I. -->
        <key>Preferred Subclass</key>
        <integer>5</integer>
    </dict>

    <!-- The following four keys are used for interface
     -- matching. -->
    <key>bConfigurationValue</key>
    <integer>MyConfigurationValue</integer>
    <key>bInterfaceNumber</key>
    <integer>MyInterfaceNumber</integer>
    <key>idProduct</key>
    <integer>MyProductID</integer>
    <key>idVendor</key>
    <integer>MyVendorID</integer>
</dict>
```


If your device is not compliant with the USB mass storage class specification, you need to develop a subclass of the `IOUSBMassStorageClass` driver to support the differences. In order to ensure that your driver loads in favor of the generic `IOUSBMassStorageClass` driver you must use the keys defined for interface matching in the Universal Serial Bus Common Class Specification, Revision 1.0 (available for download from [http://www.usb.org/developers/devclass_docs/usbccs10.pdf](http://www.usb.org/developers/devclass_docs/usbccs10.pdf).)

The interface-matching keys defined in the USB Common Class Specification consist of specific combinations of property keys. For a successful match, you must include the property keys defined by exactly one interface-matching key in your `Info.plist` file. If you use a combination of property keys _not_ defined by any interface-matching key, your driver will not match. For example, if you use the property keys for vendor, product, and interface protocol, your driver will not match. This is because there is no key that combines the property keys of vendor, product, and interface protocol.

[Table 3-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbecssdjjbumra) lists the keys in order of specificity: The interface-matching key for the most specific match (and highest probe score) is listed first.

__Table 3-3__  Interface-matching keys from the USB Common Class Specification

| Interface-matching key | Comment |
| `idVendor` + `idProduct` + `bInterfaceNumber` + `bConfigurationValue` + `bcdDevice` |  |
| `idVendor` + `idProduct` + `bInterfaceNumber` + `bConfigurationValue` |  |
| `idVendor` + `bInterfaceSubClass` + `bInterfaceProtocol` | Only if `bInterfaceClass` is0xFF |
| `idVendor` + `bInterfaceSubClass` | Only if `bInterfaceClass` is 0xFF |
| `bInterfaceClass` + `bInterfaceSubClass` + `bInterfaceProtocol` | Only if `bInterfaceClass` is not 0xFF |
| `bInterfaceClass` + `bInterfaceSubClass` | Only if `bInterfaceClass` is not 0xFF |

When an ATAPI mass storage device is discovered, the ATAPI bus controller publishes an ATA device nub that is a concrete subclass of `IOATADevice`. The ATA family defines no family-specific matching so all matching is active. This means the driver probes the device to determine if it is suited to drive it.

In its `start` method during active matching, the `IOATAPIProtocolTransport` driver compares the properties in its personality to the device’s properties. In particular, if the device’s ATA device type is ATAPI, the driver loads for that device. [Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskhjbdussa) shows the personality for the `IOATAPIProtocolTransport` driver.

__Listing 3-5__  The IOATAPIProtocolTransport driver personality dictionary

```
<dict>
    <!-- CFBundleIdentifier denotes the name of the driver in
     -- reverse DNS notation. -->
    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOATAPIProtocolTransport</string>

    <!-- IOATAPIProtocolTransport is the class the I/O Kit
     -- instantiates when probing. -->
    <key>IOClass</key>
    <string>IOATAPIProtocolTransport</string>

    <!-- IOATADevice is the nub this driver attaches to. -->
    <key>IOProviderClass</key>
    <string>IOATADevice</string>

    <!-- The next two keys describe which bus the
     -- device is on and whether it is internal
     -- or external.-->
    <key>Physical Interconnect</key>
    <string>ATAPI</string>
    <key>Physical Interconnect Location</key>
    <string>Internal<string>

    <!-- The value of this key is compared to the ATA device type
     -- of the device. -->
    <key>ata device type</key>
    <string>atapi</string>
</dict>
```

A subclass of the `IOATAPIProtocolTransport` driver should include the same keys shown in [Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskhjbdussa) in its personality dictionary. If you need to address ATAPI-specific issues such as a device that needs to do a hard reset after a particular event, you need to develop a subclass of `IOATAPIProtocolTransport` that overrides the appropriate methods. To ensure that your subclass driver loads, you should implement the `probe` method and increase the probe score after determining that your driver can, in fact, drive the device.

In order to change a device’s DMA or UDMA modes, however, you can take advantage of a feature in the `IOATAPIProtocolTransport` driver that allows a subclass to override the mode the device reports. You enable this feature by creating a KEXT that consists of an `Info.plist` file containing a dictionary named “ATAPI Mass Storage Characteristics” in addition to the keys shown in [Listing 3-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskhjbdussa). This dictionary contains the device model name and the DMA and UDMA mode values you choose. The device model name is the string the device returns when it responds to the ATA `Identify` command. The DMA and UDMA mode values are bitmasks defined in the ATA/ATAPI-5 specification (available at [http://www.t13.org](http://www.t13.org/)). [Listing 3-6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeeskfiveesri) shows an example personality dictionary that overrides the DMA and UDMA values returned by the device.

__Listing 3-6__  A personality dictionary that overrides DMA and UDMA values

```
<dict>
    <key>ATAPI Mass Storage Characteristics</key>
    <dict>
        <key>DMA Mode</key>
        <integer>0</integer>
        <key>UDMA Mode</key>
        <integer>0</integer>
        <key>device model</key>
        <string>MyDeviceModel</string>
    </dict>

    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOATAPIProtocolTransport</string>

    <key>IOClass</key>
    <string>IOATAPIProtocolTransport</string>

    <key>IOProbeScore</key>
    <integer>5000</integer>

    <key>IOProviderClass</key>
    <string>IOATADevice</string>

    <key>Physical Interconnect</key>
    <string>ATAPI</string>

    <key>Physical Interconnect Location</key>
    <string>Internal</string>

    <key>ata device type</key>
    <string>atapi</string>
</dict>
```

In this example, when this device is discovered, the I/O Kit allows all KEXTs with the key-value pair

```
<key>ata device type</key>
<string>atapi</string>
```

to probe the device. If a KEXT’s personality contains the ATAPI Mass Storage Characteristics dictionary, the I/O Kit compares the value of the `device model` string with the device model name reported by the device. If they match, the I/O Kit loads the `IOATAPIProtocolTransport` driver and applies the DMA and UDMA overrides declared in the ATAPI Mass Storage Characteristics dictionary.

After the protocol services driver loads, the peripheral device nub queries the device and publishes its device type in the I/O Registry. The I/O Kit then finds and loads the appropriate logical unit driver for the device. Unlike the bus-specific perspective of the protocol services drivers, the logical unit drivers view a mass storage device in terms of its device type as defined by the SCSI Architecture Model specifications. Thus, all four in-kernel logical unit drivers use the same matching language.

The following four properties in the personality of a logical unit driver determine which devices or device types the driver is suited for:

- The peripheral device type property
- The vendor property
- The product or model property
- The product or software revision property

These four properties vary from the general to the specific. Each specified property narrows the range of devices the driver is suitable for. The more properties the driver includes in its personality, the more specific the device it is suited to manage. The presence of the more specific properties does not make up for the absence of the peripheral device type property, however. If you do not include the peripheral device type property in your logical unit driver’s personality, it will not be considered for loading.

During the passive matching phase, the properties are examined in the order listed and the driver’s probe score is increased with each match. Every property in the driver’s personality must match in order for the driver to be considered a candidate for the device. In other words, if a driver specifies a property, it must match for that driver to be considered. If one of the more specific properties is absent, however, it does not affect the probe score because that means the driver can manage a broader range of devices.

For example, of the four listed properties, the `IOSCSIPeripheralDeviceType00` driver lists only the peripheral device type property in its personality because it can drive any device that complies with the SCSI Architecture Model specification for block storage devices. The personality dictionary for the `IOSCSIPeripheralDeviceType00` driver is shown in [Listing 3-7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeessdifbeery).

__Listing 3-7__  The IOSCSIPeripheralDeviceType00 driver personality dictionary

```
<dict>
    <!-- The CFBundleIdentifier gives the name of this KEXT in
     -- reverse-DNS notation. -->
    <key>CFBundleIdentifier</key>
    <string>com.apple.iokit.IOSCSIBlockCommandsDevice</string>

    <!-- IOSCSIPeripheralDeviceType00 is the name of the class
     -- the I/O Kit instantiates. -->
    <key>IOClass</key>
    <string>IOSCSIPeripheralDeviceType00</string>

    <!-- IOSCSIPeripheralDeviceNub is the name of the nub
     -- class this personality attaches to. -->
    <key>IOProviderClass</key>
    <string>IOSCSIPeripheralDeviceNub</string>

    <!-- This personality is suited to drive devices of peripheral
     -- device type 0. ->
    <key>Peripheral Device Type</key>
    <integer>0</integer>
</dict>
```

If you subclass a logical unit driver to address a device’s differently implemented command or added feature, you must ensure that your driver’s probe score is higher than that of a more generic driver. To do this, you add as many of the four logical unit driver personality properties as necessary to uniquely identify your device.

For example, a driver can use both vendor and product information to ensure that it gets loaded in favor of one of the Apple-provided logical unit drivers. [Listing 3-8](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeessdifeumra) shows the personality dictionary for a driver competing with the `IOSCSIPeripheralDeviceType05` driver.

__Listing 3-8__  Example logical unit driver personality dictionary


```
<dict>
    <!-- The CFBundleIdentifier value is the name of
     -- this KEXT. -->
    <key>CFBundleIdentifier</key>
    <string>com.MySoftwareCompany.driver.MyLogicalUnitDriver</string>

    <!-- The IOClass value is the name of the class
     -- the I/O Kit instantiates. -->
    <key>IOClass</key>
    <string>com_MySoftwareCompany_iokit_MyLogicalUnitDriver</string>

    <!-- The IOProviderClass value is the name of the
     -- nub this driver attaches to. -->
    <key>IOProviderClass</key>
    <string>IOSCSIPeripheralDeviceNub</string>

    <!-- The next three keys determine the device this
     -- driver is suited to drive. -->
    <key>Peripheral Device Type</key>
    <integer>5</integer>

    <key>Product Identification</key>
    <string>MyProductID</string>

    <key>Vendor Identification</key>
    <string>MyVendorID</string>
</dict>
```


After the logical unit driver loads, it publishes the appropriate device services nub with the device’s type in the I/O Registry. The I/O Kit initiates matching on this nub object and finds the appropriate generic block storage driver. The block storage driver then publishes an `IOMedia` object that represents the whole device. If the disk is Apple-formatted, the `IOApplePartitionScheme` matches on the `IOMedia` object and publishes new `IOMedia` objects for each partition.

Filter-scheme drivers must match on the properties the `IOMedia` objects publish. The standard set of properties for `IOMedia` objects include the following:

__Table 3-4__  IOMedia properties

| Key | Type | Description |
| `kIOMediaEjectableKey` | Boolean | Is the media ejectable? |
| `kIOMediaPreferredBlockSizeKey` | Number | The media’s natural block size in bytes. |
| `kIOMediaSizeKey` | Number | The media’s entire size in bytes. |
| `kIOMediaWholeKey` | Boolean | Is the media at the root of the media tree? This is true for the physical media representation, a RAID media representation, etc. |
| `kIOMediaWritableKey` | Boolean | Is the media writable? |
| `kIOMediaContentHintKey` | String | The media’s content description, as hinted at the time of the object’s creation. The string is of the _MyCompany_MyContent_ format. |
| `kIOBSDNameKey` | String | The media’s BSD device node name, which is dynamically assigned at the object’s creation. |

You can choose any subset of these properties to include in your driver’s personality dictionary, but all properties in the personality must match for your driver to be considered for loading.

The `kIOMediaContentHintKey` is the most useful property because it matches on the unique content-hint string your disk utility program places in the media’s partition (for more information on this process, see [Construction of a Mass Storage Driver Stack](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvbeur2gjjeuuqi)). You define the content-hint string your disk utility program uses, you place the same content-hint string in the `kIOMediaContentHintKey` property of your driver’s personality, and your filter-scheme driver is the only candidate to match on that media.

Unlike the SCSI Architecture Model family, the Storage family does not increase a driver’s probe score with each successful property match during the passive matching phase. If a filter-scheme driver’s personality matches successfully on an `IOMedia` object’s properties, the I/O Kit allows it to probe the media during the active matching phase. If the filter-scheme driver implements its own `probe` method, it can increase or decrease its probe score according to its ability to drive the media. However, because the filter-scheme driver that matches on the content-hint string is almost certainly the only driver candidate, it is seldom necessary to override the `probe` method. By default, the `probe` method returns `true` and the active matching phase ends as the I/O Kit chooses the one filter-scheme driver that matched on the content-hint string property.

If you develop your own filter-scheme driver, you must ensure that your driver’s personality can match on your content as identified by your content-hint string. [Listing 3-9](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbegskhijdemry) shows the personality dictionary of a filter-scheme driver that matches on the content-hint string `MySoftwareCompany_MyContent`.

__Listing 3-9__  Example filter-scheme driver personality


```
<dict>
    <key>IOStorage</key>
    <dict>
        <!-- The CFBundleIdentifier gives the name of this KEXT in
         -- reverse-DNS notation. -->
        <key>CFBundleIdentifier</key>
        <string>com.MySoftwareCompany.driver.MyFilterScheme</string>

        <!-- The Content Hint value must be identical to the content hint
         -- string your disk utility program places in the partition. -->
        <key>Content Hint</key>
        <string>MySoftwareCompany_MyContent</string>

        <!-- The IOClass value is the name of the class
         -- the I/O Kit instantiates. -->
        <key>IOClass</key>
        <string>com_MySoftwareCompany_driver_MyFilterScheme</string>

        <!-- The IOMatchCategory key is a special key that allows
         -- multiple clients to match on an IOMedia object. -->
        <key>IOMatchCategory</key>
        <string>IOStorage</string>

        <!-- The IOProviderClass is the name of the
         -- nub this driver attaches to. -->
        <key>IOProviderClass</key>
        <string>IOMedia</string>
    </dict>
</dict>
```

[Next](Developing%20a%20Universal%20Binary.md)[Previous](Mass%20Storage%20Device%20Compliance.md)


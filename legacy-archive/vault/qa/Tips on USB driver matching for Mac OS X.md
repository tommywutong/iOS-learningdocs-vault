---
title: Tips on USB driver matching for Mac OS X
apple_id: DTS10001628
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2008-08-14'
source_url: https://developer.apple.com/library/archive/qa/qa1076/_index.html
archived_at: '2026-07-18T02:29:55.580303Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1076

# Tips on USB driver matching for Mac OS X

## Q:  I can't get my kernel driver to match against my USB device. What's wrong?

A: I can't get my kernel driver to match against my USB device. What's wrong?

There could be many things causing your driver not to match, but the most common mistake is an incorrect combination of property keys in your driver's `Info.plist` property list.

USB driver matching is based on the [USB Common Class Specification](http://www.usb.org/developers/devclass_docs/usbccs10.pdf). The IOUSBFamily in conjunction with I/O Kit will use a probe score to determine the best driver candidate for a particular device.

The following tables show the probe scores obtained by specifying the corresponding keys in your driver's `Info.plist`.

Note that you should never add your own `IOProbeScore` property to a USB driver's property list. Also, don't add extra keys; only use the key combinations shown in the following tables.

__Table 1__  Properties for matching a USB device (IOProviderClass is IOUSBDevice)

| Keys | Comments | Probe Score |
| idVendor + idProduct + bcdDevice |  | 100000 |
| idVendor + idProduct |  | 90000 |
| idVendor + bDeviceSubClass + bDeviceProtocol | Only if bDeviceClass is 0xFF (vendor specific). | 80000 |
| idVendor + bDeviceSubClass | Only if bDeviceClass is 0xFF (vendor specific). | 70000 |
| bDeviceClass + bDeviceSubClass + bDeviceProtocol | Only if bDeviceClass is not 0xFF. | 60000 |
| bDeviceClass + bDeviceSubClass | Only if bDeviceClass is not 0xFF. | 50000 |

__Table 2__  Properties for matching a USB interface (IOProviderClass is IOUSBInterface)

| Keys | Comments | Probe Score |
| idVendor + idProduct + bInterfaceNumber + bConfigurationValue + bcdDevice |  | 100000 |
| idVendor + idProduct + bInterfaceNumber + bConfigurationValue |  | 90000 |
| idVendor + bInterfaceSubClass + bInterfaceProtocol | Only if bInterfaceClass is 0xFF (vendor specific). | 80000 |
| idVendor + bInterfaceSubClass | Only if bInterfaceClass is 0xFF (vendor specific). | 70000 |
| bInterfaceClass + bInterfaceSubClass + bInterfaceProtocol | Only if bInterfaceClass is not 0xFF. | 60000 |
| bInterfaceClass + bInterfaceSubClass | Only if bInterfaceClass is not 0xFF. | 50000 |

If your driver still fails to load, make sure that the value for the `CFBundleIdentifier` property in the `IOKitPersonalities` dictionary is the same value as the `CFBundleIdentifier` property for the driver as shown in Listing 1.

__Listing 1__  CFBundleIdentifier property in personality dictionary.

```xml
<?xml version="1.0" encoding="UTF-8"?> <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"> <plist version="1.0"> <dict>     <key>CFBundleDevelopmentRegion</key>     <string>English</string>     <key>CFBundleExecutable</key>     <string>${EXECUTABLE_NAME}</string>     ...     <key>CFBundleIdentifier</key>     <string>com.apple.dts.driver.HelloIOKit</string>     ...     <key>IOKitPersonalities</key>     <dict>         <key>HelloIOKit</key>         <dict>             <key>CFBundleIdentifier</key>             <string>com.apple.dts.driver.HelloIOKit</string>             <key>IOClass</key>             <string>com_apple_dts_driver_HelloIOKit</string>             ...         </dict>     </dict>     ... </dict> </plist>
```

If your driver matches when you hot-plug your device but not when your device is attached at boot time, a boot-time driver might be matching to your device. Even though your driver is a better match, I/O Kit will not terminate a driver which has already been given control over a device.

In this case, you will need to add a `OSBundleRequired` property to your driver's property list so your driver is also considered for matching at boot time.

For more information on loading KEXTs at boot time, please see _Loading Kernel Extensions at Boot Time_ in the document Kernel Extension Programming Topics.

Other driver loading problems can be diagnosed using general I/O Kit troubleshooting techniques. One useful tip is to use the diagnostic mode of the kextload command to try to load your driver by hand as shown in Listing 2

__Listing 2__  Diagnostic options for the kextload command.

```
$ kextload -nt HelloIOKit.kext
```


As shown in the previous section, the Common Class Specification details the exact nature of how the fields of the USB device and interface descriptor are used to match drivers. In some cases, however, it would be convenient to not have to create multiple I/O Kit personalities to specify different devices that are supported by a particular driver. For example, if you had to support a whole set of devices from a single vendor, you could just specify a personality that matched to all the product IDs for that vendor. If you then needed to trim the supported product IDs, you could use the `probe` method of the driver to deny matching to product IDs outside the range that the driver can support. That is the idea behind the concept of wild card matching.

In the tables above, you can substitute the asterisk `*` wild card character for any of the fields from the device or interface descriptor. The type of the property's value must be changed from `<integer>` to `<string>` when the wild card character is used as shown in Listing 3. The probe score will then be reduced by 1000 for each wild card that is specified. For example, a device driver matching on `idProduct` and `idVendor` will have a probe score of 90000. If a wild card is specified for the `idProduct`, the probe score will be reduced by 1000 to 89000. This means that a driver for the same device that does not have a wild card will out-match a wild card-enabled one.

__Listing 3__  Example wild card matching personality.

```
 <key>IOKitPersonalities</key>         <dict>                 <key>WildCardMatching</key>                 <dict>                         <key>CFBundleIdentifier</key>                         <string>com.apple.dts.driver.HelloIOKit</string>                         <key>IOClass</key>                         <string>com_apple_dts_driver_HelloIOKit</string>                         <key>IOProviderClass</key>                         <string>IOUSBDevice</string>                         <key>idProduct</key>                         <string>*</string>                         <key>idVendor</key>                         <integer>1452</integer>                 </dict>         </dict>
```

The `idProduct` property can also match against a specified range of product IDs without having to implement a `probe` method to weed out unwanted product IDs. This partial matching is done by specifying a numeric `idProductMask` property in the driver's matching personality in addition to the `idProduct` property. This mask will be bitwise ANDed with each candidate device's product ID before comparing it to the `idProduct` property.

Listing 4 shows how to specify a match on product IDs between 4752 (0x1290) and 4755 (0x1293). The value of the `idProductMask` property is 65532 (0xfffc). Thus, any product ID will be considered a match that, after being ANDed with 0xfffc, equals the `idProduct` property's value of 4752.

__Listing 4__  Example of using idProductMask to match a range of product IDs.

```
 <key>IOKitPersonalities</key>         <dict>                 <key>WildCardMatching</key>                 <dict>                         <key>CFBundleIdentifier</key>                         <string>com.apple.dts.driver.HelloIOKit</string>                         <key>IOClass</key>                         <string>com_apple_dts_driver_HelloIOKit</string>                         <key>IOProviderClass</key>                         <string>IOUSBDevice</string>                         <key>idProduct</key>                         <integer>4752</integer>                         <key>idProductMask</key>                         <integer>65532</integer>                         <key>idVendor</key>                         <integer>1452</integer>                 </dict>         </dict>
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-14 | Added documentation about Tiger wild card matching feature. Made other editorial changes. |
| 2008-08-13 | Added documentation about Tiger wild card matching feature. Made other editorial changes. |
|  | Added documentation about Tiger wild card matching feature. Made other editorial changes. |
| 2008-08-08 | Added documentation about Tiger wild card matching feature. Made other editorial changes. |
|  | Added documentation about Tiger wild card matching feature. Made other editorial changes. |
| 2001-10-02 | New document that gives some tips on getting USB driver matching to work. |


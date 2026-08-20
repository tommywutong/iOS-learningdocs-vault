---
title: ExpressCard Prevents System Sleep
apple_id: DTS10004237
resource_type: QA
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: null
published: '2007-02-28'
source_url: https://developer.apple.com/library/archive/qa/qa1517/_index.html
archived_at: '2026-07-18T02:32:04.999857Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1517

# ExpressCard Prevents System Sleep

## Q:  When our ExpressCard card is inserted, our Mac doesn't go to sleep. It keeps trying but wakes up immediately. What is causing this symptom and how can we fix it?

A: When our ExpressCard card is inserted, our Mac doesn't go to sleep. It keeps trying but wakes up immediately. What is causing this symptom and how can we fix it?

The ExpressCard slot found on Macintosh portable products such as the MacBook Pro features both a PCI Express interface and a USB interface. According to the ExpressCard Standard, the USB interface should comply with the [Universal Serial Bus specification](http://www.usb.org/developers/docs/) (currently revision 2.0). However, developers of USB functions will find that the USB specified VBUS power (5 volts) is not present at the interface. Instead the ExpressCard +3.3 V and +3.3 VAUX signals are available.

The ExpressCard interface turns off the +3.3 V signal when sleeping in accordance with the ExpressCard specification, but the +3.3 VAUX signal remains powered. It is important to understand that when a Macintosh computer is sleeping, USB devices are suspended and are capable of waking the machine if they are disconnected.

A traditional USB device indicates that it is connected by pulling either the D+ or the D- line to the VBUS power rail. An ExpressCard device should do so by pulling either the USBD+ or USBD- line to the +3.3 VAUX rail. If it instead pulls the line to the +3.3 V rail, when the computer goes to sleep, the USBD+ or USBD- line will be floating. The computer will interpret this as a device disconnect and will wake up immediately.

Thus USB functions should get their power from the +3.3 VAUX source (and if necessary also from the +3.3 V signal when operating) so that they do not disconnect when suspended.

The [PCMCIA organization](http://www.expresscard.org/) (responsible for the ExpressCard Standard document) is working on providing additional guidance in their specification, but many cards have been made that do not use the +3.3 VAUX power for their USB function. Vendors of these cards should consider redesigning their cards to use +3.3 VAUX power in order to avoid the sleep problem described earlier.

For cards already shipped, a workaround exists on systems that either have the [ExpressCard Update 1.0](http://www.apple.com/support/downloads/expresscardupdate10.html) installed or are running Mac OS X 10.4.8 or later.

If the device's USB function is a Composite class device, the workaround can be implemented using a codeless kernel extension (KEXT). The KEXT simply adds the Boolean property `ExpressCardCantWake` with a value of `true` to the device's I/O Registry entry. The USB Composite class driver checks for this property and informs the USB family if the property is set. In turn, the USB host controller driver (`AppleUSBUHCIDriver` for low- or full-speed devices or `AppleUSBEHCIDriver` for hi-speed devices) disables the wakeup-enable feature for the ExpressCard port if the device is connected there.

An example of such a codeless KEXT is available from Downloadables. Instructions on how to use it are in the project's `Info.plist` file.

If the device's USB function is not a composite class device, you can add code to your device's driver to enable the above workaround, or you can subclass `IOUSBCompositeDriver` and ensure that `IOUSBCompositeDriver::ConfigureDevice` is called. If you choose to modify your own driver, insert the code in Listing 1 into your driver's `start` method.

__Listing 1__  Code to tell the USB family that an ExpressCard device will disconnect on sleep.

```swift
 // See if this is an ExpressCard device which would disconnect on sleep (thus waking every time)     //     expressCardCantWakeRef = OSDynamicCast(OSBoolean, fDevice->getProperty(kUSBExpressCardCantWake));      if (expressCardCantWakeRef && expressCardCantWakeRef->isTrue()) {         fDevice->GetBus()->retain();         fDevice->GetBus()->message(kIOUSBMessageExpressCardCantWake, this, fDevice);         fDevice->GetBus()->release();     }
```

The `kIOUSBMessageExpressCardCantWake` message only needs to be issued once for the device and not once for each interface.

The constants `kUSBExpressCardCantWake` and `kIOUSBMessageExpressCardCantWake` are defined in the version of `IOKit/usb/USB.h` included in Xcode 2.4 and later.

- USBExpressCardCantWake: example codeless KEXT for USB composite class devices. ("qa1517_USBExpressCardCantWake.zip", 11.2K)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-02-28 | New document that describes how some ExpressCard cards can prevent system sleep and how to fix the problem. |


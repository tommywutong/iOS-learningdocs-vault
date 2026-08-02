---
title: Introducing the Apple AppleUSBFTDI kernel driver
apple_id: DTS40014014
resource_type: Technical Note
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2013-11-20'
source_url: https://developer.apple.com/library/archive/technotes/tn2315/_index.html
archived_at: '2026-07-26T19:54:12.990651Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2315

# Introducing the Apple AppleUSBFTDI kernel driver

With the release of OS X Mavericks, the AppleUSBFTDI kernel driver is included. This driver will affect existing applications that under OS X 10.8 and earlier, use the Future Technology Devices International (FTDI) D2XX libraries to communicate with hardware devices that are based on the FTDI USB-to-serial chipset. This Technical Note discusses the new Apple driver, how it affects these FTDI D2XX based applications and what alternatives such applications can implement as solutions for OS X Mavericks and beyond.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwugsbrfvke4vcbi4yq)[FTDI Applications Requiring the FTDI Kext](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwugsbrfvke4vcbi4za)[FTDI Applications That Implement a User Client Driver (D2XX Driver)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwugsbrfvke4vcbi4zq)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwugsbrfvjekrsfkjcu4q2fkm)[Downloadables](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwugsbrfvke4vcbi42a)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrgqwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The AppleUSBFTDI kernel extension is provided with OS X Mavericks to formally support application communications with hardware using the Future Technology Devices International (FTDI) chipset. Prior to OS X Mavericks, as OS X was updated, compatibility issues occurred as a result of issues between the FTDIUSBSerialDriver.kext and OS X updates. To eliminate these compatibility issues, Apple has implemented the AppleUSBFTDI for applications to use for communication with FTDI chipset based hardware accessories.

There are two categories of FTDI applications that are affected by the presence of the AppleUSBFTDI kernel extension. This Technical Note discusses these types of applications, how they are affected and the compatability solutions available for OS X Mavericks.

[Back to Top](#)

## FTDI Applications Requiring the FTDI Kext

One group of applications that communicate with FTDI based hardware requires the presence of the FTDI kernel extension. FTDI chipset based hardware presents itself as a USB Composite class device with a vendor specific interface. The interface is matched to the FTDI kext, that in turn creates a BSD serial port for use at the application layer. The application opens the serial port to communicate with the hardware.

Under OS X Mavericks, the AppleUSBFTDI kext will perform the same function as does the FTDI kext. When the hardware is attached, the AppleUSBFTDI kext is matched, and it will create a BSD serial port for applications to open. The Apple kext provides a BSD device name similar to the name provided by the FTDI driver. However, device name differences may occur and functionality may be slightly different. If the application fails to work with the hardware using the Apple driver, the preferred solution is update the application to work with the Apple driver. An application should use the IOKit framework APIs to detect the presence of the attached hardware and to identify the device name as demonstrated in the [SerialSample code](https://developer.apple.com/library/mac/samplecode/SerialPortSample). If after opening the serial port there are driver options that fail with the Apple driver, please submit a bug report.

An alternative solution is for the original FTDI driver to be installed. Both drivers define vendor specific USB Interface match criteria, however, the Apple driver intentionally sets a lesser probe score match to ensure that the FTDI Interface driver matches, when present. It is important to verify the compatibility of the FTDI driver with OS X Mavericks as kernel panics have been observed.

[Back to Top](#)

## FTDI Applications That Implement a User Client Driver (D2XX Driver)

The second group of applications that are affected by the presence of the AppleUSBFTDI kext, are those applications that implement user client drivers to communicate directly with the device from user space. Such applications will fail to open a connection with the hardware, because IOKit will already have matched the AppleUSBFTDI driver to the device. The application will see the exclusive access error 0xE00002C5 when attempting to open a connection with the device.

The recommended long term solution is to modify the application to open the BSD layer serial port for communication with the FTDI hardware. A short term solution is to implement a codeless kext, that will have a higher match priority than the AppleUSBFTDI kext to prevent IOKit from matching the AppleUSBFTDI kernel level driver to the hardware. An important ramification of the codeless kext solution is that an Installer process will be required to install the codeless kext. Under OS X Mavericks, the codeless kext must be signed.

Enclosed is a sample codeless kext project. The project includes a readme file describing the steps to modify that sample to match to your device. There are also instructions for installing the codeless kext to the `/System/Library/Extensions/` folder for test purposes only. Under OS X Mavericks, the official location for third party Extension files, is in `/Library/Extensions/`. OS X Mavericks requires that the kext be signed using a special Developer ID. See the readme file for instructions on requesting this special Developer ID.

[Back to Top](#)

## References

[WWDC 2013 Video - What's New in Kext Development](https://developer.apple.com/wwdc/videos/?id=707)

[Requesting a Developer ID Certificate for Signing Kexts](https://developer.apple.com/contact/kext/)

[Performing Serial IO Sample Code](https://developer.apple.com/library/mac/samplecode/SerialPortSample/)

[Back to Top](#)

## Downloadables

- Sample USB FTDI Codeless Kext project ("tn2315_SampleUSBFTDICodelessKext.zip", 55.4K)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-11-20 | New document that discusses the AppleUSBFTDI driver in OS X Mavericks and the compatibility issues which arise with applications communicating with FTDI D2XX based hardware. |


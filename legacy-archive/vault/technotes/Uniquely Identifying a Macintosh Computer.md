---
title: Uniquely Identifying a Macintosh Computer
apple_id: DTS10002943
resource_type: Technical Note
platform: macOS
topic: General
technology: IOKit
published: '2011-07-18'
source_url: https://developer.apple.com/library/archive/technotes/tn1103/_index.html
archived_at: '2026-07-26T19:53:43.685115Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN1103

# Uniquely Identifying a Macintosh Computer

There are two primary reasons why developers might want to uniquely identify a particular Macintosh computer. This technote describes those scenarios and provides recommended solutions for each case.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4yq)[Asset Tracking and Remote System Management](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4za)[Accessing the system serial number programmatically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4zq)[Caveats for using the serial number](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi42q)[Digital Rights Management (DRM)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi43a)[Accessing the built-in MAC address programmatically](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi43q)[Caveats for using the primary MAC address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi44a)[Network Registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4zta)[Caveats for using network registration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4ztc)[Conclusions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4zte)[References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwugsbrfvke4vcbi4zti)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydeojugmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

Developers sometimes need to uniquely identify a particular Macintosh computer. Applications that require this typically fall into two categories:

- Asset tracking and remote system management
- Digital rights management (DRM), including software and media content licensing

In general, the only consistent serial number on a Macintosh computer is on the bar code label attached to the machine's case. On current versions of Mac OS X, the About This Mac window and the System Profiler utility display this serial number. At first glance this appears to be what developers would want to use in their products, but there are caveats that this technote will discuss.

__Note:__ Beyond general advice such as provided in this technote, DTS does not support developing digital rights management products because of the significant compatibility issues involved that can affect customers. DTS does not maintain expertise in DRM techniques. Serious DRM is much more complicated than this technote describes.

[Back to Top](#)

## Asset Tracking and Remote System Management

Asset tracking applications allow system administrators to keep an inventory of the computers they manage for accounting purposes. Remote system management applications allow administrators to manage systems remotely, such as to install new software, reset passwords, view attached devices, and so on.

These applications often allow the administrator to access information about a particular computer using its serial number. This is a logical attribute to use: it's a human-readable attribute that is unique and readable even if the machine is nonfunctional.

### Accessing the system serial number programmatically

Developers of these applications often ask how to retrieve the system serial number that appears in the About This Mac window or in System Profiler. Prior to Mac OS X 10.3 "Panther", the only supported means of retrieving the serial number is to use AppleScript or Apple events to request this information from the System Profiler utility. However, starting with Panther, the serial number is presented in the property `IOPlatformSerialNumber` of the `IOPlatformExpertDevice` node in the I/O Registry. The I/O Registry accessor APIs in `IOKit.framework` can be used to retrieve this property from an application.

__Listing 1__  Reading the `IOPlatformSerialNumber` property

```c
#include <CoreFoundation/CoreFoundation.h> #include <IOKit/IOKitLib.h>  // Returns the serial number as a CFString.  // It is the caller's responsibility to release the returned CFString when done with it. void CopySerialNumber(CFStringRef *serialNumber) {     if (serialNumber != NULL) {         *serialNumber = NULL;          io_service_t    platformExpert = IOServiceGetMatchingService(kIOMasterPortDefault,                                                                          IOServiceMatching("IOPlatformExpertDevice"));          if (platformExpert) {             CFTypeRef serialNumberAsCFString =                  IORegistryEntryCreateCFProperty(platformExpert,                                                 CFSTR(kIOPlatformSerialNumberKey),                                                 kCFAllocatorDefault, 0);             if (serialNumberAsCFString) {                 *serialNumber = serialNumberAsCFString;             }              IOObjectRelease(platformExpert);         }     } }
```

### Caveats for using the serial number

It is possible for a system to lose its serial number so that it will no longer appear either in System Profiler or the I/O Registry. Repairing a system by swapping hardware components is one reason this can happen. Apple does not document the specific details of how a machine can lose its serial number. Once the serial number has been lost there is no means to restore it to the machine.

Apple does not guarantee that all future systems will have a software-readable serial number.

Both of these cases illustrate why asset tracking software should always provide a way for a serial number to be entered manually.

__Important:__ Developers should not make any assumptions about the format of the serial number such as its length or what characters it may contain.

[Back to Top](#)

## Digital Rights Management (DRM)

Digital rights management products seek to limit access to software or other digital content to licensed users of that content. DRM solutions have more stringent requirements for a system identifier:

- The identifier must be unique, otherwise licensed content could be used on more machines than was intended.
- The identifier must be stable, otherwise legitimate users could suddenly lose access to their licensed content.
- The identifier should not be easily changed, otherwise it would be too easy for unlicensed users to gain access to the content.

The Ethernet MAC (media access control) address for the primary built-in Ethernet (or Wi-Fi, on systems without Ethernet ports, such as MacBook Air) interface is the closest fit to these requirements available on Macintosh computers. The IEEE 802 networking standards specify universal addresses because a station with such an address can be attached to any LAN in the world with an assurance that the address will be unique.

All systems that can run Mac OS X include at least one built-in Ethernet port or Wi-Fi interface, so the presence of a MAC address is assured. On systems with more than one Ethernet port, one port is designated the primary port and is assigned the interface name `en0`.

### Accessing the built-in MAC address programmatically

The primary MAC address can be read from the I/O Registry as shown in the sample [Sample Code 'GetPrimaryMACAddress'](https://developer.apple.com/samplecode/GetPrimaryMACAddress/index.html).

### Caveats for using the primary MAC address

The primary MAC address is associated with a particular system main logic board. So while the address is stable, it will change should the system's main logic board need to be replaced. Or, a customer may simply want to transfer their licensed content to a newly-purchased computer. DRM solutions relying on the primary MAC address should provide a means for users to re-register their licensed content to a different MAC address.

Netbooting introduces a wrinkle with systems with multiple built-in Ethernet ports. The primary Ethernet port on these systems is the one that is connected to the NetBoot server. This means that a search for the primary port may return either of the built-in MAC addresses depending on which port was used for netbooting. Note that "built-in" does not include Ethernet ports that reside on an expansion card.

There are other means for reading a MAC address programmatically besides the I/O Registry technique employed by the GetPrimaryMACAddress sample. One is to use the function `getifaddrs`. Another is to use the CFUUID APIs in Core Foundation. Versions of Mac OS X prior to Mac OS X 10.4 "Tiger" generated version 1 UUIDs, which contain a MAC address. (Tiger generates version 4 UUIDs which are generated from random numbers. See the [Core Foundation release notes](https://developer.apple.com/releasenotes/CoreFoundation/CoreFoundation.html) and [RFC 4122: A Universally Unique IDentifier (UUID) URN Namespace](ftp://ftp.rfc-editor.org/in-notes/rfc4122.txt) for details.)

Neither the `getifaddrs` nor the CFUUID methods are suitable for DRM purposes, especially on Mac OS X 10.3 or later. On Panther, the `ifconfig` utility supports the `lladdr` option to set a locally-administered MAC address for an interface. Both `getifaddrs` and the CFUUID APIs will return the locally-administered MAC address if one exists. A DRM product that relied on these APIs would be vulnerable to an admin user using `ifconfig` to specify the same MAC address on multiple machines.

Finally, it is possible for the built-in MAC address (or any I/O Registry property for that matter) to be spoofed by knowledgeable persons. If a more robust level of security is required, such as in cases where the licensed assets have a high monetary value, developers may want to investigate the numerous hardware security tokens that are available.

[Back to Top](#)

## Network Registration

Rather than identifying a unique Macintosh computer, you may decide that you want to prevent multiple copies of the same application running on a network. The method some developers use is to register a service on the network using Bonjour with the name being a hash of the single serial number of the license. (Of course, you still need a way of generating and distributing that serial number.) Attempts to register the same service and serial number will return an error that the application uses to deny the use of the program.

Some resources you can refer to to learn more about Bonjour are:

- [NSNetServices and CFNetServices Programming Guide](https://developer.apple.com/documentation/Networking/Conceptual/NSNetServiceProgGuide/index.html)
- [Technical Q&A QA1311, 'Registering a Bonjour service multiple times'](https://developer.apple.com/qa/qa2001/qa1311.html)

### Caveats for using network registration

When using Bonjour in this way, pass in zero for the port number when registering your service. This will prevent these services from showing up when browsing.

Be sure to register a hash of the serial number, not the actual serial number, since it would be easy to use a packet sniffer to capture the raw serial number.

If the user has admin privileges, they can always disable the Bonjour daemon `mDNSResponder`. Be sure to test your application to make sure it behaves correctly in this situation.

[Back to Top](#)

## Conclusions

The schemes described here are simple ways to help uniquely identify a computer. Each approach is best suited for particular situations.

If you are serious about digital rights management, you should probably be contacting one of the many companies which specialize in DRM solutions, rather than writing a solution yourself. Both hardware solutions (such as USB dongles) and software solutions (such as licensing software) are widely available from third parties.

[Back to Top](#)

## References

- [Guidelines for use of the 24-bit Organizationally Unique Identifiers (OUI) within 32-bit Context Dependent Identifier (CDI-32™), 40-bit Context Dependent Identifier (CDI-40™), 48-bit Extended Unique Identifier (EUI-48™), 60-bit Global Identifier (EUI-60™), and 64-bit Global Identifier (EUI-64™) within existing and new applications](http://standards.ieee.org/regauth/oui/tutorials/UseOfEUI.html)
- [Guidelines for use of a 48-bit Extended Unique Identifier (EUI-48™)](http://standards.ieee.org/regauth/oui/tutorials/EUI48.html)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-18 | Minor formatting changes. |
| 2006-04-25 | Updated for Mac OS X. |
| 1997-12-01 | New document that illustrates how to identify a specific Macintosh computer. |


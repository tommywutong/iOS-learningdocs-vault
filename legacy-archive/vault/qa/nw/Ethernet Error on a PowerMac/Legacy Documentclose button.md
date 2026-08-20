---
title: Ethernet Error on a PowerMac
apple_id: DTS10001426
resource_type: QA
platform: macOS
topic: null
technology: null
published: '1995-09-15'
source_url: https://developer.apple.com/library/archive/qa/nw/nw14.html
archived_at: '2026-07-18T02:29:44.619627Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Mac OS 9 & Earlier](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxMacOS9Earlier-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library](https://developer.apple.com/referencelibrary/index.html)

|  |
| --- |
| Technical Q&A NW14Ethernet Error on a PowerMac |

|  |  |
| --- | --- |
| ---   Q: When I attempt to open the built-in Ethernet driver using the OpenDriver call on a PCI-based Macintosh, the call fails. What is the correct way to access the built-in driver on these new PowerMacs?  A: The new PCI-based PowerMacs implement Open Transport for Network Services, in which the architecture is a precursor to the changes expected for Copland. Since Open Transport is native, there is no longer a dependence on the 68K based Device Manager and Slot Manager. In order to maintain compatibility for the built-in ethernet driver, an ENET Shim was implemented so that applications which called the Ethernet driver directly could continue to work.  The ENET Shim opens when an `OpenSlot` call is made to open the Ethernet driver in NuBus slot 0. The shim intercepts this request and loads a .ENET driver entry into the driver table. From that time, applications which call `OpenDriver` will get the driver reference number for the shim driver, which then handles the various `Control` calls it receives.  Note that the shim only works for the built-in Ethernet device, not for an installed PCI Ethernet card.  The following sequence of calls works for all Ethernet connections in which Open Transport is present:   |  | | --- | | ``` /*     File:       ShowOTEnetAddr.c     Contains:   Simple app to print out Ethernet addresses for any Ethernet card on                 any Mac which has Open Transport installed.                 This includes the PCI based Macs.      Copyright:  © 1993-1995 by Apple Computer, Inc., all rights reserved.     Change History (most recent first):     2/6/96  rkubota (1) initialized the index variable to 0 in main     To Do: */  #include <stdio.h> #include <Types.h> #include <Memory.h> #include <Resources.h> #include <Events.h> #include <OpenTransport.h>          // open transport files #include <OpenTptLinks.h> struct Address8022 {     OTAddressType   fAddrFamily;     UInt8           fHWAddr[k48BitAddrLength];     UInt16          fSAP;     UInt8           fSNAP[k8022SNAPLength]; }; typedef struct Address8022 Address8022; #define kTrue   1 #define kFalse  0 //------------------------------------------------------------------------------- ---------- // Globals //------------------------------------------------------------------------------- ---------- EndpointRef     gEndpoint1; //------------------------------------------------------------------------------- ---------- // prototypes //------------------------------------------------------------------------------- ---------- OSStatus DoBind(void); OSStatus GetEthernetAddress(char *slotName); /******************************************************************************* ** DoBindENET     For this sample, we need to bind to any ethernet endpoint.  In this case     we bind to enet protocol type 0x8888.  We use an Address8022 variable     type for expediency ********************************************************************************/  OSStatus DoBind() {     OSStatus        osStatus;     TBind           gRequestInfo;     Address8022     theAddr =     {AF_8022, {0x00, 0x00, 0x00, 0x00, 0x00, 0x00}, 0x8888,                                     {0x00,0x00,0x00,0x00,0x00}};          // finish bind information     gRequestInfo.addr.buf = (UInt8 *)&theAddr;     gRequestInfo.addr.len = 10; // family type + Ethernet + type field                     // don't use sizeof(theAddr) since we are binding                     // to type 1 Ethernet address, not to an 802.2 address.     gRequestInfo.addr.maxlen = 0;     gRequestInfo.qlen = 0;      if (osStatus = OTBind(gEndpoint1, &gRequestInfo, NULL))     {         printf("\nCould not bind an endpoint, error = %d\n", osStatus);         CloseOpenTransport();         return  -4;     }      return osStatus; } /******************************************************************************* ** GetEthernetAddress ********************************************************************************/  OSStatus GetEthernetAddress(char *slotName) {     OSStatus        osStatus;     TBind           returnInfo;     Address8022     theReturnAddr =     {AF_8022, {0x00, 0x00, 0x00, 0x00, 0x00, 0x00}, 0x0000,                                      {0x00,0x00,0x00,0x00,0x00}};      returnInfo.addr.buf = (UInt8 *)&theReturnAddr;     returnInfo.addr.maxlen = 10;     // family type + 6 bytes for Ethernet + type     returnInfo.qlen = 0;       osStatus = OTGetProtAddress(gEndpoint1,&returnInfo,NULL);      if (osStatus == kOTNoError)     {         if (slotName[0] != 0x00)             printf("\nAddress for PCI Slot %s => ", slotName);         else             printf("\nAddress for Ethernet Built-In => ");          printf("%02x.",(int )theReturnAddr.fHWAddr[0]);         printf("%02x.",(int )theReturnAddr.fHWAddr[1]);         printf("%02x.",(int )theReturnAddr.fHWAddr[2]);         printf("%02x.",(int )theReturnAddr.fHWAddr[3]);         printf("%02x.",(int )theReturnAddr.fHWAddr[4]);         printf("%02x",(int )theReturnAddr.fHWAddr[5]);     }     else         printf("\n\nCould not get the Ethernet address, error = %d\n\n", osStatus);      return osStatus; } /******************************************************************************* ** main ********************************************************************************/  main() {     OSStatus        osStatus;     OTPortRecord    devicePortRecord;     Boolean         foundAPort;     UInt32          index;      printf("\n\nEthernet Address Display v1.1\n");     printf("\nThis application displays the Ethernet address for the\n");     printf("Ethernet Built-In port and PCI Ethernet cards.\n\n");      if (osStatus = InitOpenTransport())     {         printf("\n\nOpen Transport is not installed!\n\n");         return 0;     }      index = 0;         // iterate thru each OT port record for ethernet ports.     while (foundAPort = OTGetIndexedPort(&devicePortRecord,index))     {         if ((devicePortRecord.fCapabilities & kOTPortIsDLPI) &&             (devicePortRecord.fCapabilities & kOTPortIsTPI) &&             (kOTEthernetDevice == OTGetDeviceTypeFromPortRef(devicePortRecord.fRef)))         {              gEndpoint1 = OTOpenEndpoint(                 OTCreateConfiguration(devicePortRecord.fPortName),                 (OTOpenFlags)NULL, NULL,&osStatus);              if (osStatus == kOTNoError)             {                     // we have to bind the endpoint                     // before we can get it's address info                 osStatus = DoBind();                 if (osStatus == kOTNoError)                 {                     GetEthernetAddress(devicePortRecord.fSlotID);                     OTUnbind(gEndpoint1);                 }                  OTCloseProvider(gEndpoint1);             }           }         index++;     }            // closing down     CloseOpenTransport();      printf("\n\nTo quit the application press Command-Q.\n");      return 0; } ``` | |

#### [Sep 15 1995]

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

---

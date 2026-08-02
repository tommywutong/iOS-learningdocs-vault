---
title: Sandboxing a Print Dialog Extension
apple_id: DTS40014017
resource_type: Technical Note
platform: macOS
topic: Graphics & Animation
technology: AppKit
published: '2015-06-03'
source_url: https://developer.apple.com/library/archive/technotes/tn2329/_index.html
archived_at: '2026-07-26T19:54:13.001251Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2329

# Sandboxing a Print Dialog Extension

The purpose of this document is to explain the steps to Sandbox a Print Dialog Extension (PDE).

[Print Dialog Extensions and the App Sandbox](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvifeskokrcesqkmj5dukwcuivhfgskpjzjuctseififau2bjzceet2y)[Declaring Sandbox Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvcekq2mifjestshknau4rccj5megt2nkbaviskcjfgesvcz)[Testing Sandbox Compatibility](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvkeku2ujfheou2bjzceet2yinhu2ucbkreueskmjfkfs)[Communicating with the Print Driver](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvbu6tknkvhesq2bkreu4r2qkjeu4vcekjevmrks)[Storing Dynamic Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvcecvcbknke6usbi5cq)[CUPS Filter Steps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvbu6tknifheirsjjrcumskmkrcveu2uivifg)[PDE Steps](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvieirktkrcvauy)[Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvke4vcbi4yq)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Print Dialog Extensions and the App Sandbox

This Tech Note describes how Print Dialog Extensions (PDEs) are affected by the host app’s Sandbox. The App Sandbox is a security mechanism designed to limit the damage that could be done by a compromised or buggy application. For details about the App Sandbox, see the [App Sandbox](https://developer.apple.com/app-sandboxing/) developer landing page.

PDEs are plugins that are loaded when the Print dialog is shown to the user. They extend the feature set of the Print dialog, typically offering options specific to the selected printer. Since they are plugins, they run in the address space of the host app and must comply with the restrictions enforced by the host app’s Sandbox. These include:

- Limited file system access. PDEs can only access files in the app’s container. This means that PDEs cannot exchange information with their associated printer driver using files in a common directory because there is no mutually accessible directory. It also means that a PDE setting stored in NSUserDefaults is not accessible to the same PDE running under a different app.
- Networking. PDEs must not engage in any network activity whether or not the app has networking entitlements. For example, PDEs cannot directly communicate with their associated printer. However there is a mechanism for PDEs to instruct their drivers to perform certain operations with their associated printer, and to obtain the results of those operations. This is discussed below.
- Launching processes and sending AppleEvents to other processes is not allowed.
- Address Book access. If the host app has the com.apple.security.personal-information.addressbook entitlement, PDEs can access the user’s address book. On the other hand, if the host app does not have this entitlement, PDEs must handle that case appropriately. For example, a Fax PDE may require the user to manually enter phone numbers if address book access is denied.

[Back to Top](#)

## Declaring Sandbox Compatibility

The App Sandbox was introduced in OS X 10.7 Lion but the OS allowed non-compliant PDEs to run. This workaround mechanism was maintained in OS X 10.8 Mountain Lion. Finally in OS X 10.9 Mavericks, the Print dialog does not load non-compliant PDEs. Therefore all PDEs must follow the above rules for App Sandbox compatibility.

To declare compatibility, PDEs must include a key in their Info.plist. The key name is PMSandboxCompatiblePDEs and its value must be set to True.

[Back to Top](#)

## Testing Sandbox Compatibility

The easiest way to determine if a PDE is complying with Sandbox rules is to look for `sandboxd` messages in Console when running a wide variety of OS X apps.

[Back to Top](#)

## Communicating with the Print Driver

__Note:__ The CUPS daemon runs a variety of programs to process print jobs and obtain printer information. In this document, the terms “filter” and “driver” are used interchangeably.

PDEs can communicate with their associated printers, indirectly, by sending command jobs to their driver. And they can obtain information about the printer via printing system APIs, including `PMPrinterCopyState` to get the current state of the printer, and the CUPS PostScript Printer Description (PPD) APIs to get the printer’s options and defaults.

The sample code downloadable below demonstrates how to implement this mechanism.

[Back to Top](#)

## Storing Dynamic Data

Sandboxing prevents PDEs and drivers from using a shared directory on disk. Instead they can share information using the PPD file associated with the printer queue. The following are in-depth steps and example code to accomplish this.

### CUPS Filter Steps

CUPS filters should send "`PPD:` messages" to the CUPS daemon, via stderr, to ensure the PPD file is up-to-date.

- `PPD:` messages can be used to set or create key/value data within the PPD file, for example:

  ```
  PPD: DataLine1="foo" DataLine2="bar" ... DataLineN="baz"
  ```

  If the argument key exists, then it is updated, otherwise it is inserted. All dynamic data must be stored in this fashion.
- You can have multiple key/values per `PPD:` message, with a maximum `PPD:` message of 2k in size when running on OS X 10.7 or later. The size limitation before 10.7 is 1k.
- The PPD file is recreated after each `PPD:` message is processed by the CUPS daemon. It is recommended that you compress the data before encoding to save space, and minimize the number of keywords that are updated by your driver.
- The archive linked in the [Sample Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvke4vcbi4yq) section contains source files that demonstrate reading and writing PPD data with the following relevant notes:

  - The example handles combining multiple PPD options into a single status line up to the 1k limit imposed by CUPS on OS X 10.6.
  - Data is gzip'd and Base64-encoded. For the example code in testppdx.c, we end up with a net savings/compression of about 40% in the PPD file.
  - The code puts an upper limit of 16MB worth of data that can be embedded per keyword. This is based on the average compression factor, maximum number of compressed bytes that can be encoded per line (158), and the number of chunks (numbered keywords) supported by the current code (64k).

### PDE Steps

PDEs then read the PPD file to reflect the printer's options and values within the Print dialog. The following are steps the PDE should use to read the PPD file.

- Because the printing system does not consolidate `PPD:` messages before writing the PPD, it may be necessary to poll for their completion before doing other work. This is accomplished by sending a command job and waiting for that job to complete. The command job can be any job (like `ReportStatus`); all issued `PPD:` messages are guaranteed to finish before the command job status is moved to complete.

  To send the command job, use `PMPrinterSendCommand`. Alternatively, cupsDoFileRequest and IPP requests can be leveraged to do this directly. For an example of the latter, see the SampleSuppliesView -sendCommand: method within the [SampleRaster](https://developer.apple.com/legacy/library/samplecode/SampleRaster/Introduction/Intro.html) sample code project that implements an example command file filter and PDE.

  The job name that you specify as a parameter is checked (using cupsGetJobs) for job completion. The job name is the jobTitle input to `PMPrinterSendCommand`, as seen here:

  ```
  (from PMCore.h: )

  *    jobTitle:
  *      The title of the job associated with the command file. If NULL,
  *      a job title will be automatically generated but it may not be
  *      meaningful to a user.

  extern OSStatus
  PMPrinterSendCommand(
    PMPrinter       printer,
    CFStringRef     commandString,
    CFStringRef     jobTitle,
    CFDictionaryRef options) AVAILABLE_MAC_OS_X_VERSION_10_6_AND_LATER;
  ```
- Access the updated PPD file within the PDE using `cupsGetPPD3`, with `CUPS_HTTP_DEFAULT` and `PMPrinterGetID` as its primary arguments.
[Back to Top](#)

## Sample Code

This downloadable sample code supports the technique illustrated in the [Storing Dynamic Data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytimbrg4wugsbrfvcecvcbknke6usbi5cq) section.

__Note:__ Use the "Companion File" link in the upper-right corner of this page to download the sample code associated with this document.

- Dynamic PPD Sample Code ("tn2329_DynamicPPDSampleCode.zip", 8.2K)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-06-03 | Minor editorial update. |
| 2013-12-13 | New document that lists the requirements of Sandboxing a Print Driver Extension (PDE). |


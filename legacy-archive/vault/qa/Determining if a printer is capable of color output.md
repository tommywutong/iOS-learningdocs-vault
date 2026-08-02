---
title: Determining if a printer is capable of color output.
apple_id: DTS40009265
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: null
published: '2009-09-24'
source_url: https://developer.apple.com/library/archive/qa/qa1568/_index.html
archived_at: '2026-07-18T02:32:18.621508Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1568

# Determining if a printer is capable of color output.

## Q:  How do I determine if the current printer can print in color?

A: How do I determine if the current printer can print in color?

It is not possible to definitively determine if a printer can print in color. You can determine if a PPD declares the associated printer as color capable, but a PPD is not required to declare this. Alternatively a printer can be capable of color, but placed in grayscale mode by the user. Finally, it is not generally possible to determine if a non-color printer can produce grayscale output.

You can determine if the PPD believes that the printer is capable of color by looking for the \*ColorDevice keyword in the printer's PPD file. Printer Dialog Extensions (PDEs) may retrieve the corresponding PPD for the current printer by using the `-ppdFile` method of the callback object they are given when initialized. CUPS filters can obtain the path to the PPD file for the current printer from the `PPD` environment variable.

Listing 1 below shows how to do this from an application's perspective.

If you are using color support to influence how to render printed output, you should always provide a method for the user to override your initial selection.

__Listing 1__  Determining if a PPD declares a ColorDevice

```swift
bool isPrinterColor(PMPrinter printer) {     bool isColor = true;     CFURLRef ppdURL = NULL;     OSStatus err = PMPrinterCopyDescriptionURL(printer, kPMPPDDescriptionType, &ppdURL);     if((err == noErr) && (ppdURL != NULL))     {         char ppdPath[MAXPATHLEN];         if(CFURLGetFileSystemRepresentation(ppdURL, true, (UInt8*)ppdPath, sizeof(ppdPath)))         {             ppd_file_t *ppd = ppdOpenFile(ppdPath);             if(ppd != NULL)             {                 ppd_attr_t *attr = ppdFindAttr(ppd, "ColorDevice", NULL);                 if((attr != NULL) && (attr->value != NULL))                 {                     isColor  = ppd->color_device;                 }                 ppdClose(ppd);             }         }         CFRelease(ppdURL);     }     return isColor; }
```

Cocoa applications should use NSPrintInfo's [PMPrintSession](https://developer.apple.com/documentation/appkit/nsprintinfo/1534414-pmprintsession) method to obtain a PMPrintSession, then call [PMSessionGetCurrentPrinter](https://developer.apple.com/documentation/applicationservices/1458998-pmsessiongetcurrentprinter) to get the PMPrinter reference needed for `isPrinterColor` above.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-09-24 | New document that describes a heuristic that you can use to determine if a printer supports color output. |


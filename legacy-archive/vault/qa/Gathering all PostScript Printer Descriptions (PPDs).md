---
title: Gathering all PostScript Printer Descriptions (PPDs)
apple_id: DTS10004396
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2008-08-08'
source_url: https://developer.apple.com/library/archive/qa/qa1529/_index.html
archived_at: '2026-07-18T02:32:12.058424Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1529

# Gathering all PostScript Printer Descriptions (PPDs)

## Q:  I'm trying to gather all available PPDs on the users system but calling `PMCopyAvailablePPDs` with `kAllPPDDomains` returns an error. How can I get a list of all PPDs on the user's system?

A: I'm trying to gather all available PPDs on the users system but calling `PMCopyAvailablePPDs` with `kAllPPDDomains` returns an error. How can I get a list of all PPDs on the user's system?

`PMCopyAvailablePPDs` on Mac OS X 10.4 and earlier may incorrectly return no results given the `kAllPPDDomains` domain if any of the searched paths does not exist. Typically the missing directory is `~/Library/Printers/` as this folder was not created for user accounts created on older versions of Mac OS X.

A simple work around is to call `PMCopyAvailablePPDs` with specific domains instead of using the `kAllPPDDomains` constant. Listing 1 demonstrates this method.

__Listing 1__  A simple replacement for `PMCopyAvailablePPDs`

```
// Appends the discovered PPDs to the given mutable array, or does nothing on error. void AppendPPDs(PMPPDDomain domain, CFMutableArrayRef destination) {     CFArrayRef temp = NULL;     OSStatus err = PMCopyAvailablePPDs(domain, &temp);     if((err == noErr) && (temp != NULL))     {         CFArrayAppendArray(destination, temp, CFRangeMake(0, CFArrayGetCount(temp)));         CFRelease(temp);     } }  // Calls AppendPPDs using all PPD domains to gather all available PPDs CFArrayRef MyPMCopyAllAvailablePPDs() {     CFMutableArrayRef ppds = CFArrayCreateMutable(kCFAllocatorDefault, 0, &kCFTypeArrayCallBacks);     AppendPPDs(kSystemPPDDomain, ppds);     AppendPPDs(kLocalPPDDomain, ppds);     AppendPPDs(kNetworkPPDDomain, ppds);     AppendPPDs(kUserPPDDomain, ppds);     AppendPPDs(kCUPSPPDDomain, ppds);     return ppds; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-08 | Note that this issue has been resolved for Mac OS X 10.5 |
| 2007-07-18 | New document that describes a work around for an issue in PMCopyAvailablePPDs on Mac OS X 10.4 and below |


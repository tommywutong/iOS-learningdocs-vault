---
title: Combinations of cupsColorSpace, cupsColorOrder and cupsBitsPerColor values
  supported by Mac OS X
apple_id: DTS10003385
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1368/_index.html
archived_at: '2026-07-18T02:30:26.529260Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1368

# Combinations of cupsColorSpace, cupsColorOrder and cupsBitsPerColor values supported by Mac OS X

## Q:  What combinations of the CUPS PPD keywords cupsColorSpace, cupsColorOrder and cupsBitsPerColor values are supported by Mac OS X?

A: What combinations of the CUPS PPD keywords cupsColorSpace, cupsColorOrder and cupsBitsPerColor values are supported by Mac OS X?

__Table 1__  Supported cupsColorSpace - cupsColorOrder - cupsBitsPerColor combinations

| cupsColorSpace | cupsColorOrder | cupsBitsPerColor | Mac OS X version |
| CUPS_CSPACE_RGB | CUPS_ORDER_CHUNKED | 8 bits per color | 10.2 and later |
| CUPS_CSPACE_K | CUPS_ORDER_CHUNKED | 8 bits per color | 10.2 and later |
| CUPS_CSPACE_K | CUPS_ORDER_BANDED | 1 bit per color | 10.2 and later |
| CUPS_CSPACE_K | CUPS_ORDER_CHUNKED | 1 bit per color | 10.2 and later |
| CUPS_CSPACE_W | CUPS_ORDER_CHUNKED | 8 bits per color | 10.2 and later |
| CUPS_CSPACE_CMYK | CUPS_ORDER_CHUNKED | 8 bits per color | 10.2 and later |
| CUPS_CSPACE_KCMY | CUPS_ORDER_CHUNKED | 8 bits per color | 10.2 and later |
| CUPS_CSPACE_CMYK | CUPS_ORDER_BANDED | 1 bit per color | 10.3 and later |
| CUPS_CSPACE_KCMY | CUPS_ORDER_BANDED | 1 bit per color | 10.3 and later |
| CUPS_CSPACE_KCMYcm | CUPS_ORDER_BANDED | 1 bit per color | 10.3 and later |
| CUPS_CSPACE_CMY | CUPS_ORDER_BANDED | 1 bit per color | 10.3 and later |
| CUPS_CSPACE_RGBW | CUPS_ORDER_CHUNKED | 8 bits per color | 10.4 and later |
| CUPS_CSPACE_RGBA | CUPS_ORDER_CHUNKED | 8 bits per color | 10.4 and later |
| CUPS_CSPACE_K | CUPS_ORDER_CHUNKED | 16 bits per color | 10.4 and later |
| CUPS_CSPACE_W | CUPS_ORDER_CHUNKED | 16 bits per color | 10.4 and later |
| CUPS_CSPACE_RGB | CUPS_ORDER_CHUNKED | 16 bits per color | 10.4 and later |
| CUPS_CSPACE_CMYK | CUPS_ORDER_CHUNKED | 16 bits per color | 10.4 and later |

The allowed values of cupsColorSpace, cupsColorOrder and cupsBitsPerColor and their meaning are documented the CUPS Software Programmer's Manual in the "Device and Bitmap Variables" section. The CUPS Software Programmer's Manual is available at [http://www.cups.org/spm.html](http://www.cups.org/spm.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2005-08-10 | Added combinations supported in Mac OS X 10.4 and later. |
|  | New document. |


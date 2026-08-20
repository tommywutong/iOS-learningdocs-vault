---
title: Public UTIs supported by Mac OS X v10.3
apple_id: DTS10003483
resource_type: QA
platform: macOS
topic: Data Management
technology: CoreServices
published: '2005-02-08'
source_url: https://developer.apple.com/library/archive/qa/qa1406/_index.html
archived_at: '2026-07-18T02:30:31.796569Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1406

# Public UTIs supported by Mac OS X v10.3

## Q:  What are the public UTIs supported by Mac OS X v10.3?

A: UTIs (Uniform Type Identifier) were introduced in Carbon with the Pasteboard Manager on Mac OS X v10.3.

This document lists the public UTIs supported on Mac OS X v10.3. Later releases of Mac OS X will list the public UTIs supported in a new header (UTCoreTypes.h) of the LaunchServices framework.

__Table 1__  public UTIs.

| UTI | Conforms To | Description |
| public.data |  | Base type for any sort of simple byte stream, including files and in-memory data |
| public.text | public.data | Base type for all text-encoded data, including text with markup (HTML, RTF, etc.) |
| public.plain-text | public.text | Text with no markup, unspecified encoding |
| public.utf16-plain-text | public.plain-text | Plain text, UTF-16 encoding, native byte order, no BOM, (OSType 'utxt') |
| public.rtf | public.text | Rich Text Format |
| public.html | public.text | HTML, any version |
| public.xml | public.text | Generic XML |
| com.adobe.pdf | public.data | Adobe PDF |
| public.url | public.data | The bytes of a URL, (OSType 'url ') |
| public.vcard | public.data | VCard format |
| public.image | public.data | Abstract image data |
| public.jpeg | public.image | JPEG image |
| public.jpeg-2000 | public.image | JPEG-2000 image |
| public.tiff | public.image | TIFF image |
| com.apple.pict | public.image | Quickdraw PICT format |

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Lists the public UTIs (Uniform Type Identifiers) used by the Pasteboard in Mac OS X v10.3. |
| 2005-02-08 | New document that lists the public UTIs (Uniform Type Identifiers) used by the Pasteboard in Mac OS X v10.3. |


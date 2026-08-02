---
title: Releasing the iTunes Windows COM from Managed Code
apple_id: DTS40007942
resource_type: QA
platform: macOS
topic: Apple Applications
technology: null
published: '2008-08-21'
source_url: https://developer.apple.com/library/archive/qa/qa1608/_index.html
archived_at: '2026-07-18T02:32:42.108585Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1608

# Releasing the iTunes Windows COM from Managed Code

## Q:  How do I properly release the iTunes for Windows COM object from managed code?

A: How do I properly release the iTunes for Windows COM object from managed code?

The Microsoft .NET Framework common language runtime exposes COM objects through a proxy called the runtime callable wrapper (RCW). A single RCW is created for each COM object, and it maintains a reference count that is incremented every time a COM interface pointer is mapped to it. When the reference count reaches zero, the runtime releases all its references on the unmanaged COM object. Therefore, if all references have not been released on the RCW, the COM object will not be released.

To release COM objects correctly you must call the .NET Framework `Marshal.ReleaseComObject` method. This method decrements the reference count of the supplied RCW. You should use this method to free the underlying COM object as shown in Listing 1 for the iTunes COM:

__Listing 1__  Releasing the iTunes COM using the .NET `Marshal.ReleaseComObject` method.

```
using System.Runtime.InteropServices; using iTunesLib;  iTunesApp iTApp;  ... Marshal.ReleaseComObject(iTApp); // release the iTunes COM iTApp = null;
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-08-21 | New document that describes how to properly release the iTunes Windows COM from managed code |


---
title: Open Directory Plug-in Programming Guide
apple_id: TP40000918
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Dir_Plugin/ProcessingOpenDirectoryRequests/ProcessingOpenDirectoryRequests.html
archived_at: '2026-07-27T06:57:05.780049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Open Directory Plug-in Programming Guide](Introduction.md)


[Next](Processing%20Concurrent%20Requests.md)[Previous](Required%20Entry%20Points.md)

# Retired Document

__Important:__
Support for DirectoryService plug-ins has been deprecated and will be removed in a future release.

A new architecture was introduced in OS X v10.9 to allow the creation of native Open Directory modules. Unlike DirectoryService, `opendirectoryd` uses modules implemented as a standalone process that uses XPC to communicate with `opendirectoryd`. Implementing a module as an XPC service ensures a private address space and improves security and reliability, because modules cannot crash another module or `opendirectoryd`.

# Processing Open Directory Requests

Open Directory passes to the appropriate Open Directory plug-in certain requests from Open Directory clients. The requests correspond to a subset of the Open Directory function calls described in _Open Directory Programming Guide._ Every Open Directory plug-in must be prepared to process each of the requests described in this section even if only to respond that the requested service is not implemented (`eNotYetImplemented`) or not handled (`eNotHandledByThisNode`). To indicate the outcome of processing a request, the plug-in should return a result code from the list of result codes documented in _Open Directory Programming Guide._

The plug-in must be prepared to process requests for each of the Open Directory functions described in this section.

__Table 3-1__  Open Directory functions that cause the `ProcessRequest` entry point to be called

| `dsAddAttribute` | `dsGetDirNodeInfo` |
| `dsAddAttributeValue` | `dsGetRecordAttributeInfo` |
| `dsCloseAttributeList` | `dsGetRecordAttributeValueByID` |
| `dsCloseAttributeValueList` | `dsGetRecordAttributeValueByValue` |
| `dsCloseDirNode` | `dsGetRecordEntry` |
| `dsCloseRecord` | `dsGetRecordList` |
| `dsCreateRecord` | `dsGetRecordReferenceInfo` |
| `dsCreateRecordAndOpen` | `dsOpenDirNode` |
| `dsDeleteRecord` | `dsOpenRecord` |
| `dsDoAttributeValueSearch` | `dsRemoveAttribute` |
| `dsDoAttributeValueSearchWithData` | `dsRemoveAttributeValue` |
| `dsDoDirNodeAuth` | `dsSetAttributeAccess` |
| `dsDoPluginCustomCall` | `dsSetAttributeFlags` |
| `dsDoMultipleAttributeValueSearch` | `dsSetAttributeValue` |
| `dsDoMultipleAttributeValueSearchWithData` | `dsSetAttributeValues` |
| `dsFlushRecord` | `dsSetRecordAccess` |
| `dsGetAttributeEntry` | `dsSetRecordFlags` |
| `dsGetAttributeValue` | `dsSetRecordName` |

As an alternative to processing `dsCloseAttributeList`, `dsCloseAttributeValueList`, `dsGetRecordEntry`, `dsGetAttributeEntry`, and `dsGetAttributeValue` requests in the plug-in, applications can use client-side buffer parsing to process these requests. For information, see the chapter [Client Side Buffer Parsing](Client%20Side%20Buffer%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmjufvjvomi).

See [Runtime Environment](Runtime%20Environment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsmjyfvbuqmznknltc) for information on three special cases in which the `ProcessRequest` entry point of an inactive plug-in is called.

[Next](Processing%20Concurrent%20Requests.md)[Previous](Required%20Entry%20Points.md)

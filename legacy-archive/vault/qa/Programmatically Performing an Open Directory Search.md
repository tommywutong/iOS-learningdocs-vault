---
title: Programmatically Performing an Open Directory Search
apple_id: DTS10004080
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: DirectoryService
published: '2006-09-11'
source_url: https://developer.apple.com/library/archive/qa/qa1462/_index.html
archived_at: '2026-07-18T02:30:52.650924Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1462

# Programmatically Performing an Open Directory Search

## Q:  How do I programmatically search for specific records by matching attributes via the Open Directory API?

A: How do I programmatically search for specific records by matching attributes via the Open Directory API?

You'll need to use the Directory Services Framework, more specifically, the `dsDoAttributeValueSearchWithData` function found within it.

Listing 1 below gives an example:

__Listing 1__  Executing a trivial Open Directory Search.

```
//  Begin variable declaration.  tDirReference                 dirRef; long                          status = eDSNoErr; unsigned long                 numResults = 0; tDataListPtr                  nodePath = NULL; tDirNodeReference             nodeRef; tDataList                     recordTypesToSearchFor; tDataNodePtr                  patternToMatch = NULL; tDataNodePtr                  matchType; tDataListPtr                  requestedAttributes = NULL; tDataBufferPtr                dataBuff = NULL; tContextData                  context = NULL;  //  Initiate the Open Directory Service.  status = dsOpenDirService(&dirRef);  //  Allocate a buffer.  dataBuff = dsDataBufferAllocate(dirRef, 2*1024);  //  Find the default search node. status = dsFindDirNodes(dirRef, dataBuff, NULL, eDSSearchNodeName, &numResults, &context);  //  Acquire a reference to the default search node. status = dsGetDirNodeName(dirRef, dataBuff, 1, &nodePath);  //  Do some cleaning up. dsDataBufferDeAllocate(dirRef, dataBuff); dataBuff = NULL; dataBuff = dsDataBufferAllocate(dirRef, 2*1024);  //  Open root level node for search.  status = dsOpenDirNode(dirRef, nodePath, &nodeRef);  //  Build the tDataList containing the record type that you are searching for;  //  in this case, the record type is "Users".  status = dsBuildListFromStringsAlloc (dirRef, &recordTypesToSearchFor, kDSStdRecordTypeUsers, NULL);  //  Return Records of Users.   //  tDataNodePtr containing the string value to search for within all records.  patternToMatch = dsDataNodeAllocateString(dirRef, "Michael");  //  tDataNodePtr containing the constant value that pertains to the scope of the search.  matchType = dsDataNodeAllocateString(dirRef, kDSAttributesAll);  //  Build a list to contain the requested attributes of the records returned from your search.  requestedAttributes = dsBuildListFromStrings(dirRef, kDS1AttrDistinguishedName, NULL);  //  The actual query.  status = dsDoAttributeValueSearchWithData(nodeRef, dataBuff, &recordTypesToSearchFor, matchType, eDSContains,                     patternToMatch, requestedAttributes, FALSE, &numResults, &context);
```

You will also have to check the return `status` and `context` variables from the `dsFindDirNodes` and `dsDoAttributeValueSearchWithData` calls since:

- If `status` is `eDSBufferTooSmall` then the buffer size needs to be increased. For other return values please refer to the [documentation](https://developer.apple.com/documentation/Networking/Reference/Open_Directory_Ref/index.html).
- If `context` is not `NULL` then there are more items needing to be returned, in which case, you'll need to make subsequent calls to `dsDoAttributeValueSearchWithData` passing in the `context` variable. When you no longer need `context`, call `dsReleaseContinueData` to release the memory associated with it.

It would be wise to check that `numResults` is larger than `0` after the `dsFindDirNodes` call since it is possible that no search node could be returned. Once the above code is executed you'll need to pass `dataBuff` and the appropriate parameters to `dsGetRecordEntry,` `dsGetAttributeEntry,`  and `dsGetAttributeValue` in order to acquire the information that you need.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-09-11 | New document that a short guide on how to programmatically search Open Directory for matching attribute values within records. |


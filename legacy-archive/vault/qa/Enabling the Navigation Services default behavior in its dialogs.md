---
title: Enabling the Navigation Services default behavior in its dialogs
apple_id: DTS10003418
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-10-15'
source_url: https://developer.apple.com/library/archive/qa/qa1384/_index.html
archived_at: '2026-07-18T02:30:29.404287Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1384

# Enabling the Navigation Services default behavior in its dialogs

## Q:  Drag and dropping a file or folder in my Navigation Services dialog does not change the location but this action works in other application. How can I make this working in my application as well?

A: Drag and dropping a file or folder in my Navigation Services dialog does not change the location but this action works in other application. How can I make this working in my application as well?

What you need is a non-`NULL` `eventProc` when you call any of the Navigation Services dialogs creation or execution. Even an `eventProc` which does nothing is fine. That way, the Navigation Services code has a chance to add its default behavior event processing to yours (which does nothing), else, if your `eventProc` is `NULL`, the Navigation Services does not try to add his default behavior, assuming you don't want any behavior at all. And the default behavior event processing is, of course, the one which handles the drag and drop to change the location.

You can use the following `eventProc` shown in Listing 1:

__Listing 1__  An empty event Proc.

```
pascal void myDoNothingEventProc(NavEventCallbackMessage callBackSelector,       NavCBRecPtr callBackParms, void * callBackUD)     {     }
```

And you can specify this `eventProc` with the following Listing 2:

__Listing 2__  Using the empty event Proc.

```
NavEventUPP myDoNothingEventProcUPP = NewNavEventUPP(myDoNothingEventProc);  err = NavCreatePutFileDialog(       &navOptions,       kmyApplicationSignature,       kmyFileType,       myDoNothingEventProcUPP,       clientData,       &navDialog       );  DisposeNavEventUPP(myDoNothingEventProcUPP);
```

In the previous Listing 2, any of the other Navigation Services APIs such as NavPutFile, NavGetFile, NavCreateChooseFileDialog, etc could have been used as well.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-15 | New document that explains how to enable the default behavior of the Navigation Services dialogs. |


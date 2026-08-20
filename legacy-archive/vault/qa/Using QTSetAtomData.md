---
title: Using QTSetAtomData
apple_id: DTS10001754
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-09-17'
source_url: https://developer.apple.com/library/archive/qa/qa1231/_index.html
archived_at: '2026-07-18T02:30:12.718283Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1231

# Using QTSetAtomData

## Q:  I'm using `QTSetAtomData` to modify some atom data, but I'd like to know what this call does with the `atomData` pointer being passed to it.

A: `QTSetAtomData` is used to change the data of a leaf atom. It copies the number of bytes passed in as `dataSize` from the address `atomData` to the contents of atom. It will resize the atom if necessary.

__Listing 1__  .

```
OSErr QTSetAtomData(QTAtomContainer container, QTAtom  atom, long dataSize, void *atomData)
```

When using this function be aware that the position (offset) of any atoms within the `QTAtomContainer` greater than the passed in `QTAtom` will need to be re-found using `QTFindChildByID` or `QTFindChildByIndex`. Also, the passed in `QTAtomContainer` must be unlocked; this call will fail if you've locked the atom container by calling `QTLockAtomContainer`.

[Understanding QuickTime Atoms](https://developer.apple.com/library/archive/documentation/QuickTime/RM/MovieBasics/MTEditing/H-Chapter/8UnderstandingQuickT.html#//apple_ref/doc/uid/TP40000908-UnderstandingQuickTimeAtoms)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-09-17 | Editorial |
| 2003-01-14 | New document that explains what QTSetAtomData does with the data passed into it. |


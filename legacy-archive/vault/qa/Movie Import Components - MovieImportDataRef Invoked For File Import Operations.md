---
title: Movie Import Components - MovieImportDataRef Invoked For File Import Operations
apple_id: DTS40007448
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/qa/qa1596/_index.html
archived_at: '2026-07-18T02:32:21.987887Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1596

# Movie Import Components - MovieImportDataRef Invoked For File Import Operations

## Q:  Did QuickTime 7.4 change the way Movie Import Components are called when importing from files?

A: Yes, QuickTime 7.4 changed how the Movie Toolbox invokes Movie Import Components when specifically importing from files. With the release of QuickTime 7.4, the Movie Toolbox directly calls `MovieImportDataRef` with an `'alis'` (`rAliasType`) Data Reference when importing from files instead of calling `MovieImportFile` with an `FSSpec`.

There are two APIs clients of Movie Import Components may call to invoke an import operation from a file; `MovieImportFile` and `MovieImportDataRef`.

`MovieImportFile` is defined to take a File System Specification Record, or `FSSpec`, as the parameter specifying the name and location of a file. Since the time `MovieImportFile` was defined, use of the `FSSpec` with the Carbon File Manager has been deprecated and superseded by the `FSRef`.


```
pascal ComponentResult MyComponent_MovieImportFile(My_Globals glob,
                                                   const FSSpec *theFile,
                                                   Movie theMovie,
                                                   Track targetTrack,
                                                   Track *usedTrack,
                                                   TimeValue atTime,
                                                   TimeValue *durationAdded,
                                                   long inFlags,
                                                   long *outFlags)
```


`MovieImportDataRef` is defined to use the standard QuickTime Data Reference abstraction, this is the general way QuickTime describes the location of media data.


```
pascal ComponentResult MyComponent_MovieImportDataRef(My_Globals glob,
                                                      Handle dataRef,
                                                      OSType dataRefType,
                                                      Movie theMovie,
                                                      Track targetTrack,
                                                      Track *usedTrack,
                                                      TimeValue atTime,
                                                      TimeValue *durationAdded,
                                                      long inFlags,
                                                      long *outFlags)
```

Developers writing Movie Import Components should implement both selectors to accommodate both older and newer behavior. `MovieImportDataRef` may be considered the designated import API and therefore `MovieImportFile` can simply be implemented by calling `MovieImportDataRef` as shown in Listing 1.

__Listing 1__  Example `MovieImportFile` Component Implementation.

```swift
pascal ComponentResult MyComponent_MovieImportFile(My_Globals glob,
                                                   const FSSpec *theFile,
                                                   Movie theMovie,
                                                   Track targetTrack,
                                                   Track *usedTrack,
                                                   TimeValue atTime,
                                                   TimeValue *durationAdded,
                                                   long inFlags,
                                                   long *outFlags)
{
    ComponentResult err = noErr;
    AliasHandle alias = NULL;

    *outFlags = 0;

    err = NewAliasMinimal(theFile, &alias);
    if (err) return err;

    err = MovieImportDataRef(glob->self,
                            (Handle)alias,
                            rAliasType,
                            theMovie,
                            targetTrack,
                            usedTrack,
                            atTime,
                            durationAdded,
                            inFlags,
                            outFlags);

    if (alias) DisposeHandle((Handle)alias);

    return err;
}
```


Application developers calling Movie Import Components directly to import from files should not call `MovieImportFile` and move to `MovieImportDataRef`. For further details about Data Reference based QuickTime APIs see _[Updating Applications for QuickTime 6](https://developer.apple.com/library/archive/technotes/tn2140/_index.html#//apple_ref/doc/uid/DTS10003526)_.

- _[Updating Applications for QuickTime 6](https://developer.apple.com/library/archive/technotes/tn2140/_index.html#//apple_ref/doc/uid/DTS10003526)_
- _[Tagging Handle and Pointer Data References in QuickTime](https://developer.apple.com/library/archive/technotes/tn1195/_index.html#//apple_ref/doc/uid/DTS10003034)_
- [ElectricImageComponent Sample](https://developer.apple.com/samplecode/ElectricImageComponent/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-11 | New document that discusses how QuickTime 7.4+ invokes Movie Import Components when specifically importing from files. |


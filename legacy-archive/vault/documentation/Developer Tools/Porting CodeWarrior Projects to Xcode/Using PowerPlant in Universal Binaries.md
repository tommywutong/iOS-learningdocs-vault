---
title: Porting CodeWarrior Projects to Xcode
apple_id: '20001708'
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2009-06-30'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/MovingProjectsToXcode/UsingPPlantInUniversalBinaries/UsingPPlantInUniversalBinaries.html
archived_at: '2026-07-15T07:25:16.250710Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Porting CodeWarrior Projects to Xcode](Introduction%20to%20Porting%20CodeWarrior%20Projects%20to%20Xcode.md)


[Next](Where%20to%20Go%20From%20Here.md)[Previous](After%20Importing%20a%20Project.md)

# Using PowerPlant in Universal Binaries

You can use PowerPlant on an Intel-based Macintosh computer only after you make the changes detailed in this section. Most of the substantial changes that you need to make are to the PowerPlant `LStream` class. PowerPlant uses `LStream` for a number of different I/O tasks, of which the most important is reading to and writing from `'PPob'` resources. [Changing LStream Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenruheyti) provides a detailed description of all the `LStream`-related changes that are required.

If you use the `LDataBrowser` PowerPlant class and the `'DBC#'` resource, you might also need to write a resource flipper. See [Flipping the 'DBC#’ Resource Type](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrsgm4tc).

The changes discussed in this section cause `LStream` to always read and write big-endian data. After you make these changes

- `PPob` resources will work correctly on both PowerPC-based and Intel-based Macintosh computers, with the possible exception of custom types used by your application. Custom types will also work correctly if you ensure that the `LStream` constructors used by your custom types employ the streaming methods of `LStream` rather than the byte-manipulation methods.
- Data read from and written to disk or to the network and that is written with `LStream` will be portable between PowerPC-based and Intel-based Macintosh computers, with the exception of calls to the methods shown in Listing 5-1. For calls to those methods, your code should either swap bytes to big-endian format or switch to using the streaming methods of `LStream`.

Make sure that you evaluate all calls to the methods in Listing 5-1 (including calls to any subclassed versions of these methods) to see if they require byte swapping.

__Listing 5-1__  Calls that may require swapping bytes

```
LStream::PutBytes
LStream::WriteData
LStream::WriteBlock
LStream::operator << (Handle inHandle)
LStream::GetBytes
LStream::ReadData
LStream::ReadBlock
LStream::PeekData
LStream::operator >> (Handle &outHandle)
LStream::WritePtr
LStream::ReadPtr
LStream::WriteHandle
LStream::ReadHandle
```

If you have custom classes in a `PPob` resource, you should change their `LStream` constructors to avoid calling `LStream::ReadData`. Specifically, you need to change the code in the same way as the `LStream` constructors for `LControl`, `LListBox`, and other PowerPlant classes are changed in the following sections. The sections, organized by the files you need to change, describe the required code changes:

- [LStream.h](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenruhezdi)
- [LStream.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrvgq3di)
- [LControl.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrvgu4ta)
- [LListBox.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrvgy2tc)
- [LPane.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrvhazte)
- [LPrintout.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrvhe2do)
- [LScroller.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgayto)
- [LTable.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwga4de)
- [LView.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwge2do)
- [LWindow.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgizde)
- [LPopupGroupBox.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgmyte)
- [LControlView.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgm3te)
- [LScrollerView.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgqzte)
- [LPageController.cp](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjxfvbuqmrugewtenrwgq4to)

Change the `operator << (const Rect&inRect)` method from a single `WriteBlock` call to the following:

```
Rect rect;
rect.top = CFSwapInt16HostToBig(inRect.top);
rect.left = CFSwapInt16HostToBig(inRect.left);
rect.right= CFSwapInt16HostToBig(inRect.right);
rect.bottom = CFSwapInt16HostToBig(inRect.bottom);
WriteBlock(&rect, sizeof(rect));
```

Change the `operator << (const Point &inPoint)` method from a single `WriteBlock` call to the following:

```
Point pt;
pt.v = CFSwapInt16HostToBig(inPoint.v);
pt.h = CFSwapInt16HostToBig(inPoint.h);
WriteBlock(&pt, sizeof(pt));
```

Change the `operator << (SInt16 inNum)` method from a single `WriteBlock` call to the following:

```
SInt16 n;
n = CFSwapInt16HostToBig(inNum);
WriteBlock(&n, sizeof(n));
```

Change the `operator << (UInt16 inNum)` method from a single `WriteBlock` call to the following:

```
UInt16 n;
n = CFSwapInt16HostToBig(inNum);
WriteBlock(&n, sizeof(n));
```

Change the `operator << (SInt32 inNum)` method from a single `WriteBlock` call to the following:

```
SInt32 n;
n = CFSwapInt32HostToBig(inNum);
WriteBlock(&n, sizeof(n));
```

Change the `operator << (UInt32 inNum)` method from a single `WriteBlock` call to the following:

```
UInt32 n;
n = CFSwapInt32HostToBig(inNum);
WriteBlock(&n, sizeof(n));
```

Change the `operator << (float inNum)` method from a single `WriteBlock` call to the following:

```
CFSwappedFloat32 swappedFloat;
swappedFloat = CFConvertFloat32HostToSwapped(inNum);
WriteBlock(&swappedFloat, sizeof(swappedFloat));
```

Change the `operator << (bool inBool)` method from a single `WriteBlock` call to the following:

```
UInt32 boolValue;
boolValue = CFSwapInt32HostToBig(inBool);
WriteBlock(&boolValue, sizeof(boolValue));
```

In the `operator >> (Rect &outRect)` method, add this after the `ReadBlock` call:

```
outRect.top = CFSwapInt16BigToHost(outRect.top);
outRect.left = CFSwapInt16BigToHost(outRect.left);
outRect.right= CFSwapInt16BigToHost(outRect.right);
outRect.bottom = CFSwapInt16BigToHost(outRect.bottom);
```

In the `operator >> (Point &outPoint)` method, add the following after the `ReadBlock` call:

```
outPoint.v = CFSwapInt16BigToHost(outPoint.v);
outPoint.h = CFSwapInt16BigToHost(outPoint.h);
```

In the `operator >> (SInt16 &outNum)` method, add the following after the `ReadBlock` call:

`outNum = CFSwapInt16BigToHost(outNum);`

In the `operator >> (UInt16 &outNum)` method, add the following after the `ReadBlock` call:

`outNum = CFSwapInt16BigToHost(outNum);`

In the `operator >> (SInt32 &outNum)` method, add the following after the `ReadBlock` call:

`outNum = CFSwapInt32BigToHost(outNum);`

In the `operator >> (UInt32 &outNum)` method, add the following after the `ReadBlock` call:

`outNum = CFSwapInt32BigToHost(outNum);`

In the `operator >> (float &outNum)` method, replace the `ReadBlock` call with the following:

```
CFSwappedFloat32 swappedFloat;
ReadBlock(&swappedFloat, sizeof(swappedFloat));
outNum = CFConvertFloat32SwappedToHost(swappedFloat);
```

In the `operator >> (bool &outBool)` method, replace the `ReadBlock` call with the following:

```
UInt32 boolValue;
ReadBlock(&boolValue, sizeof(boolValue));
outBool = CFSwapInt32BigToHost(boolValue);
```


In the `operator << (double inNum)` method, change the `#if TARGET_CPU_PPC` block to the following:

```
#if TARGET_CPU_PPC || TARGET_CPU_X86
// PowerPC and Intel doubles -- they're 8 bytes already, so just swap
// if necessary and write.

Assert_(sizeof(inNum) == 8);
CFSwappedFloat64 swappedDouble = CFConvertDoubleHostToSwapped(inNum);
WriteBlock(&swappedDouble, sizeof(swappedDouble));
```

In the `operator >> (double& outNum)` method, change the `#if TARGET_CPU_PPC` block to the following:

```
#if TARGET_CPU_PPC || TARGET_CPU_X86
// PowerPC and Intel doubles -- they're 8 bytes already, so just read
// and swap if necessary.

Assert_(sizeof(outNum) == 8);
CFSwappedFloat64 swappedDouble;
ReadBlock(&swappedDouble, sizeof(swappedDouble));
outNum = CFConvertDoubleSwappedToHost(swappedDouble);
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&controlInfo, sizeof(SControlInfo));`

with the following lines:

```
*inStream >> controlInfo.valueMessage;
*inStream >> controlInfo.value;
*inStream >> controlInfo.minValue;
*inStream >> controlInfo.maxValue;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&listInfo, sizeof(SListBoxInfo));`

with the following lines:

```
*inStream >> listInfo.hasHorizScroll;
*inStream >> listInfo.hasVertScroll;
*inStream >> listInfo.hasGrow;
*inStream >> listInfo.hasFocusBox;
*inStream >> listInfo.doubleClickMessage;
*inStream >> listInfo.textTraitsID;
*inStream >> listInfo.LDEFid;
*inStream >> listInfo.numberOfItems;
```

In the `RestorePlace(LStream*inPlace)` method, replace the following line:

```swift
 inPlace->ReadData(&theRect, sizeof(Rect));
```

with this line:

`*inPlace >> theRect;`

Further down in the method, just under the `if (vScroll != nil)` line, replace this line:

`inPlace->ReadData(&theRect, sizeof(Rect));`

with this line:

`*inPlace >> theRect;`

And once more in the same method, just under the `if (hScroll != nil)` line, replace this line:

`inPlace->ReadData(&theRect, sizeof(Rect));`

with this line:

`*inPlace >> theRect;`

In the `LStream` constructor, replace this line:

`inStream->ReadData(&thePaneInfo, sizeof(SPaneInfo));`

with the following lines:

```
SInt32 viewPtr;
*inStream >> thePaneInfo.paneID;
*inStream >> thePaneInfo.width;
*inStream >> thePaneInfo.height;
*inStream >> thePaneInfo.visible;
*inStream >> thePaneInfo.enabled;
*inStream >> thePaneInfo.bindings.left;
*inStream >> thePaneInfo.bindings.top;
*inStream >> thePaneInfo.bindings.right;
*inStream >> thePaneInfo.bindings.bottom;
*inStream >> thePaneInfo.left;
*inStream >> thePaneInfo.top;
*inStream >> thePaneInfo.userCon;
*inStream >> viewPtr;
thePaneInfo.superView = reinterpret_cast<LView *>(viewPtr);
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&thePrintoutInfo, sizeof(SPrintoutInfo));`

with the following lines:

```
*inStream >> thePrintoutInfo.width;
*inStream >> thePrintoutInfo.height;
*inStream >> thePrintoutInfo.active;
*inStream >> thePrintoutInfo.enabled;
*inStream >> thePrintoutInfo.userCon;
*inStream >> thePrintoutInfo.attributes;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&scrollerInfo, sizeof(SScrollerInfo));`

with the following lines:

```
*inStream >> scrollerInfo.horizBarLeftIndent;
*inStream >> scrollerInfo.horizBarRightIndent;
*inStream >> scrollerInfo.vertBarTopIndent;
*inStream >> scrollerInfo.vertBarBottomIndent;
*inStream >> scrollerInfo.scrollingViewID;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&tableInfo, sizeof(STableInfo));`

with the following lines:

```
*inStream >> tableInfo.numberOfRows;
*inStream >> tableInfo.numberOfCols;
*inStream >> tableInfo.rowHeight;
*inStream >> tableInfo.colWidth;
*inStream >> tableInfo.cellDataSize;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&viewInfo, sizeof(SViewInfo));`

with the following lines:

```
*inStream >> viewInfo.imageSize.width;
*inStream >> viewInfo.imageSize.height;
*inStream >> viewInfo.scrollPos.h;
*inStream >> viewInfo.scrollPos.v;
*inStream >> viewInfo.scrollUnit.h;
*inStream >> viewInfo.scrollUnit.v;
*inStream >> viewInfo.reconcileOverhang;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&windowInfo, sizeof(SWindowInfo));`

with the following lines:

```
*inStream >> windowInfo.WINDid;
*inStream >> windowInfo.layer;
*inStream >> windowInfo.attributes;
*inStream >> windowInfo.minimumWidth;
*inStream >> windowInfo.minimumHeight;
*inStream >> windowInfo.maximumWidth;
*inStream >> windowInfo.maximumHeight;
*inStream >> windowInfo.standardSize.width;
*inStream >> windowInfo.standardSize.height;
*inStream >> windowInfo.userCon;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&cInfo, sizeof(SControlInfo));`

with the following lines:

```
*inStream >> cInfo.valueMessage;
*inStream >> cInfo.value;
*inStream >> cInfo.minValue;
*inStream >> cInfo.maxValue;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&cInfo, sizeof(SControlInfo));`

with the following lines:

```
*inStream >> cInfo.valueMessage;
*inStream >> cInfo.value;
*inStream >> cInfo.minValue;
*inStream >> cInfo.maxValue;
```


In the `LStream` constructor, replace this line:

`inStream->ReadData(&scrollerInfo, sizeof(SScrollerViewInfo));`

with the following lines:

```
*inStream >> scrollerInfo.horizBarLeftIndent;
*inStream >> scrollerInfo.horizBarRightIndent;
*inStream >> scrollerInfo.vertBarTopIndent;
*inStream >> scrollerInfo.vertBarBottomIndent;
*inStream >> scrollerInfo.scrollingViewID;
```


In the `LStream` constructor, replace these lines:

```swift
inStream->ReadData( &mBackColor, sizeof(RGBColor));
inStream->ReadData( &mFaceColor, sizeof(RGBColor));
inStream->ReadData( &mPushedTextColor, sizeof(RGBColor));
```

with the following lines:

```
*inStream >> mBackColor.red;
*inStream >> mBackColor.green;
*inStream >> mBackColor.blue;
*inStream >> mFaceColor.red;
*inStream >> mFaceColor.green;
*inStream >> mFaceColor.blue;
*inStream >> mPushedTextColor.red;
*inStream >> mPushedTextColor.green;
*inStream >> mPushedTextColor.blue;
```


If you use the `LDataBrowser` PowerPlant class, you might be using a `'DBC#'` resource. If so, you will need to write a resource flipper similar to that shown in Listing 5-2.

__Listing 5-2__  Code that flips the `'DBC#'` resource type

```swift
struct DataBrowserColumnSetup {
    DataBrowserTableViewColumnID    propertyID;         // UInt32
    DataBrowserPropertyType         propertyType;       // unsigned long
    SInt32                          nameStrIndex;
    DataBrowserPropertyFlags        propertyFlags;      // UInt32
    UInt16                          minimumWidth;
    UInt16                          maximumWidth;
    UInt16                          initialWidth;
    ControlContentType              btnContentType;     // SInt16
    ControlButtonGraphicAlignment   btnContentAlign;    // SInt16
    SInt16                          btnContentDataID;
    ControlButtonGraphicAlignment   titleAlignment;     // SInt16
    ControlButtonTextPlacement      titlePlacement;     // SInt16
    SInt16                          titleFontTypeID;
    SInt16                          titleFontStyle;
    SInt16                          titleFontSize;
    UInt16                          titleOffset;
};
typedef struct DataBrowserColumnSetup   DataBrowserColumnSetup;

OSStatus FlipDBC_(OSType dataDomain, OSType dataType,
                  short id, void* dataPtr, UInt32 dataSize,
                  Boolean currentlyNative, void* refcon)
{
    DataBrowserColumnSetup *dbc;
    UInt16 count;
    int i;

    if (currentlyNative) {
        count = *(UInt16 *) dataPtr;
        *(UInt16 *) dataPtr = EndianU16_NtoB(count);
    } else {
        count = *(UInt16 *) dataPtr;
        *(UInt16 *) dataPtr = EndianU16_BtoN(count);
    }
    dataPtr += sizeof(UInt16);
    dbc = (DataBrowserColumnSetup *) dataPtr;
    for(i = 0; i < count; i++, dbc++) {
        dbc->propertyID = Endian32_Swap(dbc->propertyID);
        dbc->propertyType = Endian32_Swap(dbc->propertyType);
        dbc->nameStrIndex = Endian32_Swap(dbc->nameStrIndex);
        dbc->propertyFlags = Endian32_Swap(dbc->propertyFlags);
        dbc->minimumWidth = Endian16_Swap(dbc->minimumWidth);
        dbc->maximumWidth = Endian16_Swap(dbc->maximumWidth);
        dbc->initialWidth = Endian16_Swap(dbc->initialWidth);
        dbc->btnContentType = Endian16_Swap(dbc->btnContentType);
        dbc->titleAlignment = Endian16_Swap(dbc->titleAlignment);
        dbc->titlePlacement = Endian16_Swap(dbc->titlePlacement);
        dbc->titleFontTypeID = Endian16_Swap(dbc->titleFontTypeID);
        dbc->titleFontStyle = Endian16_Swap(dbc->titleFontStyle);
        dbc->titleFontSize = Endian16_Swap(dbc->titleFontSize);
        dbc->titleOffset = Endian16_Swap(dbc->titleOffset);
    }
    return noErr;
}
```

[Next](Where%20to%20Go%20From%20Here.md)[Previous](After%20Importing%20a%20Project.md)


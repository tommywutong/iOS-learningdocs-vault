---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Tasks/CreatingTextStorage.html
archived_at: '2026-07-15T07:20:29.712969Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Changing%20Text%20Storage.md)[Previous](Layout%20Geometry-%20The%20NSTextContainer%20Class.md)

# Creating Text Storage

As an abstract class of a [class cluster](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7), allocating and initializing an [NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage) object actually produces an instance of a private subclass. You can use any [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) or [NSMutableAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSMutableAttributedString) initialization method to create an `NSTextStorage` object.

Having created the text storage object, you add [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) objects to the text storage using [addLayoutManager:](https://developer.apple.com/documentation/appkit/nstextstorage/1533459-addlayoutmanager). A single text storage object can have multiple layout managers (which is why this method name begins with “add” rather than “set”).

Creating a text storage object in this way and adding a layout manager is part of the process of assembling the text system programmatically, which is described in more detail in “Creating Text System Objects” in _[Cocoa Text Architecture Guide](../../Cocoa%20Text%20Architecture%20Guide/About%20the%20Cocoa%20Text%20System.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjz)_. You can also create an [NSTextView](https://developer.apple.com/documentation/appkit/nstextview) object and let it assemble the text system automatically, in which case the text view creates (and later deallocates) the text storage object. For more information, see [Creating an NSTextView Programmatically](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextUILayer/Tasks/CreateTextViewProg.html#//apple_ref/doc/uid/20000930).

[Next](Changing%20Text%20Storage.md)[Previous](Layout%20Geometry-%20The%20NSTextContainer%20Class.md)


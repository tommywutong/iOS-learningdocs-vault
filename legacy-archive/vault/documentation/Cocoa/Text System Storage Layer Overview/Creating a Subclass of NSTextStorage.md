---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Tasks/Subclassing.html
archived_at: '2026-07-15T07:20:31.729023Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Document%20Revision%20History.md)[Previous](Tracking%20the%20Size%20of%20a%20Text%20View.md)

# Creating a Subclass of NSTextStorage

[NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage) isn’t a fully concrete class; rather, it is the abstract superclass of a [class cluster](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7). It defines the storage for its [NSLayoutManager](https://developer.apple.com/documentation/appkit/nslayoutmanager) objects and implements some methods, but doesn’t provide the primitive attributed string methods to subclasses. A subclass must define the storage for its attributed string, typically as an instance variable of type [NSMutableAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSMutableAttributedString), override `init` and define its own initialization methods, and implement the primitive methods of both [NSAttributedString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/cl/NSAttributedString) and `NSMutableAttributedString`. The primitive methods are:

- [string](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/string)
- [attributesAtIndex:effectiveRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSAttributedString/attributesAtIndex:effectiveRange:)
- [replaceCharactersInRange:withString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/replaceCharactersInRange:withString:)
- [setAttributes:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/setAttributes:range:)

Beyond these requirements, if a subclass overrides or adds any methods that change its characters or attributes directly, those methods must invoke [edited:range:changeInLength:](https://developer.apple.com/documentation/appkit/nstextstorage/1529793-edited) after performing the change in order to keep the change-tracking information up to date. See the method description for more information.

[Next](Document%20Revision%20History.md)[Previous](Tracking%20the%20Size%20of%20a%20Text%20View.md)


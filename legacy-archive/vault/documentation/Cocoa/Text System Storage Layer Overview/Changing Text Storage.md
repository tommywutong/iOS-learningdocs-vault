---
title: Text System Storage Layer Overview
apple_id: 10000087i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/Tasks/ChangingTextStorage.html
archived_at: '2026-07-15T07:20:29.213151Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text System Storage Layer Overview](Introduction%20to%20Text%20System%20Storage%20Layer%20Overview.md)


[Next](Displaying%20a%20Text%20Container.md)[Previous](Creating%20Text%20Storage.md)

# Changing Text Storage

The behavior of an [NSTextStorage](https://developer.apple.com/documentation/uikit/nstextstorage) object is best illustrated by following the messages you send to change its text.There are three stages to editing a text storage object programmatically:

1. The first stage is to send it a [beginEditing](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/beginEditing) message to announce a group of changes.
2. In the second stage, you send it some editing messages, such as [deleteCharactersInRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/deleteCharactersInRange:) and [addAttributes:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/addAttributes:range:), to effect the changes in characters or attributes. Each time you send such a message, the text storage object invokes [edited:range:changeInLength:](https://developer.apple.com/documentation/appkit/nstextstorage/1529793-edited) to track the range of its characters affected since it received the `beginEditing` message.
3. For the third stage, when you’re done changing the text storage object, you send it the [endEditing](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSAttributedStrngClstr/Description.html#//apple_ref/occ/instm/NSMutableAttributedString/endEditing) message. This causes it to invoke its own [processEditing](https://developer.apple.com/documentation/appkit/nstextstorage/1525980-processediting) method, fixing attributes within the recorded range of changed characters. (See _[Text Attribute Programming Topics](../Text%20Attribute%20Programming%20Topics/Introduction%20to%20Text%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dq2i)_ for information about attribute fixing.)

After fixing its attributes, the text storage object sends a message to each associated layout manager indicating the range in the text storage object that has changed, along with the nature of those changes. The layout managers in turn use this information to recalculate their glyph locations and redisplay if necessary. `NSTextStorage` also keeps a delegate and sends it messages before and after processing edits.

[Next](Displaying%20a%20Text%20Container.md)[Previous](Creating%20Text%20Storage.md)


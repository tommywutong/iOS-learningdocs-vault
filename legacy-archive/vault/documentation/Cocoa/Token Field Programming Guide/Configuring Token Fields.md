---
title: Token Field Programming Guide
apple_id: TP40006555
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TokenField_Guide/TokenFieldsIB/TokenFieldsIB.html
archived_at: '2026-07-15T07:20:43.826616Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Token Field Programming Guide](Introduction%20to%20Token%20Field%20Programming%20Guide%20for%20Cocoa.md)


[Next](Displaying%20the%20Completion%20List.md)[Previous](How%20Token%20Fields%20Work.md)

# Configuring Token Fields

The following sections describe how to set the attributes of token fields , establish common bindings between token fields and controller objects, and to make delegate and target-action connections. You can accomplish most of these tasks in Interface Builder.

You can set the token field attributes listed in Table 3-1 in Interface Builder.

__Table 3-1__  NSTokenField attributes in Interface Builder

| Attribute | Description |
| Token Style | Choose one of Default, Plain, or Rounded. The default token style currently is Rounded—the blue rounded rectangle. Tokens in the plain style are simple text without any background; with the plain text style only one token is allowed per token field.  You can change the token style on a case-by-case basis by implementing the delegation method [tokenField:styleForRepresentedObject:](https://developer.apple.com/documentation/appkit/nstokenfielddelegate/1530203-tokenfield). |
| Comp. Delay | Specify the completion delay for the token field: the period (in seconds) after the user begins typing before the token field displays the completion list. The default value is zero, which means “display the list immediately”. |

The tokenizing character set is an attribute not displayed by Interface Builder. When users enter one of the characters from the current tokenizing character set, it tells the token field to convert the preceding string to a token. The default tokenizing character is the comma; carriage return (or newline character) is not in the set, but is implied in all cases. You can change the tokenizing character set using [setTokenizingCharacterSet:](https://developer.apple.com/documentation/appkit/nstokenfield/1534230-tokenizingcharacterset).

The Interface Builder inspector also displays attributes of the superclasses of [NSTokenField](https://developer.apple.com/documentation/appkit/nstokenfield), namely [NSTextField](https://developer.apple.com/documentation/appkit/nstextfield), [NSControl](https://developer.apple.com/documentation/appkit/nscontrol), and [NSView](https://developer.apple.com/documentation/appkit/nsview). None of the settings for these attributes has a particular consequence for token fields.

For a token field to acquire the capabilities of completion lists, non-string represented objects, and token menus, a delegate must respond to the messages sent by the control. Be sure to connect the delegate outlet to an object in the application that implements the appropriate delegation methods. Also make a target-action connection between the token field and an action method implemented by a target object in the application. You can make these connections in Interface Builder or programmatically.

[Next](Displaying%20the%20Completion%20List.md)[Previous](How%20Token%20Fields%20Work.md)


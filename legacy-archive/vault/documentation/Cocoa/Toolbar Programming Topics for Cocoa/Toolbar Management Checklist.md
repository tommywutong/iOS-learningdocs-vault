---
title: Toolbar Programming Topics for Cocoa
apple_id: 10000109i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Concepts/HowTBsCreated.html
archived_at: '2026-07-15T07:20:47.781400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Toolbar Programming Topics for Cocoa](Introduction%20to%20Toolbars.md)


[Next](Adding%20and%20Removing%20Toolbar%20Items.md)[Previous](How%20Toolbars%20Work.md)

# Toolbar Management Checklist

__Before you begin coding__:

- If you have image-based toolbar items, find or create the images (in the proper size and aspect ratio) and add them to your project as a resource.
- If you have view-based toolbar items, create each view in Interface Builder, specify an outlet for a custom controller object, and connect the view to the outlet.

  If the view is an off-the-shelf palette object, just make an outlet connection.
- Specify or (for default toolbar items) identify the unique string identifiers that you intend to use for toolbars and toolbar items.
- Add to an application menu (usually named View) the menu items Show Toolbar and Customize Toolbar..., connect these to the First Responder icon in the nib file window, and select the actions [toggleToolbarShown:](https://developer.apple.com/documentation/appkit/nswindow/1419554-toggletoolbarshown) and [runToolbarCustomizationPalette:](https://developer.apple.com/documentation/appkit/nswindow/1419284-runtoolbarcustomizationpalette). (Note that [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) automatically changes “Show Toolbar” to “Hide Toolbar” as appropriate.)

For further information, see [Adding and Removing Toolbar Items](Adding%20and%20Removing%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tklkcijbuossdirfa).

__What happens__: The application launches or a document is created or opened, causing a nib file to be loaded and its object unarchived.

- A custom controller class in [awakeFromNib](https://developer.apple.com/documentation/objectivec/nsobject/1402907-awakefromnib) or, for document-based applications, an `NSDocument` subclass in [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) completes the following steps for each toolbar it uses:

  1. It makes a new [NSToolbar](https://developer.apple.com/documentation/appkit/nstoolbar) object using [initWithIdentifier:](https://developer.apple.com/documentation/appkit/nstoolbar/1516975-init).
  2. It sets attributes of the toolbar if the defaults won’t do using [setAllowsUserCustomization:](https://developer.apple.com/documentation/appkit/nstoolbar/1516962-allowsusercustomization), [setAutosavesConfiguration:](https://developer.apple.com/documentation/appkit/nstoolbar/1516992-autosavesconfiguration), and [setDisplayMode:](https://developer.apple.com/documentation/appkit/nstoolbar/1516937-displaymode).
  3. It sets the toolbar’s delegate (usually itself).
  4. It associates the toolbar with a window by sending the NSWindow object a [setToolbar:](https://developer.apple.com/documentation/appkit/nswindow/1419731-toolbar) message.

For further information see [Adding and Removing Toolbar Items](Adding%20and%20Removing%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tklkcijbuossdirfa)

__What happens__: The `NSToolbar` object begins communicating with its delegate in order to populate the toolbar with toolbar items.

1. The window gets the allowed and default toolbar item identifiers:

   - The toolbar object calls the delegate method [toolbarAllowedItemIdentifiers:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516995-toolbaralloweditemidentifiers) to get the total set of possible toolbar items.
   - Unless it finds the default toolbar configuration in user preferences, the toolbar calls the delegate method [toolbarDefaultItemIdentifiers:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516944-toolbardefaultitemidentifiers) to get the default set.

     To have the default configuration saved to and read from user preferences, the `NSToolbar` object’s [autosavesConfiguration](https://developer.apple.com/documentation/appkit/nstoolbar/1516992-autosavesconfiguration) attribute must be set.
   - If certain toolbar items should indicate a selected state, the delegate should implement [toolbarSelectableItemIdentifiers:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516981-toolbarselectableitemidentifiers) to return the identifiers of those toolbar items.
2. The window asks for each [NSToolbarItem](https://developer.apple.com/documentation/appkit/nstoolbaritem) object (by identifier) to insert into the toolbar.

   - To add each toolbar item to the toolbar, the `NSToolbar` object sends [toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516985-toolbar) to the delegate.

     If the `NSToolbarItem` object is image-based, get the image from the application bundle (for example, by using the `NSImage` class method [imageNamed:](https://developer.apple.com/documentation/appkit/nsimage/1520015-imagenamed)) and send [setImage:](https://developer.apple.com/documentation/appkit/nstoolbaritem/1527749-image) to the toolbar item. Also set the toolbar item’s label, palette label, target, and action. You may also set a menu form representation.

     If the toolbar item is view-based, send [setView:](https://developer.apple.com/documentation/appkit/nstoolbaritem/1534039-view) to the toolbar-item object, passing in the outlet to the view. Also set the toolbar item’s label, palette label, its minimum size ([minSize](https://developer.apple.com/documentation/appkit/nstoolbaritem/1531777-minsize)), and its maximum size ([maxSize](https://developer.apple.com/documentation/appkit/nstoolbaritem/1526451-maxsize)). (If you do not set a `minSize` and `maxSize`, the view does not appear because it is sized to zero in both dimensions.) You may also set a menu form representation.
   - If the delegate wants to customize a toolbar item before it is added, it can also implement the [toolbarWillAddItem:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516964-toolbarwilladditem) notification method.

For further information see [Adding and Removing Toolbar Items](Adding%20and%20Removing%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tklkcijbuossdirfa), [Setting a Toolbar Item’s Representation](Setting%20a%20Toolbar%20Item%E2%80%99s%20Representation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdelkcijbuorsgjbcq), [Setting a Toolbar Item’s Size](Setting%20a%20Toolbar%20Item%E2%80%99s%20Size.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tilkciffekrshifba) and [Setting a Toolbar Item’s Size](Setting%20a%20Toolbar%20Item%E2%80%99s%20Size.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tilkciffekrshifba).

__What happens__: Users click toolbar items; the runtime context of the application changes.

- Declare and implement action methods for each of your custom toolbar items, usually in a custom controller class.

  When you create a toolbar item you can identify the selector of each of these methods through the [setAction:](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525723-action) method of `NSToolbarItem`. Also set the target by calling the [setTarget:](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525982-target), usually passing in `self`.
- Validate toolbar items.

  If the toolbar item is image-based, the target of an action should implement [validateToolbarItem:](https://developer.apple.com/documentation/objectivec/nsobject/1524282-validatetoolbaritem) if it wants validation more specialized than the default. If the toolbar item is view-based, you should create a subclass of `NSToolbarItem` for the item and override the [validate](https://developer.apple.com/documentation/appkit/nstoolbaritem/1525295-validate) method.

For further information, see [Validating Toolbar Items](Validating%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tglkciffeorsiirca).

__What happens__: The user chooses the Customize Toolbar menu item.

- As the customization sheet opens, the toolbar object calls the delegate methods `toolbarAllowedItemIdentifiers:` and `toolbarDefaultItemIdentifiers:`. Then as the toolbar adds each toolbar item to the customization palette, it sends to the delegate if the item kind is custom image or custom view.
- When the user adds an item to the toolbar, the toolbar invokes the delegate method [toolbar:itemForItemIdentifier:willBeInsertedIntoToolbar:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516985-toolbar); if a new instance of the toolbar item is needed, the toolbar sends `toolbarWillAddItem:` to the delegate just before it adds the item.
- Just after the user removes an item from the toolbar, the toolbar sends [toolbarDidRemoveItem:](https://developer.apple.com/documentation/appkit/nstoolbardelegate/1516970-toolbardidremoveitem) to the delegate.
- When the user drags the default set to the toolbar, the toolbar reuses as many items already in the toolbar as possible, calling `toolbarDidRemoveItem:` for the items it needs to remove and calling `toolbarWillAddItem:` for the ones it needs to add.

Note that the toolbar does not call any delegate methods when the user closes the customization sheet.

[Next](Adding%20and%20Removing%20Toolbar%20Items.md)[Previous](How%20Toolbars%20Work.md)


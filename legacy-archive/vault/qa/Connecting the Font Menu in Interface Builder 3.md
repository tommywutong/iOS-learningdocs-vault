---
title: Connecting the Font Menu in Interface Builder 3
apple_id: DTS10004555
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2008-01-21'
source_url: https://developer.apple.com/library/archive/qa/qa1571/_index.html
archived_at: '2026-07-18T02:32:19.563789Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1571

# Connecting the Font Menu in Interface Builder 3

## Q:  How do I connect items in the Font or Format menu in Interface Builder 3?

A: Interface Builder 3 provides two standard menus, the Font menu and Format menu, which contain the items most users expect for font interactions. These include displaying the Font Panel, making selected text bold, italic, or underlined, showing the Color Panel, modifying text size, text alignment, kerning and ligature options, and more. AppKit includes a shared NSFontManager instance (a singleton) for each application. Cocoa's NSFontManager provides many of the actions in the font menu; the rest are handled by the first responder.

There are three main steps:

- Open your application's Main Menu nib in Interface Builder 3.
- In IB's Library panel, find the Font (or Format) Menu Item.
- Drag it to your Main Menu.

This creates a custom object in your NIB file of type NSFontManager. At runtime, AppKit will create a single shared instance of NSFontManager. When the object in your nib is unarchived, the NSFontManager class will swap this instance out for the shared instance.

- In IB's Library panel, find "Object"
- Drag it to your nib.
- Select the new Object.
- Open IB's "Identity" Inspector (command-6)
- In the custom class box, enter "NSFontManager"

Some menu items in the Font and Format menus should be connected to the First Responder proxy, others to the Font Manager. The following table contains a reference of all the connections that have to be made for the Format menu to be fully functional. The Font menu is a subset of the Format menu.

__Table 1__  Format Menu Connections

| Menu Item | Destination | Selector |
| Font Menu |  |  |
| Show Fonts | Font Manager | orderFrontFontPanel: |
| Bold | Font Manager | addFontTrait: |
| Italic | Font Manager | addFontTrait: |
| Underline | First Responder | underline: |
| Bigger | Font Manager | modifyFont: |
| Smaller | Font Manager | modifyFont: |
| Kern Menu |  |  |
| Use Default | First Responder | useStandardKerning: |
| Use None | First Responder | turnOffKerning: |
| Tighten | First Responder | tightenKerning: |
| Loosen | First Responder | loosenKerning: |
| Ligature Menu |  |  |
| Use Default | First Responder | useStandardLigatures: |
| Use None | First Responder | turnOffLigatures: |
| Use All | First Responder | useAllLigatures: |
| Baseline Menu |  |  |
| Use Default | First Responder | unscript: |
| Superscript | First Responder | superscript: |
| Subscript | First Responder | subscript: |
| Raise | First Responder | raiseBaseline: |
| Lower | First Responder | lowerBaseline: |
| Show Colors | First Responder | orderFrontColorPanel: |
| Copy Style | First Responder | copyFont: |
| Paste Style | First Responder | pasteFont: |
| Text Menu |  |  |
| Align Left | First Responder | alignLeft: |
| Center | First Responder | alignCenter: |
| Justify | First Responder | alignJustified: |
| Align Right | First Responder | alignRight: |
| Show Ruler | First Responder | toggleRuler: |
| Copy Ruler | First Responder | copyRuler: |
| Paste Ruler | First Responder | pasteRuler: |

- [Font Panel](https://developer.apple.com/documentation/Cocoa/Conceptual/FontPanel/FontPanel.html)
- [NSFontManager Class Reference](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSFontManager_Class/Reference/Reference.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-01-21 | New document that how to connect and configure the Font/Format menus in Interface Builder 3. |


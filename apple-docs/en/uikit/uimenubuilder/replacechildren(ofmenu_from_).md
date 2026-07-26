---
title: 'replaceChildren(ofMenu:from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/replacechildren(ofmenu:from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/replacechildren(ofmenu:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/replacechildren%28ofmenu%3Afrom%3A%29.json'
content_hash: 'sha256:50919b15d901cefb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# replaceChildren(ofMenu:from:)

<sub>Instance Method</sub>

Replaces the elements in a menu with the elements returned by the specified handler block.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func replaceChildren(ofMenu parentIdentifier: UIMenu.Identifier, from childrenBlock: ([UIMenuElement]) -> [UIMenuElement])
```

## Parameters

- `parentIdentifier` — The identifier of the menu containing the children to replace.

- `childrenBlock` — A handler that returns the menu elements that replace the children in the menu associated with `parentIdentifier`. This handler has the following parameter: - **`oldChildren`** — The array of menu elements to replace.

## Discussion

Use this method to add, remove, and rearrange the children elements of a menu. For example, the following code listing uses this method to insert a Copy HTML menu element before Paste in the [UIMenuStandardEdit](../uimenu/identifier-swift.struct/standardedit.md) menu.

```swift
builder.replaceChildren(ofMenu: .standardEdit) { (oldChildren) -> [UIMenuElement] in
    // Find the index of Paste menu element.
    var indexOfPaste = 0
    for (index, menuElement) in oldChildren.enumerated() {
        if let keyCommand = menuElement as? UIKeyCommand {
            if keyCommand.action == #selector(UIResponderStandardEditActions.paste(_:)) {
                indexOfPaste = index
                break
            }
        }
    }
    
    // Create a Copy HTML menu element.
    let copyHTML = UIKeyCommand(title: "Copy as HTML",
                                action: #selector(copyHTML(_:)),
                                input: "c",
                                modifierFlags: [.control, .command])
    
    // Insert Copy HTML before the Paste menu element
    // if found; otherwise, insert Copy HTML at the
    // beginning of the array.
    var newChildren = oldChildren
    newChildren.insert(copyHTML, at: indexOfPaste)
    return newChildren
}
```

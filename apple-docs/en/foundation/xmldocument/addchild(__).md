---
title: 'addChild(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/addchild(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/addchild(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/addchild%28_%3A%29.json'
content_hash: 'sha256:e13da69c5d2ec2ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# addChild(_:)

<sub>Instance Method</sub>

Adds a child node after the last of the receiver’s existing children.

<sub>Mac Catalyst, macOS</sub>

```swift
func addChild(_ child: XMLNode)
```

## Parameters

- `child` — The [XMLNode](../xmlnode.md) object to be added.

## See Also

### Adding and Removing Child Nodes

- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of children at a specified position in the receiver’s array of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver located at a specified position in its array of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces the child node of the receiver located at a specified position in its array of children with another node.
- [- setChildren:](<setchildren(__).md>) — Sets the child nodes of the receiver.

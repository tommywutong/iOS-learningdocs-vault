---
title: 'setChildren(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/xmldocument/setchildren(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/xmldocument/setchildren(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/xmldocument/setchildren%28_%3A%29.json'
content_hash: 'sha256:e053aa975a05de13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [XMLDocument](../xmldocument.md)

# setChildren(_:)

<sub>Instance Method</sub>

Sets the child nodes of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func setChildren(_ children: [XMLNode]?)
```

## Parameters

- `children` — An array of [XMLNode](../xmlnode.md) objects. Each of these objects must represent comments, processing instructions, or the root element; otherwise, an exception is raised. Pass in `nil` to remove all children.

## See Also

### Adding and Removing Child Nodes

- [- addChild:](<addchild(__).md>) — Adds a child node after the last of the receiver’s existing children.
- [- insertChild:atIndex:](<insertchild(__at_).md>) — Inserts a node object at specified position in the receiver’s array of children.
- [- insertChildren:atIndex:](<insertchildren(__at_).md>) — Inserts an array of children at a specified position in the receiver’s array of children.
- [- removeChildAtIndex:](<removechild(at_).md>) — Removes the child node of the receiver located at a specified position in its array of children.
- [- replaceChildAtIndex:withNode:](<replacechild(at_with_).md>) — Replaces the child node of the receiver located at a specified position in its array of children with another node.

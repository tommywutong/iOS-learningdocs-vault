---
title: PHProjectChangeRequest
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.13+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phprojectchangerequest
source_url: 'https://developer.apple.com/documentation/photos/phprojectchangerequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phprojectchangerequest.json'
content_hash: 'sha256:c73c757e4afe4fb7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHProjectChangeRequest

<sub>Class</sub>

A request to change asset data in a Photos project extension.

<sub>macOS</sub>

```swift
class PHProjectChangeRequest
```

## Overview

Make a project change request to alter a project’s title or metadata. Respond to project change requests by updating your user interface as assets are added, modified, or removed.

## Relationships

- **Inherits From**: [PHChangeRequest](phchangerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating Change Requests

- [- initWithProject:](<phprojectchangerequest/init(project_).md>) — Creates a change request around the specified project.
- [title](phprojectchangerequest/title.md) — The title of the change request.
- [projectExtensionData](phprojectchangerequest/projectextensiondata.md) — Compressed project-specific data to use in the change request.

### Responding to Change Requests

- [- setProjectPreviewImage:](<phprojectchangerequest/setprojectpreviewimage(__).md>) — Updates the project preview in Photos.
- [- setKeyAsset:](<phprojectchangerequest/setkeyasset(__).md>) — Sets the key asset representing the project. _(deprecated)_

### Removing Assets

- [removeAssets(_:)](<phprojectchangerequest/removeassets(__)-n825.md>) — Removes assets of a certain type from the collection.
- [removeAssets(_:)](<phprojectchangerequest/removeassets(__)-3ytt3.md>) — Removes assets based on a fetch result.

## See Also

### Classes

- [PHProject](phproject.md) — A representation of a Photos app project extension.

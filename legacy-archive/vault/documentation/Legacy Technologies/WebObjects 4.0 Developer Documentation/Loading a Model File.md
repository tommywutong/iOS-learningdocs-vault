---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/LoadingAModelFile.html
archived_at: '2026-07-18T01:28:13.822563Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOModel.md)
[!](EOModelGroup.md)

---

# Loading a Model File

EOModels are usually loaded from model files built with the EOModeler application rather than built programmatically. EOModel files are typically stored in a project or a framework.

To load an EOModel, provide a model file's path to the constructor. Note that loading an EOModel doesn't have the effect of loading all of its entities. EOModel files can be quite large, so to reduce start-up time, entity definitions are only loaded as needed. This incremental model loading is possible because an EOModel actually consists of one index file and two files for each entity. Models have an `.eomodeld` file wrapper (which is actually a directory), and the individual entity files within the model are in ASCII format. The index file has the name `index.eomodeld`, and it contains the connection dictionary, the adaptor name, and a list of all of the entities in the model. It is this file that gets loaded when you create a new model from a path`initWithContentsOfFile:`. When an entity is loaded, EOModel posts an EOEntityLoadedNotification. The entity files are a `.plist` file that describes the entity and a .`fspec` file that describes any named fetch specifications for that entity.

Some of the EOModel methods contain the string "TableOfContents". An EOModel's "table of contents" corresponds to its `index.eomodeld` file, which is used to access the model's entities. `index.eomodeld` is just the ASCII representation of a model's table of contents.

****

---

[!](EOModel.md)
[!](EOModelGroup.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._

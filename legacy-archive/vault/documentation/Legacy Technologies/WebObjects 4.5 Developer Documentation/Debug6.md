---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Debug6.html
archived_at: '2026-07-15T08:05:14.791384Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Previous Section](Debugging%20Techniques.md)

## Specifying the Project Search Path

When you use Project Builder to build an application, it places the built application inside of the project directory. For WebObjects applications after you build the project, you'll have a __.woa__ directory inside of the project directory. This is typically the copy of the application you want to debug. If you use this default setup, WebObjects uses the components, script files, images, and other resources from the project directory instead of the copies inside of the __.woa__ directory while you debug the project. This way, you can edit scripts (__.html__, __.wod__, __.wos__ files) or change image files in your project without having to rebuild or even restart the application.
Sometimes, you want to debug framework code as well as application code. Other times, you might have moved the __.woa__ directory outside of the project directory but you still want to use the project's copies of resource files instead of those in the __.woa__ directory's. In these cases, you should set the NSProjectSearchPath user default. NSProjectSearchPath should point to the directory that contains all of your projects. WebObjects looks in the directories specified by NSProjectSearchPath for a project that has the same name as the application or framework being loaded (note that the project name is defined inside __PB.project__ and is _not_ the project's directory name). If it finds a project, it uses the resources from the project directory instead of the resources inside the __.woa__ directory.
You can change NSProjectSearchPath on a command line as follows:

```
% defaults write NSGlobalDomain NSProjectSearchPath
'("someDirectory", "someOtherDirectory", ...)'
```

[!Table of Contents](Debugging%20a%20WebObjects%20Application.md) [!Next Section](Debug7.md)

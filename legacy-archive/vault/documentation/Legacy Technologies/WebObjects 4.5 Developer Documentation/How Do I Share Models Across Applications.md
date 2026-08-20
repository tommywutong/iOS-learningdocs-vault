---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/FAQ8.html
archived_at: '2026-07-15T08:03:19.093496Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](Should%20I%20Make%20Foreign%20Key%20Attributes%20Class%20Properties.md)

# How Do I Share Models Across Applications?

You should put shared models in a shared framework. Enterprise Objects Framework automatically looks for models in the frameworks used by your application (both at run-time, and at design time in EOModeler, Interface Builder, and WebObjects Builder). Also put the enterprise object classes that correspond to the model in the framework.
In order for Enterprise Objects Framework to find a model in a framework, that framework must be built and installed. During design, Enterprise Objects Framework looks at the model in the installed version of the framework (not in the source version of the framework project). This can result in Interface Builder and WebObjects Builder not seeing the changes in the source version of the model since it's looking at the version in the installed framework, rather than at the one in your source directory. You can tell Enterprise Objects Framework to look for models in the source version of your framework projects by using the following commands (executed in a shell):

```
defaults write NSGlobalDomain
EOProjectSourceSearchPath"($(HOME)/myProjectsDirectory1,
/myOtherProjectsDirectory)"
```


Then, when EOModeler, Interface Builder, or WebObjects Builder look for models contained in one of your frameworks, it first searches all project directories within __$(HOME)/myProjectsDirectory1__ and __/myOtherProjectsDirectory__ before searching for the built versions.
[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](Entity-Relationship%20Modeling.md)

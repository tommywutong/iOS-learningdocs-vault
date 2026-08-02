---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies30.html
archived_at: '2026-07-15T07:54:36.226316Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies29.md)

# Refining Your Model

The model created for you by the wizard is just a starting point. For most applications, you need to do some additional work to your model to make it useful in your application. To refine your model so that it can be used in the Movies application, you'll ultimately need to do all of the following:

- Remove primary and foreign keys as class properties.
- Add relationships to your model if the wizard didn't have enough information to add them for you.
- Configure your model's relationships in the Advanced Relationship Inspector.
- Generate source files for the Talent class.

These steps are described in more detail throughout the rest of this tutorial.

## Opening Your Model

- In Project Builder, click the Resources category.
- Select __Movies.eomodeld__.
- Double-click the model icon.
!

Project Builder opens your model file in EOModeler, launching EOModeler first if it isn't already running. EOModeler displays your model in the Model Editor. It lists the entities for the tables you specified in the wizard-Movie, MovieRole, and Talent.!

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies31.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

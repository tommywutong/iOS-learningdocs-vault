---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/CreatingModels5.html
archived_at: '2026-07-18T01:18:00.706083Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20a%20New%20Model.md) [!Previous Section](What%20a%20New%20Model%20Includes.md)

# Updating Your Model

When you create a new model in EOModeler, the New Model Wizard prompts you to select the tables you want to include, as described in[Choosing the Tables to Include](Creating%20a%20New%20Model-2.md#apple-gezdanrx). But what if you decide at a later point that you want your model to include tables you didn't select when you first created it? Or what if your database has been modified, and you want your model to reflect the changes?

To update an existing model, choose Model ! New Updated Model. This creates a new model that you can use for cutting and pasting from. Using the New Updated Model command doesn't have a destructive effect on your original model-it just gives you a second model to use for "spare parts."
When you invoke New Updated Model, EOModeler opens a Select Tables panel (shown in [Figure 9](#apple-ge2tgmju)) that lets you specify the tables you want in the "spare parts" model. By default, the Select Tables panel selects only tables that aren't represented in your working model; accepting the selection creates a new, complementary model.

!

Figure 9. Selecting Tables for the New Updated Model

[!Table of Contents](Creating%20a%20New%20Model.md) [!Next Section](Checking%20for%20Consistency.md)

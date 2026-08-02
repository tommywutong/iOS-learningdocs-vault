---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/EnterpriseObjects/EOTools/CreatingModels6.html
archived_at: '2026-07-18T01:18:02.267894Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOF Tools and Techniques](Enterprise%20Objects%20Framework%20Tools%20and%20Techniques.md)

[!Table of Contents](Creating%20a%20New%20Model.md) [!Previous Section](Updating%20Your%20Model.md)

# Checking for Consistency

EOModeler provides consistency checking to confirm that your model is valid. For example, a model that has entities without primary keys or relationships without join components is not valid.
You can explicitly check your model at any point by choosing Model ! Check Consistency. Consistency checking is also invoked automatically whenever you save your model. When a consistency check occurs and inconsistencies are found, the Consistency Check panel appears with a list of diagnostic messages, as shown in [Figure 10](#apple-ge2tgmrx).

!

Figure 10. Checking for Consistency

If you prefer for EOModeler not to run the consistency check when you save, you can turn off this behavior with the Preferences panel.
[!Table of Contents](Creating%20a%20New%20Model.md) [!Next Section](Using%20the%20Model%20Editor.md)

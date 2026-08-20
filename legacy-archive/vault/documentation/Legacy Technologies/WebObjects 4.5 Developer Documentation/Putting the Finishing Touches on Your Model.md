---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/JavaClient/JavaClientTutorial.2a.html
archived_at: '2026-07-15T08:09:07.626264Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Creating a Java Client Application: A Tutorial

[!](Tutorial.md) [!](Transferring%20Movies%20Between%20Studios.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md)

---

# Putting the Finishing Touches on Your Model

You are almost ready to add custom behavior to your enterprise objects. But first you need to put a few finishing touches on your model.

In[Adding Relationships](Adding%20Relationships.md#apple-gm3dmmrt)
, you added relationships between the Studio and Movie entities. Now you need to verify or add a few additional relationships to your model. You might find that the relationship already exists, but just the name needs to be changed:

From the Movie (source) entity:

- 

  Form a to-many relationship to the MovieRole (destination) entity.
- 

  The source attribute is __movieID__. The destination attribute is __movieID__.
- 

  Name the relationship __roles__.
- 

  Form a to-one relationship to the PlotSummary (destination) entity.
- 

  The source attribute is __movieID__. The destination attribute is __movieID__.
- 

  Name the relationship __plotSummary__.

From the Talent (source) entity:

- 

  Form a to-many relationship to the MovieRole (destination) entity.
- 

  The source attribute is __talentID__. The destination attribute is __talentID__.
- 

  Name the relationship __roles__.
- 

  Form a to-one relationship to the TalentPhoto (destination) entity.
- 

  The source attribute is __talentID__. The destination attribute is __talentID__.
- 

  Name the relationship __photo__.

From the MovieRole (source) entity:

- 

  Form a to-one relationship to the Movie (destination) entity.
- 

  The source attribute is __movieID__. The destination attribute is __movieID__.
- 

  Name the relationship __movie__.
- 

  Form a to-one relationship to the Talent (destination) entity.
- 

  The source attribute is __talentID__. The destination attribute is __talentID__.
- 

  Name the relationship __talent__.

At this point your model is complete. There might be other relationships in your model, but the above relationships are the most important for our example project. Looking at your model using the Diagram View (select the model icon and choose Tools !
Diagram View) gives you an overview of the entities in the model and their relationships to other entities.

!

---

© 1999 Apple Computer, Inc. – (Last Updated 13 Sep 99)

[!](Tutorial.md) [!](Transferring%20Movies%20Between%20Studios.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects-2.md)

---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.1f.html
archived_at: '2026-07-15T07:59:39.380855Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.1e.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.20.md)

##  Putting the Finishing Touches on Your Model

You are almost ready to add custom behavior to your enterprise objects. But first you need to put a few finishing touches on your model.

In[Adding Relationships](CSJ_Tutorial.1b.md#apple-gm3dmmrt)
, you added relationships between the Studio and Movie entities. Now you need to verify or add a few additional relationships to your model. You might find that the relationship already exists, but just the name needs to be changed:

From the Movie (source) entity:

- Form a _to-many_ relationship to the MovieRole (destination) entity.

- The source attribute is __movieID__
  . The destination attribute is __movieID__
  .
  - Name the relationship __roles__
    .

  - Form a _to-one_ relationship to the PlotSummary (destination) entity.

    The source attribute is __movieID__
    . The destination attribute is __movieID__
    .
  
  - Name the relationship __plotSummary__
    .

    From the Talent (source) entity:

    - Form a _to-many_ relationship to the MovieRole (destination) entity.

    - The source attribute is __talentID__
      . The destination attribute is __talentID__
      .
  
  - Name the relationship __roles__
    .

  - Form a _to-one_ relationship to the TalentPhoto (destination) entity.

  - The source attribute is __talentID__
    . The destination attribute is __talentID__
    .
  
  - Name the relationship __photo__
    .

    From the MovieRole (source) entity:

    - Form a _to-one_ relationship to the Movie (destination) entity.

    - The source attribute is __movieID__
      . The destination attribute is __movieID__
      .
  
  - Name the relationship __movie__
    .

  - Form a _to-one_ relationship to the Talent (destination) entity.

  - The source attribute is __talentID__
    . The destination attribute is __talentID__
    .
  
  - Name the relationship __talent__
    .

    At this point your model is complete. There might be other relationships in your model, but the above relationships are the most important for our example project. Looking at your model using the Diagram View (select the model icon and choose Tools !
    Diagram View) gives you an overview of the entities in the model and their relationships to other entities.

    ###### 

    !

  ---

  \xA9 1999 Apple Computer, Inc.

  [Previous](CSJ_Tutorial.1e.md) | [Back Up One Level](Creating%20a%20Java%20Client%20WebObjects%20Application.md) | [Next](CSJ_Tutorial.20.md)

  Copyright © 2016 Apple Inc. All rights reserved.

  - [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
  - [Privacy Policy](http://www.apple.com/privacy/)

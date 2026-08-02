---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies38.html
archived_at: '2026-07-18T01:22:54.577927Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies37.md)

## Configuring a Repetition

Now configure MovieDetails' repetition in a way similar to the way Main's repetition is configured. First you need to create a new variable to bind to the repetition's __item__ attribute.

- Use the Add Variable/Method command to add a new variable, __movieRole,__ whose type is set to the MovieRole entity.

Don't create set and get methods for __movieRole__. You won't need accessor methods because the variable is used only within the MovieDetails component and shouldn't be visible to any other classes.

- Bind __movieRoleDisplayGroup__.__displayedObjects__ to the repetition's __list__ attribute.
- Bind __movieRole__ to the repetition's __item__ attribute.
- Bind __movieRole__.__toTalent__.__firstName__ to the __value__ attribute of the first string in the repetition.
- Bind __movieRole__.__toTalent__.__lastName__ to the __value__ attribute of the second string.
- Bind __movieRole__.__roleName__ to the __value__ attribute of the last string.

When you're done, the repetition bindings should look like the following:

!

## Running Movies

Be sure that all your project's files are saved (including the components in WebObjects Builder and the model in EOModeler), and build and run your application. In the Main page, select a movie and click the Movie Details link. Now, in addition to displaying all the movie's information, the Movie Details page should also display the movie's roles and actors.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

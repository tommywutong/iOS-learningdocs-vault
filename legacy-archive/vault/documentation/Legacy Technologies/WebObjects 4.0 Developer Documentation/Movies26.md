---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies26.html
archived_at: '2026-07-18T01:22:25.127413Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Adding%20the%20MovieDetails%20Page.md)

## Storing the Selected Movie

Now, in the MovieDetails component, create a variable that holds the application's selected movie. Later on, you'll add code to the __Main.java__ class that assigns Main's selected movie to this variable.

- Choose Add Variable/Method from the pull-down menu.

!

- Name the variable selectedMovie.
- Set the variable's type to Movie.

Movie isn't actually a class; it's an entity. It's listed in the combo box as a type along with entries for all the entities in your model. When you choose an entity as the type for your variable, WebObjects Builder recognizes that the variable is an enterprise object. Using information in the model, WebObjects Builder can determine the entity's corresponding enterprise object class and the properties of that class.

- Check the "An instance variable" box.
- Check the "A method returning the value" box.
- Check the "A method setting the value" box.
- Click Add.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies27.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

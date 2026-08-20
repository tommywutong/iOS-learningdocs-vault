---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.4c.html
archived_at: '2026-07-15T08:08:17.176769Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Setting%20Up%20a%20Master-Detail%20Configuration.md) [!](Adding%20a%20Repetition.md) [!](Running%20Movies-3.md)

---

#  Configuring a Repetition

Now configure MovieDetails' repetition in a way similar to the way Main's repetition is configured. First you need to create a new variable to bind to the repetition's __item__ attribute.

1. 

   Use the Add Key command to add a new variable, __movieRole,__ whose type is set to the MovieRole entity.

   Don't create set and get methods for __movieRole__. You won't need accessor methods because the variable is used only within the MovieDetails component and shouldn't be visible to any other classes.
2. 

   Bind __movieRoleDisplayGroup__.__displayedObjects__ to the repetition's __list__ attribute.
3. 

   Bind __movieRole__ to the repetition's __item__ attribute.
4. 

   Bind __movieRole__.__toTalent__.__firstName__ to the __value__ attribute of the first string in the repetition.
5. 

   Bind __movieRole__.__toTalent__.__lastName__ to the __value__ attribute of the second string.
6. 

   Bind __movieRole__.__roleName__ to the __value__ attribute of the last string.

   When you're done, the repetition bindings should look like the following:

   !

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Setting%20Up%20a%20Master-Detail%20Configuration.md) [!](Adding%20a%20Repetition.md) [!](Running%20Movies-3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

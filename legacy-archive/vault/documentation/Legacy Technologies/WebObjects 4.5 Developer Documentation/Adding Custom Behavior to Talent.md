---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.56.html
archived_at: '2026-07-15T08:08:27.251699Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md) [!](Generating%20Custom%20Enterprise%20Object%20Classes.md) [!](Providing%20Default%20Values%20in%20MovieRole.md)

---

#  Adding Custom Behavior to Talent

Now add the __fullName__ method to Talent and bind it to the browser.

1. 

   Open __Talent.java__ in Project Builder.

   The class file declares instance variables for all of Talent's class properties (__firstName__ and __lastName__) and implements set and get methods for those instance variables.
2. 

   Add the method, __fullName__, as follows.

   public String fullName(){

      return firstName() + " " + lastName();

   }

   After you save, __fullName__ appears in the object browser of WebObjects Builder as a property of Talent.
3. 

   Bind __talent.fullName__ to the browser's __value__ attribute.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md) [!](Generating%20Custom%20Enterprise%20Object%20Classes.md) [!](Providing%20Default%20Values%20in%20MovieRole.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

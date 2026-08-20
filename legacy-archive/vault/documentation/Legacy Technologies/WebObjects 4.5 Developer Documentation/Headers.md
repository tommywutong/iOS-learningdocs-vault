---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.9.html
archived_at: '2026-07-15T08:11:27.808363Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Classes.md) [!](Subprojects.md)

---

#  Headers

The Headers suitcase contains header files for projects that use Objective-C.

#  Other Sources

The Other Sources suitcase contains compiled code that doesn't belong to a particular class.

#  Resources

The Resources suitcase contains files that are needed by your application at run time, but which do not need to be in the web server's document root (and hence will not be accessible to users). It includes:

- 

  Configuration files
- 

  EOModel files
- 

  API files containing the keys defined by a component (for example, __Main.api__
  ) that other components can bind to (see [Reusable Components](Reusable%20Components.md#apple-geytamzw)
  ) and the rules for binding the keys. WebObjects Builder uses these files to check if a reusable component is used correctly.

#  Web Server Resources

The Web Server Resources suitcase contains files, such as images and sounds that must be under the web server's document root at run time. When developing your application, you place these files in your project directory and add them to the project (see [Adding or Deleting Items From a Project](Adding%20or%20Deleting%20Items%20From%20a%20Project.md#apple-ge4tsnzy)
). When you build your project, Project Builder copies the files in this suitcase into the WebServerResources folder of your application wrapper (see [The Application Wrapper](The%20Application%20Wrapper.md#apple-geydgmbq)
).

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](The%20Structure%20of%20a%20WebObjects%20Application%20Project.md) [!](Classes.md) [!](Subprojects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

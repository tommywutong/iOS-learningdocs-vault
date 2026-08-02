---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.27.html
archived_at: '2026-07-15T07:59:53.232445Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.26.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.28.md)

###  Adding Client-side Subprojects

You can add more than one client-side subproject to your project, especially if you want to use a framework. The subprojects containing EOInterfaceController subclasses and their nib files have to have a special project type: EOJavaClientSubproject.

To add a subproject of this type

1. Open your project in Project Builder.

2. Choose New Subproject from the Project menu.

3. In the New Subproject panel, type a name for your subproject

4. Make sure that the pop-up list displays the project type EOJavaClientSubproject.

5. Click OK.

This procedure adds only the subproject; it does not add an interface-controller subclass, a nib file, or any other files (except makefiles). It also does not add __EOJavaClient.framework__
to the root project's list of frameworks.

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.26.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.28.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

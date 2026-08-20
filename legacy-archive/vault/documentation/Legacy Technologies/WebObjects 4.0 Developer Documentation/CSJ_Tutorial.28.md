---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/JavaClient/CSJ_Tutorial.28.html
archived_at: '2026-07-15T07:59:53.855173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[JavaClient Tutorial](Creating%20a%20Java%20Client%20WebObjects%20Application.md)

_Creating a Java Client WebObjects Application_

[Previous](CSJ_Tutorial.27.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.29.md)

###  Adding Interface Controller Subclasses and Nib Files

To add an EOInterfaceController subclass with a new interface file to your client-side subproject

1. Select the Interfaces bucket in your EOJavaClientSubproject subproject

2. Choose New In Project from the File menu.

3. In the New File panel, enter the name for the new EOInterfaceController subclass and its interface file.

4. Click OK.

   The WebObjects Java Client Interface Wizard then appears, asking you to choose templates and other options for the interface.

5. Select the options that you want for the new interface file.

6. Follow the subsequent instructions until completion.

After finishing the wizard, ProjectBuilder will add two files to your client-side subproject: a source (__.java__
) file for the EOInterfaceController subclass and the nib file that is owned by the interface controller.

When you create a Java Client project, the EOInterfaceController subclass and its interface file by default have the same name as your application. If you rename these files, you must make adjustments elsewhere in your project, as described in "[Manual Adjustments to Java Client Projects](CSJ_Tutorial.2a.md#apple-gmztgnby)
."

---

\xA9 1999 Apple Computer, Inc.

[Previous](CSJ_Tutorial.27.md) | [Back Up One Level](CSJ_Tutorial.26.md) | [Next](CSJ_Tutorial.29.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

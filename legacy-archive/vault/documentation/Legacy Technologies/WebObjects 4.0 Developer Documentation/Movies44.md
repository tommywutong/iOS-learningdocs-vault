---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies44.html
archived_at: '2026-07-18T01:23:02.375080Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies43.md)

## Adding Insert, Save, and Delete Buttons

Now add the buttons that let users insert, save, and delete MovieRoles. When you're done, it should look like the following:

!

- Inside the form, add three image buttons below the Role Name text field.
- Inspect the first active image element.
- Bind the __filename__ attribute to the text (including the quotes) "DBWizardInsert.gif".
- Follow the same procedure to set the second image's __filename__ attribute to the text (including the quotes) "DBWizardUpdate.gif".
- Set the last image's __filename__ attribute to the text (including the quotes) "DBWizardDelete.gif".

The WODisplayGroup class defines the actions __insert__ and __delete__. You'll bind to the Insert/New and Delete buttons. It doesn't, however, provide a save method. You'll have to provide that yourself.

- Copy the __saveChanges__ method from the __Main.java__ class and paste it into the __MovieDetails.java__ class:

```
public void saveChanges() throws Exception {
    try {

this.session().defaultEditingContext().saveChanges();
    }
    catch (Exception exception) {
        System.err.println("Cannot save changes ");
        throw exception;
    }
}
```

- Bind __movieRoleDisplayGroup.insert__ to the Insert/New image's __action__ attribute.
- Bind the __saveChanges__ method to the "Save to database" image's __action__ attribute.
- Bind __movieRoleDisplayGroup.delete__ to the Delete image's __action__ attribute.

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

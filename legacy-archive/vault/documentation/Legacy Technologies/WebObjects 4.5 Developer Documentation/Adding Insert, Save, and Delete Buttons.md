---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.52.html
archived_at: '2026-07-15T08:08:24.045740Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Configuring%20the%20Browser.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md)

---

#  Adding Insert, Save, and Delete Buttons

Now add the buttons that let users insert, save, and delete MovieRoles. When you're done, it should look like the following:!

1. 

   Inside the form, add three image buttons below the Role Name text field.
2. 

   Inspect the first active image element.
3. 

   Bind the __filename__ attribute to the text (including the quotes) "DBWizardInsert.gif".
4. 

   Follow the same procedure to set the second image's __filename__ attribute to the text (including the quotes) "DBWizardUpdate.gif".
5. 

   Set the last image's __filename__ attribute to the text (including the quotes) "DBWizardDelete.gif".

   The WODisplayGroup class defines the actions __insert__ and __delete__, which you'll bind to the Insert/New and Delete buttons. It doesn't, however, provide a save method. You'll have to provide that yourself.
6. 

   Copy the __saveChanges__ method from the __Main.java__ class and paste it into the __MovieDetails.java__ class:

   public void saveChanges() throws Exception {

      try {

        this.session().defaultEditingContext().saveChanges();

      }

      catch (Exception exception) {

        System.err.println("Cannot save changes ");

        throw exception;

      }

   }
7. 

   Bind __movieRoleDisplayGroup.insert__ to the Insert/New image's __action__ attribute.
8. 

   Bind the __saveChanges__ method to the "Save to database" image's __action__ attribute.
9. 

   Bind __movieRoleDisplayGroup.delete__ to the Delete image's __action__ attribute.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Configuring%20the%20Browser.md) [!](Adding%20Behavior%20to%20Your%20Enterprise%20Objects.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

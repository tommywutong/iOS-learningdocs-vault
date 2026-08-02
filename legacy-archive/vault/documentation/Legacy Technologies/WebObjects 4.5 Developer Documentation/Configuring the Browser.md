---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.51.html
archived_at: '2026-07-15T08:08:23.650197Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Adding%20a%20Talent%20Display%20Group.md) [!](Adding%20Insert%2C%20Save%2C%20and%20Delete%20Buttons.md)

---

#  Configuring the Browser

Create your browser's bindings. The steps are similar to those for creating bindings for a repetition.

1. 

   Bind __talentDisplayGroup.displayedObjects__ to the browser's __list__ attribute.
2. 

   Bind __talent__ to the browser's __item__ attribute.
3. 

   Bind __talent.lastName__ to the browser's __value__ attribute.

   The __value__ attribute tells the browser what string to display. For each __item__ in its __list__, the browser evaluates the __item__'s __value__.

   The browser in the MovieDetails page should display the actors' full names, but there isn't an attribute for full name. In the next section, you'll create a custom Talent class that implements a __fullName__ method, but for now just use __talent.lastName__ as the __value__ attribute.

   A browser also has a __selections__ attribute that should be bound to an array of objects. A browser's selection can be zero, one, or many objects; but in the Talent browser, the selection should refer to a single object. Consequently, you need to add two methods to manage the browser's selection: one to return an array containing the selected Talent and one to set the selected Talent from an array object.
4. 

   Add the method __talentSelection__ to the __MovieDetails.java__ class as follows:

   public NSArray talentSelection() {

      EOEnterpriseObject aTalent;

      EOEnterpriseObject aMovieRole =

        (EOEnterpriseObject)movieRoleDisplayGroup.selectedObject();

      if (aMovieRole == null){

        return null;

      }

      aTalent = (EOEnterpriseObject)aMovieRole.valueForKey("toTalent");

      if (aTalent == null){

        return null;

      } else {

        return new NSArray(aTalent);

      }

   }

   Because the browser expects an array for its __selections__ attribute, this method packages the selected MovieRole's __talent__ object in an array. If the selected MovieRole object is __null__, __talentSelection__ simply returns __null__ to indicate that the browser shouldn't set a selection.
5. 

   Add the method __setTalentSelection__ as follows:

   public void setTalentSelection(NSArray talentArray){

      if (talentArray.count() > 0){

        EOEnterpriseObject aMovieRole =

          (EOEnterpriseObject)movieRoleDisplayGroup.selectedObject();

        EOEnterpriseObject selectedTalent =

          (EOEnterpriseObject)talentArray.objectAtIndex(0);

        aMovieRole.addObjectToBothSidesOfRelationshipWithKey(

          selectedTalent, "toTalent");

      }

   }

   Again because the browser uses an array for its __selections__ attribute, the __setTalentSelection__ method must take an array as its argument. If the size of __talentArray__ is nonzero, then this method sets the selected MovieRole's __talent__ to the first object in the array. Note that by default, a user can't select more than one actor in a browser.

   With the addition of these methods, WebObjects Builder now displays __talentSelection__ in MovieDetail's object browser.
6. 

   Bind __talentSelection__ to the browser's __selections__ attribute.

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Updating%20Objects%20in%20the%20Detail%20Display%20Group.md) [!](Adding%20a%20Talent%20Display%20Group.md) [!](Adding%20Insert%2C%20Save%2C%20and%20Delete%20Buttons.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

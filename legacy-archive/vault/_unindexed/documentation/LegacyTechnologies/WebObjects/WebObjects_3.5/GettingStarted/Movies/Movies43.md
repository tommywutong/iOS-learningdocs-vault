---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies43.html
archived_at: '2026-07-15T07:54:57.430232Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies42.md)

## Configuring the Browser

In a way similar to the way you create bindings for a repetition, create your browser's bindings.

- Bind __talentDisplayGroup.displayedObjects__ to the browser's __list__ attribute.
- Bind __talent__ to the browser's __item__ attribute.
- Bind __talent.lastName__ to the browser's __value__ attribute.

The __value__ attribute tells the browser what string to display. For each __item__ in its __list__, the browser evaluates the __item__'s __value__.

The browser in the MovieDetails page should display the actors' full names, but there isn't an attribute for full name. In the next section, you'll create a custom Talent class that implements a __fullName__ method, but for now just use __talent.lastName__ as the __value__ attribute.

A browser also has a __selections__ attribute that should be bound to a vector of objects. A browser's selection can be zero, one, or many objects; but in the Talent browser, the selection should refer to a single object. Consequently, you need to add two methods to manage the browser's selection: one to return a vector containing the selected Talent and one to set the selected Talent from a vector object.

- Add the method __talentSelection__ to the __MovieDetails.java__ class as follows:

```
public ImmutableVector talentSelection () {
    EnterpriseObject aTalent;
    EnterpriseObject aMovieRole =
        (EnterpriseObject)movieRoleDisplayGroup.selectedObject();

    if (aMovieRole == null) {
        return null;
    }

    aTalent = (EnterpriseObject)aMovieRole.valueForKey("talent");
    if (aTalent == null) {
        return null;
    } else {
        EnterpriseObject talentArray[] = {aTalent};
        return new ImmutableVector(talentArray);
    }
}
```


Because the browser expects a vector for its __selections__ attribute, this method packages the selected MovieRole's __talent__ object in a vector. If the selected MovieRole object is __null__, __talentSelection__ simply returns __null__ to indicate that the browser shouldn't set a selection.

- Add the method __setTalentSelection__ as follows:

```
public void setTalentSelection(ImmutableVector talentVector) {
    if (talentVector.size() > 0) {
        EnterpriseObject aMovieRole =
            (EnterpriseObject)movieRoleDisplayGroup.selectedObject();
        EnterpriseObject selectedTalent =
            (EnterpriseObject)talentVector.firstElement();

        aMovieRole.addObjectToBothSidesOfRelationshipWithKey(
                selectedTalent,
                "talent"
        );
    }
}
```


Again because the browser uses a vector for its __selections__ attribute, the __setTalentSelection__ method must take a vector as its argument. If __talentVector__'s size is nonzero, then this method sets the selected MovieRole's __talent__ to the first object in the vector. Note that by default, a user can't select more than one actor in a browser.

With the addition of these methods, WebObjects Builder now displays __talentSelection__ in MovieDetail's object browser.

- Bind __talentSelection__ to the browser's __selections__ attribute.

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies44.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

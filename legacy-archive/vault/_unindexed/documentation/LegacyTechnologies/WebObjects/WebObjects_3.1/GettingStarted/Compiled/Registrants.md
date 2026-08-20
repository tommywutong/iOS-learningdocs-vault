---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/Registrants.html
archived_at: '2026-07-15T07:48:25.987689Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](MainComponent.md)

# Create a second component

When users click the Show All Registrants button, the Registration application displays a second page containing the list of registrants. You'll now create the second page of the application.

- In the Registration application window, click the plus sign to add a new component.
- Type __Registrants__ as the name of the component and press Enter.

A new component window is displayed.

!

## Create the component's interface

The Registrants component uses a repetition to display the information in the list of registrants.

- Drag a WORepetition element from the Abstract Elements palette to the Registrants component window.
- Drag three WOStrings from the Abstract Elements palette into the WORepetition.
!

## Create variables

Now Registrants needs a variable that will contain the list the WORepetition is to display.

- Create a variable in the Registrants component, name it __myNameList__, and make it an array of type aPerson.
!

## Bind elements to the script

- Bind __myNameList__ to the repetition's list attribute.

WebObjects Builder creates a variable named __aPerson__ and binds to the repetition's __item__ attribute. __aPerson__ is an aPerson dictionary.

- Bind the three WOStrings to the three attributes in __aPerson__ as shown below:
!

## Implement Registrants

- Open the Script window, and change the Registrants implementation to look like this:

```
    import next.util.*;
    import next.wo.*;

    public class Registrants extends Component {
        ImmutableHashtable aPerson;
        ImmutableVector myNameList;

        public void awake() {
            myNameList = ((Application)
                application()).manager().registrants();
        }

        public void setAPerson(ImmutableHashtable newPerson) {
            aPerson = newPerson;
        }
    }
```


In the __awake__ method, Registrants accesses the list of all registered people through the Application object's __manager__ instance variable and assigns it to the __myNameList__ instance variable. This is done in __awake__ so that Registrants retrieves the list before the page is displayed.

__setAPerson__ is invoked when the WORepetition iterates through __myNameList__. It assigns the __aPerson__ variable to the method's argument.

__Note:__ Be sure to change the declarations of __myNameList__ and __aPerson__ as shown above.

- You're done implementing Registrants, so save and close the component. Choose File ! Save All to make sure that the entire application is saved.

## Add Registrants.wo to the project

As a final step before compiling, you need to add __Registrants.wo__ to the project in Project Builder. Project Builder must know about __Registrants.wo__ so that the file __Registrants.java__ is compiled during the build. If you had written __Registrants.wo__ in WebScript, it wouldn't be necessary to add the component to the file because WebScript files are not needed during the build cycle.

- Double-click the word Interfaces in Project Builder's browser.
- Select __Registrants.wo__ and click Open.
!

[!Table of Contents](compiled.book.md) [!Next Section](Build.md)

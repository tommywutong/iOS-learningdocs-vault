---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/State/ComponentObjAndState.html
archived_at: '2026-07-15T07:52:13.330874Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](StateTOC.md) [!Previous Section](SessionObjAndState.md)

## Component Objects and Component State

In WebObjects, state can also be scoped to a component, such as a dynamically generated page or a reusable component within a page. Common uses for component state include storing:

- A list of items that a user can choose from within a particular page
- The user's selection from that list
- Information that the users enters in a form
- Default values for a component's attributes

Component state typically includes the data that a page displays, such as a list of choices to present to the user. Suppose a user requests the page that lists these choices. The component that represents the page must initialize itself with the choice data and then return the response page. This completes one cycle of the request-response loop. Now, suppose the user looks at the list of choices, selects the third item, and submits a new request. The same component must be present in this second cycle to identify the choice and take the appropriate action. In short, component state often needs to persist from one cycle of the request-response loop to the next.
A simple example of component state can be seen in the first page of the DodgeLite sample application, which lists models, prices, and types of vehicles for the user to choose from (see [Figure 32](#apple-gq3tgmy)).

!Figure 32. First Page of the DodgeLite Example
This component declares instance variables for the values displayed in the browser and for the user's selection from the browsers. Before the page can be sent to the user, the instance variables that hold the values to be displayed (model, price, type) are initialized:

```
    // Java DodgeLite Main.java
    ImmutableVector models, prices, types;
    MutableVector selectedModels, selectedPrices, selectedTypes;
    String model, price, type;

    public Main() {
        super();
        java.util.Enumeration en;

        Application woApp = (Application)application();
        en = woApp.modelsDict().elements();
        models = new MutableVector();
        while (en.hasMoreElements())
            ((MutableVector)models).addElement(en.nextElement());
        en = woApp.typesDict().elements();
        while (en.hasMoreElements())
            ((MutableVector)types.addElement(en.nextElement());
        prices = woApp.prices();
    }
    // WebScript DodgeLite Main.wos
    id models, model, selectedModels;
    id prices, price, selectedPrices;
    id types, type, selectedTypes;

    - init {
        id anApplication = [WOApplication application];
        [super init];
        models = [[anApplication modelsDict] allValues];
        types = [[anApplication typesDict] allValues];
        prices = [anApplication prices];
        return self;
    }
```


The selectedModels, selectedPrices, and selectedTypes instance variables are bound to the selections attributes of the three WOBrowsers and so will contain the user's selections when the Display Cars button is clicked.
When a user starts a session of the DodgeLite application, the Main component's initialization method is invoked, initializing the component's instance variables from data accessed through the application object. From this point on, the Main component and its instance variables become part of the state stored for that user's session of the DodgeLite application. When the session is released, the component is also released. However, there are other techniques that allow you to control resource allocation on a component basis, as you'll see later in this chapter.
As with the session state, a component's state is accessible to other objects within the same session. As the result of a user's action, for example, it's quite common for one component to create the component for the next page and set its state. Looking again at the DodgeLite application, consider what happens when the user makes a selection in the first page and clicks Display Cars. The displayCars method in the Main component is invoked:

```
    // Java DodgeLite Main.java
    public Component displayCars()
    {
        SelectedCars selectedCarsPage =
            (SelectedCars)application().pageWithName("SelectedCars");

        ...

        selectedCarsPage.setModels(selectedModels);
        selectedCarsPage.setTypes(selectedTypes);
        selectedCarsPage.setPrices(selectedPrices);
        ...
        selectedCarsPage.fetchSelectedCars();

        return (Component)selectedCarsPage;
    }
    // WebScript DodgeLite Main.wos
    - displayCars
    {
        id selectedCarsPage = [[self application]
            pageWithName:@"SelectedCars"];

        ...

        [selectedCarsPage setModels:selectedModels];
        [selectedCarsPage setTypes:selectedTypes];
        [selectedCarsPage setPrices:selectedPrices];
        ...
        [selectedCarsPage fetchSelectedCars];

        return selectedCarsPage;
    }
```


The new component is created by sending a pageWithName: message to the application object. A series of messages is then sent to this new object to set its state before the object is returned as the response page.
Component state persists until the component object is deallocated, an action that can occur for various reasons, as described in the section ["Controlling Component State"](ControllingComponentState.md#apple-gy3do).

[!Table of Contents](StateTOC.md) [!Next Section](StorageStratsIntro.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

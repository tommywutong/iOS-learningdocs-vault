---
title: WebObjects Java Client Programming Guide
apple_id: TP30001017
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/DesktopApplications/T10CustomListControllers/T10CustomListControllers.html
archived_at: '2026-07-18T02:18:40.269146Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Java Client Programming Guide](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)


[Next](Using%20HTML%20on%20the%20Client.md)[Previous](Localizing%20Dynamic%20Components.md)

# Building Custom List Controllers

The public methods provided by the controller factory (`com.webobjects.eogeneration.EOControllerFactory`) allow you to dynamically generate user interfaces for many types of tasks throughout your application. However, it doesn’t provide methods for all types of tasks, such as list controllers. This topic describes how to programmatically create a list controller.

_Problem:_ You want to display a list controller containing the enterprise objects returned by a fetch.

_Solution:_ Programmatically create a list controller.

The following method constructs a list controller by first creating a generic controller, then by asking the controller factory for a list controller based on the generic controller and an entity name, and then by invoking `listObjectsWithFetchSpecification` to fetch enterprise objects into the list controller.

```

public void listWithEntityName(String entityName, EOFetchSpecification fs) {
    EOControllerFactory f = EOControllerFactory.sharedControllerFactory();

    EOController controller = f.controllerWithSpecification(new NSDictionary (new
       Object[] {entityName, EOControllerFactory.ListTask,
        EOControllerFactory.TopLevelWindowQuestion}, new Object[]
        {EOControllerFactory.EntitySpecification, EOControllerFactory.TaskSpecification,
        EOControllerFactory.QuestionSpecification}), true);

    if (controller != null) {
        EOListController listController =         (EOListController)f.controllerWithEntityName(controller,
           EOControllerFactory.List.class, entityName);
    listController.listObjectsWithFetchSpecification(fs);
    listController.setEditability(EOEditable.NeverEditable);
    listController.makeVisible();
    }
}
```

[Next](Using%20HTML%20on%20the%20Client.md)[Previous](Localizing%20Dynamic%20Components.md)


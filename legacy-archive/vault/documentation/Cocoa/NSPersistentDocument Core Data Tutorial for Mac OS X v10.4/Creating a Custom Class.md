---
title: NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.
apple_id: TP40008168
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSPersistentDocumentTutorial104/03_CustomClass/customClass.html
archived_at: '2026-07-15T07:16:50.609193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.](Introduction%20to%20NSPersistentDocument%20Core%20Data%20Tutorial%20for%20Mac%20OS%20X%20v10.4.md)


[Next](Adding%20a%20Department%20Object.md)[Previous](Creating%20the%20Project%2C%20Model%2C%20and%20Interface.md)

This document will not be modified in the future.

# Creating a Custom Class

There are three parts to implementing and using a custom Employee class for the application. First, you create the class files and update the managed object model. Second, you implement the accessor method for the derived value, and ensure that key-value observing notifications are sent when any of the value’s components changes. Third, you implement a method to initialize the employee ID for new employees.

1. In Xcode, either create a new Objective-C class and set its superclass and other details manually, or create a default implementation of a managed object class using the data modeling tool. Both achieve the same result, but through different paths. The significant advantage to using the modeling tool is that it can also auto-generate accessor and validation methods for you—in this case, however, there's no need to do so.

   To create a custom managed object class manually, perform the following steps.

   1. Create a new Objective-C class. Call the class Employee.
   2. In the Employee class’s header file, change its superclass to `NSManagedObject`.

   To create a custom managed object class using the Xcode data modeling tool, perform the following steps:

   1. In Xcode, select the data model and ensure that it is the frontmost editor—for example, simply click inside the model diagram view. (Xcode does not display the Managed Object Class option in the next step unless you do this.)
   2. Select File > New File to show the New File Assistant. In the file type outline view select Design > Managed Object Class and press Next.
   3. In the subsequent pane select the current project and target, then again press Next.
   4. In the subsequent pane (Managed Object Class Generation), select the Employee entity and uncheck the relevant boxes to specify that the implementation should not contain custom accessor or validation methods.
   5. Press Finish. Xcode creates the files for the Employee class.
2. In the data model (use the entity detail pane, or edit the name directly in the Class column in the entity browser), change the class name for the Employee entity from `NSManagedObject` to `Employee`.

The value of `fullNameAndID` is a concatenation of, and hence dependent on, the values of `lastName`, `firstName`, and `employeeID`. To ensure that the derived value is updated whenever any of its components changes, you must invoke the key-value observing method that specifies that a key is dependent on others—`setKeys:triggerChangeNotificationsForDependentKey:`. This method is typically invoked in a class’s `initialize` method.

1. In the Employee class’s header file, add a declaration for an instance method, `-(NSString *)fullNameAndID`. (Note that this is the only modification—other than the change to the superclass made in the first step—that you need to make to the header file. In particular, there is no need to add any instance variables.)
2. In the implementation file, implement the `fullNameAndID` method. It concatenates the first and last names and the employee ID, as illustrated in the example below.

```objc
- (NSString *)fullNameAndID
{
    return [NSString stringWithFormat:@"%@, %@ (%@)",
            [self valueForKey:@"lastName"],
            [self valueForKey:@"firstName"],
            [self valueForKey:@"employeeID"]];
}
```
3. In the Employee class, implement `initialize` as follows:

```objc
+ (void)initialize {
    if (self == [Employee class])
    {
        NSArray *keys = [NSArray arrayWithObjects:
            @"lastName", @"firstName", @"employeeID", nil];
        [self setKeys:keys
triggerChangeNotificationsForDependentKey:@"fullNameAndID"];
    }
}
```
4. In the nib file, change the `contentValues` binding for the pop-up menu. Set the model key path to `fullNameAndID` (the other values remain the same).

You may also add `fullNameAndID` to the data model as a transient string attribute. (In this case, since the value is solely read-only and dependent on other attributes, there is no functional benefit, but it is worth doing so that the model more fully communicates the entity’s behavior.)

Build and run the application again. You should find that the manager pop-up properly displays the full name and ID of each employee, and that the menu item titles update as you change any of the individual components.

What the steps so far have not addressed, however, is the need to ensure that the value of fullNameAndID is unique when new employees are added.

The application could benefit from a means of initializing a managed object when it is created—or more specifically, the first time it is added to the object graph. The init method (more correctly, the class’s designated initializer, `initWithEntity:insertIntoManagedObjectContext:`) is not appropriate since it is called each time the object is instantiated (when it is first created, and whenever it is subsequently retrieved from the persistent store). Core Data provides a special initialization method, `awakeFromInsert`, which is called once and only once in the lifetime of a managed object, on the first occasion it is inserted into a managed object context. This may be useful to, for example, set the creation date of a record. Contrast this with `awakeFromFetch`, which is called on subsequent occasions an object is fetched from a data store.

The following implementation is crude (and should not be used in a production application—the initial tempID reverts to `1` every time the application is launched), it serves, however, to quickly illustrate the principle.

```objc
- (void)awakeFromInsert
{
    static int tempID = 1;

    [super awakeFromInsert];
    [self setValue:[NSNumber numberWithInt:tempID++]
            forKey:@"employeeID"];
}
```


Build and run the application again. You should find that as new employees are added to the document, the employee ID is set, and the ID is incremented for each new employee. More importantly, it is now possible to differentiate between all the employees in the Managers pop-up menu.

Most of the task goals have now been met—primarily by creating a custom class to represent the Employee entity and implementing business logic.

A subtle point here is the interaction between the model and the employees array controller. Recall that you use the array controller to add new employees to the document. When the user interface was created, however, it was not configured to manage instances of a particular class. Instead it was configured to manage an entity (in this case, Employee). When you first built and tested the application, the model specified that employees should be represented by `NSManagedObject`. When the array controller created a new employee, therefore, it created a new instance of `NSManagedObject` (and set its entity description accordingly). After you updated the model, however, to specify that employees be represented by Employee, when the array controller created a new employee, it created a new instance of Employee. You will see in principle how this works in the next section when you create an instance of the Department entity.

The complete listing for the implementation of Employee class up to this point is given in Listing 3-1.

__Listing 3-1__  Implementation of the Employee class

```objc
#import <CoreData/CoreData.h>
@interface Employee : NSManagedObject
{
}
+ (void)initialize;
- (NSString *)fullNameAndID;
- (void)awakeFromInsert;
@end


@implementation Employee

+ (void)initialize
{
    if (self == [Employee class])
    {
        NSArray *keys = [NSArray arrayWithObjects:
                @"lastName", @"firstName", @"employeeID", nil];
        [self setKeys:keys triggerChangeNotificationsForDependentKey:@"fullNameAndID"];
    }
}

- (NSString *)fullNameAndID
{
    return [NSString stringWithFormat:@"%@, %@ (%@)",
            [self valueForKey:@"lastName"],
            [self valueForKey:@"firstName"],
            [self valueForKey:@"employeeID"]];
}

- (void)awakeFromInsert
{
    static int tempID = 1;

    [super awakeFromInsert];
    [self setValue:[NSNumber numberWithInt:tempID++]
            forKey:@"employeeID"];
}

@end
```


The content of the pop-up button that displays the list of employees is currently unsorted. This can make it difficult to find an employee to set as another's manager. You can ensure that the pop-up menu's content is sorted by creating a sort descriptor to associate with the array controller that manages the collection of managers and rearranging the controller's contents prior to displaying the pop-up.

1. Add outlets to the MyDocument class header file for the pop-up button and the managers array controller.

```
IBOutlet NSPopUpButton *managerPopup;
IBOutlet NSArrayController *managersArrayController;
```
2. In Interface Builder, import the header into the MyDocument nib file, and make the connections as appropriate—connect the File's Owner's new `managerPopup` outlet to the pop-up menu, and the `managersArrayController` outlet to the Employees array controller that provides the content for the pop-up menu.
3. In the MyDocument class, implement a `windowControllerDidLoadNib:` method. This method does two things:

   1. It sets an array of sort descriptors (actually an array containing a single sort descriptor) for the managers array controller;
   2. It registers the document object as an observer of `NSPopUpButtonWillPopUpNotification` events posted by the manager pop-up menu.

```objc
- (void)windowControllerDidLoadNib:(NSWindowController *)windowController
{
    [super windowControllerDidLoadNib:windowController];

    // Create a sort descriptor to sort on "fullNameAndID"
    NSSortDescriptor *sortDescriptor = [[[NSSortDescriptor alloc]
            initWithKey:@"fullNameAndID" ascending:YES] autorelease];

    // Set the sortDescriptors for the managers array controller
    [managersArrayController setSortDescriptors:[NSArray arrayWithObject:sortDescriptor]];

    [[NSNotificationCenter defaultCenter] addObserver:self
                selector:@selector(rearrangeManagersArrayController:)
                name:NSPopUpButtonWillPopUpNotification
                object:managerPopup];
}
```
4. In the MyDocument class, implement a `rearrangeManagersArrayController:` method to rearrange the objects in the managers array controller.

```objc
- (void)rearrangeManagersArrayController:(NSNotification *)note
{
    [managersArrayController rearrangeObjects];
}
```

Now build and test the application. You should find that as you add and edit employees, whenever you activate the managers pop-up button its contents are sorted alphabetically.

[Next](Adding%20a%20Department%20Object.md)[Previous](Creating%20the%20Project%2C%20Model%2C%20and%20Interface.md)


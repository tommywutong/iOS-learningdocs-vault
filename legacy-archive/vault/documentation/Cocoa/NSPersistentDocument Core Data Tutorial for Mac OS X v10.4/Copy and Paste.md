---
title: NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.
apple_id: TP40008168
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSPersistentDocumentTutorial104/05_CopyAndPaste/copyAndPaste.html
archived_at: '2026-07-15T07:16:51.569659Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.](Introduction%20to%20NSPersistentDocument%20Core%20Data%20Tutorial%20for%20Mac%20OS%20X%20v10.4.md)


[Next](Localizing%20and%20Customizing%20Model%20Property%20Names%20and%20Error%20Messages.md)[Previous](Adding%20a%20Department%20Object.md)

This document will not be modified in the future.

# Copy and Paste

Most applications support copy and paste. Copy and paste of managed objects is broadly similar to that of other objects, except that you need to be careful about how much of the object graph you copy.

The focus of this chapter is on how to copy managed objects, not how to provide an architecture for copy and paste. In this example, therefore, a simplistic approach is taken—the document object implements `cut:`, `copy:`, and `paste:`, and only supports copying of employees selected in the table view. There are many variants that could be implemented, this example illustrates just one approach. Moreover, basic Cocoa techniques such as archiving, key-value coding, and creating and setting outlets in a nib file, are not explained in detail.

Although it is not strictly necessary to modify the Employee class to support copy and paste, it makes sense to implement custom business logic in one place rather than distributing it throughout the application. The main decision you must make, however, is what it means to copy an employee—what properties of an employee are copied. It seems obvious that first name, last name, and salary should be copied. In this example, it is unlikely that department, manager, or direct reports should be copied. The department is set during the paste operation. If you copy the manager or the direct reports, you are likely to end up copying the whole object graph as you add those objects to the copy. Moreover, copying related objects presents difficulties in cases where a given object may be referred to more than once—you need to ensure uniqueness in the copied graph. Finally, the employee ID requires a judgement call. Whether or not you choose to copy it depends on the semantics of copy (or particularly of paste) in the application.

To abstract out some of this logic, declare and implement a class method—`copyKeys`—that returns an array of keys of attributes to be copied. To support copy of an employee both as an object and as a string (to paste into another application), declare and implement instance methods to return a dictionary and a string representation of the object.

1. In the Employee class, declare and implement a class method, `copyKeys`, as follows:

```objc
+ (NSArray *)copyKeys {
    static NSArray *copyKeys = nil;
    if (copyKeys == nil) {
        copyKeys = [[NSArray alloc] initWithObjects:
            @"firstName", @"lastName", @"salary", @"employeeID", nil];
    }
    return copyKeys;
}
```
2. In the Employee class, declare and implement an instance method, `dictionaryRepresentation`, as follows:

```objc
- (NSDictionary *)dictionaryRepresentation
{
    return [self dictionaryWithValuesForKeys:[[self class] copyKeys]];
}
```
3. In the Employee class, declare and implement an instance method, `stringDescription`, as follows. (Note that you are discouraged from overriding the `description` method.)

```objc
- (NSString *)stringDescription
{
    NSString *stringDescription = [self fullNameAndID];
    NSString *managerString = @"none";
    Employee *manager = [self valueForKey:@"manager"];
    if (manager != nil) {
        managerString = [manager fullNameAndID];
    }
    stringDescription = [stringDescription stringByAppendingFormat:
        @"; Manager: %@", managerString];
    return stringDescription;
}
```


In order to copy, you need to know what the current selection is. You can get this information most easily from the employees array controller. You can also define a label for the employee pasteboard type.

1. In the MyDocument class header file, declare an IBOutlet `employeeTableController` of type `NSArrayController`.

```
IBOutlet NSArrayController *employeeTableController;
```
2. In Interface Builder, import the header into the document nib file, and connect the File's Owner's `employeeTableController` outlet to the employee array controller.
3. In the MyDocument class implementation file, declare the global string `EmployeesPBoardType`. Also import the Employee header file.

```objc
#import "Employee.h"
NSString *EmployeesPBoardType = @"EmployeesPBoardType";
```
4. In the MyDocument class implementation file, implement a `copy:` method. It first retrieves the employee array controller’s selected objects. If no objects are selected, it returns immediately. Note also the declaration of an integer, `i`, that is used later.

```objc
- (void)copy:sender {

    NSArray *selectedObjects = [employeeTableController selectedObjects];
    unsigned i, count = [selectedObjects count];
    if (count == 0) {
        return;
    }
    // implementation continues....
}
```
5. Create two mutable arrays, one to contain the dictionary representations of the objects to copy, the other to contain the string representations. Iterate over the array of selected employees, adding the appropriate representation of each object to the corresponding array.

```
NSMutableArray *copyObjectsArray = [NSMutableArray arrayWithCapacity:count];
NSMutableArray *copyStringsArray = [NSMutableArray arrayWithCapacity:count];
Employee *employee;

for (i = 0; i < count; i++) {
    employee = (Employee *)[selectedObjects objectAtIndex:i];
    [copyObjectsArray addObject:[employee dictionaryRepresentation]];
    [copyStringsArray addObject:[employee stringDescription]];
}
```
6. Declare the types to be copied for the general pasteboard, and set the corresponding values. Since the dictionary representation of an employee contains only property list types, you can simply create an archive of the array to set as the data for the custom pasteboard. For the string representation, concatenate the individual strings, separating them with a newline character.

```
NSPasteboard *generalPasteboard = [NSPasteboard generalPasteboard];
[generalPasteboard declareTypes:
        [NSArray arrayWithObjects:EmployeesPBoardType, NSStringPboardType, nil]
                          owner:self];
NSData *copyData = [NSArchiver archivedDataWithRootObject:copyObjectsArray];
[generalPasteboard setData:copyData forType:EmployeesPBoardType];
[generalPasteboard setString:
    [copyStringsArray componentsJoinedByString:@"\n"]
                     forType:NSStringPboardType];
```


The complete listing for the `copy:` method is shown in Listing 5-1.

__Listing 5-1__  Complete listing of the `copy`: method

```objc
- (void)copy:sender {

    NSArray *selectedObjects = [employeeTableController selectedObjects];
    unsigned i, count = [selectedObjects count];
    if (count == 0) {
        return;
    }

    NSMutableArray *copyObjectsArray = [NSMutableArray arrayWithCapacity:count];
    NSMutableArray *copyStringsArray = [NSMutableArray arrayWithCapacity:count];
    Employee *employee;

    for (i = 0; i < count; i++) {
        employee = (Employee *)[selectedObjects objectAtIndex:i];
        [copyObjectsArray addObject:[employee dictionaryRepresentation]];
        [copyStringsArray addObject:[employee stringDescription]];
    }
    NSPasteboard *generalPasteboard = [NSPasteboard generalPasteboard];
    [generalPasteboard declareTypes:
            [NSArray arrayWithObjects:EmployeesPBoardType, NSStringPboardType, nil]
                              owner:self];
    NSData *copyData = [NSArchiver archivedDataWithRootObject:copyObjectsArray];
    [generalPasteboard setData:copyData forType:EmployeesPBoardType];
    [generalPasteboard setString:
        [copyStringsArray componentsJoinedByString:@"\n"]
                         forType:NSStringPboardType];
}
```


Build and run the application.

Although you have not yet implemented support for paste within the application, you should be able to paste a string representation of the current selection into, for example, a TextEdit document or a Mail message.

In order to paste, you create employee objects from the array of dictionaries on the pasteboard. You must insert these into the document’s managed object context, and add them to the department’s employees relationship.

1. In the MyDocument class implementation file, implement a `paste:` method. It first retrieves the employee array data from the pasteboard (using the custom pasteboard type). If there is no data, return immediately.

```objc
- (void)paste:sender {

    NSPasteboard *generalPasteboard = [NSPasteboard generalPasteboard];
    NSData *data = [generalPasteboard dataForType:EmployeesPBoardType];
    if (data == nil) {
        return;
    }
    // implementation continues....
}
```
2. To create the new employees, you need to unarchive the array of dictionaries. You also need the document’s managed object context and a way to add each new employee to the department object’s employees relationship. You can address the latter requirement using key-value coding with the `mutableSetValueForKey:` method:

```
NSArray *employeesArray = [NSUnarchiver unarchiveObjectWithData:data];
NSManagedObjectContext *moc = [self managedObjectContext];
NSMutableSet *departmentEmployees = [[self department] mutableSetValueForKey:@"employees"];
```
3. For each item in the employees array, create a new employee object and establish the relationship between it and the department. The easiest way to create a new employee is using the `NSEntityDescription` class method `insertNewObjectForEntityForName:inManagedObjectContext:`. This returns a new instance of the class specified in the managed object model to represent the Employee entity. You can then set the attribute values of the new object from the dictionary using key-value coding.

   To establish the relationship between the employee and department, you can either add the employee to the department’s employees relationship or set the department for the employee directly. (Since the relationship is modeled in both directions, and the inverse relationships properly specified, the referential integrity is maintained automatically.) For the purpose of illustrating manipulation of a to-many relationship, do the former:

```
unsigned i, count = [employeesArray count];
for (i = 0; i < count; i++) {
    Employee *newEmployee;
    newEmployee = (Employee *)[NSEntityDescription insertNewObjectForEntityForName:@"Employee"
             inManagedObjectContext:moc];
    [newEmployee setValuesForKeysWithDictionary:[employeesArray objectAtIndex:i]];
    [departmentEmployees addObject:newEmployee];
}
```


The complete listing for the `paste:` method is shown in Listing 5-2.

__Listing 5-2__  Complete listing of the `paste:` method

```objc
- (void)paste:sender {
    NSPasteboard *generalPasteboard = [NSPasteboard generalPasteboard];
    NSData *data = [generalPasteboard dataForType:EmployeesPBoardType];
    if (data == nil) {
        return;
    }

    NSManagedObjectContext *moc = [self managedObjectContext];
    NSMutableSet *departmentEmployees = [[self department] mutableSetValueForKey:@"employees"];
    NSArray *employeesArray = [NSUnarchiver unarchiveObjectWithData:data];

    unsigned i, count = [employeesArray count];
    for (i = 0; i < count; i++) {

        Employee *newEmployee;
        newEmployee = (Employee *)[NSEntityDescription insertNewObjectForEntityForName:@"Employee"
                inManagedObjectContext:moc];
        [newEmployee setValuesForKeysWithDictionary:[employeesArray objectAtIndex:i]];
        [departmentEmployees addObject:newEmployee];
    }
}
```


You should now be able to compile and test the application. You should be able to copy selected employees and paste them into either the same or a different document. You should also notice that undo and redo work appropriately.

In order to cut, you first copy the existing selection, then delete it. To delete the selected employees, you delete them from the managed object context.

1. In the MyDocument class implementation file, implement a `cut:` method. It first calls `copy:`.

```objc
- (void)cut:sender {
    [self copy:sender];

    // implementation continues....
}
```
2. To delete the employees, you need the document’s managed object context. You then need to retrieve the array of selected objects from the employee table controller. For each item in the array of selected employees, delete it from the context:

```
NSManagedObjectContext *moc = [self managedObjectContext];
NSArray *selectedEmployees = [employeeTableController selectedObjects];
unsigned i, count = [selectedEmployees count];

for (i = 0; i < count; i++) {
    Employee *employee;
    employee = (Employee *)[selectedEmployees objectAtIndex:i];
    [moc deleteObject:employee];
}
```

Alternatively, since you have a reference to the employee controller, you could send it a `removeObject:` message for each selected employee. To use this pattern you must ensure that the Deletes Object on Remove option is set for the `contentSet` binding. (Objects are deleted automatically if the array controller’s content is fetched automatically. In this case, however, the `contentSet` is bound to the department’s employees relationship, so unless the Deletes Object on Remove option is set, `removeObject:` removes the object only from the relationship, not from the object graph.)

Note that, since Employee’s department relationship delete rule is set to Nullify, there is no need to remove the employees from the department’s employees relationship—this is performed automatically by the framework.

The complete listing for the `cut:` method is shown in Listing 5-3.

__Listing 5-3__  Complete listing of the `cut:` method

```objc
- (void)cut:sender {
    [self copy:sender];

    NSManagedObjectContext *moc = [self managedObjectContext];

    NSArray *selectedEmployees = [employeeTableController selectedObjects];
    unsigned i, count = [selectedEmployees count];

    for (i = 0; i < count; i++) {
        Employee *employee;
        employee = (Employee *)[selectedEmployees objectAtIndex:i];
        [moc deleteObject:employee];
    }
}
```


You should now be able to compile and test the application. You should be able to cut selected employees from one document and paste them into either the same or a different document. You should also notice that undo and redo work appropriately.

[Next](Localizing%20and%20Customizing%20Model%20Property%20Names%20and%20Error%20Messages.md)[Previous](Adding%20a%20Department%20Object.md)


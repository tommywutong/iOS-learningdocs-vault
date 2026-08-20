---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/CustomClasses.html
archived_at: '2026-07-15T07:48:14.460586Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Frameworks.md)

# Create custom classes

Now that you have the project set up, you're ready to begin writing the application. Start by writing the business logic, that is, the custom classes in Registration. The bulk of the work of Registration is done by its custom classes. Registration's components only manage the user interface.
Registration has two custom classes: RegistrationManager and Person. RegistrationManager maintains the list of registrants and can add new users to that list. Person defines one user in the list of registrants. Its primary purpose is to validate the data that users enter.

## Implement RegistrationManager

- In Project Builder, open Registration's project window.
- Choose File ! New in Project.
- Make sure the Classes suitcase is selected, and then type __RegistrationManager.java__ as the name of the class.
- Deselect the Create header option.
- Click OK.
!- Declare RegistrationManager. Give it a single instance variable, __registrants__, which contains the list of registrants. Write a constructor to initialize the variable and an accessor method for the variable:

```
    import next.util.*;
    import next.wo.*;
    import java.io.*;

    public class RegistrationManager extends Object {
        private protected MutableVector registrants;

        public RegistrationManager() {
            super();
            String path;
            path =
                WebApplication.application().pathForResource("People",
                "array");
            if (path != null) {
                registrants = new MutableVector(new File(path));
            } else {
                registrants = new MutableVector();
            }
        }

        public ImmutableVector registrants() {
            return registrants;
        }

    }
```


The list of registants is stored in a file named __People.array__. The instance variable __registrants__ can be initialized from the file __People.array__ because the file contains data in a property list format. A property list is a compound data type that consists of strings, arrays, dictionaries, and data. Property lists can be represented in an ASCII format, and property list objects such as dictionaries and arrays can consequently be initialized from ASCII files that use this format. The file __People.array__ contains an array of dictionaries (or more explicitly, a MutableVector of ImmutableHashtables).

The constructor accesses the __People.array__ file through the WebApplication method __pathForResource__. __pathForResource__ takes a path and the file's extension as arguments:

```
    path = WebApplication.application().pathForResource("People",
            "array");
```


You can use this method to load different kinds of resources into your application-for example, images, sound files, data files, and so on.

- Write a method that writes the __registrants__ array to the __People.array__ file:

```
    private void writeRegistrantsToFile(String path) {
        FileOutputStream file;
        DataOutputStream stream;
        byte b[];
        String output;

        try {
            file = new FileOutputStream(path);
            stream = new DataOutputStream(file);

            output = registrants.toString();
            b = new byte[output.length()];
            output.getBytes(0, output.length(), b, 0);

            stream.write(b, 0, output.length());
            stream.flush();
            stream.close();
        } catch (java.io.IOException e) {
            WebApplication.application().logString(e.getMessage());
        } finally {
        }
    }
```


When a new person is added to the __registrants__ array, RegistrationManager must update the __People.array__ file. It does so with the __writeRegistrantsToFile__ method. __writeRegistrantsToFile__ sends the __toString__ message to __registrants__, which returns the contents of the array in a property list format.

- Write a method that adds a new person to the __registrants__ array:

```
    public ImmutableHashtable registerPerson(Person newPerson) {
        int i;
        ImmutableHashtable results;
        String currentName;
        String newPersonName = newPerson.name();
        String path =
            WebApplication.application().pathForResource("People",
                "array");

        if (path == null) {
            /* Create People.array if it doesn't exist. */
            path = WebApplication.application().path() +
                File.separator + "People.array";
        }

        results = newPerson.validate();
        if (((String)(results.get("valid"))).compareTo("No") == 0) {
            return results;
        }
        if (registrants.isEmpty() == false) {
            for (i = registrants.size() - 1; i >= 0; i--) {
                currentName = ((String)(((ImmutableHashtable)
                    (registrants.elementAt(i))).get("name")));
                if (currentName.compareTo(newPersonName) == 0) {
                    registrants.removeElementAt(i);
                    break;
                }
            }
        }
        registrants.addElement(newPerson.personAsDictionary());
        writeRegistrantsToFile(path);
        return results;
    }
```


__registerPerson__ is invoked when the user clicks the Register button on the application's Main page. You'll create the Main page later. __registerPerson__ first uses WebApplication's __pathForResource__ to access the __People.array__ file. If the file does not yet exist, it creates the file. Next, it makes sure that the Person object to be added contains valid information. If so, it adds that Person to the __registrants__ array. If the Person is already in the __registrants__ array, it removes that entry so that the list is effectively updated with the new information for that person. Finally, __writeRegistrantsToFile__ is invoked to update the __People.array__ file.

[!Table of Contents](compiled.book.md) [!Next Section](Person.md)
